#!/usr/bin/env python3
"""
compile-newsletter.py — assemble the weekly Daily Encounters newsletter draft.

[REBUILT 2026-04-28 from session knowledge of the cadence/output. Original
 was lost in MC's destructive cleanup.]

Cadence (cron): Sunday 18:00 PT.

Inputs:
  - 7 days of daemon scenes from each elemental channel + aerunik...ferrosid
  - That week's encoded SIML terms (from idea-cta-state.json history +
    encode-processed.jsonl)
  - Point ledger leaderboard top 10
  - Optional intro from ledger/newsletter-intros.json (manual seed pool)

Output:
  newsletters/<monday>-draft.md   (draft, NOT auto-published)

Publishing is deferred to a separate script (publish-newsletter.py) that
Daniel triggers after review. This compiler is read-only against everything
except the draft file.

Usage:
  compile-newsletter.py
  compile-newsletter.py --week 2026-04-20   # specific Monday-anchored week
  compile-newsletter.py --dry-run           # print to stdout, don't write
"""

import argparse
import datetime as dt
import json
import os
import re
import sys
import zoneinfo
from pathlib import Path
import urllib.request

MC_DIR = Path(__file__).resolve().parent.parent
CHANNELS = MC_DIR / "elemental-channels.json"
LEDGER_DIR = MC_DIR / "ledger"
NEWSLETTERS = MC_DIR / "newsletters"
PROCESSED = LEDGER_DIR / "encode-processed.jsonl"
CTA_STATE = LEDGER_DIR / "idea-cta-state.json"
INTROS = LEDGER_DIR / "newsletter-intros.json"
LOG_FILE = MC_DIR / "channel-logs" / "mc-newsletter.log"

PT = zoneinfo.ZoneInfo("America/Los_Angeles")

GLYPH = {
    "aerunik": "∴", "sentaria": "≈", "jvalion": "▲",
    "arboriel": "𐂷", "humavita": "☷", "ferrosid": "⛨",
}
DAY_NAME = {
    "aerunik": "Monday", "sentaria": "Tuesday", "jvalion": "Wednesday",
    "arboriel": "Thursday", "humavita": "Friday", "ferrosid": "Saturday",
}


def log(msg: str) -> None:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"[{dt.datetime.utcnow().isoformat()}Z] {msg}\n")


def _discord_get(url: str, token: str) -> list:
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bot {token}",
        "User-Agent": "NemaSwarmMC-newsletter/1.0",
    })
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _parse_ts(ts: str) -> dt.datetime:
    cleaned = ts.replace("Z", "+00:00")
    return dt.datetime.fromisoformat(cleaned).astimezone(dt.timezone.utc).replace(tzinfo=None)


def _monday_of(d: dt.date) -> dt.date:
    return d - dt.timedelta(days=d.weekday())


def _week_window_utc(monday: dt.date) -> tuple:
    """Mon 00:00 PT → next Mon 00:00 PT, in naive UTC."""
    start_pt = dt.datetime.combine(monday, dt.time(0, 0), tzinfo=PT)
    end_pt = start_pt + dt.timedelta(days=7)
    return (start_pt.astimezone(dt.timezone.utc).replace(tzinfo=None),
            end_pt.astimezone(dt.timezone.utc).replace(tzinfo=None))


def _fetch_scenes(daemon: str, channel_id: str, token: str,
                  start: dt.datetime, end: dt.datetime) -> list:
    """Return bot-authored messages in window, oldest-first."""
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages?limit=100"
    try:
        msgs = _discord_get(url, token)
    except Exception as e:
        log(f"{daemon}: fetch failed: {e}")
        return []
    out = []
    for m in msgs:
        if not m.get("author", {}).get("bot"):
            continue
        ts = _parse_ts(m.get("timestamp", "1970-01-01T00:00:00Z"))
        if start <= ts < end:
            out.append(m)
    out.sort(key=lambda m: m.get("timestamp", ""))
    return out


def _summarize_scene(msg: dict) -> str:
    """Pull the SIML term ref + first paragraph of the embed/body."""
    body = (msg.get("content") or "").strip()
    # term name often appears as: what i've been inside: **<TERM>**
    m = re.search(r"what i'?ve been inside:\s*\*\*([^*]+)\*\*", body)
    term = m.group(1).strip() if m else ""
    # take first paragraph after term ref or first 240 chars otherwise
    first_para = ""
    parts = [p.strip() for p in body.split("\n\n") if p.strip()]
    if parts:
        first_para = parts[0] if not term else next(
            (p for p in parts if "what i'" not in p.lower()), parts[0])
    if len(first_para) > 240:
        first_para = first_para[:237].rsplit(" ", 1)[0] + "…"
    return f"{term} — {first_para}" if term else first_para


