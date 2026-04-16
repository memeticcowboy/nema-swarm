# SIML Database

**Swarm Intelligence Meta Language** -- the formal grammar for mapping social, cognitive, institutional, and memetic dynamics.

**Version:** 1.2.1
**Core Principle:** Atomic (Objects x Relations x Verbs), Injective, Operational, Transdisciplinary

---

## What is SIML?

SIML provides a structured vocabulary for describing what happens wherever ideas, beliefs, feelings, power, or meaning are in play. It works the same way whether you are analyzing a conversation between two people, a corporate culture, a political movement, an AI system, or the internal landscape of a single mind.

The grammar has three layers:

- **Objects** (13) -- the irreducible nouns: Actor, Observer, Frame, Value, Resource, Environment, Boundary, Protocol, Signal, Narrative, Memory, Outcome, Artifact
- **Relations** (9) -- how objects connect: Distinction, Containment, Flow, Resonance, Conflict, Constraint, Mapping, Recursion, Transformation
- **Verbs** -- two coordinated loops: NEMA (sensemaking) and NEME (governance)

SIML provides the **grammar**. Daemons provide the **voice**. NEMA provides the **coordination**.

---

## Directory Structure

```
SIML/
├── terms/              # All SIML terms -- one folder per term
│   ├── {TAG}_{name}/
│   │   ├── term.yaml       # L0 Full SIML Artifact (required)
│   │   ├── nemetic.phi     # L1 Nemetic String (required)
│   │   └── insight.md      # Elemental insight analysis (when available)
│   └── ...
├── hex_registry.yaml   # Master registry of all hex tag assignments
├── manifest.yaml       # Term encoding status manifest
├── SIML_v1_2_1.md      # Full formal specification
├── SIML_Plain_English_Guide_v1.1.1.md  # Plain English guide
└── README.md
```

All SIML term output goes into `SIML/terms/`. Each term is self-contained in its own folder.

---

## Tag Prefix Table

| Prefix | Domain | Examples |
|--------|--------|----------|
| `A`    | Air element / cognitive bias / philosophical concepts | `A001_Pneuma`, `A014_Dark_Patterns` |
| `B`    | Borrowed concepts and external frameworks | `B001_Borrowed_Mind` |
| `C`    | Critical thinking / cognitive science | `C001_critical_thinking_definitions` |
| `CB`   | Cowboy Canonical terms -- core framework concepts | `CB001_Recursive_Phenomenology` |
| `D`    | Democracy / governance | `D001_democracy_networked_age` |
| `E`    | Earth element / ecological concepts | `E001_Gaia`, `E014_Autopoiesis` |
| `F`    | Fire element | `F001_Prometheus__Fire` |
| `H`    | Hypersigils and extended magical/ritual patterns | `H001_Hypersigil` |
| `L`    | Learning / pedagogy | `L001_jigsaw` |
| `M`    | Meta-level and meta-element concepts | `M001_Multiplicity`, `M099_MemeGrid` |
| `MET`  | Elemental Metal terms (mythological/alchemical) | `MET001_Gold` |
| `META` | Cross-elemental meta-synthesis | `META001_Nemetic_Pattern` |
| `N`    | Narrative and construction processes | `N001_Narrative_Construction` |
| `O`    | Openness and permeability concepts | `O001_Omega_Permeability` |
| `P`    | Psychology / learning theory | `P001_self_efficacy_theory` |
| `U`    | Underdetermination and epistemic conditions | `U001_Underdetermination` |
| `W`    | Water element / worldview-level concepts | `W001_Thales_Arche` |
| `WO`   | Wood element | `WO001_Yggdrasil` |

---

## Compression Levels

| Level | Name | Format | Use Case |
|-------|------|--------|----------|
| **L0** | Full SIML Artifact | YAML with all fields | Documentation, archival, deep analysis |
| **L1** | Nemetic String | `Phi(term) = ... + e | :tag` | Cross-substrate transmission, search index |
| **L2** | Thread Line | `N|earth|obj:Res,Env|...` | Session encoding, NEMA decoding |
| **L3** | Hex Reference | `#XXXX` | In-thread pointer to L0 artifact |
| **L4** | Nemetic Hash | `nemetic:a7f3k2` | Commitment verification, integrity check |

---

## Explore the SIML Database

- [Full Specification](specification.md) -- the complete SIML v1.2.1 spec
- [Hex Registry](registry.md) -- all registered tag prefixes and assignments
- [Encoding Guide](encoding-guide.md) -- plain English guide to SIML encoding
- [Term Browser](term-browser.md) -- browse the term database by prefix
