# Glossary

Organised by what someone would *describe*, not alphabetically. Each entry: **term** — the description someone would give — the technical handle.

## Space between things

- **Leading** — the space between lines of text. Print term, measured baseline to baseline. On the web, `line-height` — which is not identical: CSS distributes the extra space half above and half below each line, so the two are related but not interchangeable.
- **Tracking** (letterspacing) — uniform space added or removed across a run of characters. `letter-spacing`, in `em`.
- **Kerning** — space adjusted between one *specific pair* of characters, to correct an optical gap (the classic being `AV` or `To`). `font-kerning`, OpenType `kern`. **Not the same as tracking** — tracking is global, kerning is per-pair.
- **Measure** — the length of a line of text, conventionally counted in characters. `max-inline-size` in `ch`.
- **Word space** — the space between words, adjustable in justified setting. `word-spacing`.
- **Sidebearing** — the built-in space on either side of a glyph, part of the font's design.
- **Set width** — the total horizontal space a glyph occupies including sidebearings.

## Parts of a letter

- **x-height** — the height of a lowercase `x`; the main determinant of how large a face *looks* at a given point size.
- **Cap height** — the height of a capital letter.
- **Ascender** — the part rising above x-height, as in `b`, `d`, `k`.
- **Descender** — the part dropping below the baseline, as in `p`, `g`, `y`.
- **Baseline** — the invisible line the letters sit on.
- **Counter** — the enclosed or partly enclosed space inside a letter, as in `o`, `e`, `a`.
- **Aperture** — the opening of a partly closed letter, as in `c`, `s`, `e`. Narrow apertures reduce legibility at small sizes.
- **Bowl** — the rounded stroke enclosing a counter.
- **Stem** — the main vertical stroke.
- **Terminal** — how a stroke ends where there is no serif.
- **Spur, ear, tail, finial, shoulder, crossbar** — the small identifying features used in font identification.
- **Stress** — the axis of thickest-to-thinnest in a round letter. Vertical stress reads as modern, angled as humanist.

## Things that go wrong

- **Widow** — a short final line of a paragraph stranded at the top of a column or page. In web usage it also means a single word alone on the last line of a paragraph or heading. `text-wrap: pretty`.
- **Orphan** — the first line of a paragraph stranded at the bottom of a column or page. **The pair is routinely swapped** — the memory aid is that an orphan is left behind at the start, a widow is left alone at the end.
- **Rivers** — pale vertical channels of white running down a block of justified text, caused by uneven word spacing. Fixed with hyphenation, a different measure, or ragged-right setting.
- **Ladder** (stack) — three or more consecutive lines ending in a hyphen. `hyphenate-limit-lines`.
- **Rag** — the uneven right edge of unjustified text. A *good* rag varies gently; a *bad* rag makes shapes or has one very short line among long ones.
- **Tofu** — the empty rectangle shown when the font has no glyph for a character. The literal `.notdef` glyph.
- **Mojibake** — text rendered as nonsense characters because of an encoding mismatch. Distinct from tofu — tofu is a missing glyph, mojibake is misinterpreted bytes.
- **Faux bold / faux italic / synthetic small caps** — the browser inventing a weight, slant, or small caps the family does not contain. `font-synthesis: none`.
- **Layout shift on font swap** — the page jumping when a webfont replaces the fallback. Fixed with `size-adjust` and the metric override descriptors.
- **FOIT** — flash of invisible text: nothing renders until the font loads. `font-display: block`.
- **FOUT** — flash of unstyled text: the fallback renders, then swaps. `font-display: swap`. **FOUT is generally preferable to FOIT** — the reader can read.
- **FOFT** — flash of faux text: a synthesised weight renders before the real one arrives.

## Alignment and setting

