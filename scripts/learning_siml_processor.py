#!/usr/bin/env python3
"""
Learning & Metacognition SIML Processor
Processes files from Memetic_Ecology/Learning & Metacognition into SIML entries
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
SOURCE_DIR = "/tmp/Memetic_Ecology/Learning & Metacognition"
SOURCE_REPO = "/tmp/Memetic_Ecology"
SIML_TERMS_DIR = "/tmp/nema-swarm/SIML/terms"
LOG_FILE = "/tmp/nema-swarm/SIML/learning_processing.log"

def pull_latest_source():
    """Pull latest files from Memetic_Ecology repo"""
    try:
        result = subprocess.run(
            ["git", "pull", "origin", "main"],
            cwd=SOURCE_REPO,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            log_message("Pulled latest from Memetic_Ecology repo")
            return True
        else:
            log_message(f"Git pull warning: {result.stderr}")
            return False
    except Exception as e:
        log_message(f"Git pull error: {e}")
        return False

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

def get_next_hex_tag(series='L', manifest=None):
    """Get next available hex tag for L series, with gap-filling support"""
    registry = load_hex_registry()
    
    # Use provided manifest or load fresh
    if manifest is None:
        manifest = load_manifest()
    
    # Check if we're in gap-filling mode
    if manifest.get('gap_filling_mode', False):
        gap_range = manifest.get('gap_range', [])
        gap_index = manifest.get('gap_index', 0)
        
        if gap_index < len(gap_range):
            # Return next gap tag
            next_tag = gap_range[gap_index]
            manifest['gap_index'] = gap_index + 1
            
            # If we've filled all gaps, disable gap-filling mode
            if manifest['gap_index'] >= len(gap_range):
                manifest['gap_filling_mode'] = False
                manifest['next_available'] = 'L106'
            
            save_manifest(manifest)
            return next_tag, registry, manifest
    
    # Normal mode: use next_available from registry
    if series not in registry:
        registry[series] = {
            'description': 'Learning and metacognition concepts',
            'next_available': f'{series}106',
            'assigned': {},
            'collisions': {}
        }
    
    next_tag = registry[series].get('next_available', f'{series}106')
    return next_tag, registry, manifest

def claim_hex_tag(tag, term_name, registry):
    """Claim a hex tag"""
    series = tag[0]
    
    if 'assigned' not in registry[series]:
        registry[series]['assigned'] = {}
    
    registry[series]['assigned'][tag] = term_name.replace(' ', '_')
    
    # Note: next_available is managed in get_next_hex_tag for gap-filling mode
    # Only update registry next_available if not in gap-filling
    manifest = load_manifest()
    if not manifest.get('gap_filling_mode', False):
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
    
    # Extract key concepts (first substantial paragraph after title)
    paragraphs = content.split('\n\n')
    description = ""
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('#') and len(p) > 50:
            description = p[:500]  # First 500 chars for richer context
            break
    
    # Extract key headings/concepts for later encoding
    headings = re.findall(r'^#{1,3}\s+(.+)$', content, re.MULTILINE)
    key_terms = headings[:10] if headings else []

    return {
        'title': title,
        'description': description,
        'key_terms': key_terms,
        'content': content[:2000]  # First 2000 chars for richer source material
    }

def create_siml_entry(hex_tag, term_name, concepts, source_file):
    """Create SIML entry files (v2 — proper YAML stubs with status tracking)"""

    # Create directory
    dir_name = f"{hex_tag}_{term_name}"
    term_path = Path(SIML_TERMS_DIR) / dir_name
    term_path.mkdir(parents=True, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    human_name = term_name.replace('_', ' ')

    # term.yaml — proper YAML structure matching SIML v1.3 + Addendum v0.1
    term_data = {
        'term_id': hex_tag,
        'hex_tag': f'#{hex_tag}',
        'name': term_name,
        'term': human_name,
        'status': 'stub_requires_encoding',
        'description': concepts['description'][:500],
        'source': source_file,
        'date_processed': today,
        'processed_by': 'learning_siml_processor/v2',
        'siml_version': '1.3',
    }

    with open(term_path / "term.yaml", 'w', encoding='utf-8') as f:
        yaml.dump(term_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    # nemetic.phi — stub with term-specific name, not generic operators
    phi_content = f"""# NEMETIC STRING
