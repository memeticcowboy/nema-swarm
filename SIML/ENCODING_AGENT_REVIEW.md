# SIML Encoding Agent Review — Critical Thinking Terms

**Date:** 2026-03-03
**Scope:** Review of cron-based SIML encoding agent output in `SIML/terms/` against source material in `SWARM_BASE/Critical Thinking/`

---

## Executive Summary

The encoding agent had produced **450 term folders** in `SIML/terms/`, of which **136 were C-series** (Critical Thinking domain). Audit uncovered three systemic problems:

1. **Massive duplication** — the same source concept was encoded multiple times under different hex tags, with different (inconsistent) nemetic strings each time
2. **Hex tag collisions** — different concepts share the same hex tag number
3. **Low coverage** — only **99 of 386** source files (25.6%) in `Critical Thinking/` had been encoded

### Cleanup Performed (2026-03-03)

- **Removed 104 duplicate term directories** (34 C-series, 52 D-series, 15 L-series, 4 cross-series)
- **Removed 98 encoded source files** from `Critical Thinking/` (already encoded into SIML terms)
- **After cleanup:** 346 term folders remain in `SIML/terms/`; 288 source files remain in `Critical Thinking/` awaiting encoding
- **Remaining issues:** 16 hex tag collisions still need manual resolution; `swarm_base_01.md` inconsistencies remain

---

## Problem 1: Content Duplicates (Same Concept, Multiple Hex Tags)

### C-Series Duplicates (28 duplicate pairs/groups)

The agent re-encoded the same concept under new hex tags rather than recognizing it had already been processed. Each re-encoding produces a **different** nemetic string, which means the encodings are inconsistent rather than identical copies.

Example — "Subconscious Games in Decision-Making" was encoded **3 times**:

| Term | Nemetic String | Tag |
|------|---------------|-----|
| C012 | `Φ(SubconsciousGames) = σ(hidden\|manifest) ∘ ρ(automatic\|deliberate) ∘ λ(avoidance\|awareness) ∘ β(pattern\|choice) ∘ δγ(repetition\|growth) ∘ μ(illusion\|reality) + ε \| :illuminating` | `:illuminating` |
| C059 | `Φ(SubconsciousGames) = σ(hidden\|explicit) ∘ ρ(influence\|awareness) ∘ λ(revelation\|concealment) ∘ β(pattern\|chaos) ∘ δγ(belief\|truth) ∘ μ(boundary\|transgression) + ε \| :awakening` | `:awakening` |
| C136 | `Φ(SubconsciousGames) = σ(hidden\|explicit) ∘ ρ(unawareness\|awareness) ∘ λ(influence\|autonomy) ∘ β(pattern\|breakthrough) ∘ δγ(routine\|reflection) ∘ μ(automatic\|conscious) + ε \| :revealing` | `:revealing` |

**Full list of C-series exact-name duplicates:**

| Concept | Duplicate Terms | Count |
|---------|----------------|-------|
| subconscious_games_decision_making | C012, C059, C136 | 3x |
| mastering_critical_thinking_skills | C027, C035, C076 | 3x |
| ai_emotions_truthfulness_security | C031, C081 | 2x |
| analyzer_cyborg | C038, C102 | 2x |
| beliefs_structure_impact | C014, C062 | 2x |
| brain_learning_ux | C029, C077 | 2x |
| clausewitz_wondrous_trinity | C032, C075 | 2x |
| cognitive_adaptability_ai | C036, C058 | 2x |
| collective_cognition | C025, C070 | 2x |
| consciousness_reductionism_debate | C008, C040 | 2x |
| contrarian_thinking | C016, C064 | 2x |
| epistemic_challenges_open_societies | C024, C069 | 2x |
| heuristics_and_biases | C019, C052 | 2x |
| human_behavior_ai_training | C044, C078 | 2x |
| ignorance_map | C004, C056 | 2x |
| jazz_improvisation_neural_mechanisms | C023, C068 | 2x |
| meditation_bci_control | C022, C067 | 2x |
| modular_intelligence | C039, C090 | 2x |
| multiple_intelligences_theory | C049, C085 | 2x |
| post_singularity_education | C017, C060 | 2x |
| principle_of_bivalence | C054, C126 | 2x |
| psilocybin_brain_activity | C026, C072 | 2x |
| psychological_power_of_words | C030, C046 | 2x |
| quantum_entanglement_consciousness | C028, C092 | 2x |
| social_context_cognition | C013, C061 | 2x |
| status_quo_bias | C018, C065 | 2x |
| wisdom_focused_collaborative_ai | C020, C066 | 2x |

