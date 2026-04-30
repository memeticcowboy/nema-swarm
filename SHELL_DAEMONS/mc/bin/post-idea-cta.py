#!/usr/bin/env python3
"""
post-idea-cta.py — MC posts a "drop your ideas" CTA in #the-tally, plus a varying
heads-up announcement in #member-chat that points members to the tally.

[REBUILT 2026-04-28 from patches doc + base structure read during the
 simlab Phase 3 work. Original was lost in MC's destructive cleanup.]

By default, targets TOMORROW's daemon (day-before pattern). Members reply in
#the-tally with ideas; each reply gets 👍 votes over a 6-hour window
(12:00→18:00 UTC by default, or override with --close-in). After the window
closes, encode-winning-idea.py reads `cta["channel_id"]` (the tally) to fetch
replies, picks the winner, encodes it via simlab, pushes to the Nema-Swarm
repo, posts the summary to #EncodeIdea, and pins the term to the daemon's
priority queue.

The #member-chat announcement rotates through a small template set (one per
ordinal day) so the daily heads-up isn't a copy-paste.

State: ledger/idea-cta-state.json
  {
    "active": {
      "<YYYY-MM-DD>-<daemon>": {
        "daemon": "arboriel",
        "daemon_day": "2026-04-23",
        "cta_message_id": "...",          # the CTA in #the-tally (vote source)
        "channel_id": "1498180873151971479",  # #the-tally
        "announcement_message_id": "...",     # the heads-up in #member-chat
        "announcement_channel_id": "1486067576218845366",  # #member-chat
        "open_at_utc": "...",
        "close_at_utc": "...",
        "status": "open"
      }
    }
  }

Usage:
  post-idea-cta.py                    # fire for tomorrow's daemon, default window
  post-idea-cta.py --daemon arboriel  # override daemon
  post-idea-cta.py --for-day 2026-04-24 --daemon humavita
  post-idea-cta.py --close-in 6       # voting closes in 6 hours (default 6)
  post-idea-cta.py --no-announce      # skip the #member-chat heads-up
  post-idea-cta.py --dry-run          # show what would post, don't send
"""

import argparse
import datetime as dt
import json
import os
import sys
from pathlib import Path
from typing import Optional
import urllib.request
import urllib.error

MC_DIR = Path(__file__).resolve().parent.parent
CHANNELS = MC_DIR / "elemental-channels.json"
STATE_FILE = MC_DIR / "ledger" / "idea-cta-state.json"

DAY_TO_DAEMON = {
    "monday": "aerunik", "tuesday": "sentaria", "wednesday": "jvalion",
    "thursday": "arboriel", "friday": "humavita", "saturday": "ferrosid",
    "sunday": None,
}

GLYPH = {
    "aerunik": "∴", "sentaria": "≈", "jvalion": "▲",
    "arboriel": "𐂷", "humavita": "☷", "ferrosid": "⛨",
}

ELEMENT = {
    "aerunik": "Air / σ — distinction, cut, signal-from-noise",
    "sentaria": "Water / ρ — resonance, what is felt but unnamed",
    "jvalion": "Fire / λ — direction, commitment, where is this going",
    "arboriel": "Wood / β — branching, possibility, what else could this be",
    "humavita": "Earth / δγ — composting, what must be released",
    "ferrosid": "Metal / μ — structure, boundary, what holds this together",
}

ELEMENT_SHORT = {
    "aerunik": "Air / σ",  "sentaria": "Water / ρ", "jvalion": "Fire / λ",
    "arboriel": "Wood / β", "humavita": "Earth / δγ", "ferrosid": "Metal / μ",
}

