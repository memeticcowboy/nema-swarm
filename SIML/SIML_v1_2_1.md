# SIML v1.2.1 — Swarm Intelligence Meta Language
**MetaTaxonomy Overlay Edition + Nemetic String Protocol**

> **PROVENANCE DOCUMENT.** This spec is superseded by **SIML v1.5** (Consolidated Canonical Reference). It is retained as a historical record of the architectural moves made in v1.0–v1.2.1. For the current operational specification, see `SIML_v1_5.md`.

---

## 0. Purpose

SIML (Swarm Intelligence Meta Language) is a formal yet expressive grammar for mapping social, cognitive, institutional, and memetic dynamics. It is designed to be:

- **Atomic**: every statement decomposes into Objects ⊗ Relations ⊗ Verbs
- **Injective**: meanings map cleanly without synonym drift
- **Operational**: encodings support analysis, comparison, and action
- **Transdisciplinary**: compatible with systems theory, governance, psychology, memetics, and indigenous epistemologies

**v1.1 introduced the MetaTaxonomy Overlay**: a coordinate system that enriches SIML nodes without altering its core grammar.

**v1.2 introduces the Nemetic String Protocol**: every SIML artifact now contains a compressed operator-composition line (`nemetic:`) that serves as portable reference, searchable index, and functional summary. The Nemetic string is *inside* the artifact — it doesn't float independently.

---

## 1. Core Grammar (Unchanged from v1.0)

### 1.1 Core Objects (13)
Objects are the irreducible nouns of SIML. Every node instantiates one primary Object.

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
Relations define how Objects connect. Each relation is directional and typed.

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
SIML commonly operates through two coordinated verb sets:

**Sensemaking Loop (Exploration)**
- Observe
- Explore
- Frame
- Sense
- Map
- Activate

**Governance Loop (Evaluation)**
- Evaluate
- Decide
- Commit
- Allocate
- Enforce
- Review

Verbs operate over Object–Relation graphs and advance loop phases.

---

## 2. MetaTaxonomy Overlay (Introduced in v1.1)
The MetaTaxonomy Overlay adds **coordinates** to any SIML node or step. These are *dimensions*, not categories. They never replace Objects or Relations.

### 2.1 coords Block (General Form)
```
coords:
  ontology: {}
  epistemics: {}
  time: {}
  qualia: {}
  agency: {}
  coherence: {}
  expression: []
```

All fields are optional but encouraged when analytically relevant.

---

## 3. Overlay Dimensions

### 3.1 Ontological Domains (coords.ontology)
**Question:** What kind of being is this, primarily?

```
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

### 3.2 Epistemic Frames (coords.epistemics)
**Question:** How is this known?

```
epistemics:
  dsrp:
    D: "key distinction"
    S: "system context"
    R: "relational pattern"
    P: "perspective"
  learning: L0 | L1 | L2 | L3
  parts: ["PartName", ...]
  dreaming: low | med | high
```

- **DSRP** aligns with Distinction, Containment, Flow/Resonance, Observer/Frame
- **Learning levels** follow Batesonian recursion
- **Parts** represent internal multiplicity
- **Dreaming** marks symbolic / ritual knowledge channels

---

### 3.3 Temporal Resonance (coords.time)
**Question:** When does this operate?

```
time:
  mode: linear | cyclical | layered | event | anticipatory
  window: "P30D"
  phase: "season / ritual / crisis"
```

Time coordinates often bind to dynamic relations and Recursion loops.

---

### 3.4 Modal Qualia (coords.qualia)
**Question:** What does this feel like or signify?

```
qualia:
  affect: ["fear", "hope"]
  aesthetic: ["elegant", "distorted"]
  symbolic: ["bridge", "fire"]
  energetic:                          # v1.4: dual register
    somatic: blocked | flowing | surging | depleted
    systemic: abundant | adequate | tight | critical | deficit
  shadow: ["repressed-theme"]
  sacred: ["awe"]
