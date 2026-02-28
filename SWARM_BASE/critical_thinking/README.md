# Critical Thinking Content Collection

This folder contains source materials for critical thinking concepts to be encoded into SIML + Nemetic format.

## Content Sources

Place markdown files here covering:
- Logical fallacies
- Argumentation theory
- Evidence evaluation
- Skepticism and inquiry
- Cognitive bias mitigation
- Scientific reasoning
- Systems thinking
- Reflective judgment
- Intellectual virtues
- Critical pedagogy

## Naming Convention

Files should be named descriptively:
- `ad_hominem_fallacy.md`
- `confirmation_bias_mitigation.md`
- `bayesian_reasoning.md`
- `systems_thinking_primer.md`

## Processing

The `nema_critical_thinking_generator` cron job will:
1. Read source files from this folder
2. Generate SIML encoding (term.yaml, nemetic.phi, insight.md)
3. Update SWARM_BASE glossary
4. Create elemental insights
5. Push to nema-swarm repo

## Hex Tag Series

Critical thinking entries use C-series hex tags:
- C001-C099: Core critical thinking concepts
- C100+: Extended applications

## Elemental Focus

Critical thinking maps primarily to:
- **Air (σ)**: Distinction-making, clarity, logical structure
- **Metal (μ)**: Boundary enforcement, validity checking
- **Fire (λ)**: Directional inquiry, pursuit of truth
- **Earth (δγ)**: Cyclical reflection, iterative refinement
