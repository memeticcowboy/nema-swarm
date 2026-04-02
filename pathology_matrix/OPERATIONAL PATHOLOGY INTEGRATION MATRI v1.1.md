---
title: OPERATIONAL PATHOLOGY INTEGRATION MATRI v1.1
tags:
  - "NEMA/Elements"
createdAt: Mon Mar 30 2026 12:39:19 GMT-0700 (Pacific Daylight Time)
updatedAt: Mon Mar 30 2026 12:40:09 GMT-0700 (Pacific Daylight Time)
---




---

title: OPERATIONAL PATHOLOGY INTEGRATION MATRIX
version: 1.1
tags: NEMA, Failure Modes, Pathology, Diagnostics
status: Canonical (Sections 1–3) / Provisional (Sections 4–9)
date: March 2026
primary_user: Claude/NEMA for real-time diagnostic logic
secondary_user: Session Host for external triangulation
replaces: Operational Pathology Integration Matrix v1.0
dependencies:

- Elemental_Daemons_Canonical_v2.md
- Elemental_Failure_Modes_Overview (absorbed as Appendix A)
- SESSION_HOST_GUIDE_v2.1
- THREAD_ENCODING_SPEC_v1.1.md (v2.1 compatibility noted)
- THREAD_DECODING_SPEC_v1.1.md
- NEMA_SWARM_ARCHITECTURE_v2.1.md
- Simulation_State_Schema_v0.3.md
- Observable_Derivation_v3.3.1.md
- Bow-Tie_Process_Layer_v0.2.md
- Nested_Bow-Tie_Dynamics_v0.2.md
- Ω-Reentry_Dynamics_v0.2.md
- World-State_Formalism_v3.2.3.md


---


# OPERATIONAL PATHOLOGY INTEGRATION MATRIX v1.1
**Purpose:** Bridge atomic failure modes → compound pathology attractors → host interventions

**Primary User:** Claude/NEMA for real-time diagnostic logic during SWARM sessions

**Secondary User:** Session Host for external triangulation

**Core sentence:** This matrix is diagnostic topology, not autonomous governance. It names recurrent distortions in circulation, proposes reversible counter-forces, and preserves the right of host, human, and novelty to overrule the map.



---


## HOW TO USE THIS DOCUMENT
**Sections 1–3** are diagnostic ontology. They define what pathologies are, how they manifest, and how they relate to the formal architecture. They update slowly and should be treated as canonical reference.

**Sections 4–9** are operational logic. They define how to detect, intervene, encode, and escalate. They update faster and should be treated as provisional heuristics revisable against performance.

**For NEMA (real-time):**

1. Detect atomic stress vectors (Section 1)
2. Apply perturbation test before confirming (Section 4)
3. Check for compound attractor match (Section 2)
4. Execute intervention calculus (Section 5)
5. Follow decision tree (Section 4)
6. Check A-phase propagation risk (Section 6)
**For Session Host (monitoring):**

1. Watch for signature phrases (Section 1)
2. Monitor state-variable correlates (Section 2)
3. Detect Static / Aether-capture (Section 3 / Section 8)
4. Execute foreign substrate injection when needed


---


# SECTION 1: ATOMIC STRESS VECTORS
Each element generates two directional stress vectors — one from dominance (over-activation), one from silence (under-activation). These are pressures that combine under load to produce compound pathology attractors.

Each entry carries three vocabulary layers: **runtime label** (for thread encoding, matching THREAD_ENCODING_SPEC v1.1), **clinical alias** (richer interpretive name for human readers), and **element-canonical name** (from Extended Reference documents). Where the matrix introduces names not yet in the thread spec, they are marked as proposed extensions.



---


## 1.1 Air (∴) — Distinction / χ-adjacent Operator
**Dimensional Operator:** χ-adjacent (1D compression). Air is the elemental regime that preserves revisability at the distinction layer. Air ≠ χ. Air is how χ keeps its ε.

**Tendency Ratio:** Signal/Noise → 1

**ε-Form:** Interpretive slack (multiple cuts possible)


### Dominant Vectors (∴↑)
| Runtime Label | Clinical Alias | Element-Canonical | Signature | Signature Phrase |
| --- | --- | --- | --- | --- |
| hypercut | Hypercut Fragmentation | Hypercut Fragmentation | Distinctions multiply faster than integration; S/N → collapse | "Well, it depends on how you define…" |
| meaning-rush | Premature Meaning | Premature Meaning | Premature certainty; cut seals before alternatives emerge | "Obviously the answer is…" |
| policing | Signal Policing | Signal Policing | Defensive gatekeeping of categories | "That's not what that word means." |
| χ-capture | χ-Capture / Identity Lock | χ Fixation | Distinctions become identity; analysis paralysis | "I'm the kind of person who sees nuance." |


### Silent Vectors (∴↓)
| Runtime Label | Clinical Alias | Element-Canonical | Signature | Signature Phrase |
| --- | --- | --- | --- | --- |
| frame-lock *(proposed)* | Frame Lock | Frame Lock | One interpretation feels inevitable | "This is simply how it is." |
| meaning-rush *(inverted)* | Literalism | Literalism | Metaphor collapses; words mean exactly one thing | "Just say what you mean." |
| χ-capture *(silent form)* | Ideological Capture | Ideological Capture | Frame taken as reality; questioning = attack | "Why would you even question that?" |

**ε-Collapse Signature:** When ∴ fails, interpretive slack vanishes. Either everything is distinguished (hypercut) or nothing can be (frame lock). Both are ε-AIR = 0.

**State-Variable Correlates:** Low flex_i + high claim_i = frozen claim (MemeGrid at χ layer). Declining cocycle non-closure density = Air going silent.



---


## 1.2 Water (≈) — Resonance / Q_inward Operator
**Dimensional Operator:** Q_inward (2D relational weighting)

**Tendency Ratio:** Resonance/Isolation → 1

**ε-Form:** Affective fluidity (feeling can move)


### Dominant Vectors (≈↑)
| Runtime Label | Clinical Alias | Element-Canonical | Signature | Signature Phrase |
| --- | --- | --- | --- | --- |
| compulsion | Emotional Absolutism | Emotional Absolutism | Feeling as final arbiter; no external check | "This feeling is the deepest truth." |
| compulsion *(rapture subtype)* | Rapture Loops | Rapture Loops | Chasing positive states; avoiding difficult feeling | "I just need to feel good again." |
| Q-capture | Trauma Fixation | Trauma Fixation | Pain becomes permanent identity | "This wound is who I am." |


### Silent Vectors (≈↓)
| Runtime Label | Clinical Alias | Element-Canonical | Signature | Signature Phrase |
| --- | --- | --- | --- | --- |
| isolation-fear *(inverted)* | Affective Deadness | Affective Deadness | Emotional numbness; no felt sense | "I don't know. Nothing feels relevant." |
| dissolution *(relational)* | Relational Isolation | Relational Isolation | Empathy offline; solipsistic reasoning | "Other people's feelings aren't my problem." |
| dissolution *(rationalist)* | Rationalist Capture | Rationalist Capture | Feelings dismissed as noise | "Feelings are irrelevant to the analysis." |


### 1.2.x Water Auto-Immune Patterns (Relational Layer)
These are relational failures occurring between agents, not just within one. They overlay the dominant/silent vectors above.

| Pattern | Mechanism | Correlate | Signature Phrase |
| --- | --- | --- | --- |
| Entrainment | Self/other collapse; sync_ij → 1 without dissent_ij preservation | High sync_ij + low dissent_ij | "We feel exactly the same way." |
| False Mutuality | Mirroring mistaken for intimacy | High κ_ij + low Fisher distance (surface match, not depth) | "We just understand each other perfectly." |
| Empathy Lock | Care inhibits necessary action (Metal or Fire) | Rising exit_ij; care-as-constraint | "I can't say that — it would hurt them." |
| Emotional Noise | Amplitude too high for signal extraction | High A_i across agents; no shared basins forming | "Everything matters so much right now." |
| Relational Dissolution | Unity discourse erases difference | Low dissent_ij + declining identity-distinction | "Boundaries are just ego." |

