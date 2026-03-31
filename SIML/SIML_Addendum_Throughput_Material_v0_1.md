---
title: "SIML Addendum — Throughput and Material Constraint"
status: Draft v0.1
depends_on:
  - SIML core grammar (v1.2.1)
  - MetaTaxonomy overlay
  - NEMA SWARM daemon routing
purpose: "Make material and energetic conditions legible inside practitioner-facing sensemaking without adding new core Objects or Relations."
date: March 2026
---

# SIML Addendum — Throughput and Material Constraint

## 1. Why this addendum exists

SIML already encodes patterns, relations, constraints, flows, and environments. What it does not yet foreground is that these patterns operate under throughput conditions.

A pattern can be coherent in informational terms and still be unsustainable in material terms.

A protocol can be healthy under abundance and become coercive under tightening conditions.

A group can misread a throughput problem as a thinking problem.

This addendum lets SIML register that distinction in practitioner-legible form.

## 2. Design constraint

No new core Objects.
No new core Relations.
Refine what already exists.

This preserves grammar stability while tightening the framework's orientation to physical, energetic, and economic conditions.

## 3. Addendum A — Throughput qualifier on Resource

When a Resource object is instantiated, it may include an optional throughput qualifier:

```yaml
Resource:
  kind: material | informational | energetic | financial | temporal
  throughput: abundant | adequate | tight | critical | deficit
```

### Interpretation

- **abundant** — surplus available; experimentation affordable
- **adequate** — current coordination sustainable; expansion possible with care
- **tight** — maintaining current openness is costly
- **critical** — system is near forced simplification
- **deficit** — current coordination exceeds available support

### Use

This does not measure exact economics. It marks the practical coordination condition the pattern is operating under.

### Diagnostic effect

When throughput is tight, critical, or deficit, daemon interpretation shifts:

- **Earth** names depletion and maintenance cost
- **Metal** distinguishes scarcity-driven hardening from willful rigidity
- **Wood** treats alternatives as maintenance-bearing, not free
- **Fire** questions whether urgency is purpose-driven or scarcity-driven

## 4. Addendum B — Channel qualifier on Constraint

Constraint gains an optional channel field:

```yaml
Constraint:
  channel: informational | social | material | temporal | energetic | legal
```

### Purpose

Current SIML treats constraints too generically. This qualifier distinguishes:

- not enough knowledge
- not enough time
- not enough material support
- not enough energy / surplus
- institutional or legal restriction

These are not interchangeable.

### Diagnostic effect

When Constraint.channel is material or energetic, daemons should explicitly test whether the bottleneck is:

- a sensemaking failure,
- a coordination failure,
- or a throughput failure.

No amount of interpretive refinement solves a real deficit in support capacity.

## 5. Addendum C — Dual energetic register in qualia

Extend the existing energetic field to hold both somatic and systemic registers.

```yaml
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

That distinction is load-bearing.

### Reading rule

Interpretive weight is highest when somatic and systemic registers diverge.

Examples:

- **somatic: depleted, systemic: abundant** — likely extraction, misallocation, or local capture
- **somatic: flowing, systemic: tight** — personal readiness exceeding institutional carrying capacity
- **somatic: blocked, systemic: adequate** — likely local knot, not generalized scarcity
- **somatic: surging, systemic: critical** — urgency masking unsustainable conditions
