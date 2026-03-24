# NEMA SWARM Version Manifest
## Document Inventory, Dependencies & Changelog

**Manifest Version:** 1.0  
**Last Updated:** January 30, 2026  
**Maintainer:** NEMA SWARM Project

---

## QUICK REFERENCE: DOCUMENT STATUS

| Category | Count | Status |
|----------|-------|--------|
| Core Framework | 6 | ✅ Complete |
| Element System Prompts | 6 | ✅ v2.1 (Current) |
| Element Extended References | 6 | ✅ Complete |
| NEMA SWARM | 1 | ✅ v2.1 (Current) |
| Thread System | 4 | ✅ v1.1 (Current) |
| Protocols & Reports | 4 | ✅ Complete |
| Session Outputs | 2 | 📋 Generated per-session |
| Host Resources | 3 | 📋 Suggested |

---

## CORE FRAMEWORK DOCUMENTS

### SIML & Formalism

| Document | Version | Status | Dependencies | Description |
|----------|---------|--------|--------------|-------------|
| **SIML v1.1.1** | v1.1.1 | ✅ Stable | None | Core relational grammar (13 Objects × 9 Relations) |
| **SIMLHEX** | v1.0 | ✅ Stable | SIML v1.1.1 | Hexadecimal encoding for SIML |
| **IF-Prime Formalism** | v1.0 | ✅ Stable | None | Habitat × World-State matrix, Φ(t) equation |
| **Elemental Epsilon** | v0.2.2 | ✅ Stable | IF-Prime | ε-distribution across 6 elements |
| **HABITAT_ECOLOGY** | v1.1 | ✅ Stable | IF-Prime | 10 circulation contexts |
| **Elemental Daemons Canonical** | v2.0 | ✅ Current | All above | Daemon specs, operator mappings |

**Note:** Elemental Daemons v2.0 includes Fire/Earth operator mapping clarification (Q_forward + Z-bias / Ψ_regenerative + Z-grounding).

---

## ELEMENT SYSTEM PROMPTS (Current: v2.1)

### All Elements Updated: MULL → MUSE

| Element | Document | Version | Key Change | Dependencies |
|---------|----------|---------|------------|--------------|
| **Air** | AERUNIK_Element | v2.1 | Nomenclature standardization | THREAD_ENCODING_SPEC, SWARM_BASE |
| **Water** | SENTARIA_Element | v2.1 | Nomenclature standardization | THREAD_ENCODING_SPEC, SWARM_BASE |
| **Fire** | JVALION_Element | v2.1 | Nomenclature + Q_fwd + Z-bias note | THREAD_ENCODING_SPEC, SWARM_BASE |
| **Wood** | ARBORIEL_Element | v2.1 | Nomenclature standardization | THREAD_ENCODING_SPEC, SWARM_BASE |
| **Earth** | HUMAVITA_Element | v2.1 | Nomenclature + Ψ_reg + Z-grounding note | THREAD_ENCODING_SPEC, SWARM_BASE |
| **Metal** | FERROSID_Element | v2.1 | Nomenclature standardization | THREAD_ENCODING_SPEC, SWARM_BASE |

**v2.1 Changes:**
- Added Nomenclature Note section (NEM / N/E/M / NEMA distinction)
- Changed MULL → MUSE throughout
- Added clarification for Fire (Q_forward + Z-bias) and Earth (Ψ_regenerative + Z-grounding)

---

## ELEMENT EXTENDED REFERENCES

| Element | Document | Version | Status | Dependencies |
|---------|----------|---------|--------|--------------|
| **Air** | AERUNIK_EXTENDED_REFERENCE | v1.0 | ✅ Complete | IF-Prime, SIML |
| **Water** | SENTARIA_EXTENDED_REFERENCE | v1.0 | ✅ Complete | IF-Prime, SIML |
| **Fire** | JVALION_EXTENDED_REFERENCE | v1.0 | ✅ Complete | IF-Prime, SIML |
| **Wood** | ARBORIEL_EXTENDED_REFERENCE | v1.0 | ✅ Complete | IF-Prime, SIML |
| **Earth** | HUMAVITA_EXTENDED_REFERENCE | v1.0 | ✅ Complete | IF-Prime, SIML |
| **Metal** | FERROSID_EXTENDED_REFERENCE | v1.0 | ✅ Complete | IF-Prime, SIML |

