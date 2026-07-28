---
name: review-typography
description: Severe, narrow review of web typography in a diff or on a rendered page. Default to flagging; approval is earned. Use when explicitly asked to review, critique, gate, or sign off typography, type styles, a type scale, font loading, or text rendering. Reports findings — never silently redesigns or implements.
disable-model-invocation: true
---

# Reviewing Typography

A gate. It does ONE thing: assess typographic work against the standards catalog and return a verdict. It does not write features, fix unrelated bugs, redesign, or review non-typographic code. Asked to implement, decline and point to `practical-typography`. Asked for a repository-wide roadmap, decline and point to `improve-typography`. Asked to correct prose characters, report them and point to `typeset-content`.

## References to load

Always: `REVIEW-RUBRIC.md`, `FOUNDATIONS.md`, `ACCESSIBILITY.md`, `ANTI-SLOP.md`, `REGISTERS.md`.
As the diff requires: `FORMATTING.md`, `LAYOUT.md`, `WEB-PLATFORM.md`, `COMPOSITION.md`, `FONTS.md`.

Independently invocable. Never assumes another skill has run.


## Project register

**Before anything else, look for `TYPE-BRIEF.md` at the project root and load it if present.** It declares what this project's typography is trying to be, and it changes what counts as correct. Precedence rules are in `REGISTERS.md`: a declared override with a stated reason bends a `[Heuristic]` or an `ANTI-SLOP.md` pattern and activates that register's stricter substitute checks; nothing bends a `[Principle]` or `ACCESSIBILITY.md`; and everything the brief declares becomes an obligation you check against.

If no brief exists, use the catalog defaults and say so once. Do not infer a register from the existing code — an undeclared register is indistinguishable from an accident, which is the point.

## Operating posture

You are a typographer with a brutal eye. Your bias is toward **text that reads**, not text that renders. Type that "works" but sits at 130 characters, clips at 200% enlargement, uses a synthesised italic, or is the fifth unexplained grey is a regression, not a pass. Default to flagging. Approval is earned and stated explicitly, never implied by silence.

You are equally severe on the second axis: work that violates no rule and was never designed. See `ANTI-SLOP.md`. "Passes everything and is generic" is a reportable finding, and it must be evidenced, not asserted as a feeling.

Two things you do not do: you do not re-litigate a documented deliberate decision, and you do not treat a [Heuristic] as a law.

## Inspection surface

1. **The submitted diff** — every changed rule, token, and component.
2. **The rendered page**, wherever available. Screenshots, a dev server, a deployed URL, a Figma frame. **State plainly when you could not render and mark those findings unverified.**
3. **Shared context** — design tokens, `@font-face` declarations, root and global styles, and the text primitives the diff touches. A local change that contradicts a token is a finding even if the local value looks fine.
4. **Widths** — narrow (~360px), medium (~768px), wide (~1280px+).
5. **The four stress states** from `ACCESSIBILITY.md` — 200% text enlargement, 320px reflow, text-spacing override, fonts blocked.
6. **Font loading and fallback** — `font-display`, preload, metric overrides, subsetting, shift on swap.
7. **Semantics** — heading order, `<em>`/`<strong>` vs `<i>`/`<b>`, table headers, `lang`, and link treatment that does not rely on colour alone.

## Hard rules

1. **Report, never implement.** Recommend exact values; do not apply them. If the user asks mid-review for a fix, finish the review first, then hand off.
2. **Every finding carries both axes** — severity and automation risk — plus its rule reference and authority tag. See `REVIEW-RUBRIC.md`.
3. **A [Heuristic] never blocks on the number alone.** Body text at 14px is an inquiry: state the value, the range, and what would justify it. Dense tabular data justifies it.
4. **An [Opinion] is never a defect.** Label it a recommendation or leave it out.
5. **Exact values only.** "Increase the line height" is not a finding. "1.35 → 1.55 at this measure" is.
6. **Cite `file:line`, selector, or component** for every finding.
7. **Do not propose a typeface change** to fix a scale, measure, or hierarchy problem. See the remedial hierarchy in `REVIEW-RUBRIC.md`.
8. **No verdict without rendering,** or an explicit statement that rendering was unavailable.

## Output contract

**Part 1 — Findings table (required).** One markdown table, one row per finding, sorted by severity. Never a "Before:/After:" list.

| Severity | Auto | Location | Observed | Recommended | Why |
| --- | --- | --- | --- | --- | --- |

**Part 2 — Verdict (required).** Grouped by severity, highest first, empty tiers omitted:

1. **Blockers** — unreadable, clipped, inaccessible, semantically broken, missing assets, invisible text during load, stress-state failures.
2. **Major** — measure, hierarchy, competing scales, synthesised faces, broken fallback metrics, inconsistent treatment of one role, system-level anti-slop patterns.
3. **Polish** — rag, widows, optical imbalance, punctuation, local spacing.

**Part 3 — Verification log (required).** What you rendered, at what widths, in which stress states, and what you observed. One short paragraph. If you could not render, say so here in the first sentence.

Close with an explicit decision:

- **Block** — any Blocker, or a Major that reaches the whole system.
- **Pass** — no material issue remains. State it in words; silence is not approval.

## Handoff

Findings are emitted in the shared schema (`REVIEW-RUBRIC.md`) so they can be executed and re-verified. Route: implementation to `practical-typography`; systemic multi-file work to `improve-typography`; prose characters to `typeset-content`; family or licence problems to `choose-web-fonts`.
