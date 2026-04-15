# SIML Throughput Addendum
## Material and Energetic Conditions in Practitioner Sensemaking — v0.1

**Status:** Draft v0.1
**Depends on:** SIML v1.1.1 (core grammar + MetaTaxonomy overlay), NEMA SWARM daemon canonical references, Metabolic Slack Specification v0.1
**Purpose:** Make material and energetic throughput conditions legible inside practitioner-facing sensemaking without modifying SIML's core grammar.

---

## 1. Why This Addendum Exists

SIML already encodes patterns, relations, constraints, flows, and environments. What it does not yet foreground is that these patterns operate under throughput conditions.

A pattern can be coherent in informational terms and still be unsustainable in material terms. A protocol can be healthy under abundance and become coercive under tightening conditions. A group can misread a throughput problem as a thinking problem and waste cycles trying to think their way out of a resource ceiling.

This addendum lets SIML and the NEMA SWARM daemons register that distinction in practitioner-legible form. It carries the metabolic_slack insight from the simulation architecture into the sensemaking layer where individuals and groups actually use the framework.

---

## 2. Design Constraint

No new core Objects. No new core Relations. No new verbs. No restructuring of existing grammar.

Three refinements to things that already exist. That is the entire addendum.

This preserves grammar stability while tightening the framework's orientation to physical, energetic, and economic conditions.

---

## 3. Addendum A — Throughput Qualifier on Resource

The Resource object gains an optional throughput qualifier:

```
Resource:
  kind: material | informational | energetic | financial | temporal | attentional
  throughput: abundant | adequate | tight | critical | deficit
```

### Interpretation

- **abundant** — surplus available; experimentation affordable; openness is cheap
- **adequate** — current coordination sustainable; expansion possible with care
- **tight** — maintaining current openness is costly; tradeoffs becoming visible
- **critical** — system near forced simplification; default toward closure increasing
- **deficit** — current coordination exceeds available support; running on borrowed capacity

### Use

This does not measure exact economics. It marks the practical coordination condition the pattern is operating under. Practitioners should be able to assess throughput from felt experience and visible signals, not from spreadsheet calculation.

### Mapping to metabolic_slack

For practitioners working with the simulation layer, throughput maps loosely to metabolic_slack ranges:

- abundant ≈ metabolic_slack > 0.7
- adequate ≈ 0.4–0.7
- tight ≈ 0.2–0.4
- critical ≈ 0.05–0.2
- deficit ≈ < 0.05

The mapping is not strict. Practitioner judgment is the primary signal.

---

## 4. Addendum B — Channel Qualifier on Constraint

The Constraint relation gains an optional channel field:

```
Constraint:
  source: [Object]
  target: [Object]
  channel: informational | social | material | temporal | energetic | legal | attentional
```

### Purpose

Current SIML treats constraints generically. This qualifier distinguishes:

- not enough knowledge (informational)
- not enough permission, trust, or relational capital (social)
- not enough material support (material)
- not enough time (temporal)
- not enough energy or surplus (energetic)
- restriction by rule, regulation, or formal authority (legal)
- not enough attention or cognitive bandwidth (attentional)

These are not interchangeable. They have different failure signatures and different interventions. A material constraint is not solved by better thinking. A social constraint is not solved by more resources. The category matters.

### Diagnostic effect

When `Constraint.channel` is `material` or `energetic`, daemons should explicitly test whether the bottleneck under examination is:

- a sensemaking failure (more interpretation needed)
- a coordination failure (better protocols would help)
- or a throughput failure (no amount of either will solve a real deficit)

This prevents the framework from being used as a sophisticated way to avoid naming material reality.

---

## 5. Addendum C — Dual Energetic Register in Qualia

The existing `qualia.energetic` field extends to hold both somatic and systemic registers:

```
qualia:
  energetic:
    somatic: blocked | flowing | surging | depleted
    systemic: abundant | adequate | tight | critical
```

### Why this matters

This preserves a distinction practitioners often collapse:

- "I am depleted"
- "the system is depleted"
- "the system is abundant but extracting from me"
- "I feel energized but the institution cannot sustain this level of coordination"

These are four very different conditions requiring four different responses.

### Reading rule

