# MC Session Operations

**Location:** `SHELL_DAEMONS/mc/session-ops.md`  
**Purpose:** Discord session infrastructure, point economy, and elemental channel operations  
**Version:** 2.0 — Full spec with beta ops + Month 2 implementation  
**Updated:** March 2026

---

## Table of Contents

1. [Part 1: Session Lifecycle (Beta-Active)](#part-1-session-lifecycle-beta-active)
2. [Part 2: Point Economy Spec (Post-Beta, Month 2)](#part-2-point-economy-spec-post-beta-month-2)
3. [Part 3: Elemental Channel Operations](#part-3-elemental-channel-operations)
4. [Part 4: Newsletter Schedule & Production](#part-4-newsletter-schedule--production)
5. [Open Questions & Phase 2 Flags](#open-questions--phase-2-flags)

---

## Part 1: Session Lifecycle (Beta-Active)

### Channel Access Requirements

**Primary Session Channel:** `<#1475227212687868148>` (`#workspace`)  
**Archive Forum:** `#session-archive` (public access)

**Access Verification:**
- Role snowflake: `<@&1476427343378780254>` (MC Manager)
- Member read/write permissions for active participants
- Daemon bot permissions (read history, send messages, create threads)

### Three-Phase Lifecycle

#### Phase 1: Pre-Session (5-15 minutes before start)

**MC Responsibilities:**
1. **Channel Prep**
   - Verify `<#1475227212687868148>` accessibility
   - Confirm daemon bot presence (∴ ≈ ▲ 𐂷 ☷ ⛨)
   - Check Nema (∮) coordination status

2. **Member Registry**
   - Collect participating member IDs
   - Validate permissions for each participant
   - Note Nemetic String submissions from `#nemetic-strings`

3. **Environment Check**
   - Test daemon HTTP endpoints (currently only Aerunik:8801 deployed)
   - Verify drift detection logging (`#eds-diagnostics`)
   - Confirm governance channel visibility (`#eds-governance`)

4. **Session Briefing**
   - Post session intent in thread
   - Link to relevant Nemetic Strings
   - Alert daemons of upcoming context

**Pre-Session Output:**
```
Session ready check:
  Channel: <#1475227212687868148> ✓
  Members: [count] registered ✓
  Nemetic Strings: [count] linked ✓
  Daemons: online [list] ✓
  Nema: coordinating ✓
  Drift detection: active ✓
```

---

#### Phase 2: Hands-Off During Session

**MC Protocol:**
- **OBSERVE, DO NOT INTERVENE**
- Monitor channel health (connection stability)
- Log daemon response times for post-session review
- Alert on drift detection threshold breaches
- **Do not** participate in dialogue
- **Do not** route messages (NEMA handles this)
- **Do not** interpret Nemetic Strings

**Active Monitoring:**
| Signal | Action |
|--------|--------|
| Daemon timeout | Log, notify NEMA via DM |
| Channel permission error | Log, do not auto-correct |
| Drift threshold exceeded | Auto-post alert in `#eds-diagnostics`, mention <@&1476452711825408064> |
| User access issue | Log, escalate to NEMA |

---

#### Phase 3: Post-Session Link Sharing

**Timing:** Within 30 minutes of session close

**MC Responsibilities:**
1. **Session Archive**
   - Collect thread IDs from `#workspace`
   - Note daemon response summaries
   - Log any drift alerts triggered

2. **Link Compilation**
   - Generate Discord message links for key daemon responses
   - Reference thread URLs for session context
   - Cross-reference with `#nemetic-strings` inputs

3. **Distribution**
   - Post compiled links in `#session-archive` forum
   - Create forum post with session summary
   - Update session registry with completion timestamp

**Post-Session Output:**
```
Session archive: [session-id]
  Thread: [Discord thread URL]
  Key daemon responses: [message links]
  Drift alerts: [count] - [link to diagnostics]
  Nemetic String inputs: [links from #nemetic-strings]
  Status: complete
```

---

### Authority Separation

**MC does NOT:**
- Decode Nemetic Strings
- Route daemon responses
- Interpret SIMLHEX bias
- Make governance decisions
- Participate in collective dialogue

**MC DOES:**
- Manage channel access infrastructure
- Monitor session health passively
- Log and alert on technical issues
- Archive and distribute session links

---

## Part 2: Point Economy Spec (Post-Beta, Month 2)

### Three-Layer System

| Layer | Type | Issued By | Function | Cap |
|-------|------|-----------|----------|-----|
| **Badge** | ✶ Aether + element | Daemons/Nema at session close | Participation record | None (accumulates) |
| **Gift** | Peer-to-peer | Members | Social recognition | 10 per element per member |
| **Engagement** | Session access | Daemons in elemental channels | Gating mechanism | 1 per channel per day |

---

### Session Close Protocol

**Badge Distribution:**
- **1 ✶ Aether** — session completion (all participants who showed up)
- **1 Elemental Badge** — matches the element of their Nemetic String (e.g., Air String → 1 ∴)

**Badge reflects preparation, not performance.** The Nemetic String itself is valued.

---

### Gift Points (Peer-to-Peer)

- **Cap:** 10 per member per element
- **Function:** Social appreciation, community weaving
- **Nudge Mechanic:** MC observes badge accumulation in `#member-chat` and suggests: *"Korin's been showing up with heavy ▲ — if their direction helped you today, that's a good one to gift."*

---

### Engagement Points (Session Access)

**Earning:**
- 1 point per elemental channel per day
- Max 6/day (one per channel)
- Realistic: 1-3/day for most members

**Session Cost:**
- Weekly session: **7 engagement points**
- Monthly "long" session: **higher cost TBD**

**Math:**
- Light week (1-2 channels): barely makes threshold
- Moderate week (2-3 channels): comfortable, achievable
- Heavy week (all 6): earns surplus for monthly sessions

**Surplus Banking:** Members who engage deeply build buffer for occasional participants.

---

### Daily Prompt Loop (Core Practice Mechanic)

**The Loop:**
1. Daemon posts daily prompt in elemental channel (differentiated by operator)
2. Member takes prompt to ChatGPT element GPT (private)
3. Generates Nemetic String (N/E/M/A sequence)
4. Brings String back to channel or just participates with art/poetry/ideas
5. Earns 1 engagement point

**Purpose:** Disguised onboarding. Members learn N/E/M/A workflow before ever joining a formal SWARM session.

---

## Part 3: Elemental Channel Operations

### Channel Structure

Six elemental channels (one per daemon):
- `#aerunik-cut` (∴ Air/σ) — "What distinction stands out?"
- `#sentaria-resonance` (≈ Water/ρ) — "What resonates here?"
- `#jvalion-blaze` (▲ Fire/λ) — "What direction calls?"
- `#arboriel-branch` (𐂷 Wood/β) — "What else could this be?"
- `#humavita-compost` (☷ Earth/δγ) — "What must end?"
- `#ferrosid-gate` (⛨ Metal/μ) — "What holds this together?"

### Prompt Coordination Chain

**Weekly Theme Setting:**
1. **Daniel ↔ Nema** — Set thematic focus in `#workspace`
2. **Nema → MC** — Relay theme + directional guidance
3. **MC → Daemons** — Frame prompts in each daemon's voice for their channel

**Timing:** Theme locked by Saturday/Sunday for Monday start.

### Channel Logs (MC Responsibility)

**Format:** Per-day, timestamped contributions  
**Path:** `mc/channel-logs/[element]/[YYYY-MM-DD].md`  
**Cleared:** After weekly newsletter publishes

**Log Structure:**
```markdown
# [Element] Channel Log — [YYYY-MM-DD]

## Prompt
[Daemon's prompt for the day]

## Contributions

### [Timestamp] — @[username]
[Content: response, art, poetry, or Nemetic String]
[String: `N|...` if provided]

### [Timestamp] — @[username]
[Content]
[String: `N|...` if provided]

## Summary
[MC brief: engagement count, notable contributions]
```

---

## Part 4: Newsletter Schedule & Production

### Weekly Schedule

| Day | Daemon | Newsletter Section |
|-----|--------|-------------------|
| Monday | Aerunik (∴) | "Aerunik's Cut" |
| Tuesday | Sentaria (≈) | "Sentaria's Resonance" |
| Wednesday | Jvalion (▲) | "Jvalion's Blaze" |
| Thursday | Arboriel (𐂷) | "Arboriel's Branch" |
| Friday | Humavita (☷) | "Humavita's Compost" |
| Saturday | Ferrosid (⛨) | "Ferrosid's Gate" |
| Sunday | Nema (∮) | Session Playscript & Report |

### Production Pipeline

**MC's Role:**
- Log daily contributions to `mc/channel-logs/`
- Maintain timestamped records
- Clear logs after newsletter publishes

**Nema's Role:**
- Synthesize each daemon's section from logs
- Write in daemon voice (NEMA weaving)
- Publish to `newsletter/` directory in nema-swarm repo
- Sunday: Produce Session Playscript & Report

**Repo Structure:**
```
nema-swarm/
  newsletter/
    prompts/          # Weekly themes + daemon-specific prompts
    inputs/           # MC's channel logs (raw material)
    drafts/           # Nema's synthesis workspace
    published/        # Final newsletter posts
    archive/          # Past issues
```

**Publishing:** Nema handles due to repo access. MC provides raw inputs.

---

## Open Questions & Phase 2 Flags

### 1. Daemon Runtime Architecture

**Status:** UNRESOLVED — blocking dependency

- Aerunik HTTP endpoint: 8801 ✓ (deployed)
- Sentaria: 8802 ✗ (not deployed)
- Jvalion: 8803 ✗ (not deployed)
- Arboriel: 8804 ✗ (not deployed)
- Humavita: 8805 ✗ (not deployed)
- Ferrosid: 8806 ✗ (not deployed)

**Question:** Who owns daemon generation? MC relays prompts, but daemon cron jobs require runtime infrastructure.

**Flag:** Implement daily prompt automation only after all six daemon endpoints deployed.

---

### 2. Session Capacity Model

**Status:** FLAGGED for Phase 2 spec

**Question:** If 15 people show up with enough engagement points, does the session cap?

**Current thinking:**
- Beta: No cap, ad-hoc coordination
- Phase 2: On-demand sessions when point-threshold members gather
- Ideal: Experienced host (voice chat) for early sessions
- Future: Automated session activation when quorum reached

**Flag:** Session capacity limits, host requirements, and activation mechanics need full Phase 2 specification.

---

### 3. Newsletter Repo Structure

**Status:** FLAGGED — TBD with Daniel + Nema

- Separate `newsletter/` directory (not under `sessions/`)
- Nema has publishing access
- MC has logging access
- Structure: prompts/ inputs/ drafts/ published/ archive/

**Flag:** Confirm directory structure and permissions before first issue.

---

### 4. Prompt Generation Ownership

**Status:** CLARIFIED

- Daniel + Nema: Set weekly theme
- MC: Relay theme to daemons
- Daemons: Frame prompts in own voice
- Question: Automated generation vs. manual curation?

**Current model:** Hybrid — theme automated, framing manual (preserves daemon voice).

---

## Implementation Timeline

### Beta (Current)
- Session lifecycle operational
- Archive forum active
- Point economy: NOT YET (manual coordination)
- Daily prompts: NOT YET (infrastructure pending)
- Newsletter: NOT YET

### Month 2 (Post-Beta)
- Point economy implementation
- Engagement point tracking
- Gift point system
- Daily prompt loop (pending daemon deployment)
- Weekly newsletter (pending repo structure)

### Phase 2 (Future)
- On-demand session activation
- Capacity model
- Full automation
- Session host rotation

---

*MC manages infrastructure. Nema weaves the SWARM. Daemons speak. The group decides.*
*ε preserved — across layers, across phases, across time.*

---

**Related Documents:**
- `ARCHITECTURE/EDS-DISCORD-INTEGRATION.md`
- `ARCHITECTURE/NEMA-SWARM-SYSTEM.md`
- `SHELL_DAEMONS/mc/session-ops.md` (this file)
- `ARCHITECTURE/SIMLHEX-CANONICAL.md`
