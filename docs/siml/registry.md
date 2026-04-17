# Hex Registry

The SIML Hex Registry tracks all assigned tags and their domains. Each tag prefix maps to a specific elemental or conceptual domain.

---

## Tag Prefixes

| Prefix | Domain | Description |
|--------|--------|-------------|
| `A` | Air / Cognitive | Cognitive biases, psychological phenomena, philosophical concepts |
| `B` | Borrowed | Borrowed concepts and external frameworks |
| `C` | Critical Thinking | Cognitive science, critical thinking frameworks |
| `CB` | Cowboy Canonical | Core framework concepts |
| `E` | Earth / Ecology | Ecological concepts, enactive cognition, earth-element terms |
| `F` | Fire | Fire-element terms, purpose, direction |
| `H` | Hypersigils | Extended magical/ritual patterns |
| `L` | Learning | Pedagogy, learning theory, educational frameworks |
| `M` | Meta-Level | Meta-level and meta-element concepts |
| `MET` | Elemental Metal | Mythological/alchemical metal terms |
| `META` | Meta-Synthesis | Cross-elemental integration patterns |
| `N` | Narrative | Narrative and construction processes |
| `O` | Openness | Openness and permeability concepts |
| `P` | Psychology | Psychology, learning theory |
| `U` | Underdetermination | Epistemic conditions |
| `W` | Water / Worldview | Water-element terms, worldview-level concepts, cosmological frameworks |
| `WO` | Wood | Wood-element terms, growth, exploration |

---

## Registry Snapshot

```yaml
A:
  description: Cognitive biases and psychological phenomena
  next_available: A069
  # 57 terms assigned including:
  # A001: Pneuma, A002: Prana, A003: Qi
  # A007: Information_Bateson, A008: Double_Bind
  # A013: Cognitive_Distortion, A014: Dark_Patterns
  # A057: Confirmation_Bias, A059: Hyperobject
  # A060: Actual_Occasion, A063: Ecology_of_Mind

B:
  description: Borrowed concepts and external frameworks
  next_available: B003
  # B001: Borrowed_Mind, B002: LeapFrogU

C:
  description: Critical thinking and cognitive science
  next_available: C189
  # 215 terms: C001 through C188
  # C001: critical_thinking_definitions
  # C138: Confabulation, C173: Metacognitive_AI_Architectures

CB:
  description: Cowboy Canonical terms - core framework concepts
  next_available: CB015
  # 14 terms: CB001 through CB014
  # CB001: Recursive_Phenomenology
  # CB009: Co_Sphere, CB010: Rumspringa_Protocol

E:
  description: Earth element and ecological concepts
  next_available: E026
  # 25 terms: E001 through E025
  # E001: Gaia, E014: Autopoiesis, E025: Four_Spheres

F:
  description: Fire element
  next_available: F009
  # 8 terms: F001: Prometheus__Fire through F008: Retrocausality

H:
  description: Hypersigils and extended magical/ritual patterns
  next_available: H005
  # 4 terms: H001: Hypersigil through H004: StoryTech

L:
  description: Learning and metacognition concepts
  next_available: L114
  # 105 terms: L001 through L112
  # L001: Jigsaw, L081: Montessori_Method
  # L111: Third_Self, L112: Reclaimed_Hubris

M:
  description: Meta-level and meta-element concepts
  next_available: M023
  # 23 terms: M001: Multiplicity through M022: Synthetic_Intelligence
  # M099: MemeGrid

MET:
  description: Elemental Metal terms (mythological/alchemical)
  next_available: MET011
  # 10 terms: MET001: Gold through MET010: Star_State

META:
  description: Cross-elemental meta-synthesis
  # META001: Nemetic_Pattern and more

N:
  description: Narrative and construction processes
  next_available: N003
  # N001: Narrative_Construction, N002: Devolution

O:
  description: Openness and permeability concepts
  next_available: O002
  # O001: Omega_Permeability

P:
  description: Psychology and learning theory
  # P001: self_efficacy_theory and more

U:
  description: Underdetermination and epistemic conditions
  next_available: U002
  # U001: Underdetermination

W:
  description: Worldview-level concepts and cosmological frameworks
  next_available: W011
  # 10 terms: W001: Thales_Arche through W009: Cyberanimism

WO:
  description: Wood element
  # WO001: Yggdrasil through WO010+
```

---

## How Tags Work

Every SIML term receives a globally unique hex tag:

- Format: `#PREFIX + NUMBER` (e.g., `#A001`, `#W005`, `#META003`)
- Tags are assigned sequentially within each prefix
- The `next_available` field tracks the next open slot
- Tags never reuse -- even if a term is deprecated, its tag remains reserved

## SIMLHEX Operator Codes

In addition to glossary hex tags, SIMLHEX provides operator-level hex codes:

| Hex | Operator | Element | Glyph |
|-----|----------|---------|-------|
| `0x01` | σ | Air | ∴ |
| `0x02` | ρ | Water | ≈ |
| `0x03` | λ | Fire | ▲ |
| `0x04` | β | Wood | 𐂷 |
| `0x05` | δγ | Earth | ☷ |
| `0x06` | μ | Metal | ⛨ |
| `0x07` | ∮ | Aether | ✶ |

## Using Tags

Reference any term by its hex tag:

- In text: `#A001` refers to the Pneuma entry
- In nemetic strings: `tags:#A001`
- In thread encoding: `tags:#A001,#W005`
- For lookup: find the term folder at `SIML/terms/{TAG}_{name}/`

---

*For the full live registry, see [`hex_registry.yaml`](../../SIML/hex_registry.yaml) in the repository.*