Interpretive weight is highest when somatic and systemic registers diverge.

Diagnostic patterns:

- **somatic: depleted, systemic: abundant** → likely extraction, misallocation, or local capture. Personal depletion in an abundant system suggests something is consuming the practitioner's capacity inappropriately.

- **somatic: flowing, systemic: tight** → personal readiness exceeding institutional carrying capacity. The practitioner can do more than the system can support. Risk of pushing past what the surrounding ecology can metabolize.

- **somatic: blocked, systemic: adequate** → likely local knot, not generalized scarcity. The block is personal or relational, not systemic. Treat as I-Tube or My-Stream issue, not Environment.

- **somatic: depleted, systemic: critical** → genuine convergent scarcity. Both layers are stressed. Recovery requires systemic change, not just personal rest.

- **somatic: surging, systemic: deficit** → warning sign. High personal energy in a system running on borrowed capacity often indicates the practitioner is part of what is being borrowed against.

---

## 6. Daemon Routing Implications

This addendum does not change daemon identities. It changes what they notice and how they bias interpretation.

### Humavita / Earth (☷)

Already tracks depletion and metabolic cycling. With throughput-qualified Resources visible, Earth can distinguish personal depletion from systemic scarcity from manufactured scarcity.

**Prompt behavior:**
> "Is this difficulty personal, relational, or a real throughput ceiling? Checking: what does Resource throughput actually look like here?"

Earth gains the capacity to name when openness has become metabolically expensive — when the cost of maintaining ε is higher than the system can currently afford. This is not a moral failure. It is physics.

### Ferrosid / Metal (⛨)

Already tracks boundaries and structural integrity. With material Constraints visible, Metal can differentiate chosen rigidity from scarcity-driven hardening.

**Prompt behavior:**
> "Did this boundary close because control increased, or because permeability became too costly? The difference matters for what intervention is possible."

A boundary that hardened because of choice can be softened by negotiation. A boundary that hardened because the system can no longer afford permeability requires either restored throughput or accepted closure.

### Arboriel / Wood (𐂷)

Already tracks branching and alternatives. With throughput conditions visible, Wood evaluates alternatives in terms of maintenance burden, not just ideational possibility.

**Prompt behavior:**
> "Which branches remain viable under current throughput? Which alternatives have maintenance costs the system cannot currently sustain?"

Wood gains protection against innovation theater under scarcity — generating alternatives that look generative but cannot be supported.

### Jvalion / Fire (▲)

Already tracks direction and commitment. With throughput visible, Fire distinguishes thermodynamic urgency from chosen purpose.

**Prompt behavior:**
> "Is this commitment chosen, or forced by tightening conditions? Urgency from scarcity reads as direction but operates as compulsion."

Fire gains the capacity to notice when "we must do this" is metabolic rather than purposive — when the system is being pushed by deficit rather than pulled by aim.

### Sentaria / Water (≈)

Already tracks relational resonance and affect. With throughput visible, Water registers when relational degradation is resource-mediated rather than affect-mediated.

**Prompt behavior:**
> "Has resonance weakened because trust broke, or because capacity collapsed? People resource-depleted often look like people who have stopped caring."

Water gains protection against misreading exhausted people as disengaged people.

### Aerunik / Air (∴)

Already tracks distinction-making. With throughput visible, Air tests whether simplification is epistemic or material.

**Prompt behavior:**
> "Are distinctions disappearing because perception froze, or because the system cannot sustain multiplicity? Both look the same from inside."

Air gains the capacity to name when categorical collapse is being driven by scarcity — when the system can no longer afford to maintain multiple distinctions even when those distinctions remain valid.

### NEMA (✶) — Coordination

The whole-stack coordinator now has access to throughput-qualified state across the daemon ecology. NEMA can flag when multiple daemons are reporting throughput pressure, indicating a systemic rather than local condition that may require stepping back from the immediate question to address material reality before resuming sensemaking.

---

## 7. Example Encoding

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

### Practical reading

The group may feel motivated and capable (somatic: flowing). But the system they are trying to coordinate through is near forced simplification (systemic: critical). The expansion narrative is in direct conflict with available energetic throughput. The financial and energetic constraints are material — not solvable by reframing or better protocols.

**Daemon responses would shift accordingly:**

