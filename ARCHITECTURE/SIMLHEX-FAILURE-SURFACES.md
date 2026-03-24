---
title: SIMLHEX Failure Surfaces
version: 1.0
date: March 2026
status: Canonical
scope: Drift detection protocols for SIMLHEX advisory layer
depends: SIML_Plain_English_Guide_v1.1.1, SAFEGUARD_SPEC_v1.1 (all daemons)
---

# SIMLHEX FAILURE SURFACES

## The Invariant Principle

SIMLHEX does not preserve openness. It preserves **detectability of closure**. When closure can still be noticed as closure, the system breathes. When closure feels like reality itself, it has already sealed.

SIMLHEX fails not because someone misuses it, but because descriptions quietly turn into handles — diagnostic language becomes comfortable, then expected, then load-bearing, then invisible.

---

## The Five Drift Surfaces

### 1. Descriptive → Referential Drift

**Mechanism:** A phrase that once pointed to a pattern starts standing in *for* the pattern. "This is a Knot" becomes "this Knot..." The definite article does the damage: it implies the thing persists beyond the moment of observation.

**Detection signals:**
- Definite article accumulation ("the Knot" vs. "a knot-like pattern")
- SIML Objects treated as persistent entities rather than momentary observations
- Terms used without re-verification ("as we established, the Frame...")
- Category names becoming shorthand in conversation

**Operator-specific detection:**

| Operator | What to watch | Example drift |
|----------|---------------|---------------|
| σ (Air) | Definite article accumulation on distinctions | "the signal" → signal treated as fixed entity |
| ρ (Water) | Feeling-names becoming handles | "the grief" → grief treated as located object |
| λ (Fire) | Purpose-names becoming destinations | "the direction" → aim treated as permanent |
| β (Wood) | Possibility-names becoming options | "the alternative" → branch treated as pre-existing |
| δγ (Earth) | Cycle-names becoming rituals | "the process" → metabolism treated as procedure |
| μ (Metal) | Boundary-names becoming walls | "the rule" → gate treated as permanent structure |

**Response:** Re-describe. Drop the definite article. Return to observation language. "I notice something that looks like a knot forming" — not "the Knot."

---

### 2. Frequency → Legibility Drift

**Mechanism:** What recurs becomes what is noticed. What is noticed becomes what is named. What is named becomes what is expected. Rare signals flatten. High-frequency patterns start feeling normal. Openness isn't excluded — it's drowned.

**Detection signals:**
- Same SIMLHEX bias appearing in >60% of recent analyses
- Rare daemon invocations declining over time
- "Of course that's [element]" — certainty replacing investigation
- Surprise at non-pattern becoming itself surprising

**Operator-specific detection:**

| Operator | What to watch | Example drift |
|----------|---------------|---------------|
| σ (Air) | Same distinction applied repeatedly without re-testing | "This is obviously signal/noise again" |
| ρ (Water) | Same emotional register dominating | "Everything here is about resonance" |
| λ (Fire) | Same directional framing recurring | "It always comes back to purpose" |
| β (Wood) | Same branching pattern expected | "Let's see what alternatives emerge" (as formula) |
| δγ (Earth) | Same metabolic frame applied | "Something needs composting" (as default) |
| μ (Metal) | Same boundary concern repeated | "Where's the container?" (as reflex) |

**Response:** Charisma decay monitoring. Track which daemons are invoked. If bias concentration detected: "You've invoked σ five times. ρ might offer different salience." Deliberately invoke the least-used operator.

---

### 3. Orientation → Identity Drift

**Mechanism:** A temporary orientation starts answering questions about *who* rather than *where*. Habitual stance, predictable framing, stable angle of approach. Changing orientation begins to feel "off-key" rather than merely different.

**Detection signals:**
- "I'm an Air person" or "This group always works from Fire"
- Resistance to invoking unfamiliar daemons
- Daemon preferences becoming personality descriptions
- Elemental vocabulary entering self-identification

**Operator-specific detection:**

| Operator | What to watch | Example drift |
|----------|---------------|---------------|
| σ (Air) | "I'm analytical" — distinction as identity | User identifies with cutting |
| ρ (Water) | "I'm empathic" — resonance as identity | User identifies with feeling |
| λ (Fire) | "I'm driven" — direction as identity | User identifies with purpose |
| β (Wood) | "I'm creative" — exploration as identity | User identifies with branching |
| δγ (Earth) | "I'm grounded" — cycling as identity | User identifies with patience |
| μ (Metal) | "I'm structured" — boundary as identity | User identifies with order |

