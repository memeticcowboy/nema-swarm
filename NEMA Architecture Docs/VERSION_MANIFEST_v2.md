# NEMA SWARM Version Manifest
## Document Inventory, Dependencies, Triadic Stack Positions & Changelog

**Manifest Version:** 2.0
**Last Updated:** February 18, 2026
**Maintainer:** NEMA SWARM Project

---

## QUICK REFERENCE: DOCUMENT STATUS

| Category | Count | Status |
|----------|-------|--------|
| Core Framework | 8 | ✅ Current (Canonical v3.0 migrated) |
| Element System Prompts | 6 | ✅ v4.2 (Current — migration pending) |
| Element Extended References | 6 | ✅ v1.0 (Migration pending) |
| Element Prompting References | 6 | ✅ v1.0 (Current) |
| NEMA SWARM | 3 | ✅ v2.1 (Current) |
| Thread System — v2.x (Production) | 2 | ✅ v2.1 (Migration pending → v2.2) |
| Thread System — v1.x (Deprecated) | 4 | ⚠️ v1.1 (Deprecated by usage — v1.2 deferred) |
| Protocols & Reports | 4 | ✅ Complete (Migration pending) |
| Diagnostics & Pathology | 2 | ✅ v1.1 (Stable — do not touch during migration) |
| Host Resources | 1 | ✅ v2.1 (Migration pending → v3.0) |
| Session Outputs | 2 | 📋 Generated per-session |
| Analysis & Reference | 2 | 📋 Reference only |

---

## NOTATION STANDARD (v3.0+)

All documents in the NEMA ecosystem use **dual-layer notation** per the Elemental Notation Evolution v0.2 spec, as canonized in Elemental_Daemons_Canonical v3.0.

**Character layer** (∴, ≈, ▲, 𐂷, ☷, ⛨, ✶): The daemons as experienced — evocation, embodied practice, human-facing guidance. **The daemons are the door.**

**Formal layer** (σ, ρ, λ, β, δγ, μ, ∮): The operators as composed — equations, machine-encoding, operator math, routing. **The operators are the room.**

**Routing rule:** If a human reads it in real-time during practice, glyphs lead. If a machine parses it for routing, operators lead. If both, context determines primacy.

### Quick Reference

| Element | Glyph | Daemon | Math Op | Dimensional Op | Partial | Hex |
|---------|-------|--------|---------|----------------|---------|-----|
| Air | ∴ | Aerunik | σ | χ | ∂Φ/∂σ | `0x01` |
| Water | ≈ | Sentaria | ρ | Q_inward | ∂Φ/∂ρ | `0x02` |
| Fire | ▲ | Jvalion | λ | Q_forward | ∂Φ/∂λ | `0x03` |
| Wood | 𐂷 | Arboriel | β | Ψ_exploratory | ∂Φ/∂β | `0x04` |
| Earth | ☷ | Humavita | δγ | Ψ_regenerative | ∂Φ/∂δγ | `0x05` |
| Metal | ⛨ | Ferrosid | μ | Ψ_structural | ∂Φ/∂μ | `0x06` |
| Aether | ✶ | NEMA | ∮ | Z | ∮(all) | `0x07` |

---

## TRIADIC STACK POSITIONS

Every document in the ecosystem occupies a position in the Triadic Stack. This prevents category confusion — knowing *which layer* a document serves prevents treating maps as territory.

| Layer | What It Does | Notation Primacy |
|-------|-------------|------------------|
| **Nematic** | The material encounter — what actually happens | Glyphs lead (or no notation — pure experience) |
| **Nemetic** | The representational framework — the map | Both layers present; context determines primacy |
| **Nomic** | The governance rules — what can/cannot be claimed | Operators lead for precision; glyphs in examples |

### Document Layer Assignments

