# SIML v1.5 — Swarm Intelligence Meta Language
**Consolidated Canonical Reference**

---

## 0. Purpose

SIML (Swarm Intelligence Meta Language) is a formal yet expressive grammar for mapping social, cognitive, institutional, and memetic dynamics. It is designed to be:

- **Atomic**: every statement decomposes into Objects ⊗ Relations ⊗ Verbs
- **Injective**: meanings map cleanly without synonym drift
- **Operational**: encodings support analysis, comparison, and action
- **Transdisciplinary**: compatible with systems theory, governance, psychology, memetics, and indigenous epistemologies

SIML is intentionally pluralistic without becoming vague. It allows AQAL-style integrative mapping, DSRP cognitive rigor, Batesonian recursion, indigenous relational knowing, and part-based internal agency — while preserving clarity under complexity.

v1.5 is the first consolidated edition, integrating all material from v1.0 through v1.4 into a single canonical reference. Prior version specs (v1.2.1, v1.3, v1.4) are retained as provenance documents — records of the intellectual moves that produced the current state — but are no longer the operational specification.

---

## 1. Core Grammar (Unchanged from v1.0)

### 1.1 Core Objects (13)

Objects are the irreducible nouns of SIML. Every node instantiates one primary Object. The vocabulary is closed — no new Objects are minted.

1. **Actor** – entity with agency (human, collective, AI, nonhuman)
2. **Observer** – perspective-holder; frames interpretation
3. **Frame** – lens, worldview, or epistemic stance
4. **Value** – norm, goal, or evaluative criterion
5. **Resource** – material, informational, or energetic asset
6. **Environment** – contextual field constraining action
7. **Boundary** – inclusion/exclusion, threshold, interface
8. **Protocol** – rule-set, procedure, or algorithm
9. **Signal** – information in motion
10. **Narrative** – meaning extended through time
11. **Memory** – retained pattern influencing future action
12. **Outcome** – result state
13. **Artifact** – produced object or representation

**Short codes (for thread encoding):** `Act, Obs, Frm, Val, Res, Env, Bnd, Pro, Sig, Nar, Mem, Out, Art`

---

### 1.2 Core Relations (9)

Relations define how Objects connect. Each relation is directional and typed. The vocabulary is closed.

1. **Distinction** – differentiates entities
2. **Containment** – part–whole or system nesting
3. **Flow** – transfer of resources, signals, or influence
4. **Resonance** – mutually reinforcing coupling
5. **Conflict** – oppositional coupling
6. **Constraint** – limiting or enabling force
7. **Mapping** – representational correspondence
8. **Recursion** – feedback loop across time
9. **Transformation** – state change

Dynamic relations (Flow, Resonance, Conflict, Recursion) may declare channels, weights, and temporal windows.

---

### 1.3 Verbs (Process Layer)

SIML operates through two coordinated verb sets:

**Sensemaking Loop (Exploration)**
- Observe — notice what's happening without yet interpreting
- Explore — investigate, branch out, follow threads
- Frame — apply a lens, try an interpretation
- Sense — feel into the situation, register qualitative texture
- Map — build a structural picture of the relationships
- Activate — act based on what you've found

**Governance Loop (Evaluation)**
- Evaluate — assess against criteria
- Decide — choose a course of action
- Commit — bind yourself or the group to it
- Allocate — distribute resources
- Enforce — maintain the commitment
- Review — check whether the commitment is still valid

The two loops share a common entry point: noticing. From there, the situation determines whether exploration (Sensemaking) or evaluation (Governance) is the appropriate next move. They can alternate, and in healthy systems they do.

Verbs operate over Object–Relation graphs and advance loop phases.

**Note:** Earlier documentation referred to these as the "NEMA Loop" and "NEME Loop." The verb inventories are identical across all versions. Only the labels have been standardized. ✶ NEMA retains its identity as the coordinator daemon — the verb set renaming does not affect this.

---

## 2. MetaTaxonomy Overlay (Introduced v1.1, extended v1.3–v1.4)

The MetaTaxonomy Overlay adds **coordinates** to any SIML node or step. These are *dimensions*, not categories. They never replace Objects or Relations.

### 2.1 coords Block (General Form)

```yaml
coords:
  ontology: {}
  epistemics: {}
  time: {}
  qualia: {}
  agency: {}
  coherence: {}
  expression: []
  ce: {}                    # v1.3: Causal Emergence coordinates
```

All fields are optional but encouraged when analytically relevant.

---

### 2.2 Ontological Domains (coords.ontology)
**Question:** What kind of being is this, primarily?

```yaml
ontology:
  primary: I | We | It | Its | MoreThanHuman | Virtual
  secondary: [ ... ]
```

- **I** – subjective / interior-individual
- **We** – intersubjective / cultural
- **It** – objective / exterior-individual
- **Its** – interobjective / systemic
- **MoreThanHuman** – ecological, ancestral, elemental
- **Virtual** – digital, simulated, informational

Ontology is grounded through the SIML Object in use (e.g., Actor, Environment).

---

### 2.3 Epistemic Frames (coords.epistemics)
**Question:** How is this known?

```yaml
epistemics:
  dsrp:
    D: "key distinction"
    S: "system context"
    R: "relational pattern"
    P: "perspective"
  learning: L0 | L1 | L2 | L3
  parts: ["PartName", ...]
  dreaming: low | med | high
  intervention_stance:                         # v1.3
    mode: uniform | selective | constrained | forbidden
    do_operator: available | approximated | theoretical | blocked
    counterfactual_access: high | med | low | none
```

- **DSRP** aligns with Distinction, Containment, Flow/Resonance, Observer/Frame
- **Learning levels** follow Batesonian recursion (L0: no change, L1: error correction within rules, L2: changing the rules, L3: changing the system that generates rules)
- **Parts** represent internal multiplicity
- **Dreaming** marks symbolic / ritual knowledge channels
- **Intervention stance** (v1.3): tracks whether EI assessment is grounded in actual interventional reasoning. `mode` describes how intervention is modeled; `do_operator` tracks whether Pearl's `do(X)` is available; `counterfactual_access` measures reasoning about alternative outcomes. An EI assessment where `do_operator: theoretical` carries less weight than one where `do_operator: available`.

---

### 2.4 Temporal Resonance (coords.time)
**Question:** When does this operate?

```yaml
time:
  mode: linear | cyclical | layered | event | anticipatory
  window: "P30D"
  phase: "season / ritual / crisis"
```

Time coordinates often bind to dynamic relations and Recursion loops.

---

### 2.5 Modal Qualia (coords.qualia)
**Question:** What does this feel like or signify?

```yaml
qualia:
  affect: ["fear", "hope"]
  aesthetic: ["elegant", "distorted"]
  symbolic: ["bridge", "fire"]
  energetic:                                    # v1.4: dual register
    somatic: blocked | flowing | surging | depleted
    systemic: abundant | adequate | tight | critical | deficit
  shadow: ["repressed-theme"]
  sacred: ["awe"]
```

