#!/bin/bash
# Delete messages from elemental daemon channels (excluding archive thread starters and pointer notices)

CHANNELS=(
  "1496579600204169378:aerunik"
  "1496579602104193197:sentaria"
  "1496579603500765295:jvalion"
  "1496579605081882675:arboriel"
  "1496579606977843241:humavita"
  "1496579608588587390:ferrosid"
)

# Message IDs to preserve (archive thread starters and pointer notices)
# These are the most recent 3 messages in each channel (thread starter + pointer + sometimes newsletter)
# We want to delete everything OLDER than these

for entry in "${CHANNELS[@]}"; do
  IFS=: read -r channel_id name <<< "$entry"
  echo "=== Processing $name ($channel_id) ==="
  
  # Get message IDs to delete (skip the most recent 2-3 messages)
  # The pointer notice and thread starter should be preserved
  openclaw message read --channel-id "$channel_id" --limit 50 2>/dev/null | \
    jq -r '.messages[] | select(.author.id != "1486071735748001864" or (.content | contains("Archive Notice") | not)) | .id' | \
    tail -n +3 | \
    while read -r msg_id; do
      if [ -n "$msg_id" ]; then
        echo "Deleting $msg_id from $name..."
        openclaw message delete --channel-id "$channel_id" --message-id "$msg_id" 2>&1 || echo "Failed to delete $msg_id"
        sleep 2
      fi
    done
  
  echo "=== $name processing complete ==="
  sleep 5
done

echo "All channels processed."
