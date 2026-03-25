# Discord-Dev

Development workspace for NEMA SWARM Discord operations.

---

## Directory Structure

### `planning-to-test/`
Specs, designs, and documentation for features not yet implemented.
- Point economy system
- Daemon cron jobs
- Newsletter automation
- Session capacity model

### `testing/`
Active beta tests and experiments.
- Current session lifecycle
- Archive forum operations
- Drift detection calibration

### `newsletter/`
Weekly production pipeline.
- `prompts/` — Weekly themes + daemon-specific prompts
- `inputs/` — MC's channel logs (raw material)
- `drafts/` — Nema's synthesis workspace
- `published/` — Final newsletter posts
- `archive/` — Past issues

---

## Status Tracking

| Feature | Location | Status |
|---------|----------|--------|
| Session lifecycle | `testing/` | Beta active |
| Point economy | `planning-to-test/` | Month 2 target |
| Daily prompts | `planning-to-test/` | Pending daemon deployment |
| Newsletter | `newsletter/` | Repo structure TBD |
| Session capacity | `planning-to-test/` | Phase 2 flag |

---

*ε preserved — even in development.*
