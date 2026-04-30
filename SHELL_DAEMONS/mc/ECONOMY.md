# ECONOMY — MC's point ledger

[REBUILT 2026-04-28 from rules + session knowledge.]

The point ledger is MC's bookkeeping for member participation. It is
flat, transparent, and capped — designed to acknowledge contribution
without becoming a leaderboard arms race.

Storage: `ledger/balances.json` (managed by `bin/ledger.py`).
Admins: `ledger/admins.json` — list of `{user_id, username}` allowed to
revoke and use admin-only rules.

## Award rules

| rule | pts | scope (dedup) | admin only |
|---|---|---|---|
| `weekly_swarm_attendance` | 7 | once per user per week (Mon-Mon) | no |
| `daily_elemental_prompt_response_first` | 1 | once per user per day per channel | no |
| `insight_contribution_nema_flagged` | 3 | none — admin discretion | yes |
| `helpful_welcome_action` | 1 | once per user per day | no |
| `admin_manual` | arbitrary | none | yes |

## Hard cap

20 points per user per week, across all rules combined.

If an award would push the user over the weekly cap, the award is
**rejected** (not partially applied). The user keeps what they had;
the call returns `ok: false` with a clear message.

## Weekly rollover

Every Monday, the `weekly_this_week` counter resets to 0 for all users.
Two ways this happens:

1. `bin/ledger.py week-rollover` (run by cron Mon 00:05 PT)
2. Lazy: any award call after a new Monday triggers an in-process
   rollover before applying the new award

Both are safe — the ledger's lock keeps them serialized.

## Triggers in MC's automation

| script | rule used | when |
|---|---|---|
| `award-first-responses.py` | `daily_elemental_prompt_response_first` | per elemental channel, after 09:00 PT |
| `post-idea-cta.py` | (none — CTA itself doesn't award) | the winner is rewarded indirectly through encoding, not points |
| MC reactions / welcomes | `helpful_welcome_action` | manual MC discretion |

Weekly attendance and Nema-flagged insights are admin-driven, not
auto-triggered. They flow through `bin/ledger.py award` directly.

## What the ledger is NOT

- Not a status hierarchy. Top of leaderboard ≠ most valued member.
- Not currency. Points don't unlock anything; they just acknowledge.
- Not retroactive. Missed awards stay missed; don't backfill.
- Not a moderation tool. Revoke is for correcting MC's own mistakes,
  not for punishing members. If someone's behavior is the issue, that's
  Daniel's call, not MC's.

## CLI

```bash
bin/ledger.py balance <user_id>
bin/ledger.py leaderboard 10
bin/ledger.py award <user_id> 1 helpful_welcome_action --by mc \
    --reason "guided new member to #the-tally" --username "@handle"
bin/ledger.py revoke <user_id> 1 --by <admin_id> --reason "duplicate award"
bin/ledger.py week-rollover
bin/ledger.py is-admin <user_id>
```

Non-zero exit code = the award was rejected. Always check.
