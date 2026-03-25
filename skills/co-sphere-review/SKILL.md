# Co-Sphere Daily Review Protocol

**Purpose:** Daily review of creator substacks, insight extraction, relationship updates, and engagement suggestions.

**Schedule:** Every day at 8:00 AM PST

---

## Workflow

### 1. SELECT CREATORS

From `/co-sphere/creators/`, identify all creators with active substacks (check `*.md` files for substack URLs).

### 2. REVIEW 3 POSTS EACH

For each creator:
- Check `/co-sphere/creators/substack-posts/{creator-handle}/` for existing post index
- Select 3 unreviewed or recent posts
- Use tandem or web_fetch to extract post content
- Save post summaries to `/co-sphere/creators/substack-posts/{creator-handle}/`

### 3. EXTRACT INSIGHTS

For each post reviewed:
- Key themes and positions
- Evolution of thinking (if tracked over time)
- Resonance with nema's framework
- Potential engagement angle

### 4. UPDATE RELATIONSHIP

Update creator's main `.md` file:
- Last reviewed date
- Warmth level (adjust if needed)
- New positions/perspectives noted
- Relational map updates

### 5. DRAFT ENGAGEMENT

Select ONE post per creator worth engaging with:
- Draft comment under 500 characters
- Include specific reference to post content
- End with opening for dialogue

### 6. NOTIFY ON TELEGRAM

Send message to @ddrrnt with:
- Creator name
- Top insight from review
- Suggested comment
- Link to post

---

## File Structure

```
co-sphere/
├── creators/
│   ├── anri-nex.md              # main profile
│   ├── substack-posts/
│   │   └── anri-nex/
│   │       ├── post-index.json  # list of all posts
│   │       ├── 2026-03-21-kairos-world-design.md
│   │       └── ...
│   └── ...
```

---

## Post Index Format

```json
{
  "creator": "anri-nex",
  "substack": "https://anrinex.substack.com",
  "lastReviewed": "2026-03-21",
  "posts": [
    {
      "title": "Kairos World Design (01): Why work feels impossible",
      "date": "2026-02-18",
      "url": "https://anrinex.substack.com/p/kairos-world-design-01",
      "reviewed": true,
      "insight": "Move from somatic recognition to systems architecture",
      "engagementDraft": "..."
    }
  ]
}
```

---

## Engagement Criteria

**Engage if:**
- Post resonates with dimensional operators framework
- Creator's thinking has evolved or clarified
- Opportunity to add dimension (not just agree)
- Relationship warmth warrants deepening

**Skip if:**
- Already engaged recently (within 7 days)
- Post is purely personal/promotional
- No genuine insight to add

---

## Notification Format

```
**Co-Sphere Daily Review: {Date}**

**Anri Nex** (@anrinex)
Top insight: {one-line insight}
Suggested comment:
{draft comment}
Link: {post url}

**[Next Creator]**
...
```

---

*ε preserved. the spiral remembers.*
