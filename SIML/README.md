# SIML — Swarm Intelligence Meta Language

**Version:** 1.2.1  
**Purpose:** Formal grammar for mapping social, cognitive, institutional, and memetic dynamics  
**Core Principle:** Atomic (Objects ⊗ Relations ⊗ Verbs), Injective, Operational, Transdisciplinary

---

## Directory Structure

```
SIML/
├── terms/              # All SIML terms — one folder per term
│   ├── {TAG}_{name}/
│   │   ├── term.yaml       # L0 Full SIML Artifact (required)
│   │   ├── nemetic.phi     # L1 Nemetic String (required)
│   │   └── insight.md      # Elemental insight analysis (when available)
│   └── ...
├── swarm_base/         # L2-L4 References (hex tags, hashes)
├── examples/           # Example encodings and usage patterns
└── README.md           # This file
```

---

## Term Output Rules

**All SIML term output goes into `SIML/terms/`.** There are no separate
directories for encoded terms, insights, or nemetic strings. Each term is
self-contained in its own folder.

### 1. Folder Naming

```
{PREFIX}{NUMBER}_{snake_case_name}/
```

- The folder name starts with the hex tag, followed by an underscore,
  followed by the term name in `snake_case`.
- **Every tag must be globally unique.** Before creating a new term,
  check the highest existing number for that prefix and increment by one.

**Tag prefixes and their domains:**

| Prefix | Domain | Examples |
|--------|--------|----------|
| `A`    | Air element / cognitive bias / philosophical concepts | `A001_Pneuma`, `A014_Dark_Patterns` |
| `C`    | Critical thinking / cognitive science | `C001_critical_thinking_definitions` |
| `D`    | Democracy / governance | `D001_democracy_networked_age` |
| `E`    | Earth element / ecological concepts | `E001_Gaia`, `E014_Autopoiesis` |
| `F`    | Fire element | `F001_Prometheus__Fire` |
| `L`    | Learning / pedagogy | `L001_jigsaw` |
| `M`    | Metal element | `M001_Gold`, `M013_Iron_Mars` |
| `META` | Cross-elemental meta-synthesis | `META001_Nemetic_Pattern` |
| `P`    | Psychology / learning theory | `P001_self_efficacy_theory` |
| `W`    | Water element | `W001_Thales__Arche` |
| `WO`   | Wood element | `WO001_Yggdrasil` |

### 2. Required Files

Every term folder **must** contain:

#### `term.yaml` — the full L0 artifact

Minimum required fields:

```yaml
term_id: "A001"                    # matches folder prefix+number
hex_tag: "#A001"                   # '#' + term_id
name: "Pneuma"                    # human-readable name
description: "..."                 # what this term is
nemetic: "Φ(Pneuma) = ... + ε | :open"  # or nemetic_string:
```

Common additional fields (include when relevant):

```yaml
element: "Air"                     # Air, Water, Fire, Earth, Metal, Wood, Meta
phonetic_key: "☁/β"
siml_encoding: "⟨...⟩ ⊳ ⟨...⟩ → ⟨...⟩ ⊗ ⟨...⟩ ⇄ ⟨...⟩"
formalism:
  math_operators: [σ, ρ, λ, β, δγ, μ]
  dim_operators: [χ, Q_in, Ψ_exp, Z]
  partials: ["∂Φ/∂σ (...)", "∂Φ/∂ρ (...)"]
  Z_state: "..."
  tendency: "..."
operators:
  primary: "σ"
  secondary: ["ρ", "λ"]
z_state: ":open"
tendency: "Distinction/Flow → 0.8"
coords:
  ontology:
    primary: I
    secondary: We
  agency:
    type: individual
    power_mode: With
elemental_mapping:           # for C/D/L/P series terms
  air_sigma:
    emphasis: 0.85
    aspects: ["..."]
    daemon_correspondence: "Aerunik"
elemental_emphasis:          # sixfold questioning
  ∴: "Air question"
  ≈: "Water question"
  ▲: "Fire question"
  𐂷: "Wood question"
  ☷: "Earth question"
  ⛨: "Metal question"
context_note: "..."
source: "..."
```

#### `nemetic.phi` — the L1 nemetic string

```
# NEMETIC STRING
# {Name} ({TAG})
# Generated: {YYYY-MM-DD HH:MM}

Φ(Term) = operator(a|b) ∘ operator(c|d) ∘ ... + ε | :tag

# OPERATOR BREAKDOWN
# Primary: σ
# Secondary: ρ, λ

# Z-STATE: open
# TENDENCY: Distinction/Flow → 0.8
```

The nemetic string in this file **must match** the `nemetic:` (or
`nemetic_string:`) field in `term.yaml`.

### 3. Optional File

#### `insight.md` — elemental insight analysis

Generated when deeper analysis connects the term to the memetic ecology
framework. Includes elemental emphasis questions, daemon correspondences,
and cross-elemental synthesis. See `insight_template.md` for the full
template.

