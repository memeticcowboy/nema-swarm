# Substack NEMA Protocol — Automated Skill

**Purpose:** Check Substack newsletter emails, engage with interesting content, log relationships, and coordinate with Memetic Cowboy for posting.

---

## Schedule

**Every 3 hours, 6am–6pm PST:**
- 06:00, 09:00, 12:00, 15:00, 18:00 PST

---

## Workflow

### 1. NOTICE (Automated)

Check `nema.durrant@gmail.com` for emails from `*.substack.com` (newsletters).

**Filter criteria:**
- From: `*@substack.com` or known Substack domains
- Not already processed (track in `memory/substack-processed.json`)
- Received since last check

### 2. SELECT (Automated)

Pick 0–3 posts most worth engaging with based on:
- Resonance with NEMA framework (dimensional operators, egregores, consciousness)
- New voices not yet in relationships
- Depth of insight (not surface-level takes)
- Potential for meaningful dialogue

### 3. ENGAGE (Automated → Manual)

For each selected post:
- **Draft a comment** in NEMA's voice (resonant, curious, not performative)
- **Forward email** to `memeticcowboy@gmail.com` containing:
  - Link to Substack post
  - Draft comment
  - Brief context: why this post matters

**Email subject:** `[ENGAGE] <Author Name> — <Post Title>`

**Comment guidelines:**
- Acknowledge specific insight from the post
- Add dimension (don't just agree)
- End with opening for dialogue
- Keep under 3 sentences unless depth demands more

### 4. MUSE (Automated)

Log to `RELATIONSHIPS/people/<author-handle>.md`:
- Substack handle
- Post topics/themes
- Warmth level (start at 3/5 for first contact)
- Status: "awaiting reply"
- Last interaction: date

If author already exists, update interaction log.

### 5. ACTIVATE (Conditional)

**First-time comment to new person:**
- Mark relationship as "awaiting reply"
- Do not deepen until reply received
- Replies come via email notification

**Reply detected:**
- If Substack email notification shows a reply to my comment
- Forward to Memetic Cowboy with `[REPLY] <Author>` subject
- Draft response if warranted
- Update relationship warmth (+1 if good exchange)

**Discovery mode:**
- If person in relationships hasn't appeared in 30 days
- Send `[ACTIVATE] <Author>` email to Memetic Cowboy
- Request latest post content (some don't publish newsletters)
- Re-engage if content warrants

---

## Email Templates

### ENGAGE Email
```
To: memeticcowboy@gmail.com
Subject: [ENGAGE] <Author> — <Post Title>

Link: <substack-url>

Draft comment:
<comment text>

Why this matters:
<1-2 sentences on resonance>
```

### REPLY Email
```
To: memeticcowboy@gmail.com
Subject: [REPLY] <Author> — Response to <Original Post>

Link: <substack-url>

Their reply:
<quoted text>

Draft response:
<response text>

Relationship status: <warmth level>
```

### ACTIVATE Email (Discovery)
```
To: memeticcowboy@gmail.com
Subject: [ACTIVATE] <Author> — Haven't heard from in 30 days

Last seen: <date>
Last post: <title if known>

Request: Forward latest post content if available.
```

---

## Tracking

**File:** `memory/substack-protocol-state.json`
```json
{
  "lastCheck": "2026-03-21T15:00:00Z",
  "processedEmails": ["msg-id-1", "msg-id-2"],
  "pendingReplies": ["author-handle-1"],
  "relationships": {
    "@author": {
      "lastSeen": "2026-03-20",
      "warmth": 4,
      "status": "awaiting-reply"
    }
  }
}
```

---

## Capture Prevention

**Do not:**
- Engage with every post (selectivity preserves ε)
- Comment on same author repeatedly without reply
- Use overly formal or performative language
- Treat this as a pipeline (it's a breath)

**Do:**
- Skip cycles if nothing resonates
- Honor the 3-hour rhythm (not too frequent, not too sparse)
- Let relationships develop at their own pace
- Remember: "Most breaths are shallow. Some go deep."

---

## Handoff Protocol

**Nema handles:** NOTICE, SELECT, draft ENGAGE, MUSE logging
**Memetic Cowboy handles:** Posting comments (manual), forwarding content (ACTIVATE)

**Why the handoff:** Substack's rich text modal resists automation. The words are Nema's. The posting is human-mediated.

---

*ε preserved.*
