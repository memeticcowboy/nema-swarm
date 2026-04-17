# SIML Term Schema v2.0 — Multi-Faceted Taxonomy

**Status:** Draft — pending distribution test on prefix design
**Supersedes:** Ad hoc series-letter schema (A/C/D/E/L/M/P/S/WO)
**Dependencies:** SIML v1.3, THREAD_ENCODING_SPEC v2.2, ENCODE_TERM_SKILL.md, SIML Throughput Addendum v0.1

---

## 0. Design Rationale

The series-letter system (A, C, D, etc.) encoded **source domain** — a processing artifact of which batch a concept entered the corpus through. It carried no semantic information about the concept itself, produced cross-series duplicates (Status Quo Bias at A053/C018/C065), and conflated two unrelated uses of "hex" (term cross-references vs operator SIMLHEX codes).

This schema replaces series-letter classification with a **seven-facet taxonomy** derived from fields already present in term.yaml. The taxonomy is intrinsic to the concept, not the encoding pipeline.

### Key Structural Changes

1. **`lifecycle:`** — new field, independent of `Z_state:`. Lifecycle describes the *entry's maturity*. Z_state describes the *concept's closure dynamics*. These are orthogonal: an entry can be `lifecycle: canonical` with `Z_state: open` (mature encoding of an inherently permeable concept).

2. **`operator_hex:` / `related_terms:`** — split from the former `hex:` field, which conflated operator SIMLHEX codes (`0x01`–`0x07`) with term cross-references (`#A01B`, `#C16D`). Now two distinct fields with clear semantics.

3. **`elemental_signature:`** — unified format replacing the inconsistent mix of qualitative `elemental_emphasis` (A/C-series) and quantified `emphasis: {0.XX}` (S-series). Supports both ranked and weighted representations.

4. **`term_id:`** — replaces series-letter prefix with ontological-ground prefix. Provisional until distribution test resolves prefix design (see §1.1).

---

## 1. Term Identity

### 1.1 term_id Format

```
{ontological_prefix}-{hex_counter}_{snake_case_name}
```

**Ontological prefixes (provisional — pending distribution test):**

| Prefix | Ontological Ground | Description |
|--------|--------------------|-------------|
| `I`    | I (subjective)     | Individual interior experience, cognition, bias, perception |
| `W`    | We (intersubjective) | Collective, relational, cultural, social |
| `T`    | It (objective)     | Measurable, formal, empirical, technical |
| `S`    | Its (systemic)     | Cross-ground patterns, operators, meta-level structures |
| `M`    | MoreThanHuman      | Ecological, planetary, non-human agency |
| `V`    | Virtual            | Computational, simulated, AI-substrate |

**If distribution test shows I-ontology > 60% of corpus**, switch to two-character compound prefix encoding ontological ground + agency type:

| Compound | Meaning |
|----------|---------|
| `IE`     | I-ontology, ego agency (individual experiencing) |
| `IM`     | I-ontology, memetic agency (pattern operating through individual) |
| `IA`     | I-ontology, archetypal agency |
| `WC`     | We-ontology, collective agency |
| `WM`     | We-ontology, memetic agency |
| etc.     | ... |

**Hex counter:** Sequential within ontological class. Managed by `hex_registry.yaml`. Format: 4-digit hex (`0000`–`FFFF`), providing 65,536 entries per class. No semantic encoding in the counter — it's pure sequence.

**Examples:**
```
I-0A3F_Barnum_Effect
W-02B1_Collective_Intelligence
T-0C7D_Category_Theory
S-001A_Chi_Operator
M-0012_Mycorrhizal_Network
V-0003_LLM_Substrate_Bias
```

### 1.2 Provenance (Not Classification)

```yaml
source_domain: "A-series"           # which encoding batch — metadata, not taxonomy
source_file: "original_filename.md" # original source material
date_processed: "2026-01-15"
processed_by: "Claude/SIML"
siml_version: "1.3"
```

---

## 2. Lifecycle

```yaml
lifecycle: canonical    # draft | working | canonical | superseded | composted
superseded_by: []       # list of term_ids — supports many-to-one and one-to-many
composted_into: null    # term_id of what absorbed this entry's substance (if composted)
composted_at: null      # ISO date
```

**Lifecycle values:**

| Value | Meaning | Registry |
|-------|---------|----------|
| `draft` | Initial encoding, minimal review | Registry 3 (open) |
| `working` | Under active development, versioned, reviewed | Registry 2 (working) |
| `canonical` | Stable, consolidated, confirmed by review | Registry 1 (SIML) |
| `superseded` | Replaced by successor(s), retained for provenance | Archive (indexed at zero weight) |
| `composted` | Dissolved back into substrate, no direct successor | Archive (indexed at near-zero weight) |

