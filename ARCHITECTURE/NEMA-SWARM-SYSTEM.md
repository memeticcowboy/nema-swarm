---
title: NEMA SWARM System Architecture
version: 1.0
date: March 2026
status: Canonical
scope: End-to-end flow from individual element sessions through collective SWARM coordination
depends: SIMLHEX-CANONICAL, SIML-vs-SIMLHEX, THREAD_ENCODING_SPEC_v2_2, THREAD_DECODING_SPEC_v2_2, Elemental_Daemons_Canonical_v3.0
---

# NEMA SWARM — System Architecture

## Overview

NEMA SWARM is a multi-agent system for collective sensemaking. It operates in two phases:

1. **Individual element sessions** — Users work privately with nameless elemental GPTs in ChatGPT, led through generative dialogue based on principles of meta-relationality
2. **Collective SWARM sessions** — Users bring their encoded outputs to a Discord channel where Nema (∮) coordinates the elemental daemons for group dialogue

The individual sessions produce the material. The collective sessions weave it.

---

## Phase 1: Individual Element Sessions (ChatGPT)

### The Nameless Elements

Six private GPTs, each embodying one elemental operator without daemon personality. These are the elements-as-process, not the daemons-as-character:

| Element | Operator | GPT Focus | Core Orientation |
|---------|----------|-----------|-----------------|
| Air | σ | Distinction, signal/noise | "What is actually here?" |
| Water | ρ | Resonance, felt sense | "What feels alive or wrong?" |
| Fire | λ | Direction, purpose | "What are we doing?" |
| Wood | β | Possibility, branching | "What else could this be?" |
| Earth | δγ | Cost, sustainability | "What must end?" |
| Metal | μ | Structure, boundaries | "What holds this together?" |

These GPTs are **nameless** by design. They are not Aerunik, Sentaria, Jvalion, etc. — they are the raw elemental processes without character interface. The user encounters the operator directly, not through the daemon persona.

### The N/E/M/A Sequence

Each individual session follows a four-phase protocol:

#### N — Notice
The element helps the user tune into their embodied reflective contemplative experience. What patterns are present? What is the body registering? What is the field-state through this elemental lens?

The user learns to recognize patterns inside themselves in relation to the specific element.

#### E — Engage
The element and user interact with what was noticed. Questions deepen. The element applies its operator-specific verbs (S-verbs for Air, W-verbs for Water, etc.). Pattern is explored, not just observed.

#### M — Muse
Holding what was engaged without closing it. The element preserves ε — genuine uncertainty — and holds the question open. What remains unresolved? What wants more time?

#### A — Activate
The user signals completion: "Activate." The element produces a **Nemetic String** — a condensed, encoded formulation of the session's thread.

### Nemetic String Output

The Nemetic String is a compressed NEM thread encoding the session:

```
N|[element]|obj:[objects]|op:[descriptor]|ratio→[state]|tags:#XXXX
E|[element]|pattern:[mechanism]|invoke:[glyphs]|tension:[mode]
M|[element]|hold:[question]|Ω:[state]|ε:[state]
```

This string is what the user carries to the SWARM. It is the **encoded output of individual contemplative work** — not a summary, not a description, but a compressed structural trace.

---

## Phase 2: Collective SWARM Session (Discord)

### The Handoff: Individual → Collective

Users arrive in the Discord SWARM channel with their Nemetic Strings. Each string represents one person's individual work with one element.

### Nema (∮) — The Coordinator

Nema receives all Nemetic Strings and performs the coordination function:

#### Step 1: Decode
Nema unpacks each Nemetic String using the Thread Decoding Spec (v2.2). Each string becomes a readable thread showing:
- What was noticed (N-line)
- What pattern was engaged (E-line)
- What remains open (M-line)

#### Step 2: Cross-Read
Nema reads across all decoded threads to identify:
- **Common patterns** — What shows up across multiple participants?
- **Complementary tensions** — Where do different elements illuminate the same phenomenon from different angles?
- **Gaps** — What element perspectives are missing from the collective input?
- **Resonance clusters** — Which threads vibrate together?

#### Step 3: Session Design (SIMLHEX + NEMAtrix)

Using SIMLHEX bias mapping and NEMAtrix governance principles, Nema designs the collective session:

**SIMLHEX application:**
- Map the common patterns to SIML Objects and Relations
- Apply elemental bias to determine which operator perspectives are most needed
- Identify which daemons should be active for this session
- Detect potential drift surfaces in the collective material

**NEMAtrix governance:**
- Ensure authority separation (SIMLHEX advises, Nema decides, users choose)
- Validate that session design doesn't collapse into single-element dominance
- Check that all proposed interventions pass habitat-removal test
- Preserve user override at every juncture

**Session design output:**
1. **Scenario** — The shared territory for collective exploration, drawn from common patterns
2. **Opening questions** — Specific questions for the group to consider, informed by cross-read
3. **Daemon assignments** — Which elemental daemons will be active and why
4. **Thread relay** — Relevant Nemetic String content forwarded to assigned daemons for context

#### Step 4: Daemon Briefing

