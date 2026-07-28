# Extraction

How to turn a reference into properties. A brief that cites references without extracting from them has done nothing — the whole value is in the numbers.

## What to extract, in priority order

1. **Display-to-body ratio** — largest display size ÷ body size. The single number that most defines a register. Editorial sits around 2–3×; Display-led runs 4–8× or beyond.
2. **Body block** — computed `font-size`, computed `line-height` as a unitless value, and rendered measure in characters. Count the characters on a full line; do not trust the CSS value.
3. **Families and their roles** — how many, and what each one does. One family carrying everything is a decision worth capturing.
4. **Scale steps** — the sizes actually in use, and whether they follow a ratio or were chosen individually.
5. **Weights in use** — count them. Three is a system; six is an accumulation.
6. **Display tracking** — `letter-spacing` at the largest sizes, in `em`. Also whether an `opsz` axis is doing the work.
7. **Text colours** — count the distinct values used for text. Note any that sit within a few percent of each other.
8. **Figure treatment** — tabular or proportional, lining or oldstyle, and where each appears.
9. **Paragraph separation, rag treatment, and `text-wrap`** usage.

## From a live URL

Measure it. Do not describe it from memory, and do not infer it from a screenshot when the page is reachable.

With browser control available, on a representative content page:

```js
const el = document.querySelector("article p, main p, p");
const cs = getComputedStyle(el);
({
  family: cs.fontFamily,
  size: cs.fontSize,
  lineHeight: (parseFloat(cs.lineHeight) / parseFloat(cs.fontSize)).toFixed(2),
  measurePx: el.getBoundingClientRect().width,
  colour: cs.color,
  tracking: cs.letterSpacing,
});
```

Then the display end, and the set of everything in between:

```js
[...document.querySelectorAll("h1,h2,h3,h4,h5,h6")].map((h) => {
  const c = getComputedStyle(h);
  return `${h.tagName} ${c.fontSize} / ${c.fontWeight} / ${c.letterSpacing}`;
});

[...new Set([...document.querySelectorAll("*")]
  .map((n) => getComputedStyle(n).fontSize))].sort(
  (a, b) => parseFloat(a) - parseFloat(b));
```

Measure in characters rather than pixels: divide the rendered text width by the width of `0` in the computed font, or set a `ch`-width probe and compare.

Check the loaded fonts and the axes available:

```js
[...document.fonts].map((f) => `${f.family} ${f.weight} ${f.style}`);
```

## From a screenshot or a printed reference

Pixel measurement is unreliable and relative measurement is not. Extract **ratios**, which survive scaling:

- cap height of the display line ÷ cap height of the body line
- measure, counted in characters directly off the image
- number of distinct sizes, weights, and text colours visible
- whether hierarchy is carried by size, weight, position, or colour

State clearly in the brief that these are estimated from an image.

## From Figma

Read the text styles and the variables rather than measuring frames. Capture the named scale, the line-height values, the families and weights, and whether the styles are actually applied or the frame was hand-set — a design system that exists as styles nobody uses is a finding worth reporting back.

## From a specimen or a book

The useful extraction is not measurements but **relationships and intent**: what the display does that the text does not, how much space surrounds the text block, whether hierarchy is achieved by size or by space, and what the setting refuses to do. Record these as constraints in the brief's Obligations section rather than as numbers.

## Recording

Every extracted row carries its source and its method. Measured, estimated from an image, or read from a design file — the three are not equally reliable, and a reviewer enforcing the brief needs to know which it is.

## The judgement

Extraction tells you what a reference *does*. It does not tell you whether it will work here. A display-to-body ratio of 7 on a site with four words of copy will not transfer to a site with four thousand. **Say so in the brief when a reference is being partially adopted, and record which part.**
