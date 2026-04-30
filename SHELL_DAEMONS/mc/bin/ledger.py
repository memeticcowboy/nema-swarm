#!/usr/bin/env python3
"""
ledger.py — MC's point economy CLI for the NEMA SWARM.

[REBUILT 2026-04-28 from rules documented in AGENTS.md. Original was lost
 in MC's destructive cleanup. Storage schema is reconstructed (originals'
 exact format unknown; this version is internally consistent and self-
 documenting).]

Award rules + per-rule limits:
  - weekly_swarm_attendance         7 pts (auto, max once per user per week)
  - daily_elemental_prompt_response_first  1 pt (auto, max once per user per day per channel)
  - insight_contribution_nema_flagged      3 pts (admin only)
  - helpful_welcome_action          1 pt (MC's discretion, max once per user per day)
  - admin_manual                    arbitrary amount (admin only)

Hard cap: 20 pts per user per week (across all rules).

Storage:
  - ledger/balances.json — user balances + history
  - ledger/admins.json   — admin allowlist (user IDs that can credit/revoke)

Subcommands:
  ledger.py balance <user_id>
  ledger.py leaderboard [N]
  ledger.py award <user_id> <points> <rule> [--reason "..."] [--by <actor>] [--username "..."]
  ledger.py revoke <user_id> <points> --by <admin> [--reason "..."]
  ledger.py week-rollover
  ledger.py is-admin <user_id>
"""

from __future__ import annotations
import argparse
import datetime as dt
import fcntl
import json
import os
import sys
from contextlib import contextmanager
from pathlib import Path

MC_DIR = Path(__file__).resolve().parent.parent
LEDGER_DIR = MC_DIR / "ledger"
BALANCES = LEDGER_DIR / "balances.json"
ADMINS = LEDGER_DIR / "admins.json"
LOCK = LEDGER_DIR / ".ledger.lock"

WEEKLY_CAP = 20

RULE_LIMITS = {
    # rule: (max_amount_per_invocation, scope_for_dedup, admin_only)
    "weekly_swarm_attendance":              (7, "week",  False),
    "daily_elemental_prompt_response_first": (1, "day-channel", False),
    "insight_contribution_nema_flagged":    (3, None,   True),
    "helpful_welcome_action":               (1, "day",   False),
    "admin_manual":                         (None, None, True),
}


def utc_now_iso() -> str:
    return dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def monday_of(d: dt.date) -> dt.date:
    return d - dt.timedelta(days=d.weekday())


@contextmanager
def _locked():
    LEDGER_DIR.mkdir(parents=True, exist_ok=True)
    fd = os.open(str(LOCK), os.O_CREAT | os.O_RDWR, 0o644)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX)
        yield
    finally:
        try:
            fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)


def _load_balances() -> dict:
    if BALANCES.exists():
        return json.loads(BALANCES.read_text())
    return {
        "users": {},
        "week_start": monday_of(dt.date.today()).isoformat(),
        "_note": "MC point ledger. user_id keys are Discord IDs.",
    }


def _save_balances(data: dict) -> None:
    LEDGER_DIR.mkdir(parents=True, exist_ok=True)
    BALANCES.write_text(json.dumps(data, indent=2))


def _load_admins() -> set:
    if ADMINS.exists():
        d = json.loads(ADMINS.read_text())
        return {a["user_id"] for a in d.get("admins", [])}
    return set()


def is_admin(user_id: str) -> bool:
    return user_id in _load_admins()


def _ensure_user(data: dict, user_id: str, username: str = "") -> dict:
    if user_id not in data["users"]:
        data["users"][user_id] = {
            "user_id": user_id,
            "username": username or "",
            "total": 0,
            "weekly_this_week": 0,
            "history": [],
        }
    elif username and not data["users"][user_id].get("username"):
        data["users"][user_id]["username"] = username
    return data["users"][user_id]


def _check_rule_dedup(user: dict, rule: str, scope_key: str) -> bool:
    """Return True if a duplicate-by-scope award was already given today/this-week."""
    if not scope_key:
        return False
    for entry in user.get("history", []):
        if entry.get("rule") == rule and entry.get("dedup_scope") == scope_key:
            return True
    return False


