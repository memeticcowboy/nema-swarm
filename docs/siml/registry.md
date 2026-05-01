# Hex Registry

The SIML Hex Registry tracks all assigned tags and their domains. Each tag prefix maps to a specific elemental or conceptual domain.

---

## Tag Prefixes

| Prefix | Domain | Description |
|--------|--------|-------------|
| `A` | Air / Cognitive | Cognitive biases, psychological phenomena, philosophical concepts |
| `C` | Critical Thinking | Cognitive science, critical thinking frameworks |
| `CB` | Cowboy Canonical | Core framework concepts |
| `D` | Democracy | Governance, democratic systems |
| `E` | Earth / Ecology | Ecological concepts, earth-element terms |
| `F` | Fire | Fire-element terms, purpose, direction |
| `L` | Learning | Pedagogy, learning theory, educational frameworks |
| `M` | Metal | Metal-element terms, structure, boundaries |
| `META` | Meta-Synthesis | Cross-elemental integration patterns |
| `P` | Psychology | Psychology, learning theory |
| `W` | Water | Water-element terms, resonance, connection |
| `WO` | Wood | Wood-element terms, growth, exploration |

---

## Registry Snapshot

```yaml
A:
  description: Cognitive biases and psychological phenomena
  next_available: A069
  # 60+ terms assigned including:
  # A001: Pneuma, A002: Prana, A003: Qi
  # A007: Information_Bateson, A008: Double_Bind
  # A013: Cognitive_Distortion, A014: Dark_Patterns
  # A057: Confirmation_Bias, A059: Hyperobject

C:
  description: Critical thinking and cognitive science
  # A06B: critical_thinking_definitions and more

D:
  description: Democracy and governance
  # D001: democracy_networked_age and more

E:
  description: Earth element and ecological concepts
  next_available: E026
  # F012: Gaia, E014: Autopoiesis
  # E025: Four_Spheres

F:
  description: Fire element
  # A0D5: Prometheus__Fire and more

L:
  description: Learning and pedagogy
  next_available: L100+
  # L001: jigsaw through L100+

M:
  description: Metal element
  # M001: Gold through M013: Iron_Mars

META:
  description: Cross-elemental meta-synthesis
  # Z001: Nemetic_Pattern through META005

P:
  description: Psychology and learning theory
  # P001: self_efficacy_theory and more

W:
  description: Water element
  # A10B: Thales__Arche through W008

WO:
  description: Wood element
  # B015: Yggdrasil through B017
```

---

## How Tags Work

Every SIML term receives a globally unique hex tag:

- Format: `#PREFIX + NUMBER` (e.g., `#A001`, `#A10D`, `#Z002`)
- Tags are assigned sequentially within each prefix
- The `next_available` field tracks the next open slot
- Tags never reuse — even if a term is deprecated, its tag remains reserved

## Using Tags

Reference any term by its hex tag:

- In text: `#A001` refers to the Pneuma entry
- In nemetic strings: `tags:#A001`
- In thread encoding: `tags:#A001,#A10D`
- For lookup: find the term folder at `SIML/terms/{TAG}_{name}/`

---

*For the full live registry, see [`hex_registry.yaml`](../../SIML/hex_registry.yaml) in the repository.*