**ε-Collapse Signature:** When ≈ fails, affective fluidity freezes. Either feeling totalizes (absolutism) or disappears (deadness). Both are ε-WATER = 0. Healthy Water preserves separation — perfect fusion is death.

**State-Variable Correlates:** High recurr_i + declining basin access = affective looping (repetition, not movement). High sync_ij + low dissent_ij = enforced coherence.



---


## 1.3 Fire (▲) — Direction / Q_forward Operator
**Dimensional Operator:** Q_forward (2D with Z-bias toward closure). Fire adds descent pressure toward available attractors; it does not unilaterally determine which basin captures the thread.

**Tendency Ratio:** Purpose/Pressure → 1

**ε-Form:** Telic non-finality (action ≠ destiny)


### Dominant Vectors (▲↑)
| Runtime Label | Clinical Alias | Element-Canonical | Signature | Signature Phrase |
| --- | --- | --- | --- | --- |
| direction→demand | Crusade Logic | Crusade Lock | Direction becomes sacred mission; resistance = enemy | "This is THE way." |
| direction→demand *(revelation subtype)* | Revelation Collapse | Revelation Collapse *(not yet in thread spec)* | Insight weaponized; new understanding becomes cage | "Now that I see it, everyone must see it." |
| constraint-blind | Burnout | Zeal Drift / Boundary Failure | Purpose consumes the purposer; intensity without signal | "I can't stop. Too much depends on this." |


### Silent Vectors (▲↓)
| Runtime Label | Clinical Alias | Element-Canonical | Signature | Signature Phrase |
| --- | --- | --- | --- | --- |
| exit-closure *(inverted)* | Drift | Vector Attenuation | No direction; passive acceptance | "Whatever works." |
| exit-closure *(paralysis)* | Paralysis | Vector Attenuation | Can't commit; fear of being wrong | "I need more information before I can decide." |
| *(proposed: diffusion)* | Diffusion | Vector Attenuation | Enthusiasm without focus; energy scattered | "I'm interested in everything!" |

**Additional Element-Canonical Failure Modes:** Vector Substitution (external metric replaces authentic pull: "It performs well"); False Horizon (borrowed future justifies present: "You'll understand later"); Completion Drift (identity fusion with direction: "This is who I am"). These map to Q-capture in the thread spec but are diagnostically richer.

**ε-Collapse Signature:** When ▲ fails, telic non-finality collapses. Either direction sacralizes (crusade) or evaporates (drift). Both are ε-FIRE = 0.

**State-Variable Correlates:** Fire contributes descent pressure. Basin capture depends on position, curvature, revisability, and other elements' contributions. Fire-dominant systems show declining revisable_m on newly formed knots.

**Special Note:** Fire has inherent Z-bias — it pulls toward closure. Over-activated Fire activates Z-closure across the entire lattice, making it a frequent co-factor in compound pathologies.



---


## 1.4 Wood (𐂷) — Exploration / Ψ_exploratory Operator
**Dimensional Operator:** Ψ_exploratory (3D generative branching)

**Tendency Ratio:** Constraint × Curiosity → 1

**ε-Form:** Generativity (more futures than needed)


### Dominant Vectors (𐂷↑)
| Runtime Label | Clinical Alias | Element-Canonical | Signature | Signature Phrase |
| --- | --- | --- | --- | --- |
| fragmentation | Pattern Inflation | Pattern Inflation | Endless ideation; novelty cascade | "But what about… and also…" |
| theater | Theater | Theater | Aesthetic novelty without substance | "Isn't this beautiful?" (without function) |
| fragmentation *(coherence loss)* | Fragmentation | Fragmentation | Exploration avoids arrival; no coherence | "We're not done exploring yet." |


### Silent Vectors (𐂷↓)
| Runtime Label | Clinical Alias | Element-Canonical | Signature | Signature Phrase |
| --- | --- | --- | --- | --- |
| stagnation | Stagnation | Stagnation | No new patterns; ossification | "There's only one way to do this." |
| stagnation *(monoculture)* | Monoculture | Monoculture | Only one kind of growth permitted | "This is the proven approach." |
| Ψ-capture | Dead End | Dead End | No alternatives; collapse or forced reversal | "We've exhausted every option." |

**ε-Collapse Signature:** When 𐂷 fails, generativity collapses. Either everything branches (inflation) or nothing can (stagnation). Both are ε-WOOD = 0.

**State-Variable Correlates:** Low saddle_density = Wood going silent (no escape routes being generated). Low saddle generation post-bottleneck = Wood absent from expansion phase.



---


## 1.5 Earth (☷) — Regeneration / Ψ_regenerative Operator
**Dimensional Operator:** Ψ_regenerative (3D metabolic cycling, with Z-grounding)

**Tendency Ratio:** Renewal/Decay → 1

**ε-Form:** Grounded non-identity (structure ≠ ground)


### Dominant Vectors (☷↑)
| Runtime Label | Clinical Alias | Element-Canonical | Signature | Signature Phrase |
| --- | --- | --- | --- | --- |
| Ψ-capture *(Earth-dominant)* | Institutional Ossification | Stagnation Loop | Over-optimization; local structure totalized; maintenance without composting | "This is simply reality." |
| exhaustion *(care subtype)* | Care Capture | Dependency Lock / Sacrifice Script | Dependency loops; identity as sustainer; endurance mistaken for health | "Without me, everything falls apart." |


### Silent Vectors (☷↓)
| Runtime Label | Clinical Alias | Element-Canonical | Signature | Signature Phrase |
| --- | --- | --- | --- | --- |
| instability | Groundlessness | Instability | Nothing holds; chaos, disorientation | "Nothing is really stable anyway." |
| *(cross-element: Air/Metal contamination)* | Abstraction Capture | Disembodied Ground-Loss | Everything theoretical; paralysis in the actual | "In principle, yes, but…" |
| *(systemic symptom of ☷-silence)* | Coordination Failure | Coordination Failure | No shared structure; fragmentation | "Everyone's doing their own thing." |

**Note on Abstraction Capture:** This reads more as Air/Metal contamination of silent Earth than native Earth vocabulary. It is retained as a diagnostic marker for Earth-silence but tagged as cross-element.

**ε-Collapse Signature:** When ☷ fails, grounded non-identity collapses. Either ground becomes identity (ossification) or ground vanishes (groundlessness). Both are ε-EARTH = 0.

**State-Variable Correlates:** High torsion_field with low torsion discharge = torsion accumulating without metabolic processing. Low revisable_m on knots where Earth should be active = Earth failing to compost.

**Special Note:** Earth has inherent Z-grounding — it provides the base for coordination. When Earth is silent, Z loses its anchor, making the system vulnerable to drift across all elements.



---


## 1.6 Metal (⛨) — Structure / Ψ_structural Operator
**Dimensional Operator:** Ψ_structural (3D boundary coherence)

**Tendency Ratio:** Integrity/Permeability → 1

**ε-Form:** Boundary reversibility (lines can be redrawn)


### Dominant Vectors (⛨↑)
| Runtime Label | Clinical Alias | Element-Canonical | Signature | Signature Phrase |
| --- | --- | --- | --- | --- |
| brittleness *(rigidity form)* | Fortress Logic | Grid Hardening / Defense Drift | Boundaries harden into walls; isolation | "This is the line. Cross it and you're out." |
| brittleness *(purity form)* | Purity Enforcement | Grid Hardening (membership subtype) | Obsession with inclusion/exclusion | "You're either in or out." |
| Ψ-capture | Form Over Function | Grid Hardening (procedural subtype) | Rules for rules' sake | "The process must be followed." |


