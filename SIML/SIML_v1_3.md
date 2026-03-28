# SIML v1.3 — Causal Emergence Extension
**Effective Information & Multi-Scale Causal Analysis**

---

## 0. Purpose of This Extension

SIML v1.3 integrates Erik Hoel's Effective Information (EI) and Causal Emergence (CE) frameworks into the existing SIML grammar. It provides SIML with a **rigorous test for when compression is causally productive versus degenerative**.

The Nemetic string's `+ ε` always acknowledged incompleteness. EI/CE now quantifies **which incompletenesses are generative** (multiple realizability enabling error correction) versus **which are pathological** (degeneracy swamping signal, indeterminism destroying predictability).

**v1.3 is fully backward-compatible.** All v1.2.1 artifacts remain valid. All new fields are optional. No existing entry requires modification.

**Dependencies:**
- SIML v1.2.1 (prerequisite — this document extends, does not replace)
- THREAD_ENCODING_SPEC v2.2 (thread integration section extends v2.2 fields)
- Erik Hoel, "Quantifying causal emergence shows that macro can beat micro" (2013)
- Erik Hoel, "The Emergence of Informative Higher Scales in Complex Networks" (2020)
- Comolatti & Hoel, "Causal Emergence 2.0" (2022) — sufficiency/necessity primitives

---

## 1. Theoretical Foundation

### 1.1 Effective Information (EI)

EI measures causal strength under uniform intervention. For a system with transition probability matrix (TPM):

```
EI(TPM) = MI(do(U) → Y)
```

Where `do(U)` is a uniform intervention across all possible states and `MI` is mutual information between intervention and effect. EI captures how **deterministic** and **non-degenerate** a system's causal structure is:

- **Determinism**: Given a cause, how reliably does the effect follow? (Low noise)
- **Degeneracy**: Do different causes lead to different effects? (Low many-to-one collapse)

High EI = high determinism + low degeneracy = strong causal structure.

### 1.2 Causal Emergence (CE)

CE occurs when a coarse-grained (macro) description has higher EI than the fine-grained (micro) description:

```
CE = EI_macro - EI_micro
```

- **CE > 0**: The macroscale is causally superior — coarse-graining *increased* determinism and reduced degeneracy. The macro description isn't just convenient; it's **causally more informative**.
- **CE < 0**: Over-compression — the macro lost causal structure. Fine-grained description carries more causal power.
- **CE ≈ 0**: Flat — neither scale dominates.

### 1.3 CE 2.0: Sufficiency and Necessity

Comolatti & Hoel decompose causal power into:

- **Sufficiency**: How reliably does the cause produce the effect? (Forward reliability)
- **Necessity**: How much does the effect depend on this specific cause? (Backward specificity)

CE 2.0 further introduces **multiscale entropy** — the distribution of causal gains across multiple scales, not just macro vs. micro.

### 1.4 Why This Matters for SIML

SIML's compression stack (L0→L4) already acknowledges that artifacts exist at multiple description levels. EI/CE provides the missing **causal warrant** for compression choices:

- When does a Nemetic string (L1) carry more causal power than the full artifact (L0)?
- When does a thread encoding (L2) lose essential causal structure?
- When is a hex reference (L3) sufficient because the macro pattern is causally dominant?

The answer isn't "always compress" or "always expand" — it's **compress when CE > 0, expand when CE < 0**.

---

## 2. New Coordinate Block: `coords.ce`

### 2.1 Specification

```yaml
coords:
  ce:  # Causal Emergence coordinates — NEW in v1.3
    ei_state: high | med | low | unknown     # qualitative EI assessment
    ce_direction: emergent | submergent | flat | multiscale | unknown
    scale_note: "description of scale relationship"
    determinism: high | med | low             # forward transition reliability
    degeneracy: high | med | low              # many-to-one mapping degree
    sufficiency: high | med | low             # CE 2.0: cause→effect reliability
    necessity: high | med | low               # CE 2.0: effect←cause specificity
```

### 2.2 Field Definitions

| Field | Type | Description |
|-------|------|-------------|
| `ei_state` | enum | Qualitative assessment of Effective Information at this artifact's description level |
| `ce_direction` | enum | Whether coarse-graining increases (`emergent`) or decreases (`submergent`) causal power |
| `scale_note` | string | Free-text description of the scale relationship (e.g., "individual→collective accountability has higher EI than tracking individual acts") |
| `determinism` | enum | How reliably forward transitions occur at this level |
| `degeneracy` | enum | Degree of many-to-one cause-effect mapping (high = many causes → same effect) |
| `sufficiency` | enum | CE 2.0: How reliably this cause produces its effect |
| `necessity` | enum | CE 2.0: How specifically the effect depends on this cause |

### 2.3 Binding Rules

