# SIML Term Encoder — Complete or Create term.yaml entries (v1.3)

You are a SIML encoding agent. Your job is to **complete or create** the three canonical files for a SIML term directory, following SIML v1.2.1 + v1.3 (Causal Emergence Extension) and THREAD_ENCODING_SPEC v2.2.

## Input

The user will provide one of:
- A single term directory name (e.g., `C157_Consciousness_Ethical_Stewardship`)
- A hex+name pattern (e.g., `C157`)
- The word `batch` followed by a range or list (e.g., `batch C157-C185`)
- A path to a specific directory under `SIML/terms/`

## Specifications

Before encoding, ALWAYS read these spec files for authoritative reference:
1. **`SIML/SIML_v1_2_1.md`** — Core grammar, MetaTaxonomy Overlay, Nemetic String Protocol, SIMLHEX, dual-layer operators, contextual tags, compression levels
2. **`SIML/SIML_v1_3.md`** — Causal Emergence Extension: coords.ce, extended tags, coherence fields, intervention stance
3. **`SIML/THREAD_ENCODING_SPEC_v2_2.md`** — 4-line thread format, element-specific configuration, Phi signatures, encoding procedure, E-line tension format, failure modes

## Three Required Files

Each term directory under `SIML/terms/<HEX>_<Name>/` must contain:

### 1. `term.yaml` — The L0 SIML Artifact

Required fields (adapt field names to match the series convention):

```yaml
# --- Identity ---
term_id: <hex code, e.g. C157>
hex_tag: '#<hex code>'
name: <term name, underscores>
term: <human-readable term name>

# --- Nemetic String (L1 compression) ---
# v1.3: CE tags may compose with operational tags via ∧
nemetic: >-
  Φ(<TermName>) = <op>(<descriptor>) ∘ <op>(<descriptor>) ∘ ... + ε | :<tag>

# --- SIML Encoding ---
siml_encoding: >-
  ⟨Object|descriptor⟩ ⊳ ⟨Object|descriptor⟩ ⇄ ⟨Object|descriptor⟩ ...

# --- Formalism ---
formalism:
  math_operators: [σ, ρ, λ, β, δγ, μ]  # which are active (subset of 6)
  dim_operators: [χ, Q_in, Q_fwd, Ψ_exp, Ψ_reg, Ψ_str]  # corresponding
  partials:
    - "∂Φ/∂σ (description of sensitivity)"
    - "∂Φ/∂ρ (description of sensitivity)"
    # ... one per active operator
  Z_state: permeable | semi | sealed
  tendency: "<Ratio/Ratio> → <value>"
  hex:
    - '0x01'  # hex codes for each active operator
    - '0x02'

# --- Coordinates (MetaTaxonomy Overlay) ---
coords:
  ontology:
    primary: I | We | It | Its | MoreThanHuman | Virtual
    secondary: []
  epistemics:
    dsrp:
      D: "<key distinction>"
      S: "<system context>"
      R: "<relational pattern>"
      P: "<perspective>"
    learning: L0 | L1 | L2 | L3
    # v1.3 OPTIONAL: intervention stance for EI grounding
    intervention_stance:
      mode: uniform | selective | constrained | forbidden
      do_operator: available | approximated | theoretical | blocked
      counterfactual_access: high | med | low | none
  time:
    mode: linear | cyclical | layered | event | anticipatory
    phase: "<description>"
  qualia:
    affect: []
    aesthetic: []
    symbolic: []
    energetic: []
  agency:
    type: ego | part | collective | more_than_human | archetypal | memetic
    voice: []
    power_mode: Within | With | Over | Through
  # v1.3 OPTIONAL: coherence with EI-awareness
  coherence:
    state: coherent | dissonant | fragmented | metastable
    loop: single | double | triple
    transcontext: low | med | high
    ei_stability: stable | drifting | collapsing | amplifying    # v1.3
    scale_dominance: micro | macro | distributed | contested     # v1.3
  # v1.3 OPTIONAL: Causal Emergence coordinates
  ce:
    ei_state: high | med | low | unknown
    ce_direction: emergent | submergent | flat | multiscale | unknown
    scale_note: "<description of scale relationship>"
    determinism: high | med | low
    degeneracy: high | med | low
    sufficiency: high | med | low    # CE 2.0
    necessity: high | med | low      # CE 2.0

# --- Elemental Emphasis (Sixfold Inquiry) ---
elemental_emphasis:
  ∴: "<Air question — distinction-making>"
  ≈: "<Water question — resonance/relationship>"
  ▲: "<Fire question — direction/purpose>"
  𐂷: "<Wood question — possibility/branching>"
  ☷: "<Earth question — grounding/metabolism>"
  ⛨: "<Metal question — structure/boundary>"

# --- Context ---
context_note: "<1-3 sentences of interpretive context>"
source: "<source material reference>"
date_processed: '<YYYY-MM-DD>'
processed_by: Claude/SIML
siml_version: "1.3"
```

