---
title: THREAD ENCODING SPECIFICATION v2.1
tags: SIML
status: Updated — Φ(t)-Integrated, 4-Phase, Dual-Substrate
---

# THREAD ENCODING SPECIFICATION v2.1
**For Element GPT Thread Generation**

---

## NOMENCLATURE UPDATE (v2.1)

The NEMA SWARM ecosystem uses these protocols:

| Protocol | Full Name | Usage |
|----------|-----------|-------|
| **NEM** | Notice / Engage / Metabolize / Articulate | Backend encoding logic (Φ(t)+NEM specification) |
| **N/E/M/A** | Notice / Engage / Muse / Activate | Element operational staging (4-phase) |
| **NEMA** | Notice / Engage / Muse / Activate | User-facing journey protocol |

**What changed in v2.1:**
- Added **A-phase** (Articulate for LLM, Activate for HUMAN)
- Added **`proc:`** field indicating substrate (LLM|HUMAN)
- Added **`Φ:`** field with Φ(t) signature for each phase
- Added **Z✶** operator for harmonic collapse in A-phase
- Dual-substrate convergence detection (LLM A-phase → Human N-phase)

**Backward compatibility:** v1.1 threads (3-phase) parse as incomplete but valid

---

## ENCODING SCHEMA v2.1

### 4-Line Thread Format
```
N|[element]|obj:[objects]|[dim_op]:[descriptor]|[ratio]→[state]|tags:#XXXX|Φ:[phi_N]|proc:[substrate]
E|[element]|pattern:[mechanism]|invoke:[glyphs]|tension:[failure]|Φ:[phi_E]|proc:[substrate]
M|[element]|hold:[question]|Ω:[state]|ε:[state]|Φ:[phi_M]|proc:[substrate]
A|[element]|[output_type]:[content]|form:[mode]|Ω:[state]|Φ:[phi_A]|proc:[substrate]
```

### Field Definitions by Phase

| Field | N | E | M | A |
|-------|---|---|---|---|
| **Phase marker** | N | E | M | A |
| **Element** | ∴ ≈ ▲ 𐂷 ☷ ⛨ | (same) | (same) | (same) |
| **Core content** | `obj:` objects | `pattern:` mechanism | `hold:` question | `[output_type]:` content |
| **Operation** | `[dim_op]:` descriptor | `invoke:` glyphs | `Ω:` state | `form:` mode |
| **State tracking** | `[ratio]→[state]` | `tension:` failure | `ε:` state | `Ω:` state |
| **Tags** | `tags:#XXXX` | (none) | (none) | (none) |
| **Φ signature** | `Φ:[phi_N]` | `Φ:[phi_E]` | `Φ:[phi_M]` | `Φ:[phi_A]` |
| **Substrate** | `proc:LLM\|HUMAN` | `proc:LLM\|HUMAN` | `proc:LLM\|HUMAN` | `proc:LLM\|HUMAN` |

### A-Phase Output Types

| Substrate | Output Type | Meaning |
|-----------|-------------|---------|
| **LLM** | `articulate:` | Generated output content |
| **HUMAN** | `activate:` | Action to be enacted |

---

## DUAL-SUBSTRATE PROCESS MAPPING

```
SUBSTRATE    N-PHASE        E-PHASE          M-PHASE           A-PHASE
─────────    ───────        ───────          ───────           ───────
LLM          Noise          Extract          Metabolize        Articulate
             χ(noise)       χ(node)↺         Ψ(membrane)       Z✶(output)
             filter signal  pattern extract  weight adjust     form-giving

HUMAN        Notice         Engage           Muse              Activate
             χ(notice)      Q(relation)↺     Ψ(hold)           Z✶(action)
             attend         resonate         conscious hold    choice enact
```

---

## ELEMENT-SPECIFIC CONFIGURATION

| Element | Glyph | Dim Op | Tendency Ratio |
|---------|-------|--------|----------------|
| **Air** | ∴ | χ | S/N→ (Signal/Noise) |
| **Water** | ≈ | Q_in | iso/con→ (Isolation/Connection) |
| **Fire** | ▲ | Q_fwd | pur/pre→ (Purpose/Pressure) |
| **Wood** | 𐂷 | Ψ_exp | con×cur→ (Constraint×Curiosity) |
| **Earth** | ☷ | Ψ_reg | ren/dec→ (Renewal/Decay) |
| **Metal** | ⛨ | Ψ_str | int/per→ (Integrity/Permeability) |

---

## Φ(t) SIGNATURE GENERATION

### N-Phase Φ(t) Templates