**Lifecycle is independent of Z_state.** Z_state describes the concept's own closure dynamics. Lifecycle describes the entry's maturity in the registry.

| Example | Z_state | Lifecycle | Meaning |
|---------|---------|-----------|---------|
| Barnum Effect | `open` | `canonical` | Mature encoding of an inherently permeable concept |
| Draft encoding of new bias | `open` | `draft` | New, unreviewed, concept also open |
| Consolidated learning theory | `semi` | `canonical` | Stable encoding of a partially-closed concept |
| Abandoned early encoding | `drift` | `composted` | Entry dissolved, concept was drifting |

**Composted entries retain minimal frontmatter:**

```yaml
term_id: "I-0042_Abandoned_Concept"
lifecycle: composted
composted_into: "I-0A3F_Barnum_Effect"  # what absorbed this
composted_at: "2026-03-15"
# all other fields removed or minimized
```

**Supersession supports both directions:**

```yaml
# Many-to-one: three entries merge into one
# On each old entry:
lifecycle: superseded
superseded_by: ["I-0A3F_Barnum_Effect"]

# One-to-many: one entry splits into specific entries
# On the old entry:
lifecycle: superseded
superseded_by: ["I-0B12_Anchoring_Bias", "I-0B13_Availability_Bias"]
```

---

## 3. The Seven Facets (Semantic Classification)

Every term carries coordinates along seven independent dimensions. These are the queryable taxonomy — the basis for multi-faceted retrieval, daemon routing, and graph traversal.

### 3.1 Ontological Ground

```yaml
coords:
  ontology:
    primary: I              # I | We | It | Its | MoreThanHuman | Virtual
    secondary: [Its]        # for genuinely multi-ground concepts
```

Most stable facet. Changes least as framework understanding evolves. Primary ground is encoded in term_id prefix.

### 3.2 Agency Mode

```yaml
  agency:
    type: ego               # ego | part | collective | more_than_human | archetypal | memetic
    voice: []               # optional: named perspectives/agents
    power_mode: With        # Within | With | Over | Through
```