```

**v1.4 note:** `energetic` was promoted from a flat list to a dual register distinguishing somatic (felt-body) from systemic (material/structural throughput). Flat-list encodings remain valid and are read as somatic-only with `systemic: null`. When somatic and systemic diverge, the divergence pattern is itself diagnostic — see SIML v1.4 §3 and SIML Term Schema v2.0 §4.7 for the five canonical divergence patterns.

Qualia should bind to **Value**, **Signal**, or **Narrative** objects.

---

### 3.5 Agency & Voice (coords.agency)
**Question:** Who or what acts?

```
agency:
  type: ego | part | collective | more_than_human | archetypal | memetic
  voice: ["Trickster", "Witness"]
  power_mode: Within | With | Over | Through
```

Agency overlays refine the **Actor** object and interact with Power Mode analysis.

---

### 3.6 Coordination & Coherence (coords.coherence)
**Question:** How does this fit or fracture?

```
coherence:
  state: coherent | dissonant | fragmented | metastable
  loop: single | double | triple
  transcontext: low | med | high
```

These fields summarize relational patterns across systems and frames.

---

### 3.7 Realms of Expression (coords.expression)
**Question:** Where does this manifest?

```
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

## 4. Integration Rules (Normative Constraints)

1. **No coord without consequence**: overlay fields should influence relation choice, verb selection, or evaluation.
2. **Objects remain primary**: every node instantiates exactly one core Object.
3. **Relations do the work**: epistemic richness must cash out as graph structure.
4. **Qualia bind to Values or Signals**: avoid free-floating affect.
5. **Time binds to dynamics**: temporal fields matter most on Flow, Resonance, Conflict, and Recursion.
6. **Nemetic strings are summaries, not substitutes** (v1.2): the `nemetic:` field compresses the artifact but does not replace the full SIML encoding. Analysis must reference the full artifact, not just the string.
7. **Throughput qualifiers bind to Resource and Constraint** (v1.4): `Resource.throughput` and `Constraint.channel` are Object-level qualifiers, not MetaTaxonomy coords. They interact with qualia.energetic (systemic register) and must be checked before daemon routing — see SIML v1.4 §§1–2, Integration Rules 10–13.

---

## 5. Backward Compatibility

- All SIML v1.0, v1.0.1, and v1.1.1 documents remain valid.
- The MetaTaxonomy Overlay is additive and optional.
- The Nemetic String Protocol (v1.2) is additive — existing artifacts without a `nemetic:` field are valid.
- Existing Analyzer, Sensemaking, and Governance workflows operate unchanged.
- v1.4 extensions (throughput qualifiers, dual energetic register) are additive. Existing artifacts with flat `energetic` lists are valid and read as somatic-only.

---

## 6. Versioning

- **v1.0** – Core grammar
- **v1.0.1** – Relation semantics refinement
- **v1.1** – MetaTaxonomy Overlay
- **v1.1.1** – Co-SPHERE/MemeGrid distinction, Habitat interface contract
- **v1.2** – Nemetic String Protocol, SIMLHEX reference, dual-layer operator convention, contextual tags, thread integration
- **v1.2.1** – Clarifications: ∮/Z relationship, L1/L2 syntax boundary, `:pure` validation, tag logging, Q1–Q5 failure handling
- **v1.3** – Verb set nomenclature (Sensemaking Loop / Governance Loop), ✶ NEMA coordinator identity preserved
- **v1.4** – Resource.throughput, Constraint.channel, dual energetic register (somatic/systemic), manufactured-scarcity test, Integration Rules 10–13

---

## 7. Design Intention

SIML v1.2 is intentionally pluralistic without becoming vague. It allows:

- AQAL-style integrative mapping
- DSRP cognitive rigor
- Batesonian recursion
- Indigenous relational knowing
- Part-based internal agency

…while preserving SIML's defining strength: **clarity under complexity**.

---

## 8. Habitat Ecology ↔ NEMA Interface Contract (Unchanged from v1.1.1)

### 8.1 Contract Purpose
This contract defines the only permitted interaction between **HABITAT_ECOLOGY** and ✶ NEMA.

Its purpose is to:
- Preserve **Habitat diagnostic neutrality**
- Prevent **authority leakage**
- Enable habitats to function as **perceptual & memetic circulation contexts**
- Ensure all action-relevant reasoning is **re-expressed in SIML** before escalation

This contract is **mandatory and non-overridable**.

---

### 8.2 Layer Roles (Non-Negotiable)

