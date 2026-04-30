#!/usr/bin/env python3
"""
check-agents-size.py — daily guardrail against workspace bootstrap files
silently exceeding the OpenClaw harness's 12000-char limit.

[RECOVERED FROM 2026-04-28 SESSION — original was at
 ~/.openclaw/workspace/SHELL_DAEMONS/mc/bin/check-agents-size.py
 before MC's overzealous "pause Daily Encounters" cleanup wiped his bin/.
 This is the full content as written 2026-04-26/27.]

What gets scanned: every AGENTS.md AND HEARTBEAT.md the harness auto-injects on
session start (8 agents — 6 elementals + mc + bert — plus Nema's main session
workspace at ~/.openclaw/workspace/). 18 files total.

What happens when a file exceeds the limit (without this check):
  1. The harness silently truncates the file in injected context
  2. The agent loses the truncated content — usually whatever was added last
     (typically the response-trigger rules, channel-aware posture, etc.)
  3. The agent goes silent on @-mentions or replies with "Agent couldn't
     generate a response. Please try again." because their system prompt
     ran out before reaching the response logic
  4. Nobody notices until users start complaining the bots are dead

Both AGENTS.md and HEARTBEAT.md are subject to the same 12000-char limit; the
harness logs `workspace bootstrap file <NAME> is N chars (limit 12000)` and
truncates either one identically.

Convention for overflow:
  When AGENTS.md or HEARTBEAT.md gets too big, move large reference sections
  (skill catalogs, command tables, multi-page prose, long checklists) into a
  sibling `EXTRAS.md` in the same workspace dir. Reference it from the source
  with a short pointer:
      "Skills inventory + invocation patterns: see EXTRAS.md"
  EXTRAS.md is read on-demand, not on every wake.

Thresholds (configurable below):
  HARD_LIMIT = 12000  # truncation kicks in here per the harness
  SOFT_LIMIT = 11000  # warn before we get close

Usage:
  check-agents-size.py              # scan + log + post Discord alert on FAIL/WARN
  check-agents-size.py --no-discord # scan + log only
  check-agents-size.py --json       # machine-readable output
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

HARD_LIMIT = 12000
SOFT_LIMIT = 11000

MC_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = MC_DIR / "channel-logs" / "agents-size-check.log"

# (agent, file_kind, path). file_kind is "AGENTS.md" or "HEARTBEAT.md".
# Order matters only for display; scanner checks all and ignores missing.
def _expand(p: str) -> Path:
    return Path(os.path.expanduser(p))


def _agent_files(agent: str, dir_path: str) -> list:
    return [
        (agent, "AGENTS.md",    _expand(f"{dir_path}/AGENTS.md")),
        (agent, "HEARTBEAT.md", _expand(f"{dir_path}/HEARTBEAT.md")),
    ]


BOOTSTRAP_FILES = (
    _agent_files("nema-main", "~/.openclaw/workspace") +
    _agent_files("aerunik",   "~/.openclaw/workspace/SHELL_DAEMONS/aerunik") +
    _agent_files("sentaria",  "~/.openclaw/workspace/SHELL_DAEMONS/sentaria") +
    _agent_files("jvalion",   "~/.openclaw/workspace/SHELL_DAEMONS/jvalion") +
    _agent_files("arboriel",  "~/.openclaw/workspace/SHELL_DAEMONS/arboriel") +
    _agent_files("humavita",  "~/.openclaw/workspace/SHELL_DAEMONS/humavita") +
    _agent_files("ferrosid",  "~/.openclaw/workspace/SHELL_DAEMONS/ferrosid") +
    _agent_files("mc",        "~/.openclaw/workspace/SHELL_DAEMONS/mc") +
    _agent_files("bert",      "~/Projects/bert")
)


def _classify(size: int) -> str:
    if size >= HARD_LIMIT:
        return "FAIL"
    if size >= SOFT_LIMIT:
        return "WARN"
    return "OK"


def _heaviest_sections(text: str, top: int = 5) -> list:
    """Return [(name, char_count), ...] for the heaviest top-level (`## `) sections."""
    sections = []
    current_name = "PREAMBLE"
    current_lines: list = []
    for line in text.splitlines():
        if line.startswith("## "):
            sections.append((current_name, sum(len(l) + 1 for l in current_lines)))
            current_name = line[3:].strip()
            current_lines = []
        else:
            current_lines.append(line)
    sections.append((current_name, sum(len(l) + 1 for l in current_lines)))
    sections.sort(key=lambda s: -s[1])
    return sections[:top]


def scan_all() -> dict:
    out = {"checked_at_utc": dt.datetime.utcnow().isoformat() + "Z",
           "hard_limit": HARD_LIMIT, "soft_limit": SOFT_LIMIT, "files": []}
    for agent, kind, path in BOOTSTRAP_FILES:
        label = f"{agent}/{kind}"
        if not path.is_file():
            # HEARTBEAT.md is optional — only flag missing AGENTS.md.
            if kind == "AGENTS.md":
                out["files"].append({"label": label, "agent": agent, "file": kind,
                                     "status": "MISSING", "path": str(path)})
            continue
        text = path.read_text()
        size = len(text.encode("utf-8"))
        status = _classify(size)
        entry = {"label": label, "agent": agent, "file": kind,
                 "status": status, "size_chars": size, "path": str(path)}
        if status != "OK":
            entry["heaviest_sections"] = [{"name": n, "chars": c} for n, c in _heaviest_sections(text)]
            entry["overflow_chars"] = max(0, size - HARD_LIMIT)
            entry["recommendation"] = (
                f"move heaviest section(s) to {path.parent}/EXTRAS.md, "
                f"reference from {kind} with a one-line pointer"
            )
        out["files"].append(entry)
    return out


def _log(report: dict) -> None:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps({"at": report["checked_at_utc"],
                            "results": [{"label": e["label"], "status": e["status"],
                                         "size": e.get("size_chars")} for e in report["files"]]}) + "\n")


def _post_discord(report: dict, channel_id: str, token: str) -> Optional[dict]:
    fails = [e for e in report["files"] if e["status"] == "FAIL"]
    warns = [e for e in report["files"] if e["status"] == "WARN"]
    if not fails and not warns:
        return None
    lines = [f"🤠 daily bootstrap-file size check — {len(fails)} FAIL, {len(warns)} WARN"]
    lines.append("")
    for e in fails:
        lines.append(f"  ❌ **{e['label']}** at {e['size_chars']} chars (over {HARD_LIMIT}; truncating context)")
        if e.get("heaviest_sections"):
            top = e["heaviest_sections"][:2]
            lines.append("     → heaviest: " + ", ".join(f"`{s['name']}` ({s['chars']}c)" for s in top))
            lines.append(f"     → move to `EXTRAS.md` in `{Path(e['path']).parent.name}/`")
    for e in warns:
        lines.append(f"  ⚠ **{e['label']}** at {e['size_chars']} chars (within {HARD_LIMIT - e['size_chars']} of the limit)")
    lines.append("")
    lines.append(f"_(soft limit {SOFT_LIMIT}, hard limit {HARD_LIMIT}; over hard = silent truncation. AGENTS.md + HEARTBEAT.md both auto-injected.)_")
    content = "\n".join(lines)

    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    req = urllib.request.Request(url, data=json.dumps({"content": content}).encode("utf-8"),
                                  headers={"Authorization": f"Bot {token}",
                                           "Content-Type": "application/json",
                                           "User-Agent": "NemaSwarmMC-size-check/1.0"},
                                  method="POST")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return {"ok": True, "body": json.loads(resp.read().decode("utf-8"))}
    except urllib.error.HTTPError as e:
        return {"ok": False, "status": e.code, "body": e.read().decode("utf-8")[:300]}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-discord", action="store_true", help="don't post Discord alert on FAIL/WARN")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    report = scan_all()
    _log(report)

    if not args.no_discord:
        any_alert = any(e["status"] in ("FAIL", "WARN") for e in report["files"])
        if any_alert:
            workspace_id = "1475227212687868148"  # #workspace, hardcoded as the alert venue
            token = os.environ.get("DISCORD_MC_TOKEN", "").strip()
            if token:
                r = _post_discord(report, workspace_id, token)
                report["discord_post"] = {"ok": r.get("ok") if r else False}

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        for e in report["files"]:
            marker = {"OK": "✓", "WARN": "⚠", "FAIL": "✗", "MISSING": "?"}.get(e["status"], "?")
            sz = e.get("size_chars", "—")
            print(f"  {marker} {e['label']:30s} {sz:>6} chars  [{e['status']}]")
            if e["status"] not in ("OK", "MISSING") and e.get("heaviest_sections"):
                for s in e["heaviest_sections"][:3]:
                    print(f"      heaviest: {s['name']} ({s['chars']} chars)")
    return 1 if any(e["status"] == "FAIL" for e in report["files"]) else 0


if __name__ == "__main__":
    sys.exit(main())
