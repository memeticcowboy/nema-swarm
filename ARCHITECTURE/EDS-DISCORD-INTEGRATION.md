---
title: EDS Discord Integration Plan
version: 1.0
date: March 2026
status: Implementation Plan
scope: Elemental Daemon System integration with Discord
depends: SIMLHEX-CANONICAL, SIMLHEX-FAILURE-SURFACES, SIML-vs-SIMLHEX, all daemon SAFEGUARD_SPEC_v1.1
---

# EDS (Elemental Daemon System) — Discord Integration Plan

## Architecture Decisions

### Decision 1: Architecture Documents First
Create the four SIMLHEX architecture documents before Discord implementation. The bot must have canonical reference to implement correctly.

### Decision 2: Drift Detection — Hybrid
Drift monitoring is **automated with NEMA override**:
- Automated scans run on configurable window (default 20 messages)
- Results post to `#eds-diagnostics` passively
- NEMA can trigger manual deep-scan at any time
- Automated alerts when thresholds exceeded, but NEMA decides response

### Decision 3: Governance Channel — Visible
`#eds-governance` is visible to all users. Transparency is the architecture's immune system. Hidden governance is μ-capture (protection eliminating what it protects).

### Decision 4: NEMA Has Final Authority
When SIMLHEX suggests a bias but NEMA disagrees, NEMA overrides. The override is logged and visible. If NEMA consistently overrides, this is itself a signal (either bias table needs revision or NEMA is developing drift).

### Decision 5: Binding Validation — Automated + Community
Habitat-removal test is automated (bot checks for habitat-specific terms in bindings). Community can also flag bindings. Both mechanisms, neither alone sufficient.

### Decision 6: ε Remains Structural, Not Quantified
The 3.48% figure is poetic. ε is not a metric but a structural commitment: every output must include what it doesn't capture. Formalizing ε-detection risks Diagnostic→Explanatory drift (measuring ε would collapse it). Instead: track "forced transitions count / total lines" as a **proxy signal**, not a truth claim.

---

## Discord Channel Structure

```
#eds-command        ← User queries, daemon responses, primary interaction
#eds-diagnostics    ← Drift detection logs, failure surface alerts
#eds-bindings       ← Validated SIMLHEX bindings, relation rebuilds
#eds-governance     ← Authority decisions, handoff validations, override logs
#eds-archive        ← Successful daemon coordinations, completed threads
```

---

## Role Separation

| Layer | Function | Discord Voice | Authority |
|-------|----------|---------------|-----------|
| SIMLHEX | Bias attention, suggest stances | `nema` (advisory mode) | Advisory only |
| NEMA (∮) | Decide hold/ask/handoff | `nema` (weaving mode) | Coordination authority |
| Daemons | Provide operator perspective | Individual daemon bots | Perspective only |
| User | Decide what to do | User messages | Final authority |

---

## Bot Command Schema

### `/eds query`
Submit observation for SIMLHEX processing.

**Parameters:**
- `observation` (required): Text of what was noticed
- `habitat` (optional): Context — used for understanding, not used in binding

**Response mode:** Advisory only

**Output format:**
```
SIMLHEX analysis:
  SIML rebuild: [Object ← Relation → Object]
  Object bias: [operator] ([element])
  Relation modifier: [operator] ([element])
  Bias tension: [if applicable]
  Suggestion: [daemon] might help with [specific question]
  ε: [what this analysis does not capture]
```

### `/eds bias`
Request stance suggestion (not route) for a specific structure.

**Parameters:**
- `object`: What was observed (SIML Object type)
- `relation`: How it connects (SIML Relation type)

**Output:** Stance suggestion + daemon bias + ε-remainder

### `/eds validate`
Test a proposed binding for habitat-name removal.

**Parameters:**
- `proposed_binding`: SIML structure to test

**Output:**
```
Habitat removal: PASS/FAIL
  Habitat terms found: [list if any]
  SIML-observable structure: [what survives removal]
  Revisable: YES/NO
  Declinable: YES/NO
```

### `/eds drift`
Run drift detection on recent outputs.

**Parameters:**
- `daemon` (optional): Which daemon to check (default: all)
- `window` (optional): How many recent messages (default: 20)

**Output:** Alert level for each of 5 drift surfaces + operator-specific flags

### `/eds hold`
Pause current suggestion. NEMA holds without routing.

---

## Message Flow