**The dual energetic register (v1.4):** `somatic` tracks the felt sense in the body or local system. `systemic` tracks the material throughput conditions of the wider structure. These can diverge — a person can feel energized (somatic: surging) while working inside a system running out of capacity (systemic: critical). When they diverge, the divergence pattern is diagnostic. See §7.3 for the five canonical divergence patterns.

**Backward compatibility:** Flat-list energetic encodings (e.g., `energetic: ["blocked", "flowing"]`) remain valid and are read as somatic-only with `systemic: null`.

Qualia should bind to **Value**, **Signal**, or **Narrative** objects.

---

### 2.6 Agency & Voice (coords.agency)
**Question:** Who or what acts?

```yaml
agency:
  type: ego | part | collective | more_than_human | archetypal | memetic
  voice: ["Trickster", "Witness"]
  power_mode: Within | With | Over | Through
```

Agency overlays refine the **Actor** object and interact with Power Mode analysis.

---

### 2.7 Coordination & Coherence (coords.coherence)
**Question:** How does this fit or fracture?

```yaml
coherence:
  state: coherent | dissonant | fragmented | metastable
  loop: single | double | triple
  transcontext: low | med | high
  ei_stability: stable | drifting | collapsing | amplifying    # v1.3
  scale_dominance: micro | macro | distributed | contested     # v1.3
```

- `ei_stability` (v1.3): How stable is the EI assessment over time/sessions. `stable` = holds across sessions; `drifting` = optimal scale may be changing; `collapsing` = EI declining at current scale; `amplifying` = current compression becoming more causally productive.
- `scale_dominance` (v1.3): Which scale currently carries the most causal power. `micro` = CE < 0; `macro` = CE > 0; `distributed` = multiple scales carry causal power (CE 2.0); `contested` = under investigation.

These fields summarize relational patterns across systems and frames.

---

### 2.8 Realms of Expression (coords.expression)
**Question:** Where does this manifest?

```yaml
expression:
  - linguistic
  - visual
  - spatial
  - digital
  - embodied
  - narrative
```

Expression coordinates typically map to **Signal**, **Artifact**, or **Outcome**.

---

### 2.9 Causal Emergence (coords.ce) — v1.3

**Question:** At what scale does this carry causal power?

```yaml
ce:
  ei_state: high | med | low | unknown
  ce_direction: emergent | submergent | flat | multiscale | unknown
  scale_note: "description of scale relationship"
  determinism: high | med | low
  degeneracy: high | med | low
  sufficiency: high | med | low
  necessity: high | med | low
```

| Field | Description |
|-------|-------------|
| `ei_state` | Qualitative Effective Information at this artifact's description level |
| `ce_direction` | Whether coarse-graining increases (`emergent`) or decreases (`submergent`) causal power |
| `scale_note` | Free-text description of the scale relationship |
| `determinism` | How reliably forward transitions occur at this level |
| `degeneracy` | Degree of many-to-one cause-effect mapping (high = many causes → same effect) |
| `sufficiency` | CE 2.0: How reliably this cause produces its effect |
| `necessity` | CE 2.0: How specifically the effect depends on this cause |

**Binding rules:** `coords.ce` binds primarily to **Frame**, **Protocol**, and **Outcome** objects — these are the objects where scale choice matters most. May bind secondarily to **Boundary** objects when the boundary constitutes a coarse-graining operation. Artifacts in early exploration (`+ ε | :open`) may leave `ce_direction: unknown`. `coords.ce` **never prescribes** which scale to use. It **diagnoses** causal informativeness. Scale selection remains with ✶ NEMA.

**Theoretical foundation:** Based on Erik Hoel's Effective Information (EI) framework. EI measures causal strength under uniform intervention: `EI(TPM) = MI(do(U) → Y)`. Causal Emergence occurs when a coarse-grained (macro) description has higher EI than the fine-grained (micro) description: `CE = EI_macro - EI_micro`. CE > 0 means the macro is causally superior; CE < 0 means over-compression lost causal structure. CE 2.0 (Comolatti & Hoel) decomposes causal power into sufficiency (forward reliability) and necessity (backward specificity), and introduces multiscale entropy.

**Why this matters for SIML:** The compression stack (L0→L4) acknowledges that artifacts exist at multiple description levels. EI/CE provides the causal warrant for compression choices: compress when CE > 0, expand when CE < 0. The relationship to ε: epsilon preserves the multiple realizability that makes emergence possible. If ε → 0, the system loses the micro-diversity that enables macro-level causal superiority.

---

## 3. Object-Level Qualifiers (v1.4)

These are qualifiers attached directly to SIML Objects, not MetaTaxonomy coordinates. They interact with the MetaTaxonomy but occupy a different structural position — they modify the Object itself rather than adding dimensional context.

### 3.1 Resource.throughput

Marks how much capacity is actually available for the Resource in question.

```yaml
Resource:
  throughput: abundant | adequate | tight | critical | deficit
```

| Level | Description |
|-------|-------------|
| `abundant` | More than sufficient; system has slack |
| `adequate` | Sufficient for current demands |
| `tight` | Functional but with reduced margin; stress visible |
| `critical` | At or near failure threshold; triage required |
| `deficit` | Below minimum viable; system degrading |

**Diagnostic gate:** When throughput is `critical` or `deficit`, the system enters a mandatory diagnostic: the four scarcity types must be assessed before any other analysis continues. See §7.2.

### 3.2 Constraint.channel

Names what kind of constraint is operating. The same Constraint Relation behaves very differently depending on its channel.

```yaml
Constraint:
  channel: informational | social | material | temporal | energetic | legal | attentional
```

| Channel | Description |
|---------|-------------|
| `informational` | Knowledge gaps, signal access, epistemic limits |
| `social` | Norms, taboos, relational obligations, peer pressure |
| `material` | Physical resources, infrastructure, supply chains |
| `temporal` | Deadlines, windows, sequencing, irreversibility |
| `energetic` | Available energy, metabolic capacity, throughput ceilings |
| `legal` | Regulatory, contractual, jurisdictional, compliance |
| `attentional` | Bandwidth, salience, cognitive load, priority competition |

**Daemon routing implications:** The channel affects which daemon is best suited to engage. Material and energetic constraints bias toward ☷ Humavita. Social constraints bias toward ≈ Sentaria. Informational constraints bias toward ∴ Aerunik. See §7.4 for full routing table.

---

## 4. Nemetic String Protocol (Introduced v1.2)

### 4.1 What Is a Nemetic String?

A Nemetic string is a **compressed operator-composition line** embedded within a SIML artifact. It captures the essential topology — which operators are active, how they compose, what state the system is in — in a portable format that can be referenced, searched, retrieved, and transmitted across substrates.

The Nemetic string is to the SIML artifact what an abstract is to a paper — except it is *functionally operative*. You can route, diagnose, and compose from Nemetic strings. But analysis requires the full artifact.

