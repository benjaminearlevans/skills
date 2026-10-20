# board-manifest.json schema

The hand-off from `xlt-synthesize` to `xlt-board`. It's layout-agnostic: it records order and grouping, and the board builder computes positions.

```json
{
  "title": "XLT — Local vs Shared Tooling",
  "generated": "2026-10-24T10:00:00-07:00",
  "legend": { "need": "yellow", "outcome": "green", "requirement": "orange", "tool": "blue",
              "barrier": "pink", "shared_ask": "purple", "exists_not_adopted": "gray" },
  "sections": [
    {
      "id": "c01",
      "kind": "cluster",                 // cluster | needs_outcome | parking_lot | grid | legend
      "title": "Turning research into decisions",
      "subtitle": "design.discover · 5 teams",
      "rows": [
        { "row": "outcomes",     "stickies": ["o-01"] },
        { "row": "requirements", "stickies": ["r-01", "r-02"] },
        { "row": "needs",        "stickies": ["premium-002", "servicing-004"] },
        { "row": "tools",        "stickies": ["premium-011"] },
        { "row": "barriers",     "stickies": ["servicing-009"] }
      ]
    },
    { "id": "lane", "kind": "needs_outcome", "title": "Needs an outcome", "rows": [ { "row": "needs", "stickies": [] } ] },
    { "id": "grid", "kind": "grid", "title": "Sorting grid",
      "axes": { "x": "How common is the need?  One team → Every team",
                "y": "Where does the source of truth live?  One team's product → XD-wide" },
      "quadrants": ["XD-wide", "XD standards, local implementation", "Local only", "Watch"] }
  ],
  "stickies": {
    "premium-002": { "type": "need", "color": "yellow", "text": "…", "team": "premium",
                     "tag": "Premium · R1", "dashed": false, "contested": false }
  }
}
```

**Rules**
- **IDs:** every sticky ID in `rows` exists in `stickies`. Submission items keep their original IDs. Synthesized outcomes use `o-NN`, and requirements use `r-NN`.
- **`tag`:** `<Team> · R<rank>`, or `<Team>` if unranked. Requirements use `<altitude> · moves o-NN`.
- **`contested: true`:** the board marks these with a ⚑ prefix in the text.
- **The grid section** starts empty. The room fills it during the pressure test.