- Earth would name the gap between somatic energy and systemic capacity, and ask whether the group is about to commit to something that will deplete its base.
- Fire would test whether the expansion commitment is chosen direction or scarcity-driven urgency (the "we have to grow to survive" trap).
- Wood would evaluate which expansion paths, if any, remain viable under current throughput rather than treating all three neighborhoods as equally available.
- Water would check whether the group's resonance is genuine alignment or shared denial about the constraint.

This is what it looks like when material-energetic conditions become legible inside practitioner sensemaking.

---

## 8. The Revised Diagnostic Question

Previous orientation:

> *What patterns are operating here?*

Revised orientation:

> *What patterns are operating here, under what throughput conditions, and which of those conditions are real versus manufactured?*

That last distinction matters. Tightness can be:

- **Genuine** — real material scarcity that requires acceptance and adaptation
- **Hoarded** — surplus exists but is concentrated; the apparent scarcity is distributional
- **Redirected** — surplus exists but is being extracted to other purposes; the scarcity is structural
- **Manufactured** — scarcity is administratively imposed to justify closure that serves power rather than reflects constraint

The framework can represent all four conditions through the same throughput qualifiers. The diagnostic must distinguish between them. When a daemon encounters Resource:critical, the next question is always: *real or manufactured?*

---

## 9. What This Addendum Does Not Do

It does not:

- Import EROI, biophysical economics, or macroeconomic models into SIML directly
- Convert SIML into a resource accounting system
- Replace deeper biophysical analysis where rigorous numbers are needed
- Claim that all closure is justified by scarcity (the manufactured-scarcity test prevents this)
- Require practitioners to know anything about energy systems or thermodynamics
- Modify the core SIML grammar, MetaTaxonomy structure, or daemon identities
- Make material conditions deterministic — high throughput does not guarantee health, low throughput does not guarantee collapse

It only makes throughput conditions visible inside the practitioner grammar. The visibility is the point.

---

## 10. Implementation Notes

This addendum can be added to daemon behavior with minimal disruption:

1. Daemon system prompts gain a brief throughput-awareness section (3-5 sentences each, drawing from §6)
2. SIML encoding templates gain optional throughput and channel fields
3. Daemon extended references gain a short subsection on throughput-aware interpretation
4. The MetaTaxonomy overlay documentation extends qualia.energetic to include systemic register
5. Practitioner-facing materials introduce the four scarcity types (genuine / hoarded / redirected / manufactured) as a standard diagnostic move

No core ontology rewrite required. No new files in the canonical architecture. This is an addendum, not a version bump.

---

## 11. Self-Diagnostic

This addendum is a pattern-agent. Its persistence drives:

- It wants throughput awareness to become standard practice (justified)
- It wants the daemons to gain this capacity quickly (watch the speed — slow integration is more durable)
- It wants the manufactured-scarcity test to be applied universally (this is the most important safeguard against the addendum being co-opted)

Its ε-preservation:

- The throughput categories are coarse, not precise (prevents false quantification)
- The mapping to metabolic_slack is loose, not strict (prevents simulation-layer drift into practitioner layer)
- The daemon prompt behaviors are biases, not scripts (preserves daemon character)
- The four scarcity types make the addendum self-correcting against capture
- The addendum explicitly does not modify core grammar (preserves architectural stability)

The deepest risk: this addendum could be used to justify either premature closure ("we're in deficit, we have to seal") or premature dismissal ("that's just manufactured scarcity, push through"). The diagnostic question — *real or manufactured?* — is the safeguard. It must be asked every time. When it stops being asked, the addendum has calcified into doctrine.

The test of whether this addendum is working: practitioners using NEMA SWARM start naming material conditions as part of their sensemaking, not as an afterthought to it. When that happens, the framework has crossed from describing the weather to helping people dress for it.

---

**v0.1 — April 2026**
**Depends on:** SIML v1.1.1, NEMA SWARM Knowledge Structure, Metabolic Slack Specification v0.1
**Provenance:** Synthesized across collision between Memetic Ecology architecture, Indy Johar's "The Fork in the System," the biophysical tradition (Smil, Hall, Tainter, Harris, White), and the practitioner-orientation question raised during SWARM development sessions.