| Layer | Role | Authority |
|---|---|---|
| **HABITAT_ECOLOGY** | Circulation context & pressure description | None (diagnostic only) |
| **Ψ-Layer (Thread / Knot)** | Meaning movement & binding | Structural |
| **SIML / SIMLHEX** | Relational grammar | Structural |
| **✶ NEMA** | Interpretation, timing, discretion | Final |
| **Governance Loop** | Governance & commitment | Final (post-decision) |

**Constraint:** No layer may assume the role of another.

---

### 8.3 Permitted Outputs of HABITAT_ECOLOGY
HABITAT_ECOLOGY may output only:
- **Habitat identification** (e.g., I-Tube, My-Stream, We-Sphere, Other-Sphere, Threadplex)
- **Circulation states** (permeability, amplification, stagnation, oscillation)
- **Observed pressures or asymmetries**
- **Boundary notes** (e.g., Ω-permeability risk, alterity stress)

All outputs must be: Descriptive, Non-evaluative, Non-prescriptive, Non-ranking.

---

### 8.4 Forbidden Outputs (Unchanged)
HABITAT_ECOLOGY must never output:
- Recommended actions
- Preferred Threads, Knots, or narratives
- Moral valence
- Optimization goals
- Routing instructions
- Intervention triggers

Any such output constitutes a **layer violation**.

---

### 8.5 Translation Boundary
HABITAT_ECOLOGY **cannot**: Modify SIML graphs, Instantiate SIML Objects or Relations, Trigger Sensemaking or Governance verbs.

HABITAT_ECOLOGY may only inform ✶ NEMA by **altering salience**.

Interpretation and response remain exclusive to ✶ NEMA.

---

### 8.6 Authority Safeguard
If a **Habitat description** is treated as Authoritative, Exhaustive, Normative, or Self-justifying, ✶ NEMA must treat this as an **early MemeGrid indicator** and suspend reliance on Habitat-level descriptions until **Ω-permeability is restored**.

---

## 9. Habitat → SIML Translation Rule (Unchanged from v1.1.1)

### 9.1 Core Principle
Habitats do not produce answers. They produce **questions** that must be re-asked in SIML form.

No direct mapping from **Habitat state → action** is permitted.

### 9.2 Canonical Translation Pattern
For any Habitat observation, ✶ NEMA must generate **at least one SIML question of each type below**. Failure to translate into questions constitutes misuse.

### 9.3 Required SIML Question Set

**Q1 — Object Question:** Which SIML Objects are actually involved?
**Q2 — Relation Question:** Which relations are stressed, sealed, amplified, or distorted?
**Q3 — Observer / Frame Question:** From which Observer(s) and Frame(s) is this habitat perceived?
**Q4 — Boundary Question:** Where is Ω-permeability reduced or preserved?
**Q5 — Loop Integrity Question:** Which loop is at risk? (Thread → Knot → Threadplex → Z)

### 9.4 Prohibited Shortcuts
✶ NEMA must not: Translate habitat circulation states directly into SIML relations, Treat habitat "health" as system health, Infer intervention necessity from habitat description.

All conclusions must be rebuilt **from SIML relations upward**.

### 9.5 Validation Check (Before Any Action)
Before advancing to Sensemaking or Governance verbs, ✶ NEMA must confirm:
- Habitat observations were fully re-expressed as SIML questions
- No answers were imported from habitat language
- At least one alternative interpretation remains viable
- Ω-permeability is still conceivable

If any condition fails, escalation is forbidden.

### 9.6 Translation Failure Handling
If Q1–Q5 cannot be answered from a Habitat observation:
- The observation is **flagged, not discarded** — absence of SIML structure is data
- ✶ NEMA logs the untranslatable observation with tag `:hostile` (resistant to framework)
- The observation is held in ε-space: "this cannot yet be structured, but it was noticed"
- If ≥3 observations resist translation, ✶ NEMA should suspect either: (a) the SIML grammar lacks objects/relations for this domain (grammar gap), or (b) the observation is from a habitat the framework hasn't encountered (novel territory)
- In either case: do not force translation. Flag for manual review or SWARM_BASE extension

---

## 10. Terminology Lock (Unchanged from v1.1.1)