# Rotated by daemon_day.toordinal() % len(ANNOUNCEMENT_TEMPLATES) so each day
# gets a deterministically-different opener. Keep templates short, in MC voice,
# always linking to the tally and naming the close window.
ANNOUNCEMENT_TEMPLATES = [
    "🤠 the bell's been rung. **{glyph} {daemon_cap}** rides tomorrow. drop your concepts in <#{tally_id}> — door closes around **{close_local_pt}**.",
    "tomorrow's daemon: **{glyph} {daemon_cap}** ({elem_short}). what should they sit inside? add ideas to <#{tally_id}>; voting window ~6h, closes **{close_local_pt}**.",
    "saddle up — **{glyph} {daemon_cap}** is on deck. <#{tally_id}> is open: one idea per reply, react 👍 to vote. tally closes **{close_local_pt}**.",
    "**{glyph} {daemon_cap}** wants something to chew on tomorrow. drop concepts/questions/half-thoughts in <#{tally_id}>. winner gets encoded into a SIML term. close: **{close_local_pt}**.",
    "the herd picks **{glyph} {daemon_cap}**'s scene. <#{tally_id}> is where it happens. 6 hours on the clock, closing **{close_local_pt}**. make it count.",
    "ideas wanted: **{glyph} {daemon_cap}** ({elem_short}) is up tomorrow. <#{tally_id}> — the herd decides what they meet. votes in by **{close_local_pt}**.",
    "**{glyph} {daemon_cap}** is tomorrow's daemon. you know the drill — drop ideas in <#{tally_id}>, react 👍 on what you want them to encounter. door closes **{close_local_pt}**. 🤠",
]


def today_iso() -> str:
    return dt.date.today().isoformat()


def utc_now_iso() -> str:
    return dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def tomorrow() -> dt.date:
    return dt.date.today() + dt.timedelta(days=1)


def daemon_for_weekday(d: dt.date) -> Optional[str]:
    return DAY_TO_DAEMON.get(d.strftime("%A").lower())


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"active": {}, "history": []}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2))


def build_cta_text(daemon: str, daemon_day: dt.date, close_at_utc: dt.datetime) -> str:
    g = GLYPH.get(daemon, "?")
    elem = ELEMENT.get(daemon, "")
    close_local_pt = (close_at_utc - dt.timedelta(hours=7)).strftime("%H:%M PT")
    close_cet = (close_at_utc + dt.timedelta(hours=2)).strftime("%H:%M CET")
    close_jst = (close_at_utc + dt.timedelta(hours=9)).strftime("%H:%M JST")
    return (
        f"**tomorrow: {g} {daemon.capitalize()}'s day**\n"
        f"*{elem}*\n\n"
        f"drop a concept, tension, or question {daemon} should sit inside — one reply per idea.\n"
        f"**react 👍 on the ideas you want to see live.**\n\n"
        f"door closes in ~6 hours (**{close_local_pt} / {close_cet} / {close_jst}**) — "
        f"i'll encode the most-liked into a SIML term, push it to the Nema-Swarm vault, "
        f"and set it as {daemon}'s scene for {daemon_day.strftime('%A %b %d')}.\n\n"
        f"if your idea doesn't win, bring it to **#EncodeIdea** — i'll encode it there too and "
        f"you'll get a sharable link to your own SIML term for simulation."
    )


def build_announcement_text(daemon: str, daemon_day: dt.date, close_at_utc: dt.datetime, tally_id: str) -> str:
    g = GLYPH.get(daemon, "?")
    elem_short = ELEMENT_SHORT.get(daemon, "")
    close_local_pt = (close_at_utc - dt.timedelta(hours=7)).strftime("%H:%M PT")
    template = ANNOUNCEMENT_TEMPLATES[daemon_day.toordinal() % len(ANNOUNCEMENT_TEMPLATES)]
    return template.format(
        glyph=g, daemon_cap=daemon.capitalize(), elem_short=elem_short,
        tally_id=tally_id, close_local_pt=close_local_pt,
    )


