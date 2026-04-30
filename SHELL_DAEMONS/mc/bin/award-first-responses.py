#!/usr/bin/env python3
"""
award-first-responses.py — award 1 pt to first non-bot replier in each
elemental channel per day.

[REBUILT 2026-04-28 from ECONOMY rules. Original was lost in MC's destructive
 cleanup.]

Rule: daily_elemental_prompt_response_first
  - 1 pt per user per channel per day
  - Goes to the EARLIEST non-bot reply in each elemental channel after the
    daemon's daily scene was posted (09:00 PT)
  - Does not stack with weekly cap exceptions; ledger handles dedup + cap

Flow:
  1. For each elemental channel in elemental-channels.json:
     a. Fetch latest 50 messages
     b. Find that day's daemon scene post (any bot post by that elemental's
        bot account, posted today after 09:00 PT)
     c. Find the first NON-BOT reply after that scene
     d. Call ledger.py award <user_id> 1 daily_elemental_prompt_response_first
        with --scope-extra <channel_id>
  2. ledger.py dedups by day-channel scope, so re-running is safe.

Usage:
  award-first-responses.py                # process all 6 elemental channels
  award-first-responses.py --channel aerunik
  award-first-responses.py --dry-run
"""

import argparse
import datetime as dt
import json
import os
import subprocess
import sys
import zoneinfo
from pathlib import Path
import urllib.request

MC_DIR = Path(__file__).resolve().parent.parent
CHANNELS = MC_DIR / "elemental-channels.json"
LEDGER = MC_DIR / "bin" / "ledger.py"
LOG_FILE = MC_DIR / "channel-logs" / "mc-award-first.log"

PT = zoneinfo.ZoneInfo("America/Los_Angeles")
SCENE_HOUR_PT = 9   # daemon scenes post at 09:00 PT


def log(msg: str) -> None:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"[{dt.datetime.utcnow().isoformat()}Z] {msg}\n")


def _discord_get(url: str, token: str) -> list:
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bot {token}",
        "User-Agent": "NemaSwarmMC-award-first/1.0",
    })
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _parse_ts(ts: str) -> dt.datetime:
    """Discord ISO → naive UTC datetime."""
    cleaned = ts.replace("Z", "+00:00")
    return dt.datetime.fromisoformat(cleaned).astimezone(dt.timezone.utc).replace(tzinfo=None)


def _today_scene_window_utc() -> tuple:
    """(start_utc, end_utc) for today's 09:00 PT → 08:59 PT-tomorrow window."""
    now_pt = dt.datetime.now(tz=PT)
    scene_start_pt = now_pt.replace(hour=SCENE_HOUR_PT, minute=0, second=0, microsecond=0)
    if now_pt < scene_start_pt:
        # before today's scene posted → look at yesterday's
        scene_start_pt = scene_start_pt - dt.timedelta(days=1)
    scene_end_pt = scene_start_pt + dt.timedelta(days=1)
    return (
        scene_start_pt.astimezone(dt.timezone.utc).replace(tzinfo=None),
        scene_end_pt.astimezone(dt.timezone.utc).replace(tzinfo=None),
    )


def _award(user_id: str, username: str, channel_id: str, by: str = "system",
           dry_run: bool = False) -> dict:
    if dry_run:
        return {"ok": True, "dry_run": True, "user_id": user_id}
    args = [
        "/usr/bin/python3", str(LEDGER), "award",
        user_id, "1", "daily_elemental_prompt_response_first",
        "--by", by,
        "--reason", f"first reply in elemental channel {channel_id}",
        "--username", username,
        "--scope-extra", channel_id,
    ]
    proc = subprocess.run(args, capture_output=True, text=True, timeout=30)
    try:
        return json.loads(proc.stdout.strip())
    except Exception:
        return {"ok": False, "error": "ledger output not JSON",
                "stdout": proc.stdout[:300], "stderr": proc.stderr[:300]}


def process_channel(daemon: str, channel_id: str, mc_token: str,
                    dry_run: bool = False) -> dict:
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages?limit=50"
    try:
        msgs = _discord_get(url, mc_token)
    except Exception as e:
        log(f"{daemon}: fetch failed: {e}")
        return {"ok": False, "channel": daemon, "error": f"fetch: {e}"}

    win_start, win_end = _today_scene_window_utc()

    # messages come newest-first; reverse for chronological order
    chronological = list(reversed(msgs))

    # find scene post (any bot message inside the window)
    scene_msg = None
    for m in chronological:
        ts = _parse_ts(m.get("timestamp", "1970-01-01T00:00:00Z"))
        if ts < win_start or ts >= win_end:
            continue
        if m.get("author", {}).get("bot"):
            scene_msg = m
            break
    if not scene_msg:
        log(f"{daemon}: no scene post found in today's window")
        return {"ok": True, "channel": daemon, "status": "no_scene_yet"}

    scene_ts = _parse_ts(scene_msg["timestamp"])
    # find first non-bot reply after scene
    first = None
    for m in chronological:
        ts = _parse_ts(m.get("timestamp", "1970-01-01T00:00:00Z"))
        if ts <= scene_ts:
            continue
        if m.get("author", {}).get("bot"):
            continue
        first = m
        break

    if not first:
        log(f"{daemon}: no non-bot reply yet after scene {scene_msg['id']}")
        return {"ok": True, "channel": daemon, "status": "no_replies_yet"}

    user_id = first["author"]["id"]
    username = first["author"].get("username", "")
    log(f"{daemon}: first reply by @{username} ({user_id}) at {first['timestamp']}")

    r = _award(user_id, username, channel_id, dry_run=dry_run)
    return {"ok": r.get("ok", False), "channel": daemon,
            "user_id": user_id, "username": username,
            "scene_message_id": scene_msg["id"], "first_reply_message_id": first["id"],
            "ledger": r}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", default=None,
                    help="process only this elemental (e.g., aerunik)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    mc_token = os.environ.get("DISCORD_MC_TOKEN", "").strip()
    if not mc_token:
        print(json.dumps({"ok": False, "error": "DISCORD_MC_TOKEN missing"}))
        return 1

    cfg = json.loads(CHANNELS.read_text())
    elementals = cfg.get("channels", {})

    if args.channel:
        if args.channel not in elementals:
            print(json.dumps({"ok": False, "error": f"unknown channel: {args.channel}"}))
            return 1
        results = [process_channel(args.channel, elementals[args.channel]["channel_id"],
                                    mc_token, dry_run=args.dry_run)]
    else:
        results = []
        for daemon, info in elementals.items():
            results.append(process_channel(daemon, info["channel_id"], mc_token,
                                            dry_run=args.dry_run))

    print(json.dumps({"ok": True, "processed": len(results), "results": results}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