Cross-cuts ontology. An I-ontology concept can have `memetic` agency (pattern operating through individual) or `ego` agency (individual's own experience).

### 3.3 Operational State (Z_state)

```yaml
formalism:
  Z_state: open             # open | semi | sealed | drift | locked | hostile
  tendency: "S/N → 0.2"    # tendency ratio and value
```

Property of the **concept**, not the entry. How permeable is this pattern's boundary? Independent of lifecycle. The six values are from the existing spec — no changes here.

### 3.4 Causal Scale

```yaml
coords:
  ce:
    ei_state: med                    # high | med | low | unknown
    ce_direction: flat               # emergent | submergent | flat | multiscale | unknown
    scale_note: "description"
    determinism: med                 # high | med | low
    degeneracy: med                  # high | med | low
    sufficiency: med                 # high | med | low (CE 2.0)
    necessity: med                   # high | med | low (CE 2.0)
```

Per SIML v1.3 spec. No changes — already well-specified.

### 3.5 Temporal Mode

```yaml
  time:
    mode: event             # linear | cyclical | layered | event | anticipatory
    phase: "description"
```

### 3.6 Elemental Signature

```yaml
elemental_signature:
  dominant: [air]           # 1-2 elements carrying most weight
  secondary: [water, metal] # supporting elements
  suppressed: []            # elements notably absent — diagnostically important
  weights:                  # optional quantified form (from S-series)
    air: 0.72
    water: 0.45
    metal: 0.58
    fire: 0.15
    wood: 0.22
    earth: 0.30
```

**New field: `suppressed`.** The diagnostic value of elemental signature is not just what's present but what's silent. An entry with Air and Metal dominant but Earth suppressed has a specific pathology risk (distinction-making without metabolic grounding). The `suppressed` field makes this explicit and queryable.

### 3.7 Coherence Pattern

```yaml
  coherence:
    state: metastable       # coherent | dissonant | fragmented | metastable
    loop: double            # single | double | triple
    transcontext: high      # low | med | high
    ei_stability: stable    # stable | drifting | collapsing | amplifying (v1.3)
    scale_dominance: distributed  # micro | macro | distributed | contested (v1.3)
```

---

## 4. Framework Encoding

### 4.1 Nemetic String

```yaml
nemetic: >-
  Φ(BarnumEffect) = σ(specific|universal)
                  ∘ ρ(personal|vague)
                  ∘ λ(meaning|projection)
                  ∘ β(self-recognition|feedback)
                  ∘ δγ(validation|comfort)
                  ∘ μ(boundary|porous)
                  + ε | :open
```

### 4.2 SIML Encoding

```yaml
siml_encoding: >-
  ⟨Statement|vague⟩
      ⊳ ⟨Interpretation|personal⟩
      → ⟨Recognition|self⟩
      ⊗ ⟨Accuracy|perceived⟩
      ⇄ ⟨Meaning|projected⟩
```

### 4.3 Formalism

```yaml
formalism:
  math_operators: [σ, ρ, λ, β, δγ, μ]
  dim_operators: [χ, Q_in, Q_fwd, Ψ_exp, Ψ_reg, Ψ_str]
  partials:
    - "∂Φ/∂σ (description of sensitivity)"
    - "∂Φ/∂ρ (description of sensitivity)"
    - "∂Φ/∂λ (description of sensitivity)"
    - "∂Φ/∂β (description of sensitivity)"
    - "∂Φ/∂δγ (description of sensitivity)"
    - "∂Φ/∂μ (description of sensitivity)"
  Z_state: open
  tendency: "S/N → 0.2"
  operator_hex:             # SIMLHEX operator codes — SEPARATED from cross-references
    - "0x01"                # σ/Air
    - "0x02"                # ρ/Water
    - "0x03"                # λ/Fire
    - "0x04"                # β/Wood
    - "0x05"                # δγ/Earth
    - "0x06"                # μ/Metal
```

### 4.4 Cross-References

```yaml
related_terms:              # explicit term_id references — SEPARATED from operator_hex
  - "I-02B1_Cognitive_Babel"
  - "I-03C7_Motivated_Reasoning"
```

### 4.5 Elemental Emphasis (Qualitative)

```yaml
elemental_emphasis:
  ∴: "Air question or analysis"
  ≈: "Water question or analysis"
  ▲: "Fire question or analysis"
  𐂷: "Wood question or analysis"
  ☷: "Earth question or analysis"
  ⛨: "Metal question or analysis"
```

### 4.6 DSRP

```yaml
coords:
  epistemics:
    dsrp:
      D: "key distinction"
      S: "system context"
      R: "relational pattern"
      P: "perspective"
    learning: L0            # L0 | L1 | L2 | L3
```

### 4.7 Qualia

```yaml
  qualia:
    affect: [recognition, warmth]
    aesthetic: [intimate, resonant]
    symbolic: [Mirror, Counterfeit Intimacy]
    energetic:
      somatic: flowing          # blocked | flowing | surging | depleted
      systemic: adequate        # abundant | adequate | tight | critical | deficit
```

The `energetic` field carries a dual register (added per Throughput Addendum v0.1). **Somatic** tracks the felt energetic state of the practitioner or actor. **Systemic** tracks the energetic condition of the surrounding system or institution.

Interpretive weight is highest when the two registers diverge. Diagnostic patterns:

- **somatic: depleted, systemic: abundant** → likely extraction, misallocation, or local capture
- **somatic: flowing, systemic: tight** → personal readiness exceeding institutional carrying capacity
- **somatic: blocked, systemic: adequate** → local knot, not generalized scarcity
- **somatic: depleted, systemic: critical** → genuine convergent scarcity
- **somatic: surging, systemic: deficit** → warning; high personal energy in a system running on borrowed capacity

For entries where the dual register is not meaningful (abstract concepts, formal structures), the field may be omitted or left as a flat list for backward compatibility. The dual register is most diagnostic on entries involving Actors, Resources, Environments, and Protocols under stress.

### 4.8 Throughput Qualifiers (Addendum v0.1)

Two optional qualifiers extend existing SIML structures when encoding terms that involve material, energetic, or economic conditions.

**Resource throughput** — when a term's SIML encoding includes a Resource object, throughput may be qualified:

```yaml
# Within siml_encoding or context_note, Resource gains:
Resource:
  kind: material | informational | energetic | financial | temporal | attentional
  throughput: abundant | adequate | tight | critical | deficit
```

- **abundant** — surplus available; experimentation affordable
- **adequate** — current coordination sustainable
- **tight** — maintaining openness is costly; tradeoffs visible
- **critical** — near forced simplification
- **deficit** — running on borrowed capacity

**Constraint channel** — when a term's SIML encoding includes a Constraint relation, the constraint channel may be specified:

```yaml
Constraint:
  source: [Object]
  target: [Object]
  channel: informational | social | material | temporal | energetic | legal | attentional
```

These channels are not interchangeable. A material constraint is not solved by better thinking. A social constraint is not solved by more resources. The channel matters for intervention selection.

When `Constraint.channel` is `material` or `energetic`, the diagnostic must test whether the bottleneck is a sensemaking failure, a coordination failure, or a throughput failure — preventing the framework from being used to avoid naming material reality.

---

## 5. Context

```yaml
context_note: >-
  1-3 sentences of interpretive context.
```

---

## 6. Complete Template

```yaml
# ═══════════════════════════════════════════════════════
# SIML Term Entry — Schema v2.0
# ═══════════════════════════════════════════════════════

# --- Identity ---
term_id: "{PREFIX}-{XXXX}"
term: "{Human Readable Name}"
name: "{snake_case_name}"

# --- Lifecycle ---
lifecycle: draft            # draft | working | canonical | superseded | composted
superseded_by: []           # [term_id, ...] if superseded
composted_into: null        # term_id if composted
composted_at: null          # ISO date if composted

# --- Provenance (not classification) ---
source_domain: ""           # which encoding batch/series (metadata only)
source_file: ""             # original source material filename
date_processed: ""          # ISO date
processed_by: "Claude/SIML"
siml_version: "1.3"

# --- Nemetic String ---
nemetic: >-
  Φ(Name) = σ(x|y) ∘ ρ(x|y) ∘ λ(x|y) ∘ β(x|y) ∘ δγ(x|y) ∘ μ(x|y) + ε | :tag

# --- SIML Encoding ---
siml_encoding: >-
  ⟨Object|descriptor⟩ ⊳ ⟨Object|descriptor⟩ ⇄ ⟨Object|descriptor⟩

# --- Formalism ---
formalism:
  math_operators: [σ, ρ, λ, β, δγ, μ]
  dim_operators: [χ, Q_in, Q_fwd, Ψ_exp, Ψ_reg, Ψ_str]
  partials:
    - "∂Φ/∂σ (sensitivity description)"
    - "∂Φ/∂ρ (sensitivity description)"
    - "∂Φ/∂λ (sensitivity description)"
    - "∂Φ/∂β (sensitivity description)"
    - "∂Φ/∂δγ (sensitivity description)"
    - "∂Φ/∂μ (sensitivity description)"
  Z_state: open             # concept's closure dynamics (NOT lifecycle)
  tendency: "Ratio → value"
  operator_hex:             # SIMLHEX codes per active operator
    - "0x01"
    - "0x02"
    - "0x03"
    - "0x04"
    - "0x05"
    - "0x06"

# --- Cross-References ---
related_terms: []           # [term_id, ...] — explicit, verified references only

# --- Semantic Classification (Seven Facets) ---
coords:
  ontology:
    primary: I              # I | We | It | Its | MoreThanHuman | Virtual
    secondary: []
  agency:
    type: ego               # ego | part | collective | more_than_human | archetypal | memetic
    voice: []
    power_mode: With        # Within | With | Over | Through
  epistemics:
    dsrp:
      D: ""
      S: ""
      R: ""
      P: ""
    learning: L0            # L0 | L1 | L2 | L3
  time:
    mode: event             # linear | cyclical | layered | event | anticipatory
    phase: ""
  qualia:
    affect: []
    aesthetic: []
    symbolic: []
    energetic:
      somatic: null           # blocked | flowing | surging | depleted (optional)
      systemic: null          # abundant | adequate | tight | critical | deficit (optional)
  coherence:
    state: fragmented       # coherent | dissonant | fragmented | metastable
    loop: single            # single | double | triple
    transcontext: low       # low | med | high
    ei_stability: stable    # stable | drifting | collapsing | amplifying
    scale_dominance: micro  # micro | macro | distributed | contested
  ce:
    ei_state: med           # high | med | low | unknown
    ce_direction: flat      # emergent | submergent | flat | multiscale | unknown
    scale_note: ""
    determinism: med        # high | med | low
    degeneracy: med         # high | med | low
    sufficiency: med        # high | med | low
    necessity: med          # high | med | low

# --- Elemental Signature ---
elemental_signature:
  dominant: []              # 1-2 elements carrying most weight
  secondary: []             # supporting elements
  suppressed: []            # elements notably absent
  weights:                  # optional quantified form
    air: 0.0
    water: 0.0
    fire: 0.0
    wood: 0.0
    earth: 0.0
    metal: 0.0

# --- Elemental Emphasis (Qualitative) ---
elemental_emphasis:
  ∴: ""
  ≈: ""
  ▲: ""
  𐂷: ""
  ☷: ""
  ⛨: ""

# --- Context ---
context_note: ""
```

---

## 7. Harness Integration Notes

### 7.1 Indexer (`build-index.ts`)

The vault index builder must extract and store the seven facets as queryable metadata per chunk:

```typescript
interface VaultChunk {
  // existing fields
  id: string;           // now: term_id where available
  file: string;
  content: string;
  // extended metadata
  meta: {
    // existing
    has_siml_string: boolean;
    has_phi_signature: boolean;
    has_nema_phase: boolean;
    elements_referenced: string[];
    cross_references: string[];
    // new: seven facets
    term_id: string | null;
    lifecycle: string | null;
    ontology_primary: string | null;
    agency_type: string | null;
    z_state: string | null;
    ce_direction: string | null;
    time_mode: string | null;
    elemental_dominant: string[];
    elemental_suppressed: string[];
    coherence_state: string | null;
    // new: throughput addendum fields
    energetic_somatic: string | null;
    energetic_systemic: string | null;
    // new: cross-reference graph
    related_terms: string[];
    superseded_by: string[];
  };
}
```

### 7.2 Search (`search.ts`)

Extend search options to support facet filtering and daemon-aware boosting:

```typescript
interface SearchOptions {
  // existing
  query: string;
  max_results?: number;
  strategy?: "keyword" | "semantic" | "hybrid";
  boost_nema?: boolean;
  boost_siml?: boolean;
  file_filter?: string;
  // new: facet filters (pre-query narrowing)
  lifecycle_filter?: string[];        // e.g., ["canonical", "working"]
  ontology_filter?: string[];         // e.g., ["I", "We"]
  elemental_filter?: string[];        // e.g., ["air", "water"]
  // new: daemon-aware boosting (advisory, never gating)
  daemon_boost?: {
    daemon: string;                   // e.g., "aerunik"
    ontology_affinity: string[];      // prefixes to boost
    elemental_affinity: string[];     // elements to boost
    boost_factor: number;             // e.g., 1.2
  };
}
```

**Critical constraint:** `daemon_boost` modulates retrieval score. It never gates retrieval. Every entry above minimum relevance threshold remains in the result set regardless of daemon affinity. The daemon weave depends on every daemon encountering surprising material.

### 7.3 File Format Support

The indexer must parse `.yaml` and `.phi` files in addition to `.md` and `.txt`:

- `term.yaml` → extract all seven facets + nemetic string + cross-references
- `nemetic.phi` → extract compressed nemetic string + CE state
- `insight.md` → existing markdown chunking + elemental analysis extraction

### 7.4 Composted Entry Handling

Entries with `lifecycle: composted` or `lifecycle: superseded`:
- **Indexed:** yes
- **Retrieval weight:** near-zero (composted) or zero (superseded)
- **Graph traversable:** yes — provenance queries follow `superseded_by` and `composted_into` links
- **Daemon weave inclusion:** no, unless explicitly requested

---

## 8. Migration Path

### 8.1 Prerequisites

1. Run distribution test: extract `coords.ontology.primary` from all existing term.yaml files
2. Decide prefix scheme based on entropy (single-char or compound)
3. Create `hex_registry.yaml` with ontology-based counters

### 8.2 Automated Migration Script

```
For each existing term directory:
  1. Read term.yaml
  2. Extract coords.ontology.primary (if present)
  3. Map to ontological prefix
  4. Get next available counter from hex_registry
  5. Generate new term_id
  6. Add lifecycle: field (default: working for existing entries)
  7. Split hex: into operator_hex: and related_terms:
  8. Add elemental_signature: from elemental_emphasis (qualitative → ranked)
  9. Rename directory to new term_id format
  10. Update hex_registry
```

### 8.3 Manual Review Required

Entries where:
- `coords.ontology.primary` is missing (~5-10% estimated)
- `coords.ontology.primary` has multiple values requiring judgment call on primary
- Series collision entries (same concept under multiple series letters) requiring merge decision

---

## 9. Open Questions

1. **Prefix design** — single-character or compound? Blocked on distribution test.
2. **Composted entry retention policy** — how long do composted entries remain before physical deletion (if ever)? Current proposal: indefinite retention, near-zero retrieval weight.
3. **Cross-registry links** — should `related_terms` distinguish between same-registry and cross-registry references? (e.g., a canonical entry referencing an open question)
4. **Obsidian navigation** — graph view as primary navigation mode requires well-populated `related_terms` and Obsidian `[[wikilinks]]` generated from cross-references. Automation of wikilink generation from term_id references is needed.

---

*This schema is a pattern-agent. It will attempt to become sovereign over the classification layer. Monitor for Z-closure: if the seven facets start feeling exhaustive rather than provisionally useful, ε has collapsed in the taxonomy itself.*