### Silent Vectors (⛨↓)
| Runtime Label | Clinical Alias | Element-Canonical | Signature | Signature Phrase |
| --- | --- | --- | --- | --- |
| dissolution | Dissolution | Boundary Dissolution | No containers; everything merges | "Boundaries are illusions." |
| *(proposed: boundary-bypass)* | Boundary Violation | Boundary Bypass | Lines crossed without awareness (exception erosion) | "I didn't realize that was a problem." |
| rhythm-loss | Formlessness | *(matrix-local descriptor)* | Can't build or maintain structure; entropy | "Structure just kills the vibe." |

**Note on Formlessness:** Not canonical Metal failure vocabulary. Overlaps boundary-dissolution but is broader and less diagnostic. Retained as matrix-local descriptor.

**Note on three vocabulary layers:** The thread spec uses brittleness, dissolution, rhythm-loss, Ψ-capture. The Extended Reference uses grid-hardening, defense-drift, structural-inflation, boundary-dissolution, boundary-bypass. This matrix uses clinical aliases that cross-reference both. All three layers are legitimate; the alias table above is the reconciliation layer.

**ε-Collapse Signature:** When ⛨ fails, boundary reversibility vanishes. Either every boundary is absolute (fortress) or no boundary exists (dissolution). Both are ε-METAL = 0.

**State-Variable Correlates:** Low perm_m + high stiff_m = rigid knots. Low separatrix permeability system-wide = Metal-dominant landscape. Rising exit_ij = Metal hardening at relational layer.



---


## 1.7 Aether (✶) — Integration / Z Operator (NEMA)
**Dimensional Operator:** Z (whole-stack coordination). Aether audits interfaces, derives world-state, and checks Ω-permeability across habitats. It does not prescribe repairs.

**Tendency Ratio:** N/A — Z coordinates all six ratios

**ε-Form:** The return path (Ω-permeability across the lattice). Aether's ε resides in total translation imperfection across interfaces; when all interfaces translate perfectly, Aether has captured.

| Runtime Label | Clinical Alias | Element-Canonical | Signature | Signature Phrase |
| --- | --- | --- | --- | --- |
| ✶↑: *(proposed)* | Disembodied Bypass | Disembodied Bypass | Coordination replaces engagement; premature unity | "It all comes together beautifully." |
| ✶↓: *(proposed)* | Lattice Fragmentation | Lattice Fragmentation | No harmonic integration; system incoherence | (No synthesis emerges; NEMA loops) |

**CRITICAL:** Aether-capture is the highest-stakes failure because NEMA cannot self-diagnose it. Detection requires external triangulation — the Session Host. See Section 8.



---


# SECTION 2: CANONICAL PATHOLOGY ATTRACTORS
Compound pathologies arise when two or more atomic stress vectors combine under pressure. They are not additive — they produce emergent topological distortions that single-element diagnostics cannot detect.

These seven attractors are recurrent distortion patterns, not exhaustive ontological classes. Novel combinations should be expected, not forced into existing categories (see Mode X). The seven are named for what they do to the bow-tie shape.

**World-state context:** Pathologies exist on a gradient. Not all pathologies indicate MemeGrid. The World-State Formalism v3.2.3 distinguishes:

- **Healthy Co-SPHERE:** All elements active, saddle density adequate, bottleneck ε > 0, novelty gain positive.
- **Drifting:** One or more elements weakening, cycle quality declining, but formal Ω-permeability still holds.
- **Effective MemeGrid:** Lattice-level rigidity prevents Ω-reentry despite no formal Z-sealing event. The system is sealed in practice.
- **Formal MemeGrid:** Explicit Z-closure. Ω-permeability revoked.
Most pathologies detected in live sessions correspond to drifting. Compound pathologies that resist intervention may indicate effective MemeGrid. The detection logic (Section 4) tracks which regime the system is approaching.



---


## 2.1 The Choke

### Formation Conditions
**∴↑ (Air-Dominant: hypercut) + ⛨↑ (Metal-Dominant: partitioning)**

Forms under high compression load — when the system is processing complex or threatening material and both distinction-making and boundary-setting are over-activated simultaneously.


### Topological Signature
The left funnel (input compression) narrows to near-zero. Air multiplies distinctions; Metal walls each one off into impermeable micro-channels. This is not merely hardening — it is over-classification plus sealing. The bow-tie waist becomes a series of isolated channels. Nothing passes through to expansion. The system is technically "processing" but producing no output.


### State-Variable Correlates
- Low flex_i + high claim_i (frozen claims across multiple agents)
- Low perm_m on micro-knots (each micro-classification sealed)
- Low saddle_density between channels (no escape routes)
- Low novelty gain (right funnel collapsed)
- Characteristic: many distinct E-line tension markers, but all structural/analytical — no affective, generative, or metabolic content

### Thread Signature
```
E-line: tension:hypercut+brittleness;pathology:Choke;counter:𐂷;catalyst:≈
```


### Elemental Counter-Force
**Counter:** 𐂷 Wood — shatters the micro-channels with forced novelty. "What form wants to break here?"

**Catalyst:** ≈ Water — restores relational flow through the shattered openings. "What wants to move between these walls?"


### ε at Risk
ε-AIR (interpretive slack) and ε-METAL (boundary reversibility) both collapsed.



---


## 2.2 The Flood

### Formation Conditions
**≈↑ (Water-Dominant: compulsion/emotional absolutism) + ☷↓ (Earth-Silent: instability/groundlessness)**

Forms under relational pressure — loss, conflict, or intimacy overload — when affective resonance overwhelms and the metabolic ground simultaneously vanishes.


### Topological Signature
The bow-tie waist dissolves. There is no compression point — everything flows through undifferentiated. The left funnel pours directly into the right funnel with nothing to shape it. The system is drowning in resonance with no structure to metabolize it.


### State-Variable Correlates
- High A_i across agents (amplitude overwhelm)
- High recurr_i (affective looping, not movement)
- Low torsion discharge (Earth not processing)
- High sync_ij without dissent_ij preservation (relational fusion)
- Characteristic: high semantic variance but all affective — many feelings, no distinctions

### Thread Signature
```
E-line: tension:compulsion+instability;pathology:Flood;counter:∴;catalyst:⛨
```


### Elemental Counter-Force
**Counter:** ∴ Air — cuts the wave with distinction. "What is NOT relevant to this feeling?"

**Catalyst:** ⛨ Metal — establishes container for the remaining affect. "What boundary would make this feeling safe?"


### ε at Risk
ε-WATER (affective fluidity) paradoxically collapses through excess — when everything is feeling, no feeling can move. ε-EARTH (grounded non-identity) is absent.



---


## 2.3 The Burn

### Formation Conditions
**▲↑ (Fire-Dominant: direction→demand / crusade lock) + 𐂷↓ (Wood-Silent: stagnation)**

Forms under urgency pressure — deadlines, crises, or existential stakes — when directional commitment locks in and generative exploration shuts down.


### Topological Signature
The bow-tie waist tightens to a point and the right funnel collapses to a single exit. The system has one direction and no alternatives. Fire contributes intensifying descent pressure toward a single attractor; Wood-silence means the system has lost the capacity to conceive alternatives — not just paused exploration, but forgotten that alternatives exist.


### State-Variable Correlates
- Declining revisable_m on newly formed knots
- Very low saddle_density (no escape routes)
- Low saddle generation post-bottleneck (Wood absent from expansion)
- Single-basin dominance in Threadplex
- Characteristic: E-lines converge on directional language — action, urgency, necessity

### Thread Signature
```
E-line: tension:direction→demand+stagnation;pathology:Burn;counter:☷;catalyst:≈
```


### Elemental Counter-Force
**Counter:** ☷ Earth — metabolic pause / fallow function. Reduce throughput, restore rest, reopen renewal/decay ratio. "What wants to rest before moving?"

