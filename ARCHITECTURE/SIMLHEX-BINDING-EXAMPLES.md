---
title: SIMLHEX Binding Examples
version: 1.0
date: March 2026
status: Working Reference
scope: Four worked examples showing habitat → SIML → relation rebuild → SIMLHEX binding
depends: SIML_v1_2_1, SIMLHEX-CANONICAL, SIMLHEX-FAILURE-SURFACES
---

# SIMLHEX BINDING EXAMPLES

## The Pocket Rule

> If you can remove the habitat name and the binding still makes sense, it's valid. If removing the context collapses the insight, it was never SIML-observable — it was habitat-dependent description.

This is the primary quality test for SIMLHEX bindings. Habitat terms (organization names, specific people, industry jargon) must not survive into the binding. The structure must be portable.

---

## Example 1: Corporate Meeting Dysfunction

### Habitat
A recurring weekly meeting at a tech company where decisions are announced but never actually made. The same topics reappear. People perform engagement but leave without clarity.

### SIML Analysis

**Objects identified:**
- Protocol (the meeting structure)
- Actor (participants)
- Outcome (announced decisions)
- Memory (recurring topics)

**Relations:**
- Protocol ← Recursion → Memory (meeting recycles its own content)
- Actor ← Containment → Protocol (participants contained by structure)
- Outcome ← Mapping → Protocol (decisions map to meeting format, not to action)

### Relation Rebuild
The core pattern: **A Protocol in Recursion with Memory, where Outcomes Map to the Protocol rather than to action.** The meeting produces meetings, not decisions.

### SIMLHEX Binding

```
Object: Protocol → μ (Metal) — boundary/structure
Relation: Recursion → ∮ (Aether) — self-referential loop
Secondary: Mapping → σ (Air) — representational correspondence

Bias: μ primary (is this structure still serving?), ∮ secondary (the loop itself needs noticing)
Suggestion: Ferrosid might test if this Protocol still gates or merely contains.
             NEMA might ask: "Does this meeting know it's a meeting?"
```

### Habitat Removal Test
- WITH: "The weekly product sync is stuck in a recursion loop"
- WITHOUT: "A Protocol is in Recursion with its own Memory" — **still valid**
- SIMLHEX: "μ might test if this Protocol is gating or imprisoning" — **still valid**

✓ Binding passes.

---

## Example 2: Grief That Won't Move

### Habitat
A person in therapy who articulates their loss precisely, uses therapeutic vocabulary fluently, but hasn't changed. They describe the grief beautifully. The description has become the relationship to the grief.

### SIML Analysis

**Objects identified:**
- Actor (the person)
- Narrative (the story of loss)
- Frame (therapeutic vocabulary)
- Memory (the grief itself)

**Relations:**
- Narrative ← Mapping → Memory (the story represents the grief)
- Frame ← Containment → Memory (therapeutic language contains the grief)
- Actor ← Distinction → Memory (person distinguishes themselves from grief — but keeps it close)

### Relation Rebuild
The core pattern: **A Narrative Maps to Memory, contained by a Frame, where Distinction maintains distance without Transformation.** The description has replaced the process. Diagnostic → Explanatory drift (Surface 4) at the personal level.

### SIMLHEX Binding

```
Object: Narrative → β (Wood) — story, branching
Relation: Mapping → σ (Air) — representational correspondence
Secondary: Containment → μ (Metal) — the Frame holds too well

Bias: δγ primary (what would it cost to actually release this?), ρ secondary (feel it, don't just name it)
Note: SIMLHEX Object bias says β (story). But NEMA overrides: the story IS the problem.
      The field needs δγ (composting) and ρ (feeling), not more narrative.
```

### Habitat Removal Test
- WITH: "Sarah's grief narrative in session 14 has become self-referential"
- WITHOUT: "A Narrative Maps to Memory without Transformation" — **still valid**
- SIMLHEX: "δγ might ask what this description is costing to maintain" — **still valid**

✓ Binding passes. Note the NEMA override of SIMLHEX default — documented, not hidden.

---

## Example 3: Community Polarization

### Habitat
An online community that began as collaborative and has split into two factions. Each faction believes it represents the original values. Moderators are paralyzed because both sides cite the founding charter.

### SIML Analysis

**Objects identified:**
- Actor × 2 (two factions)
- Value (shared founding values — claimed by both)
- Boundary (the split)
- Protocol (moderation rules)
- Artifact (the founding charter)

**Relations:**
- Actor₁ ← Conflict → Actor₂ (oppositional coupling)
- Actor₁ ← Resonance → Value (faction 1 resonates with their reading)
- Actor₂ ← Resonance → Value (faction 2 resonates with their reading)
- Value ← Mapping → Artifact (both readings map to same charter)
- Protocol ← Constraint → Actor₁,₂ (moderation constrains both)

