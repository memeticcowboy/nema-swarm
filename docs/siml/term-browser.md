# Term Browser

The SIML database contains **490+ encoded terms** organized across all elemental domains. Each term lives in its own folder under `SIML/terms/`.

---

## Term Structure

Every term folder contains:

```
{TAG}_{name}/
├── term.yaml       # L0 Full SIML artifact (required)
├── nemetic.phi     # L1 Nemetic string (required)
└── insight.md      # Elemental insight analysis (optional)
```

---

## Terms by Domain

### Air (A-prefix) — Cognitive & Philosophical

~65 terms covering cognitive biases, philosophical concepts, and psychological phenomena.

- `#A001` **Pneuma** — Greek concept of breath/spirit as cognitive force
- `#A002` **Prana** — Sanskrit vital breath
- `#A003` **Qi** — Chinese vital energy
- `#A007` **Information (Bateson)** — "A difference that makes a difference"
- `#A008` **Double Bind** — Contradictory message patterns
- `#A013` **Cognitive Distortion** — Systematic thinking errors
- `#A014` **Dark Patterns** — Deceptive design patterns
- `#A057` **Confirmation Bias** — Seeking confirming evidence
- `#A059` **Hyperobject** — Objects massively distributed in time/space

### Water (W-prefix) — Resonance & Connection

- `#W001` **Thales' Arche** — Water as first principle
- `#W005` **Living Water** — Indigenous kinship with water-as-relative
- `#W008` and more...

### Fire (F-prefix) — Purpose & Direction

- `#F001` **Prometheus' Fire** — Stolen fire as directional force

### Wood (WO-prefix) — Growth & Exploration

- `#WO001` **Yggdrasil** — World tree as branching archetype
- Through `#WO010` and growing...

### Earth (E-prefix) — Ecology & Metabolism

~25 terms covering ecological and regenerative concepts.

- `#E001` **Gaia** — Earth as living system
- `#E014` **Autopoiesis** — Self-creating systems
- `#E025` **Four Spheres** — Atmosphere, hydrosphere, lithosphere, biosphere

### Metal (M-prefix) — Structure & Boundaries

- `#M001` **Gold** — Noble metal as structural archetype
- Through `#M013` **Iron/Mars** — Martial structure

### Meta (META-prefix) — Cross-Elemental

- `#META001` **Nemetic Pattern** — The pattern that recognizes patterns
- Through `#META005`

### Learning (L-prefix) — Pedagogy

100+ terms covering learning theory and educational frameworks.

- `#L001` **Jigsaw** — Cooperative learning structure
- Extensive coverage of pedagogical methods

### Critical Thinking (C-prefix)

- `#C001` **Critical Thinking Definitions** — Foundational concepts

### Democracy (D-prefix)

- `#D001` **Democracy in the Networked Age** — Governance evolution

### Psychology (P-prefix)

- `#P001` **Self-Efficacy Theory** — Bandura's framework

---

## Sample Term: `#A007 Information (Bateson)`

```yaml
term_id: "A007"
hex_tag: "#A007"
name: "Information (Bateson)"
description: "Gregory Bateson's definition: 'a difference that makes a difference'"
element: "Air"
nemetic: "Φ(Information) = σ(difference|distinction) ∘ σ(difference-of-difference) + ε | :open"
siml_encoding: "⟨Signal|difference⟩ ⊳ ⟨Observer|perceiver⟩ → ⟨Frame|distinction⟩ ⊗ ⟨Value|relevance⟩"
```

---

## Browsing Tips

- Terms are stored at `SIML/terms/{TAG}_{snake_case_name}/`
- Use the hex tag as a quick reference in thread encodings
- The `nemetic.phi` file contains the compressed operator string
- `insight.md` files contain deeper elemental analysis when available
- Check `manifest.yaml` for encoding status of all terms

---

*The database grows continuously. ε is preserved in every entry.*