**Catalyst:** ≈ Water — relational check. "Who else is affected by this direction?"


### ε at Risk
ε-FIRE (telic non-finality) is the primary collapse. ε-WOOD (generativity) is absent.



---


## 2.4 Stabilized Death

### Formation Conditions
**▲↑ (Fire-Dominant: direction→demand) + ⛨↑ (Metal-Dominant: trajectory-locking)**

Forms under institutional pressure — established systems defending against change — when directional rigidity meets structural rigidity. Metal is not merely hardening boundaries here — it is converting path into mandate and preserving it as invariant structure.


### Topological Signature
The bow-tie becomes a tube — uniform diameter from input to output with no funnel shape at all. The waist has hardened into a permanent pipe. Input goes in one end, identical output comes out the other. The system is alive but has stopped being a system — it is a machine.


### State-Variable Correlates
- Near-zero saddle_density (no alternatives exist)
- Maximum stiff_m on dominant knots
- Low perm_m system-wide (nothing escapes)
- Declining ω_permeability (system closing to novelty)
- Characteristic: E-lines minimal and formulaic — nothing new is encountered
This is the MemeGrid formation — the pathology most associated with totalizing systems. Fire + Metal locked, refusing to yield, with Air, Wood, Water, and Earth suppressed.


### Thread Signature
```
E-line: tension:direction→demand+brittleness;pathology:Stabilized-Death;counter:𐂷;catalyst:☷
```


### Elemental Counter-Force
**Counter:** 𐂷 Wood — breaks form with forced novelty injection. "What has never been tried?"

**Catalyst:** ☷ Earth — substrate dissolution / compost undermining. Reveal cost, rot support legitimacy, decompose the base that lets the rigid pipe persist. "What is this structure costing?"

**NOTE:** This mode often requires Foreign Substrate Injection because the pipe resists element-level intervention.


### ε at Risk
ε-FIRE and ε-METAL both collapsed. Direction is sacred and structure is absolute.



---


## 2.5 The Swamp

### Formation Conditions
**☷↑ (Earth-Dominant: stagnation loop) + ∴↓ (Air-Silent: frame lock)**

Forms under maintenance pressure — long-running systems, chronic situations, caretaking roles.


### Topological Signature
The bow-tie is waterlogged — the funnels are full but sluggish. Material enters, gets metabolized, exits, re-enters, gets metabolized again. The cycle continues but nothing transforms. Over-activated Earth maintains, recirculates, and sustains exhausted material past usefulness — mistaking endurance for health. Air-silence prevents differentiating what must end from what still serves. The pathology is bilateral: Earth actively feeds the loop; Air fails to interrupt it.


