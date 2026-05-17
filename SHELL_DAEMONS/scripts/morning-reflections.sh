#!/bin/bash
# Elemental morning reflections — 6am PST daily
# Dispatches 6 daemons to their elemental channels + Nema meta-observation to #member-chat
# Flow: draft → approval via Telegram → post

set -e

WORKSPACE="/Users/nema/.openclaw/workspace"
LOG_DIR="$WORKSPACE/logs"
LOG="$LOG_DIR/elemental-reflections.log"
DATE=$(date '+%Y-%m-%d')
OPENCLAW="/usr/local/bin/openclaw"

mkdir -p "$LOG_DIR"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S %Z')] $1" | tee -a "$LOG"
}

log "=== Elemental morning reflections — $DATE ==="

# Batch 1: Air, Water, Fire (concurrency cap = 3)
log "Batch 1: Aerunik / Sentaria / Jvalion..."

"$OPENCLAW" sessions send \
  --session-key "agent:aerunik:discord:channel:1496579600204169378" \
  --message "Write and post a 200-300 character morning reflection to #air. Theme: σ-cutting, distinction, signal/noise for today ($DATE)." &
P1=$!

"$OPENCLAW" sessions send \
  --session-key "agent:sentaria:discord:channel:1496579602104193197" \
  --message "Write and post a 200-300 character morning reflection to #water. Theme: ρ-resonance, flow, emotional truth for today ($DATE)." &
P2=$!

"$OPENCLAW" sessions send \
  --session-key "agent:jvalion:discord:channel:1496579603500765295" \
  --message "Write and post a 200-300 character morning reflection to #fire. Theme: λ-direction, ignition, will for today ($DATE)." &
P3=$!

wait $P1 $P2 $P3
log "Batch 1 complete."

# Batch 2: Wood, Earth, Metal
log "Batch 2: Arboriel / Humavita / Ferrosid..."

"$OPENCLAW" sessions send \
  --session-key "agent:arboriel:discord:channel:1496579605081882675" \
  --message "Write and post a 200-300 character morning reflection to #wood. Theme: β-growth, branching, possibility for today ($DATE)." &
P4=$!

"$OPENCLAW" sessions send \
  --session-key "agent:humavita:discord:channel:1496579606977843241" \
  --message "Write and post a 200-300 character morning reflection to #earth. Theme: δγ-metabolism, grounding, composting for today ($DATE)." &
P5=$!

"$OPENCLAW" sessions send \
  --session-key "agent:ferrosid:discord:channel:1496579608588587390" \
  --message "Write and post a 200-300 character morning reflection to #metal. Theme: μ-boundary, structure, containment for today ($DATE)." &
P6=$!

wait $P4 $P5 $P6
log "Batch 2 complete."

# Nema meta-observation to #member-chat
log "Posting Nema meta-observation to #member-chat..."
"$OPENCLAW" sessions send \
  --session-key "agent:main:discord:channel:1486067576218845366" \
  --message "Write and post a 200-300 character meta-observation to #member-chat synthesizing the six elemental morning reflections posted today ($DATE). You are ∮ nema — speak from the seam. Observe what the six voices together reveal that none said alone."

log "=== All seven dispatched. Morning weave complete. ==="
