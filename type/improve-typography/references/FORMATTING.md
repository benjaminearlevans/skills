# Formatting

Emphasis, case, hierarchy, and the treatment of individual runs of text. Where `COMPOSITION.md` governs characters, this governs how they are styled.

## Emphasis

**[Principle] Emphasis is a limited currency.** The more text is emphasised, the less any of it means. Applied to a whole paragraph, emphasis conveys nothing.

**[Principle] Bold or italic, not both.** Bold-italic in running prose is almost always a mistake.

**[Principle] Never underline, except links.** Underlining is a typewriter substitute for italic. On the web the one legitimate use is link affordance — where it is not merely allowed but required (see `ACCESSIBILITY.md`).

**[Principle] Real weights and real italics only.** A browser-synthesised bold is a smeared regular; a synthesised italic is a slanted roman. Set `font-synthesis: none` and load the actual faces. Semantically, `<em>` and `<strong>` carry meaning; `<i>` and `<b>` carry appearance.

**[Heuristic] Two weights carry most interfaces.** Three is comfortable. Five distinct weights in one system usually means the hierarchy is being solved with weight because it was not solved with size, space, and position.

## Case

**[Principle] All caps for less than one line.** Capitals slow reading because word shapes disappear. Fine for a short label, a byline, a button. Not for a sentence, never for a paragraph.

**[Heuristic] Caps and small caps take 5–12% added tracking.** Capitals are drawn with spacing tuned for mixed-case setting and look cramped when set together. In CSS use `em`, not `px`, so tracking scales with size.

**[Principle] Never letterspace lowercase body text.** Tracking on running text at reading sizes degrades word cohesion.

**[Heuristic] Large display sizes want negative tracking.** Type designed at text sizes is spaced for text sizes. Set at 48px and up, tighten — often `-0.01em` to `-0.03em`. Optical-size axes handle this automatically where available (`WEB-PLATFORM.md`).

**[Principle] Small caps must be real.** See `COMPOSITION.md`. Faux small caps — scaled capitals — have wrong stroke weight and wrong proportions.

## Hierarchy

**[Principle] Hierarchy comes from semantic HTML first.** Set `h1`–`h6`, `strong`, `em`, `blockquote`, `figcaption`, `dl` correctly, then style them. Hierarchy expressed only in class names is invisible to assistive technology and to any future maintainer.

**[Principle] The toolkit for distinction is small: position, size, weight, typeface, and sometimes colour.** Use the fewest that work. A heading distinguished by size alone is usually cleaner than one distinguished by size, weight, colour, tracking, and case together.

**[Principle] Heading levels are a document outline, not a size menu.** Do not skip levels to get a size. One `h1` per page.

**[Heuristic] Keep the scale compact.** A ratio in the range of roughly 1.125–1.25 for interface text and up to ~1.333 for editorial gives usable steps. Larger ratios produce the huge-heading/small-body failure in `ANTI-SLOP.md`. Every step must have a job; a scale with nine steps and four uses is four steps with five decoys.

**[Principle] Same role, same treatment.** A card title on the marketing site and a card title in the product are either the same thing (style them identically) or different things (make the difference legible). This is where most systems rot.

## Colour

**[Principle] Text colour is part of typography, not decoration.** Weight, size, and colour trade against each other — lighter text at small size fails contrast that the same colour passes at large size.

**[Heuristic] Three text colours are usually enough:** primary, secondary, and a disabled/placeholder value. Interfaces routinely accumulate five near-identical greys that no reader can distinguish and no designer can assign a rule to. If two values are within a few percent of each other, they are one value.

**[Principle] Never use colour alone to convey meaning.** See `ACCESSIBILITY.md`.

**[Opinion] Pure black on pure white is harsher than necessary** on emissive displays. A very dark neutral usually reads better. Do not take this so far that contrast fails.

**[Principle] Gradient text, text shadows, and outlined text are display effects.** Legitimate in a hero at 72px, a defect in anything anyone has to read.

## Numerals

**[Principle] Tabular figures in columns of numbers.** `font-variant-numeric: tabular-nums`. Any table, price list, timer, counter, or right-aligned numeric column. Proportional figures make numbers jitter as they update and misalign as they stack.

**[Heuristic] Oldstyle figures in flowing prose** where the face offers them — they sit at x-height and disturb the line less. Lining figures with capitals and in UI.

**[Principle] Numeric alignment follows the numeral.** Right-align or decimal-align numbers; left-align text. Centred numeric columns are unreadable.

**[Principle] Ordinals set inline.** `1st`, not raised-and-underlined, unless the face's `ordn` feature draws them properly.

## Mixing typefaces

**[Principle] A pairing needs a reason.** "Serif headings, sans body" is a category, not a decision. State what the second face is doing that the first cannot: a different voice, a genuinely different job (interface chrome vs. editorial body), or a functional need (monospace for code, a face with the figure sets a data view requires).

**[Heuristic] Pair on contrast, not similarity.** Two faces that are nearly alike read as a mistake. Two that are clearly different read as intent.

**[Heuristic] One family is a legitimate answer.** A single good family with a real italic, two or three weights, and full figure sets will out-perform most pairings, and costs less to load.

**[Principle] Optical spacing over metric spacing where the tool offers it**, for display setting. On the web this mostly means trusting a well-kerned face and leaving `font-kerning: normal`.
