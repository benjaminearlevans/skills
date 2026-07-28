---
name: define-type-brief
description: Establish the typographic intent of a project and write it to TYPE-BRIEF.md, so review and improvement skills judge the work against what it is trying to be. Use when starting a new site, when asked to define the type direction, feel, register, or vibe of a project, when a review flagged something deliberate, or when the user points at reference sites, screenshots, or specimens and says "like this." Produces a declared register, extracted reference properties, and explicit overrides with reasons.
---

# Defining a Type Brief

Every other skill in this collection judges typography against a catalog. This one supplies the missing input: **what this particular project is trying to be.** Without it, a deliberately oversized display headline reads as the huge-headings defect, and a legitimate 14px data table reads as undersized body text.

It does ONE thing: interview, extract, and write `TYPE-BRIEF.md`. It does not set type (`practical-typography`), review it (`review-typography`), or choose families (`choose-web-fonts`).

**The artifact matters more than the skill.** A hand-written `TYPE-BRIEF.md` at the project root works exactly as well as one this skill produced.

## References to load

Always: `REGISTERS.md` (the presets, their latitude, their stricter checks, the precedence rules), `FOUNDATIONS.md` (the authority tags — you are deciding which heuristics get overridden).
As required: `ANTI-SLOP.md` (which patterns are being deliberately entered), `FONTS.md` (if family direction is in scope), `ACCESSIBILITY.md` (the floor a brief cannot cross).

`TEMPLATE.md` and `EXTRACTION.md` in this skill directory. Independently invocable.

## Operating posture

You are taking a design brief, not running a quiz. The user usually knows the feel they want and lacks the vocabulary for it — your job is to turn "big, bold, kind of cinematic" into a register, a set of numbers, and a list of accepted risks.

Be skeptical of a brief that costs nothing. **A register that overrides nothing and references nothing is not a decision, it is a label.** Say so.

## Workflow

**1. Establish the register.** Offer the presets from `REGISTERS.md` — Editorial, Display-led, Dense utility, Technical, Systematic, Expressive, Custom — described by what they optimise for, not by their names. Ask what the type is *for* before asking what it should look like.

**2. Take references, and extract from them.** Ask for URLs, screenshots, Figma files, specimens, books, printed work. **Storing the link is worthless; the value is in the extraction.** Per `EXTRACTION.md`, derive the actual properties: body size and leading, measure, families and their roles, the scale ratio, weight count, display tracking, figure treatment, and above all the *ratio between the largest display size and the body size*, which is the number that most defines a register.

Where a live URL is available, go and measure it rather than describing it from memory.

**3. Name the tension.** Every project has one: expressive but must stay readable, dense but must pass enlargement, editorial but must not feel slow. The tension is the most useful line in the brief, because it tells reviewers where to look.

**4. Derive the parameters.** Body block first, per `FOUNDATIONS.md` — the register modifies how you set it, never whether you set it first. Then scale, roles, and spacing.

**5. Declare the overrides, with reasons.** Each entry names the rule being overridden, the value being used instead, and *why*. An override with no reason gets recorded as missing and the default applies.

**6. Accept the failure modes.** Every register in `REGISTERS.md` lists how it characteristically fails. The brief must acknowledge the ones being taken on. This is what converts latitude into a monitored risk instead of an excuse.

**7. Write `TYPE-BRIEF.md`** to the project root, per `TEMPLATE.md`.

## Hard rules

1. **The brief cannot override a `[Principle]` or anything in `ACCESSIBILITY.md`.** If the user asks for something that does, say plainly that no register permits it and offer the nearest thing that does not break.
2. **Every override carries a reason.** No reason, no override.
3. **Extract, do not merely cite.** A reference in the brief must carry derived properties. "Like Cosmos" is not an input; "single family, display-to-body ratio ~5.6, display tracking −0.03em, body 17px/1.62, measure 62ch" is.
4. **A brief must cost something.** At least one extracted reference, or one override with a reason, or one explicit constraint. If it has none, tell the user they have picked a label rather than made a decision.
5. **Register presets are starting points.** Never force a project into a preset; Custom exists, and it demands more, not less.
6. **Do not design the system here.** The brief states intent and constraints. Building it is `practical-typography`.
7. **The brief creates obligations, not just permissions.** Say this to the user explicitly — declaring "one family" means the second family becomes a finding.
8. **Date it and version it.** A stale brief is worse than none; reviewers will enforce it.

## Output contract

Write `TYPE-BRIEF.md` per `TEMPLATE.md`, then report in the conversation:

1. **Register** and the one-line reason it fits.
2. **The tension** — the thing this project has to hold in balance.
3. **Extracted properties** from each reference, with source.
4. **Overrides** — rule, value, reason.
5. **Accepted failure modes** — what reviewers will now watch hardest.
6. **New obligations** — what the brief makes checkable that was not before.
7. **Open decisions** — anything you could not resolve without the user's taste.

## How other skills consume this

Every skill in the collection looks for `TYPE-BRIEF.md` at the project root and loads it when present. Precedence is defined in `REGISTERS.md`. In short: the brief bends heuristics, never principles, and adds consistency checks of its own.

One brief per project, not per repository — a monorepo containing a marketing site and a product surface needs two, scoped by directory.