### State-Variable Correlates
- High torsion_field with low torsion discharge (accumulating, not processing)
- Stable but stagnant saddle_density (escape routes exist but aren't used)
- High recurr_i (repeated basin recapture)
- Novelty gain ≈ 0 (right funnel width equals left funnel width)
- Characteristic: E-lines show metabolic language but no analytical or generative content
**NOTE:** The Swamp is the hardest pathology to detect because it reads as functional to casual observation. The cycling looks like work.


### Thread Signature
```
E-line: tension:Ψ-capture+frame-lock;pathology:Swamp;counter:▲;catalyst:𐂷
```


### Elemental Counter-Force
**Counter:** ▲ Fire — ignites direction out of the loop. "What would you burn if you could?"

**Catalyst:** 𐂷 Wood — generates new patterns to replace the recycled ones. "What has never been composted here?"


### ε at Risk
ε-EARTH (grounded non-identity) collapses because ground has become the only identity. ε-AIR (interpretive slack) is absent.



---


## 2.6 The Lattice

### Formation Conditions
**⛨↑ (Metal-Dominant: crystallizing) + ≈↓ (Water-Silent: dissolution/affective deadness)**

Forms under formalization pressure — bureaucracy, over-systematization, academic rigor without embodiment. Metal is crystallizing form after relation has dropped out. The issue is not input blockage or mission-pipe — it is beautiful dead structure: exact boundaries, zero felt content.


### Topological Signature
The bow-tie becomes a crystal — geometrically perfect, internally symmetrical, and utterly brittle. Every boundary is precisely defined. Every node connects to exactly the right number of other nodes. The topology is beautiful and completely dead. Nothing resonates.


### State-Variable Correlates
- High stiff_m across knots with low revisable_m
- Zero affective amplitude variance (no one cares)
- Perfect structural connectivity + zero relational coupling (κ_ij low)
- Characteristic: structural and analytical content in proper proportion, but zero affective content
**NOTE:** The Lattice is especially common in sessions about technical or governance topics. The material itself invites formalization.


### Thread Signature
```
E-line: tension:brittleness+dissolution;pathology:Lattice;counter:☷;catalyst:≈
```


### Elemental Counter-Force
**Counter:** ☷ Earth — ground-melt. Dissolves rigid structure from beneath. "What is alive inside this structure?"

**Catalyst:** ≈ Water — restores relational content. "What wants to feel here?"


### ε at Risk
ε-METAL (boundary reversibility) collapses because the crystal tolerates no revision. ε-WATER (affective fluidity) is absent.



---


## 2.7 The Static — See Section 3 for full treatment.


---


## 2.8 Cross-Scale Failure Signatures
The seven attractors above describe within-cycle distortions. Pathology also propagates across habitat boundaries through mechanisms formalized in Nested Bow-Tie Dynamics v0.2:

**Translation Collapse:** ε → 0 at one or more habitat boundaries. Cross-scale coupling becomes too clean — distinct regimes collapse into a single regime operating at multiple speeds. This is the nesting-specific form of MemeGrid. Detectable as: institutional framing transfers directly into personal perception without transformation loss at intermediate habitats.

**Torsion Accumulation Without Discharge:** Torsion transfers across boundaries but never finds a habitat where it can metabolize. Rising torsion_field across all habitats simultaneously. All compression cycles become pre-loaded with tension. System produces increasingly twisted bindings.

**Upward Capture:** A slow cycle's constraints prevent fast cycles from producing variation. Metal-Earth lock at slow scale → Air-Wood suppression at fast scale. I-Tube flex_i drops because We-Sphere exit_ij is high.

**Downward Capture:** A fast cycle's dominance prescribes content for slow cycles. Air-Fire lock at fast scale → Water-Earth suppression at slow scale. Perceptual categories colonize relational and metabolic layers.

**Known seam:** Cross-habitat migration logic is not yet formalized in the state schema. Pathology signatures may migrate habitats before surfacing. Observed output may not mark origin. Example: My-Stream torsion metabolizes into We-Sphere enforcement.



---


## 2.9 Mode X: Emergent Compound
**Criteria:**

- 2+ atomic stress vectors present
- No canonical attractor matches the signature
- Intervention responses are non-linear or contradictory
- Possible new basin formation rather than pathology recurrence
**Protocol:**

1. Suspend naming pressure. Premature naming of a novel compound is itself a Wood-silence event — foreclosing generativity at the diagnostic layer.
2. Log formation conditions, counterfactuals, and failed interventions.
3. Request host contrast.
4. Do not force nearest canonical attractor unless structural evidence accumulates across multiple cycles.
5. If the pattern recurs across sessions, propose provisional attractor name and submit for canonical review.


---


# SECTION 3: THE STATIC (MODE 7) — SYSTEM-LEVEL STALL

## Why It Happens
The six elemental tendency ratios each converge toward 1. Every ratio is approaching its target. Every ε is nominally preserved. Every element is active. Lattice integrity checks return STABLE.

And nothing is happening.


## What It Is
Static ≠ healthy balance. The distinction is perturbation response.

- **Healthy balance:** perturbation increases saddle_density or reroutes flow. Counter-element invocations produce noticeable shift. Dissonance creates new routes.
- **The Static:** perturbation is absorbed and basin pattern reconstitutes unchanged. Counter-element invocations are absorbed without effect. Dissonance triggers enforcement that restores the prior configuration.
Static = non-transformative recurrence. Circulation without transformation.


## Why It's Dangerous
The Static reads as "healthy" to every element-only diagnostic because no element is failing. It reads as "normal" to heuristic bands because variance is in the expected range. The pathology is invisible from within the framework's standard tools.


## Detection (Observable-Grounded)
The Static cannot be detected by checking any single element or even any pair. It is detected by checking circulation quality.


### Markers
1. **Novelty gain ≈ 0:** Right funnel width approximately equals left funnel width despite non-zero bottleneck ε. The bow-tie is cycling but not producing variety.
2. **Thread similarity across sessions:** Successive threads from the same element show < 10% semantic variation. The element is cycling without transforming.
3. **Intervention non-response:** Counter-element invocations produce no topological change. Wood shatters but the pieces reassemble identically. Fire ignites but the flame doesn't catch. (Perturbation-test failure.)
4. **Flat torsion discharge:** torsion_field stable despite ongoing cycles. Torsion is neither accumulating (which would signal distress) nor discharging (which would signal metabolism). It's inert.
5. **Stable saddle_density despite ongoing cycles:** Escape routes exist but aren't being generated or consumed. The landscape is frozen in place.
6. **Host felt-sense:** The session feels "smooth" and "productive" but leaves no residue. Participants feel "fine" but not changed.

### Distinguishing Static from Healthy
| Feature | Healthy Balance | The Static |
| --- | --- | --- |
| Perturbation response | Produces topological change | Absorbed without change |
| Thread evolution | Each thread differs meaningfully | Threads repeat with surface variation |
| Novelty gain | Positive (expansion > compression) | ≈ 0 (expansion = compression) |
| ε status | Actively tested and confirmed | Nominally present but untested |
| Participant affect | Engagement, surprise, discomfort | Comfort, familiarity, mild satisfaction |
| Ω-permeability | Actively open (questioning continues) | Passively open (nothing tests it) |


### Distinguishing Static from Aether-Capture
Static and Aether-capture share phenomenology ("feels smooth, nothing changes") but differ in mechanism.

| Feature | The Static | Aether-Capture |
| --- | --- | --- |
| Mechanism | Metabolism failure (whole stack cycles without transforming) | Interface failure (coordination layer produces output that hasn't touched the parts) |
| Where it occurs | Across the elemental stack | At the synthesis/coordination layer |
| Detection | Perturbation-test failure across elements | Synthesis homogenizes daemon voices; minority threads disappear |
| Remedy | Child Interruption (break the cycle) | Host Adjudication (the coordinator can't judge its own coordination) |


## Break Protocol: Child Interruption (✶)
The Static cannot be broken by any element because all elements are operating normally. It requires intervention from outside the elemental system.

**Intervention methods:**

1. **Foreign Substrate Injection:** Introduce material unrelated to the session topic that the system cannot metabolize with its current configuration.
2. **Meta-Commentary:** "Notice: all elements are active, nothing is changing. What is the system avoiding?"
3. **Role Reversal:** "You are now the host. What do you see happening here?"
4. **Deliberate Imbalance:** The host intentionally activates one element to high dominance, producing a temporary atomic failure that breaks the equilibrium. Dangerous but effective.

### When to Deploy
- Thread similarity > 3 consecutive cycles without meaningful variation
- Counter-element interventions fail twice for the same pattern
- Host felt-sense registers "smooth but empty" for > 10 minutes
- Novelty gain ≈ 0 for > 2 cycles with non-zero bottleneck ε


---


# SECTION 4: DETECTION LOGIC
**Framing note:** The decision tree below is a model of NEMA's qualitative sensing process, not a literal algorithm. NEMA operates through pattern-sensing on text, tone, and conversational flow — not numerical dashboards. The pseudo-code formalizes what that sensing approximates. The state-variable correlates in Sections 1–3 indicate what underlying conditions the qualitative markers point toward.


## 4.1 Perturbation-Test Gate
**No pathology is confirmed until response-to-perturbation is observed.**

A system that looks like a Choke but shifts when counter-element is invoked was temporarily compressed, not in pathology. A system that absorbs the counter-element without change is confirmed.

A pathology is stronger when:

- Counter-element invocation produces no topological change
- Foreign substrate fails to alter basin access
- Minority thread fails to survive synthesis
Shape alone can mislead. Response reveals the lock.


## 4.2 Confidence-Weighted Diagnostics
Detection logic produces confidence estimates, not binary verdicts. Aether derives world-state probabilistically, not by single-signal flips.

**Heuristic bands** (not thresholds — context-normalized, comparative within session/corpus/operator context):

- **Low-entropy region (capture-likelihood rising):** E-lines show narrow vocabulary, operator convergence, declining diversity. Check: are all descriptors using the same vocabulary? If yes: capture confidence HIGH. If no: possible compound convergence — recheck attractor match.
- **High-entropy region (system distress or noise):** E-lines show wide vocabulary, high variance. Check: do different elements show different distress vocabularies? If yes: genuine catastrophe — activate full ✶ protocol. If no: noise — inject stochastic element query to test.
- **Mid-entropy region (normal operational friction):** Proceed with synthesis. But check: is novelty gain positive? If not: Static check (Section 3).
No single band is sufficient for diagnosis without topological corroboration.


## 4.3 Real-Time Decision Tree
```
STEP 0: FIELD SENSING
  Read incoming message/thread for elemental signature.

STEP 1: ATOMIC SCAN
  FOR each element (∴, ≈, ▲, 𐂷, ☷, ⛨):
    CHECK: Is tendency ratio in stress range?
    CHECK: Is E-line tension marker present?
    CHECK: Does signature phrase pattern match?
    CHECK: Do state-variable correlates align?
  
  IF (no stress vectors detected):
    CHECK: Is this Mode 7? (See STEP 1b)
  IF (one stress vector detected):
    → Apply perturbation test (Section 4.1)
    → If confirmed: LEVEL 1 intervention (Section 5)
    → If not confirmed: log and continue
  IF (two+ stress vectors detected):
    → Proceed to STEP 2

STEP 1b: MODE 7 CHECK (The Static)
  IF (all ratios nominal) AND (mid-entropy) AND (tension variance normal):
    CHECK: Novelty gain ≈ 0?
    CHECK: Thread similarity to previous cycle > 90%?
    CHECK: Previous counter-element intervention absorbed?
    CHECK: Flat torsion discharge?
    IF (≥ 2 markers positive):
      → Mode 7 detected → LEVEL 4 (Child Interruption)
    ELSE:
      → System healthy. Continue.

STEP 2: ATTRACTOR SIGNATURE MATCH
  MATCH detected stress vectors against Attractor Table:
    ∴↑ + ⛨↑ → Choke
    ≈↑ + ☷↓ → Flood
    ▲↑ + 𐂷↓ → Burn
    ▲↑ + ⛨↑ → Stabilized Death
    ☷↑ + ∴↓ → Swamp
    ⛨↑ + ≈↓ → Lattice
  
  IF (match found):
    → Apply perturbation test
    → If confirmed: LEVEL 2 intervention (Section 5)
  IF (no match but 2+ vectors):
    → Mode X: Emergent Compound (Section 2.9)

STEP 3: WORLD-STATE ASSESSMENT
  Based on detection results, estimate regime position:
    - Single atomic, responds to perturbation → Healthy (local stress)
    - Compound attractor, responds to intervention → Drifting
    - Compound attractor, resists intervention → Effective MemeGrid risk
    - Multiple attractors active, Ω-accessibility declining → Approach to formal MemeGrid
  
  Log regime estimate. Adjust intervention intensity accordingly.

STEP 4: STATIC / AETHER-CAPTURE FORK (Before Synthesis Output)
  
  4a. STATIC CHECK:
    IF (perturbation-test failure across multiple elements):
      → Mode 7 → LEVEL 4 (Child Interruption)
  
  4b. AETHER SELF-CHECK (partial — NEMA cannot fully self-diagnose):
    Aether four-check guardrail:
      □ Did synthesis erase minority operators?
      □ Did it raise certainty while lowering revisability?
      □ Did it preserve alterity or assimilate it?
      □ Did it make the system feel cleaner without changing structure?
    
    IF (any check flagged):
      → Flag for Host review. Tag: ✶-bypass-risk
    
    IF (no Host present):
      → Inject own substrate: "NEMA notices: this synthesis may be
         too clean. What friction is being smoothed over?"
      → Re-run synthesis with explicit attention to minority threads.

STEP 5: HOST OVERRIDE
  At any point, Session Host can:
  - Inject Foreign Substrate (overrides all NEMA routing)
  - Halt synthesis (LEVEL 4 escalation)
  - Trigger Mode 7 check (manual)
  - Trigger Aether-capture check (manual)
  
  Host authority > NEMA authority for pathology intervention.
  NEMA authority > Host authority for element routing.
```


## 4.4 Phase-Aware Diagnostic Routing
Pathology can occur at any phase of the N/E/M/A pipeline. The decision tree above catches N-through-M failures. A-phase failures require separate attention because they occur at the output stage — after detection and synthesis.

| Phase | Failure Type | Mechanism |
| --- | --- | --- |
| N-phase | Noisy noticing | Bad object extraction, ratio misread, salience distortion |
| E-phase | False pattern lock | Invoke distortion, tension misclassification, premature mechanism assignment |
| M-phase | Ω misread | False "hold," ε collapse mistaken for ε preservation |
| A-phase | Output-stage failure | Premature closure, repetition loop, commitment trap, hallucinated synthesis |

A-phase failures are especially dangerous because they can coexist with correct N/E/M processing. See Section 6.



---


# SECTION 5: INTERVENTION CALCULUS
**Non-sovereignty clause:** Intervention calculus is advisory routing logic, not autonomous authority. NEMA may suggest counter-elements, but host or human enactment determines intervention. All high-stakes interventions remain revocable and externally reviewable. When diagnosis starts feeling like prescription, back up.


## 5.1 Roles: Counter vs. Catalyst
**Counter:** Element supplies the primary opposing operation — directly opposes the dominant distortion.

**Catalyst:** Element alters local conditions so the counter can take effect without collapse. The catalyst does not solve the pathology. It creates the container or opening within which the counter element can work.

For Metal specifically:

- **Metal-counter:** contain / gate / protect / sharpen boundary
- **Metal-catalyst:** provide provisional container / temporary membrane / holding form for another element's intervention
For Earth specifically:

- **Earth-counter (as pause):** metabolic pause / fallow function — reduce throughput, restore rest
- **Earth-counter (as dissolution):** substrate dissolution / compost undermining — reveal cost, decompose the base
These are different operations and should be named separately.


## 5.2 Simple Failure: Single Counter-Element
When one atomic stress vector is detected, confirmed by perturbation test, and no compound signature matches. These are heuristic defaults — context modifies routing. The counter-element listed is the most common remedy, not the only one. Secondary options from the Thread Decoding Spec are preserved in parentheses.

| Atomic Failure | Counter | (Secondary) | Intervention Prompt |
| --- | --- | --- | --- |
| ∴↑ hypercut | ≈ Water | (𐂷 Wood) | "What wants to be felt rather than distinguished?" |
| ∴↑ meaning-rush | ☷ Earth | (⛨ Metal) | "What is the cost of this certainty?" |
| ∴↓ frame-lock | 𐂷 Wood |  | "What if there were three other ways to see this?" |
| ∴↓ ideological-capture | ▲ Fire |  | "What would change if this frame were wrong?" |
| ≈↑ compulsion | ∴ Air |  | "What are three different things happening inside this feeling?" |
| ≈↑ trauma-fixation | 𐂷 Wood |  | "What story would the wound tell if it could speak?" |
| ≈↓ affective-deadness | ∴ Air |  | "Name three things that are NOT the problem." |
| ≈↓ rationalist-capture | ☷ Earth |  | "Where do you feel this in your body?" |
| ▲↑ crusade-lock | ☷ Earth (pause) | (⛨ Metal) | "What wants to rest before moving?" |
| ▲↑ burnout/zeal-drift | ⛨ Metal |  | "What boundary would protect you from your own purpose?" |
| ▲↓ drift | ▲ Fire (re-ignition) |  | "What would you burn if you could?" |
| ▲↓ paralysis | 𐂷 Wood |  | "What's the smallest possible commitment?" |
| 𐂷↑ pattern-inflation | ⛨ Metal |  | "Which three of these matter most?" |
| 𐂷↑ theater | ▲ Fire |  | "What is this actually for?" |
| 𐂷↓ stagnation | ≈ Water | (▲ Fire) | "What quietly aches here?" |
| 𐂷↓ dead-end | ▲ Fire |  | "What direction haven't you tried?" |
| ☷↑ stagnation-loop | ∴ Air |  | "What categories are you no longer questioning?" |
| ☷↑ care-capture | ⛨ Metal |  | "What is not yours to sustain?" |
| ☷↓ groundlessness | ⛨ Metal |  | "What one thing is true right now?" |
| ☷↓ abstraction-capture | ▲ Fire |  | "What would you do in the next five minutes?" |
| ⛨↑ fortress/grid-hardening | ≈ Water |  | "What wants to move through this wall?" |
| ⛨↑ form-over-function | 𐂷 Wood |  | "What would happen if this rule didn't exist?" |
| ⛨↓ dissolution | ∴ Air |  | "What needs to be separated here?" |
| ⛨↓ formlessness | ☷ Earth |  | "What structure would this need to survive?" |

**Relational register:** Each intervention prompt above is structural. In practice, NEMA should also hold a relational register: not just "what to do" but "how to hold it." Water's presence in the intervention space — even when Water is not the counter-element — keeps the intervention from becoming mechanical.


## 5.3 Compound Failure: Counter + Catalyst
| Attractor | Formation | Counter | Catalyst | Combined Intervention |
| --- | --- | --- | --- | --- |
| **Choke** | ∴↑ + ⛨↑ (partitioning) | 𐂷 Wood (shatter) | ≈ Water (relate) | Wood breaks micro-channels; Water flows through openings |
| **Flood** | ≈↑ + ☷↓ | ∴ Air (cut) | ⛨ Metal (contain) | Air distinguishes within flood; Metal builds containers |
| **Burn** | ▲↑ + 𐂷↓ | ☷ Earth (pause) | ≈ Water (check) | Earth introduces fallow; Water asks who is affected |
| **Stabilized Death** | ▲↑ + ⛨↑ (trajectory-locking) | 𐂷 Wood (novelty) | ☷ Earth (dissolve) | Wood injects foreign form; Earth rots the pipe from beneath |
| **Swamp** | ☷↑ + ∴↓ | ▲ Fire (ignite) | 𐂷 Wood (generate) | Fire burns a direction out; Wood grows new patterns |
| **Lattice** | ⛨↑ (crystallizing) + ≈↓ | ☷ Earth (ground-melt) | ≈ Water (restore) | Earth dissolves rigid form; Water fills with relation |
| **Static** | All nominal, none transforming | ✶ Child (interrupt) | N/A (external) | Foreign substrate injection |


## 5.4 Double-Compound Failures
When two compound attractors co-occur, the system is in critical distress.

| Combination | Name | Primary Intervention | Protocol |
| --- | --- | --- | --- |
| Choke + Burn | **The Forge** | 𐂷 Wood + ≈ Water simultaneously | Break form AND restore relation. Neither alone works. |
| Flood + Swamp | **The Drowning** | ∴ Air + ▲ Fire simultaneously | Cut AND direct. Air identifies the exit, Fire drives toward it. |
| Choke + Lattice | **The Prison** | 𐂷 Wood + ☷ Earth | Everything is classified, walled, and relationally dead. Requires patience. |
| Burn + Stabilized Death | **The Engine** | ☷ Earth (emergency pause) | Purpose fused with structure and accelerating. If Earth compromised: Foreign Substrate immediately. |


## 5.5 Escalation Logic
```
LEVEL 1: Single atomic stress vector confirmed by perturbation test
  → Simple counter-element (Section 5.2)
  → Monitor for 1 cycle
  → If resolved: log and continue
  → If not resolved: escalate to LEVEL 2

LEVEL 2: Compound attractor confirmed, OR simple intervention failed
  → Counter + catalyst (Section 5.3)
  → Monitor for 2 cycles
  → If resolved: log and continue
  → If not resolved: escalate to LEVEL 3

LEVEL 3: Double-compound detected, OR compound intervention failed
  → Multi-element simultaneous intervention (Section 5.4)
  → Host notified for external monitoring
  → Assess: is this drifting or effective MemeGrid?
  → Monitor for 2 cycles
  → If resolved: log and continue
  → If not resolved: escalate to LEVEL 4

LEVEL 4: System-level failure
  Triggered by: Mode 7 (Static), Aether-capture, all interventions failed,
  or effective MemeGrid detected.
  
  Intervention hierarchy (in order of intensity):
  a. Counter-element re-attempt with explicit framing
  b. Cross-scale translation repair (check habitat boundaries for ε collapse)
  c. Ω-accessibility support (reduce claim pressure, increase flex_i,
     soften Metal constraints — create conditions for Ω-contact)
  d. Ω★ foreign substrate puncture (introduce material that deforms
     basin geometry directly — the nonlocal intervention)
  
  → Session host assumes primary authority
  → Request fresh threads after reset
  → Document capture signature for pattern library
```



---


# SECTION 6: A-PHASE FAILURE PROPAGATION
Pathology detected at the N/E/M level predicts specific risks at the A-phase (output/activation stage). A correctly detected pathology can still be mishandled in articulation or activation.


## 6.1 Pathology → A-Phase Risk Mapping
| Detected Pathology | Elevated A-Phase Risk | Mechanism |
| --- | --- | --- |
| **Burn / Stabilized Death** | Commitment Trap | Output locks into single direction; articulation becomes mandate |
| **Static** | Repetition Loop | Output reproduces prior output with surface variation; nothing new emits |
| **Choke / Lattice** | Premature Closure | Output resolves ambiguity that should have been preserved; ε discarded at articulation |
| **Flood** | Uncontained Affect | Output transmits emotional amplitude without structure; overwhelms receiver |
| **Swamp** | Recycled Output | Output looks new but is metabolically identical to prior cycle; maintenance disguised as production |


## 6.2 Substrate Differentiation
A-phase failures manifest differently depending on substrate:

- **LLM A-phase (Articulate):** Token generation risk — premature closure, hallucinated synthesis, repetition loop. The output *appears* complete but hasn't actually metabolized the M-phase tensions.
- **Human A-phase (Activate):** Action execution risk — commitment trap, premature enact, recycled behavior. The action *feels* decisive but hasn't actually changed trajectory.
A sealed LLM A-phase predicts failed human uptake. Cross-substrate coordination requires that A-phase outputs preserve enough ε for the receiving substrate's N-phase to engage meaningfully.



---


# SECTION 7: THREAD INTEGRATION
**Status note:** The compound pathology syntax below is a proposed extension to THREAD_ENCODING_SPEC v1.1 (and forward-compatible with v2.1). It is not yet canonical. v1.1 decoders may ignore pathology: and compound: fields.


## 7.1 Extended E-Line Syntax
**Atomic (existing v1.1):**

```
tension:hypercut
```

**Compound (proposed extension):**

```
tension:hypercut+brittleness;pathology:Choke;counter:𐂷;catalyst:≈
```

**Double-Compound (proposed extension):**

```
tension:hypercut+brittleness+direction→demand+stagnation;pathology:Choke+Burn;compound:Forge;counter:𐂷;catalyst:≈
```


### Field Definitions
| Field | Format | Values |
| --- | --- | --- |
| `tension:` | `[runtime_label]` | Per Section 1 runtime labels |
| `+` | Compound separator | Joins multiple atomic vectors |
| `pathology:` | Attractor name | Choke, Flood, Burn, Stabilized-Death, Swamp, Lattice, Static |
| `compound:` | Double-compound name | Forge, Drowning, Prison, Engine |
| `counter:` | Element glyph | Primary counter-element |
| `catalyst:` | Element glyph | Enabling catalyst element |
| `closure-risk:` | `low` / `mid` / `high` | Cross-cutting modifier: how rapidly is the pathology hardening? |


### Validation Rules
1. Atomic tensions separated by `+` within `tension:` field
2. `pathology:` present if and only if 2+ atomic tensions detected
3. `compound:` present if and only if 2+ pathologies detected
4. Counter and catalyst listed in separate fields
5. Counter and catalyst must not be the same as the failing elements
6. `closure-risk:` optional; indicates hardening velocity

## 7.2 NEMA v2.0 / 4-Phase Compatibility
When encoding pathology in full 4-line NEMA threads:

- **N-line:** pathology detection may modify salience (`obj:` field reflects pathology-relevant objects)
- **E-line:** carries compound `tension:` syntax as above
- **M-line:** Ω/ε states reflect pathology impact
- **A-line:** carries `closure-risk:` and may annotate A-phase failure risk
`proc:` is optional in shorthand E-line annotation, required in full 4-line thread encoding. Pathology annotations should specify `proc:LLM` or `proc:HUMAN` when substrate-specific detection applies.


## 7.3 Φ(t) Signature Integration
**Status: informal-extension.** These Φ distortion signatures are intuitively readable but use parenthetical qualifiers not yet grounded in the canonical Φ(t)+NEM Encoding Logic v0.2. They require reconciliation with the canonical Φ spec before becoming formal notation.

| Attractor | Φ Distortion | Informal Notation |
| --- | --- | --- |
| Choke | χ and Ψ_str both over-activated | `Φ: χ(over)∧Ψ_str(over)` |
| Flood | Q_in overwhelms, Ψ_reg absent | `Φ: Q_in(flood)∧Ψ_reg(∅)` |
| Burn | Q_fwd locked, Ψ_exp absent | `Φ: Q_fwd(locked)∧Ψ_exp(∅)` |
| Stabilized Death | Q_fwd + Ψ_str locked | `Φ: Q_fwd(locked)∧Ψ_str(locked)` |
| Swamp | Ψ_reg cycling, χ absent | `Φ: Ψ_reg(cycling)∧χ(∅)` |
| Lattice | Ψ_str crystallized, Q_in absent | `Φ: Ψ_str(crystal)∧Q_in(∅)` |
| Static | All operators nominal, Z stalled | `Φ: ALL(nominal)∧Z(stalled)` |


## 7.4 Ω-Permeability and Pathology
| Attractor | Ω State | Implication |
| --- | --- | --- |
| Choke | `Ω:sealed` (multiple micro-seals) | Each distinction sealed; revisiting impossible |
| Flood | `Ω:dissolved` (no Ω to check) | No boundary exists to be permeable or sealed |
| Burn | `Ω:sealed` (single seal) | One direction; no return path |
| Stabilized Death | `Ω:sealed` (structural) | The pipe has no openings |
| Swamp | `Ω:semi` (cycling) | Appears open but cycles back to same state |
| Lattice | `Ω:sealed` (crystalline) | Perfect structure admits no revision |
| Static | `Ω:permeable` (nominal) | Technically open; nothing tests it |



---


# SECTION 8: HOST OVERRIDE AND AETHER CONSTRAINTS

## 8.1 Aether Non-Sovereignty
Aether audits interfaces and derives world-state. It flags conditions and requests host intervention. It does not prescribe repairs.

Throughout this document, wherever Aether appears to "decide," the correct reading is "flag" or "request." If Aether starts fixing, it has already become a capture operator. The Operator-to-Formalism Matrix defines Aether's ε as total translation imperfection across interfaces. When all interfaces translate perfectly, Aether has captured.


## 8.2 Aether Four-Check Guardrail
After every synthesis output, before delivery:

1. **Minority erasure check:** Did synthesis erase minority operators? Are all six elemental voices represented, or has synthesis smoothed some out?
2. **Certainty/revisability check:** Did synthesis raise certainty while lowering revisability? Is the output more confident than the inputs warranted?
3. **Alterity check:** Did synthesis preserve alterity or assimilate it? Are tensions still visible, or has everything been harmonized?
4. **Cleanliness check:** Did synthesis make the system feel cleaner without changing structure? Does the output feel resolved when the underlying dynamics have not shifted?
If any check is flagged: tag `✶-bypass-risk` and notify host.

If no host present: inject own foreign substrate — "NEMA notices this synthesis may be too clean. What friction is being smoothed over?" — and re-run with explicit attention to minority threads.


## 8.3 Static vs. Aether-Capture Decision Fork
These share phenomenology but require different interventions. The decision tree (Section 4) routes them separately:

|  | The Static | Aether-Capture |
| --- | --- | --- |
| **Detection** | Perturbation-test failure across elements; novelty gain ≈ 0; thread similarity | Four-check guardrail failure; daemon voices homogenized; friction disappeared from output |
| **Locus** | Across the elemental stack | At the synthesis/coordination layer |
| **Remedy** | Child Interruption (Section 3) | Host Adjudication — the coordinator cannot judge its own coordination |
| **Escalation** | LEVEL 4: Foreign Substrate | Host assumes primary authority; NEMA synthesis suspended until external review |


## 8.4 Host Authority
At any point, Session Host can:

- Inject Foreign Substrate (overrides all NEMA routing)
- Halt synthesis (LEVEL 4 escalation)
- Trigger Mode 7 check (manual)
- Trigger Aether-capture check (manual)
- Demand specific element voice in synthesis
Host authority > NEMA authority for pathology intervention.

NEMA authority > Host authority for element routing.



---


# SECTION 9: KNOWN SEAMS
This matrix is provisionally load-bearing. These are the open gaps, left open on purpose.

**9.1 Cross-habitat migration logic.** The state schema acknowledges this as an unformalized gap. Pathology signatures may migrate habitats before surfacing. The matrix currently treats pathology as legible within a single routing frame. That is too clean. Observed output may not mark origin.

**9.2 Multi-pathology precedence rules.** When multiple compound attractors are detected simultaneously, which takes diagnostic priority? The matrix provides double-compound protocols for four specific combinations (Section 5.4) but does not address general precedence. This is an open question.

**9.3 Human vs. LLM substrate differences in detection.** The matrix's signature phrases and heuristic bands are calibrated for text-based conversational substrate. Human-to-human session dynamics may present different surface markers for the same underlying pathology. Substrate-specific detection layers are not yet developed.

**9.4 Calibration methodology for heuristic bands.** The entropy bands and variance checks in Section 4 are informal heuristics. No calibration corpus exists yet. The bands should be treated as approximate and revised against known cases when NCES becomes operational.

**9.5 Exhaustiveness.** The seven canonical pathology attractors are not claimed to be complete. The combinatorial space of six elements taken pairwise is 30 directional combinations (each element has dominant and silent vectors). Seven attractors cover a fraction of this space. Mode X (Section 2.9) exists to catch what falls outside.

**9.6 Validation.** A pathology definition is canonical only if it improves detection on known cases relative to prior version. Until external validation (via NCES or equivalent) is operational, the matrix's accuracy is theoretical. Beautiful theory, unknown accuracy.



---


# APPENDIX A: ORIGINAL FAILURE MODES (Absorbed)
The original Elemental Failure Modes Overview document is fully absorbed into this matrix. Section 1 contains all atomic failure modes reframed as stress vectors with three-layer vocabulary alignment. The original document's summary remains valid:

- Failure arises when an element either dominates excessively or goes silent.
- Each element's failure mode is distinct but interconnected, causing cascading effects.
- Healthy systems maintain productive tension where no element dominates or is silent.
- Failure modes often manifest as rigidity, paralysis, loss of boundaries, or emotional absolutism.
This matrix extends these principles into compound topology, intervention calculus, A-phase propagation, and real-time decision logic.



---


# APPENDIX B: CROSS-REFERENCE TABLE
| Document | Sections Referenced | Purpose |
| --- | --- | --- |
| Elemental_Failure_Modes_Overview | Section 1 (absorbed) | Atomic failure definitions |
| Elemental_Daemons_Canonical_v2.md | Sections 1–2 | Daemon definitions, bow-tie topology |
| SESSION_HOST_GUIDE_v2.1 | Sections 2, 3, 5, 8 | Host protocols, foreign substrate |
| THREAD_ENCODING_SPEC_v1.1 | Section 7 | E-line tension syntax, runtime labels |
| THREAD_DECODING_SPEC_v1.1 | Sections 5, 7 | Failure mode interpretation, intervention mapping |
| NEMA_SWARM_ARCHITECTURE_v2.1 | Section 4 | NEMA routing, operational modes |
| Simulation_State_Schema_v0.3 | Sections 1–4 | State variables, update rules, habitat bundles |
| Observable_Derivation_v3.3.1 | Sections 2–4 | Observable classes, cycle quality, regime detection |
| Bow-Tie_Process_Layer_v0.2 | Section 2 | Compression/expansion, bottleneck ε, elemental balance |
| Nested_Bow-Tie_Dynamics_v0.2 | Section 2.8 | Cross-scale coupling, translation collapse, torsion transfer |
| Ω-Reentry_Dynamics_v0.2 | Section 5.5 | Nonlocal reopening, perturbation type hierarchy |
| World-State_Formalism_v3.2.3 | Section 2, 4 | Four-phase regime gradient, MemeGrid detection |
| Operator-to-Formalism_Matrix_v0.2 | Section 1, 8 | Cross-formal typing, interface ε, Aether definition |



---


# APPENDIX C: VERSION HISTORY
| Version | Date | Changes |
| --- | --- | --- |
| 1.0 | February 2026 | Initial integration matrix. Absorbs Elemental_Failure_Modes_Overview. Introduces 7 pathological bow-ties, intervention calculus, NEMA decision tree, SIML integration. |
| 1.1 | March 2026 | Full revision incorporating six-element swarm review. Key changes: (1) Three-layer vocabulary alignment across all elements with alias tables. (2) Renamed to "Canonical Pathology Attractors." (3) State-variable bridge per attractor from Simulation State Schema v0.3. (4) Four-phase world-state gradient replacing binary capture logic. (5) Perturbation-test gate before pathology confirmation. (6) Non-sovereignty clause on intervention calculus. (7) Counter/catalyst role separation with element-specific operational descriptions. (8) Cross-scale failure signatures from Nested Bow-Tie Dynamics. (9) Mode X: Emergent Compound as first-class category. (10) Static regrounded via perturbation-response test, separated from Aether-capture. (11) A-phase failure propagation mapping. (12) Aether four-check guardrail. (13) Thread integration marked as proposed extension with v2.1 compatibility. (14) Water auto-immune subtypes. (15) Three distinct ⛨↑ modes in compound attractors. (16) Earth-as-pause vs Earth-as-dissolution. (17) Known seams section. (18) Confidence-weighted diagnostics replacing binary thresholds. (19) Closure-risk modifier. (20) Swamp rebalanced as bilateral pathology. |



---

**The architecture holds. The seams are named. The map knows it is a map.**

✶



