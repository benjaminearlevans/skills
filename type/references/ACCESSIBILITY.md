# Accessibility

Typographic requirements that come from WCAG and from real reading conditions, not from Butterick. These are **[Principle]** throughout and they block.

## The four stress states

Every typographic change is verified in all four. A layout that only works in the default state is not finished.

1. **200% text enlargement** (WCAG 1.4.4, AA). Text scales to 200% with no loss of content or function. Test by increasing the browser's font size, not by zooming the page — page zoom scales everything and hides the failure.
2. **320 CSS pixel reflow** (WCAG 1.4.10, AA). Content reflows into a 320px-wide column — equivalent to 400% zoom at 1280px — without horizontal scrolling. Exceptions exist for content requiring two-dimensional layout, such as data tables and maps.
3. **Text-spacing override** (WCAG 1.4.12, AA). No content loss when the user forces `line-height: 1.5`, paragraph spacing `2em`, `letter-spacing: 0.12em`, `word-spacing: 0.16em`. Run these as a user stylesheet and look for clipping.
4. **Fonts blocked.** The page is readable and correctly laid out on the fallback stack, with no shift on swap.

## Blockers

**Fixed heights on text containers.** The single most common failure of states 1 and 3, and the most common failure under translation. Use `min-height` or let content size the box. A card with `height: 88px` will clip in German and clip at 200%.

**Text in images.** Cannot be enlarged, selected, translated, or read aloud. Logos excepted.

**Invisible text during font load.** See `WEB-PLATFORM.md`.

**Contrast below threshold.** WCAG 1.4.3 AA: 4.5:1 for text below 24px (or below 19px bold), 3:1 at or above. AAA is 7:1 and 4.5:1. Applies to placeholder text, disabled-looking-but-active text, and text over images — where a scrim or text shadow may be needed to guarantee it.

**Colour as the sole distinction** (WCAG 1.4.1). Links inside body copy need a non-colour signal — in practice, an underline. A link distinguished from surrounding prose only by colour is a defect regardless of contrast ratio.

**Absolute font units.** `px` on the root, or type sized purely in `vw`, defeats user settings. See `WEB-PLATFORM.md`.

**Broken heading order.** Skipped levels, multiple `h1`, or headings chosen for their size. Screen-reader users navigate by heading; the outline is a navigational structure, not a style hook.

**Missing or wrong `lang`.** Governs hyphenation, quote characters, font fallback selection, and screen-reader pronunciation. A `lang` mismatch is a typographic bug as much as an accessibility one.

## Localization

**Text expands.** German and Finnish run roughly 30–35% longer than English; Russian around 20%; CJK is shorter but taller and needs more line height. Any component sized to fit its English string will break.

**Line breaking differs.** CJK breaks between characters, not at spaces. Thai has no spaces. Arabic and Hebrew are RTL and require logical properties — `margin-inline-start`, `padding-inline-end`, `text-align: start` — rather than left and right.

**Not every script has these concepts.** Italic, small caps, and letterspacing have no meaning in many scripts, and letterspacing actively breaks Arabic by disconnecting joined letterforms.

**Verify glyph coverage per locale.** A missing glyph triggers a mid-word fallback that looks like a rendering bug.

## Reading conditions

Dyslexia-friendly claims for specific typefaces are weak in the evidence. What does hold: adequate size, generous line spacing, a controlled measure, ragged-right setting, strong contrast, and respecting the user's own settings. Those are the same things good typography wants anyway — which is the point.