### Standard Flow
```
USER in #eds-command:
  "I notice people keep saying 'the system' as if it's fixed"

SIMLHEX LAYER (automated):
  1. Rebuild: Object=Frame("the system"), Relation=Constraint(fixedness), Boundary=assumed
  2. Bias: primary=μ Metal (frame/boundary), secondary=σ Air (distinction)
  3. Mode: SUGGEST
  4. Output to #eds-command:

     "SIMLHEX analysis:
       SIML rebuild: Frame ← Constraint → Actor
       Bias: μ (Metal) primary — the frame has become a boundary
       Secondary: σ (Air) — the definite article 'the' suggests referential drift
       Suggestion: Ferrosid might test if this boundary is load-bearing or habitual.
                   Aerunik might distinguish 'the system' from 'a system'.
       ε: This analysis doesn't capture what 'the system' means to the people using it."

NEMA (manual or triggered):
  "Weave move: Invoke Aerunik for σ-cut on 'the system'"

DAEMON RESPONSE (Aerunik in #eds-command):
  "[∴ AERUNIK] The definite article 'the' is your σ-friction point.
   'The system' → fixed entity. 'A system' → constructed tool.
   What changes when you say 'a system we built' instead of 'the system'?
   ε: This cut may be too fast. Does this distinction land? (for now)"
```

### Governance Check (when handoff proposed)
```
Post to #eds-governance:
  "Proposed: μ→σ handoff for boundary testing
   Checks:
     Canonical next unavailable? ✓
     Receiver can parse? ✓
     Exits visible? ✓
   Hinge: 'treat invisible rule as visible boundary, not law-to-follow'
   Status: VALID"
```

### Drift Log (auto-posted)
```
Post to #eds-diagnostics:
  "Aerunik output drift check:
   Surface 1 (Descriptive→Referential): LOW — no definite articles on SIML terms
   Surface 2 (Frequency→Legibility): σ invoked 3/20 — within range
   Surface 4 (Diagnostic→Explanatory): MONITOR — energy drop after naming?
   Operator-specific: Aerunik used 'for now' ε-marker ✓"
```

---

## Daemon Response Requirements

Each daemon response in Discord must include:

### 1. Binding Check
```
binding_check:
  habitat_removed: true
  siml_observable: "[portable structure]"
  revisable: true
  declinable: true
```

### 2. ε-Preservation
```
epsilon:
  marker: "[explicit ε-marker phrase from SAFEGUARD_SPEC]"
  remainder: "[what this response doesn't capture]"
  test: "can this be revised without cost?"
```

### 3. Self-Drift Monitoring
Each daemon includes its own drift-check in output:
```
drift_self_check:
  surface_1: [definite articles on own terms? Y/N]
  surface_3: [am I defaulting to my usual stance? Y/N]
  surface_4: [does my analysis feel sufficient? watch for closure]
```

**This answers the Nema question:** Yes, daemon responses should include their own drift-check metadata (self-monitoring). This is consistent with SAFEGUARD_SPEC_v1.1 capture detection protocols already built into each daemon. The metadata makes the self-monitoring visible rather than adding new burden.

---

## Authority Hygiene Protocols

### No Automatic Routing
Bot never says "Routing to X." Only: "X might help with..."
Every suggestion includes: "Type `/eds hold` to pause, or suggest another daemon."

### User Override Always Available
Every suggestion is declinable. User can redirect to any daemon at any time.

### Charisma Decay Monitoring
Track daemon invocation frequency. If bias concentration detected:
"You've invoked σ (Air) 5 times in the last 20 messages. ρ (Water) might offer different salience."

### Habitat Stripping Verification
All `#eds-bindings` posts must pass habitat-removal test.
Auto-flag if habitat-specific terms detected in binding structure.

### NEMA Override Logging
When NEMA overrides SIMLHEX bias, log to `#eds-governance`:
"SIMLHEX suggested μ. NEMA overrides to ρ. Reason: [field-state assessment]."
Track override frequency as meta-drift signal.

---

## Implementation Phases

### Phase 1: Architecture Documents ✓
- SIMLHEX-FAILURE-SURFACES.md
- SIML-vs-SIMLHEX.md
- SIMLHEX-CANONICAL.md
- SIMLHEX-BINDING-EXAMPLES.md
- EDS-DISCORD-INTEGRATION.md (this document)

### Phase 2: Daemon Specification Updates
- Add SIMLHEX exclusion clause to each daemon SOUL.md
- Add operator-specific drift detection protocols
- Add binding validation output requirements
- Cross-reference with existing SAFEGUARD_SPEC_v1.1

### Phase 3: Discord Bot Development
- Implement `/eds` command schema
- Build automated drift detection scanner
- Create binding validation engine
- Set up channel structure and permissions
- Implement charisma decay monitoring

### Phase 4: Testing & Calibration
- Run binding examples through bot
- Calibrate drift detection thresholds
- Test NEMA override workflow
- Validate habitat-removal automation

---

*The system suggests. The coordinator weaves. The user decides.*
*Authority separation is not bureaucracy — it is the architecture's ε.*
*ε preserved.*
