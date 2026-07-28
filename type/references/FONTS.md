# Fonts

Choosing a typeface. `WEB-PLATFORM.md` covers delivering one.

## The first question

**[Principle] Is the existing family already good enough?** The default answer is yes more often than agents assume. Changing a typeface is one of the most expensive changes available — it invalidates the scale, the measure, the vertical rhythm, and every screenshot. Change it only when a stated requirement fails, not because a different face would be pleasant.

Grounds for change that are real: missing script coverage; no true italic; missing figure sets a data-dense product needs; a licence that does not permit the intended use; a payload that cannot be subset to budget; a display face doing the job of a text face.

Grounds that are not: "feels dated," "everyone uses it," unattributed taste.

## Evaluation criteria

Assess a candidate against all of these before recommending it.

1. **Purpose.** Interface, editorial body, marketing display, data-dense, code, or mixed. A face optimised for one is often wrong for another. **[Principle] Display faces are not for long-form reading** — tight spacing and high contrast that read well at 64px fail at 17px.
2. **Reading size and measure.** A face's x-height, counters, and spacing determine how it behaves at the size you will actually set it. Evaluate at the real size, on the real measure, in the real medium — never from a specimen poster.
3. **Family completeness.** A true italic (drawn, not sloped). Enough real weights. Small caps if the design calls for them. Both figure sets — lining and oldstyle, tabular and proportional. Currency and mathematical symbols. **[Principle] A family without a true italic cannot set body prose.**
4. **Script and language coverage.** Check every locale the product ships in, including diacritic-heavy Latin (Polish, Vietnamese, Czech), Greek, Cyrillic, CJK, and RTL scripts. A missing glyph falls back mid-word and is a defect.
5. **Licensing.** Web embedding permitted, pageview or domain limits, self-hosting permitted, subsetting permitted, whether the licence covers the app as well as the marketing site. **[Principle] A licence problem is a blocker, not a preference.**
6. **Delivery.** Available as WOFF2, subsettable, variable axes if useful, total payload against budget. See `WEB-PLATFORM.md`.
7. **OpenType support.** `kern`, `liga`, `smcp`, `onum`/`lnum`, `tnum`/`pnum`, `frac`, `ss__` stylistic sets, and an `opsz` axis if present.
8. **Fallback compatibility.** How far the metrics sit from the fallback stack, and whether `size-adjust` can close the gap. A face with an unusually large or small x-height relative to its em is harder to fall back from.

## Positions worth holding lightly

**[Opinion] Butterick favours professionally licensed text faces** over system and open-source fonts, and is specifically hostile to Google Fonts. Treat this as an informed preference, not a rejection rule. Many open and system faces are excellent; several widely used ones are not. Judge the individual face against the criteria above, not its distribution channel.

**[Principle] The durable version of that argument:** font quality matters, and it cannot substitute for composition and layout. A well-chosen face set at the wrong size on the wrong measure is worse than a plain face set correctly. Never recommend a typeface change as a fix for a problem that is actually a scale, measure, or hierarchy problem.

**[Superseded] Screen-optimised faces are more legible on screen.** See `FOUNDATIONS.md`.

**[Opinion] System font stacks are a legitimate choice**, not a failure of nerve — zero payload, no layout shift, native feel on each platform. Their cost is that the design looks different everywhere and you control none of it.

## Pairing

**[Principle] A pairing requires a stated rationale.** See `FORMATTING.md`. If the rationale is "serif for headings, sans for body," there is no rationale.

**[Heuristic] Three families is the practical ceiling** for most products: one text, one display or interface, one monospace. Often two. Often one.

**[Principle] Monospace is for code and for aligned data**, not for body prose and not for atmosphere. Its uniform widths are a functional property, not a style.

## Output expectations

`choose-web-fonts` recommends **no more than three directions, with one marked as the default**, each carrying: the families, the rationale tied to the criteria above, the trade-offs, the licence position, the payload, and the implementation. A recommendation without a trade-off has not been thought about.
