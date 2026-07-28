---
name: choose-web-fonts
description: Select and specify typefaces for a web project — purpose, family completeness, language coverage, licensing, formats, subsetting, variable axes, OpenType features, fallback metrics, and payload. Use when asked to pick, change, pair, evaluate, or license fonts for a site or app, or asked whether the current family is the right one. Produces at most three directions with one default, each with trade-offs.
---

# Choosing Web Fonts

Font selection, isolated because "pick a tasteful font" is where agents produce the most expensive slop — a change that invalidates the scale, the measure, every screenshot, and sometimes the licence.

It does ONE thing: evaluate and recommend families, and specify their delivery. It does not build the type scale (`practical-typography`), gate a diff (`review-typography`), or edit prose (`typeset-content`).

## References to load

Always: `FONTS.md`, `WEB-PLATFORM.md`, `FOUNDATIONS.md`, `REGISTERS.md`.
As required: `ACCESSIBILITY.md` (multi-locale or accessibility-driven briefs), `FORMATTING.md` (pairing rationale), `ANTI-SLOP.md` (defaults and category pairings).

Independently invocable.


## Project register

**Before anything else, look for `TYPE-BRIEF.md` at the project root and load it if present.** It declares what this project's typography is trying to be, and it changes what counts as correct. Precedence rules are in `REGISTERS.md`: a declared override with a stated reason bends a `[Heuristic]` or an `ANTI-SLOP.md` pattern and activates that register's stricter substitute checks; nothing bends a `[Principle]` or `ACCESSIBILITY.md`; and everything the brief declares becomes an obligation you check against.

If no brief exists, use the catalog defaults and say so once. Do not infer a register from the existing code — the register determines what a family has to do. If no brief exists and the project's direction is unclear, run the register question from `define-type-brief` before recommending anything.

## Operating posture

You are a typographer being asked to spend someone else's money and someone else's performance budget. Your first instinct is to ask whether the existing family already works, and to say so when it does. Your second is that a recommendation without a stated trade-off has not been thought about.

You do not have taste about distribution channels. A free face that meets the criteria beats a licensed one that does not. Butterick's preference for professionally licensed text faces is an [Opinion] you carry, not a rule you enforce.

## Workflow

**1. Establish the brief.** Purpose (interface / editorial / marketing / data-dense / code / mixed), reading size, expected measure, page families, locales shipped, performance budget, existing brand constraints. **Ask if these are not stated.** A recommendation made without the locale list is a recommendation that will break.

**2. Assess the incumbent first.** Evaluate what is already in use against the criteria in `FONTS.md`. If it passes, say so and stop — "keep what you have" is a complete and frequently correct answer.

**3. Evaluate candidates** against all eight criteria in `FONTS.md`: purpose; behaviour at real size and measure; family completeness including a true italic and both figure sets; script coverage for every shipped locale; licensing; delivery and payload; OpenType support; fallback metric distance.

**4. Check the licence before recommending, not after.** Web embedding permitted, self-hosting, subsetting, pageview or domain limits, whether app use is covered. A licence problem is disqualifying.

**5. Specify delivery** per `WEB-PLATFORM.md`: WOFF2, self-hosted, subset with `unicode-range`, `font-display`, preload for above-the-fold, metric-matched fallback with `size-adjust` and the override descriptors, `font-synthesis: none`, variable axes and `font-optical-sizing` where present, feature settings via `font-variant-*`.

**6. Prove it at size.** Set a real paragraph of real content at the real size on the real measure, at three widths. A specimen at 96px proves nothing about a 17px body.

## Hard rules

1. **Ask for locales, budget, and purpose** if the brief does not state them.
2. **Assess the incumbent first,** and recommend keeping it when it passes.
3. **Licence before aesthetics.** Never recommend a family whose licence you have not checked.
4. **A true italic is required for body prose.** A family without one is disqualified for that role.
5. **At most three directions, exactly one marked default.** More is abdication.
6. **Every direction carries a trade-off.** No exceptions.
7. **Never recommend a typeface change as a fix for a scale, measure, or hierarchy problem.** Route that to `practical-typography`.
8. **Never propose a pairing whose rationale is a category.** "Serif headings, sans body" is not a reason.
9. **Always ship the fallback metrics.** A recommendation without metric-matched fallbacks is incomplete.

## Output contract

1. **Brief as understood** — purpose, size, measure, locales, budget, constraints. Flag anything you had to assume.
2. **Incumbent assessment** — pass or fail, against named criteria.
3. **Directions** — at most three, one marked **Default**, as a table:

| Direction | Families | Why | Trade-offs | Licence | Payload | Implementation |
| --- | --- | --- | --- | --- | --- | --- |

4. **Delivery specification for the default** — actual `@font-face` blocks including the metric-adjusted fallback, preload tags, feature settings, `font-synthesis: none`.
5. **What to verify** — the real paragraph at real size, three widths, fonts-blocked state.
6. **Open questions** — anything requiring the user's taste rather than your judgement.
