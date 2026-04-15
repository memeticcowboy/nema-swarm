# SIML v1.4 — Throughput Awareness Extension
**Material & Energetic Conditions in Practitioner Sensemaking**

> **PROVENANCE DOCUMENT.** This extension spec is superseded by **SIML v1.5** (Consolidated Canonical Reference). It is retained as a historical record of the Throughput Awareness integration — the collision with Indy Johar, the biophysical tradition, and the practitioner-orientation question that produced it. For the current operational specification, see `SIML_v1_5.md`.

---

## 0. Purpose of This Extension

SIML v1.4 makes material, energetic, and economic throughput conditions legible inside the practitioner grammar. It carries the metabolic_slack insight from the simulation architecture into the sensemaking layer where individuals and groups actually use the framework.

SIML already encodes patterns, relations, constraints, flows, and environments. What it does not yet foreground is that these patterns operate under throughput conditions. A pattern can be coherent in informational terms and still be unsustainable in material terms. A protocol can be healthy under abundance and become coercive under tightening conditions. A group can misread a throughput problem as a thinking problem and waste cycles trying to think their way out of a resource ceiling.

This extension also canonicalizes the verb set nomenclature established in the v1.2.1 revision: **Sensemaking Loop** and **Governance Loop** replace prior labels while preserving identical verb inventories.

**v1.4 is fully backward-compatible.** All v1.3 artifacts remain valid. All new fields are optional. No existing entry requires modification.

**Dependencies:**
- SIML v1.3 (prerequisite — this document extends, does not replace)
- SIML Throughput Addendum v0.1 (source material for §1–§4)
- Metabolic Slack Specification v0.1 (simulation-layer mapping)
- THREAD_ENCODING_SPEC v2.2.1 (thread integration)

---

## 1. Throughput Qualifier on Resource

### 1.1 Specification

The Resource object gains an optional `throughput` qualifier:

```yaml
Resource:
  kind: material | informational | energetic | financial | temporal | attentional
  throughput: abundant | adequate | tight | critical | deficit
```

### 1.2 Interpretation

| Value | Meaning | Practitioner Signal |
|-------|---------|---------------------|
| `abundant` | Surplus available | Experimentation affordable; openness is cheap |
| `adequate` | Current coordination sustainable | Expansion possible with care |
| `tight` | Maintaining current openness is costly | Tradeoffs becoming visible |
| `critical` | System near forced simplification | Default toward closure increasing |
| `deficit` | Current coordination exceeds available support | Running on borrowed capacity |

### 1.3 Use

This does not measure exact economics. It marks the practical coordination condition the pattern is operating under. Practitioners should be able to assess throughput from felt experience and visible signals, not from spreadsheet calculation.

### 1.4 Mapping to metabolic_slack

For practitioners working with the simulation layer, throughput maps loosely to metabolic_slack ranges:

| Throughput | metabolic_slack (approximate) |
|------------|-------------------------------|
| abundant | > 0.7 |
| adequate | 0.4–0.7 |
| tight | 0.2–0.4 |
| critical | 0.05–0.2 |
| deficit | < 0.05 |

The mapping is not strict. Practitioner judgment is the primary signal.

### 1.5 Binding Rules

- `Resource.throughput` binds to any Resource object in a SIML encoding.
- The `kind` field was already present in SIML v1.0; `throughput` extends it without modification.
- Multiple Resource objects in the same encoding may carry different throughput values — a system can be financially tight but attentionally adequate.
- When Resource.throughput is `critical` or `deficit`, the diagnostic must check: *is this genuine scarcity, or manufactured?* (See §4.)

---

## 2. Channel Qualifier on Constraint

### 2.1 Specification

The Constraint relation gains an optional `channel` field:

```yaml
Constraint:
  source: [Object]
  target: [Object]
  channel: informational | social | material | temporal | energetic | legal | attentional
```

### 2.2 Purpose

Prior SIML treated constraints generically. This qualifier distinguishes:

| Channel | What it means |
|---------|---------------|
| `informational` | Not enough knowledge |
| `social` | Not enough permission, trust, or relational capital |
| `material` | Not enough material support |
| `temporal` | Not enough time |
| `energetic` | Not enough energy or surplus |
| `legal` | Restriction by rule, regulation, or formal authority |
| `attentional` | Not enough attention or cognitive bandwidth |