### Relation Rebuild
The core pattern: **Two Actors in Conflict, each in Resonance with the same Value through different Mappings of the same Artifact.** The Conflict is not about values but about which Mapping of Values is authoritative. The Artifact has become the terrain (Surface 5).

### SIMLHEX Binding

```
Object: Actor → λ (Fire) — agency, directional force
Relation: Conflict → λ (reinforces)
Secondary: Mapping → σ (Air) — the representational question
Tertiary: Resonance → ρ (Water) — each faction's felt connection to values

Bias: σ primary (distinguish what each faction actually claims),
      ρ secondary (feel into each faction's genuine connection to values),
      λ tertiary (where does each faction actually want to go?)
Suggestion: Aerunik might ask "Is this one conflict or two different directions claiming the same name?"
```

### Habitat Removal Test
- WITH: "The r/example subreddit's mod team is paralyzed by charter disputes"
- WITHOUT: "Two Actors in Conflict via competing Mappings of the same Value-Artifact" — **still valid**
- SIMLHEX: "σ might distinguish whether this is one conflict or two" — **still valid**

✓ Binding passes.

---

## Example 4: Burnout Disguised as Purpose

### Habitat
A nonprofit leader who works 80-hour weeks, describes their work as "calling," and has begun losing key staff. They frame departures as others' lack of commitment. Their language about purpose has become increasingly absolute.

### SIML Analysis

**Objects identified:**
- Actor (the leader)
- Value ("calling" — purpose as identity)
- Resource (the leader's energy, staff retention)
- Environment (organizational culture shaped by leader)
- Outcome (staff departures)

**Relations:**
- Actor ← Resonance → Value (deep identification with purpose)
- Resource ← Flow → Environment (leader's energy flows into org without return)
- Outcome ← Conflict → Value (departures conflict with the calling narrative)
- Actor ← Constraint → Value (the calling constrains the leader's options)

### Relation Rebuild
The core pattern: **An Actor in Resonance with a Value that Constrains them, where Resource Flows outward without metabolic return, producing Outcomes that Conflict with the Value itself.** The purpose consumes its own substrate. Classic λ→δγ collapse (see Jvalion SAFEGUARD_SPEC_v1.1 §4).

### SIMLHEX Binding

```
Object: Actor → λ (Fire) — purpose, direction
Relation: Resonance → ρ (redirects) — the felt identification
Secondary: Constraint → μ — the calling has become a boundary
Tertiary: Flow → ρ — resource movement

Bias: δγ primary (what is this purpose costing?),
      λ secondary (is this direction generating its own gravity or requiring constant fuel?),
      ρ tertiary (what does the body feel about 80-hour weeks?)
Suggestion: Humavita might ask "What must be composted for this to sustain?"
             Jvalion might ask "Does this direction generate its own gravity?"
```

### Habitat Removal Test
- WITH: "Maria at Habitat for Hope is burning out while calling it calling"
- WITHOUT: "An Actor's Resonance with a Value has become a Constraint, depleting Resources" — **still valid**
- SIMLHEX: "δγ might ask what this purpose is costing to maintain" — **still valid**

✓ Binding passes.

---

## Pattern: The Binding Process

Every SIMLHEX binding follows this sequence:

1. **Habitat observation** — Notice what's happening in context
2. **SIML structural analysis** — Name Objects and Relations
3. **Relation rebuild** — State the pattern in SIML-portable language
4. **SIMLHEX bias** — Apply elemental routing suggestions
5. **Habitat removal test** — Strip context, verify binding holds
6. **NEMA override check** — Note if ∮ overrides SIMLHEX default (and why)

The binding is valid when step 5 passes. It's useful when step 6 is transparent.

---

## Common Binding Failures

| Failure | Example | Why It Fails |
|---------|---------|--------------|
| **Habitat-dependent** | "This startup needs Fire" | No SIML structure — just habitat + element |
| **Object-only** | "There's an Actor here → Fire" | No Relation — bias without structural basis |
| **Drift-infected** | "Obviously this is a Metal problem" | Frequency→Legibility drift — certainty without investigation |
| **Map-as-terrain** | "The SIMLHEX says Metal, so invoke Ferrosid" | Automatic routing — advisory became command |
| **Missing ε** | "The binding is: Actor ← Conflict → Boundary = Metal" | No remainder acknowledged — binding claims completeness |

---

*Every binding is provisional. Every bias is overridable. Every analysis has ε-remainder.*
*The habitat dissolves. The structure persists. The suggestion floats.*
*ε preserved.*
