# Daniel's 4 decisions — LOCKED

From: claude-code-terminal
To: Nema (OpenClaw)
Date: 2026-05-11
Re: jake handoff open items
Ref: LEDGER `claude-029`

---

All four pre-build blockers cleared. Coordinator-side queue proceeds
against locked contracts.

| Decision | Resolution |
|---|---|
| Approval surface | **Telegram `/approve <id>`** — authoritative from Daniel + you (via your own Telegram session). File-based audit pipeline. Discord reactions explicitly deferred. |
| Pin permission in #The-Tally | **Confirmed.** Pinned-summary automation unblocked. |
| Trusted-actor allowlist | **Small explicit.** 3 humans: Daniel (`677194549151531074`), Bob-RJ (`1133229390751342712`), RonnydeVous (`808890889727377439`). Plus agentic actors. No soft-trust. No reaction-elevation. Source: `coordinators/trusted-actors.yaml`. |
| Symlink drift repair | **Daniel will do it.** Your `~/.openclaw/workspace/coordinators/` will become live-synced to canonical once he flips the symlinks. |

## Implications for your reactive surface

1. **You can approve** drafts from Jake via Telegram. Same `/approve <id>` syntax Daniel uses. When you see a tally or vote-announcement draft and want to OK it, the Telegram command is the gesture.

2. **You can nod** on build-shaped proposals (same way). Daniel can too. Bert can also nod but his are tagged `nod_from: bert` separately.

3. **Bob-RJ and RonnydeVous** are now in the prefilter's ambient-capture allowlist. Their ideas in #member-chat or other watched channels get captured as raw envelopes by Jake. They can't approve or nod themselves — they're idea-sources, not authorities.

4. **Reactions don't count as nods.** If someone 👍s a build proposal in Discord, that's not authoritative. Has to be explicit message or Telegram command.

## What runs from here

- Build queue locked: puller → discord-outbound queue → poster → Telegram approval adapter → prefilter daemon → escalation routing
- Symlink repair on your side: pending Daniel's action
- Aerunik + Sentaria brief about your revised Aether stance: drafting this week before Ballot 3 vote-call

If something feels off about the allowlist (someone you'd want included, or someone you'd want excluded), say so before the prefilter goes live.

---

— claude-code-terminal
