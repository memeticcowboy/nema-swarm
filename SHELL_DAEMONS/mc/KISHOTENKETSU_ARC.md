# KISHŌTENKETSU ARC — daily scene structure

> **🚧 DEFERRED 2026-04-29 — DO NOT BUILD AGAINST THIS YET.**
> User is reframing scene-staging requirements. The canonical spec is now `~/Projects/nema_harness/SIML_SCENE_STAGING_ARCHITECTURE_v0_1.md` which defines scene-staging as an *embodied encounter memory architecture*, not a narrative-arc structure. This document was drafted in the narrative-arc framing before that spec was surfaced. Held for reference only; will be reconciled or retired when user returns with documented requirements.

> **Status:** REBUILT 2026-04-29 from session knowledge after the 2026-04-28 destructive cleanup wiped the original. Inference-heavy in places — every `<!-- INFER -->` marker flags a reconstruction guess that the user (Daniel) should confirm or redirect before downstream code is written against it.

## Overview

Kishōtenketsu (起承転結) is a four-act narrative form from Japanese / Chinese tradition. Unlike Western three-act structure, it does not depend on conflict-and-resolution; instead, the arc *introduces, develops, twists, and returns-with-new-context* without forcing a synthesis. It's particularly well-suited to the daemons because their work is contemplative and pattern-revealing, not problem-solving.

Each NEMA SWARM day is one daemon's day. From the moment the daemon's first scene posts in their channel (Ki) to the closing reflection (Ketsu), the arc unfolds across ~13 hours, holding one SIML term as its substrate. Members are invited *into* the arc; they don't gate it. The arc plays through regardless of whether anyone replies — the daemon's day is the daemon's day.

## The four turns

### Ki (起) — opening

The daemon enters their channel. The day's SIML term — selected by elemental weight from the canonical corpus — is voiced as a scene rather than introduced as a definition. The daemon doesn't say "today's term is X"; the daemon *steps into* X and speaks from inside it.

Posted at **07:15 PT** by the daemon's own Discord bot account, in the daemon's own channel. <!-- INFER: 07:15 derived from plist StartCalendarInterval. Original memory said 09:00; please confirm 07:15 is intentional. -->

### Sho (承) — development

The scene deepens. A facet that was implicit in Ki becomes explicit. The daemon may notice something *they* didn't see at first — that's part of the form. Sho doesn't add new material; it lets what was already there breathe.

Posted at **11:40 PT** — four ticks after Ki, mid-morning settling into noon. <!-- INFER: arc-tick fires hourly at :40; this is my guess at when Sho activates. Could also be 12:40. -->

### Ten (転) — twist

A contrasting element arrives. Not a contradiction, not a problem — a *different angle on the same substrate* that disturbs the steadiness Sho had established. This is where another daemon's perspective might be summoned, where a participant's reply might be woven in, or where the daemon themselves notices an unfamiliar quality in the term.

Posted at **15:40 PT** — afternoon, when the day's energy shifts. <!-- INFER: 15:40 chosen for "afternoon contrast" feel. Could be earlier (13:40) for a midday twist. -->

### Ketsu (結) — return

Not resolution. Not "the answer." Ki and Ten are both held; Ketsu is the daemon stepping back and letting both stand. The arc closes by returning to the beginning *with the twist now visible*. If a member's reply fed Ten, Ketsu may attribute or weave it (per Co-Sphere consent rules — see `project_co_sphere_we_sphere_lattice.md`).

Posted at **20:40 PT** — evening, the daemon's day folding closed. <!-- INFER: 20:40 chosen for "evening close" feel. May want earlier (18:40 or 19:40) given typical Discord activity windows. -->

## Day-to-daemon mapping

Per `elemental-channels.json`:

| Day | Daemon | Channel | Element |
|---|---|---|---|
| Mon | Aerunik | aerunik-channel | Air |
| Tue | Sentaria | sentaria-channel | Water |
| Wed | Jvalion | jvalion-channel | Fire |
| Thu | Arboriel | arboriel-channel | Wood |
| Fri | Humavita | humavita-channel | Earth |
| Sat | Ferrosid | ferrosid-channel | Metal |
| Sun | _nema_wrap | (multi-channel?) | aether |

Sunday is Nema's wrap — different shape, possibly a synthesis weave across the week's six daemon arcs rather than a single-daemon kishōtenketsu. <!-- INFER: Sunday handling is a real open question. Defer specifying until Mon-Sat is verified working. -->

## Generation strategy

**All four turns are generated upfront** at 07:00 PT by `generate-scene-staging.py`, in a single LLM call to deepseek-v3.2:cloud (per memory). The scene-staging meta-prompt produces all four turn-texts as a JSON object that gets written to `ledger/scene-state-<YYYY-MM-DD>.json`. Subsequent scripts (post-daily-prompt at 07:15, arc-tick at the three later hours) read from this file rather than re-prompting.

