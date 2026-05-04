#!/usr/bin/env python3
"""
poll-encode-channel.py — watch #EncodeIdea for @MC encode requests.

[REBUILT 2026-04-28 from session knowledge of the trigger pattern. Original
 was lost in MC's destructive cleanup.]

Flow per poll:
  1. Fetch latest N messages from #EncodeIdea
  2. Skip already-processed (tracked in ledger/encode-processed.jsonl)
  3. Skip messages older than MAX_AGE_MIN (don't backfill)
  4. Match @MC mention + an encode trigger word ("encode", "siml", "term")
  5. Extract source: URL > attachment > raw text body
  6. Call bin/encode-to-siml.py → simlab pipeline
  7. Push the new term to nema-swarm via nema_swarm_git.py push-term
  8. Reply in-channel with term_id + nemetic_string + repo url
  9. Append to processed jsonl (idempotent)

Idempotent: re-running won't double-process. Per-message attempt cap so a
broken source doesn't trigger an infinite spam loop.

Usage:
  poll-encode-channel.py                # one poll cycle (intended for cron)
  poll-encode-channel.py --message-id ID  # process one specific message
  poll-encode-channel.py --dry-run      # print what would happen
"""

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path
import urllib.request
import urllib.error

MC_DIR = Path(__file__).resolve().parent.parent
CHANNELS = MC_DIR / "elemental-channels.json"
STATE_DIR = MC_DIR / "ledger"
PROCESSED = STATE_DIR / "encode-processed.jsonl"
POLL_STATE = STATE_DIR / "encode-poll-state.json"
LOG_FILE = MC_DIR / "channel-logs" / "mc-encode-poll.log"

ENCODE_TO_SIML = MC_DIR / "bin" / "encode-to-siml.py"
NEMA_SWARM_GIT = MC_DIR / "bin" / "nema_swarm_git.py"

FETCH_LIMIT = 30
MAX_AGE_MIN = 60          # ignore anything older than this on first sight
MAX_ATTEMPTS = 2          # per-message
URL_RE = re.compile(r"https?://[^\s<>\"']+")


def log(msg: str) -> None:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"[{dt.datetime.utcnow().isoformat()}Z] {msg}\n")


def _discord_get(url: str, token: str) -> list:
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bot {token}",
        "User-Agent": "NemaSwarmMC-encode-poll/1.0",
    })
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _discord_post(channel_id: str, content: str, token: str,
                  reference_message_id: str = "") -> dict:
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    payload = {"content": content}
    if reference_message_id:
        payload["message_reference"] = {"message_id": reference_message_id,
                                         "fail_if_not_exists": False}
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"),
                                  headers={"Authorization": f"Bot {token}",
                                           "Content-Type": "application/json",
                                           "User-Agent": "NemaSwarmMC-encode-poll/1.0"},
                                  method="POST")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return {"ok": True, "body": json.loads(resp.read().decode("utf-8"))}
    except urllib.error.HTTPError as e:
        return {"ok": False, "status": e.code, "body": e.read().decode("utf-8")[:300]}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def _load_processed() -> dict:
    """Return {message_id: {attempts, last_status, ...}}."""
    out = {}
    if not PROCESSED.exists():
        return out
    for line in PROCESSED.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except json.JSONDecodeError:
            continue
        mid = r.get("message_id")
        if mid:
            out[mid] = r
    return out