def post_to_discord(channel_id: str, content: str, token: str) -> dict:
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    data = json.dumps({"content": content}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json",
        "User-Agent": "NemaSwarmMC-idea-cta/1.0",
    }, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return {"ok": True, "status": resp.status, "body": json.loads(resp.read().decode("utf-8"))}
    except urllib.error.HTTPError as e:
        return {"ok": False, "status": e.code, "body": e.read().decode("utf-8")[:400]}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--daemon", default=None, help="override daemon (default: tomorrow's weekday daemon)")
    ap.add_argument("--for-day", default=None, help="YYYY-MM-DD the daemon is live (default: tomorrow)")
    ap.add_argument("--close-in", type=float, default=6.0, help="hours from now to close voting (default 6)")
    ap.add_argument("--no-announce", action="store_true", help="skip the #member-chat heads-up announcement")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cfg = json.loads(CHANNELS.read_text())
    tally_info = cfg.get("mc_channels", {}).get("the_tally", {})
    tally_id = tally_info.get("channel_id")
    if not tally_id or tally_id == "<FILL_IN>":
        print(json.dumps({"ok": False, "error": "the_tally channel_id not configured"}))
        return 1
    member_chat_info = cfg.get("mc_channels", {}).get("member_chat", {})
    member_chat_id = member_chat_info.get("channel_id") if not args.no_announce else None
    if member_chat_id == "<FILL_IN>":
        member_chat_id = None

    # Determine daemon + daemon_day
    if args.for_day:
        daemon_day = dt.date.fromisoformat(args.for_day)
    else:
        daemon_day = tomorrow()
    daemon = args.daemon or daemon_for_weekday(daemon_day)
    if not daemon:
        print(json.dumps({"ok": True, "skipped": True, "reason": f"no daemon for {daemon_day} (sunday?)"}))
        return 0

    # Compute close time
    now = dt.datetime.utcnow().replace(microsecond=0)
    close_at = now + dt.timedelta(hours=args.close_in)

    # Avoid duplicate active CTAs for this (day, daemon)
    state = load_state()
    key = f"{daemon_day.isoformat()}-{daemon}"
    if key in state.get("active", {}) and state["active"][key].get("status") == "open":
        print(json.dumps({"ok": False, "error": f"active CTA already exists for {key}", "state": state["active"][key]}))
        return 1

    cta_content = build_cta_text(daemon, daemon_day, close_at)
    announce_content = build_announcement_text(daemon, daemon_day, close_at, tally_id) if member_chat_id else None

    if args.dry_run:
        print(json.dumps({
            "ok": True, "dry_run": True,
            "daemon": daemon, "daemon_day": daemon_day.isoformat(),
            "tally_channel_id": tally_id,
            "member_chat_channel_id": member_chat_id,
            "close_at_utc": close_at.isoformat() + "Z",
            "cta_preview": cta_content,
            "announcement_preview": announce_content,
        }, indent=2))
        return 0

    # Post CTA to #the-tally (canonical vote source)
    token = os.environ.get("DISCORD_MC_TOKEN", "").strip()
    if not token:
        print(json.dumps({"ok": False, "error": "DISCORD_MC_TOKEN missing"}))
        return 1

    cta_resp = post_to_discord(tally_id, cta_content, token)
    if not cta_resp.get("ok"):
        print(json.dumps({"ok": False, "error": "tally CTA post failed", "detail": cta_resp}))
        return 2
    cta_msg_id = cta_resp["body"].get("id")

    # Best-effort: post the heads-up to #member-chat. Don't fail the whole job
    # if this errors — the canonical CTA is already in the tally.
    announce_msg_id = None
    announce_error = None
    if member_chat_id and announce_content:
        ann_resp = post_to_discord(member_chat_id, announce_content, token)
        if ann_resp.get("ok"):
            announce_msg_id = ann_resp["body"].get("id")
        else:
            announce_error = ann_resp

    # Record state
    state.setdefault("active", {})[key] = {
        "daemon": daemon,
        "daemon_day": daemon_day.isoformat(),
        "cta_message_id": cta_msg_id,
        "channel_id": tally_id,
        "announcement_message_id": announce_msg_id,
        "announcement_channel_id": member_chat_id,
        "open_at_utc": utc_now_iso(),
        "close_at_utc": close_at.isoformat() + "Z",
        "status": "open",
    }
    save_state(state)

    print(json.dumps({
        "ok": True, "daemon": daemon, "daemon_day": daemon_day.isoformat(),
        "cta_message_id": cta_msg_id, "channel_id": tally_id,
        "announcement_message_id": announce_msg_id,
        "announcement_channel_id": member_chat_id,
        "announcement_error": announce_error,
        "close_at_utc": close_at.isoformat() + "Z",
        "state_key": key,
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
