# Anti-slop

The taxonomy of typographic work that is not broken but is not chosen. Rules in `FOUNDATIONS.md` catch defects. This file catches the other failure: everything passes and the result is generic.

Findings from this file are real findings. Their severity is usually Major or Polish, rarely Blocker — but a page that clears every other reference and clears none of this has not been designed.

## Scale and hierarchy failures

- **Huge headings on undersized body.** The signature of a scale built downward from a display size. See `FOUNDATIONS.md` derivation order.
- **Arbitrary scale.** Sizes with no ratio, no rationale, and no relationship to each other — usually the residue of successive one-off decisions.
- **Decoy steps.** A nine-step scale with four steps in use. Every step must have a job.
- **Hierarchy solved with weight.** Five weights doing the work that size, space, and position should be doing.
- **Every card inventing its own hierarchy.** Repeated components are where consistency is actually tested. If three card variants use three different title sizes, there is no system, only a stylesheet.
- **Typography compensating for weak information architecture.** When six things all need to be emphasised, the problem is that the page is trying to say six things. Escalate it as a structure problem; do not fix it with type.

## Colour and treatment failures

- **Five near-identical greys.** Nobody can distinguish them and nobody can state the rule that assigns them.
- **All-caps letterspaced labels everywhere.** One of these is a nice detail. Fourteen is a tic.
- **Gradient text, outlined text, and text shadow** on anything anyone reads.
- **Pure black on pure white** across a long-form reading surface.

## Setting failures

- **Full-width reading columns.** Prose inheriting a wide container's width.
- **Centred paragraphs.**
- **Display faces set at body size** for long-form reading.
- **Fixed heights that clip** enlarged or translated text. Also an accessibility blocker.
- **Manual line breaks** tuning a rag at one viewport width.

## Selection failures

- **Pairing by category.** "Serif for headings, sans for body" with no stated reason.
- **The unchosen default.** The current one is a geometric-ish grotesk with generous whitespace and a 1.25 scale. Ten years ago it was something else. The tell is that nobody in the project can say why this face rather than a near neighbour.
- **A heading scale lifted whole from a starter template**, then never questioned.
- **A typeface change proposed as a fix** for a scale, measure, or hierarchy problem.

## The cargo cult

Butterick's argument in the *websites* chapter is the spine of this file. Template systems and component libraries were supposed to free designers from fiddly technical work so they could think about design. Mostly they accelerated adoption of a new set of unexamined defaults. Page by page the web looks better than it did a decade ago, at the cost of looking the same everywhere. **Ugly was traded for boring.**

The failure mode is not incompetence. It is lateral imitation — looking at other websites for ideas, because that is the easiest place to look, and arriving where everyone else arrived.

**The prescription is not originality for its own sake. It is to imitate from better and wider sources.** Books. Posters. Type specimens. Signage. Editorial design. Software from other eras. Printed ephemera. Anything with a typographic tradition longer than the web's. Stealing is fine; steal from further away.

## Declaring a register is not amnesty

A project's `TYPE-BRIEF.md` may suspend named patterns in this file — Display-led suspends huge-headings, Expressive suspends gradient-text in declared display roles. That suspension is conditional and narrow:

- It requires a **stated reason**. Without one, the pattern still applies.
- It activates the register's **substitute checks** from `REGISTERS.md`, which are stricter. Display-led buys latitude on heading size by accepting harder scrutiny of the body block, the display tracking, the measure at display size, and the 320px reflow.
- It never reaches `[Principle]` rules or `ACCESSIBILITY.md`.

**And it does nothing at all for the last section of this file.** No register excuses the unchosen default. A brief that declares "Display-led" and cites nothing, overrides nothing, and accepts no failure mode has not made a decision — it has attached a label to one. Report that: the register is undeclared in substance regardless of what the heading says.

## How to report this

Findings from this file must be **specific and evidenced**, never a vibe. Wrong: "the typography feels generic." Right: "Every one of the four card variants sets its title at a different size (16/17/18/20px) with no rule distinguishing them; the underlying decision — what a card title *is* — has not been made."

State what was not decided, and what deciding it would require. Do not propose a redesign in a review; that is `improve-typography`'s job or the user's.