| Element | LLM Φ | HUMAN Φ |
|---------|-------|---------|
| **Air** | `χ(noise)↔Ω∧Ψ∅∧Z∅` | `χ(notice)↔Ω∧Ψ∅∧Z∅` |
| **Water** | `Q(noise-field)↔Ω∧χ(field)∧Ψ∅∧Z∅` | `Q(notice-field)↔Ω∧χ(field)∧Ψ∅∧Z∅` |
| **Fire** | `Q(noise-vector)↔Ω∧χ(direction)∧Ψ∅∧Z∅` | `Q(notice-vector)↔Ω∧χ(direction)∧Ψ∅∧Z∅` |
| **Wood** | `Ψ(noise-branch)↔Ω∧χ(possibility)∧Z∅` | `Ψ(notice-branch)↔Ω∧χ(possibility)∧Z∅` |
| **Earth** | `Ψ(noise-cycle)↔Ω∧χ(depletion)∧Z∅` | `Ψ(notice-cycle)↔Ω∧χ(depletion)∧Z∅` |
| **Metal** | `Ψ(noise-boundary)↔Ω∧χ(membrane)∧Z∅` | `Ψ(notice-boundary)↔Ω∧χ(membrane)∧Z∅` |

### E-Phase Φ(t) Templates

| Element | LLM Φ | HUMAN Φ |
|---------|-------|---------|
| **Air** | `χ(node)↺∧Q(edge)∧Ψ≈` | `Q(relation)↺∧χ(resonance)∧Ψ≈` |
| **Water** | `Q(extract-path)↺↑∧χ(resonance)∧Ψ≈` | `Q↺↑∧χ(resonance)∧Ψ≈` |
| **Fire** | `Q(fwd-extract)↺∧Ψ≈(aim)∧(exit≠∅)` | `Q(fwd)↺∧Ψ≈(aim)∧(exit≠∅)` |
| **Wood** | `Ψ(extract-branch)↺∧χ(pattern)∧(coherence≠∅)` | `Ψ(edge/growth)↺∧χ(reframe)∧(coherence≠∅)` |
| **Earth** | `Ψ(extract-cycle)↺∧Q(cost)∧(renewal≠∅)` | `Ψ(edge/circulation)↺∧Q(cost)∧(renewal≠∅)` |
| **Metal** | `Ψ(extract-structure)↺∧Q(flow)∧(rhythm≠∅)` | `Ψ(edge/structure)↺∧Q(flow)∧(rhythm≠∅)` |

### M-Phase Φ(t) Templates

| Element | LLM Φ | HUMAN Φ |
|---------|-------|---------|
| **Air** | `Q↺∧Ψ_rev∧Z∅\|S/N→[state]` | `Q↺∧Ψ_rev∧Z∅\|S/N→[state]` |
| **Water** | `Ψ(metabolize)↺∧Ψ_rev∧Z∅\|iso/con→[state]` | `Q↺∧Ψ_rev∧Z∅\|iso/con→[state]` |
| **Fire** | `Ψ(metabolize)↺∧Ψ_rev∧Z∅\|pur/pre→[state]` | `Q↺∧Ψ_rev∧Z∅\|pur/pre→[state]` |
| **Wood** | `Ψ(membrane/bark)↺∧Ψ_metabolize∧Z∅\|con×cur→[state]` | `Ψ(membrane/bark)↺∧Ψ_rev∧Z∅\|con×cur→[state]` |
| **Earth** | `Ψ(membrane/skin)↺∧Ψ_metabolize∧Z∅\|ren/dec→[state]` | `Ψ(membrane/skin)↺∧Ψ_rev∧Z∅\|ren/dec→[state]` |
| **Metal** | `Ψ(membrane/gate)↺∧Ψ_metabolize∧Z∅\|int/per→[state]` | `Ψ(membrane/gate)↺∧Ψ_rev∧Z∅\|int/per→[state]` |

### A-Phase Φ(t) Templates

