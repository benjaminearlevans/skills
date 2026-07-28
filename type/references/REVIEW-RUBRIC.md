# Review rubric

The shared vocabulary. `review-typography`, `improve-typography`, and `typeset-content` all emit findings in this shape, which is what lets them chain: an `improve` plan can be executed and then verified by `review` against the same rule ids.

## Two orthogonal axes

Every finding carries **both**. They answer different questions and neither implies the other.

### Severity — how much it matters

- **Blocker.** Unreadable, clipped, inaccessible, semantically broken, missing font assets, invisible text during load, licence violation, layout shift on font swap, failure of any stress state in `ACCESSIBILITY.md`. Blocks approval.
- **Major.** Off-measure body text, absent or incoherent hierarchy, competing type scales, synthesised faces, broken fallback metrics, inconsistent treatment of the same role, an `ANTI-SLOP.md` pattern at system level.
- **Polish.** Awkward rag, a widow, optical imbalance, punctuation, local spacing, a single instance of a pattern that is fine elsewhere.
- **Pass.** No material issue remains. Stated explicitly, never implied by silence.

### Automation risk — who is allowed to fix it

- **SAFE-AUTO.** Deterministic, reversible, no judgement, no ambiguity. Apply without asking.
- **CONTEXTUAL.** Correct fix depends on meaning, locale, or design intent. Propose a diff; require confirmation.
- **NEVER-AUTO.** Report only. User-generated content, evidentiary or legal text, localization strings without a locale, house-style choices, anything inside a `COMPOSITION.md` exclusion zone, and anything requiring a design decision the user has not made.

A Blocker can be NEVER-AUTO. A Polish item can be SAFE-AUTO. Do not collapse the axes.

## Project register (read before judging)

If `TYPE-BRIEF.md` exists at the project root, **load it first**. It declares the project's register and its deliberate overrides, and it changes what counts as a finding. Full precedence rules in `REGISTERS.md`; in short:

- A declared override with a stated reason **suspends** the named `[Heuristic]` or `ANTI-SLOP.md` pattern, and **activates the register's substitute checks** — which are usually stricter, on a different axis.
- No brief overrides a `[Principle]` or anything in `ACCESSIBILITY.md`. Ever.
- An override with no stated reason is not an override: apply the default, and raise the missing reason as a Major finding against the brief.
- **The brief adds obligations.** Anything it declares — one family, a fixed display tracking, a capped weight count — becomes checkable. Divergence from the brief is a finding in its own right, tagged `TYPE-BRIEF#<section>`.

If no brief exists, judge against the catalog defaults, and say once in the verdict that no brief was found. Do not infer a register from the code — an undeclared register is indistinguishable from an accident, which is the point.

## Finding schema

Every finding, in every skill:

- `id` — stable within the report, e.g. `TY-014`
- `rule` — the reference file and rule, e.g. `FOUNDATIONS.md#line-length`, or `TYPE-BRIEF#obligations` for a divergence from the declared brief
- `authority` — Principle / Heuristic / Opinion (see `FOUNDATIONS.md`)
- `severity` — Blocker / Major / Polish
- `automation` — SAFE-AUTO / CONTEXTUAL / NEVER-AUTO
- `location` — `file:line`, selector, component, or route
- `observed` — what is there now, quoted exactly
- `recommended` — the exact replacement value, not a direction
- `why` — one sentence, tied to the rule

**A finding citing a [Heuristic] may not be a Blocker on the number alone.** It opens an inquiry: state the observed value, the range, and what would justify sitting outside it. **A finding citing an [Opinion] may not be a defect at all** — it is a recommendation, and must be labelled as one.

## Output contract

Findings render as a single markdown table, one row per finding, never as a "Before:/After:" list:

| Severity | Auto | Location | Observed | Recommended | Why |
| --- | --- | --- | --- | --- | --- |

Then a verdict, grouped by severity, highest tier first, empty tiers omitted. Close with an explicit **Block** or **Pass**.

## Escalation triggers

Flag on sight:

- Body text outside 15–25px with no stated reason
- A reading column with no `max-inline-size`, or a measure over ~90ch
- `line-height` with a unit; `font-size` in `px` on the root; type sized in bare `vw`
- Both first-line indent and inter-paragraph space
- Justified text without `hyphens: auto`
- Centred paragraphs
- Missing `font-synthesis: none` where a family lacks a real italic or the needed weights
- `font-display: block`, or no `font-display` at all
- `@font-face` with no metric-adjusted fallback
- Fixed `height` on any container holding text
- Text in an image
- Heading levels skipped, or more than one `h1`
- In-prose links distinguished by colour alone
- Missing or wrong `lang`
- Straight quotes, `--` as a dash, `...` as an ellipsis in prose
- Synthesised small caps
- Proportional figures in a numeric column
- Three or more near-identical text colours
- Four or more weights in one system
- The same semantic role set differently in two places

## Remedial preference hierarchy

When proposing fixes, prefer earlier moves to later ones. Later moves are more expensive and more likely to be wrong.

1. **Delete it.** The redundant weight, the fifth grey, the decoy scale step, the rule that space could replace.
2. **Use an existing token or component.** Never introduce a new value where one exists within a few percent.
3. **Fix the body block** — size, line height, measure. Most downstream symptoms resolve here.
4. **Fix the derivation** — rebuild the heading scale outward from the corrected body.
5. **Fix semantics** — correct heading levels, `<em>`/`<strong>`, `lang`, table headers.
6. **Fix delivery** — `font-display`, preload, metric-matched fallback, subsetting, `font-synthesis`.
7. **Fix composition** — hand to `typeset-content`; do not hand-edit prose characters inside a CSS review.
8. **Polish** — `text-wrap`, tracking, rag, hanging punctuation.
9. **Change the typeface.** Last, and only against `FONTS.md` criteria. Never as a fix for 3–5.

## Verification requirement

**No finding about appearance may be raised or closed without rendering.** Narrow (~360px), medium (~768px), wide (~1280px+), plus the four stress states in `ACCESSIBILITY.md` where relevant. If rendering is not available in the current environment, say so explicitly in the report and mark the affected findings as unverified rather than asserting them.
