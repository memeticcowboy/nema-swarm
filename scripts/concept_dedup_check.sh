#!/bin/bash
# concept_dedup_check.sh
# Semantic concept deduplication checker for NEMA SWARM
# Usage: ./concept_dedup_check.sh "Concept Name" [similarity_threshold]

CONCEPT="$1"
THRESHOLD="${2:-0.7}"  # Default 70% similarity
WORKSPACE="/tmp/nema-swarm"
TERMS_DIR="$WORKSPACE/SIML/terms"

if [ -z "$CONCEPT" ]; then
    echo "Usage: $0 \"Concept Name\" [similarity_threshold]"
    exit 1
fi

# Normalize concept name for comparison
NORMALIZED=$(echo "$CONCEPT" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]//g')

echo "Checking for semantic duplicates of: $CONCEPT"
echo "Normalized: $NORMALIZED"
echo ""

# Check existing term directories for similar concepts
FOUND_DUPS=0

for term_dir in "$TERMS_DIR"/*/; do
    if [ -d "$term_dir" ]; then
        # Extract term name from directory
        term_name=$(basename "$term_dir")
        
        # Read term.yaml if exists
        if [ -f "$term_dir/term.yaml" ]; then
            # Extract source_term from YAML
            source_term=$(grep -E "^source_term:" "$term_dir/term.yaml" | sed 's/source_term: //' | tr -d '"' | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]//g')
            
            # Extract term_id
            term_id=$(grep -E "^term_id:" "$term_dir/term.yaml" | sed 's/term_id: //' | tr -d '"')
            
            # Simple substring matching (can be enhanced with fuzzy matching)
            if [ -n "$source_term" ]; then
                # Check if normalized concept is substring of source_term or vice versa
                if [[ "$source_term" == *"$NORMALIZED"* ]] || [[ "$NORMALIZED" == *"$source_term"* ]]; then
                    echo "POTENTIAL DUPLICATE FOUND:"
                    echo "  Directory: $term_name"
                    echo "  Term ID: $term_id"
                    echo "  Source Term: $(grep -E "^source_term:" "$term_dir/term.yaml" | sed 's/source_term: //' | tr -d '"')"
                    echo ""
                    FOUND_DUPS=$((FOUND_DUPS + 1))
                fi
            fi
        fi
    fi
done

# Also check SWARM_BASE glossary for similar entries
if [ -f "$WORKSPACE/SWARM_BASE/swarm_base_01.md" ]; then
    echo "Checking SWARM_BASE glossary..."
    
    # Extract all term names from glossary
    glossary_terms=$(grep -E "^- \*\*Term:\*\*" "$WORKSPACE/SWARM_BASE/swarm_base_01.md" | sed 's/- \*\*Term:\*\* //' | tr '[:upper:]' '[:lower:]')
    
    while IFS= read -r gterm; do
        gterm_normalized=$(echo "$gterm" | sed 's/[^a-z0-9]//g')
        
        if [ -n "$gterm_normalized" ]; then
            if [[ "$gterm_normalized" == *"$NORMALIZED"* ]] || [[ "$NORMALIZED" == *"$gterm_normalized"* ]]; then
                echo "GLOSSARY MATCH FOUND: $gterm"
                FOUND_DUPS=$((FOUND_DUPS + 1))
            fi
        fi
    done <<< "$glossary_terms"
fi

if [ $FOUND_DUPS -eq 0 ]; then
    echo "No semantic duplicates found. Safe to proceed."
    exit 0
else
    echo "Found $FOUND_DUPS potential duplicate(s). Review before creating new entry."
    exit 1
fi