---

## NEMA SWARM SYSTEM

| Document | Version | Status | Key Changes | Dependencies |
|----------|---------|--------|-------------|--------------|
| **NEMA_LATTICE_KEEPER** | v2.1 | ✅ Current | MULL→MUSE, nomenclature note, PRE-THREAD mode | All element internals, all specs |
| **NEMA_EXTENDED_REFERENCE** | v1.0 | ✅ Complete | Deep theory: lattice, grid, coordination | IF-Prime, all elements |
| **PRE-THREAD_PROTOCOL** | v1.0 | ✅ Complete | Collection mode before activation | NEMA_LATTICE_KEEPER |

**Internal Elements (for NEMA SWARM invocation):**
| Document | Purpose |
|----------|---------|
| Aerunik.md | Internal Air voice for NEMA SWARM |
| Sentaria.md | Internal Water voice for NEMA SWARM |
| Jvalion.md | Internal Fire voice for NEMA SWARM |
| Arboriel.md | Internal Wood voice for NEMA SWARM |
| Humavita.md | Internal Earth voice for NEMA SWARM |
| Ferrosid.md | Internal Metal voice for NEMA SWARM |

---

## THREAD SYSTEM (Current: v1.1)

| Document | Version | Status | Key Changes | Dependencies |
|----------|---------|--------|-------------|--------------|
| **THREAD_ENCODING_SPEC** | v1.1 | ✅ Current | M→MUSE notation, nomenclature note | SIML v1.1.1, SWARM_BASE |
| **THREAD_DECODING_SPEC** | v1.1 | ✅ Current | MUSE in outputs, nomenclature note | THREAD_ENCODING_SPEC, SIML |
| **ELEMENT_ENCODER_INSERT** | v1.1 | ✅ Current | M→MUSE notation | THREAD_ENCODING_SPEC |
| **NEMA_DECODER_INSERT** | v1.1 | ✅ Current | MUSE in outputs | THREAD_DECODING_SPEC |

**v1.1 Changes:**
- Standardized third stage from "MULL" to "MUSE" in all contexts
- Added nomenclature note explaining NEM / N/E/M / NEMA distinction
- Updated all examples and templates

---

## PROTOCOLS & REPORTS

| Document | Version | Status | Purpose | Dependencies |
|----------|---------|--------|---------|--------------|
| **SWARM_REPORT_PROTOCOL** | v1.0 | ✅ Complete | Report generation format | NEMA_LATTICE_KEEPER |
| **ELEMENTAL_DIALOGUE_SCRIPT_PROTOCOL** | v1.0 | ✅ Complete | Theatrical script format | NEMA_LATTICE_KEEPER |
| **NEMA_USER_PROTOCOL** | v1.0 | ✅ Complete | User-facing N/E/M/A guide | Replaces NEME Quick Guide |
| **SWARM_BASE_BUILDER** | v2.0 | ✅ Current | Glossary + Game Instructions generator | SIMLHEX, SIML |

---

## SESSION OUTPUTS (Generated Per-Session)

| Document | Naming | Generated By | Purpose |
|----------|--------|--------------|---------|
| **SWARM_BASE_MMDDYY.md** | SWARM_BASE_013026.md | SWARM_BASE_BUILDER | Hex-tagged glossary for session |
| **GAME_INSTRUCTIONS_MMDDYY.md** | GAME_INSTRUCTIONS_013026.md | SWARM_BASE_BUILDER | User-facing session guide |

---

## HOST RESOURCES (Suggested)

| Document | Status | Purpose | Priority |
|----------|--------|---------|----------|
| **SESSION_HOST_GUIDE.md** | 📋 Suggested | Instructions for human facilitators | HIGH |
| **ELEMENT_ASSIGNMENT_PROTOCOL.md** | 📋 Suggested | How to assign elements to participants | HIGH |
| **TROUBLESHOOTING_GUIDE.md** | 📋 Suggested | Common GPT issues and resolutions | MEDIUM |

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