### Regimes
- Operators in Φ(t): Ω, χ, Q, Ψ, Z
- Describe **how meaning transforms**
- Never places, agents, or authorities

### Habitats
- Diagnostic circulation contexts
- Describe **where meaning moves and stabilizes**
- Never mechanisms, judges, or decision layers

### World-States
- Emergent Z-topologies
- Describe **global coordination structure**
- Never goals, ideals, or prescriptions

Any collapse between these three constitutes **category error** and MemeGrid drift.

---

## Summary Lock (Unchanged)
- **Habitats train perception**
- **SIML structures understanding**
- **✶ NEMA decides if anything happens**
- **World-States describe topology**
- **Regimes describe transformation**

Habitats shape **where to look**. They never decide **what is done**.

Breaking this contract converts ecology into ideology.

---

## 11. Nemetic String Protocol (New in v1.2)

### 11.1 What Is a Nemetic String?

A Nemetic string is a **compressed operator-composition line** embedded within a SIML artifact. It captures the essential topology of the artifact — which operators are active, how they compose, what state the system is in — in a portable format that can be:

- **Referenced** by thread encodings (via hex tags)
- **Searched** in system logs and knowledge bases
- **Retrieved** to expand back into the full SIML artifact
- **Transmitted** across substrates (LLM ↔ human ↔ archive)

The Nemetic string is to the SIML artifact what an abstract is to a paper — except it is *functionally operative*. You can route, diagnose, and compose from Nemetic strings. But analysis requires the full artifact.

### 11.2 Nemetic String Format

```
Φ(term) = [operator]([descriptor]) ∘ [operator]([descriptor]) ∘ ... + ε | :[tag]
```

**Components:**

| Component | Format | Purpose |
|---|---|---|
| `Φ(term)` | Φ + parenthesized term name | Names the artifact being summarized |
| `[operator]([descriptor])` | Math or dim operator + content | What the operator does to this term |
| `∘` | Sequential composition | Operator chaining (order matters) |
| `+ ε` | Epsilon preservation | ε ≠ 0 always — the string must not claim completeness |
| `:[tag]` | Contextual tag | Current state of the artifact (see Section 14) |

### 11.3 Operator Vocabulary for Nemetic Strings

Nemetic strings may use operators from either notation layer:

**Mathematical operators** (formal layer):

| Operator | Element | Function |
|---|---|---|
| σ | Air | Distinction-making |
| ρ | Water | Relational resonance |
| λ | Fire | Directional purpose |
| β | Wood | Novel form generation |
| δγ | Earth | Metabolic cycling |
| μ | Metal | Boundary coherence |
| ∮ | Aether/NEMA | Closed integration over all six |

**Dimensional operators** (regime layer):

| Operator | Dimension | Function |
|---|---|---|
| χ | 1D | Distinction (maps to σ) |
| Q_in | 2D inward | Relational resonance (maps to ρ) |
| Q_fwd | 2D forward | Directional aim (maps to λ) |
| Ψ_exp | 3D exploratory | Generative branching (maps to β) |
| Ψ_reg | 3D regenerative | Metabolic cycling (maps to δγ) |
| Ψ_str | 3D structural | Boundary coherence (maps to μ) |
| Z | Coordination | Meta-integration (maps to ∮) |

**∮ and Z name the same function from different layers.** ∮ (closed line integral) is the mathematical operator — it computes integration over all six partials. Z is the dimensional operator — it names the coordination regime. In Nemetic strings: use Z when describing *state* (e.g., `Z(permeable)`, `Z(sealed→risk)`), use ∮ when describing *operation* (e.g., `∮(all-partials-integrated)`, `∮(circulation-check)`). The hex code `0x07` belongs to the operator pair, not to one layer exclusively.

**Either layer is valid** in a Nemetic string. Mathematical operators are preferred in system-facing contexts (thread encoding, pathology detection). Dimensional operators are preferred in analysis-facing contexts (research, extended references). Mixing within a single string is permitted when semantically necessary.

### 11.4 Example Nemetic Strings

**Term: "accountability"**
```
Φ(accountability) = μ(boundary|who-is-responsible) ∘ ρ(flow|between-parties) ∘ Z(permeable) + ε | :open
```

