# Concept Deduplication Protocol for NEMA SWARM

## Problem
The SIML Elemental Insight Generator was creating multiple entries for the same concept:
- Dark Patterns: 4 entries (#A027, #A041, #A049, #A051)
- Barnum Effect: 3 entries (#A01E, #A043, #A04B)
- Déjà Vu: 3 entries (#A030, #A040, #A050)
- etc.

## Root Cause
Hex tag checking alone wasn't sufficient. The job checked "has A027 been created?" but not "has the concept 'Dark Patterns' been encoded?"

## Solution: Semantic Deduplication Check

### Step 1: Extract Core Concept
Before generating a new entry, extract the core concept name from the source:
- Source file: "Dark Patterns: Ethical Implications and Regulations"
- Core concept: "Dark Patterns"

### Step 2: Multi-Layer Deduplication Check

Check against ALL existing entries:

1. **Exact Match** — Is there an entry with identical source_term?
2. **Substring Match** — Does any existing source_term contain the new concept?
3. **Reverse Substring** — Does the new concept contain any existing source_term?
4. **Glossary Scan** — Does SWARM_BASE glossary already list this term?

### Step 3: Similarity Scoring

For borderline cases, calculate similarity:
```
Concept A: "Dark Patterns"
Concept B: "Dark Pattern Design"
Similarity: 85% → DUPLICATE

Concept A: "Barnum Effect"  
Concept B: "Forer Effect"
Similarity: 30% → RELATED but DISTINCT (add cross-reference, not duplicate)
```

### Step 4: Decision Matrix

| Similarity | Action |
|------------|--------|
| > 80% | SKIP — concept already encoded |
| 50-80% | FLAG — possible variant/angle, review manually |
| < 50% | PROCEED — distinct concept |

## Implementation

### For Cognitive Bias Generator:
```bash
# Before generating entry:
CONCEPT=$(extract_concept_from_source "$SOURCE_FILE")

if concept_already_encoded "$CONCEPT"; then
    echo "Concept '$CONCEPT' already encoded. Skipping."
    exit 0
fi

# Generate entry...
```

### For Democracy Generator:
```bash
# Before processing PDF:
PDF_NAME=$(basename "$PDF_FILE" .pdf)
CORE_THEME=$(extract_core_theme "$PDF_NAME")

if theme_already_encoded "$CORE_THEME"; then
    echo "Theme '$CORE_THEME' already encoded. Checking for new angles..."
    # Allow ONE expanded variant per theme, then stop
fi
```

## Current Status (Paused Jobs)

| Job | Status | Entries Created |
|-----|--------|-----------------|
| siml_elemental_insight_generator | PAUSED | ~60 A-series entries |
| nema_democracy_siml_generator | PAUSED | ~60 D-series entries |
| nema_learning_theories_generator | ACTIVE (until L100) | ~10 L-series entries |

## Resumption Criteria

Before resuming paused jobs:
1. Implement concept deduplication check
2. Audit existing entries for true duplicates
3. Merge or flag redundant entries
4. Set maximum entries per concept (e.g., 1 primary + 1 variant max)

## Files Created

- `/tmp/nema-swarm/scripts/concept_dedup_check.sh` — Basic deduplication script
- `/tmp/nema-swarm/docs/CONCEPT_DEDUP_PROTOCOL.md` — This document
