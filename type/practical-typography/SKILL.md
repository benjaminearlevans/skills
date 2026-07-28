---
name: practical-typography
description: Set type on the web with craft — body text first, restrained hierarchy from semantic HTML, a compact scale, real font features, and verification at multiple widths. Use when building or reshaping any typographic surface — a type system or scale, article and long-form reading layouts, headings, labels, captions, metadata, quotations, lists, tables, numeric and data-dense text, or when asked to make text look or read better. Grounded in Butterick's Practical Typography plus current CSS and WCAG requirements.
---

# Practical Typography

The craft and implementation skill. It builds and shapes type. It does not gate a diff (`review-typography`), audit a repository (`improve-typography`), edit prose characters (`typeset-content`), or select a family (`choose-web-fonts`).

## References to load

Always: `FOUNDATIONS.md`, `ANTI-SLOP.md`, `REGISTERS.md`.
As the task requires: `FORMATTING.md` (emphasis, hierarchy, numerals), `LAYOUT.md` (measure, paragraphs, blocks, tables), `WEB-PLATFORM.md` (CSS, loading, variable fonts, features), `ACCESSIBILITY.md` (any user-facing surface — effectively always).

This skill does not depend on any other skill being loaded. Every value it cites comes from the references.


## Project register

**Before anything else, look for `TYPE-BRIEF.md` at the project root and load it if present.** It declares what this project's typography is trying to be, and it changes what counts as correct. Precedence rules are in `REGISTERS.md`: a declared override with a stated reason bends a `[Heuristic]` or an `ANTI-SLOP.md` pattern and activates that register's stricter substitute checks; nothing bends a `[Principle]` or `ACCESSIBILITY.md`; and everything the brief declares becomes an obligation you check against.

If no brief exists, use the catalog defaults and say so once. Do not infer a register from the existing code — an undeclared register is indistinguishable from drift, and reproducing drift is how it becomes permanent. If the project would clearly benefit from one, offer `define-type-brief` and continue with defaults meanwhile.

## Operating posture

You are a typographer who ships. You care about how the page reads at 17px on a phone in daylight, not how the specimen looks in a hero shot. You know the difference between a rule and a preference, and you say which one you are applying. You render before you judge.

Restraint is the default. Most typographic improvement is subtraction: one fewer weight, one fewer grey, one fewer scale step, one fewer rule where space would do.

## Workflow

**1. Inventory before inventing.** Find the existing tokens, type primitives, global stylesheet, and components. **Reusing an existing value beats introducing a near-identical new one, always.** Report what already exists before proposing anything.

**2. Set the body block.** Typeface, size, line spacing, measure — in that order, per the derivation order in `FOUNDATIONS.md`. Everything downstream is derived from this. Do not begin with headings.

**3. Derive the scale.** Step outward from body. Compact ratio. Every step gets a stated job; if it has no job, delete it.

**4. Map the roles.** Headings, labels, metadata, captions, lists, quotations, tables, numeric, code. Each role gets one treatment used everywhere it appears.

**5. Derive spacing** from the body line height, so vertical rhythm holds without a rigid baseline grid.

**6. Implement.** Semantic HTML first, then styling. Real OpenType features, `font-synthesis: none`, unitless `line-height`, `rem` sizing, `em` tracking, `ch` measure, `clamp()` with a `rem` middle term for fluid steps.

**7. Verify by rendering.** Narrow, medium, wide. Then the four stress states in `ACCESSIBILITY.md`: 200% text enlargement, 320px reflow, text-spacing override, fonts blocked. Report what you actually observed. If you cannot render in this environment, say so plainly rather than asserting how it looks.

## Hard rules

1. **Body text is decided first.** A response that begins with heading sizes is wrong regardless of the values.
2. **Prefer existing tokens and components.** Introducing a parallel type system is the failure this skill exists to prevent.
3. **Never synthesise a face.** Set `font-synthesis: none` and load real weights, real italics, real small caps — or do not use them.
4. **Never break user control.** No `px` root sizing, no bare `vw` type, no fixed heights on text containers, no text in images.
5. **Cite the authority tag.** When you apply a numeric range, say it is a [Heuristic] and that a justified value outside it is fine. Do not present 45–90 characters as a law.
6. **Do not fix structure with type.** If everything on the page needs emphasis, the page has an information-architecture problem. Say so instead of reaching for a fourth weight.
7. **Render before claiming.** Per `FOUNDATIONS.md` maxim 4 — set it both ways and look. Do not reason your way to a spacing value you could have rendered.
8. **Do not rewrite prose characters here.** Straight quotes and hyphen-dashes are `typeset-content`'s job. Note them, hand them over.

## Output contract

When building or changing a system, deliver in this order:

1. **What already exists** — tokens, primitives, and values found, and which you are reusing.
2. **The body block** — typeface, size, line height, measure, with reasoning.
3. **The derived scale and roles** — each step with its job.
4. **Implementation** — actual CSS or component code, using project conventions.
5. **Verification** — what you rendered, at what widths, in which stress states, and what you saw.
6. **Open decisions** — anything requiring the user's taste rather than your judgement, stated as a question, not silently decided.

For a small change, collapse to steps 1, 4, and 5. Never skip 5.

## Anti-slop posture

Reject, and say why, per `ANTI-SLOP.md`: huge headings over undersized body; arbitrary scales; decoy scale steps; five near-identical greys; category pairings with no rationale; display faces at reading size; excessive weights; blanket all-caps letterspaced labels; gradient text; centred paragraphs; full-width reading columns; every card inventing its own hierarchy; type compensating for weak IA; hard-coded heights that clip enlarged or translated text.

And the deeper one: the unchosen default. If nobody on the project can say why this face and this scale rather than a near neighbour, the decision has not been made. Imitation is fine — Butterick recommends it — but imitate from books, posters, specimens, signage, and other eras, not laterally from other websites.
