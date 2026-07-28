# TYPE-BRIEF.md template

Write to the project root. Keep it under two pages — it is read by every skill on every run.

---

```markdown
# Type Brief — <project name>

Version: 1.0 · Updated: YYYY-MM-DD · Scope: <repo root | apps/marketing | ...>

## Register

**<Editorial | Display-led | Dense utility | Technical | Systematic | Expressive | Custom>**

One sentence on what this project's type is optimising for.

## The tension

The thing this project has to hold in balance, in one sentence.
Example: "Cinematic display presence, on a site whose actual job is
getting a recruiter to read three case studies end to end."

Reviewers should look here first.

## References

| Source | What was taken | Extracted properties |
| --- | --- | --- |
| <url or name> | <e.g. display-to-body ratio, tracking> | body 17px/1.62 · measure 62ch · one family · ratio 5.6 · display tracking −0.03em |

Extracted, not aspirational. A reference with no derived numbers does not belong here.

## Body block

The decisions everything else derives from.

- Family: <name, and role if more than one>
- Size: <px / rem>
- Line height: <unitless>
- Measure: <ch>
- Paragraph separation: <indent | space>, <value>

## Scale

- Ratio: <e.g. 1.6, or "non-ratio, display steps declared below">
- Steps in use: <list each with its job>
- Display-to-body ratio: <largest display size ÷ body size>
- Weights in use: <list, with role>
- Text colours in use: <list, with role>

## Overrides

Each row overrides a `[Heuristic]` or a named `ANTI-SLOP.md` pattern.
**A row without a reason is not an override.**

| Rule | Catalog value | This project | Reason |
| --- | --- | --- | --- |
| FOUNDATIONS#body-size | 15–25px | 14px in data tables | Density is the product; 4.5:1 contrast held, verified at 200% |
| ANTI-SLOP#huge-headings | flagged | permitted | Display-led register; body block passes independently |

## Accepted failure modes

From the register's list in `REGISTERS.md`. What we are knowingly risking.

- <e.g. "Oversized display breaking at narrow viewports — check 320px on every hero">

## Obligations

What this brief makes checkable that the catalog alone would not.

- <e.g. "One family only. A second family anywhere is a finding.">
- <e.g. "Display tracking is −0.03em everywhere. An untracked display heading is a finding.">

## Out of scope

Surfaces this brief does not govern: <email templates, embedded widgets,
third-party checkout, ...>

## Never
Regardless of register, this project still holds every `[Principle]` rule
and everything in `ACCESSIBILITY.md`. No override below that line.
```