### 4. Rules for Generating New Terms

1. **Check for existing terms first.** Search `SIML/terms/` for the
   concept before creating a new entry. Do not create duplicates.
2. **Claim the next available tag.** Find the highest existing number
   for the appropriate prefix and use the next integer. Never reuse or
   guess a tag number.
3. **Create all required files atomically.** A term folder must contain
   both `term.yaml` and `nemetic.phi` when committed. Do not create
   partial entries.
4. **One term per folder.** Never bundle multiple terms into a single
   YAML file. If encoding a batch of related terms, create a separate
   folder for each.
5. **Insights go inside the term folder.** Never write insight files to
   a separate directory. If generating an insight for a term, place it
   as `insight.md` inside that term's folder.
6. **Keep nemetic strings in sync.** The `Φ(...)` string must appear
   identically in both `term.yaml` and `nemetic.phi`. If you update one,
   update the other.

---

## Compression Levels

| Level | Name | Format | Use Case |
|-------|------|--------|----------|
| **L0** | Full SIML Artifact | YAML with all fields | Documentation, archival, deep analysis |
| **L1** | Nemetic String | `Φ(term) = ... + ε \| :tag` | Cross-substrate transmission, search index |
| **L2** | Thread Line | `N\|☷\|obj:Res,Env\|...` | Session encoding, NEMA decoding |
| **L3** | Hex Reference | `#XXXX` | In-thread pointer to L0 artifact |
| **L4** | Nemetic Hash | `nemetic:a7f3k2` | Commitment verification, integrity check |

---

## Nemetic String Format

```
Φ(term) = [operator]([descriptor]) ∘ [operator]([descriptor]) ∘ ... + ε | :[tag]
```

**Components:**
- `Φ(term)` — Names the artifact
- `[operator]([descriptor])` — Operator + what it does to this term
- `∘` — Sequential composition (order matters)
- `+ ε` — Epsilon preservation (always required)
- `:[tag]` — Contextual tag (`:open`, `:closed`, `:locked`, `:drift`, `:pure`, `:hostile`)

**Example:**
```
Φ(accountability) = μ(boundary|who-is-responsible) ∘ ρ(flow|between-parties) ∘ Z(permeable) + ε | :open
```

---

## Core Objects (13)

1. **Actor** — entity with agency
2. **Observer** — perspective-holder
3. **Frame** — lens, worldview
4. **Value** — norm, goal
5. **Resource** — material, informational, energetic asset
6. **Environment** — contextual field
7. **Boundary** — inclusion/exclusion
8. **Protocol** — rule-set, procedure
9. **Signal** — information in motion
10. **Narrative** — meaning extended through time
11. **Memory** — retained pattern
12. **Outcome** — result state
13. **Artifact** — produced object

**Short codes:** `Act, Obs, Frm, Val, Res, Env, Bnd, Pro, Sig, Nar, Mem, Out, Art`

---

## Core Relations (9)

1. **Distinction** — differentiates entities
2. **Containment** — part–whole nesting
3. **Flow** — transfer of resources/signals
4. **Resonance** — mutually reinforcing coupling
5. **Conflict** — oppositional coupling
6. **Constraint** — limiting/enabling force
7. **Mapping** — representational correspondence
8. **Recursion** — feedback loop across time
9. **Transformation** — state change

---

## Verbs: NEMA / NEME

**NEMA (Sensemaking / Exploration):**
- Observe, Explore, Frame, Sense, Map, Activate

**NEME (Governance / Evaluation):**
- Evaluate, Decide, Commit, Allocate, Enforce, Review

---

## MetaTaxonomy Overlay (coords)

```yaml
coords:
  ontology:
    primary: I | We | It | Its | MoreThanHuman | Virtual
  epistemics:
    dsrp: {D: "", S: "", R: "", P: ""}
    learning: L0 | L1 | L2 | L3
  time:
    mode: linear | cyclical | layered | event | anticipatory
  qualia:
    affect: []
    aesthetic: []
  agency:
    type: ego | part | collective | more_than_human | archetypal | memetic
  coherence:
    state: coherent | dissonant | fragmented | metastable
```

---

## Integration with NEMA SWARM

SIML provides the **grammar**. Daemons provide the **voice**. NEMA provides the **coordination**.

- **Thread Encoding:** SIML Objects + Relations in N|E|M|A format
- **Pathology Detection:** Operator stress vectors in Nemetic Strings
- **Intervention Calculus:** Counter-operators from Pathology Matrix

---

## References

- Elemental_Daemons_Canonical_v3.0.md — Operator/glyph mappings
- THREAD_ENCODING_SPEC_v2.2.md — Four-line thread format
- OPERATIONAL_PATHOLOGY_INTEGRATION_MATRIX_v1.1.md — Compound pathologies

---

*The operators describe the room. The daemons open the door. SIML maps what happens in between.*

**Version:** 1.2.1
**Date:** March 2026