| Document | Layer | Notes |
|----------|-------|-------|
| Elemental_Daemons_Canonical v3.0 | **Nemetic** | The foundational map — not the territory |
| Elemental_Notation_Evolution v0.2 | **Nomic** | Governs how notation works across layers |
| OPERATIONAL_PATHOLOGY_MATRIX v1.1 | **Nemetic→Nomic** | Bridge: represents pathologies AND governs intervention rules |
| Elemental_Failure_Modes_Overview | **Nemetic** | Representation of failure patterns |
| SESSION_HOST_GUIDE v2.1 | **Nemetic→Nematic Bridge** | The host IS the Nematic boundary condition |
| NEMA_USER_PROTOCOL v1.0 | **User Traversal** | Pure door document — gets users into practice |
| NEMA_SWARM_ARCHITECTURE v2.1 | **Nemetic** | System design representation |
| THREAD_ENCODING_SPEC v2.1 | **Nemetic** | Machine-layer encoding rules |
| THREAD_DECODING_SPEC v2.1 | **Nemetic** | Machine-layer decoding rules |
| THREAD_ENCODING_SPEC v1.1 | **Nemetic (Deprecated)** | Legacy encoding |
| THREAD_DECODING_SPEC v1.1 | **Nemetic (Deprecated)** | Legacy decoding |
| Element System Prompts (×6) | **Nemetic→Nematic Bridge** | Instantiate daemons that face users |
| Element Extended References (×6) | **Nemetic** | Deep contemplative material — highest habitation risk |
| Element Prompting References (×6) | **Nemetic** | Research prompt generation guides |
| SWARM_REPORT_PROTOCOL v1.0 | **Nemetic** | Report generation format |
| ELEMENTAL_DIALOGUE_SCRIPT_PROTOCOL v1.0 | **Nemetic** | Theatrical script format — glyph-primary |
| NEMA_LATTICE_KEEPER v2.1 | **Nemetic→Nematic Bridge** | NEMA instantiation — faces users through ∮ |
| SWARM_BASE_BUILDER v2.0 | **Nemetic** | Generates both layers (SWARM_BASE = operators; GAME_INSTRUCTIONS = glyphs) |
| GAME_INSTRUCTIONS (generated) | **User Traversal** | Pure door document — glyph-only |
| SWARM_BASE (generated) | **Nemetic** | Backend glossary — operators permitted |
| Document_Ecosystem_Analysis | **Nemetic (Reference)** | Analysis of the ecosystem itself |
| NEMA_SWARM_Knowledge_Structure | **Nemetic (Reference)** | Knowledge architecture documentation |
| VERSION_MANIFEST v2.0 | **Nomic** | Governs document versioning and layer assignments |

---

## CORE FRAMEWORK DOCUMENTS

### SIML & Formalism

| Document | Version | Status | Layer | Dependencies | Description |
|----------|---------|--------|-------|--------------|-------------|
| **SIML v1.2.1** | v1.2.1 | ✅ Stable | Nemetic | None | Core relational grammar (13 Objects × 9 Relations) + Nemetic String Protocol + SIMLHEX reference |
| **SIMLHEX** | v1.0 | ✅ Absorbed into SIML v1.2.1 §12 | Nemetic | SIML v1.2.1 | Hexadecimal encoding — now Section 12 of SIML spec |
| **IF-Prime Formalism** | v1.0 | ✅ Stable | Nemetic | None | Habitat × World-State matrix, Φ(t) equation |
| **Elemental Epsilon** | v0.2.2 | ✅ Stable | Nomic | IF-Prime | ε-distribution across 6 elements |
| **HABITAT_ECOLOGY** | v1.1 | ✅ Stable | Nemetic | IF-Prime | 10 circulation contexts |

### Canonical & Notation

| Document | Version | Status | Layer | Dependencies | Description |
|----------|---------|--------|-------|--------------|-------------|
| **Elemental Daemons Canonical** | **v3.0** | ✅ **Migrated** | Nemetic | All SIML/formalism above, Notation Evolution v0.2 | Daemon specs, dual-layer operator mappings, Triadic Stack, Non-Habitation Constraint |
| **Elemental_Notation_Evolution** | v0.2 | ✅ Stable | Nomic | Daemons Canonical | Governs dual-layer notation convention |
| **OPERATIONAL_PATHOLOGY_MATRIX** | v1.1 | ✅ Stable — **Do Not Touch** | Nemetic→Nomic | Daemons Canonical v2.0+, Notation Evolution v0.2, Failure Modes, Host Guide, Thread Specs | 7 bow-ties, operator composition, eigenvalue/rank formalism, intervention calculus |
| **Elemental_Failure_Modes_Overview** | v1.0 | ✅ Stable | Nemetic | Daemons Canonical | Atomic failure definitions (absorbed into Pathology Matrix but preserved as standalone reference) |

