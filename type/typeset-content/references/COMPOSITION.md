# Composition

Character-level correctness in prose. This is the catalog `typeset-content` runs on, and the one `review-typography` cites when it finds a straight quote in a heading.

Every rule carries an **authority tag** (see `FOUNDATIONS.md`) and an **automation risk** (see `REVIEW-RUBRIC.md`): `SAFE-AUTO`, `CONTEXTUAL`, or `NEVER-AUTO`.

## Hard exclusion zones

**Nothing in this file may be applied inside:** code blocks, inline code, `<pre>`/`<code>`, URLs, email addresses, file paths, identifiers, CLI examples, regular expressions, JSX/TSX attribute values, template literal expressions, YAML/TOML/JSON keys and values that are configuration rather than prose, HTML attribute values, or any localization string without a known locale.

This exclusion is **[Principle]** and absolute. A curly quote in a shell command is a broken shell command.

## Quotes and apostrophes

**[Principle] Use typographic quotes in prose.** `"` `"` and `'` `'`, not `"` and `'`. — `SAFE-AUTO` in prose.

**[Principle] Apostrophes point downward** — they take the closing-single form (`'`), shaped like a 9, never the opening form shaped like a 6. — `SAFE-AUTO`.

**[Principle] Elisions take a closing apostrophe, not an opening quote.** This is the single most common smart-quote bug, because naive algorithms see a leading `'` and open a quotation. Correct: `'90s`, `'tis`, `'em`, `rock 'n' roll`, `fish 'n' chips`. Wrong: `'90s`. — `SAFE-AUTO` against a maintained elision list; `CONTEXTUAL` otherwise.

**[Principle] Nesting: doubles outside, singles inside** in US convention. — `CONTEXTUAL`.

**[Principle] Locale governs quote characters.** `„…"` in German, `«… »` with non-breaking spaces in French, `「…」` in Japanese, `«…»` in Russian. — `NEVER-AUTO` without a declared locale.

**[Principle] Foot and inch marks are straight, or better, primes.** `5′ 11″` ideally; `5' 11"` acceptable; `5' 11"` is wrong. Same for minutes and seconds of arc and time. — `CONTEXTUAL` (requires recognising a measurement).

## Dashes and hyphens

**[Principle] Three characters, three jobs.** Hyphen `-` joins compounds and breaks words. En dash `–` spans ranges and expresses "to" or "through" (`1914–18`, `Monday–Friday`, `London–Paris route`), and joins compound adjectives where one element is already multi-word (`post–World War II`). Em dash `—` marks a parenthetical break in a sentence. — `CONTEXTUAL`.

**[Principle] Never simulate a dash with multiple hyphens.** `--` and `---` are typewriter artifacts. — `SAFE-AUTO` in prose.

**[Opinion] Em dash spacing.** Unspaced (`word—word`) is US convention; spaced en dash (`word – word`) is common in UK and European setting. Pick one, apply consistently. — `NEVER-AUTO`; consistency is the finding, not the choice.

**[Principle] A hyphen is not a minus sign.** Use `−` (U+2212) in mathematical contexts. — `CONTEXTUAL`.

## Spaces and breaks

**[Principle] One space between sentences.** Two is a typewriter habit; proportional fonts already space sentences correctly. — `SAFE-AUTO`.

**[Principle] Never two consecutive word spaces**, and never spaces used to create indentation or alignment in prose. — `SAFE-AUTO`.

**[Principle] Use non-breaking spaces to prevent bad breaks:** after `¶` and `§`, between a number and its unit (`10 kg`, `4 GB`), between initials and surname, in `Fig. 4`, `p. 12`, `Ch. 3`, and before the final word of a heading to prevent a one-word last line. — `CONTEXTUAL`.

**[Principle] No manual line breaks for visual adjustment in flowing text.** A `<br>` inserted to fix a rag at one viewport width breaks at every other width. Use `text-wrap: balance`, a `<wbr>`, or a non-breaking space. — `CONTEXTUAL`.

**[Heuristic] Optional (soft) hyphens** `&shy;` are legitimate for long unbreakable compounds in narrow columns, especially in German. — `NEVER-AUTO`.

## Marks and symbols

**[Principle] Ellipsis is one character** — `…` (U+2026), not `...`. Spacing around it follows house style. — `SAFE-AUTO`.

**[Principle] Use real symbol characters**, not alphabetic approximations: `©` not `(c)`, `®` not `(r)`, `™` not `(tm)`, `°` not `o`, `×` not `x` in dimensions, `÷`, `≤`, `≥`, `≠`, `±`, `→`. — `SAFE-AUTO` for the unambiguous ones; `CONTEXTUAL` for `×` (which collides with the letter).

**[Principle] Use real accented characters**, not unaccented substitutes or combining hacks. Normalise to NFC. — `SAFE-AUTO`.

**[Principle] Fractions use real glyphs or the `frac` OpenType feature**, not `1/2` set as three characters. — `CONTEXTUAL`.

**[Heuristic] One exclamation point is plenty in a long document.** — `NEVER-AUTO`; report only.

**[Opinion] Ampersands are for proper names**, not as a general substitute for "and". — `NEVER-AUTO`; report only.

## Ligatures and figures

**[Principle] Standard ligatures on in text** (`fi`, `fl`, `ffi`), via `font-variant-ligatures: common-ligatures`. — see `WEB-PLATFORM.md`.

**[Principle] Discretionary ligatures off by default.** They are display ornaments. — `SAFE-AUTO` as a CSS default.

**[Principle] No ligatures in code.** Programming ligatures alter the visual identity of operators and are a legibility hazard in a context where character-level accuracy is the whole point. — `SAFE-AUTO` as a CSS default (`font-variant-ligatures: none` on `code`, `pre`).

**[Principle] Figure sets have jobs.** Tabular lining figures in columns of numbers; proportional oldstyle figures in flowing prose if the face has them. See `FORMATTING.md`. — `CONTEXTUAL`.

## Small caps

**[Principle] Real small caps only.** If the face has no `smcp`, do not use small caps at all. `font-variant-caps: small-caps` may synthesise; `font-synthesis-small-caps: none` prevents it. — `SAFE-AUTO` as a CSS guard.

**[Heuristic] Small caps and full caps take 5–12% added tracking.** — `CONTEXTUAL`.

## Application matrix

`SAFE-AUTO` — apply without asking, inside prose, outside exclusion zones: repeated spaces, double sentence spacing, `...` → `…`, `--`/`---` → dash, straight quotes and apostrophes in unambiguous prose, `(c)`/`(tm)`/`(r)`, unaccented substitutes with a known target, discretionary-ligature and code-ligature CSS defaults.

`CONTEXTUAL` — propose with a diff, require confirmation: hyphen↔en dash, quote nesting, non-breaking space insertion, foot/inch and prime marks, `×`, fractions, figure-set changes, removal of manual line breaks, tracking on caps.

`NEVER-AUTO` — report only, never modify: user-generated content, legal or quoted text where the source characters are evidentiary, localization strings without a locale, house-style choices (em dash spacing, ampersand usage), exclamation-point density, soft hyphens, anything inside an exclusion zone.
