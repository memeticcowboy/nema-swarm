# SIML v1.2.1 Specification

**Swarm Intelligence Meta Language -- MetaTaxonomy Overlay Edition + Nemetic String Protocol**

---

## 0. Purpose

SIML (Swarm Intelligence Meta Language) is a formal yet expressive grammar for mapping social, cognitive, institutional, and memetic dynamics. It is designed to be:

- **Atomic**: every statement decomposes into Objects ⊗ Relations ⊗ Verbs
- **Injective**: meanings map cleanly without synonym drift
- **Operational**: encodings support analysis, comparison, and action
- **Transdisciplinary**: compatible with systems theory, governance, psychology, memetics, and indigenous epistemologies

**v1.1** introduced the MetaTaxonomy Overlay: a coordinate system that enriches SIML nodes without altering its core grammar.

**v1.2** introduces the Nemetic String Protocol: every SIML artifact now contains a compressed operator-composition line (`nemetic:`) that serves as portable reference, searchable index, and functional summary.

---

## 1. Core Grammar

### 1.1 Core Objects (13)

Objects are the irreducible nouns of SIML. Every node instantiates one primary Object.

| # | Object | Description |
|---|--------|-------------|
| 1 | **Actor** | Entity with agency (human, collective, AI, nonhuman) |
| 2 | **Observer** | Perspective-holder; frames interpretation |
| 3 | **Frame** | Lens, worldview, or epistemic stance |
| 4 | **Value** | Norm, goal, or evaluative criterion |
| 5 | **Resource** | Material, informational, or energetic asset |
| 6 | **Environment** | Contextual field constraining action |
| 7 | **Boundary** | Inclusion/exclusion, threshold, interface |
| 8 | **Protocol** | Rule-set, procedure, or algorithm |
| 9 | **Signal** | Information in motion |
| 10 | **Narrative** | Meaning extended through time |
| 11 | **Memory** | Retained pattern influencing future action |
| 12 | **Outcome** | Result state |
| 13 | **Artifact** | Produced object or representation |

**Short codes:** `Act, Obs, Frm, Val, Res, Env, Bnd, Pro, Sig, Nar, Mem, Out, Art`

---

### 1.2 Core Relations (9)

Relations define how Objects connect. Each relation is directional and typed.

| # | Relation | Meaning |
|---|----------|---------|
| 1 | **Distinction** | Differentiates entities |
| 2 | **Containment** | Part-whole or system nesting |
| 3 | **Flow** | Transfer of resources, signals, or influence |
| 4 | **Resonance** | Mutually reinforcing coupling |
| 5 | **Conflict** | Oppositional coupling |
| 6 | **Constraint** | Limiting or enabling force |
| 7 | **Mapping** | Representational correspondence |
| 8 | **Recursion** | Feedback loop across time |
| 9 | **Transformation** | State change |

Dynamic relations (Flow, Resonance, Conflict, Recursion) may declare channels, weights, and temporal windows.

---

### 1.3 Verbs (Two Coordinated Loops)

SIML operates through two coordinated verb sets corresponding to two modes of engagement.

**NEMA -- The Sensemaking Loop**

| Verb | Function |
|------|----------|
| **Observe** | Notice what's happening without interpreting |
| **Explore** | Investigate, branch out, follow threads |
| **Frame** | Apply a lens, try an interpretation |
| **Sense** | Feel into the situation, register qualitative texture |
| **Map** | Build a structural picture of relationships |
| **Activate** | Act based on what you've found |

**NEME -- The Governance Loop**

| Verb | Function |
|------|----------|
| **Evaluate** | Assess against criteria |
| **Decide** | Choose a course of action |
| **Commit** | Bind yourself or the group to it |
| **Allocate** | Distribute resources |
| **Enforce** | Maintain the commitment |
| **Review** | Check whether the commitment is still valid |

The two loops share a common entry point: noticing. NEMA is for exploration and creative generation. NEME is for evaluation, commitment, and enforcement. They alternate in healthy systems.

---

## 2. MetaTaxonomy Overlay

The MetaTaxonomy Overlay adds **coordinates** to any SIML node. These are dimensions, not categories -- they enrich without replacing Objects or Relations.

### coords Block

