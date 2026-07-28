# Registers

A **register** is the typographic intent of a project: what its type is optimising for. It is declared in a project's `TYPE-BRIEF.md` and read by every skill in this collection.

A register does not relax review. **It re-targets it.** Each register buys latitude on some axes and pays for it with stricter scrutiny on others, because each has a characteristic way of failing. Declaring "Display-led" does not silence the huge-headings finding — it converts it from a prohibition into an accepted risk, and the risk is then audited.

## What a register can and cannot do

**Can override:** `[Heuristic]` ranges in `FOUNDATIONS.md`, and named patterns in `ANTI-SLOP.md`.

**Cannot override, ever:** anything tagged `[Principle]`, and everything in `ACCESSIBILITY.md`. No register excuses failing 200% enlargement, 320px reflow, text-spacing override, contrast thresholds, semantic heading order, or a synthesised typeface. A Big Type site that clips at 200% is broken, not bold.

**Adds obligations:** whatever the brief declares, the implementation is now checked against it. A brief that says "one family, weight-based hierarchy" makes the second family on the pricing page a finding that would not otherwise exist.

## The registers

### 1. Editorial

*Reading is the product.* Essays, long-form, publications, documentation-adjacent prose.

Typical: scale ratio 1.2–1.333 · body 17–20px · leading 1.55–1.7 · measure 60–75ch · true italic mandatory · oldstyle figures in prose · one or two families.

Stricter on: measure discipline, leading at the measure used, rag quality, widow and orphan control, italic quality, paragraph separation consistency.

Latitude: none needed — this register sits closest to the catalog defaults.

Failure mode: precious and slow. Hierarchy so gentle that scanning is impossible. Everything the same size.

### 2. Display-led (Big Type)

*The headline is the design.* Agency sites, fashion, film and title-treatment homages, portfolios, campaign pages.

Typical: scale ratio 1.5–2.0, with display steps often jumping outside any ratio · display tracking −0.02 to −0.04em, or an `opsz` axis · frequently one family carrying everything · heavy weight contrast · body **still 16–19px**.

Stricter on: **the body block, specifically.** This register's failure is measured at the bottom of the scale, not the top. Also: display tracking and optical sizing; measure at display size (a 96px headline running 90 characters is unreadable); wrapping and reflow at 320px, where oversized type breaks first; whether the display-to-body relationship is systematic or arbitrary per page.

Latitude: `ANTI-SLOP#huge-headings` is suspended **only** if the body block independently passes. Large scale ratios permitted. Non-ratio display steps permitted where declared.

Failure mode: exactly the pattern it is licensed to break — oversized headings sitting on body text that was never designed. Also catastrophic narrow-viewport breakage.

### 3. Dense utility

*Information density is the product.* Dashboards, admin tools, data tables, trading and monitoring interfaces.

Typical: body 13–15px legitimately · leading 1.35–1.5 · compact scale 1.125–1.2 · tabular lining figures mandatory · short measures · two weights.

Stricter on: contrast ratios, because small text has no margin — 4.5:1 is a floor, not a target; tabular figures in every numeric column; numeric alignment; **200% enlargement and 320px reflow, which dense layouts fail before anything else**; whether small sizes are load-bearing or merely inherited.

Latitude: `FOUNDATIONS#body-size` lower bound relaxes to 13px for data surfaces. Tighter leading permitted.

Failure mode: the bottom of the size range is illegible for anyone over forty; the layout collapses under enlargement.

### 4. Technical

*Scannability across deep hierarchy.* Developer docs, API references, technical writing.

Typical: monospace as a first-class family, not an accent · four to six genuinely distinguishable heading levels · body 16–18px · measure 65–80ch for prose, unconstrained for code · ligatures off in code.

Stricter on: heading semantics and level integrity — no skipped levels, no headings chosen for size; whether levels five and six are actually distinguishable; inline code treatment against surrounding prose; code block typography; prose measure held independently of code measure.

Latitude: more hierarchy levels than the catalog would otherwise encourage.

Failure mode: six heading levels that read as four. Inline code that disrupts the line.

### 5. Systematic

*Restraint as the position.* Swiss-influenced, grid-driven, deliberately neutral.

Typical: one family · hierarchy from weight and position rather than size · compact scale 1.125–1.2 · strict grid · minimal colour.

Stricter on: consistency, which is the entire proposition — a single inconsistency costs more here than in any other register; grid adherence; whether the weight-based hierarchy actually functions at reading distance; whether "neutral" has become "undifferentiated."

Latitude: unusually small size contrast between levels permitted.

Failure mode: hierarchy too subtle to work. Cold to the point of unreadable intent.

### 6. Expressive

*Voice forward.* Brand and campaign sites, launches, personality-led marketing.

Typical: a display face permitted in display roles · a text face required for anything read at length · more licence for effects, colour, and case play · often two or three families.

Stricter on: **the boundary.** Where does expression stop and reading begin? Effects — gradient text, outlines, shadows, extreme tracking — may not touch any surface read at length. The body face must be a text face. Every expressive element is checked for whether it survives translation and enlargement.

Latitude: `ANTI-SLOP#gradient-text` and display-face usage permitted **in declared display roles only**.

Failure mode: effects bleeding into reading surfaces. A display face doing body work.

### 7. Custom

No preset fits. The brief must then supply, explicitly: what the type is optimising for, which heuristics are overridden and why, which failure modes are being accepted, and at least one extracted reference. A Custom register with none of these is not a register — it is the absence of a decision, and skills should say so.

## Precedence

Highest to lowest. Each level only overrides the one below it.

1. `[Principle]` rules and `ACCESSIBILITY.md` — absolute, never overridable.
2. A **declared override in `TYPE-BRIEF.md` carrying a stated reason** — overrides `[Heuristic]` ranges and named `ANTI-SLOP.md` patterns, and activates the register's substitute checks.
3. Register preset defaults from this file.
4. Catalog defaults.

**An override without a stated reason is not an override.** Note it, apply the default, and report the missing reason as a finding against the brief.
