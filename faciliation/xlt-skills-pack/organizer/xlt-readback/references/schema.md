# prework.json schema (v1.0)

`prework.json` is the single source of truth for one lead's submission. The interview updates it as it goes, and `render.py` generates every other file from it. Never edit the generated files by hand.

```json
{
  "schema_version": "1.0",
  "team": {
    "id": "premium",                 // lowercase slug, from config.md team list if present
    "name": "Premium",
    "product_area": "Card and travel app",
    "size": "~40 designers",
    "ai_setup": "One sentence, lead's words",
    "ai_position": "early | building | established | leading | unsure"
  },
  "items": [
    {
      "id": "premium-007",           // <team.id>-NNN, never reused
      "type": "need | outcome | tool | barrier | shared_ask",
      "text": "Sticky text, max 15 words, plain",
      "detail": "Fuller description in plain language",
      "lead_words": "Verbatim phrase the lead used, if distinctive",
      "pdlc_moment": "design.define",          // codes from reference-pack.md
      "rank": 1,                               // 1-5 for top five, null if unranked
      "links": ["premium-003"],                // need->outcome, tool->need, barrier->need, shared_ask->need
      "example": "A concrete instance, or null",
      "frequency": "every sprint, or null",
      "cost": "half a day per brief, or null",
      "completeness": { "example": true, "grounded": false, "linked": true },
      "bucket": "instructions",                // tools only; null otherwise
      "lead_term": "our brief bot",            // tools only; the lead's name for it
      "built_or_adopted": "built | adopted | null",
      "hub_status": "in_hub_used | exists_not_adopted | not_in_hub | unknown",
      "tier_guess": "xd_wide | xd_standards_local | local_only | unsure",
      "axis_common": 4,                        // 1-5 or null
      "axis_context": 2,                       // 1-5 or null
      "source": "interview | scan",
      "agent_drafted": false                   // true if the agent wrote the wording and the lead confirmed it
    }
  ],
  "terms": [
    { "term": "brief bot", "meaning": "Lead's explanation", "bucket": "instructions" }
  ],
  "open_items": ["Things the lead wants raised in the room"],
  "session": {
    "started": "2026-10-21T09:00:00-07:00",
    "updated": "2026-10-21T09:18:00-07:00",
    "phase": "0-welcome | 1-snapshot | 2-problems | 3-outcomes | 4-inventory | 5-shared | 6-sort | 7-readback | done",
    "scan_consent": false,
    "confirmed": false
  }
}
```

## Rules

- **Write as you go.** Add each item the moment the lead names it. Update its fields as probing fills them in. Update `session.phase` and `session.updated` at each phase change.
- **`completeness` is derived:**
  - `example` is true when `example` is non-null.
  - `grounded` is true when `frequency` or `cost` is non-null.
  - `linked` is true when `links` is non-empty. Outcomes count as linked when any need links to them.
- **Redaction:** no person's name appears anywhere. Use roles instead ("a senior designer", "our PM"). Product and tool names are kept.
- **IDs are stable.** If an item is dropped, delete it. Never renumber.
