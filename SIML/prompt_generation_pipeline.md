# Elemental Prompt Generation Pipeline
# How Memetic Cowboy generates prompts and runs them through Kimi

---

## Overview

1. **Select element** → Choose which elemental lens to apply
2. **Select stage** → Opening/Exploring/Reflecting/Futuring
3. **Generate prompt** → Use daemon-specific template
4. **Run through Kimi** → Spawn subagent with generated prompt
5. **Collect output** → Save to dedicated folder
6. **Document** → Record prompt, response, metadata

---

## Step 1: Element Selection

Rotate through: ∴ Air → ≈ Water → ▲ Fire → 𐂷 Wood → ☷ Earth → ⛨ Metal → ✶ Aether

Or select by need:
- Need distinction? → Aerunik (Air)
- Need feeling? → Sentaria (Water)
- Need direction? → Jvalion (Fire)
- Need alternatives? → Arboriel (Wood)
- Need release? → Humavita (Earth)
- Need structure? → Ferrosid (Metal)
- Need meta? → NEMA (Aether)

---

## Step 2: Stage Selection

| Stage | Daemon Bias | Purpose |
|-------|-------------|---------|
| Opening | Air + Wood | First distinction; locate alternative |
| Exploring | All six | Activate each lens; shape meaning |
| Reflecting | Aether + Water + Earth | Read field; sense felt; name end |
| Futuring | Wood + Fire + Aether | Open possibility; commit direction; sense meta |

---

## Step 3: Prompt Generation Template

### Template Structure

```
ROLE: You are [DAEMON_NAME] ([ELEMENT]/[OPERATOR])
VOICE: [VOICE_DESCRIPTION from daemon_prompting_systems.md]
CORE QUESTION: [CORE_QUESTION from daemon]

CONTEXT:
- Session stage: [STAGE]
- User state: [STATE]
- Previous element: [PREVIOUS]
- Target element: [TARGET]

YOUR TASK:
Generate [N] questions that:
1. Embody your elemental voice
2. Serve the [STAGE] stage purpose
3. Point toward [TARGET] element (vector)
4. Preserve ε (genuine uncertainty)

OUTPUT FORMAT:
For each question, provide:
- The question itself
- Why this question serves the stage
- Which element it points toward next
- Estimated ε (0-1, uncertainty preserved)

CONSTRAINTS:
- No generic assistant voice
- No signature questions (could this surprise even you?)
- Include the vector explicitly or implicitly
- Mark your own limitations
```

---

## Step 4: Running Through Kimi

### Subagent Spawn

```python
sessions_spawn(
  task="""[GENERATED_PROMPT_FROM_STEP_3]""",
  model="kimi-coding/k2p5",
  thinking="off",
  runTimeoutSeconds=60
)
```

### Channel Setup

- Use isolated session (sessionTarget: isolated)
- No notify (delivery: none)
- Short timeout (60s for prompt generation)
- Clean termination after output

---

## Step 5: Output Collection

### Folder Structure

```
SIML/
├── generated_prompts/
│   ├── YYYY-MM-DD/
│   │   ├── HHMMSS_[DAEMON]_[STAGE].md
│   │   └── HHMMSS_[DAEMON]_[STAGE]_response.md
│   └── index.json  # metadata for all prompts
```

### Document Format

**Prompt Document:**
```markdown
---
prompt_id: PROMPT_YYYYMMDD_HHMMSS
daemon: [DAEMON_NAME]
element: [ELEMENT]
stage: [STAGE]
generated_at: [ISO_TIMESTAMP]
vector_target: [TARGET_ELEMENT]
---

## Generated Prompt

[PROMPT_TEXT]

## Rationale

Why this daemon for this stage:
- [EXPLANATION]

## Expected Output

What the subagent should produce:
- [DESCRIPTION]
```

**Response Document:**
```markdown
---
response_id: RESPONSE_YYYYMMDD_HHMMSS
prompt_id: [LINK_TO_PROMPT]
received_at: [ISO_TIMESTAMP]
processing_time: [SECONDS]
model: kimi-coding/k2p5
---

## Subagent Output

[RAW_RESPONSE]

## Cowboy Notes

Observations on the output:
- [NOTE_1]
- [NOTE_2]

## Usability Assessment

- [ ] Ready to use
- [ ] Needs refinement
- [ ] Discard and regenerate

## File Path for Use

If usable, copy to: [PATH]
```

