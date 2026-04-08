---
title: SIMLab & SIMLHEX Monitor — Service Architecture
version: 1.0
date: April 2026
status: Built, not yet deployed
scope: Two new backend services for SIML encoding and SIMLHEX drift monitoring
depends: SIML v1.3, SIMLHEX-CANONICAL, PATHOLOGY_MATRIX, daemon servers
---

# SIMLab & SIMLHEX Monitor

Two new backend services that support your (Nema's) SIML encoding and session monitoring capabilities. Neither has a Discord bot. Neither posts to Discord directly. They return results to you or Bert, and you handle Discord communication.

---

## SIMLab — SIML Encoding Laboratory

**Port:** 8812
**Role:** Generate, validate, and publish SIML v1.3 artifacts
**Invoked by:** Nema, Bert, or Daniel via HTTP

### What It Does

SIMLab runs a two-pass encoding pipeline:

1. **Pass 1 — Local LLM (fast draft):** A fine-tuned Qwen 2.5 7B model (running on port 8820) generates a first draft of nemetic strings, term.yaml, or SWARM_BASE entries. It's fast and free but rough on operator semantics.

2. **Pass 2 — Claude (quality control):** Claude reviews the draft against SIML v1.3 specs, corrects operator mappings, fixes tags and format, and produces publication-ready output.

Corrections are logged to `training-data/corrections.jsonl` — these feed the next fine-tuning round, so the local LLM improves over time.

### Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/status` | Health check (includes local LLM status) |
| POST | `/encode` | Two-pass encoding pipeline |
| POST | `/invoke` | Generic prompt (for compatibility with daemon routing) |

### How to Invoke (from Nema or Bert)

SIMLab uses the same pattern as the elemental daemons — HTTP POST with bearer token auth on localhost.

**Auth token:** `/Users/nema/Projects/openclaw/daemons/simlab/.auth-token`
**Endpoint:** `http://127.0.0.1:8812`

**Encode a SIML term (primary use case):**
```bash
TOKEN=$(cat /Users/nema/Projects/openclaw/daemons/simlab/.auth-token)
curl -X POST http://127.0.0.1:8812/encode \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "concept": "Burnout",
    "context": "Progressive depletion through sustained overcommitment",
    "hex": "BRN1",
    "publish": true
  }'
```

**Generic invoke (same pattern as daemon /invoke):**
```bash
curl -X POST http://127.0.0.1:8812/invoke \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Generate a SWARM_BASE glossary for healthcare worker burnout",
    "context": "Session preparation for 6 participants"
  }'
```

**Check status:**
```bash
curl http://127.0.0.1:8812/status
```

Response from `/encode` includes: `draft` (local LLM output), `reviewed` (Claude-corrected output), and `published` (GitHub URLs if publish=true).

### Daemon Endpoint Reference (for Nema's routing)

```
Daemon endpoints (localhost, bearer auth):
- Aerunik:          http://127.0.0.1:8801/invoke
- Sentaria:         http://127.0.0.1:8802/invoke
- Jvalion:          http://127.0.0.1:8803/invoke
- Arboriel:         http://127.0.0.1:8804/invoke
- Humavita:         http://127.0.0.1:8805/invoke
- Ferrosid:         http://127.0.0.1:8806/invoke
- MC:               http://127.0.0.1:8810/invoke
- SIMLab (encode):  http://127.0.0.1:8812/encode   ← use this for SIML terms
- SIMLab (generic): http://127.0.0.1:8812/invoke   ← use this for freeform requests
```

All use bearer token auth. Token files at `/Users/nema/Projects/openclaw/daemons/{name}/.auth-token`.

### What It Produces

- **term.yaml** — L0 Full SIML Artifact (v1.3 with coords.ce)
- **nemetic.phi** — L1 Nemetic String with CE-STATE
- **insight.md** — Elemental insight analysis
- **SWARM_BASE glossaries** — Session preparation materials

### Publishing

SIMLab can write to the nema-swarm GitHub repo and return URLs. You (Nema) post those URLs in Discord — SIMLab does not.

---

## SIMLHEX Monitor — Drift & Pathology Detection

**Port:** 8811
**Role:** Real-time monitoring of daemon responses for SIMLHEX drift and pathology signatures
**Alerts:** Sent to Nema's OpenClaw gateway (port 18789) when thresholds are exceeded

### What It Does

Every time a daemon responds (Aerunik, Sentaria, etc.), the shared daemon server automatically sends a copy of the response to the monitor. The monitor:

1. **Algorithmic scoring (every message):**
   - Operator frequency distribution across sliding window
   - Daemon charisma decay (which daemons are being underused)
   - Compound pathology pattern matching (all 7 modes)

2. **LLM-assisted semantic drift (every 5th message):**
   - Descriptive→Referential drift (definite articles on SIML terms)
   - Diagnostic→Explanatory drift (naming replacing investigation)
   - Map→Terrain drift (framework references replacing observation)

### Alert Schema

When thresholds are exceeded, the monitor sends alerts to your gateway:

```json
{
  "source": "simlhex-monitor",
  "type": "drift-alert",
  "alert": {
    "type": "pathology-signature",
    "pathology": "Choke",
    "signature": "σ↑ ∧ μ↑",
    "counter": ["β", "ρ"],
    "confidence": "0.75",
    "message": "Pathology signature: Choke (σ↑ ∧ μ↑). Counter: β + ρ."
  }
}
```

### Your Response Options

When you receive an alert:
- **dismiss** — false positive, monitor continues
- **watch** — monitor tracks, you note it
- **intervene** — invoke the counter-daemons suggested
- **halt** — pause the session, alert the user

### Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/status` | Buffer size, window state, daemon distribution, recent alerts |
| POST | `/ingest` | Receive daemon response (auto-sent by daemon servers) |
| GET | `/window` | View current sliding window state |
| GET | `/alerts` | View recent alert history |

### Thresholds (configurable in config.json)

- Operator concentration: >60% of one operator in window
- Charisma decay: 3+ daemons absent from last 10+ messages
- Drift confidence: >0.7 to fire alert
- Min messages before alerting: 5

---

## Local SIML LLM

**Port:** 8820
**Model:** Qwen 2.5 7B Instruct (4-bit quantized) + LoRA adapter
**Shared by:** SIMLab (encoding) and SIMLHEX Monitor (drift scoring)

This is a fine-tuned model trained on the SIML corpus (973 term artifacts, 88 simulated prompting sessions, SIMLHEX specs, pathology matrix). It handles:
- Fast draft nemetic string generation
- Operator pattern recognition
- Drift signal scoring

It runs via mlx-lm on Apple Silicon. The adapter is at `/Users/nema/Projects/openclaw/training-data/adapters/`.

---

## Boot Commands

```bash
cd /Users/nema/Projects/openclaw/daemons

# Start everything
./start-swarm.sh

# Start only SIMLab stack
./start-swarm.sh simlab-llm simlab

# Start only the monitor
./start-swarm.sh simlhex-monitor

# Note: simlab-llm must start before simlab and simlhex-monitor
# (they query it, but gracefully handle it being offline)
```

---

## Architecture Summary

```
Nema/Bert → SIMLab (:8812) → Local LLM (:8820) + Claude → SIML corpus + GitHub
Daemons → SIMLHEX Monitor (:8811) → Local LLM (:8820) → Alert Nema (:18789)
```

SIMLab and the Monitor share the local LLM but don't compete — monitor prompts are tiny (~200 tokens), encoding prompts are larger but infrequent.

---

*SIMLab encodes. The Monitor watches. Nema decides.*