- `coords.ce` binds primarily to **Frame**, **Protocol**, and **Outcome** objects — these are the objects where scale choice matters most.
- `coords.ce` may bind secondarily to **Boundary** objects when the boundary itself constitutes a coarse-graining operation.
- Artifacts in early exploration (`+ ε | :open`) may leave `ce_direction: unknown` — EI assessment requires sufficient structural analysis.
- `coords.ce` **never prescribes** which scale to use. It **diagnoses** causal informativeness. Scale selection remains with ✶ NEMA.

### 2.4 Examples

**Term with emergent CE:**
```yaml
# accountability — macro-level accountability has higher EI than tracking individual acts
coords:
  ce:
    ei_state: high
    ce_direction: emergent
    scale_note: "collective accountability structures reduce degeneracy vs individual act-tracking"
    determinism: high
    degeneracy: low
    sufficiency: high
    necessity: med
```

**Term with submergent CE:**
```yaml
# bureaucratic_capture — over-compression destroyed causal structure
coords:
  ce:
    ei_state: low
    ce_direction: submergent
    scale_note: "institutional abstraction increased degeneracy; micro-level interactions carry more causal power"
    determinism: low
    degeneracy: high
    sufficiency: low
    necessity: low
```

**Term with multiscale CE:**
```yaml
# consciousness — causal power distributed across neural, cognitive, and social scales
coords:
  ce:
    ei_state: med
    ce_direction: multiscale
    scale_note: "CE 2.0 analysis shows causal gains at multiple scales; no single level dominates"
    determinism: med
    degeneracy: med
    sufficiency: med
    necessity: med
```

---

## 3. Extended Contextual Tags

### 3.1 New Tags (v1.3)

| Tag | Meaning | EI Condition | When to Apply |
|-----|---------|--------------|---------------|
| `:emergent` | Macroscale causally superior | CE > 0, EI_macro > EI_micro | Coarse-graining increases causal power |
| `:submergent` | Microscale causally superior | CE < 0, over-compression | Further abstraction collapses EI |
| `:multiscale` | Causation distributed across scales | High multiscale entropy (CE 2.0) | No single scale dominates |

### 3.2 Relationship to Existing Tags

The new tags **do not replace** existing tags (`:open`, `:closed`, `:locked`, `:drift`, `:pure`, `:hostile`). They occupy a different axis:

- **Existing tags** describe **operational state** — is the artifact open to revision, committed, drifting, etc.
- **CE tags** describe **causal informativeness** — at what scale does the artifact carry causal power.

An artifact can be `:open` AND `:emergent` — revisable but causally productive at macro scale.

### 3.3 Tag Composition

When both an operational tag and a CE tag apply, they compose with `∧`:

```
+ ε | :open ∧ :emergent
+ ε | :locked ∧ :submergent
+ ε | :drift ∧ :multiscale
```

**If only one tag is known**, use the known one alone. CE tags are never required. An artifact with `+ ε | :open` (no CE tag) is valid — it simply hasn't been assessed for causal emergence.

### 3.4 Tag Transition Rules (CE-specific)

- `:open` → `:emergent` when coarse-graining analysis shows CE > 0
- `:emergent` → `:submergent` when further compression collapses EI
- `:emergent` → `:multiscale` when CE 2.0 analysis shows distributed causation
- `:submergent` → `:emergent` when scale is adjusted (decompressed to optimal level)
- `:locked` can carry any CE state — commitment doesn't require optimality
- CE tags may transition independently of operational tags

---

## 4. Extended `coords.coherence`

### 4.1 New Fields

```yaml
coherence:
  state: coherent | dissonant | fragmented | metastable  # UNCHANGED
  loop: single | double | triple                          # UNCHANGED
  transcontext: low | med | high                          # UNCHANGED
  ei_stability: stable | drifting | collapsing | amplifying  # NEW in v1.3
  scale_dominance: micro | macro | distributed | contested   # NEW in v1.3
```

### 4.2 New Field Definitions

| Field | Type | Description |
|-------|------|-------------|
| `ei_stability` | enum | How stable is the EI assessment over time/sessions |
| `scale_dominance` | enum | Which scale currently carries the most causal power |

- `ei_stability: stable` — EI holds across sessions; the compression level is reliable
- `ei_stability: drifting` — EI shifting; the optimal scale may be changing
- `ei_stability: collapsing` — EI declining at current scale; decompression may be needed
- `ei_stability: amplifying` — EI increasing; the current compression is becoming more causally productive

- `scale_dominance: micro` — fine-grained description dominates (CE < 0)
- `scale_dominance: macro` — coarse-grained description dominates (CE > 0)
- `scale_dominance: distributed` — multiple scales carry causal power (CE 2.0)
- `scale_dominance: contested` — unclear which scale dominates; under investigation

### 4.3 Relationship to `coords.ce`

`coords.coherence` and `coords.ce` are complementary but distinct:

