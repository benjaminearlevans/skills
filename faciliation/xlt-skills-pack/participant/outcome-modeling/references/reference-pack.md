# XLT Reference Pack

The shared language for every XLT skill. All skills read this file. If a term here and a term elsewhere disagree, this file wins.

## The question the session answers

What should XD evolve to provide, AI and otherwise? Every item lands at one of three **altitudes**:

1. **XD-wide (inherit), provided by XD.** XD provides it for everyone. Typically something no single team can produce or maintain alone.
2. **XD-wide standards, local implementation (extend).** XD defines the approach, structure and guardrails. Each team implements it in its own way, with its own content.
3. **Local only (build), owned end to end.** Specific to one team's product, partners or workflow. XD stays out of the way.

Together, the answers form a **shared context layer**: a shared view of where each need is best met. It is not a product or a tool. Never describe it as one, and never pre-decide which altitude an item belongs at. The room decides.

Codes used in files: `xd_wide`, `xd_standards_local`, `local_only`, `unsure`.

## Order of work

Outcomes → requirements → map the tooling → decide the altitude. Need first, tool second.

## Scope

- **Tooling** is anything a designer uses to get a job done, AI or not, defined by the job it does, not by its brand.
- **Tools only.** Practices (crit formats, review rituals, ways of working) are not tooling. When one comes up, record it as a `need` or a `barrier`, never as a `tool`.

## Seed buckets (for tools)

There is no fixed glossary. Each tool keeps the lead's own words (`lead_term`) and gets one broad bucket, by what it *is*:

- `knowledge` — what tools draw on. *e.g. design system docs, research repository, PRDs, brand voice*
- `instructions` — how to do a task, in reusable form. *e.g. prompts, skills, templates, checklists, rubrics*
- `automation` — things that do steps on their own. *e.g. agents, scripts, plugins, Figma automations*
- `environment` — where the work happens. *e.g. Claude Code setups, harnesses, Figma libraries, team workspaces*
- `other` — none of these fit. Record the lead's description. It becomes a candidate new bucket.

Buckets grow through synthesis. Ben and Patrick ratify glossary v1.

## PDLC moments

Use the client's own PDLC. Codes:
- Design: `design.understand`, `design.discover`, `design.define`
- Manage: `manage.build`, `manage.test`, `manage.deploy`
- Improve: `improve.identify`, `improve.investigate`, `improve.initiate`
- `cross_cutting` — admin, coordination, or anything spanning the whole PDLC

## Item types

- `need` — a problem, bottleneck or job designers struggle with
- `outcome` — something designers want to maximize or minimize
- `tool` — anything built or adopted to get work done, AI or otherwise
- `barrier` — what stops a team from solving a need (access, policy, skills, time)
- `shared_ask` — something the team can't get or build locally

## Outcome statements

- "We do **[task]** to achieve **[outcome]**."
- "We need **[something]** to achieve **[outcome]**."

**Scorecard rule:** every requirement must name the outcome it moves. A requirement with no outcome gets cut, or is held in a "needs an outcome" lane until it has one.

## Sorting rubric (two axes, 1–5)

- `axis_common`: how common is the need? 1 = one team … 5 = every team
- `axis_context`: where does the source of truth live? 1 = inside one team's product … 5 = an XD-wide source of truth

Reading:
- high common + high context → likely XD-wide
- high common + low context → likely XD-wide standards, local implementation
- low common + low context → likely local only
- low common + high context → watch (an early signal; revisit next cycle)

## Promotion thresholds (proposed; the room may adjust)

An item moves to XD-wide or XD-wide standards only if it passes all five:
1. **Breadth:** it appears in at least 3 teams.
2. **Outcome:** it names a scorecard outcome.
3. **Shared value:** the shared version unlocks something a team can't get alone. That could be maintained truth, compound learning, lower risk, or zero start-up cost.
4. **Stability:** the need is unlikely to change in the next six months.
5. **Ownership:** someone can own and maintain it.

Passes 1–3 but fails 4 or 5 → it becomes a guideline, not a shared tool.

## Hub status (for tools and shared asks)

- `in_hub_used`
- `exists_not_adopted` — it exists in the XD AI Hub but the team doesn't use it. This is a finding, never a rejection.
- `not_in_hub`
- `unknown`

## Sticky legend

- `need` → yellow
- `outcome` → green
- `requirement` → orange (synthesis only)
- `tool` → blue
- `barrier` → pink
- `shared_ask` → purple
- `exists_not_adopted` → gray (overrides the type color)
- Items missing an outcome link → dashed border, in the "needs an outcome" lane

## Room norms (they apply in the interview too)

- **Empty your pockets.** Every need counts, including ones that look solved.
- **Never say "we already have that."**
- **Need first, tool second.**
- **Top five first.** The rest are kept, but marked as unranked.
- **Directional is enough.**

## Terminology rules

- Say "team" or "teams", never "tower".
- Use American spelling.