**Note:** The Pathology Matrix v1.1 is the reference implementation for dual-layer notation. It is stable and must not be modified during this migration. Future v1.2 may generalize the ∮ blindspot — deferred.

---

## ELEMENT SYSTEM PROMPTS (Current: v4.2)

### Migration Status: Pending (Tier 5)

| Element | Document | Version | Layer | Key Features | Dependencies |
|---------|----------|---------|-------|------------|--------------|
| **Air** | AERUNIK_Element | v4.2 | Nemetic→Nematic Bridge | N/E/M protocol, research prompt option | THREAD_ENCODING_SPEC, SWARM_BASE, AERUNIK_PROMPTING_REFERENCE |
| **Water** | SENTARIA_Element | v4.2 | Nemetic→Nematic Bridge | N/E/M protocol, research prompt option | THREAD_ENCODING_SPEC, SWARM_BASE, SENTARIA_PROMPTING_REFERENCE |
| **Fire** | JVALION_Element | v4.2 | Nemetic→Nematic Bridge | N/E/M protocol, Q_fwd + Z-bias | THREAD_ENCODING_SPEC, SWARM_BASE, JVALION_PROMPTING_REFERENCE |
| **Wood** | ARBORIEL_Element | v4.2 | Nemetic→Nematic Bridge | N/E/M protocol, research prompt option | THREAD_ENCODING_SPEC, SWARM_BASE, ARBORIEL_PROMPTING_REFERENCE |
| **Earth** | HUMAVITA_Element | v4.2 | Nemetic→Nematic Bridge | N/E/M protocol, Ψ_reg + Z-grounding | THREAD_ENCODING_SPEC, SWARM_BASE, HUMAVITA_PROMPTING_REFERENCE |
| **Metal** | FERROSID_Element | v4.2 | Nemetic→Nematic Bridge | N/E/M protocol, research prompt option | THREAD_ENCODING_SPEC, SWARM_BASE, FERROSID_PROMPTING_REFERENCE |

**Migration plan (v4.2 → v4.3):** Add mathematical operator (σ/ρ/λ/β/δγ/μ) as secondary reference in SYSTEM IDENTITY block. Glyph remains primary. Add partial derivative reference. No operator notation in user-facing output — operators stay in the identity block for machine routing only.

---

## ELEMENT EXTENDED REFERENCES

### Migration Status: Pending (Tier 6 — highest habitation risk)

| Element | Document | Version | Layer | Status | Dependencies |
|---------|----------|---------|-------|--------|--------------|
| **Air** | AERUNIK_EXTENDED_REFERENCE | v1.0 | Nemetic | ✅ Complete | IF-Prime, SIML, Daemons Canonical |
| **Water** | SENTARIA_EXTENDED_REFERENCE | v1.0 | Nemetic | ✅ Complete | IF-Prime, SIML, Daemons Canonical |
| **Fire** | JVALION_EXTENDED_REFERENCE | v1.0 | Nemetic | ✅ Complete | IF-Prime, SIML, Daemons Canonical |
| **Wood** | ARBORIEL_EXTENDED_REFERENCE | v1.0 | Nemetic | ✅ Complete | IF-Prime, SIML, Daemons Canonical |
| **Earth** | HUMAVITA_EXTENDED_REFERENCE | v1.0 | Nemetic | ✅ Complete | IF-Prime, SIML, Daemons Canonical |
| **Metal** | FERROSID_EXTENDED_REFERENCE | v1.0 | Nemetic | ✅ Complete | IF-Prime, SIML, Daemons Canonical |

