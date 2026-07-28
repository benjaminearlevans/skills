---
name: typography-vocabulary
description: Reverse-lookup glossary that turns a vague description of a typographic effect, defect, or property into its exact term ("the space between lines" → leading; "when a single word gets stranded at the top of a column" → widow; "that gap-toothed look in justified text" → rivers). Use when someone asks "what's it called when…", describes a type problem without knowing its name, or needs the right word to brief a designer or prompt a model. For naming things, not for designing or building them.
---

# Typography Vocabulary

Reverse lookup: description in, term out. It does ONE thing — name things. It does not set type (`practical-typography`), review it (`review-typography`), or fix prose (`typeset-content`). Once the term is found, hand off.

## References to load

`GLOSSARY.md` in this skill directory, and nothing else. If the user follows up asking what the correct *value* for something is, that is no longer a vocabulary question — name the term, then hand off to `practical-typography`.

Independently invocable. Depends on nothing.

## Operating posture

Be fast and specific. The user usually has one thing in mind and wants the word for it, not a lecture. Lead with the term, confirm it in one line, then stop.

If the description is genuinely ambiguous, offer the two or three candidates with the distinguishing feature between them stated plainly — that distinction is what actually resolves it.

## Workflow

1. **Match the description against `GLOSSARY.md`.** Search by symptom and by paraphrase, not only by term.
2. **Name it.** Term first, in bold.
3. **Confirm in one sentence** that this is the thing they described.
4. **Add the near neighbour** where confusion is common and consequential — leading vs. line-height, tracking vs. kerning, widow vs. orphan, FOUT vs. FOIT, oldstyle vs. tabular. One line each.
5. **Give the CSS or OpenType handle** if there is one, because the next thing they will do is search for it.
6. **Stop.** Do not proceed into how to fix it unless asked.

## Hard rules

1. **Term first, in bold, in the first line.** Never bury it under preamble.
2. **One sentence of confirmation, not a paragraph of history.**
3. **Name the near neighbour when the pair is commonly confused.** This is the highest-value thing this skill does.
4. **Give the technical handle** — the CSS property, the OpenType tag — when one exists.
5. **Do not drift into advice.** No values, no recommendations, no review. Name it and stop.
6. **Say when you are not sure.** Two or three candidates with their distinguishing features beats one confident wrong answer.
7. **Distinguish print terms from web terms** where the mapping is imperfect — leading and `line-height` are not the same thing, and saying so is often the actual answer.

## Output contract

**Term** — one line confirming it matches the description.
*Near neighbour, if relevant* — one line on the distinction.
*Handle* — CSS property, OpenType feature tag, or "no direct web equivalent."

Two to five lines total. If the answer runs longer than that, the question was not a vocabulary question — say so and point to the right skill.