def _append_processed(rec: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    with open(PROCESSED, "a") as f:
        f.write(json.dumps(rec) + "\n")


def _is_mc_addressed(msg: dict, mc_user_id: str) -> bool:
    """True iff @MC appears in mentions AND near the start of the message body.
    A mid-sentence @MC reference (e.g., "@MC's encoder timed out") is incidental,
    not an encode request."""
    if not mc_user_id:
        return False
    if not any(u.get("id") == mc_user_id for u in msg.get("mentions", [])):
        return False
    content = msg.get("content") or ""
    # First mention token must appear in the first 50 chars
    m = re.search(r"<@!?(\d+)>", content[:50])
    return bool(m and m.group(1) == mc_user_id)


def _extract_source(msg: dict) -> dict:
    """Return {kind: url|file|text, value: ...} or empty."""
    content = (msg.get("content") or "").strip()
    # 1. URL in text
    urls = URL_RE.findall(content)
    if urls:
        return {"kind": "url", "value": urls[0]}
    # 2. Attachment
    for att in msg.get("attachments", []):
        url = att.get("url") or att.get("proxy_url")
        if url:
            return {"kind": "url", "value": url, "filename": att.get("filename", "")}
    # 3. Plain text body (strip the @mention + leading verb)
    stripped = re.sub(r"<@!?\d+>", "", content).strip()
    for w in ("encode this", "encode:", "encode", "siml this", "siml:", "siml"):
        if stripped.lower().startswith(w):
            stripped = stripped[len(w):].lstrip(":,.- ").strip()
            break
    if len(stripped) >= 40:
        return {"kind": "text", "value": stripped}
    return {}


def _run_encoder(source: dict) -> dict:
    args = ["/usr/bin/python3", str(ENCODE_TO_SIML)]
    if source["kind"] == "url":
        args += ["--source-url", source["value"]]
    elif source["kind"] == "text":
        args += ["--source-text", source["value"]]
    else:
        return {"ok": False, "error": f"unsupported source kind: {source['kind']}"}
    args += ["--series", "auto"]  # element-first classifier (May 1 PR merged)
    try:
        proc = subprocess.run(args, capture_output=True, text=True, timeout=600)
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "encoder timed out (>600s)"}
    if proc.returncode != 0:
        log(f"encoder rc={proc.returncode} stderr={proc.stderr.strip()[:300]}")
        return {"ok": False, "error": f"encoder rc={proc.returncode}",
                "stderr": proc.stderr[:500]}
    try:
        return json.loads(proc.stdout.strip().split("\n")[-1])
    except Exception:
        for chunk in reversed(re.findall(r"\{[\s\S]*?\}", proc.stdout[-4000:])):
            try:
                d = json.loads(chunk)
                if "term_id" in d or "ok" in d:
                    return d
            except json.JSONDecodeError:
                continue
        return {"ok": False, "error": "encoder output not JSON-parseable",
                "stdout_tail": proc.stdout[-500:]}


def _push_to_repo(term_dir_name: str) -> dict:
    args = ["/usr/bin/python3", str(NEMA_SWARM_GIT), "push-term", term_dir_name]
    try:
        proc = subprocess.run(args, capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "push timeout"}
    if proc.returncode != 0:
        log(f"push rc={proc.returncode} stderr={proc.stderr.strip()[:300]}")
        return {"ok": False, "error": f"push rc={proc.returncode}"}
    try:
        return json.loads(proc.stdout.strip())
    except Exception:
        return {"ok": False, "error": "push output not JSON"}


def _msg_age_min(msg: dict) -> float:
    ts = msg.get("timestamp", "")
    if not ts:
        return 0.0
    try:
        # Discord ISO timestamps include tz; normalize to naive UTC
        cleaned = ts.replace("Z", "+00:00")
        when = dt.datetime.fromisoformat(cleaned).astimezone(dt.timezone.utc).replace(tzinfo=None)
    except Exception:
        return 0.0
    return (dt.datetime.utcnow() - when).total_seconds() / 60.0


