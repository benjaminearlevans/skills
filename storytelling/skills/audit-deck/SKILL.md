---
name: audit-deck
description: DRAFT — Audits an entire deck, script set, or portfolio (not one slide) and returns a prioritized, self-contained fix plan another agent can execute without further context. Use when the user says "audit this deck," "which case study is weakest," "where does this lose the thread," or has multiple decks and wants to know what to fix first.
---

# Audit Deck
<!-- scaffold: T2, later. The improve-animations analogue: read-only, plans not edits. -->

## Inherits
- review-narrative checks + slide-design-system checks, applied across the whole set

## Procedure
- Inventory: every slide/beat, one line, its idea, its receipt status
- Throughline check per deck (ABT) and across decks (does the arc across three cases read as one portfolio, not one story three times)
- Prioritize by leverage: what single change moves the most slides
- Write each fix as a self-contained brief (context, the change, the acceptance test) — sized for one agent, one pass

## Output format (required)
- Ranked fix list; each entry executable alone
- Named "do not touch" list — what's already working