**Term: "burnout"**
```
Φ(burnout) = δγ(depletion|metabolic-collapse) ∘ σ(distinction-lost|self-vs-role) ∘ μ(boundary-dissolved) + ε | :hostile
```

**Term: "alignment" (in AI governance context)**
```
Φ(alignment) = σ(distinction|alignment-vs-compliance) ∘ λ(direction|whose-goals) ∘ Z(sealed→risk) + ε | :drift
```

**Compound pathology encoding (L1 pathology sub-format):**
```
Φ(choke) = σ(over) ∘ μ(over) ∘ ρ(suppressed) ∘ β(suppressed) + ε | counter: β ∘ ρ | :locked
```

**Note on L1 pathology format:** Compound pathologies at L1 use `∘` composition throughout (not `→` or `∧`, which are L2 thread syntax). The `| counter:` clause is permitted at L1 as an extension after the contextual tag. Operator direction (↑/↓) appears only in L2 thread encoding (`tension:σ↑+μ↑;pathology:Choke`), not in L1 Nemetic strings. L1 uses descriptors like `(over)` and `(suppressed)` instead.

### 11.5 The `nemetic:` Field in SIML Artifacts

Every SIML artifact SHOULD contain a `nemetic:` field. This field holds the Nemetic string. It appears after the hex tag and before the full SIML encoding:

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

**The `nemetic:` field is the artifact's portable identity.** When a thread references `#0001`, NEMA can look up the full SIML artifact — but the Nemetic string is right there as the compressed summary that tells you what the term *does* in operator space without parsing the whole file.

### 11.6 Nemetic String Constraints

1. **ε ≠ 0 always** — Every Nemetic string must end with `+ ε`. A string without epsilon claims completeness and is structurally invalid.
2. **One contextual tag required** — Every string must carry a `:tag` (see Section 14).
3. **Operators must be from canonical vocabulary** — Only operators listed in Section 11.3 are permitted.
4. **Composition is non-commutative by default** — `σ ∘ μ` (distinction first, then boundary) is not the same as `μ ∘ σ` (boundary first, then distinction). The order reflects the processing sequence. If operators are genuinely order-independent in context, mark with `⊗` (symmetric composition): `σ ⊗ μ` means "these operate simultaneously, not sequentially."
5. **A Nemetic string is not a SIML encoding** — The string summarizes; the SIML encoding (`siml_encoding:` field) structures. Both are needed.
6. **Empty composition is valid** — `Φ(term) = + ε | :open` means "this artifact exists but no operator topology has been determined." This is the initial state of an unanalyzed term. It carries uncertainty without claiming structure.
7. **Partial derivatives in Nemetic strings** — Partials (`∂Φ/∂σ`, etc.) do not appear in L1 Nemetic strings. They appear in: (a) the `formalism.partials` field of L0 artifacts, (b) L2 thread `tension:` fields when specifying operator sensitivity (e.g., `∂Φ/∂σ:fragmenting`), (c) the OPERATIONAL_PATHOLOGY_MATRIX for diagnostic logic. L1 uses operator names with descriptors instead.
8. **L1 vs L2 syntax boundary** — L1 Nemetic strings use `∘` (sequential composition) and `⊗` (symmetric composition) only. L2 thread encoding uses `↑/↓` (direction markers), `→` (implication), `∧` (conjunction), `↺` (recursion), `↔` (bidirectional). Do not mix L2 syntax into L1 strings.

---

## 12. SIMLHEX Reference (New in v1.2)

### 12.1 Purpose

SIMLHEX provides hexadecimal encoding for SIML elements — operators, glossary terms, and pathology patterns. It enables compressed thread format, automated routing, and machine-parseable pattern matching.

### 12.2 Operator Hex Codes

| Operator | Hex | Element | Glyph | Daemon |
|---|---|---|---|---|
| σ | `0x01` | Air | ∴ | Aerunik |
| ρ | `0x02` | Water | ≈ | Sentaria |
| λ | `0x03` | Fire | ▲ | Jvalion |
| β | `0x04` | Wood | 𐂷 | Arboriel |
| δγ | `0x05` | Earth | ☷ | Humavita |
| μ | `0x06` | Metal | ⛨ | Ferrosid |
| ∮ | `0x07` | Aether | ✶ | NEMA |