**Near-duplicates (similar concepts, different names):**

| Concept | Terms |
|---------|-------|
| authority/influence | C010_authority_influence, C034_authority_figure_influence |
| essential questions | C047_essential_questions, C083_essential_questions_inquiry, C088_art_of_essential_questions |
| memory storage | C048_memory_storage_mechanism, C084_brain_memory_storage_mechanism |
| cognitive biases | C050_cognitive_biases, C087_cognitive_biases_quirks |
| knowledge/learning | C015_knowledge_learning, C063_knowledge_learning_wisdom |
| quantum brain | C033_quantum_entanglement_brain, C082_quantum_entanglement_brain_function |

### D-Series Duplicates (SEVERE — 56 of 69 terms are duplicates)

The Democracy domain is the worst affected. The agent appears to have re-encoded the same ~7 core concepts dozens of times with variant suffixes:

| Base Concept | Number of Copies |
|-------------|-----------------|
| democracy_networked_age | ~12 variants |
| liquid_democracy | 8 variants |
| memetic_governance | 8 variants |
| integrated_civic_symbolic_stack | 5 variants |
| epistemic_justice | ~8 variants |
| technocratic_plateau | ~7 variants |
| integrated_governance_synthesis | 3 variants |
| deliberation_attention_economy | 2 variants |

Only ~13 of 69 D-series terms appear to be unique concepts (D001-D008, D030, D031, D042, D056, D069).

### L-Series Duplicates (14 exact-name duplicate pairs)

| Concept | Original | Duplicate |
|---------|----------|-----------|
| Cognitive Load Theory | L011 | L086 |
| 4E Cognition | L012 | L088 |
| Social Learning Theory | L013 | L089 |
| Situated Learning | L014 | L090 |
| Self Determination Theory | L015 | L091 |
| Transformative Learning Theory | L016 | L092 |
| Constructionism | L017 | L093 |
| Experiential Learning | L018 | L094 |
| Spaced Repetition | L019 | L095 |
| Flow Theory | L020 | L096 |
| Elaboration Theory | L031 | L053 |
| Cognitive Flexibility Theory | L033 | L056 |
| Discovery Learning | L034 | L071 |
| Cognitive Apprenticeship | L028 | L059 |
| Pedagogical Content Knowledge | L058 | L082 |

---

## Problem 2: Hex Tag Collisions (Same Number, Different Concepts)

These terms share a hex tag number, meaning the tag is no longer a unique identifier:

| Tag | Concept 1 | Concept 2 |
|-----|-----------|-----------|
| A060 | Actual_Occasion | Attention_Fragmentation |
| C001 | Confabulation | critical_thinking_definitions |
| E012 | Ethnomethodology | Structural_Coupling |
| E013 | Contexture | Sense_Making |
| E015 | Sequential_Organization | Whitehead_Concrescence |
| E016 | Discursive_Psychology | Mycorrhizal_Network |
| M001 | Gold | Multiplicity |
| M002 | Silver | Authenticity |
| M003 | Iron | Permeability |
| M004 | Blacksmith | Metabolism |
| M005 | Metal_in_Wu_Xing | Triality |
| M006 | Alchemical_Gold | Fractal_Depth |
| M007 | Silver_Healing | Distinction |
| M008 | Swords_to_Plowshares | Stewardship |
| M009 | Strategic_Metals_Dependency | Tertiary_Emergence |
| M010 | Star_State | Tertiary_Retention |

The M-series collisions (M001-M010) appear to be from two separate encoding passes — one for elemental/mythological Metal concepts, one for abstract/nemetic concepts — that both started numbering at M001.

---

## Problem 3: Coverage Gap

### By the Numbers

| Metric | Count |
|--------|-------|
| Total Critical Thinking source files | 386 |
| Unique source files referenced by terms | 99 |
| Source files NOT yet encoded | **289 (74.9%)** |
| C-series terms missing `source_file` field | 36 |

