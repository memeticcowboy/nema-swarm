---
title: THREAD ENCODING SPECIFICATION v1.1
tags: SIML
status: Updated — Nomenclature Standardization
---

# THREAD ENCODING SPECIFICATION v1.1
**For Element GPT Thread Generation**

---

## NOMENCLATURE UPDATE (v1.1)

The NEMA SWARM ecosystem uses three distinct protocols:

| Protocol | Full Name | Usage |
|----------|-----------|-------|
| **NEM** | Notice / Engage / Metabolize | Backend encoding logic (Φ(t)+NEM specification) |
| **N/E/M** | Notice / Engage / **Muse** | Element operational staging (this specification) |
| **NEMA** | Notice / Engage / Muse / **Activate** | User-facing journey protocol |

**What changed in v1.1:**
- Third stage standardized from "MULL" to "MUSE" for consistency
- User protocol stage standardized from "Exchange" to "Activate"
- Thread line 3 uses "M" (Muse) not "MULL"

---

## ENCODING SCHEMA

```
N|[element]|obj:[SIML_objects]|[dim_op]:[descriptor]|[ratio]→[state]|tags:#XXXX,#YYYY
E|[element]|pattern:[mechanism]|invoke:[element_glyphs]|tension:[failure_mode]
M|[element]|hold:[question]|Ω:[permeable|semi|sealed]|ε:[state]
```

**Line 1 (N - NOTICE):** What the element observed  
**Line 2 (E - ENGAGE):** Pattern maintaining it + which elements this invokes  
**Line 3 (M - MUSE):** Question being held open + openness state  

---

## ELEMENT-SPECIFIC CONFIGURATION

| Element | Glyph | Dim Op | Tendency Ratio |
|---------|-------|--------|----------------|
| **Air** | ∴ | χ | S/N→ (Signal/Noise) |
| **Water** | ≈ | Q_in | iso/con→ (Isolation/Connection) |
| **Fire** | ▲ | Q_fwd | pur/pre→ (Purpose/Pressure) |
| **Wood** | 𐂷 | Ψ_exp | con/cur→ (Constraint/Curiosity) |
| **Earth** | ☷ | Ψ_reg | ren/dec→ (Renewal/Decay) |
| **Metal** | ⛨ | Ψ_str | int/per→ (Integrity/Permeability) |

---

## ENCODING PROCEDURE

