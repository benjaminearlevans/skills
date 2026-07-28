# Web platform

Typography as the browser actually implements it. This is the layer Butterick does not cover; it comes from CSS Fonts Level 4, CSS Text, and current browser behaviour.

## Loading

**[Principle] Text must never be invisible while a font loads.** `font-display: swap` or `optional`. `block` produces a flash of invisible text and fails the reader. `optional` is strongest for body text on repeat visits; `swap` is the safe general default.

**[Principle] Preload the fonts used above the fold**, `<link rel="preload" as="font" type="font/woff2" crossorigin>`. Without `crossorigin` the preload is discarded and fetched twice.

**[Principle] Self-host in WOFF2.** Third-party font CDNs add a connection, a privacy surface, and a point of failure. WOFF2 only — WOFF, TTF, and EOT fallbacks are dead weight.

**[Principle] Subset aggressively** and declare `unicode-range` per subset so the browser fetches only what the page needs. Latin body text should not be paying for Cyrillic.

**[Heuristic] Budget.** Roughly 100KB of font payload for a content site, more only with a reason. A four-weight two-family stack with no subsetting will blow this by several times over.

## Fallback and layout shift

**[Principle] Every `@font-face` needs metric-matched fallbacks.** The layout shift when a webfont replaces a fallback is caused by differing metrics, and it is fixable in CSS, not by hoping:

```css
@font-face {
  font-family: "Body Fallback";
  src: local("Arial");
  size-adjust: 107%;
  ascent-override: 90%;
  descent-override: 22%;
  line-gap-override: 0%;
}
```

Then list the real face first and the adjusted fallback second. **A font stack whose fallback shifts the page is a blocker**, not a polish item.

## Variable fonts

**[Principle] Prefer high-level properties over `font-variation-settings`.** `font-weight: 450` is animatable, inheritable, and interoperable; `font-variation-settings: "wght" 450` overrides the lot and breaks inheritance. Use the low-level property only for axes with no high-level equivalent.

Common axes: `wght` weight, `wdth` width, `opsz` optical size, `slnt` slant, `ital` italic, `GRAD` grade.

**[Principle] `font-optical-sizing: auto`** where the face has an `opsz` axis. This is the correct solution to the display-tracking problem in `FORMATTING.md` — the face adjusts its own contrast and spacing per size.

**[Heuristic] A variable font pays for itself past roughly three static weights.** Below that, static instances are usually smaller.

## Features

Prefer the high-level `font-variant-*` properties over `font-feature-settings`, for the same inheritance reason.

```css
:root { font-kerning: normal; font-variant-ligatures: common-ligatures; }
.tabular { font-variant-numeric: tabular-nums lining-nums; }
.prose   { font-variant-numeric: oldstyle-nums proportional-nums; }
code, pre { font-variant-ligatures: none; }
.smallcaps { font-variant-caps: small-caps; }
```

**[Principle] `font-synthesis: none`** on the root, or at minimum `font-synthesis-weight: none; font-synthesis-style: none; font-synthesis-small-caps: none`. This is what makes "no fake bold, italic, or small caps" enforceable rather than aspirational — without it the browser will happily invent them and nobody will notice in review.

## Sizing and measure

**[Principle] Size type in `rem`.** `px` on the root defeats the browser font-size setting. Pure `vw` defeats zoom and fails WCAG 1.4.4.

**[Principle] Fluid type uses `clamp()` with a `rem` middle term** so zoom still works: `font-size: clamp(1rem, 0.95rem + 0.25vw, 1.125rem)`. A `clamp()` whose middle term is viewport-only is the same failure as pure `vw`.

**[Principle] `line-height` unitless.** A unit'd line-height does not scale with inherited size and breaks every nested element.

**[Principle] `letter-spacing` in `em`,** never `px`, so tracking scales with size.

**[Heuristic] Measure in `ch`.** Note `ch` resolves against the computed font's `0` glyph, so verify the rendered measure after a font swap rather than trusting the number.

## Wrapping and breaking

- `text-wrap: balance` — headings and short blocks of a few lines. Has a line-count limit in browsers; not for body copy.
- `text-wrap: pretty` — body copy; addresses orphaned last words.
- `hyphens: auto` with a correct `lang` attribute — mandatory if justifying, useful in narrow columns. **The `lang` attribute is what makes hyphenation and locale-correct quotes work at all.**
- `overflow-wrap: anywhere` on user-generated content and URLs to prevent overflow.
- `hanging-punctuation: first last` where supported — small win, no cost.

## Verification

**[Principle] Render before judging.** Any claim about how type looks must be checked at narrow (~360px), medium (~768px), and wide (~1280px+) widths, with fonts loaded and with fonts blocked. See `ACCESSIBILITY.md` for the four required stress states.
