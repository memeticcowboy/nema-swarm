# SIML Encoding Guide

**A Plain English Introduction to the Swarm Intelligence Meta Language**

---

## What SIML Is

SIML stands for **Substrate-Independent Memetic Language**. It is a grammar — a structured way of describing what is happening in any situation where ideas, beliefs, feelings, power, or meaning are in play.

SIML is not a theory. It doesn't tell you what things mean. It gives you a consistent vocabulary for naming the parts and connections so that meaning can be investigated without collapsing into vagueness or premature certainty.

The grammar has three layers:

- **Objects** (the nouns — what's there)
- **Relations** (the connections — how things relate)
- **Verbs** (the process — what's being done about it)

Everything in SIML is built from combinations of these three.

---

## The 13 Core Objects

| Object | What It Means |
|--------|---------------|
| **Actor** | Anything with agency — a person, group, AI, organization |
| **Observer** | A perspective-holder who frames interpretation |
| **Frame** | A lens or worldview that shapes interpretation |
| **Value** | A norm, goal, or evaluative criterion |
| **Resource** | Material, informational, or energetic asset |
| **Environment** | The contextual field constraining action |
| **Boundary** | Membrane determining inside vs. outside |
| **Protocol** | Repeatable pattern of coordinated action |
| **Signal** | Information in motion |
| **Narrative** | Meaning extended through time |
| **Memory** | Retained pattern influencing future action |
| **Outcome** | Result state |
| **Artifact** | Produced object or representation |

---

## How to Read a SIML Encoding

A typical SIML encoding looks like this:

```
⟨Frame|kinship⟩ ⊳ ⟨Actor|Indigenous-community⟩ ⇄ ⟨Environment|water-beings⟩
→ ⟨Value|reciprocity⟩ ⊗ ⟨Protocol|sacred-stewardship⟩ → ⟨Outcome|living-harmony⟩
```

Read it as: *"A kinship frame shapes how the Indigenous community relates (with mutual feedback) to water-beings as environment. This enables reciprocity as a value, which is in tension with sacred stewardship as protocol, which in turn enables living harmony as outcome."*

---

## How to Read a Nemetic String

The compressed form:

```
Φ(Living-Water) = ρ(kinship-resonance|water-as-relative) ∘ δγ(cyclical-gift|reciprocal-flow)
  ∘ μ(sacred-boundary|protected-waters) ∘ σ(distinction|living-vs-dead-water) + ε | :pure
```

**Components:**

| Part | Meaning |
|------|---------|
| `Φ(name)` | "The pattern of..." |
| `ρ(...)` | Water/resonance operator applied to... |
| `δγ(...)` | Earth/metabolism operator applied to... |
| `μ(...)` | Metal/structure operator applied to... |
| `σ(...)` | Air/distinction operator applied to... |
| `∘` | "flows into" (composition) |
| `+ ε` | Uncertainty preserved (always) |
| `\| :tag` | State tag (`:pure`, `:open`, `:sword`, etc.) |

---

## The Operator Vocabulary

| Symbol | Element | Function |
|--------|---------|----------|
| `σ` | Air ∴ | Distinction — separates signal from noise |
| `ρ` | Water ≈ | Resonance — attunes to relational field |
| `λ` | Fire ▲ | Direction — generates purpose and momentum |
| `β` | Wood 𐂷 | Exploration — branches into novelty |
| `δγ` | Earth ☷ | Metabolism — cycles between decay and renewal |
| `μ` | Metal ⛨ | Structure — maintains permeable boundaries |
| `Z` | Aether ✶ | Integration — weaves all operators together |

---

## Creating a SIML Entry

### Step 1: Identify the Core Concept

What are you encoding? A concept, framework, phenomenon, or dynamic.

### Step 2: Map to Objects and Relations

Which of the 13 objects are involved? How are they connected?

### Step 3: Determine Elemental Emphasis

Which operators dominate? Every concept leans toward certain elements.

### Step 4: Write the Nemetic String

Compose the operators that capture the concept's essence.

### Step 5: Create the `term.yaml`

```yaml
term_id: "X001"
hex_tag: "#X001"
name: "Your Term"
description: "What this term captures"
element: "Primary Element"
nemetic: "Φ(term) = ... + ε | :tag"
siml_encoding: "⟨...⟩ ⊳ ⟨...⟩ → ⟨...⟩"
```

### Step 6: Write the `nemetic.phi`

The compressed L1 string in a standalone file.

---

## State Tags

State tags mark the current condition of a pattern:

| Tag | Meaning |
|-----|---------|
| `:open` | Exploratory, unresolved |
| `:pure` | Clean, uncontaminated |
| `:sword` | Directed, with edge |
| `:steam` | Transforming, in flux |
| `:organ` | Living instrument, functional |
| `:monument` | Archived, awaiting return |

---

*For the full specification, see the [SIML v1.2.1 Specification](specification.md).*