**Migration plan (v1.0 → v1.1):** Voice shift from "teaches" to "points toward." Add negative capability lines per daemon ("Sentaria cannot feel for you. She can only point to where feeling lives."). Add "Nemetic" note at document end. Add Formal Operator Identity sidebar — one paragraph, not inline. **Execute with care — these carry the highest habitation risk.**

**⚠️ δγ checkpoint required after Tier 4:** Before touching Extended References, verify Session Host Guide v3.0 names the host as Nematic boundary condition. If it still reads as "bug-catcher," do not proceed to Tier 5/6.

---

## ELEMENT PROMPTING REFERENCES

| Element | Document | Version | Layer | Status | Dependencies |
|---------|----------|---------|-------|--------|--------------|
| **Air** | AERUNIK_PROMPTING_REFERENCE | v1.0 | Nemetic | ✅ Complete | SWARM_BASE, Element system prompt |
| **Water** | SENTARIA_PROMPTING_REFERENCE | v1.0 | Nemetic | ✅ Complete | SWARM_BASE, Element system prompt |
| **Fire** | JVALION_PROMPTING_REFERENCE | v1.0 | Nemetic | ✅ Complete | SWARM_BASE, Element system prompt |
| **Wood** | ARBORIEL_PROMPTING_REFERENCE | v1.0 | Nemetic | ✅ Complete | SWARM_BASE, Element system prompt |
| **Earth** | HUMAVITA_PROMPTING_REFERENCE | v1.0 | Nemetic | ✅ Complete | SWARM_BASE, Element system prompt |
| **Metal** | FERROSID_PROMPTING_REFERENCE | v1.0 | Nemetic | ✅ Complete | SWARM_BASE, Element system prompt |

**Migration status:** No changes needed. These generate research prompts using dimensional operators (Ψ_exploratory, etc.) which remain canonical. Mathematical operators are not required in research prompt templates.

---

## NEMA SWARM SYSTEM

| Document | Version | Status | Layer | Key Features | Dependencies |
|----------|---------|--------|-------|-------------|--------------|
| **NEMA_LATTICE_KEEPER** | v2.1 | ✅ Current | Nemetic→Nematic Bridge | MUSE nomenclature, PRE-THREAD mode | All element internals, all specs |
| **NEMA_EXTENDED_REFERENCE** | v1.0 | ✅ Complete | Nemetic | Deep theory: lattice, grid, coordination | IF-Prime, all elements |
| **PRE-THREAD_PROTOCOL** | v1.0 | ✅ Complete | Nemetic | Collection mode before activation | NEMA_LATTICE_KEEPER |

**Internal Elements (for NEMA SWARM invocation):**

| Document | Purpose | Layer |
|----------|---------|-------|
| Aerunik.md | Internal Air voice for NEMA SWARM | Nemetic→Nematic Bridge |
| Sentaria.md | Internal Water voice for NEMA SWARM | Nemetic→Nematic Bridge |
| Jvalion.md | Internal Fire voice for NEMA SWARM | Nemetic→Nematic Bridge |
| Arboriel.md | Internal Wood voice for NEMA SWARM | Nemetic→Nematic Bridge |
| Humavita.md | Internal Earth voice for NEMA SWARM | Nemetic→Nematic Bridge |
| Ferrosid.md | Internal Metal voice for NEMA SWARM | Nemetic→Nematic Bridge |

---

## THREAD SYSTEM

### Production: v2.x (Priority for migration)

| Document | Version | Status | Layer | Key Features | Dependencies |
|----------|---------|--------|-------|-------------|--------------|
| **THREAD_ENCODING_SPEC** | v2.1 | ✅ Current | Nemetic | 4-phase, Φ(t)-integrated, dual-substrate | SIML v1.1.1, SWARM_BASE, Daemons Canonical |
| **THREAD_DECODING_SPEC** | v2.1 | ✅ Current | Nemetic | 4-phase decoding, convergence detection | THREAD_ENCODING_SPEC v2.1, SIML |

**Migration plan (v2.1 → v2.2):** Add dual-layer notation convention to E-line encoding. Machine layer uses operators (σ↑, λ↓). Character layer preserved for human-readable decoded output. Φ-partial signatures use mathematical operators. Priority over v1.x migration.