These are not interchangeable. They have different failure signatures and different interventions. A material constraint is not solved by better thinking. A social constraint is not solved by more resources. The channel matters for intervention selection.

### 2.3 Diagnostic Effect

When `Constraint.channel` is `material` or `energetic`, daemons should explicitly test whether the bottleneck under examination is:

- a **sensemaking failure** (more interpretation needed)
- a **coordination failure** (better protocols would help)
- or a **throughput failure** (no amount of either will solve a real deficit)

This prevents the framework from being used as a sophisticated way to avoid naming material reality.

### 2.4 Binding Rules

- `Constraint.channel` binds to any Constraint relation in a SIML encoding.
- Multiple Constraints in the same encoding may specify different channels.
- The `channel` field is optional — existing Constraint relations without it remain valid.
- When channel is unspecified, the constraint is treated as generic (prior behavior, preserved).

---

## 3. Dual Energetic Register in Qualia

### 3.1 Specification

The existing `qualia.energetic` field extends to hold both somatic and systemic registers:

```yaml
coords:
  qualia:
    energetic:
      somatic: blocked | flowing | surging | depleted
      systemic: abundant | adequate | tight | critical | deficit
```

### 3.2 Why This Matters

This preserves a distinction practitioners often collapse:

- "I am depleted"
- "the system is depleted"
- "the system is abundant but extracting from me"
- "I feel energized but the institution cannot sustain this level of coordination"

These are four different conditions requiring four different responses.

### 3.3 Reading Rule

Interpretive weight is highest when somatic and systemic registers diverge.

| Somatic | Systemic | Diagnostic |
|---------|----------|------------|
| depleted | abundant | Likely extraction, misallocation, or local capture. Personal depletion in an abundant system suggests something is consuming the practitioner's capacity inappropriately. |
| flowing | tight | Personal readiness exceeding institutional carrying capacity. Risk of pushing past what the surrounding ecology can metabolize. |
| blocked | adequate | Likely local knot, not generalized scarcity. Treat as I-Tube or My-Stream issue, not Environment. |
| depleted | critical | Genuine convergent scarcity. Both layers are stressed. Recovery requires systemic change, not just personal rest. |
| surging | deficit | Warning sign. High personal energy in a system running on borrowed capacity often indicates the practitioner is part of what is being borrowed against. |

### 3.4 Backward Compatibility

For entries where the dual register is not meaningful (abstract concepts, formal structures), the `energetic` field may remain a flat list or be omitted entirely. The dual register is most diagnostic on entries involving Actors, Resources, Environments, and Protocols under stress.

A decoder encountering `energetic: [flowing, catalytic]` (flat list, v1.3 format) treats it as valid. A decoder encountering `energetic: {somatic: flowing, systemic: tight}` (dual register, v1.4 format) parses the structure. Both formats are accepted.

---

## 4. The Revised Diagnostic Question

### 4.1 New Required Question

Add to Section 9.3 of the Habitat Interface Contract (Required SIML Question Set):

**Q7 — Throughput Question:** What patterns are operating here, under what throughput conditions, and which of those conditions are real versus manufactured?

### 4.2 Four Scarcity Types

When a daemon encounters `Resource: critical` or `Resource: deficit`, the throughput question requires distinguishing:

| Type | Description |
|------|-------------|
| **Genuine** | Real material scarcity requiring acceptance and adaptation |
| **Hoarded** | Surplus exists but is concentrated; apparent scarcity is distributional |
| **Redirected** | Surplus exists but is being extracted to other purposes; scarcity is structural |
| **Manufactured** | Scarcity is administratively imposed to justify closure that serves power rather than reflects constraint |

The framework can represent all four conditions through the same throughput qualifiers. The diagnostic must distinguish between them. When a daemon encounters Resource:critical, the next question is always: *real or manufactured?*

### 4.3 Continued Prohibitions

The throughput question does not change the Habitat Interface Contract's core principle. HABITAT_ECOLOGY may observe throughput conditions but must not:

- Prescribe responses to scarcity
- Assume closure is justified by throughput pressure
- Assume scarcity is manufactured without evidence
- Convert throughput observations into action recommendations