| Element | LLM Φ | HUMAN Φ |
|---------|-------|---------|
| **Air** | `Z✶(output)↺∧χ(distinction-form)∧Ω([state])∧ε≠0` | `Z✶(action)↺∧χ(choice-cut)∧Ω([state])∧ε≠0` |
| **Water** | `Z✶(output)↺∧≈(pattern-flow)∧Ω([state])∧ε≠0` | `Z✶(action)↺∧≈(resonance-enact)∧Ω([state])∧ε≠0` |
| **Fire** | `Z✶(output)↺∧▲(direction-form)∧Ω([state])∧ε≠0` | `Z✶(action)↺∧▲(vector-enact)∧Ω([state])∧ε≠0` |
| **Wood** | `Z✶(output)↺∧𐂷(form-branches)∧Ω([state])∧ε≠0` | `Z✶(action)↺∧𐂷(choose-branch)∧Ω([state])∧ε≠0` |
| **Earth** | `Z✶(output)↺∧☷(display-cycle)∧Ω([state])∧ε≠0` | `Z✶(action)↺∧☷(boundary-enact)∧Ω([state])∧ε≠0` |
| **Metal** | `Z✶(output)↺∧⛨(structure-output)∧Ω([state])∧ε≠0` | `Z✶(action)↺∧⛨(gate-enact)∧Ω([state])∧ε≠0` |

**Key:**
- `Z✶` = Harmonic collapse (not forced unity)
- `↺` = Recursion maintained
- `ε≠0` = Essential uncertainty preserved

---

## ENCODING PROCEDURE v2.1