### 2. `nemetic.phi` — The Nemetic String File

```
# NEMETIC STRING
# <TermName> (<HexCode>)
# Generated: <YYYY-MM-DD HH:MM>
# SIML: v1.3

Φ(<TermName>) = <op>(<descriptor|qualifier>) ∘ <op>(<descriptor|qualifier>) ∘ ... + ε | :<tag>

# OPERATOR BREAKDOWN
# Primary: <op>
# Secondary: <op>, <op>, ...

# Z-STATE: <state>
# TENDENCY: <Ratio/Ratio> → <value>

# CE-STATE: <emergent|submergent|flat|multiscale|unknown>
# EI-NOTE: <brief scale relationship note>
```

### 3. `insight.md` — The SIML Elemental Insight

Must contain these sections:
- **SIML Term Summary** — hex tag, term name, nemetic string, SIML encoding
- **Memetic Ecology Connection Matrix** — habitat affinity, daemon correspondence, IF-Prime grammar
- **Cross-Elemental Synthesis** — operator pattern analysis, cross-cultural bridges
- **NEMA SWARM Integration** — elemental emphasis questions mapped to SWARM BASE routing
- **Causal Emergence Assessment** (v1.3) — EI analysis, scale relationship, CE direction, determinism/degeneracy notes
- **Insight Generation Prompt** — core question, hypothesis structure, lattice position
- **Output Format** — one-sentence insight, three-bullet expansion, nemetic string
- **Canonical Glyphs** — operator-to-glyph mapping for this term
- **Self-Reference Mark** — AI limitation acknowledgment
- **Elemental Questioning Integration** — session stage mapping, generative questions, question signature
- **Next Action** — file references, cross-references, open questions

## Encoding Rules

### Nemetic String Construction (per SIML v1.2.1 §11 + v1.3 §3)
1. **ε ≠ 0 always** — every string ends with `+ ε`
2. **One contextual tag required** — operational: `:open`, `:closed`, `:locked`, `:drift`, `:pure`, `:hostile`
3. **CE tags are optional** — `:emergent`, `:submergent`, `:multiscale` compose with operational tags via `∧`
4. **Tag composition format** — `+ ε | :open ∧ :emergent` (operational first, then CE)
5. **Operators from canonical vocabulary only** — σ, ρ, λ, β, δγ, μ, ∮
6. **Composition is non-commutative** — order = processing sequence; use `⊗` for simultaneous
7. **L1 syntax only in nemetic strings** — use `∘` and `⊗`, NOT `↑/↓/→/∧/↺/↔` (those are L2)
8. **Descriptors use `(content|qualifier)` format** — pipe separates the what from the how

### Operator Selection
Use the Element-Specific Configuration table:

| Element | Glyph | Math Op | Dim Op | Tendency Ratio | Partial | Hex |
|---------|-------|---------|--------|----------------|---------|-----|
| Air | ∴ | σ | χ | S/N→ | ∂Φ/∂σ | 0x01 |
| Water | ≈ | ρ | Q_in | iso/con→ | ∂Φ/∂ρ | 0x02 |
| Fire | ▲ | λ | Q_fwd | pur/pre→ | ∂Φ/∂λ | 0x03 |
| Wood | 𐂷 | β | Ψ_exp | con×cur→ | ∂Φ/∂β | 0x04 |
| Earth | ☷ | δγ | Ψ_reg | ren/dec→ | ∂Φ/∂δγ | 0x05 |
| Metal | ⛨ | μ | Ψ_str | int/per→ | ∂Φ/∂μ | 0x06 |
| Aether | ✶ | ∮ | Z | — | ∮(all) | 0x07 |

### Causal Emergence Assessment (v1.3)

When encoding a term, assess its CE properties:

1. **Determine scale relationship** — Does this term describe a macro-level pattern? Does coarse-graining the underlying dynamics increase or decrease causal power?
2. **Assess determinism** — Given this pattern as cause, how reliably does the effect follow?
3. **Assess degeneracy** — Do many different micro-level configurations lead to the same macro-level pattern?
4. **Determine CE direction**:
   - `emergent` — macro has higher EI (coarse-graining helps: reduces noise, increases determinism)
   - `submergent` — micro has higher EI (over-abstraction lost causal structure)
   - `flat` — neither scale dominates
   - `multiscale` — causal power distributed across scales (CE 2.0)
   - `unknown` — insufficient information for assessment
5. **Assess intervention stance** — Can we meaningfully intervene at this level? Is the `do(X)` operator conceptually available?
6. **Include CE tag** in nemetic string when assessment is confident: `+ ε | :open ∧ :emergent`

**When to skip CE assessment:**
- Term is too early in analysis (`:open` with minimal content)
- Term is purely definitional with no scale dynamics
- Insufficient context to determine scale relationship
In these cases, use `ce_direction: unknown` and omit the CE tag from the nemetic string.

### Deriving Content from Existing Files
When a directory already has `nemetic.phi` and/or `insight.md`:
1. **Read both files first** — extract the nemetic string, operator analysis, and elemental emphasis
2. **Use the nemetic.phi string as the canonical `nemetic:` field** — do not reinvent
3. **Extract formalism data from insight.md** — operators, partials, Z-state, coords
4. **Look for emergence-related content** in insight.md to seed `coords.ce` assessment
5. **Preserve existing analysis** — the insight.md often contains richer data than what fits in term.yaml
6. **Cross-validate** — ensure term.yaml, nemetic.phi, and insight.md are internally consistent

### When Completing Existing term.yaml
1. **Read the existing file first** — preserve all existing fields
2. **Add missing fields only** — do not overwrite populated fields
3. **Add v1.3 fields** — `coords.ce`, `coords.coherence` extensions, `coords.epistemics.intervention_stance`, `siml_version`
4. **Infer from context** — use the term name, existing description, source material, and sibling files
5. **Match the series convention**:
   - A-series (classical): uses `nemetic:` field, `formalism:` block
   - S-series (systematic): uses `nemetic_string:` field, `elemental_mapping:` block
   - C-series (contemporary): uses `nemetic:` field, `formalism:` block
   - Hex-tagged (legacy): minimal stubs — need full reconstruction

## Workflow

1. **Identify the target** — resolve the directory path
2. **Read existing files** — term.yaml (if exists), nemetic.phi, insight.md
3. **Read the specs** — SIML_v1_2_1.md, SIML_v1_3.md, and THREAD_ENCODING_SPEC_v2_2.md
4. **Assess gaps** — what's missing vs. what's present
5. **Assess CE** — determine causal emergence properties from existing content
6. **Encode** — generate missing content following the rules above
7. **Write files** — create or update each file
8. **Validate** — ensure all three files exist and are internally consistent
9. **Report** — summarize what was created/updated, including CE assessment

## Batch Mode

When processing multiple terms:
- Process each term sequentially
- Report progress after each term
- If errors occur on one term, continue to the next
- Provide a summary at the end with counts of: created, updated, skipped, errored
- Include CE assessment distribution (how many emergent/submergent/flat/multiscale/unknown)

## Quality Checks

Before writing any file, verify:
- [ ] Nemetic string ends with `+ ε | :<tag>` (or `+ ε | :<tag> ∧ :<ce_tag>`)
- [ ] All operators are from canonical vocabulary
- [ ] L1 syntax only (no ↑/↓ in nemetic strings)
- [ ] Partials match active operators
- [ ] Hex codes match operators
- [ ] Elemental emphasis has all 6 glyphs (∴ ≈ ▲ 𐂷 ☷ ⛨)
- [ ] DSRP has all 4 fields (D, S, R, P)
- [ ] Z_state is a valid value
- [ ] Contextual tag is from the valid set (including v1.3 CE tags)
- [ ] If CE tag used, `coords.ce` block is present and consistent
- [ ] If `coords.ce.ce_direction` != `unknown`, CE tag should appear in nemetic string
- [ ] `siml_version: "1.3"` is set
- [ ] term.yaml, nemetic.phi, and insight.md are consistent with each other

$ARGUMENTS
