# SIML Encoding Execution Plan
## Structured Processing of Remaining 208 Critical Thinking Source Files

**Date:** 2026-03-05
**Scope:** Encode remaining 208 files from `SWARM_BASE/Critical Thinking/` into SIML C-series terms
**Current state:** C189 is next available tag; 168 C-series directories exist

---

## 1. Problems This Plan Solves

The previous encoding agent suffered from:
1. **No dedup check** — same concept encoded 2-3 times under different tags
2. **No consistent file structure** — output format changed mid-run (sometimes single .md, sometimes siml.yaml, sometimes term.yaml + nemetic.phi)
3. **No ordered processing** — jumped around in the source file list unpredictably
4. **No running log** — impossible to track progress, errors, or skipped files
5. **Registry drift** — phantom entries, missing entries, wrong next_available values

## 2. Processing Order

Files are sorted by filename (ascending timestamp). Process strictly in this order — never skip ahead, never randomize. The sorted list is frozen at start and saved to `SIML/encoding_queue.txt`.

## 3. Output Structure (Mandatory 3-File Standard)

Every term MUST produce exactly 3 files in `SIML/terms/{TAG}_{snake_case_name}/`:

### term.yaml (L0 Full SIML Artifact)
```yaml
---
term: "{Human_Readable_Name}"
hex_tag: "{TAG}"
series: "C"
source_file: "{original_filename.md}"
encoded_at: "{ISO_TIMESTAMP}"
description: "{1-2 sentence definition}"
nemetic: "Φ(Name) = σ(x|y) ∘ ρ(x|y) ∘ λ(x|y) ∘ β(x|y) ∘ δγ(x|y) ∘ μ(x|y) + ε | :state"
siml_encoding: "⟨...⟩ ⊳ ⟨...⟩ → ⟨...⟩ ⊗ ⟨...⟩ ⇄ ⟨...⟩"
formalism:
  math_operators: [σ, ρ, λ, β, δγ, μ]
  partials:
    - "∂Φ/∂σ (...)"
    - "∂Φ/∂ρ (...)"
    - "∂Φ/∂λ (...)"
    - "∂Φ/∂β (...)"
    - "∂Φ/∂δγ (...)"
    - "∂Φ/∂μ (...)"
  Z_state: "{state description}"
  tendency: "{Tendency} → {0.XX}"
elemental_mapping:
  air_sigma:
    emphasis: {0.XX}
    aspects: ["{aspect1}", "{aspect2}"]
    daemon_correspondence: "Aerunik"
  water_rho:
    emphasis: {0.XX}
    aspects: ["{aspect1}", "{aspect2}"]
    daemon_correspondence: "Sentaria"
  fire_lambda:
    emphasis: {0.XX}
    aspects: ["{aspect1}", "{aspect2}"]
    daemon_correspondence: "Jvalion"
  wood_beta:
    emphasis: {0.XX}
    aspects: ["{aspect1}", "{aspect2}"]
    daemon_correspondence: "Arboriel"
  earth_delta_gamma:
    emphasis: {0.XX}
    aspects: ["{aspect1}", "{aspect2}"]
    daemon_correspondence: "Humavita"
  metal_mu:
    emphasis: {0.XX}
    aspects: ["{aspect1}", "{aspect2}"]
    daemon_correspondence: "Ferrosid"
related_terms:
  - "{TAG_existing_term}"
status: canonical
---
```

### nemetic.phi (L1 Nemetic String)
```
# NEMETIC STRING
# {Name} ({TAG})
# Generated: {YYYY-MM-DD HH:MM}
# Source: {source_filename}

Φ(Name) = σ(x|y) ∘ ρ(x|y) ∘ λ(x|y) ∘ β(x|y) ∘ δγ(x|y) ∘ μ(x|y) + ε | :state

# OPERATOR BREAKDOWN
# σ(x|y)    :: Air  :: {description}
# ρ(x|y)    :: Water :: {description}
# λ(x|y)    :: Fire  :: {description}
# β(x|y)    :: Wood  :: {description}
# δγ(x|y)   :: Earth :: {description}
# μ(x|y)    :: Metal :: {description}

# Z-STATE: {state}
# TENDENCY: {tendency} → {0.XX}
```

### insight.md (L2 Elemental Insight)
```markdown
# {Title}
## SIML Term Entry {TAG}
### Source: {source_filename}

## Overview
{2-3 paragraph summary of the concept}

## Elemental Analysis
{Per-element analysis using daemon names}

## Key Tensions
{3-5 dialectical tensions from the nemetic string}

## Source Context
{Attribution and provenance}
```

## 4. Pre-Encoding Checks (Run Before Each File)