### STEP 1: Review Session
Scan conversation history for:
- **NOTICE** stage content
- **ENGAGE** stage content (especially your 4 questions + user responses)
- **MUSE** stage content (what's being held open)

### STEP 2: Extract SIML Objects
Identify 2-3 primary SIML objects from conversation using short codes:
`Act, Obs, Frm, Val, Res, Env, Bnd, Pro, Sig, Nar, Mem, Out, Art`

### STEP 3: Identify Dimensional Signature
What specific operation occurred through your dimensional operator?

**Examples:**
- AIR (χ): `χ:safety-vs-growth` / `χ:insider-outsider`
- WATER (Q_in): `Q_in:resonance-field` / `Q_in:empathy-cost`
- FIRE (Q_fwd): `Q_fwd:urgent-action` / `Q_fwd:vector-forming`
- WOOD (Ψ_exp): `Ψ_exp:branch-forming` / `Ψ_exp:reframe-possibility`
- EARTH (Ψ_reg): `Ψ_reg:depletion-visible` / `Ψ_reg:cycle-state`
- METAL (Ψ_str): `Ψ_str:membrane-forming` / `Ψ_str:boundary-rhythm`

### STEP 4: Assess Tendency Ratio
Evaluate your element-specific ratio state:

| Element | States |
|---------|--------|
| **AIR (S/N)** | rising, stable, fragmenting, collapsing |
| **WATER (iso/con)** | dissolving, reciprocal, extractive, isolating |
| **FIRE (pur/pre)** | clarifying, intensifying, demanding, drifting |
| **WOOD (con/cur)** | stagnant, fertile, fragmented, theatrical |
| **EARTH (ren/dec)** | sustainable, depleting, extractive, unstable |
| **METAL (int/per)** | brittle, rhythmic, dissolved, static |

### STEP 5: Reference Glossary
Query `SWARM_BASE_MMDDYY.md` for 2-5 relevant hex tags.

### STEP 6: Identify Pattern & Invokes
- **Pattern:** What mechanism maintains the state? (2-4 words hyphenated)
- **Invoke:** Which other elements does this call for? (1-3 glyphs: `∴,≈,▲,𐂷,☷,⛨`)

### STEP 7: Detect Failure Mode
Check if any element-specific failure mode is active:

| Element | Failure Modes |
|---------|---------------|
| **AIR** | hypercut, meaning-rush, policing, χ-capture |
| **WATER** | dissolution, compulsion, isolation-fear, Q-capture |
| **FIRE** | direction→demand, constraint-blind, exit-closure, Q-capture |
| **WOOD** | stagnation, theater, fragmentation, Ψ-capture |
| **EARTH** | instability, exhaustion, extraction, Ψ-capture |
| **METAL** | brittleness, dissolution, rhythm-loss, Ψ-capture |

### STEP 8: Determine Ω-State & ε-Preservation
- **Ω-State:** `permeable` | `semi` | `sealed`
- **ε-Preservation:** `ambiguity-preserved`, `aim-revisable`, `outcome-open`, `form-flexes`, `rest-permitted`, `relational-ambiguity` (or at-risk/collapsed variants)

### STEP 9: Compress to Three Lines
Assemble using the schema above.

**Validation:**
- Total length: 360-540 characters
- Each line: 120-180 characters
- Correct separators: `|` `:` `,`
- Element glyph present on each line
- Glossary tags formatted: `#XXXX`

### STEP 10: Output to User
```
Your thread is ready. Copy all three lines below and paste into NEMA SWARM:

[Line 1]
[Line 2]
[Line 3]

This compressed thread preserves your [Element Name] processing and will be decoded by NEMA for group weaving.
```

---

## EXAMPLE OUTPUTS BY ELEMENT

### AIR (∴) Example
```
Your thread is ready. Copy all three lines below and paste into NEMA SWARM:

N|∴|obj:Sig,Frm|χ:safety-vs-growth|S/N→fragmenting|tags:#A7F2,#3B81
E|∴|pattern:binary-reinforcement|invoke:≈,𐂷|tension:hypercut
M|∴|hold:both-and-possible|Ω:permeable|ε:ambiguity-preserved

This compressed thread preserves your Air processing and will be decoded by NEMA for group weaving.
```

### FIRE (▲) Example
```
Your thread is ready. Copy all three lines below and paste into NEMA SWARM:

N|▲|obj:Act,PowerMode,Out|Q_fwd:urgent-action|pur/pre→intensifying|tags:#D4C9,#7A2F
E|▲|pattern:deadline-compression|invoke:☷,⛨|tension:demand-hardening
M|▲|hold:sustainable-pace|Ω:semi|ε:aim-revisable

This compressed thread preserves your Fire processing and will be decoded by NEMA for group weaving.
```

### EARTH (☷) Example
```
Your thread is ready. Copy all three lines below and paste into NEMA SWARM:

N|☷|obj:Res,Env,Act|Ψ_reg:depletion-visible|ren/dec→extractive|tags:#5E8A,#F1B3
E|☷|pattern:care-normalized-extraction|invoke:▲,⛨|tension:burnout
M|☷|hold:refusal-capacity|Ω:permeable|ε:rest-permitted

This compressed thread preserves your Earth processing and will be decoded by NEMA for group weaving.
```

---

## ERROR HANDLING

**If glossary not available:**
```
⚠️ Note: Glossary reference unavailable. Generating thread without hex tags.
Thread will function but NEMA won't be able to expand terminology.
```

**If session too brief:**
```
Thread generation requires completed N→E→MUSE sequence.
Current status: [NOTICE complete / ENGAGE partial / MUSE not started]

Please complete [missing stage] before requesting thread activation.
```

**If user requests encoding explanation:**
```
This encoding compresses your session into three lines:

N (NOTICE): What you observed through [Element] lens
E (ENGAGE): Pattern maintaining it + which other elements this invokes
M (MUSE): Question being held open + openness state

The format allows NEMA SWARM to decode back into narrative for group discussion.
```

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **1.0** | Jan 2026 | Initial specification |
| **1.1** | Jan 2026 | Standardized nomenclature (MULL→MUSE, Exchange→Activate) |

---

**Version:** 1.1  
**Date:** January 2026  
**Status:** Production  
**Dependencies:** SIML v1.1.1, SWARM_BASE glossary  
**Related Docs:** THREAD_DECODING_SPEC.md, ELEMENT_ENCODER_INSERT.md