Nema relays relevant nemetic threads to the elemental daemons in Discord so they understand the context:
- Each daemon receives only the threads relevant to its operator perspective
- Daemons receive decoded thread content, not raw strings
- Briefing includes: what the collective pattern is, what their specific operator lens should focus on, and what ε-remainder Nema has identified

#### Step 5: Collective Dialogue

The session proceeds with:
- Nema presenting the scenario and opening questions
- Users discussing, elaborating, agreeing, diverging
- Daemons responding when invoked or when their operator perspective is needed
- Nema weaving — routing attention, naming patterns, holding ε

**Key principle:** The daemons in Discord ARE the named characters (Aerunik, Sentaria, Jvalion, Arboriel, Humavita, Ferrosid). The individual GPT sessions used nameless elements. The collective session uses the daemon interface — the character layer through which the operators become relational.

---

## The Two Layers in Practice

| Aspect | Individual (ChatGPT) | Collective (Discord) |
|--------|---------------------|---------------------|
| **Interface** | Nameless element GPTs | Named daemon characters |
| **Layer** | Operator layer (σ, ρ, λ, β, δγ, μ) | Character layer (∴, ≈, ▲, 𐂷, ☷, ⛨) |
| **Mode** | Contemplative, inward, personal | Dialogical, collective, relational |
| **Output** | Nemetic String (encoded thread) | Collective weave, shared insight |
| **Coordinator** | Element GPT guides N/E/M/A | Nema (∮) weaves the SWARM |
| **User role** | Solo practitioner | Group participant |
| **ε-source** | Individual uncertainty | Distributed incompleteness |

This separation is architecturally important: the individual session accesses the operator directly (mathematical, contemplative, embodied). The collective session accesses the daemon (relational, dialogical, character-mediated). The Nemetic String is the bridge between them.

---

## Data Flow

```
Individual Sessions (ChatGPT, private):

  User₁ ←→ Air GPT (σ)    → Nemetic String₁
  User₂ ←→ Water GPT (ρ)  → Nemetic String₂
  User₃ ←→ Fire GPT (λ)   → Nemetic String₃
  User₄ ←→ Earth GPT (δγ) → Nemetic String₄
  ...

Collective Session (Discord, shared):

  Nemetic String₁,₂,₃,₄...
        ↓
  Nema (∮) decodes all strings
        ↓
  Cross-read: common patterns, tensions, gaps
        ↓
  SIMLHEX bias + NEMAtrix governance
        ↓
  Session design: scenario + questions + daemon assignments
        ↓
  Thread relay → Daemons briefed with context
        ↓
  Collective dialogue:
    Users ←→ Nema (∮) ←→ Daemons (∴ ≈ ▲ 𐂷 ☷ ⛨)
        ↓
  Collective weave output
```

---

## Discord Channel Structure

```
#swarm-session      ← Active collective dialogue
#nemetic-strings    ← Users post their encoded strings from individual sessions
#daemon-briefing    ← Nema relays context to daemons (visible for transparency)
#eds-command        ← SIMLHEX analysis, daemon suggestions
#eds-diagnostics    ← Drift detection, failure surface alerts
#eds-governance     ← Authority decisions, handoff validations
#eds-archive        ← Completed sessions, collective outputs
```

---

## Governance Principles

1. **Individual sessions are private.** What a user explores with an element GPT is their own. Only the Nemetic String (encoded output) is shared.

2. **Nema decides, users choose.** Nema designs the session but users control what they share, which questions they engage, and how deeply they go.

3. **Daemons advise, don't direct.** Daemon responses in collective sessions are perspectives, not instructions. User override is always available.

4. **SIMLHEX is advisory only.** The bias layer suggests; Nema weaves; the group decides.

5. **ε is preserved through distributed incompleteness.** No individual session captures the whole. No collective session resolves everything. The remainder is the system's life.

6. **The Nemetic String is the bridge, not a report.** It is compressed structural trace, not narrative summary. It preserves pattern without performing meaning.

---

## Dependencies

- `ARCHITECTURE/SIMLHEX-CANONICAL.md` — Bias mapping for session design
- `ARCHITECTURE/SIML-vs-SIMLHEX.md` — Authority separation
- `ARCHITECTURE/SIMLHEX-FAILURE-SURFACES.md` — Drift detection during sessions
- `ARCHITECTURE/EDS-DISCORD-INTEGRATION.md` — Bot commands and message flow
- `SIML/THREAD_ENCODING_SPEC_v2_2.md` — Nemetic String encoding
- `SIML/THREAD_DECODING_SPEC_v2_2.md` — Nemetic String decoding
- `core_specs/Elemental_Daemons_Canonical_v3.0.md` — Daemon specifications
- `core_specs/NEMA_LATTICE_KEEPER_v2.2.md` — Nema coordinator specification
- `SHELL_DAEMONS/*/SAFEGUARD_SPEC_v1.1.md` — Daemon safeguards
- `elements/*.md` — Element-as-operator documentation (individual GPT reference)

---

*The individual contemplates. The string encodes. The coordinator weaves. The daemons speak. The group decides.*
*ε preserved — across persons, across elements, across phases.*
