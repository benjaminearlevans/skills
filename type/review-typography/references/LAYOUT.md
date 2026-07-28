# Layout

How set text occupies the page: measure, paragraphs, blocks, lists, tables, and space.

## Measure and columns

**[Heuristic] 45–90 characters per line.** Below ~45 the eye returns too often and hyphenation gets ugly; above ~90 it loses the start of the next line. Express as `max-inline-size: 68ch` or equivalent — a fixed pixel width drifts off-measure the moment the face or size changes.

**[Principle] A reading column must be capped independently of its container.** The most common measure failure on the modern web is a prose block inheriting the width of a full-bleed layout section. Wide containers are fine; wide *text* is not.

**[Heuristic] Multiple columns rarely work on screen.** They require the reader to scroll up to continue, unless the column height fits the viewport. Reserve for print stylesheets and short blocks.

## Paragraphs

**[Principle] First-line indent OR space between paragraphs. Never both.** Both together is redundant — each is a complete signal that a paragraph has ended.

**[Heuristic] An indent runs one to four times the body size.** A paragraph space of roughly 0.5–1 line height reads well; a full blank line is usually too much.

**[Principle] No indent on the first paragraph** after a heading or a break. There is nothing to distinguish it from.

**[Principle] Do not centre paragraphs.** Centring destroys the consistent left edge the eye returns to. A centred heading, pull quote, or caption of one to three lines is fine. A centred paragraph is not.

**[Heuristic] Ragged-right is usually correct on the web.** Justification requires hyphenation to avoid rivers, and browser h&j is weak. If you do justify, `hyphens: auto` is mandatory and `text-wrap: pretty` helps. **[Principle] Justified text without hyphenation is a defect.**

## Blocks

**[Principle] A block quotation is distinguished by indentation and space, not by quotation marks, italics, or a smaller size** — and certainly not by all four. Long passages of italic are hard to read. Reducing the size implies the quoted material matters less.

**[Heuristic] Lists want a hanging indent** so the marker sits in the margin and the text edge stays aligned. Set the space between items to less than the space above and below the list, so the list reads as one object.

**[Principle] Tables: minimum rules, maximum alignment.** Space separates columns better than lines do. If rules are needed, hairlines and few. Numeric columns get tabular figures and right or decimal alignment. Header cells are `<th>` with a `scope`.

**[Principle] Rules and borders are a last resort.** Space is the primary separator; a rule is what you use when space has failed or is unavailable. A page with rules around every region reads as a form.

**[Heuristic] Control widows and orphans.** `orphans: 2; widows: 2` for paged media; on screen, `text-wrap: pretty` addresses the single-word last line. A one-word final line of a heading is the most visible case — fix it with a non-breaking space or `text-wrap: balance`.

## Space

**[Principle] Work outward from the text, not inward from the edges.** Set the body, derive spacing from its line height, and let the margins be what remains.

**[Principle] Space above binds less than space below separates.** A heading belongs to the text beneath it. Its space above should exceed its space below, or it will appear to belong to the preceding section.

**[Heuristic] Derive the spacing scale from the body line height** so vertical rhythm holds without needing a strict baseline grid. A separate spacing scale invented independently of the type scale is how systems drift.

**[Principle] Grids constrain, they do not decide.** A grid organises the relationship between elements. It does not tell you what the elements should be.

**[Principle] Foreground and background.** Decide which elements are the subject. Navigation, chrome, badges, and decoration are background and must not out-shout the body.

**[Principle] Every card must not invent its own hierarchy.** Repeated components are where consistency is won or lost — see `ANTI-SLOP.md`.