### Terms Missing Source File Provenance

These 36 C-series terms have no `source_file` field in their `term.yaml`, making it impossible to trace them back to their source material:

C001_Confabulation, C004_ignorance_map, C012-C029 (range), C031-C036, C038-C040, C044, C046-C050, C089_psilocybin_ego_dissolution, C136_subconscious_games_decision_making

**Pattern:** The C012-C050 range appears to be an earlier encoding pass that did not track source files. The C056-C136 range (later pass) does include `source_file` references. This suggests the agent was improved at some point to add provenance tracking, but the older terms were never backfilled.

### One Source File Encoded Twice

`1771907212350_232647_.md` was encoded into both `C054_principle_of_bivalence` and `C126_principle_of_bivalence` — an exact duplicate from the same source.

---

## Problem 4: swarm_base_01.md Inconsistencies

The glossary file `SWARM_BASE/swarm_base_01.md` (9,295 lines, 157 entries) has its own issues:

### Internal Duplicates
23 term names appear 2+ times in swarm_base_01.md with different hex tags. Notable triples:
- "Subconscious Games in Decision-Making" appears at C012, C021, and C059
- "Status Quo Bias" appears at C018, C065, and A053
- "Mastering Critical Thinking Skills" appears at C027, C035, and C076

### Hex Tag Conflict: C021
Within swarm_base_01.md, hex tag **#C021** is assigned to two different terms:
- "Scientist Mindset" (line ~2296)
- "Subconscious Games in Decision-Making" (line ~4778)

### Tag Mismatch Between swarm_base_01.md and SIML/terms/
**A059** is assigned to "AI Cognitive Offloading" in swarm_base_01.md but to `A059_Hyperobject` in SIML/terms/ — a completely different concept. Meanwhile, SIML/terms/ has AI Cognitive Offloading at `A038_AI_Cognitive_Offloading` instead.

### 19 Orphaned Tags
19 hex tags in swarm_base_01.md have no corresponding directory in SIML/terms/:
`A042, A043, A044, A046, A047, A048, A049, A04B, A04C, A04E, A04F, A050, A051, A052, A054, A056, A05C, A05D`, and the second C021 usage.

Some of these topics DO exist in SIML/terms/ under different tags (e.g., swarm_base's `A043_Barnum_Effect` corresponds to SIML/terms' `A01B_Barnum_Effect`).

### Cross-Series Duplicates
Some concepts are duplicated across different series prefixes:
- `Chthulucene`: E007 and WO009
- `Cognitive_Dissonance`: A01A and P005
- `Wu_Xing_Wood`: WO002 and WO011
- `Status_Quo_Bias`: A053, C018, and C065
- `Cognitive_Flexibility_Theory`: L033, L056, and P008
- `Connectivism`: L023 and P009

---

## Root Cause Analysis

The encoding agent likely suffers from:

1. **No deduplication check** — Before encoding a new term, the agent does not check whether a term with the same name or from the same source file already exists in `SIML/terms/`
2. **No hex tag registry** — The agent assigns hex tags without consulting a central registry, leading to collisions when multiple encoding passes use overlapping number ranges
3. **Stateless cron execution** — Each cron run appears to process source files independently without tracking which files have already been processed
4. **Multiple encoding passes with different configurations** — The D-series variants (e.g., `_ist`, `_sr`, `_istf`, `_expanded`, `_base`) suggest the agent was run with different encoding modes that each produced a separate encoding of the same concept

---

## Recommendations

1. **Deduplicate existing terms** — For each duplicate group, select the canonical version (prefer the one with `source_file` provenance) and remove or archive the others
2. **Implement a processed-files manifest** — Before encoding, check a manifest of already-processed source files to avoid re-encoding
3. **Implement hex tag registry** — Maintain a `hex_registry.yaml` that tracks all assigned hex tags to prevent collisions
4. **Backfill `source_file` for older terms** — The C012-C050 range needs source provenance added
5. **Process remaining 289 files** — Nearly 75% of Critical Thinking source material remains unencoded
6. **Reconcile D-series** — The Democracy domain needs significant cleanup; 56 of 69 entries are variants of 7 core concepts