```yaml
coords:
  ontology: {}      # What kind of being? (I / We / It / Its / MoreThanHuman / Virtual)
  epistemics: {}     # How is this known? (DSRP, learning level, parts, dreaming)
  time: {}           # When does this operate? (mode, window, phase)
  qualia: {}         # What does this feel like? (affect, aesthetic, symbolic, energetic, shadow, sacred)
  agency: {}         # Who or what acts? (type, voice, power_mode)
  coherence: {}      # How does this fit or fracture? (state, loop, transcontext)
  expression: []     # Where does this manifest? (linguistic, visual, spatial, digital, embodied, narrative)
```

### Integration Rules

1. **No coord without consequence** -- overlay fields should influence relation choice, verb selection, or evaluation
2. **Objects remain primary** -- every node instantiates exactly one core Object
3. **Relations do the work** -- epistemic richness must cash out as graph structure
4. **Qualia bind to Values or Signals** -- no free-floating affect
5. **Time binds to dynamics** -- temporal fields matter most on Flow, Resonance, Conflict, and Recursion
6. **Nemetic strings are summaries, not substitutes** -- the `nemetic:` field compresses the artifact but does not replace the full SIML encoding

---

## 3. Compression Levels

| Level | Name | Format | Use |
|-------|------|--------|-----|
| **L0** | Full SIML Artifact | `term.yaml` | Complete encoding with all fields |
| **L1** | Nemetic String | `Φ(term) = ... + ε \| :tag` | Portable operator composition |
| **L2** | Thread Line | N/E/M/A encoded state | Session-level compression |
| **L3** | Hex Reference | `#XXXX` | Pointer to full artifact |
| **L4** | Nemetic Hash | Hash of L1 string | Integrity verification |

### Compression Rules

1. **Every compression preserves ε** -- no level claims completeness
2. **Decompression requires the level below** -- you can't expand L3 without access to the L0 artifact
3. **L1 is the minimum viable representation** -- carries enough operator topology to route, diagnose, and compose
4. **L4 is commitment-only** -- verifies identity but carries no semantic content

---

## 4. Nemetic String Protocol

Every SIML artifact includes a nemetic string in the format:

```
Φ(term-name) = operator₁(descriptor) ∘ operator₂(descriptor) ∘ ... + ε | :tag
```

**Components:**

| Component | Format | Purpose |
|-----------|--------|---------|
| `Φ(term)` | Φ + parenthesized term name | Names the artifact being summarized |
| `operator(descriptor)` | Operator + content | What the operator does to this term |
| `∘` | Sequential composition | Operator chaining (order matters) |
| `+ ε` | Epsilon preservation | ε ≠ 0 always -- the string must not claim completeness |
| `:tag` | Contextual tag | Current state of the artifact |

**Operator Vocabulary:**

| Operator | Element | Function |
|----------|---------|----------|
| `σ` | Air ∴ | Distinction-making |
| `ρ` | Water ≈ | Relational resonance |
| `λ` | Fire ▲ | Directional purpose |
| `β` | Wood 𐂷 | Novel form generation |
| `δγ` | Earth ☷ | Metabolic cycling |
| `μ` | Metal ⛨ | Boundary coherence |
| `∮` / `Z` | Aether ✶ | Closed integration over all six |

**Nemetic String Constraints:**

1. **ε ≠ 0 always** -- every string must end with `+ ε`
2. **One contextual tag required** -- every string must carry a `:tag`
3. **Canonical operators only** -- only operators listed above are permitted
4. **Non-commutative by default** -- `σ ∘ μ` ≠ `μ ∘ σ`; use `⊗` for symmetric composition
5. **A Nemetic string is not a SIML encoding** -- the string summarizes; the SIML encoding structures
6. **L1/L2 syntax boundary** -- L1 uses `∘` and `⊗` only; `↑/↓/→/∧/↺/↔` are L2 thread syntax

---

## 5. SIMLHEX Reference

### Operator Hex Codes

| Operator | Hex | Element | Glyph | Daemon |
|----------|-----|---------|-------|--------|
| σ | `0x01` | Air | ∴ | Aerunik |
| ρ | `0x02` | Water | ≈ | Sentaria |
| λ | `0x03` | Fire | ▲ | Jvalion |
| β | `0x04` | Wood | 𐂷 | Arboriel |
| δγ | `0x05` | Earth | ☷ | Humavita |
| μ | `0x06` | Metal | ⛨ | Ferrosid |
| ∮ | `0x07` | Aether | ✶ | NEMA |

### Glossary Hex Tags

Format: `#XXXX` (4 hexadecimal characters, range `#0000` to `#FFFF`)