- **Justified** — both edges flush. Requires hyphenation to avoid rivers.
- **Ragged right** (flush left) — the default and usually correct setting for the web.
- **H&J** — hyphenation and justification, the engine that decides line breaks in professional composition. Browsers have a weak one.
- **Hanging punctuation** — pulling quotation marks and hyphens slightly outside the text edge so the margin looks optically straight. `hanging-punctuation`.
- **Optical margin alignment** — the general version of the same idea, applied to all glyphs.
- **Hanging indent** (outdent) — first line to the left of the rest of the block. Standard for lists and bibliographies.
- **First-line indent** — the opposite. Never combine with space between paragraphs.
- **Drop cap** — an oversized opening letter set down into the first lines. **Initial cap** (raised cap) — the same idea sitting on the baseline and rising above.
- **Run-in head** — a heading set on the same line as the text it introduces.
- **Folio** — a page number. **Recto/verso** — right-hand and left-hand pages.
- **Grade** — a weight-like axis that changes apparent darkness without changing widths, so text does not reflow. Variable axis `GRAD`.

## Numerals

- **Lining figures** — numerals all at cap height, aligned. OpenType `lnum`.
- **Oldstyle figures** (text figures) — numerals with ascenders and descenders that sit at x-height. OpenType `onum`. Better inside running prose.
- **Tabular figures** — every numeral the same width, so columns align and updating numbers do not jitter. OpenType `tnum`.
- **Proportional figures** — each numeral its natural width. OpenType `pnum`.
- **Superiors / inferiors** — raised and lowered small numerals for footnotes and chemistry. `sups`, `sinf`.
- **Slashed / dotted zero** — a zero disambiguated from a capital O, standard in monospace. Often `zero` or a stylistic set.

## Font features

- **Ligature** — two or more letters drawn as one glyph, most commonly `fi` and `fl`. Standard: `liga`. **Discretionary ligature** — an ornamental one, off by default: `dlig`.
- **Small caps** — capitals drawn at roughly x-height with correct stroke weight. `smcp`. **Petite caps** — smaller still, at true x-height: `pcap`.
- **Stylistic set** — an alternate design for a group of glyphs, e.g. a single-storey `a`. `ss01`–`ss20`.
- **Swash** — an ornamental extended variant. `swsh`.
- **Titling caps** — capitals redrawn for large display sizes with lighter strokes. `titl`.
- **Optical size** — a face redrawn per size: more contrast and tighter spacing when large, the opposite when small. Variable axis `opsz`, `font-optical-sizing: auto`. **This is the correct answer to "why does my heading look too loose?"**
- **Hinting** — instructions telling a rasteriser how to snap a glyph to a low-resolution pixel grid. Largely obsolete on modern displays.

## Classification

- **Humanist / old-style (garalde)** — angled stress, modest contrast, calligraphic. Garamond, Jenson.
- **Transitional** — more vertical stress, more contrast. Baskerville, Times.
- **Didone (modern)** — vertical stress, extreme contrast, hairline serifs. Bodoni, Didot. Poor at small sizes.
- **Slab serif** — heavy rectangular serifs. Clarendon, Rockwell.
- **Grotesque / neo-grotesque** — early sans; neo-grotesque is the tighter, more neutral mid-century version. Akzidenz, Helvetica.
- **Geometric sans** — built from circles and straight lines. Futura, Avenir.
- **Humanist sans** — sans with calligraphic proportions and open apertures; generally the most legible sans at text size. Frutiger, Gill Sans.
- **Superellipse / rounded / squarish** — descriptive rather than historical categories.

## Web delivery

- **Subsetting** — stripping unused glyphs from a font file. Paired with `unicode-range` so the browser only fetches what it needs.
- **Variable font** — one file with continuous axes. Common axes: `wght`, `wdth`, `opsz`, `slnt`, `ital`, `GRAD`.
- **Font stack** — the ordered `font-family` list, real face first, metric-adjusted fallback next.
- **Metric override descriptors** — `size-adjust`, `ascent-override`, `descent-override`, `line-gap-override`. What you use to stop a fallback shifting the page.
- **Balance / pretty** — `text-wrap: balance` evens out line lengths in short blocks like headings; `text-wrap: pretty` fixes orphaned last words in body copy.
