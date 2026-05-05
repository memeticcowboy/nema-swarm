# Descriptive Analytics — NEMAtic Insight

## Source Caveat

Descriptive Analytics has no dedicated Wikipedia article as of this encoding (2026-05-04). The canonical-source position is filled instead by:

- Wikipedia's *Prescriptive Analytics* article, which describes descriptive as "examining historical performance through data mining to identify reasons behind past outcomes"
- Wikipedia's *Analytics* article, which lists descriptive among five analytics types (descriptive, diagnostic, predictive, prescriptive, cognitive) without elaboration
- Canonical field knowledge: data warehousing, OLAP, KPI dashboards, BI, data mining, statistical summary methods

This encoding should be re-grounded against a canonical source if one becomes available. The `needs_research: true` flag in term.yaml carries this caveat forward.

## What Descriptive Analytics Does

Descriptive analytics is the foundational phase of the analytics triad. It takes historical data — event streams, transactions, measurements, logs — and produces structured summaries that make the past legible. Concretely, this includes:

- **Aggregation**: counts, sums, averages, percentiles, distributions over chosen dimensions
- **KPIs**: metrics elevated to operational significance (revenue per quarter, defect rate per shift, churn per cohort)
- **Dashboards**: integrated visual surfaces showing multiple metrics in context
- **OLAP cubes**: multi-dimensional structures supporting slice-and-dice exploration
- **Data mining**: pattern extraction (clustering, association, anomaly detection) surfacing relationships not visible in flat queries
- **Statistical summary**: central tendencies, variance, distribution shape

The output is what the organization sees when it looks back at itself.

## Position in the Triad

| Phase | Question | Operator | NEMA frame |
|-------|----------|----------|-----------|
| **Descriptive (Z009)** | **What happened?** | **μ (form)** | **structure crystallized from history** |
| Predictive (Z008) | What will happen? | σ (selection) | projection without commitment |
| Prescriptive (Z010) | What should we do? | Ω∘λ (closure ∘ decision) | participatory loop-closure |

Descriptive sits at the foundation. Without it, predictive analytics has no historical-pattern surface from which to extrapolate, and prescriptive analytics has no substrate to close upon. Every higher layer of the analytics stack depends on the form-extraction this layer performs.

## Why μ (form) Is the Right Operator

μ is the operator of structure, boundary, crystallization — the move from continuous flow to discrete form. Descriptive analytics is fundamentally a form-extraction operation: it takes the formless flow of raw events and produces forms (metrics, charts, summaries) that can be reasoned about.

The other operators don't fit:
- σ (selection) is the predictive cut — descriptive doesn't yet project
- λ (decision) requires forward commitment — descriptive doesn't act
- ρ (resonance) is field-level — descriptive operates on bounded historical scope
- Ω (closure) requires loop-completion — descriptive is one stage of a larger loop

μ captures what's distinctive: the act of giving discrete, communicable form to event-streams that were previously formless to the organization.

## The Selection Problem

Descriptive analytics is often experienced as objective — "this is what happened" — but is in fact deeply selection-laden. Each metric is a choice; each dimension is a choice; each aggregation window is a choice. The dashboard shows what was selected to be shown. What goes uncomputed is also what goes unseen.

This invisibility is structural. Consumers of dashboards rarely interrogate the choices that produced the metrics — they treat the output as the fact rather than the rendering of the fact. NEMAtically, this is the descriptive frame's quiet ε-content: the "should" of "what should we measure" has already been smuggled in by the time anyone reads the dashboard. The descriptive layer presents itself as ε-free, but it is built on prior prescriptions about measurement.

## Connection to Business Intelligence

Descriptive analytics overlaps heavily with business intelligence but is not identical:

- **BI** emphasizes the *operational surfacing* of analytical output — the dashboard, the report, the executive summary, the data-democratization tooling
- **Descriptive analytics** emphasizes the *analytical operations* themselves — the aggregations, the data mining, the statistical methods

The relationship: descriptive analytics produces what BI presents. They are co-evolutionary in practice but theoretically distinguishable. Most operational data teams use the terms interchangeably, which obscures this distinction without doing real harm except when one wants to discuss the layer separately from its presentation.

## The Diagnostic Boundary

The Wikipedia *Analytics* article distinguishes descriptive from diagnostic analytics — descriptive answers "what happened" while diagnostic answers "why did it happen." In practice the boundary is fluid: data mining surfaces patterns that strongly suggest causal structure, and dashboard drill-downs are often used diagnostically.

For NEMAtic purposes, descriptive and diagnostic both operate under μ at the framework scale. The diagnostic operation is descriptive-with-causal-questioning, but the underlying operator is still form-extraction from historical data. A separate Z-term for diagnostic analytics could be encoded later if useful — Z reserved range still has Z004–Z007 available.

## Connection to the NEMA Loop

In the NEMA loop (σ→ρ→λ→μ→Ω), descriptive analytics maps to **μ**. Within the loop's flow, μ is the structure-giving stage that follows σ→ρ→λ — but at the framework-scale we are encoding here, descriptive analytics is the *substrate* over which the entire loop operates. The fractal pattern: each loop iteration includes descriptive moments (form-giving) at multiple scales.

This is consistent with the NEMA framework's recursive structure — operators don't appear only once at one scale, but recur at every scale where the loop can be read.

## Closure Property

Descriptive's z_state is **closed-historical**, distinct from prescriptive's **integrating** closure. The past is closed because it has already happened — descriptive analytics does not alter it, only renders it. This is structurally different from prescriptive closure, which closes the *future* loop by committing to action. Both are closures; they operate at different ends of the temporal axis.

Predictive (Z008) sits between them as **open** — neither historically closed (because it speaks of unknowns) nor participatory-closed (because it does not commit).

## ε Note

Descriptive analytics is the layer where ε is *most plausibly excluded* from the formal frame, but as noted in the Selection Problem section above, ε enters silently through the choice of what to measure. The ε is one step removed: not in the descriptive output itself, but in the prior prescription about which descriptive outputs to compute.

This is worth flagging because organizations often mistake descriptive analytics for objective ground truth. The ground is not truth — it is selected representation of truth, with all the ε-content that selection carries.

## ∮ Foundation Note

Descriptive Analytics is the analytics frame's first eyes. Before any prediction or prescription, the frame must have a way of *seeing what was*. Descriptive is that seeing. The triad on disk now reads:

- Z009 — Descriptive Analytics — μ — what happened (form)
- Z008 — Predictive Analytics — σ — what will (projection)
- Z010 — Prescriptive Analytics — Ω∘λ — what should (closure)

Three terms, one triad. Each requires the layer below; each is required by the layer above. The Z-series now carries the framework's analytics taxonomy as a coherent unit.
