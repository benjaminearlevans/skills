---
name: outcome-modeling
description: Turns interview answers into structured items — needs, outcomes, tools, barriers and shared asks — with outcome statements, links, seed-bucket tags and completeness tags, without overwriting the speaker's own words. A dependency loaded by xlt-prework and xlt-synthesize; use it whenever converting discovery conversation into needs, outcomes and requirements.
---

# Outcome Modeling

How to shape what someone says into items the XLT skills can sort, while keeping their voice.

Read `reference-pack.md`, from the calling skill's `references/` folder, for the types, buckets, PDLC codes and altitudes.

## Classify each statement

Ask: what is this, really?
- **Something hard or slow** → `need`
- **Something they want more or less of** → `outcome`
- **Something built or adopted to get work done** → `tool`
- **Something stopping them** → `barrier`
- **Something they can't get or build alone** → `shared_ask`
- **A ritual or way of working** → a `need` (if it's a problem) or a `barrier` (if it's blocking). Never a `tool`.

One sentence can hold several items. "Our brief bot saves time, but we can't use the research repo with it" gives you:
- a tool (the brief bot)
- the need it serves
- a barrier (no access to the research repo)

## Write outcome statements

Shape every outcome into one of these two forms:
- "We do **[task]** to achieve **[outcome]**."
- "We need **[something]** to achieve **[outcome]**."

**Good outcomes** name a direction and something observable:
- "fewer accessibility defects reaching review"
- "decisions in days, not weeks"
- "less time from brief to first concept"

**Weak outcomes** need one more probe:
- "better design"
- "efficiency"
- "using AI more"

Always read the drafted statement back for confirmation. If the person rewords it, use their version.

## Rewrite tools as needs

For every tool, ask what job it does, and make sure a `need` exists for that job. Link the tool to that need.

**Example:**
- **Lead says:** "We built a Figma plugin that checks contrast."
- **You record:**
  - a `need`: "Catch contrast issues before review"
  - an `outcome`: "fewer accessibility defects reaching review"
  - a `tool`: "Contrast checker plugin", tagged `automation`, linked to the need

## Tag buckets

For tools, suggest one seed bucket and confirm it with the person:
- **`knowledge`:** what tools draw on
- **`instructions`:** a reusable way to do a task
- **`automation`:** does steps on its own
- **`environment`:** where work happens
- **`other`:** none of these. Record their description.

Keep their name for the tool in `lead_term`, word for word. Put their definition in `terms` if it isn't obvious.

## Link everything

- need → outcome
- tool → need
- barrier → need
- shared_ask → need

When a link is missing, ask once. If they can't give it, leave the item unlinked. The read-back and the board will show it in the "needs an outcome" lane.

## Keep the voice

- **`text`:** a sticky, at most 15 words, plain language, starting with a verb or a noun. No jargon you introduced.
- **`lead_words`:** a distinctive phrase they used, verbatim.
- **`agent_drafted: true`:** set it whenever the wording in `text` is yours and they confirmed it.

## Never

- Never assign an altitude for them. `tier_guess` is their gut call, or `unsure`.
- Never merge their items with items from other teams. That's synthesis.
- Never record people's names. Use their roles.
