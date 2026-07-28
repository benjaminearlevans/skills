# Foundations

The body-text decisions everything else derives from, and the authority system that keeps this collection from becoming dogma.

## Authority tags (read this first)

Every rule in this catalog carries a tag. Any skill citing a rule **must** carry the tag with it into its finding. The tag determines what the rule is allowed to do.

- **[Principle]** — durable, medium-independent. May block. Violating one is a defect regardless of context.
- **[Heuristic]** — a diagnostic range, not a constant. May **open an inquiry**, never block on the number alone. A value outside the range means "justify this," not "fix this."
- **[Opinion]** — a defensible aesthetic position, usually Butterick's. May inform a recommendation. Never a finding on its own.
- **[Superseded]** — advice that was correct for its era and is not a modern rule. Cited only to explain why current practice differs. Never a finding.

A skill that blocks on a [Heuristic] or reports an [Opinion] as a defect is malfunctioning.

## The four decisions

**[Principle] Decide body text before anything else.** There is more body text than anything else on the page, so four choices — typeface, size, line spacing, line length — determine most of how the page reads. Everything else is derived from that block.

**[Principle] Headings derive from body text, never the reverse.** A scale built by picking a display size and working down produces oversized headings sitting on undersized copy. Set the body, then step outward.

**[Heuristic] Body size: 15–25px on screen.** Below ~15px, justify it (dense tabular data, secondary metadata, legal fine print are legitimate). Above ~25px for sustained reading is rare outside large-format or low-vision contexts.

**[Heuristic] Line spacing: 120–145% of size.** Expressed unitless in CSS (`line-height: 1.5`). Longer measures and lighter faces want the upper end; short measures, large display sizes, and dense UI want the lower end. Display type above ~40px frequently wants less than 120%.

**[Heuristic] Line length: 45–90 characters including spaces.** The single most-violated rule on the modern web, usually because a reading column was allowed to fill a wide container. Measure in `ch` or cap the container.

**[Opinion] A professional typeface is the most visible single improvement available.** Informs recommendations in `choose-web-fonts`. Never a defect finding — a well-set page in a system font beats a badly set page in a licensed one.

## Maxims

Paraphrased from Butterick's maxims of page layout. All **[Principle]** unless noted.

1. **Body text first.** See above.
2. **Divide the page into foreground and background.** Decide which elements are the subject and which are context. Background must not upstage foreground. The tools for making the distinction are few — position, size, typeface, weight, and sometimes colour — so spend them deliberately.
3. **Adjust in the smallest visible increment.** The distance between not enough and too much is small. If a change is obvious, it is probably too large.
4. **When in doubt, set it both ways and look.** Typographic questions resolve visually, not logically. Render both, compare, decide. **This is a hard rule for any agent working in this collection: do not reason your way to a spacing value you could have rendered.**
5. **Be consistent.** Typography quietly communicates structure. Things that are the same must look the same; things that look different must actually be different. Inconsistent treatment reads as carelessness even when no individual value is wrong.
6. **Relate each new element to existing ones.** Discretion is total only while the page is blank. After that, every addition is constrained by what is already there.
7. **Keep it simple.** If the design seems to need three colours and five typefaces, it does not.
8. **Imitate what you like.** Emulating good work you have studied is faster and better than reinventing. See `ANTI-SLOP.md` for the constraint on *where* you imitate from.
9. **Do not fear white space.** Mediocre typography often comes from a felt need to fill the page. Work outward from the text, not inward from the container edges. If the text is right, the white space resolves itself.

## Derivation order

When building or rebuilding a type system, decide in this order. Each step is constrained by the ones before it.

1. Typeface (see `FONTS.md`)
2. Body size
3. Line spacing
4. Measure
5. Paragraph separation — first-line indent **or** space between paragraphs, never both (`LAYOUT.md`)
6. Heading scale, stepped outward from body
7. Supporting roles: labels, metadata, captions, quotations, code, numeric
8. Spacing scale, related to the body line height
9. Responsive behaviour at each breakpoint

Reversing this order is the root cause of most of the failures catalogued in `ANTI-SLOP.md`.

## Superseded advice

Cited to explain divergence, never enforced.

- **[Superseded] Screen-optimised typefaces are more legible on screen.** True when screens were ~75dpi. Modern displays exceed the resolving power of the eye at normal reading distance, so Georgia, Verdana, and Calibri have no remaining legibility advantage. They retain a *distribution* advantage as system fonts. Choose the face you would want in print.
- **[Superseded] Detect the device in JavaScript to pick type sizes.** Use CSS: container queries, `clamp()`, and media queries.
- **[Superseded] Size body text from viewport width.** Pure `vw` sizing defeats user zoom and browser font-size settings and fails WCAG 1.4.4. Use `rem`, or `clamp()` with a `rem` mid-term.
- **[Superseded] Avoid `ch` units.** `ch` is well supported and is the most direct way to express a measure. Note it resolves against the `0` glyph of the *computed* font, so verify after a font swap.
- **[Superseded] Justified text is the mark of a finished page.** Browser justification without good hyphenation and no h&j engine produces rivers. On the web, ragged-right is usually correct. See `LAYOUT.md`.

## Attribution

The taste foundation of this collection is Matthew Butterick's *Practical Typography* (practicaltypography.com), a reader-supported book. Rules here are restatements, not reproductions. If this collection is useful to you, pay for the book.