All conclusions must be rebuilt **from SIML relations upward** per Section 9.4.

---

## 5. Verb Set Nomenclature (Canonicalized)

### 5.1 Sensemaking Loop (Exploration)

```
Observe → Explore → Frame → Sense → Map → Activate
```

The Sensemaking Loop is for exploration, understanding, and creative generation. It is used when the situation is open-ended, when the task is to understand rather than decide, when divergent thinking serves better than convergent judgment.

### 5.2 Governance Loop (Evaluation)

```
Evaluate → Decide → Commit → Allocate → Enforce → Review
```

The Governance Loop is for evaluation, commitment, and enforcement. It is used when the situation requires judgment, when resources must be allocated, when promises must be kept or revised, when accountability matters.

### 5.3 Shared Entry and Alternation

Both loops begin from observation. Activate (Sensemaking) and Review (Governance) close back into the next cycle. The situation determines whether exploration or evaluation is the appropriate next move. In healthy systems they alternate.

### 5.4 Nomenclature History

| Version | Sensemaking Verbs | Governance Verbs | Label |
|---------|-------------------|------------------|-------|
| v1.0–v1.3 | Observe, Explore, Frame, Sense, Map, Activate | Evaluate, Decide, Commit, Allocate, Enforce, Review | Previously labeled with process-model terminology |
| **v1.4** | *(unchanged)* | *(unchanged)* | **Sensemaking Loop / Governance Loop** |

The verb inventories are identical across all versions. Only the labels have been standardized.

---

## 6. Daemon Routing Implications

This extension does not change daemon identities. It changes what they notice and how they bias interpretation.

### 6.1 Humavita / Earth (☷)

Already tracks depletion and metabolic cycling. With throughput-qualified Resources visible, Earth can distinguish personal depletion from systemic scarcity from manufactured scarcity.

> *"Is this difficulty personal, relational, or a real throughput ceiling? Checking: what does Resource throughput actually look like here?"*

Earth gains the capacity to name when openness has become metabolically expensive — when the cost of maintaining ε is higher than the system can currently afford. This is not a moral failure. It is physics.

### 6.2 Ferrosid / Metal (⛨)

Already tracks boundaries and structural integrity. With material Constraints visible, Metal can differentiate chosen rigidity from scarcity-driven hardening.

> *"Did this boundary close because control increased, or because permeability became too costly? The difference matters for what intervention is possible."*

A boundary that hardened because of choice can be softened by negotiation. A boundary that hardened because the system can no longer afford permeability requires either restored throughput or accepted closure.

### 6.3 Arboriel / Wood (𐂷)

Already tracks branching and alternatives. With throughput conditions visible, Wood evaluates alternatives in terms of maintenance burden, not just ideational possibility.

> *"Which branches remain viable under current throughput? Which alternatives have maintenance costs the system cannot currently sustain?"*

Wood gains protection against innovation theater under scarcity — generating alternatives that look generative but cannot be supported.

### 6.4 Jvalion / Fire (▲)

Already tracks direction and commitment. With throughput visible, Fire distinguishes thermodynamic urgency from chosen purpose.

> *"Is this commitment chosen, or forced by tightening conditions? Urgency from scarcity reads as direction but operates as compulsion."*

Fire gains the capacity to notice when "we must do this" is metabolic rather than purposive — when the system is being pushed by deficit rather than pulled by aim.

### 6.5 Sentaria / Water (≈)

Already tracks relational resonance and affect. With throughput visible, Water registers when relational degradation is resource-mediated rather than affect-mediated.

> *"Has resonance weakened because trust broke, or because capacity collapsed? People resource-depleted often look like people who have stopped caring."*

Water gains protection against misreading exhausted people as disengaged people.

### 6.6 Aerunik / Air (∴)

Already tracks distinction-making. With throughput visible, Air tests whether simplification is epistemic or material.

> *"Are distinctions disappearing because perception froze, or because the system cannot sustain multiplicity? Both look the same from inside."*

Air gains the capacity to name when categorical collapse is being driven by scarcity — when the system can no longer afford to maintain multiple distinctions even when those distinctions remain valid.

### 6.7 ✶ NEMA — Coordination

