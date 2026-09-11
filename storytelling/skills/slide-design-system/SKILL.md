---
name: slide-design-system
description: DRAFT — Turns beats into slides under Benjamin's locked visual grammar (one idea per slide, FROM/TO contrast, monochrome-first, 1920×1080 grid) and reviews existing slides against it. Use when the user is building or critiquing slides, a deck, or a keynote, or asks how a slide should look, what goes on it, or whether a slide is doing any work.
---

# Slide Design System
<!-- scaffold: T2. LOW freedom for numeric values, medium for composition. References carry the research. -->

## Inherits
- philosophy.md principle "one idea at a time"; mayer-multimedia.md; data-ink-preattentive.md

## Locked values (verbatim, no interpretation)
- 1920×1080, render 2×; margins 120 side / 96 top+bottom → 1680×888
- Spacing scale 8/16/24/40/48/96/120
- Grids: A content 8-col · B phones 5×314 gap 40 · C tiles 5×5 352×198 gap 24
- Corners: tiles 8 · cards 16 · devices Apple squircle
- Type: hierarchy from size and tracking, not weight; core ramp names
- Colour: one dominant brand colour per slide; black/white carry surfaces

## Composition rules (each with its research why)
- One idea per slide → segmenting, cognitive load [R, Mayer/Sweller]
- FROM left / TO right contrast → contrast principle [T0]
- Never read the slide aloud; on-screen text is a headline, not a script → redundancy [R, Mayer]
- Labels next to what they label; visual appears when spoken → contiguity [R, Mayer]
- One dominant colour = signaling [R, Mayer]
- Chart title states the so-what [P, Knaflic]
- 3-second glance test [P, Duarte/Reynolds]
- One evolving visual language across a sequence, never a new metaphor per slide (Signal Geometry)

## Motion pointer
- Deck animation devices and grammar live in the existing bxn-deck-motion skill — link, don't duplicate

## Output format (required)
- Per slide: idea (one line) · FROM / TO · dominant element · what's on standby · grid used

## Review mode
- Same Line → Problem → Fix → Why table as review-narrative, scoped to visuals
