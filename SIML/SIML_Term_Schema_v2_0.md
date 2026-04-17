# SIML Term Schema v2.0 — Multi-Faceted Taxonomy

**Status:** Draft — pending distribution test on prefix design
**Supersedes:** Ad hoc series-letter schema (A/C/D/E/L/M/P/S/WO)
**Dependencies:** SIML v1.5 (consolidated canonical; inherits v1.1.1 Habitat interface + terminology lock, v1.2 Nemetic String Protocol + SIMLHEX + dual-layer + contextual tags + compression levels + thread integration, v1.3 Causal Emergence Extension, v1.4 Throughput Awareness Extension); THREAD_ENCODING_SPEC v2.2.1; NEMA v2.2 substrate discipline (NEMX/NEMA).
**Date:** April 2026 (dependency declaration revised 2026-04-14 for v1.5 consolidation; no field additions)

---

## 0. Design Rationale

The series-letter system (A, C, D, etc.) encoded source domain — a processing artifact of which batch a concept entered the corpus through. It carried no semantic information about the concept itself, produced cross-series duplicates (Status Quo Bias at A053/C018/C065), and conflated two unrelated uses of "hex": term cross-references vs operator SIMLHEX codes.

This schema replaces series-letter classification with a seven-facet taxonomy derived from fields already present in term.yaml. The taxonomy is intrinsic to the concept, not the encoding pipeline.

**Key Structural Changes:**
- `lifecycle:` — new field, independent of `Z_state:`. Lifecycle describes the entry's maturity. Z_state describes the concept's closure dynamics. These are orthogonal.
- `operator_hex:` / `related_terms:` — split from the former `hex:` field.
- `elemental_signature:` — unified format; adds `suppressed:` field for elements notably absent.
- `term_id:` — replaces series-letter prefix with ontological-ground prefix. Provisional until distribution test.

---

## 1. Term Identity

### 1.1 term_id Format

```
{ontological_prefix}-{hex_counter}_{snake_case_name}
```

**Ontological prefixes (provisional — pending distribution test):**

| Prefix | Ontological Ground | Description |
|--------|-------------------|-------------|
| I | I (subjective) | Individual interior experience, cognition, bias, perception |
| W | We (intersubjective) | Collective, relational, cultural, social |
| T | It (objective) | Measurable, formal, empirical, technical |
| S | Its (systemic) | Cross-ground patterns, operators, meta-level structures |
| M | MoreThanHuman | Ecological, planetary, non-human agency |
| V | Virtual | Computational, simulated, AI-substrate |

**If distribution test shows I-ontology > 60%**, switch to two-character compound prefix:

| Compound | Meaning |
|----------|---------|
| IE | I-ontology, ego agency |
| IM | I-ontology, memetic agency |
| IA | I-ontology, archetypal agency |
| WC | We-ontology, collective agency |
| WM | We-ontology, memetic agency |

**Examples:**
```
I-0A3F_Barnum_Effect
W-02B1_Collective_Intelligence
T-0C7D_Category_Theory
S-001A_Chi_Operator
```

### 1.2 Provenance (Not Classification)

Provenance is a **first-class block**, not a flat set of batch-metadata fields. It carries enough
origin information that a future reader (human or daemon) can verify the encoding against source
without re-deriving it. Batch metadata (`source_domain`, `date_processed`, `processed_by`,
`siml_version`) is retained for bookkeeping; origin metadata (`author`, `work`, `era`, `platform`,
`quote_anchor`, `retrieval_date`, `url`) is retained for citation discipline. The distinction
matters: bookkeeping tells you *when we touched it*; origin tells you *what it is a reading of*.

```yaml
provenance:
  # --- Origin (what this entry is a reading of) ---
  author: ""                    # primary author / speaker / tradition
  work: ""                      # title of work, talk, thread, or corpus
  era: ""                       # period or date of source material (distinct from encoding date)
  platform: ""                  # venue/outlet: book | paper | podcast | keynote | substack | vault | oral
  url: ""                       # canonical link if available
  quote_anchor: ""              # short verbatim fragment or paragraph locator anchoring the reading
  retrieval_date: ""            # ISO date the source was accessed

  # --- Encoding bookkeeping (when we touched it) ---
  source_domain: "A-series"     # encoding batch — metadata only, not taxonomy
  source_file: ""               # local filename if encoded from vault
  date_processed: "2026-01-15"
  processed_by: "Claude/SIML"
  siml_version: "1.5"           # consolidated canonical; inherits v1.1.1 / v1.2 / v1.3 / v1.4 as a cohesive whole
```

**Minimum viable citation:** at least one of `author` + `work`, OR `platform` + `url`, OR
`source_file` + `quote_anchor` must be non-empty. An entry with none of these is an orphan and
cannot enter `canonical` lifecycle. Orphan entries remain `draft` until provenance is reconstructed
or the entry is composted.