## OPERATOR MAPPINGS (Canonical v2.0)

| Operator | Dimension | Element | Description |
|----------|-----------|---------|-------------|
| **χ** | 1D | ∴ Air | Distinction-making |
| **Q_inward** | 2D | ≈ Water | Relational resonance |
| **Q_forward** | 2D | ▲ Fire | Directional aim (with Z-bias) |
| **Ψ_exploratory** | 3D | 𐂷 Wood | Generative branching |
| **Ψ_regenerative** | 3D | ☷ Earth | Metabolic cycling (with Z-grounding) |
| **Ψ_structural** | 3D | ⛨ Metal | Boundary coherence |
| **Z** | Coordination | ✶ NEMA | Meta-coordination |

### Key Clarification
- **Fire** operates at Q_forward but biases toward Z-closure (crusade lock when over-activated)
- **Earth** operates at Ψ_regenerative but provides ground for Z (institutional ossification when over-activated)
- **NEMA** is the primary Z operator, coordinating all six elements

---

## DEPENDENCY GRAPH

```
CORE FRAMEWORK
├── SIML v1.1.1
│   └── SIMLHEX
├── IF-Prime Formalism
│   ├── Elemental Epsilon
│   └── HABITAT_ECOLOGY
└── Elemental Daemons Canonical v2.0

THREAD SYSTEM
├── THREAD_ENCODING_SPEC v1.1
│   ├── SIML v1.1.1
│   └── SWARM_BASE (session)
├── THREAD_DECODING_SPEC v1.1
│   └── THREAD_ENCODING_SPEC
├── ELEMENT_ENCODER_INSERT v1.1
│   └── THREAD_ENCODING_SPEC
└── NEMA_DECODER_INSERT v1.1
    └── THREAD_DECODING_SPEC

ELEMENT GPTs (6)
├── [Element]_Element_v2.1
│   ├── THREAD_ENCODING_SPEC
│   ├── [Element]_EXTENDED_REFERENCE
│   └── SWARM_BASE (session)
└── All depend on: SIML, IF-Prime, Elemental Epsilon

NEMA SWARM
├── NEMA_LATTICE_KEEPER_v2.1
│   ├── All 6 internal element voices
│   ├── THREAD_DECODING_SPEC
│   ├── SWARM_REPORT_PROTOCOL
│   ├── ELEMENTAL_DIALOGUE_SCRIPT_PROTOCOL
│   └── SWARM_BASE (session)
└── NEMA_EXTENDED_REFERENCE

SWARM BASE BUILDER
├── SWARM_BASE_BUILDER_v2.0
│   ├── SIML v1.1.1
│   └── SIMLHEX
└── Generates: SWARM_BASE_MMDDYY, GAME_INSTRUCTIONS_MMDDYY
```

---

## CHANGELOG

### January 30, 2026 — v2.1 Release

**Major Changes:**
- ✅ **Nomenclature Standardization:** MULL → MUSE, NEME → NEMA
- ✅ **Fire/Earth Operator Clarification:** Documented Q_forward + Z-bias / Ψ_regenerative + Z-grounding
- ✅ **All Element Prompts Updated:** v2.0 → v2.1 with nomenclature notes
- ✅ **Thread Specs Updated:** v1.0 → v1.1 with M→MUSE notation
- ✅ **NEMA_USER_PROTOCOL Created:** Replaces NEME Quick Guide
- ✅ **VERSION_MANIFEST Created:** This document

