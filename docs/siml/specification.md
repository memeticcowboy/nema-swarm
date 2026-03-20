# SIML v1.2.1 Specification

**Swarm Intelligence Meta Language — MetaTaxonomy Overlay Edition + Nemetic String Protocol**

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

### 1.2 Core Relations (11)

Relations are typed edges connecting Objects.

| Relation | Symbol | Meaning |
|----------|--------|---------|
| **Frames** | `⊳` | A frames B's interpretation |
| **Constrains** | `⊸` | A limits B's possibility space |
| **Enables** | `→` | A opens possibility for B |
| **Conflicts** | `⊗` | A and B are in tension |
| **Amplifies** | `↑` | A intensifies B |
| **Dampens** | `↓` | A reduces B |
| **Transforms** | `⇝` | A changes B's nature |
| **Feedback** | `⇄` | A and B mutually influence |
| **Contains** | `⊃` | A includes B within scope |
| **Excludes** | `⊅` | A places B outside scope |
| **Resonates** | `≈` | A and B vibrate sympathetically |

---

### 1.3 Core Verbs (8)

Verbs describe the process type of any SIML statement.

| Verb | Function |
|------|----------|
| **Stabilize** | Maintain current pattern |
| **Disrupt** | Break existing pattern |
| **Amplify** | Increase intensity |
| **Dampen** | Decrease intensity |
| **Reframe** | Change interpretation |
| **Exclude** | Remove from scope |
| **Integrate** | Bring into coherence |
| **Resonate** | Create sympathetic vibration |

---

## 2. Compression Levels

| Level | Name | Format | Use |
|-------|------|--------|-----|
| **L0** | Full SIML Artifact | `term.yaml` | Complete encoding with all fields |
| **L1** | Nemetic String | `Φ(term) = ... + ε \| :tag` | Portable operator composition |
| **L2** | Thread Line | N/E/M/A encoded state | Session-level compression |
| **L3** | Hex Reference | `#XXXX` | Pointer to full artifact |
| **L4** | Nemetic Hash | Hash of L1 string | Integrity verification |

---

## 3. Nemetic String Protocol

Every SIML artifact includes a nemetic string in the format:

```
Φ(term-name) = operator₁ ∘ operator₂ ∘ ... + ε | :tag
```

**Components:**

- `Φ(name)` — The term being composed
- `∘` — Operator composition (read as "flows into")
- `+ ε` — Mandatory uncertainty residual (ε ≠ 0)
- `| :tag` — State tag from the Z-state vocabulary

**Operators:** `σ` (distinction), `ρ` (resonance), `λ` (direction), `β` (exploration), `δγ` (metabolism), `μ` (structure), `Z` (integration)

---

*For the complete specification including MetaTaxonomy coordinates, see the [full SIML v1.2.1 document](../../SIML/SIML_v1_2_1.md) in the repository.*