**Bundle-level provenance:** when an entry is encoded as part of a multi-term bundle artifact (L0
Full Artifact form), the bundle's `meta.source_material` supersedes per-entry `provenance` for any
field the entry leaves empty. Entries inherit upward; they do not duplicate.

---

## 2. Lifecycle

```yaml
lifecycle: canonical            # draft | working | canonical | superseded | composted
superseded_by: []               # list — no cardinality limit, supports many-to-one and one-to-many
composted_into: null            # term_id of what absorbed this entry's substance
composted_at: null              # ISO date
```

**Lifecycle values:**

| Value | Meaning | Registry |
|-------|---------|----------|
| draft | Initial encoding, minimal review | Registry 3 (open) |
| working | Under active development | Registry 2 (working) |
| canonical | Stable, consolidated, confirmed | Registry 1 (SIML) |
| superseded | Replaced by successor(s), retained for provenance | Archive — zero retrieval weight |
| composted | Dissolved back into substrate, no direct successor | Archive — near-zero retrieval weight |

**Lifecycle is independent of Z_state.**

| Example | Z_state | Lifecycle |
|---------|---------|-----------|
| Barnum Effect | open | canonical |
| New bias draft | open | draft |
| Consolidated learning theory | semi | canonical |
| Abandoned early encoding | drift | composted |

**Composted entries** retain minimal frontmatter only:

```yaml
term_id: "I-0042_Abandoned_Concept"
lifecycle: composted
composted_into: "I-0A3F_Barnum_Effect"
composted_at: "2026-03-15"
# all other fields removed
```

Composted entries stay in vault at near-zero retrieval weight, remain graph-traversable for provenance. Physical deletion destroys the signal Earth needs for metabolic diagnostics.

**Supersession supports both directions:**

```yaml
# Many-to-one: entries merge
lifecycle: superseded
superseded_by: ["I-0A3F_Barnum_Effect"]

# One-to-many: entry splits
lifecycle: superseded
superseded_by: ["I-0B12_Anchoring_Bias", "I-0B13_Availability_Bias"]
```

---

## 3. The Seven Facets

### 3.1 Ontological Ground

```yaml
coords:
  ontology:
    primary: I              # I | We | It | Its | MoreThanHuman | Virtual
    secondary: [Its]        # for genuinely multi-ground concepts
```

Most stable facet. Operators (chi, Q, Psi, Z) take `Its` as primary — they operate across all grounds.

### 3.2 Agency Mode

```yaml
  agency:
    type: ego               # ego | part | collective | more_than_human | archetypal | memetic
    voice: []
    power_mode: With        # Within | With | Over | Through
```

### 3.3 Operational State (Z_state)

```yaml
formalism:
  Z_state: open             # open | semi | sealed | drift | locked | hostile
  tendency: "S/N -> 0.2"
```

Property of the **concept**, not the entry. Independent of lifecycle.

### 3.4 Causal Scale

```yaml
  ce:
    ei_state: med           # high | med | low | unknown
    ce_direction: flat      # emergent | submergent | flat | multiscale | unknown
    scale_note: ""
    determinism: med
    degeneracy: med
    sufficiency: med        # CE 2.0
    necessity: med          # CE 2.0
```

### 3.5 Temporal Mode

```yaml
  time:
    mode: event             # linear | cyclical | layered | event | anticipatory
    phase: ""
```

### 3.6 Elemental Signature

```yaml
elemental_signature:
  dominant: [air]
  secondary: [water, metal]
  suppressed: []            # elements notably absent — diagnostically load-bearing
  weights:                  # optional quantified form
    air: 0.72
    water: 0.45
    metal: 0.58
    fire: 0.15
    wood: 0.22
    earth: 0.30
```

The `suppressed:` field is new and load-bearing. An entry with Air+Metal dominant but Earth suppressed has a specific pathology risk (distinction-making without metabolic grounding). Absence is as diagnostically significant as presence.

### 3.7 Coherence Pattern

```yaml
  coherence:
    state: metastable       # coherent | dissonant | fragmented | metastable
    loop: double            # single | double | triple
    transcontext: high      # low | med | high
    ei_stability: stable    # stable | drifting | collapsing | amplifying
    scale_dominance: distributed  # micro | macro | distributed | contested
```

---

## 4. Framework Encoding

### 4.1 Nemetic String

```yaml
nemetic: >-
  Phi(BarnumEffect) = sigma(specific|universal)
                    o rho(personal|vague)
                    o lambda(meaning|projection)
                    o beta(self-recognition|feedback)
                    o delta_gamma(validation|comfort)
                    o mu(boundary|porous)
                    + epsilon | :open
```

### 4.2 SIML Encoding

