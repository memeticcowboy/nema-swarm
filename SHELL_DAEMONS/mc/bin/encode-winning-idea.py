#!/usr/bin/env python3
"""
encode-winning-idea.py — close any due CTA windows, encode the winner, publish.

[REBUILT 2026-04-28 from session knowledge of the flow. Original was lost
 in MC's destructive cleanup.]

Flow (per due CTA):
  1. Read ledger/idea-cta-state.json — find any "active" CTAs whose
     close_at_utc has passed
  2. Fetch replies to the CTA message in #the-tally (where the CTA was posted)
  3. Tally 👍 (or ❤️/🔥/etc.) reactions per reply
  4. Pick winner: highest votes; tiebreak by earliest timestamp
  5. Encode the winning idea via bin/encode-to-siml.py → simlab pipeline
  6. Push the new term to nema-swarm via bin/nema_swarm_git.py push-term
  7. Post summary to #EncodeIdea with attribution + Φ-formula + URL
  8. Mark state closed; move to history

Idempotent: re-running won't double-process. Tracks encode_attempts; gives up
after MAX_ATTEMPTS to prevent re-spam loops.

Usage:
  encode-winning-idea.py                # process all due CTAs
  encode-winning-idea.py --key 2026-04-27-aerunik  # one CTA only
  encode-winning-idea.py --dry-run      # show what would happen
"""

import argparse
import datetime as dt
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional
import urllib.request
import urllib.error

MC_DIR = Path(__file__).resolve().parent.parent
CHANNELS = MC_DIR / "elemental-channels.json"
STATE_FILE = MC_DIR / "ledger" / "idea-cta-state.json"
LOG_FILE = MC_DIR / "channel-logs" / "mc-encode-winner.log"

ENCODE_TO_SIML = MC_DIR / "bin" / "encode-to-siml.py"
NEMA_SWARM_GIT = MC_DIR / "bin" / "nema_swarm_git.py"

MAX_ATTEMPTS = 3
GLYPH = {
    "aerunik": "∴", "sentaria": "≈", "jvalion": "▲",
    "arboriel": "𐂷", "humavita": "☷", "ferrosid": "⛨",
}


def log(msg: str) -> None:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"[{dt.datetime.utcnow().isoformat()}Z] {msg}\n")


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"active": {}, "history": []}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2))


def _discord_get(url: str, token: str) -> dict:
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bot {token}",
        "User-Agent": "NemaSwarmMC-encode-winner/1.0",
    })
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _discord_post(channel_id: str, content: str, token: str) -> dict:
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    req = urllib.request.Request(url, data=json.dumps({"content": content}).encode("utf-8"),
                                  headers={"Authorization": f"Bot {token}",
                                           "Content-Type": "application/json",
                                           "User-Agent": "NemaSwarmMC-encode-winner/1.0"},
                                  method="POST")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return {"ok": True, "body": json.loads(resp.read().decode("utf-8"))}
    except urllib.error.HTTPError as e:
        return {"ok": False, "status": e.code, "body": e.read().decode("utf-8")[:300]}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def _fetch_replies(channel_id: str, after_id: str, token: str) -> list:
    """Fetch messages posted AFTER the CTA message in the same channel."""
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages?limit=100&after={after_id}"
    return _discord_get(url, token)


def _tally_votes(msg: dict) -> int:
    """Sum reaction counts on a message. 👍 weighted highest; other reactions count too."""
    total = 0
    for r in msg.get("reactions", []):
        emoji = r.get("emoji", {}).get("name", "")
        count = r.get("count", 0)
        if emoji in ("👍", "🔥", "❤️", "✅", "🌿"):
            total += count
    return total


def _run_encoder(idea_text: str, daemon: str) -> dict:
    """Call encode-to-siml.py with the idea as source-text. Returns parsed JSON or error."""
    args = [
        "/usr/bin/python3", str(ENCODE_TO_SIML),
        "--source-text", idea_text,
        "--series", "C",  # legacy default; auto-classify lands in May 1 PR
        "--name-hint", daemon.capitalize() + "_idea",
    ]
    try:
        proc = subprocess.run(args, capture_output=True, text=True, timeout=600)
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "encoder timed out (>600s)"}
    if proc.returncode != 0:
        log(f"encoder rc={proc.returncode} stderr={proc.stderr.strip()[:300]}")
        return {"ok": False, "error": f"encoder rc={proc.returncode}", "stderr": proc.stderr[:500]}
    # encoder prints final JSON on stdout
    try:
        return json.loads(proc.stdout.strip().split("\n")[-1])
    except Exception:
        # Try to find last {...} block
        import re
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
        return {"ok": False, "error": "push timeout (>120s)"}
    if proc.returncode != 0:
        log(f"push rc={proc.returncode} stderr={proc.stderr.strip()[:300]}")
        return {"ok": False, "error": f"push rc={proc.returncode}"}
    try:
        return json.loads(proc.stdout.strip())
    except Exception:
        return {"ok": False, "error": "push output not JSON"}