# {human_name} ({hex_tag})
# Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}
# SIML: v1.3
# STATUS: stub_requires_encoding — run /encode-term {hex_tag} to complete

\u03a6({term_name}) = \u03c3(...) \u2218 \u03c1(...) \u2218 \u03bb(...) \u2218 \u03b2(...) \u2218 \u03b4\u03b3(...) \u2218 \u03bc(...) + \u03b5 | :open

# OPERATOR BREAKDOWN
# Primary: (requires encoding)
# Secondary: (requires encoding)

# Z-STATE: (requires assessment)
# TENDENCY: (requires assessment)

# CE-STATE: unknown
# EI-NOTE: (requires assessment)
"""

    (term_path / "nemetic.phi").write_text(phi_content, encoding='utf-8')

    # insight.md — structured stub with all required sections marked for completion
    insight_content = f"""---
insight_id: INSIGHT_{datetime.now().strftime("%Y%m%d_%H%M")}_{term_name}_{hex_tag}
term: "{human_name}"
hex_tag: "#{hex_tag}"
generated_at: "{datetime.now().isoformat()}"
source: "{source_file}"
status: stub_requires_encoding
siml_version: "1.3"
---

# SIML Insight: {human_name}

## Core Definition

{concepts['description']}

---

## SIML Encoding

*(Requires /encode-term completion)*

---

## Elemental Emphasis Analysis

### \u2234 Air \u2014 The Distinction-Maker
*(To be completed)*

### \u2248 Water \u2014 The Resonance-Keeper
*(To be completed)*

### \u25b2 Fire \u2014 The Direction-Holder
*(To be completed)*

### \U000100b7 Wood \u2014 The Possibility-Brancher
*(To be completed)*

### \u2637 Earth \u2014 The Grounding-Force
*(To be completed)*

### \u26e8 Metal \u2014 The Structure-Guardian
*(To be completed)*

---

## Causal Emergence Assessment (v1.3)

*(Requires assessment)*

---

## Source Material

{concepts['content'][:1000]}

---

*Generated by learning_siml_processor v2 | SIML v1.3*
*Status: stub_requires_encoding*
"""

    (term_path / "insight.md").write_text(insight_content, encoding='utf-8')

    return term_path

def process_next_file():
    """Process the next file in queue"""
    
    # Pull latest source first
    pull_latest_source()
    
    manifest = load_manifest()
    
    # Get list of files in source directory
    source_files = sorted([f for f in os.listdir(SOURCE_DIR) if f.endswith('.md')])
    
    # Filter out already processed files
    processed_files = {p['source_file'] for p in manifest.get('processed', [])}
    source_files = [f for f in source_files if f not in processed_files]
    
    # Skip files that were already processed as duplicates (L101-L105, L103-L105)
    # These were from the incorrect source directory
    skip_files = {
        '10 - Memory Reconsolidation and Machine Unlearning.md',
        '11 - Memory Pruning and Revisiting.md',
        '12 - Thermodynamic Learning Efficiency.md',
        '13 - Kolb\'s Learning Styles and Bloom\'s Taxonomy.md',
        '14 - Educational Game Design Principles.md',
        '15 - Neuroplasticity and Brain-Computer Interfaces.md',
        '16 - Direct Brain Skill-Writing via fMRI.md',
        '17 - AI-Personalized Math Tutoring.md',
    }
    source_files = [f for f in source_files if f not in skip_files]
    
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
    
    # Get hex tag (manifest is updated inside get_next_hex_tag for gap-filling)
    hex_tag, registry, manifest = get_next_hex_tag('L', manifest)
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
        'siml_path': str(term_path),
        'status': 'stub_requires_encoding'
    }
    
    if 'processed' not in manifest:
        manifest['processed'] = []
    manifest['processed'].append(processed_entry)
    
    if 'log' not in manifest:
        manifest['log'] = []
    manifest['log'].append(f"[{datetime.now().isoformat()}] Processed {next_file} as {hex_tag}")
    
    save_manifest(manifest)
    
    # Note: Source files are NOT deleted from Memetic_Ecology repo
    # They are tracked as processed in the manifest
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
