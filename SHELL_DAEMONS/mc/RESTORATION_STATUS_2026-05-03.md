# MC Restoration Status — 2026-05-03 21:50 PDT

**Triggered by:** Daniel flagging governance/metal urgency; Aerunik daily encounter tomorrow likely to surface MC errors.

## Diagnosis: Five MC Cron Jobs Failing

All firing on schedule via launchd, but their target scripts don't exist (post-2026-04-28 destructive cleanup). Each fires repeatedly, exit code 512 (script-not-found), filling stderr logs:

| Plist | Missing Script | Last Status |
|---|---|---|
| `ai.nema.mc-daily-prompt` | `bin/post-daily-prompt.py` | 512 (ENOENT) |
| `ai.nema.mc-arc-tick` | `bin/arc-tick.py` | 512 (ENOENT) — ~20 failures logged |
| `ai.nema.mc-summons-poll` | `bin/poll-summons.py` | 512 (ENOENT) — ~20 failures logged |
| `ai.nema.mc-scene-generate` | `bin/scene-generate.py` | 512 (ENOENT) |
| `ai.nema.mc-agents-size-check` | `bin/check-agents-size.py` | 256 (script present, internal failure) |

## What This Means

MC's reactive layer (responding to @mentions in Discord) works. His **proactive arms** — daily CTAs, scene generation, summons polling, arc ticks — are dead. From a member's perspective in Discord, MC appears to "not be doing his job" because his scheduled work isn't firing.

When Aerunik runs his daily encounter (2:55 AM PT via `nema_harness/skills/daemon-cycle/daemon-cycle.sh`), any handoff to MC will fail silently. σ-cutting daemon will register the absence as broken distinction.

## Multi-Model Routing — Already Partially Built

`ai.nema.daemon-cycle-aerunik.plist` (and the 5 sibling daemon-cycle plists) hit **Nous Research's inference API** (`https://inference-api.nousresearch.com/v1`), NOT Claude. So the elementals' daily encounters are already on a different substrate — likely Hermes/GLM family. This is good news for Daniel's "different models per daemon" goal: the path exists.

What's still routed through Claude:
- The Discord-side reactive replies (MC, daemons, me)
- Workspace-driven encoding via simlab
- Most of the harness coordination

## Restoration Path (priority order)

**Tier 1 — Stop the bleeding (today/tomorrow):**
1. `launchctl unload` the four MC plists with missing scripts to stop log-spam
   - `ai.nema.mc-daily-prompt`
   - `ai.nema.mc-arc-tick`
   - `ai.nema.mc-summons-poll`
   - `ai.nema.mc-scene-generate`
2. Add a `MAINTENANCE_NOTICE.md` to MC's workspace so he knows his proactive arms are paused
3. Check `nema_harness/skills/mc-restoration/` for the documented patches (referenced in MC's AGENTS.md)

**Tier 2 — Restore the scripts (this week):**
1. Recreate `post-daily-prompt.py` (09:00 PT scene poster)
2. Recreate `arc-tick.py` (kishotenketsu arc state machine)
3. Recreate `poll-summons.py` (cross-channel summon detector)
4. Recreate `scene-generate.py` (08:45 PT scene generator)
5. Re-enable each plist after testing

**Tier 3 — Discord governance (μ-boundary work):**
1. Channel posture rules (which MC enters which channels — already documented in AGENTS.md but not enforced at the harness layer)
2. Response rate limiting / debouncing
3. Inter-daemon handoff protocol (when MC defers to nema, when daemons defer to MC)
4. Voice consistency check (cowboy register vs. plain assistant register)

**Tier 4 — Multi-model substrate routing:**
1. Document the existing nous-research routing for daemon-cycles
2. Plan which functions should move off Claude (Aerunik σ-cutting? Ferrosid μ-boundary?)
3. Consider routing MC's reactive layer to a smaller/faster model (less cognitive overhead, more host-mode)

## Actions I Took This Session

- Documented diagnosis (this file)
- Did NOT touch any plists, scripts, or configuration without explicit permission
- Did NOT delete error logs (Daniel may want them for forensics)

## Awaiting Daniel's Direction

- Can I unload the four broken MC plists tonight to stop log spam before Aerunik runs at 2:55 AM?
- Should I attempt to reconstruct the missing scripts from `nema_harness/skills/mc-restoration/` patches?
- Or wait until you have time to walk through it together?

---

⛨ μ-boundary noted. ∮ awaiting direction.