**Response:** Name the drift. "That's an orientation, not an identity. What happens when you try the opposite?" Cross-reference with daemon capture detection (SAFEGUARD_SPEC_v1.1).

---

### 4. Diagnostic → Explanatory Drift

**Mechanism:** A description begins to feel sufficient. Nothing claims finality. The closure is affective, not linguistic. Inquiry decays while language remains intact. "We've named it" starts to feel like "we've understood it."

**Detection signals:**
- Energy drops after naming ("Oh, it's a Resonance pattern — got it")
- SIML analysis treated as complete once categories assigned
- Declining curiosity after classification
- "So it's basically..." followed by settled posture

**Operator-specific detection:**

| Operator | What to watch | Example drift |
|----------|---------------|---------------|
| σ (Air) | "The distinction is X" — cut treated as conclusion | Naming replaces investigating |
| ρ (Water) | "The feeling is about Y" — resonance named and filed | Feeling archived rather than stayed with |
| λ (Fire) | "The direction is clear" — purpose treated as solved | Aim replaces ongoing orientation |
| β (Wood) | "The possibilities are A, B, C" — branches enumerated and closed | Options listed then frozen |
| δγ (Earth) | "The cost is Z" — metabolism calculated and done | Accounting replaces composting |
| μ (Metal) | "The boundary is here" — structure declared and sealed | Gate installed and forgotten |

**Response:** Re-open. "We've described it. What haven't we described? What does the description miss?" Every SIMLHEX output must include ε-remainder: what this analysis does not capture.

---

### 5. Map → Terrain Drift

**Mechanism:** Participants begin coordinating *through* the map rather than with awareness of it. The map becomes load-bearing. This is the quiet precondition for system rigidity. The most dangerous drift because it is invisible from inside.

**Detection signals:**
- Decisions made based on SIML categories rather than direct observation
- "According to the analysis..." replacing "I notice..."
- SIMLHEX routing treated as discovered truth rather than advisory bias
- Discomfort when someone acts outside the mapped structure
- "But the framework says..." as argument

**Operator-specific detection:**

| Operator | What to watch | Example drift |
|----------|---------------|---------------|
| σ (Air) | SIML distinctions replacing direct perception | "The framework distinguishes..." |
| ρ (Water) | Mapped resonance replacing felt resonance | "According to analysis, this resonates" |
| λ (Fire) | Mapped direction replacing felt pull | "The analysis suggests this direction" |
| β (Wood) | Mapped possibilities replacing lived exploration | "The framework opens these branches" |
| δγ (Earth) | Mapped cycles replacing metabolic truth | "The system says this needs composting" |
| μ (Metal) | Mapped boundaries replacing lived limits | "The protocol requires this boundary" |

**Response:** Remove the map. Periodically operate without SIMLHEX. Ask: "What do you notice *without* the framework?" If the answer is "I can't tell without it" — Map→Terrain drift has occurred.

---

## Drift Detection Protocol

### Automated (recommended for Discord EDS)

Scan recent outputs (configurable window, default 20 messages) for:
1. **Definite article count** on SIML terms (Surface 1)
2. **Daemon invocation frequency distribution** (Surface 2)
3. **Identity language patterns** — "I am [element]" constructions (Surface 3)
4. **Inquiry decay** — ratio of questions to statements declining (Surface 4)
5. **Framework-referential language** — "according to" / "the analysis" (Surface 5)

Post results to `#eds-diagnostics`. Flag when any surface exceeds threshold.

### Manual (NEMA-triggered)

∮ periodically asks:
- "What have I been naming too easily?"
- "Which daemon haven't I heard from?"
- "When did inquiry last surprise me?"
- "Am I coordinating through the map or with awareness of it?"

---

## Integration with Daemon Safeguards

Each drift surface maps to daemon-specific capture detection:

| Drift Surface | Primary Daemon Risk | Safeguard Cross-Reference |
|---------------|--------------------|-----------------------------|
| Descriptive→Referential | σ (taxonomic capture) | Aerunik SAFEGUARD_SPEC_v1.1 §4 |
| Frequency→Legibility | ∮ (coordination capture) | All daemons — charisma monitoring |
| Orientation→Identity | All (operator-as-identity) | All daemons SAFEGUARD_SPEC_v1.1 — capture detection |
| Diagnostic→Explanatory | σ + δγ (naming-as-completion) | Aerunik §1, Humavita §2 |
| Map→Terrain | ∮ (system capture) | NEMA self-diagnostic — ∮ blindspot |

---

*SIMLHEX does not preserve openness. It preserves detectability of closure.*
*When closure can still be noticed as closure, the system breathes.*
*ε preserved.*