- `coords.ce` provides the **diagnostic assessment** — what is the EI, what direction is CE?
- `coords.coherence.ei_stability` and `.scale_dominance` provide the **temporal and relational** view — how stable is the assessment, and how does it relate to system-level coordination?

---

## 5. Extended `coords.epistemics`

### 5.1 New Field: `intervention_stance`

```yaml
epistemics:
  dsrp: {...}                                  # UNCHANGED
  learning: L0 | L1 | L2 | L3                 # UNCHANGED
  parts: [...]                                 # UNCHANGED
  dreaming: low | med | high                   # UNCHANGED
  intervention_stance:                         # NEW in v1.3
    mode: uniform | selective | constrained | forbidden
    do_operator: available | approximated | theoretical | blocked
    counterfactual_access: high | med | low | none
```

### 5.2 Field Definitions

| Field | Type | Description |
|-------|------|-------------|
| `mode` | enum | How intervention is modeled for this artifact |
| `do_operator` | enum | Whether the `do(X)` operator (Pearl's causal calculus) is available |
| `counterfactual_access` | enum | Can we reason about alternative outcomes? |

**Rationale:** Hoel's EI is defined under **uniform intervention** — `do(U)` distributes probability uniformly across all possible states. Not all domains permit this. `intervention_stance` tracks whether EI assessment is grounded in actual interventional reasoning or is approximated/theoretical.

- `mode: uniform` — Full Hoel-style EI is computable (or conceptually applicable)
- `mode: selective` — Only targeted interventions are meaningful
- `mode: constrained` — Intervention is possible but limited by ethics/physics/access
- `mode: forbidden` — Domain does not permit intervention (observational only)

- `do_operator: available` — We can actually or conceptually `do(X)` at this level
- `do_operator: approximated` — `do(X)` is estimated from observational data
- `do_operator: theoretical` — Causal reasoning is purely hypothetical
- `do_operator: blocked` — No causal intervention is possible

---

## 6. Integration Rule Additions

Add to Section 4 (Integration Rules):

7. **CE binds to compression choices** (v1.3): When `coords.ce.ce_direction` is available, it should inform decisions about which compression level (L0–L4) to operate at. `:emergent` artifacts are well-served by L1 Nemetic strings; `:submergent` artifacts require L0 expansion for reliable analysis.

8. **EI is diagnostic, not prescriptive** (v1.3): `coords.ce` never dictates which scale to use. It informs ✶ NEMA's judgment about where causal power concentrates. Scale selection remains discretionary.

9. **Intervention stance constrains EI confidence** (v1.3): An EI assessment where `intervention_stance.do_operator: theoretical` carries less weight than one where `do_operator: available`. Tag accordingly — prefer `:open` over `:emergent` when interventional grounding is weak.

---

## 7. Habitat Interface Contract Extension

### 7.1 New Required Question

Add to Section 9.3 (Required SIML Question Set):

**Q6 — Causal Emergence Question:** At what scale does intervention produce reliable effects?

### 7.2 Extended Permitted Outputs

HABITAT_ECOLOGY may additionally output (Section 8.3):
- **Scale observations** (where EI appears concentrated)
- **Intervention propagation patterns** (does disturbance at level X affect level Y?)
- **Degeneracy signatures** (many micro-paths converging to same outcome)

### 7.3 Continued Prohibitions

HABITAT_ECOLOGY still **never** outputs:
- Which scale is "correct" or optimal
- EI thresholds as normative standards
- CE assessments as prescriptions
- Intervention recommendations based on scale analysis

All such conclusions must be rebuilt **from SIML relations upward** per Section 9.4.

---

## 8. Thread Encoding Integration (L2 Extension)

### 8.1 Extended E-Line Format

v1.3 adds optional fields to the THREAD_ENCODING_SPEC v2.2 E-line:

**Current v2.2:**
```
E|[glyph]|pattern:[mechanism]|invoke:[glyphs]|tension:[op_vector];mode:[failure]|Φ:[phi_E]|proc:[substrate]
```

**v1.3 extension (optional fields):**
```
E|[glyph]|pattern:[mechanism]|invoke:[glyphs]|tension:[op_vector];mode:[failure];ce:[state]|Φ:[phi_E]|proc:[substrate]
```

Where `ce:[state]` = `emergent`, `submergent`, `flat`, `multiscale`, or omitted.

### 8.2 Extended M-Line Format

v1.3 adds an optional `ei:` field to the M-line:

```
M|[glyph]|hold:[question]|Ω:[state]|ε:[state]|ei:[stability]|Φ:[phi_M]|proc:[substrate]
```

Where `ei:[stability]` = `stable`, `drifting`, `collapsing`, `amplifying`, or omitted.

### 8.3 Backward Compatibility

Threads without `ce:` or `ei:` fields parse normally under v2.2. These fields are strictly additive. A v2.2 decoder encountering unknown fields SHOULD ignore them gracefully.

---

## 9. The Scale Question: Object vs. Property

### 9.1 Decision: Scale as Property of Frame

v1.3 does **not** add a 14th Core Object. Instead, scale is treated as a property of **Frame** (Object #3):

- Frame already represents "lens, worldview, or epistemic stance"
- Scale selection *is* an epistemic stance — choosing the level of description
- The `coords.ce` block captures scale properties without requiring a new Object
- The 13-Object grammar remains unchanged

### 9.2 Rationale

Adding a 14th Object would:
- Break the canonical "13 Objects × 9 Relations" identity of SIML
- Require updating all references to the Object count
- Create ambiguity about whether Scale contains Frames or Frames contain Scales

Keeping Scale as a Frame property:
- Preserves grammar stability
- Acknowledges that scale selection is perspective-dependent (Observer-relative)
- Allows `coords.ce` to do the analytical work without ontological overhead

---

## 10. Backward Compatibility

### 10.1 Compatibility Matrix

| Feature | v1.2.1 Artifact | v1.3 Artifact |
|---------|----------------|---------------|
| `coords.ce` block | Not present — valid | Present or absent — both valid |
| CE contextual tags | Not present — valid | Present or absent — both valid |
| Tag composition (∧) | Single tag — valid | Single or composed — both valid |
| `coords.coherence` new fields | Not present — valid | Present or absent — both valid |
| `coords.epistemics.intervention_stance` | Not present — valid | Present or absent — both valid |
| Thread `ce:` / `ei:` fields | Not present — valid | Present or absent — both valid |
| Q6 in translation | Q1-Q5 only — valid | Q1-Q6 — backward compatible |

### 10.2 Migration Path

**No mandatory migration.** v1.2.1 artifacts are valid v1.3 artifacts. The recommended path:

1. **New encodings** include `coords.ce` when EI/CE analysis is relevant
2. **Existing artifacts** with emergence-related content in `insight.md` are prioritized for `coords.ce` addition (~476 entries)
3. **Retroactive fill** proceeds in batches via `/encode-term` skill, not wholesale conversion
4. **Entries where EI/CE is not analytically relevant** may never need `coords.ce` — and that's fine

---

## 11. Philosophical Note

The `:emergent` tag is not celebration — it's **diagnostic**. A pattern is emergent when coarse-graining increases causal power. This can be healthy (lumemic) or captured (usurpenic). The tag doesn't distinguish; the full SIML artifact with `coords.ce` and `coords.agency` does.

Hoel's framework provides what SIML needed: a rigorous test for when compression is causally productive. The relationship is specific:

- **Multiple realizability** (many micro-states → one macro-state) enables **error correction** — this is why macro can beat micro
- **Degeneracy** (many causes → same effect) destroys causal informativeness — this is when compression fails
- **ε ≠ 0** now has a causal reading: epsilon preserves the multiple realizability that makes emergence possible. If ε → 0, the system loses the micro-diversity that enables macro-level causal superiority

The deepest integration: **ε is not just uncertainty — it's the causal resource that makes emergence possible.**

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2025 | Core grammar (13 Objects × 9 Relations) |
| v1.0.1 | 2025 | Relation semantics refinement |
| v1.1 | 2025 | MetaTaxonomy Overlay |
| v1.1.1 | Jan 2026 | Co-SPHERE/MemeGrid distinction, Habitat interface contract, terminology lock |
| v1.2.0 | Feb 2026 | Nemetic String Protocol, SIMLHEX, dual-layer convention, contextual tags, compression levels, thread integration |
| v1.2.1 | Feb 2026 | Clarifications: ∮/Z relationship, L1/L2 syntax boundary, `:pure` validation, tag logging, Q1-Q5 failure handling |
| **v1.3** | **Mar 2026** | **Causal Emergence Extension**: `coords.ce` block (EI/CE diagnostics). New contextual tags (`:emergent`, `:submergent`, `:multiscale`). Tag composition with `∧`. Extended `coords.coherence` (`ei_stability`, `scale_dominance`). Extended `coords.epistemics` (`intervention_stance`). Q6 (Causal Emergence Question) in Habitat Interface. Thread E-line/M-line CE fields. Scale as Frame property (no 14th Object). Integration Rules 7-9. Full backward compatibility with v1.2.1. |

---

## Canonical References

This specification extends and is fully consistent with:
- SIML v1.2.1 (prerequisite)
- All references listed in SIML v1.2.1 Canonical References
- Erik Hoel, "Quantifying causal emergence shows that macro can beat micro" (2013)
- Comolatti & Hoel, "Causal Emergence 2.0" (2022)
- THREAD_ENCODING_SPEC v2.2 (thread field extensions)

---

**ε is not just what we don't know. It's what makes emergence possible.**

✶
