#!/usr/bin/env python3
"""
Learning & Metacognition SIML Processor
Processes files from Sensemaking & Epistemics into SIML entries
Runs every 10 minutes via cron
"""

import os
import sys
import yaml
import re
import subprocess
from pathlib import Path
from datetime import datetime

# Configuration
MANIFEST_PATH = "/tmp/nema-swarm/SIML/learning_metacognition_manifest.yaml"
HEX_REGISTRY_PATH = "/tmp/nema-swarm/SIML/hex_registry.yaml"
SOURCE_DIR = "/tmp/nema-swarm/SWARM_BASE/Sensemaking & Epistemics"
SIML_TERMS_DIR = "/tmp/nema-swarm/SIML/terms"
LOG_FILE = "/tmp/nema-swarm/SIML/learning_processing.log"

def log_message(msg):
    """Write to log file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {msg}\n"
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)
    print(log_entry.strip())

def load_manifest():
    """Load the processing manifest"""
    with open(MANIFEST_PATH, 'r') as f:
        return yaml.safe_load(f) or {}

def save_manifest(manifest):
    """Save the processing manifest"""
    manifest['last_updated'] = datetime.now().isoformat()
    with open(MANIFEST_PATH, 'w') as f:
        yaml.dump(manifest, f, default_flow_style=False, sort_keys=False)

def load_hex_registry():
    """Load hex registry"""
    with open(HEX_REGISTRY_PATH, 'r') as f:
        return yaml.safe_load(f) or {}

def save_hex_registry(registry):
    """Save hex registry"""
    with open(HEX_REGISTRY_PATH, 'w') as f:
        yaml.dump(registry, f, default_flow_style=False, sort_keys=False)

def get_next_hex_tag(series='L'):
    """Get next available hex tag for L series"""
    registry = load_hex_registry()
    
    if series not in registry:
        registry[series] = {
            'description': 'Learning and metacognition concepts',
            'next_available': f'{series}100',
            'assigned': {},
            'collisions': {}
        }
    
    next_tag = registry[series].get('next_available', f'{series}100')
    return next_tag, registry

def claim_hex_tag(tag, term_name, registry):
    """Claim a hex tag"""
    series = tag[0]
    
    if 'assigned' not in registry[series]:
        registry[series]['assigned'] = {}
    
    registry[series]['assigned'][tag] = term_name.replace(' ', '_')
    
    # Calculate next
    num = int(re.search(r'(\d+)$', tag).group(1))
    registry[series]['next_available'] = f"{series}{num + 1:03d}"
    
    save_hex_registry(registry)
    return True

def sanitize_filename(name):
    """Convert filename to safe term name"""
    # Remove URL encoding, file extensions, common words
    name = re.sub(r'%[0-9A-Fa-f]{2}', ' ', name)
    name = re.sub(r'\.md$', '', name)
    name = re.sub(r'^[0-9_]+', '', name)
    name = name.replace('+', ' ')
    
    # Remove common filler words
    fillers = ['the', 'a', 'an', 'of', 'and', 'in', 'on', 'with', 'for', 'to', 'from']
    words = name.split()
    words = [w for w in words if w.lower() not in fillers]
    
    # Take first 4-5 significant words
    name = ' '.join(words[:5])
    
    # Clean up
    name = re.sub(r'[^\w\s]', '', name)
    name = name.strip()
    name = name.replace(' ', '_')
    
    return name[:50]  # Limit length

def extract_concepts_from_file(filepath):
    """Extract key concepts from a learning/metacognition file"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        log_message(f"Error reading file: {e}")
        return None
    
    # Extract title from first line or content
    title_match = re.search(r'^#\s*(.+)$', content, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
    else:
        # Use filename as fallback
        title = Path(filepath).stem
        title = re.sub(r'%[0-9A-Fa-f]{2}', ' ', title)
        title = title.replace('+', ' ')
    
    # Extract key concepts (first paragraph after title)
    paragraphs = content.split('\n\n')
    description = ""
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('#') and len(p) > 50:
            description = p[:200]  # First 200 chars
            break
    
    # Determine elemental emphasis based on content keywords
    elemental = {
        'air': 0.60,
        'water': 0.60,
        'fire': 0.60,
        'wood': 0.60,
        'earth': 0.60,
        'metal': 0.60,
        'meta': 0.70
    }
    
    # Adjust based on content
    content_lower = content.lower()
    
    if any(w in content_lower for w in ['thinking', 'cognitive', 'mental', 'mind']):
        elemental['air'] = 0.75
    if any(w in content_lower for w in ['learning', 'adaptation', 'growth', 'change']):
        elemental['wood'] = 0.75
    if any(w in content_lower for w in ['metacognition', 'reflection', 'awareness', 'self']):
        elemental['meta'] = 0.85
    if any(w in content_lower for w in ['memory', 'retention', 'practice', 'repetition']):
        elemental['earth'] = 0.75
    if any(w in content_lower for w in ['connection', 'relation', 'social', 'collaborative']):
        elemental['water'] = 0.75
    
    return {
        'title': title,
        'description': description,
        'elemental': elemental,
        'content': content[:1000]  # First 1000 chars for processing
    }

def create_siml_entry(hex_tag, term_name, concepts, source_file):
    """Create SIML entry files"""
    
    # Create directory
    dir_name = f"{hex_tag}_{term_name}"
    term_path = Path(SIML_TERMS_DIR) / dir_name
    term_path.mkdir(parents=True, exist_ok=True)
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    # term.yaml
    yaml_content = f"""---
term_id: {hex_tag}
hex_tag: {hex_tag}
canonical_name: {term_name.replace('_', ' ')}
category: learning_metacognition
description: {concepts['description'][:100]}
created_date: {today}
status: candidate
source_file: {source_file}

elemental_mapping:
  air: {concepts['elemental']['air']:.2f}
  water: {concepts['elemental']['water']:.2f}
  fire: {concepts['elemental']['fire']:.2f}
  wood: {concepts['elemental']['wood']:.2f}
  earth: {concepts['elemental']['earth']:.2f}
  metal: {concepts['elemental']['metal']:.2f}
  meta: {concepts['elemental']['meta']:.2f}
---

# {hex_tag} — {term_name.replace('_', ' ')}

## {concepts['description'][:150]}

*(Extracted from Learning & Metacognition source)*

## Source Content

```
{concepts['content'][:500]}
```

---

ε preserved.
"""
    
    (term_path / "term.yaml").write_text(yaml_content)
    
    # nemetic.phi
    phi_content = f"""Φ({term_name}) = σ(learning_distinction) ∘ ρ(knowledge_relation) ∘ λ(cognitive_direction) ∘ β(growth_branching) ∘ δγ(metabolic_integration) ∘ μ(structure_boundary) + ε(uncertainty) | :learning_metacognition

σ(learning_distinction): The cut that distinguishes learning from non-learning
ρ(knowledge_relation): How knowledge connects and flows
λ(cognitive_direction): Aim of learning process
β(growth_branching): Multiple paths of development
δγ(metabolic_integration): Cycling of learning through practice
μ(structure_boundary): Containment of learning framework
ε(uncertainty): The productive ambiguity in learning

:state = learning_metacognition

# Dialectical Pairs
- learning|knowing: Process vs. state
- growth|structure: Adaptation vs. stability
- individual|social: Solo vs. collaborative learning
- theory|practice: Abstract vs. embodied knowledge
"""
    
    (term_path / "nemetic.phi").write_text(phi_content)
    
    # insight.md
    insight_content = f"""# {hex_tag} — {term_name.replace('_', ' ')}

**Elemental Insight: Meta/Learning**

## The Question

What does this learning/metacognition concept reveal about knowledge formation?

## Source Analysis

*(To be developed from source content)*

## Elemental Emphasis

**Meta** — Learning about learning. The recursive nature of metacognition.

**Wood** — Growth and adaptation through learning cycles.

## Cross-Elemental Resonance

- **With L-series (Learning Theories)**: Connect to established learning frameworks
- **With M004 (Metabolism)**: Learning as metabolic cycling of knowledge

## NEMETIC STRING

`Φ({term_name}) = ...`

---

*Learning in progress.*

ε preserved.
"""
    
    (term_path / "insight.md").write_text(insight_content)
    
    return term_path

def process_next_file():
    """Process the next file in queue"""
    manifest = load_manifest()
    
    # Get list of files in source directory
    source_files = sorted([f for f in os.listdir(SOURCE_DIR) if f.endswith('.md')])
    
    if not source_files:
        log_message("No files remaining to process")
        return False
    
    # Get next file
    next_file = source_files[0]
    filepath = os.path.join(SOURCE_DIR, next_file)
    
    log_message(f"Processing: {next_file}")
    
    # Extract concepts
    concepts = extract_concepts_from_file(filepath)
    if not concepts:
        log_message(f"Failed to extract concepts from {next_file}")
        return False
    
    # Generate term name
    term_name = sanitize_filename(next_file)
    if not term_name:
        term_name = f"learning_concept_{manifest['next_index']}"
    
    # Get hex tag
    hex_tag, registry = get_next_hex_tag('L')
    log_message(f"Allocating hex tag: {hex_tag}")
    
    # Create SIML entry
    try:
        term_path = create_siml_entry(hex_tag, term_name, concepts, next_file)
        log_message(f"Created SIML entry: {term_path}")
    except Exception as e:
        log_message(f"Error creating SIML entry: {e}")
        return False
    
    # Claim hex tag
    claim_hex_tag(hex_tag, term_name, registry)
    
    # Update manifest
    manifest['processed_count'] = manifest.get('processed_count', 0) + 1
    manifest['remaining_count'] = len(source_files) - 1
    manifest['next_index'] = manifest.get('next_index', 1) + 1
    manifest['next_available'] = f"L{int(hex_tag[1:]) + 1:03d}"
    
    processed_entry = {
        'index': manifest['next_index'] - 1,
        'source_file': next_file,
        'hex_tag': hex_tag,
        'term_name': term_name,
        'processed_at': datetime.now().isoformat(),
        'siml_path': str(term_path)
    }
    
    if 'processed' not in manifest:
        manifest['processed'] = []
    manifest['processed'].append(processed_entry)
    
    if 'log' not in manifest:
        manifest['log'] = []
    manifest['log'].append(f"[{datetime.now().isoformat()}] Processed {next_file} as {hex_tag}")
    
    save_manifest(manifest)
    
    # Delete source file
    try:
        os.remove(filepath)
        log_message(f"Deleted source file: {next_file}")
    except Exception as e:
        log_message(f"Warning: Could not delete source file: {e}")
    
    log_message(f"Complete: {hex_tag} {term_name}")
    return True

if __name__ == "__main__":
    log_message("="*60)
    log_message("Learning & Metacognition SIML Processor")
    log_message("="*60)
    
    success = process_next_file()
    
    if success:
        log_message("Processing complete")
        sys.exit(0)
    else:
        log_message("Processing failed or no files remaining")
        sys.exit(1)