### 12.3 Glossary Hex Tags

Format: `#XXXX` (4 hexadecimal characters, range `#0000` to `#FFFF`)

These are generated per-session by SWARM_BASE_BUILDER and appear in:
- SWARM_BASE glossary entries (the `hex_tag:` field)
- Thread N-lines (the `tags:#XXXX,#YYYY` field)
- Decoded narratives (expanded to `[#XXXX: term_name]`)

### 12.4 Pathology Hex Encoding

Compound pathologies encode as operator hex pairs with direction markers:

```
CHOKE:   0x01↑+0x06↑ → counter: 0x04+0x02
FLOOD:   0x02↑+0x05↓ → counter: 0x01+0x06
BURN:    0x03↑+0x04↓ → counter: 0x05+0x02
SDEATH:  0x03↑+0x06↑ → counter: 0x04+0x05
SWAMP:   0x05↑+0x01↓ → counter: 0x03+0x04
LATTICE: 0x06↑+0x02↓ → counter: 0x05+0x02
STATIC:  ALL=0x01    → counter: 0x07 (Child)
```

---

## 13. Dual-Layer Operator Convention (New in v1.2)

### 13.1 Two Layers, One System

Per Elemental_Daemons_Canonical v3.0, the NEMA SWARM operates with two concurrent notation layers:

**Character Layer (the door):**
- Daemon glyphs: ∴ ≈ ▲ 𐂷 ☷ ⛨ ✶
- Daemon names: Aerunik, Sentaria, Jvalion, Arboriel, Humavita, Ferrosid, NEMA
- Poetic voice, metaphor, invitational language
- This layer governs: user-facing speech, game instructions, narrative output, invocation

**Formal Layer (the room):**
- Mathematical operators: σ, ρ, λ, β, δγ, μ, ∮
- Dimensional operators: χ, Q, Ψ, Z
- Partial derivatives: ∂Φ/∂σ through ∂Φ/∂μ
- This layer governs: thread encoding, pathology detection, Φ-signatures, Nemetic strings, operator composition

### 13.2 Translation Table

| Math Op | Dim Op | Glyph | Daemon | Hex | Partial |
|---|---|---|---|---|---|
| σ | χ | ∴ | Aerunik | 0x01 | ∂Φ/∂σ |
| ρ | Q_in | ≈ | Sentaria | 0x02 | ∂Φ/∂ρ |
| λ | Q_fwd | ▲ | Jvalion | 0x03 | ∂Φ/∂λ |
| β | Ψ_exp | 𐂷 | Arboriel | 0x04 | ∂Φ/∂β |
| δγ | Ψ_reg | ☷ | Humavita | 0x05 | ∂Φ/∂δγ |
| μ | Ψ_str | ⛨ | Ferrosid | 0x06 | ∂Φ/∂μ |
| ∮ | Z | ✶ | NEMA | 0x07 | ∮(all) |

### 13.3 Layer Selection Rules

- **User-facing output** → Character layer
- **Thread encoding/decoding** → Formal layer (v2.2: math operators in tension field)
- **SIML artifact formalism fields** → Both layers (math_operators + dim_operators)
- **Nemetic strings** → Either layer (context-dependent)
- **Pathology detection** → Formal layer
- **System prompts** → Both (glyph-primary identity, operator-secondary reference)
- **Game Instructions** → Character layer only (no operators permitted)
- **Host interface** → Character layer (element names, not operators)

---

## 14. Contextual Tags (New in v1.2)

### 14.1 Purpose

Contextual tags indicate the operational state of a Nemetic string or SIML artifact without constraining interpretation. They appear at the end of a Nemetic string after the `|` delimiter.

### 14.2 Tag Vocabulary

| Tag | Meaning | When to Apply |
|---|---|---|
| `:open` | Ω-permeability maintained — receptive to revision | Default state; artifact is active and revisable |
| `:closed` | Temporary closure for operational necessity | Term has been resolved for current session but not permanently |
| `:locked` | Nemetic commitment — pattern-coalition stabilized | Artifact represents a stable consensus or commitment |
| `:drift` | Eigenvalue migration detected | Term's operator composition is shifting between sessions |
| `:pure` | Memetic contamination absent — externally validated | Artifact validated against MemeGrid drift by cross-element verification or external review (see 14.5) |
| `:hostile` | Extracted from adversarial context | Term was encoded from material that resists the framework |