def process_due_cta(key: str, cta: dict, mc_token: str, encode_channel_id: str,
                    dry_run: bool = False) -> dict:
    """Process one due CTA. Returns result dict; updates cta in place."""
    daemon = cta["daemon"]
    daemon_day = cta["daemon_day"]
    cta_msg_id = cta["cta_message_id"]
    channel_id = cta["channel_id"]

    log(f"processing {key}: daemon={daemon} daemon_day={daemon_day} attempt={cta.get('encode_attempts', 0) + 1}")

    if dry_run:
        return {"ok": True, "dry_run": True, "key": key}

    # Fetch replies
    try:
        replies = _fetch_replies(channel_id, cta_msg_id, mc_token)
    except Exception as e:
        log(f"{key}: fetch replies failed: {e}")
        return {"ok": False, "error": f"fetch replies: {e}"}

    if not replies:
        log(f"{key}: no replies during voting window — falling back to no-replies close")
        cta["status"] = "closed_no_replies"
        cta["closed_at_utc"] = dt.datetime.utcnow().isoformat() + "Z"
        cta["result"] = {"reason": "no member replies during voting window"}
        return {"ok": True, "status": "no_replies"}

    # Pick winner
    scored = sorted(replies, key=lambda m: (-_tally_votes(m), m.get("timestamp", "")))
    winner = scored[0]
    winner_text = (winner.get("content") or "").strip()
    winner_author = winner.get("author", {}).get("username", "anonymous")
    winner_votes = _tally_votes(winner)
    log(f"{key}: winner @{winner_author} ({winner_votes} votes): {winner_text[:120]}")

    if not winner_text:
        cta["status"] = "closed_empty_winner"
        cta["closed_at_utc"] = dt.datetime.utcnow().isoformat() + "Z"
        return {"ok": True, "status": "empty_winner"}

    # Encode
    cta["encode_attempts"] = cta.get("encode_attempts", 0) + 1
    log(f"{key}: encoding winner via simlab (attempt {cta['encode_attempts']})")
    enc = _run_encoder(winner_text, daemon)
    if not enc.get("ok"):
        log(f"{key}: encode failed: {enc.get('error', 'unknown')}")
        if cta["encode_attempts"] >= MAX_ATTEMPTS:
            cta["status"] = "closed_encode_failed"
            cta["closed_at_utc"] = dt.datetime.utcnow().isoformat() + "Z"
            cta["result"] = {"error": "max_attempts_exceeded", "encode_attempts": cta["encode_attempts"]}
        return {"ok": False, "error": enc.get("error"), "encode_attempts": cta["encode_attempts"]}

    term_id = enc.get("term_id", "?")
    term_dir = enc.get("term_dir", "")
    term_dir_name = Path(term_dir).name if term_dir else ""
    nemetic = enc.get("nemetic_string", "")

    # Push
    pushed = _push_to_repo(term_dir_name) if term_dir_name else {"ok": False}
    pushed_url = pushed.get("url") if pushed.get("ok") else None

    # Post summary to #EncodeIdea
    g = GLYPH.get(daemon, "?")
    summary = (
        f"new SIML term encoded from @{winner_author}'s idea:\n\n"
        f"**{term_id}** — `{nemetic}`\n\n"
        f"pinned as {daemon.capitalize()}'s scene for {daemon_day}. "
        + (f"📦 published → {pushed_url}" if pushed_url else "(vault only — repo push deferred)")
        + "\n\nwant your own concept encoded? drop a URL/PDF/text here and i'll run it."
    )
    _discord_post(encode_channel_id, summary, mc_token)

    cta["status"] = "closed"
    cta["closed_at_utc"] = dt.datetime.utcnow().isoformat() + "Z"
    cta["result"] = {
        "daemon": daemon,
        "daemon_day": daemon_day,
        "winner_author": winner_author,
        "winner_votes": winner_votes,
        "term_id": term_id,
        "term_dir_name": term_dir_name,
        "pushed": pushed.get("ok", False),
        "pushed_url": pushed_url,
        "key": key,
    }
    return {"ok": True, "key": key, "term_id": term_id, "pushed_url": pushed_url}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--key", default=None, help="process only this CTA key")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    mc_token = os.environ.get("DISCORD_MC_TOKEN", "").strip()
    if not mc_token:
        print(json.dumps({"ok": False, "error": "DISCORD_MC_TOKEN missing"}))
        return 1

    cfg = json.loads(CHANNELS.read_text())
    encode_channel_id = cfg.get("mc_channels", {}).get("encode", {}).get("channel_id", "")

    state = load_state()
    now = dt.datetime.utcnow().replace(tzinfo=None)
    results = []

    keys_to_process = [args.key] if args.key else list(state.get("active", {}).keys())
    for key in keys_to_process:
        cta = state.get("active", {}).get(key)
        if not cta:
            results.append({"key": key, "ok": False, "error": "not in active"})
            continue
        if cta.get("status") != "open":
            continue
        close_at = dt.datetime.fromisoformat(cta["close_at_utc"].rstrip("Z"))
        if close_at > now and not args.key:
            continue  # not yet due; skip silently
        r = process_due_cta(key, cta, mc_token, encode_channel_id, dry_run=args.dry_run)
        results.append(r)
        # Move closed CTAs to history
        if cta.get("status", "open") != "open":
            state.setdefault("history", []).append({**cta, "key": key})
            state["active"].pop(key, None)

    if not args.dry_run:
        save_state(state)

    print(json.dumps({"ok": True, "processed": len(results), "results": results}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