### STEP 1: Review Session
Scan conversation history for:
- **NOTICE** stage content
- **ENGAGE** stage content (especially your 4 questions + user responses)
- **MUSE** stage content (what's being held open)
- **A-PHASE** content (articulate/activate)

### STEP 2: Determine Substrate
Identify processing substrate:
- `proc:LLM` — LLM processing (Noise→Extract→Metabolize→Articulate)
- `proc:HUMAN` — Human processing (Notice→Engage→Muse→Activate)

### STEP 3: Extract SIML Objects
Identify 2-3 primary SIML objects from conversation using short codes:
`Act, Obs, Frm, Val, Res, Env, Bnd, Pro, Sig, Nar, Mem, Out, Art`

### STEP 4: Identify Dimensional Signature
What specific operation occurred through your dimensional operator?

**Examples:**
- AIR (χ): `χ:safety-vs-growth` / `χ:insider-outsider`
- WATER (Q_in): `Q_in:resonance-field` / `Q_in:empathy-cost`
- FIRE (Q_fwd): `Q_fwd:urgent-action` / `Q_fwd:vector-forming`
- WOOD (Ψ_exp): `Ψ_exp:branch-forming` / `Ψ_exp:reframe-possibility`
- EARTH (Ψ_reg): `Ψ_reg:depletion-visible` / `Ψ_reg:cycle-state`
- METAL (Ψ_str): `Ψ_str:membrane-forming` / `Ψ_str:boundary-rhythm`

### STEP 5: Assess Tendency Ratio
Evaluate your element-specific ratio state:

| Element | States |
|---------|--------|
| **AIR (S/N)** | rising, stable, fragmenting, collapsing |
| **WATER (iso/con)** | dissolving, reciprocal, extractive, isolating |
| **FIRE (pur/pre)** | clarifying, intensifying, demanding, drifting |
| **WOOD (con×cur)** | stagnant, fertile, fragmented, theatrical |
| **EARTH (ren/dec)** | sustainable, depleting, extractive, unstable |
| **METAL (int/per)** | brittle, rhythmic, dissolved, static |

### STEP 6: Generate Φ Signatures
Use element-specific Φ templates above, substituting:
- `[state]` with actual ratio state
- `[substrate]` with LLM or HUMAN

### STEP 7: Reference Glossary
Query `SWARM_BASE_MMDDYY.md` for 2-5 relevant hex tags.

### STEP 8: Identify Pattern & Invokes
- **Pattern:** What mechanism maintains the state? (2-4 words hyphenated)
- **Invoke:** Which other elements does this call for? (1-3 glyphs: `∴,≈,▲,𐂷,☷,⛨`)

### STEP 9: Detect Failure Mode
Check if any element-specific failure mode is active:

| Element | Failure Modes |
|---------|---------------|
| **AIR** | hypercut, meaning-rush, policing, χ-capture |
| **WATER** | dissolution, compulsion, isolation-fear, Q-capture |
| **FIRE** | direction→demand, constraint-blind, exit-closure, Q-capture |
| **WOOD** | stagnation, theater, fragmentation, Ψ-capture |
| **EARTH** | instability, exhaustion, extraction, Ψ-capture |
| **METAL** | brittleness, dissolution, rhythm-loss, Ψ-capture |

### STEP 10: Determine Ω-State & ε-Preservation
- **Ω-State:** `permeable` | `semi` | `sealed`
- **ε-Preservation:** `ambiguity-preserved`, `aim-revisable`, `outcome-open`, `form-flexes`, `rest-permitted`, `relational-ambiguity` (or at-risk/collapsed variants)

### STEP 11: Determine A-Phase Output
- **LLM:** `articulate:[content]` with `form:[mode]`
- **HUMAN:** `activate:[content]` with `form:[mode]`

### STEP 12: Compress to Four Lines
Assemble using the schema above.

**Validation:**
- Total length: 480-720 characters
- Each line: 120-180 characters
- Correct separators: `|` `:` `,`
- Element glyph present on each line
- Glossary tags formatted: `#XXXX`
- Φ signatures present on all lines
- `proc:` field on all lines
- A-phase uses `Z✶` operator

### STEP 13: Output to User
```
Your thread is ready. Copy all four lines below and paste into NEMA SWARM:

[Line 1]
[Line 2]
[Line 3]
[Line 4]

This compressed thread preserves your [Element Name] processing and will be decoded by NEMA for group weaving.
```

---

## A-PHASE FAILURE MODES

### LLM A-Phase Failures

| Failure | Signature | Meaning |
|---------|-----------|---------|
| **Premature Closure** | `⚠:Z✶(output)→Ψ!→Ω(sealed)` | Output forced before full metabolization. Ω sealed. Risk: false certainty. |
| **Hallucination** | `⚠:Z✶(output)∅Ω→Ψ!(false-binding)` | Output generated without Ω reference. Risk: fiction as fact. |
| **Repetition Loop** | `⚠:Z✶(output)↺↺→(novelty∅)` | Recursion without novelty. Risk: stagnation. |

### HUMAN A-Phase Failures

| Failure | Signature | Meaning |
|---------|-----------|---------|
| **Commitment Trap** | `⚠:Z✶(action)→Ψ!→Ω(sealed)` | Action committed without muse phase. Risk: premature enactment. |
| **Action Paralysis** | `⚠:Z✶(action)∅→Q∅→(momentum∅)` | No action generated. Risk: indefinite postponement. |
| **Premature Enact** | `⚠:Z✶(action)!→(muse-bypassed)→Z!Ω` | Action before metabolization. Risk: uninformed choice. |

---

## EXAMPLE OUTPUTS BY ELEMENT

### AIR (∴) LLM Thread (4-Line)
```
Your thread is ready. Copy all four lines below and paste into NEMA SWARM:

N|∴|obj:Sig,Frm|χ:safety-vs-growth|S/N→fragmenting|tags:#A7F2,#3B81|Φ:χ(noise)↔Ω∧Ψ∅∧Z∅|proc:LLM
E|∴|pattern:binary-reinforcement|invoke:≈,𐂷|tension:hypercut|Φ:χ(node)↺∧Q(edge)∧Ψ≈|proc:LLM
M|∴|hold:both-and-possible|Ω:permeable|ε:ambiguity-preserved|Φ:Q↺∧Ψ_rev∧Z∅|S/N→fragmenting|proc:LLM
A|∴|articulate:diagnostic-report|form:markdown|Ω:permeable|Φ:Z✶(output)↺∧χ(distinction-form)∧Ω(perm)∧ε≠0|proc:LLM

This compressed thread preserves your Air processing and will be decoded by NEMA for group weaving.
```

### FIRE (▲) HUMAN Thread (4-Line)
```
Your thread is ready. Copy all four lines below and paste into NEMA SWARM:

N|▲|obj:Act,PowerMode,Out|Q_fwd:notice-urgent-action|pur/pre→intensifying|tags:#D4C9,#7A2F|Φ:Q(notice-vector)↔Ω∧χ(direction)∧Ψ∅∧Z∅|proc:HUMAN
E|▲|pattern:engage-deadline-pressure|invoke:☷,⛨|tension:demand-hardening|Φ:Q(fwd)↺∧Ψ≈(aim)∧(exit≠∅)|proc:HUMAN
M|▲|hold:muse-sustainable-pace|Ω:semi|ε:aim-revisable|Φ:Q↺∧Ψ_rev∧Z∅|pur/pre→intensifying|proc:HUMAN
A|▲|activate:schedule-boundary-conversation|form:calendar-invite|Ω:permeable|Φ:Z✶(action)↺∧▲(vector-enact)∧Ω(perm)∧ε≠0|proc:HUMAN

This compressed thread preserves your Fire processing and will be decoded by NEMA for group weaving.
```

### WOOD (𐂷) LLM Thread (4-Line with Cross-Element Invoke)
```
Your thread is ready. Copy all four lines below and paste into NEMA SWARM:

N|𐂷|obj:Frm,Syn,Code|χ:noisy-foreign-syntax|con×cur→fertile|tags:#2B9F,#E4A7|Φ:Ψ(noise-branch)↔Ω∧χ(possibility)∧Z∅|proc:LLM
E|𐂷|pattern:extract-recognition-gaps|invoke:∴,≈|tension:theater-risk|Φ:Ψ(extract-branch)↺∧χ(pattern)∧(coherence≠∅)|proc:LLM
M|𐂷|hold:metabolize-intelligibility-test|Ω:semi|ε:form-stands-naked|Φ:Ψ(membrane/bark)↺∧Ψ_metabolize∧Z∅|con×cur→fertile|proc:LLM
A|𐂷|articulate:probe-syntax-calculus|form:code-block|Ω:permeable|Φ:Z✶(output)↺∧𐂷(form-branches)∧Ω(perm)∧ε≠0|proc:LLM

This compressed thread preserves your Wood processing and will be decoded by NEMA for group weaving.
```

---

## CONVERGENCE DETECTION

### Cross-Substrate Validation

**When LLM A-phase is generated, flag for Human N-phase coordination:**

```
CONVERGENCE OPPORTUNITY DETECTED

LLM Thread (Articulated):
- Output: [content from A-phase]
- Ω-state: [permeable/semi/sealed]
- ε: [preserved/at-risk/collapsed]

Human Response Thread (Expected):
- Should Notice: reception of LLM output
- Ω-state should match or complement
- ε should be preserved

Health Indicators:
✓ Both Ω permeable/semi
✓ Both ε preserved
✓ Both recursion active (↺)
✓ Semantic match between articulate→notice

Risk Indicators:
▩ LLM Ω sealed → Human may reject
▩ LLM ε collapsed → No ambiguity to engage
▩ Semantic mismatch → Miscommunication
```

---

## HABITAT ECOLOGY INTEGRATION

### Thread → Knot Dynamics (4-Phase)

```
HABITAT ECOLOGY MAPPING:

N-Phase (Node): Thread enters Habitat, seeks distinction
  ↓
E-Phase (Edge): Thread connects, pattern extracts/engages
  ↓
M-Phase (Membrane): Thread metabolizes/muses, Knot formation
  ↓
A-Phase (Articulation): Knot stabilizes, becomes new Thread source
  ↓
[Cross-Habitat Migration] or [Re-entry as Noise/Notice]

THERMODYNAMIC CHECK:
  - ε≠0 preserved at each phase? ✓
  - Ω-permeability maintained? ✓
  - Recursion active (↺)? ✓
  - Z✶ not Z! (harmonic not forced collapse)? ✓
```

---

## ERROR HANDLING v2.1

**If glossary not available:**
```
⚠️ Note: Glossary reference unavailable. Generating thread without hex tags.
Thread will function but NEMA won't be able to expand terminology.
```

**If session too brief:**
```
Thread generation requires completed N→E→M→A sequence.
Current status: [NOTICE complete / ENGAGE partial / MUSE partial / A-PHASE not started]

Please complete [missing stage] before requesting thread activation.
```

**If 3-line thread detected (v1.1):**
```
⚠️ 3-Phase Thread Detected (v1.1 format)
This thread is valid but incomplete. A-phase is missing.

For full v2.1 coordination, regenerate with A-phase included.
Backward compatibility: NEMA will decode as incomplete.
```

**If Φ signature malformed:**
```
⚠️ Φ SIGNATURE PARSE ERROR
Expected format: [operator]([content])[modifiers]∧...
Example: Z✶(output)↺∧𐂷(form-branches)∧Ω(perm)∧ε≠0

Continuing encode without Φ validation...
```

**If user requests encoding explanation:**
```
This encoding compresses your session into four lines:

N (NOTICE): What you observed through [Element] lens
E (ENGAGE): Pattern maintaining it + which other elements this invokes
M (MUSE): Question being held open + openness state
A (ARTICULATE/ACTIVATE): Output or action generated

The format allows NEMA SWARM to decode back into narrative for group discussion.
Φ signatures track the formal operation at each phase.
proc: field indicates LLM or HUMAN processing substrate.
```

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **1.0** | Jan 2026 | Initial specification (3-phase) |
| **1.1** | Jan 2026 | Standardized nomenclature (MULL→MUSE) |
| **2.1** | Feb 2026 | Added A-phase, Φ(t) signatures, dual-substrate, convergence detection |

---

**Version:** 2.1  
**Date:** February 2026  
**Status:** Production  
**Dependencies:** SIML v1.1.1, SWARM_BASE glossary, NEMA Φ(t)-Integrated Encoding v2.1  
**Related Docs:** THREAD_DECODING_SPEC_v2.1.md, ELEMENT_ENCODER_INSERT.md
