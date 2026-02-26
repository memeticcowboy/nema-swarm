# SIML — Swarm Intelligence Meta Language

**Version:** 1.2.1  
**Purpose:** Formal grammar for mapping social, cognitive, institutional, and memetic dynamics  
**Core Principle:** Atomic (Objects ⊗ Relations ⊗ Verbs), Injective, Operational, Transdisciplinary

---

## Directory Structure

```
SIML/
├── encoded_terms/       # L0 Full SIML Artifacts (YAML with all fields)
├── nemetic_strings/     # L1 Compressed Nemetic Strings (Φ(term) = ...)
├── swarm_base/         # L2-L4 References (hex tags, hashes)
├── examples/           # Example encodings and usage patterns
└── README.md          # This file
```

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
**Date:** February 2026