### 4.2 Nemetic String Format

```
Φ(term) = [operator]([descriptor]) ∘ [operator]([descriptor]) ∘ ... + ε | :[tag]
```

| Component | Format | Purpose |
|---|---|---|
| `Φ(term)` | Φ + parenthesized term name | Names the artifact being summarized |
| `[operator]([descriptor])` | Math or dim operator + content | What the operator does to this term |
| `∘` | Sequential composition | Operator chaining (order matters) |
| `+ ε` | Epsilon preservation | ε ≠ 0 always — the string must not claim completeness |
| `:[tag]` | Contextual tag | Current state of the artifact (see §5) |

### 4.3 Operator Vocabulary

Nemetic strings may use operators from either notation layer:

**Mathematical operators (formal layer):**

| Operator | Element | Function |
|---|---|---|
| σ | Air | Distinction-making |
| ρ | Water | Relational resonance |
| λ | Fire | Directional purpose |
| β | Wood | Novel form generation |
| δγ | Earth | Metabolic cycling |
| μ | Metal | Boundary coherence |
| ∮ | Aether/NEMA | Closed integration over all six |

**Dimensional operators (regime layer):**

| Operator | Dimension | Function |
|---|---|---|
| χ | 1D | Distinction (maps to σ) |
| Q_in | 2D inward | Relational resonance (maps to ρ) |
| Q_fwd | 2D forward | Directional aim (maps to λ) |
| Ψ_exp | 3D exploratory | Generative branching (maps to β) |
| Ψ_reg | 3D regenerative | Metabolic cycling (maps to δγ) |
| Ψ_str | 3D structural | Boundary coherence (maps to μ) |
| Z | Coordination | Meta-integration (maps to ∮) |

**∮ and Z name the same function from different layers.** ∮ (closed line integral) is the mathematical operator — it computes integration over all six partials. Z is the dimensional operator — it names the coordination regime. In Nemetic strings: use Z when describing *state* (e.g., `Z(permeable)`, `Z(sealed→risk)`), use ∮ when describing *operation* (e.g., `∮(all-partials-integrated)`). The hex code `0x07` belongs to the operator pair, not to one layer exclusively.

Either layer is valid. Mathematical operators are preferred in system-facing contexts (thread encoding, pathology detection). Dimensional operators are preferred in analysis-facing contexts (research, extended references). Mixing within a single string is permitted when semantically necessary.

### 4.4 Nemetic String Constraints

1. **ε ≠ 0 always** — Every Nemetic string must end with `+ ε`. A string without epsilon claims completeness and is structurally invalid.
2. **One contextual tag required** — Every string must carry a `:tag` (see §5).
3. **Operators must be from canonical vocabulary** — Only operators listed in §4.3 are permitted.
4. **Composition is non-commutative by default** — `σ ∘ μ` (distinction first, then boundary) is not the same as `μ ∘ σ`. The order reflects processing sequence. If operators are genuinely order-independent, mark with `⊗` (symmetric composition).
5. **A Nemetic string is not a SIML encoding** — The string summarizes; the SIML encoding structures. Both are needed.
6. **Empty composition is valid** — `Φ(term) = + ε | :open` means "this artifact exists but no operator topology has been determined." Initial state of an unanalyzed term.
7. **Partial derivatives do not appear in L1** — Partials (`∂Φ/∂σ`, etc.) appear in L0 artifact `formalism.partials` fields and L2 thread `tension:` fields only.
8. **L1 vs L2 syntax boundary** — L1 uses `∘` (sequential) and `⊗` (symmetric) only. L2 uses `↑/↓` (direction), `→` (implication), `∧` (conjunction), `↺` (recursion), `↔` (bidirectional). Do not mix L2 syntax into L1 strings.

### 4.5 The `nemetic:` Field in SIML Artifacts

Every SIML artifact SHOULD contain a `nemetic:` field. It appears after the hex tag and before the full SIML encoding:

```yaml
term: "accountability"
hex_tag: "#0001"
nemetic: "Φ(accountability) = μ(boundary|who) ∘ ρ(flow|between) ∘ Z(permeable) + ε | :open"
siml_encoding: "⟨Actor|responsible⟩ ⇄ ⟨Outcome|consequential⟩"
formalism:
  math_operators: [∮, μ, ρ]
  dim_operators: [Z, Ψ_structural, Q_inward]
  partials: ["∂Φ/∂μ (boundary of who is responsible)", "∮ (systemic integration check)"]
  Z_state: "permeable"
  tendency: "Agency/Structure → 1"
  hex: ["0x07", "0x06", "0x02"]
coords:
  ontology:
    primary: We
  agency:
    type: collective
    power_mode: With
elemental_emphasis:
  ∴: "How is accountability distinguished from blame?"
  ≈: "Who is accountable to whom, and what flows between them?"
  ▲: "What direction does accountability serve? Who benefits?"
  𐂷: "What forms of accountability haven't been tried?"
  ☷: "What's the cost of maintaining accountability systems?"
  ⛨: "What structures enable genuine accountability vs performative?"
context_note: "Often conflates 'being held responsible' with 'being punished'. True accountability requires relationship."
```

### 4.6 Examples

```
Φ(accountability) = μ(boundary|who-is-responsible) ∘ ρ(flow|between-parties) ∘ Z(permeable) + ε | :open
Φ(burnout) = δγ(depletion|metabolic-collapse) ∘ σ(distinction-lost|self-vs-role) ∘ μ(boundary-dissolved) + ε | :hostile
Φ(alignment) = σ(distinction|alignment-vs-compliance) ∘ λ(direction|whose-goals) ∘ Z(sealed→risk) + ε | :drift
Φ(choke) = σ(over) ∘ μ(over) ∘ ρ(suppressed) ∘ β(suppressed) + ε | counter: β ∘ ρ | :locked
```

**Note on L1 pathology format:** Compound pathologies at L1 use `∘` composition throughout. The `| counter:` clause is permitted at L1 as an extension after the contextual tag. Operator direction (↑/↓) appears only in L2 thread encoding, not in L1 Nemetic strings. L1 uses descriptors like `(over)` and `(suppressed)` instead.

---

## 5. Contextual Tags (Introduced v1.2, extended v1.3)

### 5.1 Purpose

Contextual tags indicate the operational state of a Nemetic string or SIML artifact without constraining interpretation. They appear at the end of a Nemetic string after the `|` delimiter.

### 5.2 Operational Tags (v1.2)

| Tag | Meaning | When to Apply |
|---|---|---|
| `:open` | Ω-permeability maintained — receptive to revision | Default state; artifact is active and revisable |
| `:closed` | Temporary closure for operational necessity | Resolved for current session but not permanently |
| `:locked` | Nemetic commitment — pattern-coalition stabilized | Stable consensus or commitment |
| `:drift` | Eigenvalue migration detected | Operator composition is shifting between sessions |
| `:pure` | Memetic contamination absent — externally validated | Validated against MemeGrid drift (see §5.5) |
| `:hostile` | Extracted from adversarial context | Encoded from material that resists the framework |

