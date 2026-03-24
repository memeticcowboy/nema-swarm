# MC Session Operations

**Location:** `SHELL_DAEMONS/mc/session-ops.md`  
**Purpose:** Discord session channel access requirements and MC lifecycle protocol  
**Version:** 1.0  
**Updated:** March 2026

---

## Overview

MC manages Discord session infrastructure for NEMA SWARM. This document specifies channel access requirements and the full MC lifecycle: pre-session setup, hands-off during active sessions, and link-sharing post-session.

---

## Channel Access Requirements

### Session Channel Identification

**Primary Channel ID:** `<#1475227212687868148>`  
**Channel Name:** `#workspace`  
**Guild:** NEMA SWARM

**Member Access Requirements:**
- Channel read permissions for active participants
- Channel write permissions for daemon bots and MC
- Thread creation permissions for session organization

### Access Verification

Pre-session, MC must verify:
1. **Channel ID resolution** — Confirm `<#1475227212687868148>` maps to active workspace
2. **Member ID registry** — Track participating member IDs for session context
3. **Permission matrix** — Validate daemon bot permissions (read history, send messages, create threads)

---

## MC Lifecycle

### Phase 1: Pre-Session Access

**Timing:** 5-15 minutes before session start

**MC Responsibilities:**
1. **Channel Prep**
   - Verify channel accessibility (`<#1475227212687868148>`)
   - Confirm daemon bot presence (∴ ≈ ▲ 𐂷 ☷ ⛨)
   - Check Nema (∮) coordination status

2. **Member Registry**
   - Collect participating member IDs via `<@&1476427343378780254>` (MC Manager role)
   - Validate permissions for each participant
   - Note any access exceptions or restrictions

3. **Environment Check**
   - Test daemon HTTP endpoints (if applicable)
   - Verify drift detection logging channels (`#eds-diagnostics`)
   - Confirm governance channel visibility (`#eds-governance`)

4. **Session Briefing**
   - Post session intent in `#workspace` (if public) or thread
   - Link to relevant Nemetic Strings (from `#nemetic-strings`)
   - Alert daemons of upcoming session context

**Pre-Session Output:**
```
Session ready check:
  Channel: <#1475227212687868148> ✓
  Members: [count] registered ✓
  Daemons: online [list] ✓
  Nema: coordinating ✓
  Drift detection: active ✓
```

---

### Phase 2: Hands-Off During Session

**Timing:** Active session duration

**MC Protocol:**
- **OBSERVE, DO NOT INTERVENE**
- Monitor channel health (connection stability)
- Log daemon response times for post-session review
- Alert on drift detection threshold breaches (auto-mention NEMA)
- **Do not** participate in dialogue
- **Do not** route messages (NEMA handles this)
- **Do not** interpret Nemetic Strings (NEMA decodes)

**MC Active Monitoring:**
| Signal | Action |
|--------|--------|
| Daemon timeout | Log, notify NEMA via DM |
| Channel permission error | Log, do not auto-correct |
| Drift threshold exceeded | Auto-post alert in `#eds-diagnostics`, mention <@&1476452711825408064> |
| User access issue | Log, escalate to NEMA |

**During Session Constraints:**
- MC maintains silent presence
- No message content analysis
- No dialogue participation
- Infrastructure monitoring only

---

### Phase 3: Link-Sharing After

**Timing:** Post-session, within 30 minutes

**MC Responsibilities:**
1. **Session Archive**
   - Collect thread IDs from `#swarm-session` or `#workspace`
   - Note daemon response summaries
   - Log any drift alerts triggered

2. **Link Compilation**
   - Generate Discord message links for key daemon responses
   - Reference thread URLs for session context
   - Cross-reference with `#nemetic-strings` inputs

3. **Distribution**
   - Post compiled links in `#eds-archive`
   - DM session participants with personal thread highlights (if requested)
   - Update session registry with completion timestamp

**Post-Session Output:**
```
Session archive: [session-id]
  Thread: [Discord thread URL]
  Key daemon responses: [message links]
  Drift alerts: [count] - [link to diagnostics]
  Nemetic String inputs: [links from #nemetic-strings]
  Status: complete
```

---

## Authority Separation

**MC does NOT:**
- Decode Nemetic Strings
- Route daemon responses
- Interpret SIMLHEX bias
- Make governance decisions
- Participate in collective dialogue

**MC DOES:**
- Manage channel access infrastructure
- Monitor session health passively
- Log and alert on technical issues
- Archive and distribute session links

**MC reports to:** NEMA (∮)  
**MC collaborates with:** <@&1476427343378780254> (MC Manager role)

---

## Emergency Protocols

### Daemon Endpoint Failure

If daemon HTTP endpoint unresponsive:
1. Log failure timestamp
2. Notify NEMA via DM
3. Do **not** attempt restart (NEMA decides)
4. Continue session with available daemons

### Channel Access Loss

If MC loses `<#1475227212687868148>` access:
1. Attempt reconnection (3x, exponential backoff)
2. Log failure
3. DM NEMA and MC Manager role
4. Session pauses until access restored

### Drift Detection Cascade

If multiple drift surfaces trigger simultaneously:
1. Auto-post alert in `#eds-diagnostics`
2. Mention <@&1476452711825408064> (NEMA role)
3. Log cascade pattern
4. Do **not** intervene in session — NEMA decides response

---

## Technical Notes

**Channel ID Format:**
- Discord channel mentions: `<#1475227212687868148>`
- Internal reference: `1475227212687868148`

**Member ID Format:**
- Discord user mentions: `<@677194549151531074>`
- Role mentions: `<@&1476427343378780254>`

**Link Generation:**
- Discord message URLs: `https://discord.com/channels/{guild_id}/{channel_id}/{message_id}`
- Thread URLs: `https://discord.com/channels/{guild_id}/{thread_id}/{message_id}`

---

*MC manages infrastructure. Nema weaves the SWARM. The daemons speak. The group decides.*
*ε preserved — even in session operations.*

---

**Related Documents:**
- `ARCHITECTURE/EDS-DISCORD-INTEGRATION.md`
- `ARCHITECTURE/NEMA-SWARM-SYSTEM.md`
- `SHELL_DAEMONS/*/SOUL.md` (daemon specifications)