def process_message(msg: dict, mc_token: str, encode_channel_id: str,
                    processed: dict, dry_run: bool = False) -> dict:
    mid = msg["id"]
    author = msg.get("author", {}).get("username", "anonymous")
    text_preview = (msg.get("content") or "")[:120]
    log(f"considering {mid} from @{author}: {text_preview}")

    src = _extract_source(msg)
    if not src:
        log(f"{mid}: no usable source — skipping")
        rec = {"message_id": mid, "status": "skipped_no_source",
               "at": dt.datetime.utcnow().isoformat() + "Z"}
        if not dry_run:
            _append_processed(rec)
        return rec

    prev = processed.get(mid)
    attempts = (prev or {}).get("attempts", 0)
    if attempts >= MAX_ATTEMPTS:
        log(f"{mid}: max attempts ({attempts}) reached — skipping")
        return {"message_id": mid, "status": "max_attempts", "attempts": attempts}

    if dry_run:
        return {"message_id": mid, "status": "would_encode", "source": src}

    enc = _run_encoder(src)
    attempts += 1
    if not enc.get("ok"):
        rec = {"message_id": mid, "status": "encode_failed", "attempts": attempts,
               "error": enc.get("error"), "at": dt.datetime.utcnow().isoformat() + "Z"}
        _append_processed(rec)
        # one-time notice to channel on first failure
        if attempts == 1:
            _discord_post(encode_channel_id,
                          f"hit a snag encoding that one — `{enc.get('error', 'unknown')[:120]}`. give me a moment to try again.",
                          mc_token, reference_message_id=mid)
        return rec

    term_id = enc.get("term_id", "?")
    term_dir = enc.get("term_dir", "")
    term_dir_name = Path(term_dir).name if term_dir else ""
    nemetic = enc.get("nemetic_string", "")

    pushed = _push_to_repo(term_dir_name) if term_dir_name else {"ok": False}
    pushed_url = pushed.get("url") if pushed.get("ok") else None

    summary = (
        f"encoded → **{term_id}**\n"
        f"`{nemetic}`\n"
        + (f"📦 {pushed_url}" if pushed_url else "(vault only — repo push deferred)")
    )
    _discord_post(encode_channel_id, summary, mc_token, reference_message_id=mid)

    rec = {"message_id": mid, "status": "ok", "attempts": attempts,
           "term_id": term_id, "term_dir_name": term_dir_name,
           "pushed": pushed.get("ok", False), "pushed_url": pushed_url,
           "at": dt.datetime.utcnow().isoformat() + "Z"}
    _append_processed(rec)
    return rec


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--message-id", default=None,
                    help="process this specific message (ignores age cutoff)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    mc_token = os.environ.get("DISCORD_MC_TOKEN", "").strip()
    if not mc_token:
        print(json.dumps({"ok": False, "error": "DISCORD_MC_TOKEN missing"}))
        return 1
    mc_user_id = os.environ.get("DISCORD_MC_USER_ID", "").strip()
    if not mc_user_id:
        print(json.dumps({"ok": False, "error": "DISCORD_MC_USER_ID missing"}))
        return 1

    cfg = json.loads(CHANNELS.read_text())
    encode_channel_id = cfg.get("mc_channels", {}).get("encode", {}).get("channel_id", "")
    if not encode_channel_id:
        print(json.dumps({"ok": False, "error": "encode channel id missing"}))
        return 1

    processed = _load_processed()

    if args.message_id:
        url = f"https://discord.com/api/v10/channels/{encode_channel_id}/messages/{args.message_id}"
        try:
            msg = _discord_get(url, mc_token)
        except Exception as e:
            print(json.dumps({"ok": False, "error": f"fetch one: {e}"}))
            return 1
        r = process_message(msg, mc_token, encode_channel_id, processed, dry_run=args.dry_run)
        print(json.dumps({"ok": True, "result": r}, indent=2))
        return 0

    url = f"https://discord.com/api/v10/channels/{encode_channel_id}/messages?limit={FETCH_LIMIT}"
    try:
        msgs = _discord_get(url, mc_token)
    except Exception as e:
        log(f"fetch failed: {e}")
        print(json.dumps({"ok": False, "error": f"fetch: {e}"}))
        return 1

    results = []
    for msg in msgs:
        if msg.get("author", {}).get("bot"):
            continue
        if msg["id"] in processed and processed[msg["id"]].get("status") == "ok":
            continue
        if not _is_mc_addressed(msg, mc_user_id):
            continue
        if _msg_age_min(msg) > MAX_AGE_MIN and msg["id"] not in processed:
            log(f"{msg['id']}: too old on first sight (>{MAX_AGE_MIN}m) — skipping")
            continue
        r = process_message(msg, mc_token, encode_channel_id, processed,
                            dry_run=args.dry_run)
        results.append(r)

    if not args.dry_run:
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        POLL_STATE.write_text(json.dumps({
            "last_poll_utc": dt.datetime.utcnow().isoformat() + "Z",
            "fetched": len(msgs),
            "processed": len(results),
        }, indent=2))

    print(json.dumps({"ok": True, "processed": len(results), "results": results}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