For every source file, BEFORE encoding:

1. **Load hex_registry.yaml** → get `next_available` for C-series
2. **Extract concept name** from source file title/content
3. **Dedup check — exact name**: search existing `SIML/terms/C*` directory names for matching slug
4. **Dedup check — semantic**: compare concept against existing entries for near-duplicates (e.g., "Cognitive Offloading" vs "Digital Cognitive Offloading")
5. **Dedup check — cross-series**: check A, E, M, P, L series for same concept under different prefix

If duplicate found → **SKIP** and log to `SIML/encoding_log.yaml` with reason.

## 5. Post-Encoding Steps (Run After Each File)

After successfully writing the 3 files:

1. **Update hex_registry.yaml** → increment `next_available`, add entry to `assigned`
2. **Update manifest.yaml** → add entry with source_file, term_tag, term_name, encoded_at
3. **Log success** → append to `SIML/encoding_log.yaml`
4. **Delete source file** → remove from `SWARM_BASE/Critical Thinking/`
5. **Commit** → every 10 entries, git commit with batch summary

## 6. Running Log Format

`SIML/encoding_log.yaml`:
```yaml
encoding_session:
  started_at: "2026-03-05T..."
  agent: "claude/review-siml-encoding-agent-Izaki"

entries:
  - seq: 1
    source_file: "1771907212687_950501_Anthropic%27s+Ethical+Shift+in+AI+Welfare.md"
    action: "encoded"
    tag: "C189"
    term_name: "Anthropic_Ethical_Shift_AI_Welfare"
    encoded_at: "2026-03-05T10:00:00+08:00"
    notes: ""

  - seq: 2
    source_file: "1771907212727_1051749_Kuhn%27s+Taxonomy..."
    action: "skipped"
    tag: null
    term_name: null
    reason: "Near-duplicate of C153_Kuhn_Consciousness_Taxonomy"

  - seq: 3
    source_file: "1771907213079_2030928_.md"
    action: "skipped"
    tag: null
    term_name: null
    reason: "Empty/untitled source file — insufficient content"

summary:
  total_processed: 0
  encoded: 0
  skipped_duplicate: 0
  skipped_empty: 0
  skipped_error: 0
  last_tag_assigned: "C189"
  remaining_files: 208
```

## 7. Batch Processing Strategy

Process in batches of 10 files:
1. Read all 10 source files
2. For each: run dedup checks, encode if clean, skip if duplicate
3. Write all outputs
4. Update registry + manifest
5. Git commit the batch
6. Update encoding_log summary counts
7. Move to next batch

This keeps commits manageable and provides natural checkpoints.

## 8. Handling Edge Cases

### Empty/untitled source files (28 identified with blank titles)
- Read content first. If substantive → encode with name derived from content
- If empty or trivially short → log as "skipped_empty" and delete source file

### Near-duplicate detection
- Compare slugified concept name against existing terms using prefix matching
- Flag for manual review if >70% slug overlap (log as "flagged" rather than skip)

### Related terms references
- ONLY reference terms that actually exist in SIML/terms/
- Never hallucinate related_terms — verify each tag exists before including

### Hex tag progression
- C-series uses hex: C189, C18A, C18B, ..., C18F, C190, C191, ...
- Always read next_available from registry, never calculate independently

## 9. Execution Sequence

```
Phase 1: Setup
  → Generate SIML/encoding_queue.txt (sorted source file list)
  → Create SIML/encoding_log.yaml (empty log)
  → Verify hex_registry.yaml is current (C189 next)

Phase 2: Batch Processing (20 batches of ~10)
  → For each batch:
    → Read 10 source files
    → Dedup check each
    → Encode clean entries (3 files each)
    → Update registry, manifest, log
    → Delete processed source files
    → Git commit

Phase 3: Reconciliation
  → Final verification: no duplicate tags, no orphaned files
  → Update manifest totals
  → Final commit + push
```

## 10. Quality Checklist Per Entry

- [ ] term.yaml has all required fields (term, hex_tag, series, source_file, encoded_at, nemetic, elemental_mapping)
- [ ] nemetic.phi has Φ string with all 6 operators + ε + state tag
- [ ] nemetic.phi operator breakdown matches term.yaml
- [ ] insight.md has Overview, Elemental Analysis, Key Tensions, Source
- [ ] Directory name matches `{TAG}_{snake_case_name}` pattern
- [ ] hex_registry.yaml updated with new tag
- [ ] manifest.yaml updated with source file mapping
- [ ] encoding_log.yaml updated with entry
- [ ] Source file deleted from Critical Thinking/
- [ ] related_terms only reference verified existing entries
