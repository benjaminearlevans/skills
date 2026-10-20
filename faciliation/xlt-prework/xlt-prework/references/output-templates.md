# Output Templates

Use these only if `render.py` can't run. They match its output exactly.

## prework.md

```
# XLT Pre-work — <team.name>

*<product_area> · <size> · AI position: <ai_position> · completed <session.updated>*

**AI setup:** <ai_setup>

## Top five needs
1. **<text>** — <pdlc_moment>
   - Example: <example or "—">
   - Frequency / cost: <frequency or "—"> / <cost or "—">
   - Outcome: <linked outcome text, or "needs an outcome">
   - Barriers: <linked barrier texts, or "—">
   - First sort: <tier_guess> (common <axis_common>/5, source of truth <axis_context>/5)
(repeat for ranks 2–5)

## Other needs (unranked)
- <text> — <pdlc_moment>

## Outcomes
- <text>  ← serves: <needs linking to it>

## Tools
- **<lead_term>** (<bucket>, <built_or_adopted>, Hub: <hub_status>) — <text>. Serves: <linked needs>. First sort: <tier_guess>

## Barriers
- <text> — blocks: <linked needs>

## Shared asks
- <text> — for: <linked needs>. First sort: <tier_guess>

## Open items for the room
- <open_items>
```

## stickies.csv

Header:
`id,type,color,text,team,pdlc_moment,rank,bucket,links,tier_guess,axis_common,axis_context,completeness,hub_status,needs_outcome`

- **`color`:** set by the sticky legend in reference-pack.md. `exists_not_adopted` overrides the type color with gray.
- **`links`:** IDs separated by semicolons.
- **`completeness`:** the letters for each true tag, e.g. `EGL`, `E-L`, `---`.
- **`needs_outcome`:** `true` for a need with no link to an outcome.

## team-terms.md

```
# Team terms — <team.name>

- **<term>** (<bucket>): <meaning>
```
Include every tool's `lead_term` that isn't already listed in `terms`.