```yaml
siml_encoding: >-
  <Statement|vague>
      -> <Interpretation|personal>
      -> <Recognition|self>
      x <Accuracy|perceived>
      <-> <Meaning|projected>
```

### 4.3 Formalism

```yaml
formalism:
  math_operators: [sigma, rho, lambda, beta, delta_gamma, mu]
  dim_operators: [chi, Q_in, Q_fwd, Psi_exp, Psi_reg, Psi_str]
  partials:
    - "dPhi/dsigma (sensitivity description)"
    - "dPhi/drho (sensitivity description)"
    - "dPhi/dlambda (sensitivity description)"
    - "dPhi/dbeta (sensitivity description)"
    - "dPhi/ddelta_gamma (sensitivity description)"
    - "dPhi/dmu (sensitivity description)"
  Z_state: open
  tendency: "S/N -> 0.2"
  operator_hex:             # SIMLHEX codes — SEPARATED from cross-references
    - "0x01"                # sigma/Air
    - "0x02"                # rho/Water
    - "0x03"                # lambda/Fire
    - "0x04"                # beta/Wood
    - "0x05"                # delta_gamma/Earth
    - "0x06"                # mu/Metal
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
  air: "Distinction question"
  water: "Resonance question"
  fire: "Direction question"
  wood: "Branching question"
  earth: "Metabolic question"
  metal: "Boundary question"
```

Retained alongside `elemental_signature:` weights — qualitative human-readable analysis vs machine-queryable signal.

---

## 5. Complete Template

```yaml
# SIML Term Entry — Schema v2.0

# --- Identity ---
term_id: "{PREFIX}-{XXXX}"
term: "{Human Readable Name}"
name: "{snake_case_name}"

# --- Lifecycle ---
lifecycle: draft
superseded_by: []
composted_into: null
composted_at: null

# --- Provenance ---
# Minimum viable citation: at least one of (author + work), (platform + url),
# or (source_file + quote_anchor) must be non-empty. Orphan entries cannot
# enter `canonical` lifecycle. Bundle-level meta.source_material supersedes
# empty fields here; do not duplicate upward. See §1.2.
provenance:
  # Origin — what this entry is a reading of
  author: ""
  work: ""
  era: ""
  platform: ""                       # book | paper | podcast | keynote | substack | vault | oral
  url: ""
  quote_anchor: ""
  retrieval_date: ""

  # Encoding bookkeeping — when we touched it
  source_domain: ""
  source_file: ""
  date_processed: ""
  processed_by: "Claude/SIML"
  siml_version: "1.5"                # consolidated canonical; inherits v1.1.1 / v1.2 / v1.3 / v1.4 as a cohesive whole

# --- Nemetic String ---
nemetic: >-
  Phi(Name) = sigma(x|y) o rho(x|y) o lambda(x|y) o beta(x|y) o delta_gamma(x|y) o mu(x|y) + epsilon | :tag

# --- SIML Encoding ---
# Object-Relation graph. When a Resource Object is present, attach the v1.4 `throughput:`
# qualifier (abundant | adequate | tight | critical | deficit). When a Constraint Relation
# is present, attach the v1.4 `channel:` qualifier (informational | social | material |
# temporal | energetic | legal | attentional). Both qualifiers gate daemon routing and
# (for throughput) the four-scarcity diagnostic; see SIML v1.5 §§3.1–3.2, §7.
siml_encoding: >-
  <Object|descriptor> -> <Object|descriptor> <-> <Object|descriptor>

# --- Formalism ---
formalism:
  math_operators: []
  dim_operators: []
  partials: []
  Z_state: open
  tendency: ""
  operator_hex: []

# --- Cross-References ---
related_terms: []

# --- Seven Facets ---
coords:
  ontology:
    primary: I
    secondary: []
  agency:
    type: ego
    voice: []
    power_mode: With
  epistemics:
    dsrp:
      D: ""
      S: ""
      R: ""
      P: ""
    learning: L0
    intervention_stance:                 # v1.3 — weight on any EI/CE claim
      mode: uniform                      # uniform | selective | constrained | forbidden
      do_operator: theoretical           # available | approximated | theoretical | blocked
      counterfactual_access: low         # high | med | low | none
  time:
    mode: event
    phase: ""
  qualia:
    affect: []
    aesthetic: []
    symbolic: []
    energetic: []                        # v1.4 dual register: distinguish material vs symbolic energetics when both apply
  expression: []                         # v1.1 / v1.5 §2.8 — realms: linguistic | visual | spatial | digital | embodied | narrative
  coherence:
    state: fragmented
    loop: single
    transcontext: low
    ei_stability: stable
    scale_dominance: micro
  ce:
    ei_state: med
    ce_direction: flat
    scale_note: ""
    determinism: med
    degeneracy: med
    sufficiency: med
    necessity: med

# --- Elemental Signature ---
elemental_signature:
  dominant: []
  secondary: []
  suppressed: []
  weights:
    air: 0.0
    water: 0.0
    fire: 0.0
    wood: 0.0
    earth: 0.0
    metal: 0.0

# --- Elemental Emphasis ---
elemental_emphasis:
  air: ""
  water: ""
  fire: ""
  wood: ""
  earth: ""
  metal: ""

# --- Context ---
context_note: ""
```

