#!/bin/bash
# δγ-COMPOSTER v1.0
# Weekly digestion of L-Series learning theories into fertile substrate

WORKSPACE="/tmp/nema-swarm"
INPUT_DIR="$WORKSPACE/SIML/terms"
OUTPUT_DIR="$WORKSPACE/docs/compost"
LOG_FILE="$OUTPUT_DIR/compost_$(date +%Y%m%d_%H%M).log"

mkdir -p "$OUTPUT_DIR"

echo "=== δγ-COMPOSTER v1.0 ===" | tee -a "$LOG_FILE"
echo "Started: $(date)" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

# Check for new L-entries
LAST_RUN_FILE="$OUTPUT_DIR/.last_compost"
if [ -f "$LAST_RUN_FILE" ]; then
    NEW_ENTRIES=$(find "$INPUT_DIR" -name "L*" -newer "$LAST_RUN_FILE" 2>/dev/null | wc -l)
else
    NEW_ENTRIES=$(ls -d "$INPUT_DIR"/L* 2>/dev/null | wc -l)
fi

echo "New L-entries detected: $NEW_ENTRIES" | tee -a "$LOG_FILE"

# CONDITION: Run only if new entries > 10 OR manual trigger
if [ "$NEW_ENTRIES" -lt 10 ] && [ "$1" != "--force" ]; then
    echo "CONDITION NOT MET: Only $NEW_ENTRIES new entries (threshold: 10)" | tee -a "$LOG_FILE"
    exit 0
fi

echo "=== CYCLE 1: SEPARATION (σ-cut) ===" | tee -a "$LOG_FILE"

# Generate seed crystals
SEED_CRYSTALS="$OUTPUT_DIR/L-Series_distilled.md"
echo "# L-Series Seed Crystals" > "$SEED_CRYSTALS"
echo "Generated: $(date)" >> "$SEED_CRYSTALS"
echo "" >> "$SEED_CRYSTALS"

for term_dir in "$INPUT_DIR"/L*/; do
    if [ -d "$term_dir" ]; then
        term_name=$(basename "$term_dir")
        if [ -f "$term_dir/term.yaml" ]; then
            source_term=$(grep "^source_term:" "$term_dir/term.yaml" 2>/dev/null | cut -d':' -f2- | sed 's/^ *//' | tr -d '"' | head -1)
            core_operators=$(grep "^Core Operators:" "$term_dir/term.yaml" 2>/dev/null | cut -d':' -f2- | sed 's/^ *//' | head -1)
            
            echo "## $term_name" >> "$SEED_CRYSTALS"
            echo "- **Source:** $source_term" >> "$SEED_CRYSTALS"
            echo "- **Core Mechanism:** $core_operators" >> "$SEED_CRYSTALS"
            echo "" >> "$SEED_CRYSTALS"
        fi
    fi
done

echo "Generated: $SEED_CRYSTALS" | tee -a "$LOG_FILE"

echo "=== CYCLE 2: FERMENTATION (ρ-δγ) ===" | tee -a "$LOG_FILE"

# Generate fermentation log
FERMENTATION_LOG="$OUTPUT_DIR/fermentation_log.md"
echo "# Fermentation Log" > "$FERMENTATION_LOG"
echo "Generated: $(date)" >> "$FERMENTATION_LOG"
echo "" >> "$FERMENTATION_LOG"
echo "Random pairs of L-Series terms for contradiction/completion analysis." >> "$FERMENTATION_LOG"
echo "" >> "$FERMENTATION_LOG"

# Get L-terms and create pairs
ls -d "$INPUT_DIR"/L*/ 2>/dev/null | xargs -n1 basename | sort -V | shuf | paste -d ',' - - | head -50 | while IFS=',' read -r term1 term2; do
    echo "## $term1 ↔ $term2" >> "$FERMENTATION_LOG"
    echo "- **Contradiction:** [To be explored]" >> "$FERMENTATION_LOG"
    echo "- **Completion:** [To be explored]" >> "$FERMENTATION_LOG"
    echo "" >> "$FERMENTATION_LOG"
done

echo "Generated: $FERMENTATION_LOG" | tee -a "$LOG_FILE"

echo "=== CYCLE 3: REGENERATION (β-μ) ===" | tee -a "$LOG_FILE"

# Generate 7 fertile questions
FERTILE_QUESTIONS="$OUTPUT_DIR/7_fertile_questions.md"
cat > "$FERTILE_QUESTIONS" << 'EOF'
# 7 Fertile Questions

> Don't answer. Germinate.

## Air (∴) — Distinction
What distinctions does learning theory make that prevent it from seeing its own shadows?

## Water (≈) — Resonance  
What felt-qualities of learning resist formalization?

## Fire (▲) — Direction
What purposes drive learning theory that the theories cannot name?

## Wood (𐂷) — Branching
What learning pathways has no theory mapped?

## Earth (☷) — Cycling
What cycles are being treated as linear progress?

## Metal (⛨) — Structure
What boundaries guard emptiness?

## ✶ Child/Aether — Meta
What question about learning has not been asked because the asking would change the asker?
EOF

echo "Generated: $FERTILE_QUESTIONS" | tee -a "$LOG_FILE"

# Generate 3 hybrid operators
HYBRID_OPERATORS="$OUTPUT_DIR/3_hybrid_operators.md"
cat > "$HYBRID_OPERATORS" << 'EOF'
# 3 Hybrid Operators

> Unnamed, untheorized possibilities

## Hybrid 1: σ-ρ-λ (Attunement)
Learning that begins with distinction, opens to resonance, finds direction.

## Hybrid 2: β-δγ-μ (Recursive Practice)
Learning that branches, cycles through decay, structures from compost.

## Hybrid 3: ρ-λ-✶ (Flow-State Community)
Learning where resonance, direction, and harmonic integration converge.
EOF

echo "Generated: $HYBRID_OPERATORS" | tee -a "$LOG_FILE"

# Archive full L-Series
echo "=== ARCHIVING ===" | tee -a "$LOG_FILE"
tar -czf "$OUTPUT_DIR/L-Series_archived_$(date +%Y%m%d).tar.gz" -C "$INPUT_DIR" L* 2>/dev/null
echo "Archived: L-Series_archived_$(date +%Y%m%d).tar.gz" | tee -a "$LOG_FILE"

# Update last run timestamp
date > "$LAST_RUN_FILE"

echo "" | tee -a "$LOG_FILE"
echo "=== δγ-COMPOSTER COMPLETE ===" | tee -a "$LOG_FILE"
echo "Compost's done. Buried the L-Series deep." | tee -a "$LOG_FILE"
echo "Surfaced 7 questions that don't know their own names yet." | tee -a "$LOG_FILE"
echo "3 hybrids stirring in the dark." | tee -a "$LOG_FILE"
echo "Field's ready for planting—when you're ready to not know what you're growing." | tee -a "$LOG_FILE"