def award(user_id: str, points: int, rule: str, *, by: str = "system",
          reason: str = "", username: str = "", scope_extra: str = "") -> dict:
    """Apply an award. Returns {ok, new_total, weekly_this_week, ...}."""
    if rule not in RULE_LIMITS:
        return {"ok": False, "error": f"unknown rule: {rule}"}
    max_per_invoke, scope_kind, admin_only = RULE_LIMITS[rule]
    if admin_only and not is_admin(by):
        return {"ok": False, "error": f"rule {rule} is admin-only; {by} is not an admin"}
    if max_per_invoke is not None and points > max_per_invoke:
        return {"ok": False, "error": f"rule {rule} caps at {max_per_invoke} per invocation; got {points}"}
    if points <= 0:
        return {"ok": False, "error": "points must be positive"}

    today = dt.date.today()
    week_start = monday_of(today).isoformat()

    # Build dedup scope key
    scope_key = ""
    if scope_kind == "week":
        scope_key = f"week:{week_start}"
    elif scope_kind == "day":
        scope_key = f"day:{today.isoformat()}"
    elif scope_kind == "day-channel":
        scope_key = f"day:{today.isoformat()}:channel:{scope_extra or 'unknown'}"

    with _locked():
        data = _load_balances()
        # Auto-rollover if a new week started
        if data.get("week_start") != week_start:
            for u in data["users"].values():
                u["weekly_this_week"] = 0
            data["week_start"] = week_start

        user = _ensure_user(data, user_id, username)

        if scope_kind and _check_rule_dedup(user, rule, scope_key):
            return {"ok": False, "error": f"rule {rule} already awarded for scope {scope_key}",
                    "user_id": user_id, "total": user["total"]}

        if user["weekly_this_week"] + points > WEEKLY_CAP:
            return {"ok": False, "error": f"would exceed weekly cap {WEEKLY_CAP}; current weekly={user['weekly_this_week']}, requested={points}",
                    "user_id": user_id, "total": user["total"]}

        user["total"] += points
        user["weekly_this_week"] += points
        user["history"].append({
            "at": utc_now_iso(),
            "delta": points,
            "rule": rule,
            "by": by,
            "reason": reason,
            "dedup_scope": scope_key or None,
        })
        _save_balances(data)

    return {
        "ok": True,
        "user_id": user_id,
        "username": user["username"],
        "delta": points,
        "rule": rule,
        "total": user["total"],
        "weekly_this_week": user["weekly_this_week"],
        "weekly_remaining": max(0, WEEKLY_CAP - user["weekly_this_week"]),
    }


def revoke(user_id: str, points: int, by: str, reason: str = "") -> dict:
    if not is_admin(by):
        return {"ok": False, "error": f"revoke is admin-only; {by} is not an admin"}
    if points <= 0:
        return {"ok": False, "error": "points must be positive"}
    with _locked():
        data = _load_balances()
        if user_id not in data["users"]:
            return {"ok": False, "error": f"unknown user: {user_id}"}
        user = data["users"][user_id]
        user["total"] = max(0, user["total"] - points)
        user["weekly_this_week"] = max(0, user["weekly_this_week"] - points)
        user["history"].append({
            "at": utc_now_iso(),
            "delta": -points,
            "rule": "revoke",
            "by": by,
            "reason": reason,
        })
        _save_balances(data)
    return {"ok": True, "user_id": user_id, "total": user["total"], "weekly_this_week": user["weekly_this_week"]}


def balance(user_id: str) -> dict:
    data = _load_balances()
    user = data["users"].get(user_id)
    if not user:
        return {"ok": True, "user_id": user_id, "total": 0, "weekly_this_week": 0,
                "weekly_remaining": WEEKLY_CAP, "exists": False}
    return {
        "ok": True,
        "user_id": user_id,
        "username": user.get("username", ""),
        "total": user["total"],
        "weekly_this_week": user["weekly_this_week"],
        "weekly_remaining": max(0, WEEKLY_CAP - user["weekly_this_week"]),
        "exists": True,
    }


def leaderboard(n: int = 10) -> dict:
    data = _load_balances()
    rows = sorted(
        ({"user_id": uid, "username": u.get("username", ""), "total": u["total"]}
         for uid, u in data["users"].items()),
        key=lambda r: -r["total"],
    )
    return {"ok": True, "leaderboard": rows[:n], "week_start": data.get("week_start")}


def week_rollover() -> dict:
    today = dt.date.today()
    new_week = monday_of(today).isoformat()
    with _locked():
        data = _load_balances()
        if data.get("week_start") == new_week:
            return {"ok": True, "rollover_skipped": True, "week_start": new_week}
        for u in data["users"].values():
            u["weekly_this_week"] = 0
        data["week_start"] = new_week
        _save_balances(data)
    return {"ok": True, "rollover_done": True, "week_start": new_week}


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_bal = sub.add_parser("balance"); p_bal.add_argument("user_id")
    p_lb  = sub.add_parser("leaderboard"); p_lb.add_argument("n", nargs="?", type=int, default=10)
    p_aw  = sub.add_parser("award")
    p_aw.add_argument("user_id"); p_aw.add_argument("points", type=int); p_aw.add_argument("rule")
    p_aw.add_argument("--reason", default=""); p_aw.add_argument("--by", default="system")
    p_aw.add_argument("--username", default=""); p_aw.add_argument("--scope-extra", default="")
    p_rv  = sub.add_parser("revoke")
    p_rv.add_argument("user_id"); p_rv.add_argument("points", type=int)
    p_rv.add_argument("--by", required=True); p_rv.add_argument("--reason", default="")
    sub.add_parser("week-rollover")
    p_ad = sub.add_parser("is-admin"); p_ad.add_argument("user_id")

    args = ap.parse_args()
    if args.cmd == "balance":
        r = balance(args.user_id)
    elif args.cmd == "leaderboard":
        r = leaderboard(args.n)
    elif args.cmd == "award":
        r = award(args.user_id, args.points, args.rule, by=args.by, reason=args.reason,
                  username=args.username, scope_extra=args.scope_extra)
    elif args.cmd == "revoke":
        r = revoke(args.user_id, args.points, by=args.by, reason=args.reason)
    elif args.cmd == "week-rollover":
        r = week_rollover()
    elif args.cmd == "is-admin":
        r = {"ok": True, "user_id": args.user_id, "is_admin": is_admin(args.user_id)}
    else:
        r = {"ok": False, "error": f"unknown command: {args.cmd}"}
    print(json.dumps(r, indent=2))
    return 0 if r.get("ok") else 2


if __name__ == "__main__":
    sys.exit(main())