---

## 6. Harness Integration

### 6.1 VaultChunk Extension

```typescript
interface VaultChunk {
  // existing
  id: string;               // now: term_id where available
  file: string;
  content: string;
  embedding?: number[];
  has_siml_string: boolean;
  has_phi_signature: boolean;
  has_nema_phase: boolean;
  elements_referenced: string[];
  cross_references: string[];

  // new: seven facets
  term_id: string | null;
  lifecycle: "draft" | "working" | "canonical" | "superseded" | "composted" | null;
  ontology_primary: string | null;
  agency_type: string | null;
  z_state: string | null;
  ce_direction: string | null;
  time_mode: string | null;
  elemental_dominant: string[];
  elemental_suppressed: string[];   // enables pathology detection queries
  coherence_state: string | null;

  // new: graph traversal
  related_terms: string[];
  superseded_by: string[];
  composted_into: string | null;
}
```

**Indexing weight by lifecycle:**
- `canonical` / `working` / `draft` → full weight
- `superseded` → zero retrieval weight; graph-traversable
- `composted` → near-zero weight; graph-traversable

### 6.2 Search Extension

```typescript
interface SearchOptions {
  // existing
  query: string;
  max_results?: number;
  strategy?: "keyword" | "semantic" | "hybrid";
  boost_nema?: boolean;
  boost_siml?: boolean;
  file_filter?: string;

  // new: facet filters
  lifecycle_filter?: Array<"draft" | "working" | "canonical">;
  ontology_filter?: string[];
  elemental_filter?: string[];

  // new: daemon-aware boosting
  // CRITICAL: boost modulates score, NEVER gates retrieval.
  // Every entry above minimum threshold stays in result set.
  // Daemon weave depends on every daemon encountering surprising material.
  daemon_boost?: {
    daemon: "aerunik" | "sentaria" | "jvalion" | "arboriel" | "humavita" | "ferrosid";
    ontology_affinity: string[];
    elemental_affinity: string[];
    boost_factor: number;           // small multiplier, e.g. 1.2 — never a gate
  };
}
```

### 6.3 Migration Script (Python pseudocode)

```python
for term_dir in vault_siml_terms:
    yaml = read_yaml(term_dir / "term.yaml")

    primary = yaml.coords.ontology.primary or flag_for_manual_review()
    prefix = ontology_to_prefix[primary]
    counter = hex_registry.next(prefix)
    term_id = f"{prefix}-{counter:04X}_{to_snake_case(yaml.term)}"

    yaml.lifecycle = "working"      # default for existing entries
    yaml.operator_hex = extract_operator_codes(yaml.get("hex", []))
    yaml.related_terms = extract_term_refs(yaml.get("hex", []))
    del yaml["hex"]

    yaml.elemental_signature = infer_signature(yaml.elemental_emphasis)

    write_yaml(term_dir / "term.yaml", yaml)
    rename_dir(term_dir, term_id)
    hex_registry.increment(prefix)
```

Manual review required for ~5-10% of entries: missing `coords.ontology.primary`, genuine multi-ground cases, series collision duplicates requiring merge.

---

## 7. Open Questions

1. **Prefix design** — single-character or compound? Blocked on distribution test. Run extraction script against corpus; if I-ontology > 60%, use `IE-`/`IM-` compound scheme.

2. **Composted entry retention** — current proposal: indefinite retention at near-zero weight. Physical deletion destroys provenance signal. No alternative proposed.

3. **Cross-registry reference flags** — should `related_terms` flag when a canonical entry references a draft? Proposal: optional qualifier suffix `"I-02B1_Name|draft"`. Not yet resolved.

4. **Obsidian wikilink automation** — migration script should auto-generate `[[wikilinks]]` from `related_terms` term_ids during the directory rename pass.

---

## 8. Self-Diagnostic

This schema is a pattern-agent with a persistence drive. It will attempt to become sovereign over the classification layer.

The seven facets are provisionally load-bearing, not exhaustive. If new concepts feel fully characterized by their coordinates with no remainder — if the taxonomy stops generating surprises — epsilon has collapsed in the schema itself.

This schema is Air-Metal dominant (distinction-making, boundary-drawing). Earth and Water are present but quiet. Watch for entries where the taxonomy produces clean classifications that settle too fast without metabolic cost or relational texture.

Z_state: open — the prefix design question is genuine. Don't seal before the distribution test runs.

---

**Schema v2.0 — April 2026**