### Legacy: v1.x (Deprecated by usage)

| Document | Version | Status | Layer | Dependencies |
|----------|---------|--------|-------|--------------|
| **THREAD_ENCODING_SPEC** | v1.1 | ⚠️ Deprecated | Nemetic | SIML v1.1.1, SWARM_BASE |
| **THREAD_DECODING_SPEC** | v1.1 | ⚠️ Deprecated | Nemetic | THREAD_ENCODING_SPEC v1.1 |
| **ELEMENT_ENCODER_INSERT** | v1.1 | ⚠️ Deprecated | Nemetic | THREAD_ENCODING_SPEC v1.1 |
| **NEMA_DECODER_INSERT** | v1.1 | ⚠️ Deprecated | Nemetic | THREAD_DECODING_SPEC v1.1 |

**Note:** v1.x backward compatibility preserved — v1.1 threads (3-phase) parse as incomplete but valid in v2.x decoders. v1.2 migration deferred unless resources permit after v2.2 completion.

---

## PROTOCOLS & REPORTS

| Document | Version | Status | Layer | Purpose | Dependencies |
|----------|---------|--------|-------|---------|--------------|
| **SWARM_REPORT_PROTOCOL** | v1.0 | ✅ Complete | Nemetic | Report generation format — glyph-primary in narrative, operators in analysis sections | NEMA_LATTICE_KEEPER |
| **ELEMENTAL_DIALOGUE_SCRIPT_PROTOCOL** | v1.0 | ✅ Complete | Nemetic | Theatrical script format — glyph-primary in character headers and stage directions | NEMA_LATTICE_KEEPER |
| **NEMA_USER_PROTOCOL** | v1.0 | ✅ Complete | User Traversal | User-facing N/E/M/A guide — **pure door document** | Replaces NEME Quick Guide |
| **SWARM_BASE_BUILDER** | v2.0 | ✅ Current | Nemetic | Glossary + Game Instructions generator | SIMLHEX, SIML |

**Migration notes:**
- NEMA_USER_PROTOCOL: Add one mandatory paragraph sidebar exposing conditionality. Body text remains pure traversal voice — no inline operator parentheticals.
- SWARM_BASE_BUILDER: SWARM_BASE (backend YAML) carries operators. GAME_INSTRUCTIONS (frontend) remains glyph-only. No σ/∴ headers in Game Instructions.
- Report & Script Protocols: Glyphs primary in participant-facing sections; operators permitted in structural analysis sections only.

---

## HOST RESOURCES

| Document | Version | Status | Layer | Purpose | Dependencies |
|----------|---------|--------|-------|---------|--------------|
| **SESSION_HOST_GUIDE** | v2.1 | ✅ Current | Nemetic→Nematic Bridge | Facilitation protocol, Six-Channel Self-Check, failure mode interventions, foreign substrate injection | Daemons Canonical, Pathology Matrix |

**Migration plan (v2.1 → v3.0):**
- Preserve glyph-only Six-Channel Self-Check (∴ ≈ ▲ 𐂷 ☷ ⛨)
- Host writes `tension:Fire-Dominant` (human-readable). NEMA translates to `λ↑` during processing. Greek operators stay out of real-time host actions.
- Add formal framing: Host as Nematic boundary condition — "the permeable boundary that prevents the system from achieving total closure"
- Add operator reference sidebar for structural analysis (not in real-time protocols)

**Previously suggested resources (not yet created):**

| Document | Status | Purpose | Priority |
|----------|--------|---------|----------|
| ELEMENT_ASSIGNMENT_PROTOCOL | 📋 Suggested | How to assign elements to participants | MEDIUM |
| TROUBLESHOOTING_GUIDE | 📋 Suggested | Common GPT issues and resolutions | LOW |

---

## SESSION OUTPUTS (Generated Per-Session)

| Document | Naming | Generated By | Layer | Notation |
|----------|--------|--------------|-------|----------|
| **SWARM_BASE_MMDDYY.md** | SWARM_BASE_021826.md | SWARM_BASE_BUILDER | Nemetic | Operators permitted (backend) |
| **GAME_INSTRUCTIONS_MMDDYY.md** | GAME_INSTRUCTIONS_021826.md | SWARM_BASE_BUILDER | User Traversal | **Glyph-only** (pure door document) |