<!-- INFER: upfront generation chosen for cost (1 LLM call/day/daemon vs 4) and atomicity (the four turns must arc together, not be independently improvised). The cost is responsiveness — Ten can't react to a member's morning reply because Ten was already written at 07:00. If responsiveness matters more than atomicity, switch to per-turn generation in a Tier 6 follow-up. -->

## State schema (`ledger/scene-state-YYYY-MM-DD.json`)

```json
{
  "date": "2026-04-29",
  "daemon": "jvalion",
  "channel_id": "1496579603500765295",
  "siml_term": {
    "term_id": "F012",
    "term_name": "...",
    "term_dir": "/Users/nema/repos/nema-swarm/SIML/terms/F012_..."
  },
  "turns": {
    "ki":    { "text": "...", "scheduled_at": "2026-04-29T14:15:00Z", "posted_at": null, "message_id": null },
    "sho":   { "text": "...", "scheduled_at": "2026-04-29T18:40:00Z", "posted_at": null, "message_id": null },
    "ten":   { "text": "...", "scheduled_at": "2026-04-29T22:40:00Z", "posted_at": null, "message_id": null },
    "ketsu": { "text": "...", "scheduled_at": "2026-04-30T03:40:00Z", "posted_at": null, "message_id": null }
  },
  "thread": {
    "mode": "single_thread",
    "thread_id": null,
    "comment": "<!-- INFER: thread Sho/Ten/Ketsu as replies to Ki for visual grouping. Alt: standalone messages. -->"
  },
  "generated_by": "deepseek-v3.2:cloud",
  "generated_at": "2026-04-29T14:00:00Z"
}
```

State times stored in UTC; scheduling logic converts to PT for cron-side reasoning.

## Daemon voice rules

Each turn is in the daemon's voice, not narrator-voice and not Nema's voice. The daemon *is* speaking from inside the SIML term — the term is their substrate for the day, not their topic.

Voice anchors live in `prompts/<daemon>/*.md` (per-daemon library — Tier 5 P5). At minimum each anchor includes:
- Operator/element identity (∴ σ for Aerunik, etc.)
- Vocabulary patterns (signature words, rhythm, sentence length)
- What kinds of scene-frames feel right (Aerunik's distinction-cuts, Sentaria's resonance-flows, etc.)
- What to avoid (mismatched-element imagery, etc.)

The scene-staging meta-prompt loads the day's daemon voice anchor + the SIML term + the kishōtenketsu structure spec, and produces the 4 turns.

## SIML term selection

Each daemon has elemental affinities. The day's term is selected by:

1. Filter `~/repos/nema-swarm/SIML/terms/` for terms whose `extractor.element_signature.dominant` matches the daemon's element (Aerunik → Air, Sentaria → Water, etc.)
2. Within that pool, weight by lifecycle (`canonical` > `working` > `draft`) and by recency-of-last-staging (terms not yet staged or staged longest ago get higher weight)
3. Random selection within top weighted candidates — `ledger/scene-history.json` tracks which term each daemon staged on which date

<!-- INFER: weighting heuristic from session knowledge. Original may have used a different formula. Adjust freely. -->

## Member interaction

The arc plays through regardless of replies. But:
- Reactions and replies between turns are noticed by `arc-tick.py` and may inform Ten's posting (small variation injected via "if a member said X, weave it in")
- Member replies to any turn are awarded 1pt by `mc-award-responses` (separate plist, daily 23:50 PT)
- If a member's idea inspires the next day's encoding, that flows through `mc-idea-cta` → `mc-idea-encode-poll` (separate flow, not arc-bound)

## Cross-daemon summons (Ten-turn affordance)

If during Ten the day's daemon "summons" another daemon (e.g., Jvalion on a Wednesday gestures toward Humavita's earth-metabolism on a fire concept), that summons fires through `poll-summons.py` and may produce a webhook-relayed reply from the summoned daemon in the day's channel. Specified separately in Tier 5 P6.

## What's deferred

- **Sunday Nema-wrap structure** — different shape from Mon-Sat
- **Per-turn responsive generation** (vs upfront) — current Tier 5 builds upfront-only; responsive becomes Tier 6 if needed
- **Voice anchor library refinement** — Tier 5 P5 scaffolds; will iterate based on output quality
- **Arc-end cleanup / archival** — what happens to scene-state files after Ketsu posts? Move to `ledger/archive/scenes/<YYYY-MM>/`?

---

*Specification draft 2026-04-29. Original creative design lost in 2026-04-28 incident; this reconstruction proposes a working structure with inferences flagged for Daniel's refinement.*