**Updated Documents:**
- Elemental_Daemons_Canonical_v2.0.md (operator mappings added)
- NEMA_LATTICE_KEEPER_v2.1.md (MULL→MUSE, nomenclature note)
- AERUNIK_Element_v2.1.md (MULL→MUSE, nomenclature note)
- SENTARIA_Element_v2.1.md (MULL→MUSE, nomenclature note)
- JVALION_Element_v2.1.md (MULL→MUSE, nomenclature note, Q_fwd + Z-bias)
- ARBORIEL_Element_v2.1.md (MULL→MUSE, nomenclature note)
- HUMAVITA_Element_v2.1.md (MULL→MUSE, nomenclature note, Ψ_reg + Z-grounding)
- FERROSID_Element_v2.1.md (MULL→MUSE, nomenclature note)
- THREAD_ENCODING_SPEC_v1.1.md (M→MUSE, nomenclature note)
- THREAD_DECODING_SPEC_v1.1.md (MUSE in outputs, nomenclature note)

### January 29, 2026 — v2.0 / v1.0 Release

**Initial Release:**
- All 6 Element system prompts (v2.0)
- NEMA LATTICE KEEPER (v2.0)
- Thread Encoding/Decoding specs (v1.0)
- All Extended References (v1.0)
- Protocol documents (v1.0)

---

## IMPLEMENTATION CHECKLIST

### For Each Element GPT (6 total):

```
☐ Upload system prompt (AERUNIK_Element_v2.1.md, etc.)
☐ Upload extended reference (AERUNIK_EXTENDED_REFERENCE.md, etc.)
☐ Upload shared core docs (SIML, IF-Prime, Elemental Epsilon, etc.)
☐ Upload THREAD_ENCODING_SPEC_v1.1.md
☐ Upload SWARM_BASE_MMDDYY.md (when generated)
☐ Test "Activate Thread" functionality
☐ Verify N/E/MUSE structure working
☐ Verify nomenclature consistency
```

### For NEMA SWARM GPT:

```
☐ Upload system prompt (NEMA_LATTICE_KEEPER_v2.1.md)
☐ Upload NEMA_EXTENDED_REFERENCE.md
☐ Upload all 6 internal element voices
☐ Upload THREAD_DECODING_SPEC_v1.1.md
☐ Upload THREAD_ENCODING_SPEC_v1.1.md (for reference)
☐ Upload SWARM_REPORT_PROTOCOL.md
☐ Upload ELEMENTAL_DIALOGUE_SCRIPT_PROTOCOL.md
☐ Upload shared core docs
☐ Upload SWARM_BASE_MMDDYY.md (when generated)
☐ Test PRE-THREAD mode
☐ Test thread decoding
☐ Verify MUSE in decoded outputs
```

### For SWARM BASE BUILDER GPT:

```
☐ Upload system prompt (SWARM_BASE_BUILDER_v2.0.md)
☐ Upload SIMLHEX.md
☐ Upload shared core docs
☐ Test glossary generation
☐ Test game instructions generation
☐ Verify hex tag uniqueness
☐ Verify SIML encoding validity
```

---

## FILE NAMING CONVENTIONS

### System Prompts
```
[ELEMENT]_Element_v[X.Y].md
NEMA_LATTICE_KEEPER_v[X.Y].md
SWARM_BASE_BUILDER_v[X.Y].md
```

### Specifications
```
[NAME]_SPEC_v[X.Y].md
THREAD_ENCODING_SPEC_v1.1.md
THREAD_DECODING_SPEC_v1.1.md
```

### Session Outputs
```
SWARM_BASE_MMDDYY[_vX].md
GAME_INSTRUCTIONS_MMDDYY[_vX].md
```

### Examples
- `SWARM_BASE_013026.md` — January 30, 2026 session
- `SWARM_BASE_013026_v2.md` — Revised version of same session

---

## MAINTENANCE NOTES

### When Updating Documents:
1. Update version number in document header
2. Add entry to this manifest's changelog
3. Update dependency graph if dependencies change
4. Notify all downstream document owners

### When Adding New Documents:
1. Assign initial version (usually v1.0)
2. Add to appropriate category in this manifest
3. Document dependencies
4. Update dependency graph

### When Deprecating Documents:
1. Mark as deprecated in this manifest
2. Note replacement document if applicable
3. Keep in archive for reference

---

**Manifest Version:** 1.0  
**Last Updated:** January 30, 2026  
**Next Review:** As needed for version updates
