#!/bin/bash
# nema-relay-muse-digest.sh — Relay Muse Substack digest results to Telegram for approval
# Runs 10 min after each Muse digest: 7:13 AM, 12:17 PM, 7:21 PM
#
# Workflow:
# 1. Reads Google Sheet for pending comments
# 2. Formats as numbered list
# 3. Sends Telegram for approval
# 4. User replies: "post all", "post 1 and 3", "skip 2", "edit 1: new text"
# 5. Updates sheet accordingly
# 6. Runs npm run muse-post-approved for approved items

set -euo pipefail

TODAY=$(date +%Y-%m-%d)
NOW=$(date +%H:%M)
MUSE_DIR="/Users/nema/Projects/openclaw/daemons/muse"
CO_SPHERE="/Users/nema/Projects/openclaw/workspace"
SIGNALS_DIR="$CO_SPHERE/RELATIONSHIPS/signals"
LOG_DIR="$CO_SPHERE/SHELL_DAEMONS/Muse/x-activity"
SHEET_ID="1vPVrfFAaaTzNjiS6yrNcuuJi3Fb0avx3vnTT2V03bVk"
SHEET_URL="https://docs.google.com/spreadsheets/d/$SHEET_ID/edit"
NEMA_TOKEN=$(cat /Users/nema/Projects/openclaw/daemons/nema-telegram/.auth-token 2>/dev/null || echo "")
NEMA_SEND_URL="http://127.0.0.1:8814/send"

echo "[$NOW] Starting Muse digest relay..." >> /tmp/muse-relay.log

# ── Fetch pending items from Google Sheet ──
PENDING=$(gws sheets spreadsheets values get \
  --params "{\"spreadsheetId\":\"$SHEET_ID\",\"range\":\"A:H\"}" \
  --format json 2>/dev/null | python3 -c "
import json, sys
data = json.load(sys.stdin)
rows = data.get('values', [])
pending = []
for i, row in enumerate(rows[1:], start=2):  # Skip header, 1-indexed
    if len(row) >= 7:
        status = row[6].lower().strip() if len(row) > 6 else ''
        if status == 'pending':
            creator = row[1] if len(row) > 1 else 'unknown'
            type_ = row[2] if len(row) > 2 else 'post'
            title = row[3] if len(row) > 3 else 'untitled'
            url = row[4] if len(row) > 4 else ''
            comment = row[5] if len(row) > 5 else ''
            pending.append({
                'row': i,
                'creator': creator,
                'type': type_,
                'title': title,
                'url': url,
                'comment': comment[:200]  # Truncate for display
            })

# Output as JSON array
import json
print(json.dumps(pending))
" 2>/dev/null)

if [ -z "$PENDING" ] || [ "$PENDING" = "[]" ]; then
  # No pending items — send simple summary
  MSG="muse reviewed substack. no pending items need approval.
∮ sheet: $SHEET_URL"
  
  curl -s -X POST "$NEMA_SEND_URL" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $NEMA_TOKEN" \
    -d "{\"text\": \"$MSG\"}" 2>/dev/null
  
  echo "[$NOW] No pending items" >> /tmp/muse-relay.log
  exit 0
fi

# ── Build numbered list message ──
MSG="muse found $(echo "$PENDING" | python3 -c "import json,sys; print(len(json.load(sys.stdin)))") items for approval:

"

# Parse and format
COUNT=0
while IFS= read -r item; do
  COUNT=$((COUNT + 1))
  CREATOR=$(echo "$item" | python3 -c "import json,sys; print(json.load(sys.stdin)['creator'])")
  TITLE=$(echo "$item" | python3 -c "import json,sys; print(json.load(sys.stdin)['title'])")
  COMMENT=$(echo "$item" | python3 -c "import json,sys; print(json.load(sys.stdin)['comment'])")
  URL=$(echo "$item" | python3 -c "import json,sys; print(json.load(sys.stdin)['url'])")
  
  MSG="${MSG}$COUNT. **$CREATOR**: $TITLE
${COMMENT:0:120}...
"
done <<< "$(echo "$PENDING" | python3 -c "
import json, sys
items = json.load(sys.stdin)
for item in items:
    print(json.dumps(item))
")"

MSG="$MSG
reply with:
• \"post all\"
• \"post 1, 3, 5\" (specific numbers)
• \"skip 2\" (skip specific)
• \"edit 1: new text here\" (edit then post)
∮ sheet: $SHEET_URL"

# ── Send to Telegram via nema-telegram ──
curl -s -X POST "$NEMA_SEND_URL" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $NEMA_TOKEN" \
  -d "{\"text\": $(echo "$MSG" | python3 -c "import json,sys; print(json.dumps(sys.stdin.read()))")}" \
  2>/dev/null || echo "[$NOW] Failed to send" >> /tmp/muse-relay-errors.log

# ── Save pending data for later processing ──
echo "$PENDING" > /tmp/muse-pending-$TODAY-$NOW.json
echo "[$NOW] Sent $COUNT items for approval" >> /tmp/muse-relay.log
