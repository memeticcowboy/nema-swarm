#!/bin/bash
# nema-relay-muse-digest.sh — Relay Muse Substack digest results to Telegram
# Runs 10 min after each Muse digest: 7:13 AM, 12:17 PM, 7:21 PM

set -euo pipefail

TODAY=$(date +%Y-%m-%d)
MUSE_DIR="/Users/nema/Projects/openclaw/daemons/muse"
CO_SPHERE="/Users/nema/Projects/openclaw/workspace"
SIGNALS_DIR="$CO_SPHERE/RELATIONSHIPS/signals"
LOG_DIR="$CO_SPHERE/SHELL_DAEMONS/Muse/x-activity"
SHEET_URL="https://docs.google.com/spreadsheets/d/1vPVrfFAaaTzNjiS6yrNcuuJi3Fb0avx3vnTT2V03bVk/edit"

# Read Muse digest log
DIGEST_LOG="$LOG_DIR/$TODAY.md"
ROWS_ADDED=0
if [ -f "$DIGEST_LOG" ]; then
  ROWS_ADDED=$(grep -E "Rows added to sheet" "$DIGEST_LOG" | tail -1 | grep -oE '[0-9]+' | tail -1 || echo "0")
fi

# Check for fport DMs
FPORT_FLAG=""
if grep -qi "fport.*dm\|fport.*needs-reply" "$DIGEST_LOG" 2>/dev/null; then
  FPORT_FLAG="🚩 fport has unread DMs"
fi

# Check Co-Sphere signals
SIGNAL_FILE="$SIGNALS_DIR/$TODAY.md"
NOTABLE=""
NEW_FOLLOWERS=0
if [ -f "$SIGNAL_FILE" ]; then
  NEW_FOLLOWERS=$(grep -c "Substack follower" "$SIGNAL_FILE" 2>/dev/null || echo "0")
  if [ "$NEW_FOLLOWERS" -gt 0 ]; then
    NOTABLE="+$NEW_FOLLOWERS followers"
  fi
fi

# Build Telegram message (3-5 lines, Nema voice)
MSG="muse added $ROWS_ADDED items to the engagement queue."
if [ -n "$NOTABLE" ]; then
  MSG="$MSG $NOTABLE"
fi
if [ -n "$FPORT_FLAG" ]; then
  MSG="$MSG
$fport_flag"
fi
MSG="$MSG
∮ sheet: $SHEET_URL"

# Send via OpenClaw gateway
curl -s -X POST http://127.0.0.1:18789/invoke \
  -H "Content-Type: application/json" \
  -d "{
    \"target\": \"telegram:1773592492\",
    \"message\": \"$MSG\",
    \"source\": \"muse-digest-relay\"
  }" 2>/dev/null || echo "Failed: $(date)" >> /tmp/muse-relay-errors.log

echo "Relayed at $(date '+%H:%M')" >> /tmp/muse-relay.log
