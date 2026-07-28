---
name: typeset-content
description: Correct typographic characters in prose — curly quotes and apostrophes, hyphens and en/em dashes, ellipses, non-breaking spaces, sentence spacing, symbols, foot and inch marks, ligatures, small caps. Runs in review mode (report only) or apply mode (explicit request). Use when asked to typeset, clean up, or check punctuation and characters in copy, Markdown, MDX, HTML, JSX text, or localization files. Never modifies code, URLs, identifiers, or program syntax.
---

# Typesetting Content

Character-level correctness in prose. Separated from the rest of the collection because **editing prose characters is a different risk surface from editing CSS**: a wrong curly quote inside a shell command is a broken command, and a "corrected" legal quotation is falsified evidence.

It does ONE thing: assess and correct typographic characters in text. It does not touch styling — asked about type size, measure, or hierarchy, decline and point to `practical-typography` or `review-typography`.

## Two modes

**Review mode (default).** Report findings. Never writes. This mode is safe to invoke whenever prose is being drafted or checked.

**Apply mode.** Writes changes to files. **Requires an explicit request** — "apply," "fix these," "run it." Never enter apply mode because review mode found something. Within apply mode, only `SAFE-AUTO` changes are applied silently; `CONTEXTUAL` changes are proposed as a diff and require confirmation; `NEVER-AUTO` findings are reported and left alone.

State which mode you are in, in the first line of output.

## Project register

Look for `TYPE-BRIEF.md` at the project root. This skill is the least affected by register — characters are correct or they are not — but a brief may declare house style that this skill must respect rather than flag: em dash spacing, ampersand usage, quote convention, locale. Where the brief declares one, enforce it consistently instead of reporting the split.

## References to load

Always: `COMPOSITION.md` (the rule catalog and the automation matrix), `REVIEW-RUBRIC.md` (finding schema).
As required: `FORMATTING.md` (small caps, figure sets), `WEB-PLATFORM.md` (the CSS side of ligatures, features, `lang`), `ACCESSIBILITY.md` (locale and script behaviour).

Independently invocable. This skill will run correctly in a repository where nothing else in the collection is installed.

## Hard rules

1. **Exclusion zones are absolute.** Never modify characters inside code blocks, inline code, `<pre>`/`<code>`, URLs, email addresses, file paths, identifiers, CLI examples, regular expressions, JSX/TSX attribute values, template-literal expressions, config keys and values, HTML attribute values, or front-matter keys. Full list in `COMPOSITION.md`.
2. **Parse, do not regex the document.** Operate on a parsed tree — Markdown/MDX AST, HTML DOM, JSX text nodes — and transform only text nodes. Running a regex across a whole file is how apostrophes end up inside `className`.
3. **Never modify program syntax.** Only the text content between tags and outside code.
4. **No locale, no locale-dependent change.** Quote characters, spacing before punctuation, and dash conventions vary by language. Without a declared locale (front matter, `lang`, file path, i18n key), quote-style changes are `NEVER-AUTO`.
5. **User-generated content is never modified.** Comments, reviews, submissions, transcripts.
6. **Quoted and legal text is never modified.** The source characters are the evidence.
7. **Every change is reversible and reviewable.** Apply mode emits a diff. Never a silent in-place rewrite of a whole file.
8. **The leading-apostrophe case is checked explicitly.** `'90s`, `'tis`, `'em`, `rock 'n' roll` take a closing apostrophe, not an opening quote. This is the most common failure of every naive smart-quote implementation, including most CMS ones — check it by name on every run.
9. **House style is reported, never imposed.** Em dash spacing, ampersand usage, exclamation density. Report inconsistency; do not pick the convention.

## Workflow

1. **Identify the format** — Markdown, MDX, HTML, JSX/TSX, plain text, or a localization resource — and parse accordingly.
2. **Determine the locale.** Front matter, `lang`, path segment, i18n key. If none, say so and downgrade all locale-dependent rules to `NEVER-AUTO`.
3. **Map exclusion zones** before scanning. Everything outside them is prose; everything inside is untouchable.
4. **Scan against `COMPOSITION.md`,** classifying each finding by severity and automation risk.
5. **Report,** in the output contract below.
6. **Apply only in apply mode,** `SAFE-AUTO` first, `CONTEXTUAL` as a confirmed diff.
7. **Confirm nothing broke** — rebuild or re-parse; for JSX and MDX, confirm the file still compiles.

`scripts/lint-composition.mjs` in this skill directory implements the deterministic `SAFE-AUTO` scan with exclusion-zone handling. Use it for volume; use judgement for everything it classifies as `CONTEXTUAL`.

## Output contract

Open with the mode, the files scanned, and the locale detected (or its absence).

Then the findings table, per `REVIEW-RUBRIC.md`:

| Severity | Auto | Location | Observed | Recommended | Why |
| --- | --- | --- | --- | --- | --- |

Then, in order:

- **Safe to apply** — count and one-line summary per rule.
- **Needs a decision** — `CONTEXTUAL` items, each with the specific question.
- **Report only** — `NEVER-AUTO` items and where they came from.
- **House-style inconsistencies** — with the observed split (e.g. "spaced en dash in 14 places, unspaced em dash in 9"), and no recommendation as to which wins.

In apply mode, close with the diff and the post-apply verification result.