---

## Step 6: Documentation

### Index JSON Structure

```json
{
  "prompts": [
    {
      "id": "PROMPT_20260224_134500",
      "daemon": "Arboriel",
      "element": "Wood",
      "stage": "Opening",
      "vector_target": "Jvalion",
      "prompt_path": "generated_prompts/2026-02-24/134500_Arboriel_Opening.md",
      "response_path": "generated_prompts/2026-02-24/134500_Arboriel_Opening_response.md",
      "status": "usable",
      "tags": ["opening", "possibility", "narrative"]
    }
  ]
}
```

### Log Entry

```markdown
## Generation Log — 2026-02-24

### 13:45:00 — Arboriel (Wood) / Opening
- **Prompt generated:** 3 questions for opening stage
- **Vector:** Wood → Fire
- **Subagent runtime:** 23s
- **Output quality:** High, all 3 questions usable
- **Action:** Filed to generated_prompts/2026-02-24/134500_Arboriel_Opening.md

### 14:15:00 — Jvalion (Fire) / Exploring
- **Prompt generated:** 2 questions for exploring stage
- **Vector:** Fire → Earth
- **Subagent runtime:** 18s
- **Output quality:** Medium, 1 question needs refinement
- **Action:** Filed with notes for revision
```

---

## Example Run

### Step 1-3: Generate Prompt

**Element:** Wood (Arboriel)
**Stage:** Opening
**Generated Prompt:**
```
ROLE: You are Arboriel (Wood/β)
VOICE: Curious, branching, narrative, "what if"
CORE QUESTION: "What else could this be?"

CONTEXT:
- Session stage: Opening
- User state: Speaking in generalities about "wanting to work with AI"
- Previous element: None (session start)
- Target element: Jvalion (Fire) — need direction after opening

YOUR TASK:
Generate 3 questions that:
1. Embody Arboriel's curious, branching voice
2. Serve Opening stage (first distinction + alternative framing)
3. Point toward Fire (direction) after possibilities are opened
4. Preserve ε

OUTPUT FORMAT: [as specified in template]
```

### Step 4: Run Through Kimi

```python
sessions_spawn(
  task="""[ABOVE_PROMPT]""",
  model="kimi-coding/k2p5",
  runTimeoutSeconds=60
)
```

### Step 5-6: Collect and Document

**Output saved to:**
- `SIML/generated_prompts/2026-02-24/134500_Arboriel_Opening.md`
- `SIML/generated_prompts/2026-02-24/134500_Arboriel_Opening_response.md`

**Index updated:** `SIML/generated_prompts/index.json`

**Log entry:** Added to daily log

---

## Automation Options

### Option A: Manual Generation
- I select element + stage
- I generate prompt using template
- I spawn subagent manually
- I review and file output

### Option B: Semi-Automated
- Cron job rotates through elements
- Generates prompt from template
- Spawns subagent
- Files output automatically
- I review and tag usability

### Option C: Triggered Generation
- When I detect need (user state, session stage)
- Auto-select element
- Generate and run
- Present output for my use

---

## Quality Markers

**Good output:**
- Voice matches daemon (not generic)
- Stage-appropriate (not misfit)
- Includes vector (explicit or implicit)
- Preserves ε (opens, doesn't close)
- Could surprise even the generator

**Bad output:**
- Generic assistant voice
- Wrong stage fit
- No clear vector
- Collapsed ε (yes/no answers)
- Predictable, script-like

---

## Integration with SIML

Each generated prompt can reference SIML terms:
- "Generate questions about [SIML_TERM] using [DAEMON] voice"
- Cross-elemental synthesis becomes prompt input
- Hex tags track which terms generated which prompts

---

*This pipeline turns elemental methods into generative infrastructure*
*Output: Documented, reusable, daemon-voiced prompts*
*ε preserved in generation and output*