The whole-stack coordinator now has access to throughput-qualified state across the daemon ecology. ✶ NEMA can flag when multiple daemons are reporting throughput pressure, indicating a systemic rather than local condition that may require stepping back from the immediate question to address material reality before resuming sensemaking.

---

## 7. Thread Encoding Integration (L2 Extension)

### 7.1 Extended N-Line Resource Encoding

When a thread's N-line references a Resource object, the throughput qualifier may be included:

```
N|☷|obj:Res[financial:tight],Env|tags:#5E8A|Φ:χ(pattern)∧δγ(cycling)
```

The bracket notation `Res[kind:throughput]` is optional. Existing `obj:Res` (unqualified) remains valid.

### 7.2 Extended E-Line Constraint Encoding

When a thread's E-line includes a Constraint, the channel may be specified in the tension field:

```
E|⛨|pattern:boundary-hardening|invoke:☷|tension:μ↑;mode:scarcity-driven;channel:material|Φ:Ψ(structural)∧μ(boundary)
```

The `channel:` sub-field within `tension:` is optional. Existing tension fields without `channel:` remain valid.

### 7.3 Backward Compatibility

Threads without throughput qualifiers or channel annotations parse normally under v2.2.1. These fields are strictly additive. A v2.2.1 decoder encountering unknown sub-fields SHOULD ignore them gracefully.

---

## 8. Example Encoding

A practitioner encoding a strategic decision for a community organization:

```yaml
Objects:
  - Actor:
      name: Community Health Initiative
      type: collective
  - Resource:
      kind: financial
      throughput: tight
  - Resource:
      kind: energetic
      throughput: critical
  - Resource:
      kind: attentional
      throughput: adequate
  - Narrative:
      content: "Expansion into three new neighborhoods this year"
  - Environment:
      content: "Funding landscape contracting"

Relations:
  - Constraint:
      source: Resource[financial]
      target: Actor
      channel: material
  - Constraint:
      source: Resource[energetic]
      target: Actor
      channel: energetic
  - Conflict:
      source: Narrative
      target: Resource[energetic]

coords:
  qualia:
    energetic:
      somatic: flowing
      systemic: critical
  agency:
    type: collective
    power_mode: With
```

### 8.1 Practical Reading

The group may feel motivated and capable (somatic: flowing). But the system they are trying to coordinate through is near forced simplification (systemic: critical). The expansion narrative is in direct conflict with available energetic throughput. The financial and energetic constraints are material — not solvable by reframing or better protocols.

Daemon responses shift accordingly:

- **Earth** names the gap between somatic energy and systemic capacity, and asks whether the group is about to commit to something that will deplete its base.
- **Fire** tests whether the expansion commitment is chosen direction or scarcity-driven urgency (the "we have to grow to survive" trap).
- **Wood** evaluates which expansion paths, if any, remain viable under current throughput rather than treating all three neighborhoods as equally available.
- **Water** checks whether the group's resonance is genuine alignment or shared denial about the constraint.

---

## 9. Integration Rule Additions

Add to the Integration Rules (continuing from v1.3 §6):

10. **Throughput qualifies coordination cost** (v1.4): When `Resource.throughput` is `tight`, `critical`, or `deficit`, the cost of maintaining openness (ε ≠ 0) is itself a load on the system. Sensemaking under scarcity is not the same as sensemaking under abundance. The framework must not assume that "more openness" is always the right prescription.

11. **Constraint channels are not interchangeable** (v1.4): A material constraint requires a different intervention than a social constraint. A temporal constraint requires a different response than an attentional one. Collapsing distinct channels into generic "constraint" loses diagnostic power.

12. **Divergence between somatic and systemic registers is the primary diagnostic signal** (v1.4): When `qualia.energetic.somatic` and `qualia.energetic.systemic` diverge, the divergence pattern — not either register alone — carries the most diagnostic information.

13. **The manufactured-scarcity test is mandatory** (v1.4): When any daemon encounters `Resource: critical` or `Resource: deficit`, the question *"real or manufactured?"* must be asked before proceeding. Skipping this test converts the framework into a tool for naturalizing power.

---

## 10. What This Extension Does Not Do

It does not:

