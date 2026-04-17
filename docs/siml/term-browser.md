# Term Browser

The SIML database contains **480+ encoded terms** organized across all elemental and conceptual domains. Each term lives in its own folder under `SIML/terms/`.

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

### Air (A-prefix) -- Cognitive & Philosophical

57 terms covering cognitive biases, philosophical concepts, and psychological phenomena.

- `#A001` **Pneuma** -- Greek concept of breath/spirit as cognitive force
- `#A002` **Prana** -- Sanskrit vital breath
- `#A003` **Qi** -- Chinese vital energy
- `#A007` **Information (Bateson)** -- "A difference that makes a difference"
- `#A008` **Double Bind** -- Contradictory message patterns
- `#A013` **Cognitive Distortion** -- Systematic thinking errors
- `#A014` **Dark Patterns** -- Deceptive design patterns
- `#A057` **Confirmation Bias** -- Seeking confirming evidence
- `#A059` **Hyperobject** -- Objects massively distributed in time/space
- `#A060` **Actual Occasion** -- Whitehead's processual unit
- `#A063` **Ecology of Mind** -- Bateson's relational epistemology

### Borrowed (B-prefix) -- External Frameworks

- `#B001` **Borrowed Mind** -- External cognitive frameworks
- `#B002` **LeapFrogU** -- Educational leapfrog model

### Critical Thinking (C-prefix) -- Cognitive Science

215 terms covering critical thinking, cognitive science, consciousness studies, and AI cognition.

- `#C001` **Critical Thinking Definitions** -- Foundational concepts
- `#C105` **Cabrera Critical Thinking Critique** -- DSRP-based analysis
- `#C138` **Confabulation** -- Memory fabrication patterns
- `#C173` **Metacognitive AI Architectures** -- AI self-reflection models

### Cowboy Canonical (CB-prefix) -- Core Framework

14 terms defining the core Memetic Cowboy framework concepts.

- `#CB001` **Recursive Phenomenology** -- Self-referential experience analysis
- `#CB009` **Co-SPHERE** -- Collaborative sphere model
- `#CB010` **Rumspringa Protocol** -- Exploratory boundary protocol
- `#CB011` **Lariat Protocol** -- Containment and retrieval pattern
- `#CB013` **SelfMesh** -- Self-referential mesh network
- `#CB014` **6DOF** -- Six degrees of freedom framework

### Earth (E-prefix) -- Ecology & Metabolism

25 terms covering ecological, enactive, and regenerative concepts.

- `#E001` **Gaia** -- Earth as living system
- `#E011` **Enactive Cognition** -- Mind as embodied action
- `#E014` **Autopoiesis** -- Self-creating systems
- `#E022` **Mycorrhizal Network** -- Fungal communication systems
- `#E024` **Bioneering** -- Biological pioneering
- `#E025` **Four Spheres** -- Atmosphere, hydrosphere, lithosphere, biosphere

### Fire (F-prefix) -- Purpose & Direction

8 terms covering fire-element dynamics and directional force.

- `#F001` **Prometheus' Fire** -- Stolen fire as directional force
- `#F002` **Agni** -- Vedic fire deity and transformative power
- `#F006` **Global Workspace Theory** -- Consciousness as broadcast
- `#F008` **Retrocausality** -- Backward-in-time causation

### Hypersigils (H-prefix) -- Magical/Ritual Patterns

- `#H001` **Hypersigil** -- Extended magical pattern
- `#H002` **Hyperstition** -- Fiction that makes itself real
- `#H003` **Hauntology** -- Derridean spectral presence
- `#H004` **StoryTech** -- Narrative as technology

### Learning (L-prefix) -- Pedagogy & Metacognition

105 terms covering learning theory, educational frameworks, and cognitive enhancement.

- `#L001` **Jigsaw** -- Cooperative learning structure
- `#L011` **Cognitive Load Theory** -- Sweller's processing limits
- `#L029` **Bloom's Taxonomy** -- Hierarchical learning objectives
- `#L043` **Zone of Proximal Development** -- Vygotsky's learning edge
- `#L079` **Rhizomatic Learning** -- Non-hierarchical knowledge growth
- `#L081` **Montessori Method** -- Child-directed learning
- `#L085` **Waldorf Education** -- Steiner's holistic pedagogy
- `#L106` **AI Agent Memory Types** -- Machine learning memory models
- `#L111` **Third Self** -- Emergent identity beyond dual self
- `#L112` **Reclaimed Hubris** -- Constructive overreach

### Meta-Level (M-prefix) -- Meta Concepts

23 terms covering meta-level concepts and systemic patterns.

- `#M001` **Multiplicity** -- Internal plurality
- `#M003` **Permeability** -- Boundary openness
- `#M016` **SWAY** -- Influence dynamics
- `#M017` **SWARM** -- Collective intelligence model
- `#M022` **Synthetic Intelligence** -- Artificial cognition
- `#M099` **MemeGrid** -- Memetic control lattice

### Elemental Metal (MET-prefix) -- Mythological/Alchemical

10 terms covering metal-element archetypes and material culture.

- `#MET001` **Gold** -- Noble metal as structural archetype
- `#MET002` **Silver** -- Lunar metal, healing properties
- `#MET003` **Iron** -- Martial structure and force
- `#MET004` **Blacksmith** -- Transformative craft
- `#MET006` **Alchemical Gold** -- Transmutation and perfection
- `#MET008` **Swords to Plowshares** -- Transformation of purpose
- `#MET010` **Star State** -- Stellar metallurgy

### Meta-Synthesis (META-prefix) -- Cross-Elemental

- `#META001` **Nemetic Pattern** -- The pattern that recognizes patterns

### Narrative (N-prefix) -- Construction Processes

- `#N001` **Narrative Construction** -- How stories are built
- `#N002` **Devolution** -- Decentralization of power

### Openness (O-prefix) -- Permeability

- `#O001` **Omega Permeability** -- Ω-boundary openness measure

### Underdetermination (U-prefix) -- Epistemic Conditions

- `#U001` **Underdetermination** -- When evidence doesn't determine theory

### Water (W-prefix) -- Worldview & Resonance

10 terms covering cosmological frameworks and relational ontologies.

- `#W001` **Thales' Arche** -- Water as first principle
- `#W002` **Anaximander's Apeiron** -- The boundless as origin
- `#W006` **Ahmed Orientation** -- Queer phenomenology of direction
- `#W008` **Bohm-Pribram Holographic** -- Holographic universe model
- `#W009` **Cyberanimism** -- Digital animism

### Wood (WO-prefix) -- Growth & Exploration

- `#WO001` **Yggdrasil** -- World tree as branching archetype
- `#WO007` **Tentacular Thinking** -- Haraway's non-hierarchical thought

### Psychology (P-prefix) -- Behavioral Science

- `#P001` **Self-Efficacy Theory** -- Bandura's framework

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
- Check `hex_registry.yaml` for the authoritative list of all tag assignments

---

*The database grows continuously. ε is preserved in every entry.*
