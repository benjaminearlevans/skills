---
name: xlt-readback
description: After the XLT local vs shared tooling session, reads the worked FigJam board (and any redline notes) and produces the session deliverables — requirements map by altitude, outcome scorecard, retire/transform/adopt shortlist, XD-standards frameworks needed, local-only bounty list, ratified glossary v1 and top-down reconciliation. Use when the user types /xlt-readback or asks to write up the XLT session results.
---

# XLT Readback

Turn the worked board into the deliverables, and seed the next cycle.

## Inputs
- **The FigJam board URL.** Read it with `get_figjam`, after loading `figma-use-figjam`.
- **The pre-session `board-manifest.json`, `v0-map.md` and `glossary-proposal.md`**, so you can see what changed.
- **Optional:** live-capture notes, photos of paper redlines, and the top-down list.

## Steps
1. **Diff the board against the manifest:**
   - stickies moved between clusters
   - new stickies (written in the room, so no submission ID)
   - removed or struck-through stickies
   - anything placed on the sorting grid, with its quadrant
2. **Settle each requirement's altitude.** Take the quadrant it was placed in. If it wasn't placed, keep the draft altitude and mark it `not discussed`.
3. **Apply the promotion thresholds** to every XD-wide and XD-standards item, recording which tests it passes. If it passes 1–3 but fails 4 or 5, turn it into a guideline.
4. **Write the deliverables** to `xlt-deliverables.md`, in this order:
   1. **Directional requirements**, by altitude, each with the outcome it moves.
   2. **Outcome scorecard**, with the outcomes the room ranked highest at the top.
   3. **Retire / transform / adopt shortlist**, measured against the requirements.
   4. **XD-standards frameworks and guidelines** local builders need.
   5. **Local-only bounty list.**
   6. **Glossary v1**: the ratified proposal plus any changes the room made.
   7. **Top-down reconciliation**: tag each item `both`, `bottom_up_only` or `top_down_only`, or say it's still pending.
   8. **Open questions and owners**, as named in the room. Leave the owner blank if no one was named. Never invent one.
5. **Seed the next cycle:** write `next-cycle-seed.md` listing the watch-quadrant items, the needs-an-outcome items, and the contested items not resolved in the room.

## Rules
- **Every line traces** to a sticky or a note. Mark items written in the room as `[room]`.
- **Directional, not a spec.** Don't add detail the room didn't give.
- **Use "teams", never "towers".** Use American spelling.
