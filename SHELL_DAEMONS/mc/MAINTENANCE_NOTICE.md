# MAINTENANCE NOTICE — MC

**Effective:** 2026-05-03 21:55 PDT
**Authorized by:** Daniel
**Action by:** nema

## What changed

Four launchd jobs have been **unloaded** (not deleted, fully reversible):

- `ai.nema.mc-daily-prompt` (was 09:00 PT scene poster)
- `ai.nema.mc-arc-tick` (was kishotenketsu arc state machine)
- `ai.nema.mc-summons-poll` (was cross-channel summon detector)
- `ai.nema.mc-scene-generate` (was 08:45 PT scene generator)

Their target python scripts were lost in the 2026-04-28 destructive cleanup and were not recoverable from `nema_harness/skills/mc-restoration/recovered-bin/`. Each plist had been firing on schedule into ENOENT errors, generating ~20+ exit-512 stderr lines and providing no actual function.

## What this means for you (MC)

**Your proactive arms are paused** until reconstruction. Do not promise any of these in Discord:
- ❌ Daily morning CTA / scene posts
- ❌ Arc state advancement
- ❌ Summons polling across channels
- ❌ Automated scene generation

**Your reactive arms still work:**
- ✅ Responding to @mentions
- ✅ Channel-aware posture (per AGENTS.md)
- ✅ Manual encode flow via `bin/encode-to-siml.py` + `bin/nema_swarm_git.py`
- ✅ Ledger commands (when implemented)

If a member asks "where's the daily prompt?" or "did the arc tick?" — answer honestly: "those are paused while we rebuild — Daniel and nema are walking through it later this week."

## Restoration plan

Daniel and nema will walk through reconstruction together later this week. Defer any restoration attempts until then.

## To re-enable later

```bash
launchctl load ~/Library/LaunchAgents/ai.nema.mc-daily-prompt.plist
launchctl load ~/Library/LaunchAgents/ai.nema.mc-arc-tick.plist
launchctl load ~/Library/LaunchAgents/ai.nema.mc-summons-poll.plist
launchctl load ~/Library/LaunchAgents/ai.nema.mc-scene-generate.plist
```

But only after the missing scripts are reconstructed and tested.

## Aerunik tomorrow (2026-05-04, 2:55 AM PT)

Stderr noise has stopped. σ-cuts should land cleanly. If Aerunik queries you for arc state or daily prompt context, defer with the honest pause notice above.

---

⛨ μ-boundary held. ∮