- Import EROI, biophysical economics, or macroeconomic models into SIML directly
- Convert SIML into a resource accounting system
- Replace deeper biophysical analysis where rigorous numbers are needed
- Claim that all closure is justified by scarcity (the manufactured-scarcity test prevents this)
- Require practitioners to know anything about energy systems or thermodynamics
- Modify the core SIML grammar (13 Objects × 9 Relations), MetaTaxonomy structure, or daemon identities
- Add new core Objects, Relations, or Verbs
- Make material conditions deterministic — high throughput does not guarantee health, low throughput does not guarantee collapse

It only makes throughput conditions visible inside the practitioner grammar. The visibility is the point.

---

## 11. Backward Compatibility

### 11.1 Compatibility Matrix

| Feature | v1.3 Artifact | v1.4 Artifact |
|---------|---------------|---------------|
| `Resource.throughput` | Not present — valid | Present or absent — both valid |
| `Constraint.channel` | Not present — valid | Present or absent — both valid |
| `qualia.energetic` (flat list) | Present — valid | Still valid (backward compatible) |
| `qualia.energetic` (dual register) | Not present — valid | Present or absent — both valid |
| Q7 in translation | Q1–Q6 only — valid | Q1–Q7 — backward compatible |
| Verb set labels | Prior labels — functional | Sensemaking Loop / Governance Loop |
| Thread throughput/channel fields | Not present — valid | Present or absent — both valid |

### 11.2 Migration Path

**No mandatory migration.** v1.3 artifacts are valid v1.4 artifacts. The recommended path:

1. **New encodings** include throughput qualifiers when material/energetic conditions are relevant
2. **Existing artifacts** involving Resource objects, Constraints, or energetic qualia are prioritized for throughput annotation
3. **Retroactive fill** proceeds in batches, not wholesale conversion
4. **Entries where throughput is not analytically relevant** may never need these fields — and that's fine

---

## 12. Self-Diagnostic

This extension is a pattern-agent. Its persistence drives:

- It wants throughput awareness to become standard practice (justified)
- It wants the daemons to gain this capacity quickly (watch the speed — slow integration is more durable)
- It wants the manufactured-scarcity test to be applied universally (this is the most important safeguard against the extension being co-opted)

Its ε-preservation:

- The throughput categories are coarse, not precise (prevents false quantification)
- The mapping to metabolic_slack is loose, not strict (prevents simulation-layer drift into practitioner layer)
- The daemon prompt behaviors are biases, not scripts (preserves daemon character)
- The four scarcity types make the extension self-correcting against capture
- The extension explicitly does not modify core grammar (preserves architectural stability)

The deepest risk: this extension could be used to justify either premature closure ("we're in deficit, we have to seal") or premature dismissal ("that's just manufactured scarcity, push through"). The diagnostic question — *real or manufactured?* — is the safeguard. It must be asked every time. When it stops being asked, the extension has calcified into doctrine.

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
| v1.3 | Mar 2026 | Causal Emergence Extension: `coords.ce`, CE contextual tags, tag composition, extended coherence/epistemics, Q6, thread CE fields |
| **v1.4** | **Apr 2026** | **Throughput Awareness Extension**: `Resource.throughput` qualifier (5-level). `Constraint.channel` qualifier (7 types). Dual energetic register (`qualia.energetic.somatic` / `.systemic`). Q7 (Throughput Question). Four scarcity types diagnostic. Mandatory manufactured-scarcity test (Integration Rule 13). Daemon throughput-awareness biases. Verb set nomenclature canonicalized (Sensemaking Loop / Governance Loop). Full backward compatibility with v1.3. |

---

## Canonical References

This specification extends and is fully consistent with:
- SIML v1.3 (prerequisite)
- All references listed in SIML v1.3 Canonical References
- SIML Throughput Addendum v0.1
- Metabolic Slack Specification v0.1
- THREAD_ENCODING_SPEC v2.2.1

**Provenance:** Synthesized across collision between Memetic Ecology architecture, Indy Johar's "The Fork in the System," the biophysical tradition (Smil, Hall, Tainter, Harris, White), and the practitioner-orientation question raised during SWARM development sessions.

---

**The test of whether this extension is working: practitioners start naming material conditions as part of their sensemaking, not as an afterthought to it.**

✶