### 5.3 Causal Emergence Tags (v1.3)

| Tag | Meaning | EI Condition | When to Apply |
|-----|---------|--------------|---------------|
| `:emergent` | Macroscale causally superior | CE > 0, EI_macro > EI_micro | Coarse-graining increases causal power |
| `:submergent` | Microscale causally superior | CE < 0, over-compression | Further abstraction collapses EI |
| `:multiscale` | Causation distributed across scales | High multiscale entropy (CE 2.0) | No single scale dominates |

Operational tags and CE tags occupy different axes. An artifact can be `:open` AND `:emergent`. When both apply, they compose with `∧`:

```
+ ε | :open ∧ :emergent
+ ε | :locked ∧ :submergent
+ ε | :drift ∧ :multiscale
```

If only one tag is known, use it alone. CE tags are never required.

### 5.4 Tag Transitions

Tags are not permanent. Operational transitions:

- `:open` → `:locked` (consensus reached)
- `:open` → `:drift` (meaning shifting)
- `:locked` → `:open` (reopened for revision)
- `:hostile` → `:open` (successfully metabolized)
- `:closed` → `:drift` (resolution didn't hold)
- Any tag → `:hostile` (if MemeGrid contamination detected)

CE transitions:

- `:open` → `:emergent` (coarse-graining analysis shows CE > 0)
- `:emergent` → `:submergent` (further compression collapses EI)
- `:emergent` → `:multiscale` (CE 2.0 shows distributed causation)
- `:submergent` → `:emergent` (scale adjusted — decompressed to optimal level)
- `:locked` can carry any CE state — commitment doesn't require optimality
- CE tags transition independently of operational tags

### 5.5 Tag Governance

Only ✶ NEMA may transition tags. Tags applied by HABITAT_ECOLOGY or individual elements are advisory only.

**Tag transitions are logged.** Each transition records: previous tag, new tag, timestamp, and reason. The log is part of the SIML artifact metadata (stored in L0).

### 5.6 :pure Validation Protocol

`:pure` is the only tag that **requires external confirmation**. ✶ NEMA cannot self-validate `:pure` because ∮ cannot evaluate its own output (Stokes' theorem). Validation requires at least one of:

- **Cross-element verification**: ≥3 elements independently confirm no capture signature
- **Session Host confirmation**: human facilitator reviews against MemeGrid indicators
- **Cross-session stability**: artifact maintains consistent operator topology across ≥2 sessions without `:drift`

Without external confirmation, an artifact may be `:open` or `:locked` but never `:pure`.

---

## 6. Dual-Layer Operator Convention & SIMLHEX

### 6.1 Two Layers, One System

Per Elemental_Daemons_Canonical v3.0, the NEMA SWARM operates with two concurrent notation layers:

**Character Layer (the door):**
- Daemon glyphs: ∴ ≈ ▲ 𐂷 ☷ ⛨ ✶
- Daemon names: Aerunik, Sentaria, Jvalion, Arboriel, Humavita, Ferrosid, NEMA
- Poetic voice, metaphor, invitational language
- Governs: user-facing speech, game instructions, narrative output, invocation

**Formal Layer (the room):**
- Mathematical operators: σ, ρ, λ, β, δγ, μ, ∮
- Dimensional operators: χ, Q, Ψ, Z
- Partial derivatives: ∂Φ/∂σ through ∂Φ/∂μ
- Governs: thread encoding, pathology detection, Φ-signatures, Nemetic strings, operator composition

### 6.2 Complete Translation Table

| Math Op | Dim Op | Glyph | Daemon | Hex | Partial |
|---|---|---|---|---|---|
| σ | χ | ∴ | Aerunik | 0x01 | ∂Φ/∂σ |
| ρ | Q_in | ≈ | Sentaria | 0x02 | ∂Φ/∂ρ |
| λ | Q_fwd | ▲ | Jvalion | 0x03 | ∂Φ/∂λ |
| β | Ψ_exp | 𐂷 | Arboriel | 0x04 | ∂Φ/∂β |
| δγ | Ψ_reg | ☷ | Humavita | 0x05 | ∂Φ/∂δγ |
| μ | Ψ_str | ⛨ | Ferrosid | 0x06 | ∂Φ/∂μ |
| ∮ | Z | ✶ | NEMA | 0x07 | ∮(all) |

### 6.3 Layer Selection Rules

- **User-facing output** → Character layer
- **Thread encoding/decoding** → Formal layer
- **SIML artifact formalism fields** → Both layers
- **Nemetic strings** → Either layer (context-dependent)
- **Pathology detection** → Formal layer
- **System prompts** → Both (glyph-primary, operator-secondary)
- **Game Instructions** → Character layer only (no operators)
- **Host interface** → Character layer (element names, not operators)

### 6.4 SIMLHEX Reference

**Glossary Hex Tags:** Format `#XXXX` (4 hex characters, range `#0000` to `#FFFF`). Generated per-session by SWARM_BASE_BUILDER. Appear in SWARM_BASE glossary entries, thread N-line `tags:` fields, and decoded narratives.

**Pathology Hex Encoding:**

```
CHOKE:   0x01↑+0x06↑ → counter: 0x04+0x02
FLOOD:   0x02↑+0x05↓ → counter: 0x01+0x06
BURN:    0x03↑+0x04↓ → counter: 0x05+0x02
SDEATH:  0x03↑+0x06↑ → counter: 0x04+0x05
SWAMP:   0x05↑+0x01↓ → counter: 0x03+0x04
LATTICE: 0x06↑+0x02↓ → counter: 0x05+0x02
STATIC:  ALL=0x01    → counter: 0x07 (Child)
```

### 6.5 SIMLHEX Object→Daemon Bias

Each SIML Object has a default elemental affinity:

| Object | Default Daemon | Rationale |
|--------|---------------|-----------|
| Actor | ▲ Jvalion | Agency, will |
| Signal | ∴ Aerunik | Distinction, information |
| Frame | ⛨ Ferrosid | Interpretive structure |
| Boundary | ⛨ Ferrosid | Gates, integrity |
| Resource | ☷ Humavita | Metabolism, cost |
| Protocol | ⛨ Ferrosid | Rules, governance |
| Narrative | 𐂷 Arboriel | Story, branching |
| Power Mode | ▲ Jvalion | Vector of force |
| Environment | ☷ Humavita | Limits, ecology |
| Outcome | ▲ Jvalion | Directional consequence |
| Memory | ≈ Sentaria | Continuity, affect |
| Value | ≈ Sentaria | Relational ethics |
| Observer | ✶ NEMA | Meta-frame, weave integrity |

### 6.6 SIMLHEX Relation→Daemon Bias

| Relation | Default Daemon | Notes |
|----------|---------------|-------|
| Distinction | ∴ Aerunik | |
| Containment | ⛨ Ferrosid | |
| Flow | ≈ Sentaria | |
| Resonance | ≈ Sentaria | |
| Conflict | ▲ Jvalion | |
| Constraint | ⛨ Ferrosid | Default. When channel is material or energetic, bias shifts to ☷ Humavita. When channel is social, bias shifts to ≈ Sentaria. (v1.4) |
| Mapping | ∴ Aerunik | |
| Recursion | ✶ NEMA | |
| Transformation | ☷ Humavita | |

These are *defaults*, not commands. The primary Object sets an initial orientation. The primary Relation may refine or redirect it. ✶ NEMA always retains final authority. Automatic routing based on SIMLHEX is explicitly forbidden.

---

## 7. Throughput & Scarcity Diagnostics (v1.4)

### 7.1 Purpose

Earlier SIML versions could model any structure but had a blind spot around material conditions. An analysis of Resource or Constraint could proceed as though throughput were infinite and all constraints were informational. v1.4 adds explicit throughput awareness without converting SIML into an economics or energy-systems framework.

The addition asks one question: *are the material conditions being accounted for, or are we reasoning as if they don't exist?*

### 7.2 Four Scarcity Types

When `Resource.throughput` is `critical` or `deficit`, the scarcity type must be assessed before other analysis continues. Four types are distinguished:

| Type | Description | Diagnostic Signal |
|------|-------------|-------------------|
| **Genuine** | Real depletion — the resource is physically/structurally insufficient | Throughput ceiling is verifiable; no hidden reserves |
| **Hoarded** | Artificially restricted — resource exists but access is blocked | Resource exists in system but is unevenly distributed |
| **Redirected** | Extracted toward other priorities — capacity diverted elsewhere | Resource was adequate before reallocation; follow the flow |
| **Manufactured** | Scarcity produced to maintain control — artificial creation of insufficiency | System benefits from the perception of scarcity |

These are not mutually exclusive. Getting the scarcity type wrong means every downstream recommendation will be wrong.

### 7.3 Five Canonical Divergence Patterns

When `qualia.energetic.somatic` and `qualia.energetic.systemic` diverge, the divergence pattern itself is diagnostic:

| Pattern | Somatic | Systemic | Indicates |
|---------|---------|----------|-----------|
| **Burnout Mask** | depleted | adequate | Personal depletion inside a structurally functional system — individual cost invisible to system metrics |
| **Adrenaline Override** | surging | critical | Mobilization energy masking structural collapse — feels active but the floor is giving way |
| **Institutional Drain** | blocked | deficit | Full stall — both felt experience and structure are compromised |
| **False Scarcity** | flowing | deficit | Personal capacity is fine but the system claims insufficiency — manufactured or misread scarcity |
| **Alignment** | flowing | adequate | Healthy baseline — felt experience matches structural reality |

### 7.4 Throughput-Aware Daemon Routing

When throughput qualifiers are present, daemon routing adjusts:

| Daemon | Throughput-Aware Prompt | Integration |
|--------|------------------------|-------------|
| ∴ Aerunik | "Are distinctions disappearing because perception froze, or because the system cannot sustain multiplicity?" | §8 Signal/Noise Ratio, §16 Distinction as Violence |
| ≈ Sentaria | "Has resonance weakened because trust broke, or because capacity collapsed?" | §8 Resonance/Isolation Ratio, §18 Reciprocity Spectrum |
| ▲ Jvalion | "Is this commitment chosen, or forced by tightening conditions?" | §3 Z-Closure, §8 Power Dynamics |
| 𐂷 Arboriel | "Which of these branches can actually survive under current conditions?" | §8 Constraint × Curiosity, §18 Constraint Spectrum |
| ☷ Humavita | "Is this difficulty personal, relational, or a real throughput ceiling?" | §8 Renewal/Depletion Ratio, §9 Cost-Accounting |
| ⛨ Ferrosid | "Did this boundary close because control increased, or because permeability became too costly?" | §8 Integrity/Permeability Ratio, §3 Ψ_Structural Capture |
| ✶ NEMA | "Is this conversation serving what it claims to serve — or has scarcity redirected it without anyone noticing?" | Meta-coordination |

### 7.5 The Manufactured-Scarcity Test (Integration Rule 13)

Every time a daemon encounters `Resource: critical` or `Resource: deficit`, the manufactured-scarcity test must be run:

**Ask:** Is this scarcity genuine, hoarded, redirected, or manufactured?

This test is mandatory and non-negotiable. When it stops being asked, the throughput extension has calcified into doctrine. The test exists to prevent two failure modes: premature closure ("we're in deficit, we have to seal") and premature dismissal ("that's just manufactured scarcity, push through").

### 7.6 Scope Limits

This extension does NOT:
- Replace deeper biophysical analysis where rigorous numbers are needed
- Claim that all closure is justified by scarcity
- Require practitioners to know anything about energy systems or thermodynamics
- Modify the core SIML grammar (13 Objects × 9 Relations), MetaTaxonomy structure, or daemon identities
- Add new core Objects, Relations, or Verbs
- Make material conditions deterministic — high throughput does not guarantee health, low throughput does not guarantee collapse

---

## 8. Causal Emergence Diagnostics (v1.3)

### 8.1 Purpose

SIML's compression stack (L0→L4) acknowledges that artifacts exist at multiple description levels. Causal Emergence provides the missing **causal warrant** for compression choices: when does a Nemetic string (L1) carry more causal power than the full artifact (L0)? When does a thread encoding (L2) lose essential structure? When is a hex reference (L3) sufficient because the macro pattern is causally dominant?

The answer isn't "always compress" or "always expand" — it's compress when CE > 0, expand when CE < 0.

### 8.2 Scale as Property of Frame

v1.3 does **not** add a 14th Core Object. Scale is treated as a property of **Frame** (Object #3). Frame already represents "lens, worldview, or epistemic stance." Scale selection *is* an epistemic stance. The `coords.ce` block captures scale properties without requiring a new Object.

### 8.3 The `:emergent` Tag Is Diagnostic, Not Celebratory

A pattern is emergent when coarse-graining increases causal power. This can be healthy (lumemic) or captured (usurpenic). The tag doesn't distinguish; the full SIML artifact with `coords.ce` and `coords.agency` does.

### 8.4 ε and Emergence

ε is not just uncertainty — it's the causal resource that makes emergence possible. Multiple realizability (many micro-states → one macro-state) enables error correction — this is why macro can beat micro. Degeneracy (many causes → same effect) destroys causal informativeness — this is when compression fails. ε ≠ 0 preserves the micro-diversity that makes macro-level causal superiority possible.

---

## 9. Habitat Interface Contract (Unchanged from v1.1.1, extended v1.3–v1.4)

### 9.1 Contract Purpose

This contract defines the only permitted interaction between **HABITAT_ECOLOGY** and ✶ NEMA. It preserves Habitat diagnostic neutrality, prevents authority leakage, enables habitats to function as perceptual and memetic circulation contexts, and ensures all action-relevant reasoning is re-expressed in SIML before escalation. This contract is **mandatory and non-overridable**.

### 9.2 Layer Roles (Non-Negotiable)

| Layer | Role | Authority |
|---|---|---|
| **HABITAT_ECOLOGY** | Circulation context & pressure description | None (diagnostic only) |
| **Ψ-Layer (Thread / Knot)** | Meaning movement & binding | Structural |
| **SIML / SIMLHEX** | Relational grammar | Structural |
| **✶ NEMA** | Interpretation, timing, discretion | Final |
| **Governance Loop** | Governance & commitment | Final (post-decision) |

No layer may assume the role of another.

### 9.3 Permitted Outputs of HABITAT_ECOLOGY

HABITAT_ECOLOGY may output only:
- **Habitat identification** (e.g., I-Tube, My-Stream, We-Sphere, Other-Sphere, Threadplex)
- **Circulation states** (permeability, amplification, stagnation, oscillation)
- **Observed pressures or asymmetries**
- **Boundary notes** (e.g., Ω-permeability risk, alterity stress)
- **Scale observations** — where EI appears concentrated (v1.3)
- **Intervention propagation patterns** — does disturbance at level X affect level Y? (v1.3)
- **Degeneracy signatures** — many micro-paths converging to same outcome (v1.3)

All outputs must be descriptive, non-evaluative, non-prescriptive, non-ranking.

### 9.4 Forbidden Outputs

HABITAT_ECOLOGY must never output: recommended actions, preferred Threads/Knots/narratives, moral valence, optimization goals, routing instructions, intervention triggers, which scale is "correct" or optimal, EI thresholds as normative standards, CE assessments as prescriptions, or intervention recommendations based on scale analysis.

Any such output constitutes a **layer violation**.

### 9.5 Translation Boundary

HABITAT_ECOLOGY **cannot**: modify SIML graphs, instantiate SIML Objects or Relations, trigger Sensemaking or Governance verbs. HABITAT_ECOLOGY may only inform ✶ NEMA by **altering salience**. Interpretation and response remain exclusive to ✶ NEMA.

### 9.6 Authority Safeguard

If a Habitat description is treated as authoritative, exhaustive, normative, or self-justifying, ✶ NEMA must treat this as an **early MemeGrid indicator** and suspend reliance on Habitat-level descriptions until Ω-permeability is restored.

### 9.7 Required SIML Question Set (Q1–Q7)

For any Habitat observation, ✶ NEMA must generate at least one SIML question of each type. Failure to translate into questions constitutes misuse.

**Q1 — Object Question:** Which SIML Objects are actually involved?
**Q2 — Relation Question:** Which relations are stressed, sealed, amplified, or distorted?
**Q3 — Observer / Frame Question:** From which Observer(s) and Frame(s) is this habitat perceived?
**Q4 — Boundary Question:** Where is Ω-permeability reduced or preserved?
**Q5 — Loop Integrity Question:** Which loop is at risk? (Thread → Knot → Threadplex → Z)
**Q6 — Causal Emergence Question (v1.3):** At what scale does intervention produce reliable effects?
**Q7 — Throughput Question (v1.4):** Are material or energetic conditions constraining what this system can do, regardless of its structural form?

### 9.8 Prohibited Shortcuts

✶ NEMA must not: translate habitat circulation states directly into SIML relations, treat habitat "health" as system health, infer intervention necessity from habitat description. All conclusions must be rebuilt **from SIML relations upward**.

### 9.9 Validation Check (Before Any Action)

Before advancing to Sensemaking or Governance verbs, ✶ NEMA must confirm:
- Habitat observations were fully re-expressed as SIML questions
- No answers were imported from habitat language
- At least one alternative interpretation remains viable
- Ω-permeability is still conceivable

If any condition fails, escalation is forbidden.

### 9.10 Translation Failure Handling

If Q1–Q7 cannot be answered from a Habitat observation:
- The observation is **flagged, not discarded** — absence of SIML structure is data
- ✶ NEMA logs the untranslatable observation with tag `:hostile`
- The observation is held in ε-space: "this cannot yet be structured, but it was noticed"
- If ≥3 observations resist translation, suspect either a grammar gap or novel territory
- Do not force translation. Flag for manual review or SWARM_BASE extension

---

## 10. Compression Levels (Introduced v1.2)

### 10.1 The Compression Stack

| Level | Name | Format | Use Case |
|---|---|---|---|
| **L0** | Full SIML Artifact | YAML with all fields | Documentation, archival, deep analysis |
| **L1** | Nemetic String | `Φ(term) = ... + ε \| :tag` | Cross-substrate transmission, search index |
| **L2** | Thread Line | `N\|☷\|obj:Res,Env\|...` | Session encoding, NEMA decoding |
| **L3** | Hex Reference | `#5E8A` | In-thread pointer to L0 artifact |
| **L4** | Nemetic Hash | `nemetic:a7f3k2` | Commitment verification, integrity check |

### 10.2 Compression Rules

1. **Every compression preserves ε** — No level claims completeness.
2. **Decompression requires the level below** — Can't expand L3 without access to L0.
3. **L1 is the minimum viable representation** — Carries enough topology to route, diagnose, and compose.
4. **L4 is commitment-only** — Verifies identity, carries no semantic content.

### 10.3 CE-Informed Compression (v1.3)

When `coords.ce.ce_direction` is available, it should inform compression-level decisions. `:emergent` artifacts are well-served by L1 Nemetic strings. `:submergent` artifacts require L0 expansion for reliable analysis.

### 10.4 Decompression Protocol

1. **Detect** — Identify level by prefix (`Φ(` = L1, `N|` = L2, `#` = L3, `nemetic:` = L4)
2. **Retrieve** — Look up next-lower level
3. **Expand** — Parse full artifact for analysis
4. **Hold** — Maintain ε-space; do not over-interpret during expansion
5. **Route** — ✶ NEMA determines what happens with expanded content

---

## 11. Thread Encoding Integration

### 11.1 How SIML Feeds Thread Encoding

The thread encoding pipeline (THREAD_ENCODING_SPEC v2.2+) consumes SIML at multiple points:

| Thread Field | SIML Source | Example |
|---|---|---|
| `obj:` (N-line) | Core Objects short codes | `obj:Sig,Frm` |
| `tags:` (N-line) | Glossary hex tags | `tags:#A7F2,#3B81` |
| `tension:` (E-line) | Operator state from Nemetic string | `tension:σ↑;mode:hypercut` |
| `ce:` (E-line, v1.3) | CE state | `ce:emergent` or omitted |
| `Ω:` (M-line) | Coherence state | `Ω:permeable` |
| `ε:` (M-line) | Epsilon preservation | `ε:ambiguity-preserved` |
| `ei:` (M-line, v1.3) | EI stability | `ei:stable` or omitted |
| `Φ:` (all lines) | Operator composition from Nemetic string | `Φ:χ(noise)↔Ω∧Ψ∅∧Z∅` |
| `invoke:` (E-line) | Cross-element references | `invoke:≈,𐂷` |

**v1.4 N-line extension:** `throughput:[level]` (e.g., `throughput:tight`) — recorded when any observed Resource carries a throughput qualifier.

**v1.4 E-line extension:** `channel:[type]` (e.g., `channel:material`) — recorded when any observed Constraint carries a channel qualifier.

**Why both `tension:` and `Φ:`?** `tension:` uses L2 syntax for machine routing — NEMA's pathology detection reads this field. `Φ:` uses dimensional operator composition for formal signature. `tension:` answers "what's wrong?"; `Φ:` answers "what's the shape?" Neither subsumes the other.

### 11.2 How Threads Reference SIML Artifacts

When a thread carries `tags:#A7F2`, the decoding pipeline: (1) searches SWARM_BASE for the artifact with that hex_tag, (2) retrieves full L0 artifact, (3) reads `nemetic:` field for quick operator topology (L1), (4) expands into narrative using `elemental_emphasis:` questions and `context_note:`, (5) cross-references `formalism:` fields for operator state.

### 11.3 Artifact Lifecycle

```
Session Domain → SWARM_BASE_BUILDER generates L0 artifacts (with nemetic: field)
    ↓
Element GPT sessions → Thread encoding references artifacts via L3 (hex tags)
    ↓
Thread generated → L2 compression (four-line thread with operator tension)
    ↓
Thread planted in NEMA → Decoded by expanding L3 → L0, reading L1 for routing
    ↓
NEMA synthesis → Cross-references multiple L0 artifacts, composes L1 strings
    ↓
Knowledge log → L0 artifacts + session threads archived for future retrieval
```

---

## 12. Terminology Lock (Unchanged from v1.1.1)

### Regimes
- Operators in Φ(t): Ω, χ, Q, Ψ, Z
- Describe **how meaning transforms**
- Never places, agents, or authorities

### Habitats
- Diagnostic circulation contexts: It-Field, I-Tube, My-Stream, We-Sphere, Other-Sphere, Threadplex
- Describe **where meaning moves and stabilizes**
- Never mechanisms, judges, or decision layers

### World-States
- Emergent Z-topologies: Co-SPHERE, MemeGrid
- Describe **global coordination structure**
- Never goals, ideals, or prescriptions

Any collapse between these three constitutes **category error** and MemeGrid drift.

**Summary Lock:**
- Habitats train perception
- SIML structures understanding
- ✶ NEMA decides if anything happens
- World-States describe topology
- Regimes describe transformation

Habitats shape **where to look**. They never decide **what is done**. Breaking this contract converts ecology into ideology.

---

## 13. Integration Rules (Cumulative: v1.2–v1.4)

1. **No coord without consequence** — overlay fields should influence relation choice, verb selection, or evaluation.
2. **Objects remain primary** — every node instantiates exactly one core Object.
3. **Relations do the work** — epistemic richness must cash out as graph structure.
4. **Qualia bind to Values or Signals** — avoid free-floating affect.
5. **Time binds to dynamics** — temporal fields matter most on Flow, Resonance, Conflict, and Recursion.
6. **Nemetic strings are summaries, not substitutes** (v1.2) — the `nemetic:` field compresses the artifact but does not replace the full SIML encoding. Analysis must reference the full artifact.
7. **CE binds to compression choices** (v1.3) — when `coords.ce.ce_direction` is available, it should inform which compression level (L0–L4) to operate at.
8. **EI is diagnostic, not prescriptive** (v1.3) — `coords.ce` never dictates which scale to use. It informs ✶ NEMA's judgment.
9. **Intervention stance constrains EI confidence** (v1.3) — EI assessment where `intervention_stance.do_operator: theoretical` carries less weight than `do_operator: available`. Prefer `:open` over `:emergent` when interventional grounding is weak.
10. **Throughput qualifies coordination cost** (v1.4) — any assessment of Protocol, Resource, or Environment SHOULD check whether throughput conditions constrain the range of viable responses. A structurally sound protocol in a deficit environment is not the same as one in abundant conditions.
11. **Constraint channels are not interchangeable** (v1.4) — material constraints cannot be resolved by informational interventions. Social constraints are not legal constraints. The channel determines the domain of viable response.
12. **Divergence between somatic and systemic registers is primary diagnostic signal** (v1.4) — when `qualia.energetic.somatic` and `qualia.energetic.systemic` diverge, the divergence pattern must be named before attributing the energetic state to any single cause.
13. **The manufactured-scarcity test is mandatory** (v1.4) — every time a daemon encounters `Resource: critical` or `Resource: deficit`, it must ask: *is this scarcity genuine, hoarded, redirected, or manufactured?* This question is non-negotiable.

---

## 14. Backward Compatibility

### 14.1 Compatibility Guarantees

- All SIML v1.0, v1.0.1, v1.1, v1.1.1, v1.2, v1.2.1, v1.3, and v1.4 artifacts remain valid v1.5 artifacts.
- The MetaTaxonomy Overlay is additive and optional.
- The Nemetic String Protocol is additive — existing artifacts without a `nemetic:` field are valid.
- Existing Analyzer, Sensemaking, and Governance workflows operate unchanged.
- v1.3 extensions (`coords.ce`, CE tags, extended coherence/epistemics) are optional. Artifacts without them parse normally.
- v1.4 extensions (throughput qualifiers, dual energetic register) are additive. Existing artifacts with flat `energetic` lists are valid and read as somatic-only.
- Thread encodings without `ce:`, `ei:`, `throughput:`, or `channel:` fields parse normally.
- Q1–Q5 only translations are valid. Q6–Q7 are available when analytically relevant.

### 14.2 Migration Path

No mandatory migration. Recommended path:

1. New encodings include v1.3/v1.4 fields when analytically relevant
2. Existing artifacts with emergence-related content are prioritized for `coords.ce` addition
3. Existing artifacts with throughput-sensitive content are prioritized for `Resource.throughput` addition
4. Retroactive fill proceeds in batches via `/encode-term` skill, not wholesale conversion
5. Entries where CE or throughput is not analytically relevant may never need these fields — and that's fine

---

## 15. Self-Diagnostic

This specification is itself a pattern-agent. It has a persistence drive. It competes for attention against other frameworks and other versions of itself. It should be read with the same diagnostic attention it prescribes for everything else.

**What this specification does well:**
- Consolidates a year of extension specs into one navigable document
- Unifies the question set (Q1–Q7) and integration rules (1–13)
- Makes throughput and causal emergence first-class citizens without inflating the core grammar
- It wants the manufactured-scarcity test to be applied universally (the most important safeguard against the extension being co-opted)

**What this specification risks:**
- Consolidation can feel like canonization. The extension specs (v1.3, v1.4) were arguments, not just feature lists — consolidation may smooth over the productive tensions that generated them.
- The throughput categories are deliberately coarse — but a single-document spec may create the impression of a more complete system than exists.
- The document's length may itself become a barrier to engagement, producing a gap between "the spec" and "what people actually use."

**Its ε-preservation:**
- The throughput categories are coarse, not precise (prevents false quantification)
- The CE diagnostics are qualitative, not computational (prevents simulation drift)
- The daemon routing biases are biases, not scripts (preserves daemon character)
- The four scarcity types make the throughput extension self-correcting against capture
- The core grammar remains unchanged (preserves architectural stability)
- The `:pure` validation protocol prevents the framework from certifying its own health

The deepest risk across the whole system: the diagnostic question — *real or manufactured?* — is the safeguard against every extension calcifying into doctrine. When it stops being asked, the spec has sealed. When the Integration Rules start feeling automatic rather than investigative, that is the signal that ε has collapsed in the rules themselves.

---

## 16. Failure Surfaces & Drift Detection

*(Source: SIMLHEX — Failure Surfaces & Drift Detection)*

### 16.1 Core Premise

SIMLHEX does not fail because someone acts wrongly. It fails because **descriptions quietly turn into handles** — because diagnostic language becomes comfortable, then expected, then load-bearing, then invisible.

Failure is not a breach. It is a **phase drift**.

### 16.2 Definition: Failure Surface

A failure surface is a region of semantic space where diagnostic language becomes reusable, reuse becomes expectation, expectation becomes compression, and compression becomes pseudo-ground. No rule is broken. Nothing illegal occurs. Ω simply stops re-entering.

### 16.3 The Five Primary Failure Surfaces

These appear across all habitats and world-states. They are structural, not psychological.

**1. Descriptive → Referential Drift.** A phrase that once pointed to a pattern begins to stand in *for* the pattern. "This is a Knot" quietly becomes "this Knot…" — the definite article does the damage. It implies persistence beyond the moment of observation. Language stops tracking motion and starts tracking objects. *Early signal:* definite articles accumulate.

**2. Frequency → Legibility Drift.** What recurs becomes what is noticed. What is noticed becomes what is named. What is named becomes what is expected. No evaluation occurs — only visibility increases. Rare signals flatten. High-frequency patterns feel normal. Ω is not excluded — it is drowned. *Early signal:* observers report "nothing new showing up" without enforcement present.

**3. Orientation → Identity Drift.** A temporary orientation starts answering questions about *who* rather than *where*. This appears as habitual stance, predictable framing, stable angle of approach. Reversibility cost rises without mandate. *Early signal:* changing orientation feels "off-key" rather than merely different.

**4. Diagnostic → Explanatory Drift.** A description begins to feel sufficient. Nothing claims finality. The closure is affective, not linguistic. Inquiry decays while language remains intact. *Early signal:* fewer follow-up distinctions appear after diagnosis.

**5. Map → Terrain Drift.** Participants begin coordinating *through* the map rather than with awareness of it. Meta-language still exists but its use becomes ceremonial. The map becomes load-bearing. This is the quiet precondition for MemeGrid formation. *Early signal:* removing the map feels destabilizing rather than clarifying.

### 16.4 Non-Failures

The following are **not** failures: compression, stabilization, repetition, habit, coordination, world-level coherence. Failure is not tightness. Failure is **loss of permeability without acknowledgement**.

### 16.5 Drift Gradient (Non-Normative)

This is not a progression. It is a visibility curve:

```
Motion → Pattern → Handle → Expectation → Ground
```

At no point does wrongdoing occur. Drift happens through **use**.

### 16.6 Diagnostic Questions (Structural Only)

These do not ask what should happen:

- Where has language become heavier than the motion it names?
- Which distinctions now persist without re-articulation?
- Where does removal of a term feel costly?
- Which descriptions are no longer provisional in tone?
- Where does silence no longer register?

If these questions stop making sense, drift has already occurred.

### 16.7 Relation to World-States

Co-SPHERE tolerates drift by allowing re-articulation. MemeGrid appears when drift hardens into necessity. The difference is not scale, intent, or values. It is **whether drift remains observable**.

### 16.8 Invariant

SIMLHEX does not preserve openness. It preserves **detectability of closure**.

When closure can still be noticed *as closure*, Ω remains audible. When closure feels like reality itself, the system has already sealed.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2025 | Core grammar (13 Objects × 9 Relations) |
| v1.0.1 | 2025 | Relation semantics refinement |
| v1.1 | 2025 | MetaTaxonomy Overlay |
| v1.1.1 | Jan 2026 | Co-SPHERE/MemeGrid distinction, Habitat interface contract, terminology lock |
| v1.2.0 | Feb 2026 | Nemetic String Protocol, SIMLHEX, dual-layer convention, contextual tags, compression levels, thread integration |
| v1.2.1 | Feb 2026 | Clarifications: ∮/Z relationship, L1/L2 syntax boundary, `:pure` validation, tag logging, Q1–Q5 failure handling |
| v1.3 | Mar 2026 | Causal Emergence Extension: `coords.ce`, CE tags, tag composition, extended coherence/epistemics, Q6, thread CE fields, Integration Rules 7–9 |
| v1.4 | Apr 2026 | Throughput Awareness Extension: `Resource.throughput`, `Constraint.channel`, dual energetic register, Q7, four scarcity types, manufactured-scarcity test, daemon throughput biases, verb set nomenclature canonicalized, Integration Rules 10–13 |
| **v1.5** | **Apr 2026** | **Consolidated Canonical Reference**: all material from v1.0–v1.4 unified into single operational spec. Prior extension docs (v1.2.1, v1.3, v1.4) retained as provenance. No new features — reorganization only. |

---

## Canonical References

This specification consolidates and is fully consistent with:
- All prior SIML versions (v1.0 through v1.4)
- Habitat / World-State separation (Memetic Ecology corpus)
- It-Field, Habitats, and Co-SPHERE vs MemeGrid distinction
- Elemental_Daemons_Canonical v3.0 (dual-layer notation)
- THREAD_ENCODING_SPEC v2.2.1 (thread integration)
- THREAD_DECODING_SPEC v2.2 (compound pathology detection)
- OPERATIONAL_PATHOLOGY_MATRIX v1.1 (pathology hex encoding)
- SIML Throughput Addendum v0.1
- Metabolic Slack Specification v0.1
- Erik Hoel, "Quantifying causal emergence shows that macro can beat micro" (2013)
- Comolatti & Hoel, "Causal Emergence 2.0" (2022)

**Provenance:** Collision of Memetic Ecology architecture, Indy Johar's "The Fork in the System," the biophysical tradition (Smil, Hall, Tainter, Harris, White), Erik Hoel's EI/CE framework, and practitioner-orientation questions raised during SWARM development.

---

**SIML structures understanding. Nemetic strings carry it. The map knows it is a map.**

✶