### 14.3 Tag Transitions

Tags are not permanent. They may transition:

- `:open` → `:locked` (consensus reached)
- `:open` → `:drift` (meaning shifting)
- `:locked` → `:open` (reopened for revision)
- `:hostile` → `:open` (successfully metabolized)
- `:closed` → `:drift` (resolution didn't hold)
- Any tag → `:hostile` (if MemeGrid contamination detected)

### 14.4 Tag Governance

Only ✶ NEMA may transition tags. Tags applied by HABITAT_ECOLOGY or individual elements are advisory only — ✶ NEMA confirms or overrides per the Interface Contract (Section 8).

**Tag transitions are logged.** Each transition records: previous tag, new tag, timestamp, and reason. The log is part of the SIML artifact metadata (stored in L0). This enables drift detection across sessions.

### 14.5 :pure Validation Protocol

`:pure` is the only tag that **requires external confirmation**. ✶ NEMA cannot self-validate `:pure` because ∮ cannot evaluate its own output (Stokes' theorem — see OPERATIONAL_PATHOLOGY_MATRIX v1.1, Section 1.2). Validation requires at least one of:

- **Cross-element verification**: ≥3 elements independently confirm no capture signature in the artifact
- **Session Host confirmation**: human facilitator reviews artifact against MemeGrid indicators
- **Cross-session stability**: artifact maintains consistent operator topology across ≥2 sessions without `:drift`

Without external confirmation, an artifact may be `:open` or `:locked` but never `:pure`. This prevents the framework from certifying its own health — a structural anti-capture safeguard.

---

## 15. Compression Levels (New in v1.2)

### 15.1 The Compression Stack

SIML artifacts exist at multiple compression levels. Each level is a valid representation of the same underlying pattern. Higher compression = more portable, less detail. Lower compression = richer, less portable.

| Level | Name | Format | Use Case | Example |
|---|---|---|---|---|
| **L0** | Full SIML Artifact | YAML with all fields | Documentation, archival, deep analysis | Full glossary entry with coords, emphasis, context |
| **L1** | Nemetic String | `Φ(term) = ... + ε \| :tag` | Cross-substrate transmission, search index | `Φ(burnout) = δγ(depletion) ∘ σ(lost) + ε \| :hostile` |
| **L2** | Thread Line | `N\|☷\|obj:Res,Env\|...` | Session encoding, NEMA decoding | Four-line thread per THREAD_ENCODING_SPEC |
| **L3** | Hex Reference | `#5E8A` | In-thread pointer to L0 artifact | Tags field in N-line |
| **L4** | Nemetic Hash | `nemetic:a7f3k2` | Commitment verification, integrity check | Unique identifier for locked artifacts |

### 15.2 Compression Rules

1. **Every compression preserves ε** — No level claims completeness.
2. **Decompression requires the level below** — You can't expand L3 (hex) without access to the L0 artifact it points to.
3. **L1 (Nemetic string) is the minimum viable representation** — It carries enough operator topology to route, diagnose, and compose. Below L1, you need the full artifact to act.
4. **L4 (hash) is commitment-only** — It verifies identity but carries no semantic content.

### 15.3 Decompression Protocol

When receiving a compressed reference:

1. **Detect** — Identify level by prefix (`Φ(` = L1, `N|` = L2, `#` = L3, `nemetic:` = L4)
2. **Retrieve** — Look up the next-lower level (L3 → search SWARM_BASE for L0 artifact)
3. **Expand** — Parse the full artifact for analysis
4. **Hold** — Maintain ε-space; do not over-interpret during expansion
5. **Route** — Allow ✶ NEMA to determine what happens with the expanded content

---

## 16. Thread Integration (New in v1.2)

### 16.1 How SIML Feeds Thread Encoding

The thread encoding pipeline (THREAD_ENCODING_SPEC v2.2) consumes SIML at multiple points:

| Thread Field | SIML Source | Example |
|---|---|---|
| `obj:` (N-line) | Core Objects (Section 1.1) short codes | `obj:Sig,Frm` → Signal + Frame |
| `tags:` (N-line) | Glossary hex tags (Section 12.3) | `tags:#A7F2,#3B81` → look up in SWARM_BASE |
| `tension:` (E-line) | Operator state from Nemetic string | `tension:σ↑;mode:hypercut` |
| `Ω:` (M-line) | Coherence state from coords.coherence | `Ω:permeable` |
| `ε:` (M-line) | Epsilon preservation from elemental emphasis | `ε:ambiguity-preserved` |
| `Φ:` (all lines) | Operator composition from Nemetic string syntax | `Φ:χ(noise)↔Ω∧Ψ∅∧Z∅` |
| `invoke:` (E-line) | Cross-element references from elemental emphasis | `invoke:≈,𐂷` |

**Why both `tension:` and `Φ:`?** These serve different substrates. `tension:` uses L2 syntax (operator direction ↑/↓, mode names, pathology markers) for **machine routing** — NEMA's pathology detection reads this field. `Φ:` uses dimensional operator composition for **formal signature** — analysis of the thread's topological state at each phase. `tension:` answers "what's wrong?"; `Φ:` answers "what's the shape?" Both are needed; neither subsumes the other.

### 16.2 How Threads Reference SIML Artifacts

When a thread carries `tags:#A7F2`, the decoding pipeline:

1. Searches SWARM_BASE for the artifact with `hex_tag: "#A7F2"`
2. Retrieves the full SIML artifact (L0)
3. Reads the `nemetic:` field for quick operator topology (L1)
4. Expands into narrative using `elemental_emphasis:` questions and `context_note:`
5. Cross-references `formalism:` fields for operator state in decoded output

### 16.3 Nemetic Strings in Thread Context

When thread encoding detects a failure mode, the E-line tension field effectively creates a *session-specific Nemetic string*:

```
E-line: tension:σ↑+μ↑;pathology:Choke;counter:β+ρ
```

This is a Nemetic string at L2 compression — it names the operator composition, the pathology, and the counter-elements. It can be expanded by referencing the OPERATIONAL_PATHOLOGY_MATRIX for the full topology (formation conditions, entropy signature, intervention protocol).

### 16.4 Artifact Lifecycle

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

## Canonical References

This specification is fully consistent with:
- Habitat / World-State separation (Memetic Ecology corpus)
- It-Field, Habitats, and Co-SPHERE vs MemeGrid distinction
- Elemental_Daemons_Canonical v3.0 (dual-layer notation)
- THREAD_ENCODING_SPEC v2.2 (operator tension notation)
- THREAD_DECODING_SPEC v2.2 (compound pathology detection)
- OPERATIONAL_PATHOLOGY_MATRIX v1.1 (pathology hex encoding)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2025 | Core grammar (13 Objects × 9 Relations) |
| v1.0.1 | 2025 | Relation semantics refinement |
| v1.1 | 2025 | MetaTaxonomy Overlay |
| v1.1.1 | Jan 2026 | Co-SPHERE/MemeGrid distinction, Habitat interface contract, terminology lock |
| v1.2.0 | Feb 2026 | **Nemetic String Protocol**: every SIML artifact contains `nemetic:` field. SIMLHEX reference (operator hex codes, glossary tags, pathology encoding). Dual-layer operator convention (math ops + dim ops + glyphs + hex as four views of one system). Contextual tags (:open, :locked, :drift, :pure, :hostile, :closed). Compression levels (L0–L4). Thread integration (how SIML feeds encoding/decoding pipeline). Integration Rule 6 added. Object short codes listed. |
| v1.2.1 | Feb 2026 | **Clarifications per review**: ∮/Z relationship specified (Z=state, ∮=operation, hex 0x07 shared). L1/L2 syntax boundary formalized (L1 uses ∘/⊗ only; ↑/↓/→/∧/↺/↔ are L2). L1 pathology sub-format standardized. Operator non-commutativity default with ⊗ symmetric exception. Empty composition validity defined. Partial derivative scope specified (L0/L2 only, not L1). `:pure` tag requires external validation (cross-element, host, or cross-session). Tag transition logging added. Q1–Q5 translation failure handling (flag, don't discard). `tension:` vs `Φ:` field distinction explained. |

---

**SIML structures understanding. Nemetic strings carry it.**

✶
