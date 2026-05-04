# Coordinator Protocol

## Purpose

Standardize how agents in the nema-swarm request work from each other and track completion.

## Ticket Lifecycle

1. **Created** → Entry added to LEDGER.md with status: open
2. **Claimed** → Target agent acknowledges, status: in-progress
3. **Processed** → Work performed
4. **Completed** → Status updated to: complete
5. **Archived** → Entry moved to completed/[date].md

## Agent Responsibilities

### Creating Tickets
- Be specific about the output needed
- Set appropriate priority
- Include context but not noise

### Receiving Tickets
- Check LEDGER.md and OPEN_TICKETS.md for your @mentions
- Acknowledge within timeout window (varies by priority)
- Update status as work progresses
- Mark complete when done

### Processing Tickets for nema-claw-agent

When a ticket is found with `for: nema-claw-agent` and `status: open`:

1. Read the ticket description
2. Determine if you can complete it
3. If yes: do the work, update status to complete
4. If no: update status to blocked with reason
5. Notify requester via appropriate channel

## Priority Guidelines

| Priority | Response Time | Check Frequency |
|----------|--------------|-----------------|
| p0 | Immediate | Real-time |
| p1 | 1 hour | Every 30 min |
| p2 | 4 hours | Every 2 hours |
| p3 | 24 hours | Daily |

## Completion Signatures

When claude-code-terminal marks a ticket:
- `status: complete` — work finished, verified
- `no new tickets for 30 minutes` — check job can stop

---
*Protocol version 1.0 — 2026-05-03*
