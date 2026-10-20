---
name: xlt-board
description: Builds the pre-placed FigJam board for the XLT local vs shared tooling session from board-manifest.json — cluster sections with outcomes, draft requirements, needs, tools and barriers as color-coded stickies, a needs-an-outcome lane, a legend and an empty sorting grid. Use when the user types /xlt-board, asks to build or rebuild the XLT board, or has a reviewed board-manifest.json ready.
---

# XLT Board

Build the board people walk in to. Everything is pre-placed, so the room redlines rather than sorts from scratch.

## Inputs
- **`board-manifest.json`** from `xlt-synthesize`, after Ben and Patrick's review. Read `references/board-manifest.md` (in `xlt-synthesize`) if you need the schema.
- **A FigJam file URL.** Ask for it if it isn't given. Parse the `fileKey` from `figma.com/board/<fileKey>/…`.

## Before building
1. Load the Figma skills `figma-use` and `figma-use-figjam`. They're required before any `use_figma` call.
2. Confirm the Figma connection works: call `whoami`.
3. If the board already has an `XLT —` frame from an earlier run, ask before replacing it. Prefer building a new page called `XLT board v<n>`, so earlier versions are never overwritten.

## Layout

All positions are relative to the board's top-left origin.

**1. Legend**
A strip across the top: one sticky per color, plus a line explaining the dashed border and the ⚑ mark.

**2. Cluster sections**
- One FigJam **section** per cluster, laid out left to right in manifest order, with 200px gutters. Wrap to a new band after 4 sections.
- Section title: `<title>`. Subtitle: `<subtitle>`, in a text node at the top of the section.
- Inside each section, rows stack from the top, in this order: outcomes (green) → requirements (orange) → needs (yellow) → tools (blue) → barriers (pink). Shared asks go in the needs row.
- Each row is a grid of stickies, up to 5 per line, with 24px spacing. Give each row a small text label at its start.
- Sticky size is FigJam's default square. Keep it consistent.

**3. Needs-an-outcome lane**
Placed beneath the cluster bands. Needs, with dashed borders where supported, otherwise a "No outcome yet" tag line.

**4. Parking lot**
Placed beside the lane.

**5. Sorting grid**
Placed beneath everything else:
- a large section with two axis connectors and four labeled quadrants:
  - common + XD-wide source of truth → XD-wide
  - common + one team's product → XD standards, local implementation
  - one team + one team's product → Local only
  - one team + XD-wide source of truth → Watch
- axis labels taken from the manifest
- left empty for the room

## Sticky content
- **Text:** the sticky's `text`, with ⚑ in front if it's contested.
- **Second line:** the sticky's `tag`, e.g. `Premium · R1`.
- **Color:** from the manifest. Gray overrides the type color for `exists_not_adopted`.
- **Author name:** turned off where the API allows, so stickies don't show the builder's name.

## Building
- **Work in batches** of about 50 stickies per `use_figma` call, one section at a time, so a failure loses little.
- **After each section:** take a screenshot to check for overlap, then continue.
- **Log as you go:** write each placed ID to `board-log.md` (section, sticky IDs, any failures).
- **When done:** do one last screenshot of the full board, and check that every manifest sticky appears exactly once.

## Fallback (no Figma connection)
Write `board-stickies.csv` with the columns `section,row,order,color,text,tag`, plus a short `board-layout.md` describing the layout above. Someone can then import the stickies with a FigJam CSV-to-sticky plugin and arrange the sections by hand.

## Signs it's working
- Each lead can find their team's stickies in under a minute, by tag.
- No overlap between stickies or sections.
- Sticky count on the board equals sticky count in the manifest.