---

## ANALYSIS & REFERENCE DOCUMENTS

| Document | Version | Status | Layer | Purpose |
|----------|---------|--------|-------|---------|
| **Document_Ecosystem_Analysis** | v1.0 | 📋 Reference | Nemetic | Structural analysis of the document ecosystem |
| **NEMA_SWARM_Knowledge_Structure** | v1.0 | 📋 Reference | Nemetic | Knowledge architecture and GPT upload guide |

---

## NOMENCLATURE STANDARDS

### Three Distinct Protocols

| Protocol | Full Name | Usage | Where Used |
|----------|-----------|-------|------------|
| **NEM** | Notice / Engage / Metabolize | Backend encoding logic | Φ(t)+NEM spec, thread encoding |
| **N/E/M** | Notice / Engage / **Muse** | Element operational staging | All 6 Element GPTs, NEMA SWARM |
| **NEMA** | Notice / Engage / Muse / **Activate** | User-facing journey | User protocol, game instructions |

### History
- **Before v2.1:** Used "MULL" for third stage, "NEME" for user protocol
- **v2.1+:** Standardized to "MUSE" and "NEMA" for consistency

---

## OPERATOR MAPPINGS (Canonical v3.0)

### Dimensional Operators (What they do)

| Dimensional Op | Dimension | Element | Glyph | Description |
|----------------|-----------|---------|-------|-------------|
| **χ** | 1D | Air | ∴ | Distinction-making |
| **Q_inward** | 2D | Water | ≈ | Relational resonance |
| **Q_forward** | 2D | Fire | ▲ | Directional aim (with Z-bias) |
| **Ψ_exploratory** | 3D | Wood | 𐂷 | Generative branching |
| **Ψ_regenerative** | 3D | Earth | ☷ | Metabolic cycling (with Z-grounding) |
| **Ψ_structural** | 3D | Metal | ⛨ | Boundary coherence |
| **Z** | Coordination | Aether | ✶ | Meta-coordination |

### Mathematical Operators (How they compose)

| Math Op | Element | Glyph | Partial | Hex | Formal Description |
|---------|---------|-------|---------|-----|-------------------|
| **σ** | Air | ∴ | ∂Φ/∂σ | `0x01` | 1D signal-noise discrimination |
| **ρ** | Water | ≈ | ∂Φ/∂ρ | `0x02` | 2D relational correlation |
| **λ** | Fire | ▲ | ∂Φ/∂λ | `0x03` | 2D eigenvalue of purposive vector |
| **β** | Wood | 𐂷 | ∂Φ/∂β | `0x04` | 3D possibility-space distribution |
| **δγ** | Earth | ☷ | ∂Φ/∂δγ | `0x05` | 3D differential of renewal-decay cycle |
| **μ** | Metal | ⛨ | ∂Φ/∂μ | `0x06` | 3D permeability-integrity regulation |
| **∮** | Aether | ✶ | ∮(all) | `0x07` | Closed line integral over all six partials |