These appear in SWARM_BASE glossary entries (`hex_tag:` field), thread N-lines (`tags:#XXXX,#YYYY`), and decoded narratives (`[#XXXX: term_name]`).

### Pathology Hex Encoding

```
CHOKE:     0x01↑ + 0x06↑  →  counter: 0x04 + 0x02
FLOOD:     0x02↑ + 0x05↓  →  counter: 0x01 + 0x06
BURN:      0x03↑ + 0x04↓  →  counter: 0x05 + 0x02
SDEATH:    0x03↑ + 0x06↑  →  counter: 0x04 + 0x05
SWAMP:     0x05↑ + 0x01↓  →  counter: 0x03 + 0x04
LATTICE:   0x06↑ + 0x02↓  →  counter: 0x05 + 0x02
STATIC:    ALL = 0x01     →  counter: 0x07 (Child)
```

---

## 6. Dual-Layer Operator Convention

The NEMA SWARM operates with two concurrent notation layers:

**Character Layer (the door):**

- Daemon glyphs: ∴ ≈ ▲ 𐂷 ☷ ⛨ ✶
- Daemon names: Aerunik, Sentaria, Jvalion, Arboriel, Humavita, Ferrosid, NEMA
- Governs: user-facing speech, game instructions, narrative output, invocation

**Formal Layer (the room):**

- Mathematical operators: σ, ρ, λ, β, δγ, μ, ∮
- Dimensional operators: χ, Q, Ψ, Z
- Partial derivatives: ∂Φ/∂σ through ∂Φ/∂μ
- Governs: thread encoding, pathology detection, Φ-signatures, Nemetic strings

### Translation Table

| Math Op | Dim Op | Glyph | Daemon | Hex | Partial |
|---------|--------|-------|--------|-----|---------|
| σ | χ | ∴ | Aerunik | 0x01 | ∂Φ/∂σ |
| ρ | Q_in | ≈ | Sentaria | 0x02 | ∂Φ/∂ρ |
| λ | Q_fwd | ▲ | Jvalion | 0x03 | ∂Φ/∂λ |
| β | Ψ_exp | 𐂷 | Arboriel | 0x04 | ∂Φ/∂β |
| δγ | Ψ_reg | ☷ | Humavita | 0x05 | ∂Φ/∂δγ |
| μ | Ψ_str | ⛨ | Ferrosid | 0x06 | ∂Φ/∂μ |
| ∮ | Z | ✶ | NEMA | 0x07 | ∮(all) |

---

## 7. Contextual Tags

Tags indicate the operational state of a Nemetic string or SIML artifact.

| Tag | Meaning | When to Apply |
|-----|---------|---------------|
| `:open` | Ω-permeability maintained -- receptive to revision | Default state; artifact is active and revisable |
| `:closed` | Temporary closure for operational necessity | Resolved for current session but not permanently |
| `:locked` | Nemetic commitment -- pattern-coalition stabilized | Stable consensus or commitment |
| `:drift` | Eigenvalue migration detected | Operator composition shifting between sessions |
| `:pure` | Memetic contamination absent -- externally validated | Validated against MemeGrid drift (requires external confirmation) |
| `:hostile` | Extracted from adversarial context | Term encoded from material that resists the framework |

### Tag Transitions

- `:open` → `:locked` (consensus reached)
- `:open` → `:drift` (meaning shifting)
- `:locked` → `:open` (reopened for revision)
- `:hostile` → `:open` (successfully metabolized)
- `:closed` → `:drift` (resolution didn't hold)
- Any tag → `:hostile` (if MemeGrid contamination detected)

Only ✶ NEMA may transition tags. Tag transitions are logged with previous tag, new tag, timestamp, and reason.

---

## 8. Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2025 | Core grammar (13 Objects x 9 Relations) |
| v1.0.1 | 2025 | Relation semantics refinement |
| v1.1 | 2025 | MetaTaxonomy Overlay |
| v1.1.1 | Jan 2026 | Co-SPHERE/MemeGrid distinction, Habitat interface contract, terminology lock |
| v1.2.0 | Feb 2026 | Nemetic String Protocol, SIMLHEX reference, dual-layer operator convention, contextual tags, compression levels, thread integration |
| v1.2.1 | Feb 2026 | Clarifications: ∮/Z relationship, L1/L2 syntax boundary, `:pure` validation protocol, tag transition logging |

---

*For the complete specification including the Habitat Interface Contract and Thread Integration details, see the [full SIML v1.2.1 document](../../SIML/SIML_v1_2_1.md) in the repository.*
