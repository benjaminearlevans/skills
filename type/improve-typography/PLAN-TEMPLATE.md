# Plan template

One file per plan in `plans/`. Named `NN-short-slug.md`. The executor has **zero context from the audit conversation and zero typographic taste**. Every value they need is in this file or the plan has failed.

---

```markdown
# Plan NN — <imperative title>

## Leverage
One sentence: what improves, and across how much of the product.

## Severity / automation
Severity: Blocker | Major | Polish
Automation: SAFE-AUTO | CONTEXTUAL | NEVER-AUTO
Rules: FOUNDATIONS.md#line-length, WEB-PLATFORM.md#loading

## Context the executor needs
Three to six sentences. What the current state is and why it is wrong.
State the rule and its authority tag. If the rule is a [Heuristic], state
why this specific case falls outside the acceptable range rather than
citing the number alone.

## Scope
In scope: exact files and selectors.
Out of scope: named, so the executor does not wander.

## Changes

### 1. path/to/file.css:120

Before:
```css
.prose { font-size: 15px; line-height: 1.4; }
```

After:
```css
.prose { font-size: 1.0625rem; line-height: 1.6; max-inline-size: 68ch; }
```

Why: <one sentence tied to the rule>

### 2. path/to/next/file.tsx:44
...

## Do not change
Anything not listed above. In particular: <named adjacent things the
executor might be tempted to tidy>.

## Verification
1. Run: <exact command, with the folder it runs in>
2. Render <route> at 360px, 768px, 1280px.
3. Confirm measure is 45–90 characters — count on the widest breakpoint.
4. Set browser font size to 200%; confirm no clipping or overlap.
5. Reflow at 320px; confirm no horizontal scroll.
6. Apply the WCAG 1.4.12 text-spacing overrides; confirm no content loss.
7. Block font loading; confirm layout does not shift on swap.

## Screenshots to capture
- <route> at 360px, before and after
- <route> at 1280px, before and after
- <route> at 200% text enlargement, after

## Done when
- [ ] Every change above applied exactly
- [ ] Every verification step passes
- [ ] No file outside Scope modified
- [ ] Screenshots captured
```

---

## Rules for writing plans

1. **Inline every value.** Never reference the audit, another plan, or "the standard we discussed."
2. **Exact paths and line numbers,** with a code excerpt so the executor can confirm they are in the right place.
3. **Before and after as literal code,** not prose description.
4. **Specify the folder every command runs in.**
5. **A "Do not change" section is mandatory.** Uncontained executors tidy.
6. **Verification is objective.** "Looks better" is not a step. "Measure is 45–90 characters" is.
7. **One concern per plan.** If a plan has two unrelated concerns it is two plans.
8. **If the plan requires a taste decision, it is not a plan.** Escalate to the user, or resolve it in the audit and inline the resolved value.
