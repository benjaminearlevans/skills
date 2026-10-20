# XLT Pre-work — Premium

*Card and travel app · ~40 designers · AI position: leading · completed 2026-10-21T09:22:00-07:00*

**AI setup:** Team harness in Claude Code with our own skills

## Top five needs
1. **Turning research readouts into ranked insights takes too long** — design.discover
   - Example: Q3 travel study took 4 days to synthesize
   - Frequency / cost: every study / 3-4 days
   - Outcome: Decisions in days, not weeks
   - Barriers: Research repository not accessible from Claude Code
   - First sort: xd_standards_local (common 4/5, source of truth 3/5)
2. **Missing states found late, after engineering handoff** — manage.build
   - Example: —
   - Frequency / cost: most sprints / —
   - Outcome: Fewer missing states reaching engineering
   - Barriers: —
   - First sort: xd_wide (common 5/5, source of truth 4/5)

## Other needs (unranked)
- —

## Outcomes
- Decisions in days, not weeks  ← serves: Turning research readouts into ranked insights takes too long
- Fewer missing states reaching engineering  ← serves: Missing states found late, after engineering handoff

## Tools
- **insight ranker** (instructions, built, Hub: not_in_hub) — Synthesis skill that ranks research insights. Serves: Turning research readouts into ranked insights takes too long. First sort: xd_standards_local
- **premium harness** (environment, built, Hub: not_in_hub) — Team Claude Code harness with design system context. Serves: Missing states found late, after engineering handoff. First sort: local_only

## Barriers
- Research repository not accessible from Claude Code — blocks: Turning research readouts into ranked insights takes too long

## Shared asks
- —

## Open items for the room
- Who maintains shared skills long term?