def _load_terms_for_week(start: dt.datetime, end: dt.datetime) -> list:
    """Walk encode-processed.jsonl + cta history; collect terms encoded in window."""
    out = []
    seen = set()

    if PROCESSED.exists():
        for line in PROCESSED.read_text().splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            if r.get("status") != "ok":
                continue
            try:
                at = dt.datetime.fromisoformat(r.get("at", "").rstrip("Z"))
            except Exception:
                continue
            if not (start <= at < end):
                continue
            tid = r.get("term_id")
            if tid and tid not in seen:
                seen.add(tid)
                out.append({
                    "term_id": tid,
                    "source": "EncodeIdea",
                    "url": r.get("pushed_url"),
                })

    if CTA_STATE.exists():
        try:
            state = json.loads(CTA_STATE.read_text())
        except json.JSONDecodeError:
            state = {}
        for cta in state.get("history", []):
            res = cta.get("result") or {}
            tid = res.get("term_id")
            if not tid or tid in seen:
                continue
            try:
                closed = dt.datetime.fromisoformat(
                    cta.get("closed_at_utc", "").rstrip("Z"))
            except Exception:
                continue
            if not (start <= closed < end):
                continue
            seen.add(tid)
            out.append({
                "term_id": tid,
                "source": f"the-tally ({res.get('daemon', '?')})",
                "winner": res.get("winner_author"),
                "url": res.get("pushed_url"),
            })
    return out


def _leaderboard_top(n: int = 10) -> list:
    bal_file = LEDGER_DIR / "balances.json"
    if not bal_file.exists():
        return []
    data = json.loads(bal_file.read_text())
    rows = sorted(
        ({"username": u.get("username", ""), "user_id": uid, "total": u["total"]}
         for uid, u in data.get("users", {}).items()),
        key=lambda r: -r["total"],
    )
    return rows[:n]


def _intro_for_week(monday: dt.date) -> str:
    if not INTROS.exists():
        return ""
    try:
        d = json.loads(INTROS.read_text())
    except json.JSONDecodeError:
        return ""
    pool = d.get("pool", [])
    if not pool:
        return ""
    return pool[monday.toordinal() % len(pool)]


def _render(monday: dt.date, scenes_by_daemon: dict, terms: list,
            leaders: list, intro: str) -> str:
    sun = monday + dt.timedelta(days=6)
    title = f"# Daily Encounters — week of {monday.isoformat()} → {sun.isoformat()}"

    parts = [title, ""]
    if intro:
        parts += [intro, ""]
    parts += [
        "*howdy. another week of daemons stepping into scenes. here's the trail.*",
        "",
        "## the week's encounters",
        "",
    ]
    for daemon in ("aerunik", "sentaria", "jvalion", "arboriel", "humavita", "ferrosid"):
        scenes = scenes_by_daemon.get(daemon, [])
        glyph = GLYPH.get(daemon, "?")
        day = DAY_NAME.get(daemon, "")
        parts.append(f"### {glyph} {daemon.capitalize()} — {day}")
        if not scenes:
            parts.append("*no scene this week.*")
        else:
            for s in scenes:
                parts.append(f"- {s}")
        parts.append("")

    parts += ["## new SIML terms encoded", ""]
    if not terms:
        parts.append("*no encodings closed this week.*")
    else:
        for t in terms:
            line = f"- **{t['term_id']}** — via {t['source']}"
            if t.get("winner"):
                line += f" (winner: @{t['winner']})"
            if t.get("url"):
                line += f" → {t['url']}"
            parts.append(line)
    parts.append("")

    parts += ["## point ledger — top of the leaderboard", ""]
    if not leaders:
        parts.append("*ledger is empty.*")
    else:
        for i, row in enumerate(leaders, 1):
            uname = row["username"] or row["user_id"][:8]
            parts.append(f"{i}. @{uname} — {row['total']} pts")
    parts.append("")
    parts += [
        "---",
        "",
        "*see y'all in the next round. drop ideas in #the-tally; encode anything in #EncodeIdea.*",
        "— mc",
    ]
    return "\n".join(parts) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--week", default=None,
                    help="Monday date (YYYY-MM-DD) anchoring the week to compile")
    ap.add_argument("--dry-run", action="store_true", help="print, don't write")
    args = ap.parse_args()

    mc_token = os.environ.get("DISCORD_MC_TOKEN", "").strip()
    if not mc_token:
        print(json.dumps({"ok": False, "error": "DISCORD_MC_TOKEN missing"}))
        return 1

    cfg = json.loads(CHANNELS.read_text())
    elementals = cfg.get("channels", {})

    if args.week:
        monday = dt.date.fromisoformat(args.week)
        if monday.weekday() != 0:
            monday = _monday_of(monday)
    else:
        monday = _monday_of(dt.date.today())

    start, end = _week_window_utc(monday)
    log(f"compiling for week {monday}; window UTC {start} → {end}")

    scenes_by_daemon = {}
    for daemon, info in elementals.items():
        scenes = _fetch_scenes(daemon, info["channel_id"], mc_token, start, end)
        scenes_by_daemon[daemon] = [_summarize_scene(s) for s in scenes if _summarize_scene(s)]

    terms = _load_terms_for_week(start, end)
    leaders = _leaderboard_top(10)
    intro = _intro_for_week(monday)

    body = _render(monday, scenes_by_daemon, terms, leaders, intro)

    if args.dry_run:
        print(body)
        return 0

    NEWSLETTERS.mkdir(parents=True, exist_ok=True)
    out_path = NEWSLETTERS / f"{monday.isoformat()}-draft.md"
    out_path.write_text(body)
    log(f"draft written: {out_path}")
    print(json.dumps({"ok": True, "path": str(out_path),
                       "scenes": sum(len(v) for v in scenes_by_daemon.values()),
                       "terms": len(terms),
                       "leaders": len(leaders)}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