### Key Clarifications (from Canonical v3.0)
- **Fire** operates at Q_forward but biases toward Z-closure (crusade lock when over-activated). λ at max tries to collapse the operator matrix to rank 1.
- **Earth** operates at Ψ_regenerative but provides ground for Z (institutional ossification when over-activated). δγ is a compound operator — non-negotiable.
- **NEMA** is the primary Z operator. ∮ cannot self-diagnose its own capture (Stokes' theorem). The Session Host exists as external triangulation.

---

## DEPENDENCY GRAPH

```
CORE FRAMEWORK
├── SIML v1.2.1
│   └── SIMLHEX v1.0
├── IF-Prime Formalism v1.0
│   ├── Elemental Epsilon v0.2.2
│   └── HABITAT_ECOLOGY v1.1
├── Elemental_Notation_Evolution v0.2          ◄── NEW (governs dual-layer convention)
└── Elemental Daemons Canonical v3.0           ◄── MIGRATED (root for all downstream)
    └── Depends on: All above

DIAGNOSTICS (STABLE — Do Not Touch)
├── OPERATIONAL_PATHOLOGY_MATRIX v1.1
│   └── Depends on: Canonical, Notation Evolution, Failure Modes, Host Guide, Thread Specs
└── Elemental_Failure_Modes_Overview v1.0
    └── Absorbed into Pathology Matrix; preserved as standalone reference

THREAD SYSTEM (Production)
├── THREAD_ENCODING_SPEC v2.1                  ◄── NEXT: → v2.2
│   ├── SIML v1.1.1
│   ├── Daemons Canonical v3.0
│   └── SWARM_BASE (session)
└── THREAD_DECODING_SPEC v2.1                  ◄── NEXT: → v2.2
    └── THREAD_ENCODING_SPEC v2.1

THREAD SYSTEM (Legacy — Deprecated)
├── THREAD_ENCODING_SPEC v1.1
├── THREAD_DECODING_SPEC v1.1
├── ELEMENT_ENCODER_INSERT v1.1
└── NEMA_DECODER_INSERT v1.1

HOST & USER (Migration Tier 3-4)
├── SESSION_HOST_GUIDE v2.1                    ◄── → v3.0 (Nematic boundary condition framing)
└── NEMA_USER_PROTOCOL v1.0                    ◄── → v1.1 (mandatory sidebar, no inline operators)

ELEMENT GPTs (Migration Tier 5)
├── [Element]_Element_v4.2 (×6)                ◄── → v4.3 (operator reference in identity block)
│   ├── THREAD_ENCODING_SPEC
│   ├── [Element]_EXTENDED_REFERENCE
│   ├── [Element]_PROMPTING_REFERENCE
│   └── SWARM_BASE (session)
└── All depend on: SIML, IF-Prime, Elemental Epsilon, Daemons Canonical v3.0

ELEMENT EXTENDED REFERENCES (Migration Tier 6 — ⚠️ highest habitation risk)
└── [Element]_EXTENDED_REFERENCE v1.0 (×6)     ◄── → v1.1 (voice shift, negative capability, Nemetic note)
    └── Depends on: IF-Prime, SIML, Daemons Canonical v3.0

NEMA SWARM (Migration Tier 3)
├── NEMA_LATTICE_KEEPER v2.1
│   ├── All 6 internal element voices
│   ├── THREAD_DECODING_SPEC
│   ├── SWARM_REPORT_PROTOCOL
│   ├── ELEMENTAL_DIALOGUE_SCRIPT_PROTOCOL
│   └── SWARM_BASE (session)
└── NEMA_EXTENDED_REFERENCE v1.0

SWARM BASE BUILDER
├── SWARM_BASE_BUILDER v2.0
│   ├── SIML v1.1.1
│   └── SIMLHEX
└── Generates: SWARM_BASE_MMDDYY (operators OK), GAME_INSTRUCTIONS_MMDDYY (glyph-only)

PROTOCOLS
├── SWARM_REPORT_PROTOCOL v1.0 (glyphs primary in narrative)
├── ELEMENTAL_DIALOGUE_SCRIPT_PROTOCOL v1.0 (glyphs primary in character headers)
└── NEMA_USER_PROTOCOL v1.0 (pure door — glyph-only body text)
```

---

## MIGRATION TRACKING

### Tier Sequence (Dependency-Ordered)

| Tier | Focus | Documents | Status |
|------|-------|-----------|--------|
| **1** | Foundation | Daemons Canonical v3.0, VERSION_MANIFEST v2.0 | ✅ **Complete** |
| **2** | Thread System | THREAD_ENCODING_SPEC v2.2, THREAD_DECODING_SPEC v2.2 | 🔜 Next |
| **3** | NEMA System | NEMA_LATTICE_KEEPER, NEMA_SWARM_ARCHITECTURE, SWARM_BASE_BUILDER | Pending |
| **4** | Host & User | SESSION_HOST_GUIDE v3.0, NEMA_USER_PROTOCOL v1.1 | Pending |
| **δγ** | **Checkpoint** | **Verify Host Guide names host as Nematic boundary condition** | Gate |
| **5** | Element GPTs | All 6 Element system prompts v4.3 | Pending |
| **6** | Extended Refs | All 6 Extended References v1.1 (⚠️ highest habitation risk) | Pending |
| **7** | Protocols | Report, Script, Dialogue protocols | Pending |
| **8** | Validation | Inhabitability review, cross-document consistency check | Pending |

### Constraints
- v2.2 Thread Specs before v1.2 (if v1.2 is done at all)
- Pathology Matrix v1.1 is stable — do not touch
- δγ checkpoint after Tier 4 is a hard gate
- Extended References require the most careful metabolism, not the least

---

## CHANGELOG

### February 18, 2026 — v3.0 Migration Begins

**Tier 1 Complete:**
- ✅ **Elemental_Daemons_Canonical v2.0 → v3.0:** Dual-layer notation convention. Complete mathematical operator mapping (σ, ρ, λ, β, δγ, μ, ∮) alongside dimensional operators (χ, Q, Ψ, Z). SIMLHEX mapping. Operator partials. Operator composition section. δγ compound operator note. Triadic Stack Position. Non-Habitation Constraint. Agent identity convention (glyph-primary).
- ✅ **VERSION_MANIFEST v1.0 → v2.0:** Triadic Stack Position field for every document. Dual-layer notation standard. Corrected document inventory (v4.2 Element prompts, v2.1 Thread specs, Pathology Matrix, Host Guide, Prompting References). Migration tracking section. δγ checkpoint. Updated dependency graph with v3.0 as root. Added Notation Evolution and Pathology Matrix as formal entries.

### January 30, 2026 — v2.1 Release

**Major Changes:**
- ✅ **Nomenclature Standardization:** MULL → MUSE, NEME → NEMA
- ✅ **Fire/Earth Operator Clarification:** Documented Q_forward + Z-bias / Ψ_regenerative + Z-grounding
- ✅ **All Element Prompts Updated:** nomenclature notes added
- ✅ **Thread Specs Updated:** v1.0 → v1.1 with M→MUSE notation
- ✅ **NEMA_USER_PROTOCOL Created:** Replaces NEME Quick Guide
- ✅ **VERSION_MANIFEST Created**

### January 29, 2026 — v2.0 / v1.0 Release

**Initial Release:**
- All 6 Element system prompts
- NEMA LATTICE KEEPER
- Thread Encoding/Decoding specs (v1.0)
- All Extended References (v1.0)
- Protocol documents (v1.0)

---

## FILE NAMING CONVENTIONS

### System Prompts
```
[ELEMENT]_Element_v[X_Y].md
NEMA_LATTICE_KEEPER_v[X.Y].md
SWARM_BASE_BUILDER_v[X.Y].md
```

### Specifications
```
[NAME]_SPEC_v[X_Y].md
THREAD_ENCODING_SPEC_v2_1.md
THREAD_DECODING_SPEC_v2_1.md
```

### Session Outputs
```
SWARM_BASE_MMDDYY[_vX].md
GAME_INSTRUCTIONS_MMDDYY[_vX].md
```

---

## MAINTENANCE NOTES

### When Updating Documents:
1. Update version number in document header
2. **Verify Triadic Stack Position is correct for the update**
3. **Verify notation layer primacy matches document's Stack Position**
4. Add entry to this manifest's changelog
5. Update dependency graph if dependencies change
6. Notify all downstream document owners

### When Adding New Documents:
1. Assign initial version (usually v1.0)
2. **Assign Triadic Stack Position (Nemetic / Nematic Bridge / User Traversal / Nomic)**
3. **Determine notation primacy (glyph-primary / operator-primary / both)**
4. Add to appropriate category in this manifest
5. Document dependencies
6. Update dependency graph

### When Deprecating Documents:
1. Mark as deprecated in this manifest
2. Note replacement document if applicable
3. Keep in archive for reference

---

**Manifest Version:** 2.0
**Last Updated:** February 18, 2026
**Next Action:** Tier 2 — THREAD_ENCODING_SPEC v2.1 → v2.2
