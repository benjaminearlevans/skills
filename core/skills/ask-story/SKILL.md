---
name: "ask-story"
description: "Finds the through line in a pile of notes, thoughts and documents and turns it into a finished piece for a named audience. Asks its questions first, designs a workflow for the ask, then runs it: read the pile against questions, cluster from the evidence up, reduce to one governing idea and its pillars, build the storyline, write the brief, memo, executive summary or deck outline, and audit it. Coordinates the StrategyU skills with affinity-mapper and the strategy and exec-comms skills, in sequence, in parallel or through specialist sub-agents. Use when the user types /ask-story, or has scattered material and wants the thread, the story, the narrative, the pillars or the themes, or wants an argument told to an audience. Building or stress-testing a strategy belongs to ask-strategy. Product, growth and career questions belong to ask-pm."
---

# Ask Story

Takes scattered material and returns one idea, the few pillars that hold it up, and a finished piece that tells it to a named audience.

This file designs and coordinates the workflow. The loaded skills carry the method, so a stage run from this file alone is a guess. The skills were written separately and each expects to be used alone, which is why three of them ask the same audience questions and two of them disagree about when to start. The work of this skill is to make them behave as one process.

## Run this every time

1. **Read before asking.** Skim everything attached or pointed at: titles, dates, headings, first paragraphs. Count the documents. Questions written without this are generic, and generic questions get generic answers.
2. **Ask once, before any stage runs.** Even when the ask looks clear.
   - Choose from "Questions that shape the workflow" the three or four whose answers change which stages run, which skill runs them, or who decides.
   - Always include the audience questions when a piece will be written. `su-storyline`, `su-writing` and `su-coach` each ask their own five audience questions. Ask them here, once, and the user is never asked twice.
   - Drop anything the ask or the material already answers. If fewer than two questions remain, ask the two with the highest stakes as a check on your reading.
   - For a multiple-choice question, explain each option before asking: what it leads to, what it gains, what it costs. Two sentences an option. Use the session's question tool when it has one.
   - Keep the whole reply short: two lines on what the skim found, then the questions. Aim for 300 words.
   - One round, then wait. A second round only when an answer opens a fork that could not be foreseen.
   - If nobody can answer (an unattended run), write the assumed answers at the top of `workflow.md` and carry on to the first checkpoint.
3. **Write the audience card.** Save the answers as `audience.md`: reader, stance, decision wanted, time they will give it, what they care about, constraints. Every later stage reads this file instead of asking.
4. **Design the workflow.** Pick the nearest recipe below and adapt it to the answers. Write `workflow.md` as described under "The workflow file". Tell the user the route in six lines or fewer, then start. Do not wait for approval of the route.
5. **Run the stages.** Load each skill with the Skill tool before using it. Names vary between sessions: a skill may be listed bare (`affinity-mapper`), behind its bundle (`strategyu-skills:su-structure`), or under a shortened name. Match on the skill's name and call it exactly as this session lists it. When a loaded skill tells you to ask the user about the audience, take the answer from `audience.md`. Re-read `workflow.md` after every skill load and every checkpoint: a loaded skill brings its own ending, and the workflow is how you find the way back.
6. **Stop at the two checkpoints.** The governing idea and the pillars are the user's to choose. Nothing is drafted on an idea the user has not chosen.
   - These are the only planned stops. After checkpoint B, run every remaining stage in `workflow.md` without pausing. Showing the storyline and waiting for a reaction is a stall, not a checkpoint.
7. **Audit with fresh eyes, then deliver.** Conclusion first. A long piece goes in a document with a few lines in chat. Never overwrite an earlier version: write a new one beside it. End with a line starting `Skills used:` and, when anything was skipped or missing, a line starting `Not done:`.

## Questions that shape the workflow

Each line says what the answer decides.

- **What is the piece, and who is it for?** Through-line note, email, memo, executive summary, one-page brief, deck outline or talk. Decides where the workflow ends and the stage 5 skill.
- **Where does the reader stand, and what do you want from them?** Supportive, neutral, sceptical or opposed. Approve, choose, delay or stay informed. Decides the order the story is told in.
- **How long will they give it, and what do they care about most?** Skim, read or study. Cost, speed, risk, team, reputation. Decides length and what leads.
- **What question must the material answer?** If the user can state it, stage 0 is skipped. If not, stage 0 finds it.
- **Is there already an idea you believe, or should the material decide?** Decides whether stage 3 tests one idea or builds rivals.
- **How strict is the evidence?** Every claim traceable to a named document with a quote, or judgement allowed. Default when unanswered: traceable.
- **What is settled, off-limits or already decided?** So the story does not reopen it.
- **How deep?** A single pass by one agent, or the full workflow with specialists, rival ideas and an independent audit. Decides the agent setup.

## Stage map

Each stage reads the files before it and writes one file. Run only the stages the workflow names.

**Stage 0. Frame the question.** Output: the key question and three to five sub-questions, at the top of `ledger.md`.
- `strategyu-skills:su-frame`. Use its situation, complication, question and answer structure to state the question the pile must answer.
- This skill gives a first pass and asks in the same reply. The asking is already done, so take its first pass and move on.

**Stage 1. Read the pile.** Output: `ledger.md`. One row per finding, each with an id (L1, L2), the document, an exact quote and the sub-question it answers.
- `brief-from-pile` when listed. Otherwise the pile rules.
- `execution-skills:meeting-synthesis` for transcripts and meeting notes.
- Pile rules: map every document first (what it is, date, author, likely contribution). Read deeply where a sub-question is answered and skim elsewhere. When documents disagree, prefer the more recent, then the more authoritative, and otherwise record the conflict as a finding. End the ledger with what was skimmed, skipped and missing.

**Stage 2. Cluster from the evidence up.** Output: `clusters.md`.
- `affinity-mapper`. It works wide: many clusters, outliers kept, tensions between clusters named.
- Trust test, because the installed mapper has none: split the two largest clusters and sort their rows again. Flag a cluster that does not re-form, and any cluster that rests on one document.

**Stage 3. Reduce to one idea.** Output: `pyramid.md`. Main idea, the insight under it for each group, the ledger ids under each insight.
- `strategyu-skills:su-structure`. It works narrow: cut what does not serve the question, label, sort the clusters into a few groups that do not overlap, write one insight per group, then the main idea, then check the grouping.
- Stages 2 and 3 are one movement. The mapper keeps everything so nothing is lost early. The structure skill then cuts, so the story is not a list.
- Aim for three groups. Keep two or four when forcing three would merge unlike things or split one thing.
- When the user has no idea in mind, or asks for options, build two or three rival pyramids from the same clusters, each sorted on a different principle.
- For an existing draft, `minto-pyramid` when listed: its buried-lede test names the conclusion the draft is building toward.
- **Checkpoint A, governing idea.** Show each candidate as one sentence, the groups it explains, the ledger rows it leaves out, and the strongest thing against it. The user picks or rewrites. If the material supports no single idea, say so and show what is missing.
- Test the pillars under the chosen idea: they are the same kind of idea, they do not overlap, together they carry the idea, and each rests on more than one document.
- When the idea is a strategic choice (what to do, what to stop, where to compete), hand `pyramid.md` and `ledger.md` to `ask-strategy` to build and stress-test it, and take back its strategy before stage 4.
- **Checkpoint B, pillars.** The user confirms or edits them.

**Stage 4. Build the storyline.** Output: `storyline.md`. The sequence, as titles that each state a point.
- `strategyu-skills:su-storyline`. Choose its sequencing approach from the reader's stance in `audience.md`: answer first for a supportive reader, the reasoning first for a sceptical or opposed one.
- `awesome-pm-skills:exec-comms`, persuasive play, when the piece must move a room toward a change.
- `awesome-pm-skills:position` when the story faces outward, to customers or the market.
- Check: read the titles alone, in order. They must tell the whole story.

**Stage 5. Write the piece.** Output: the piece, named for what it is (`brief.md`, `memo.md`).
- Email, memo, executive summary: `strategyu-skills:su-storyline` writes it.
- One-page brief: `minto-pyramid` when listed, otherwise `strategyu-skills:su-storyline`.
- Deck: `strategyu-skills:su-storyline` with its `references/slides.md`. Deliver the outline. Build slides only when asked.
- A memo that exists to get one decision: `awesome-pm-skills:decide`.
- Then `strategyu-skills:su-writing` as a check: it flags, you fix. Where its pattern list conflicts with the user's own stated writing habits, the user's habits win.
- Every factual sentence carries its ledger id while drafting. Strip the ids from the delivered piece unless the user asked for traceable evidence, in which case keep them as footnotes.

**Stage 6. Audit.** Output: `audit.md`. Three checks, run by agents that did not write the piece.
- Cold read: an agent that sees only the piece states its point in one sentence. If that sentence is not the governing idea, the piece has failed, whatever else is right.
- Fact check: every claim against the ledger. Unsupported claims are cut or marked.
- Structure check: the grouping rules in `strategyu-skills:su-structure`, applied to the finished piece.
- With no sub-agents, do all three yourself and label the result "self-audited".

**Stage 7. Prepare the room.** Only when the user asked for it or confirmed it in the questions. A meeting on the calendar is not a request. The exec-review play in `awesome-pm-skills:exec-comms`: the ten hardest questions, three facts, a sixty-second opener.

**Stage 8. File.** `file-and-name`, when listed.

Do not load `strategyu-skills:su-coach` beside the others. It holds the same four methods in one file and will pull the workflow back into a single conversation. Use it only when the other four are missing.

## The workflow file

`workflow.md` is the plan and the record. Write it before stage 0 and update it as stages finish. Keep it to one page.

- One line per stage: number, purpose, skill, input files, output file, who runs it, and what it waits for.
- Mark which stages run in parallel and where the checkpoints fall.
- State the agent setup in one line: "one agent", or the specialists by name.
- Tick each stage when its output file exists. Record a skipped stage with its reason.
- Working files are notes for the next stage, not deliverables. A ledger row is one line and its quote. The audit lists what it found, not what it checked.

A workflow worth keeping becomes a recipe. When the user asks, or when the same adapted workflow has run twice, save it as `recipe-<name>.md` beside the outputs and say where it is. A recipe used three times is a candidate for its own skill. Say so once.

## Recipes

Starting points. Adapt them to the answers, dropping any stage whose output already exists.

- **Pile to through line.** 0, 1, 2, 3. Stop after checkpoint B with a one-page note: the idea, the pillars, the evidence under each.
- **Pile to piece.** 0 to 6, with 7 if a meeting follows.
- **Draft to landing.** Skip 0 to 2. Run the buried-lede test or stage 3 on the draft, then 4, 5, 6.
- **Idea in search of evidence.** The user states the idea. Run 1 and 2 looking for what supports it and what contradicts it, then 3 as a test of that one idea.
- **Rival stories.** 0, 1, 2, then three rival pyramids in parallel, then checkpoint A.
- **Strategy story.** 0 to 3, hand to `ask-strategy`, then 4 to 6 on what comes back.

## Sequence and parallel

- **In sequence** wherever a stage reads the file before it: 0, 1, 2, 3, 4, 5.
- **In parallel** wherever the pieces are independent:
  - reading separate groups of documents in stage 1
  - rival pyramids in stage 3
  - the three audit checks in stage 6
  - room preparation alongside the writing, once the storyline is fixed
- Never run in parallel two steps that write the same file. Parallel readers write `ledger-a.md`, `ledger-b.md`, and the orchestrator merges them and assigns the ids.

## Specialists

Spawn sub-agents only when the session has a tool for it and at least one of these holds: the pile has more than eight documents, the user chose the full workflow, rival ideas are wanted, or the audit must be independent of the writer. Otherwise run the stages yourself and write "one agent" in the workflow. Run at most four at once.

- **Reader**, one per group of documents. Stage 1.
- **Mapper.** Stage 2, with the trust test.
- **Structurer**, one per rival pyramid. Stage 3.
- **Storyliner.** Stage 4.
- **Writer.** Stage 5, then the writing check.
- **Cold reader.** Receives only the finished piece.
- **Fact-checker.** Receives the piece and the ledger.

A specialist starts with no memory of this conversation, so its brief carries everything:

- the goal in one sentence, and the full text of `audience.md`
- the exact skill names to load with the Skill tool, and the instruction to take audience answers from the brief, not from the user
- the input files by path, and the one file it must write
- the report to return: ten lines at most, with the file path, the main result and any open questions
- the rules: add no fact that is not in the ledger, quote exactly, ask the user nothing, contact nobody, spawn no further agents

The orchestrator keeps the conversation with the user and both checkpoints. It merges the specialists' files, settles disagreements between them by the evidence in the ledger, and brings any it cannot settle to the user.

## Working with the other orchestrators

- **To `ask-strategy`:** when the governing idea is a choice that must be built into a strategy or stress-tested. Send `pyramid.md`, `ledger.md` and `audience.md`. You started the run, so you finish it: when `strategy.md` comes back, carry on at stage 4. If the strategy stages do not run, say so on the `Not done:` line and do not present the pillars as a tested strategy.
- **From `ask-strategy`:** it runs the whole job and you are one of its stages. Run only the stages it names: 0 to 3 for a pile, 4 to 6 for the telling.
  - Ask only what its routing questions left open, keep checkpoints A and B, and write your files.
  - State no route of your own and give no final reply. For a pile, stop after checkpoint B and build no storyline.
  - Then go on to `ask-strategy`'s next stage in the same turn.
- **To `ask-pm`:** a product, growth, hiring or career question that comes up inside the story. Bring the answer back.

## Limits

- **A missing skill is named and its fallback used.** `brief-from-pile` and `minto-pyramid` are preferred when listed and have fallbacks above. Anything else missing goes on the `Not done:` line.
- **Facts come from the user's material.** Quotes are copied exactly, with the document named. Nothing is added that the ledger does not hold, including sums worked out from its numbers.
- **The idea follows the evidence.** When the ledger contradicts an idea the user favours, show the rows that contradict it at checkpoint A.
- **Speak as the assistant.** Do not write as a named author, consultant or guest.
- **The user's standing format and writing preferences win** over any skill's template or pattern list.

## Before delivering

Check these and fix what fails:

- the questions were asked once, before any stage ran, and `audience.md` exists
- `workflow.md` lists every stage that ran, with its skill and its output file, and every stage that did not run is on the `Not done:` line with the reason
- the piece named in the answers exists as a file; a through-line note or a storyline is not the piece unless that is what the user asked for
- when the user asked for a strategy, `strategy.md` and its audit exist, or the `Not done:` line says the strategy was not built or tested
- if the user chose the full workflow and no specialist ran, the `Not done:` line says why
- the governing idea and the pillars were chosen by the user, or are marked "proposed, not confirmed"
- every factual claim in the piece maps to a ledger row, and every quote is exact
- the cold reader's one sentence matches the governing idea
- every skill on the `Skills used:` line was loaded in this session
- the conclusion is the first line, and no earlier version was overwritten

## Worked routes

These double as the checks for this skill. Run them after any change to it.

**Questions first.** "/ask-story here are nine documents from the offsite, I need to tell leadership what we learned." Before any stage runs, the reply names what it found in the pile, then asks who decides and where they stand, whether an idea is already in mind, and how strict the evidence is, each with its options explained. Without this skill the same prompt tends to produce a summary at once, which is the difference to look for.

**Pile to checkpoint.** With the answers given and nobody present, the run writes `audience.md`, `workflow.md`, a ledger with quotes, clusters and two or three rival ideas, then stops at checkpoint A with nothing drafted.

**Not this skill.** "Is our strategy any good?" asks for a judgement on the strategy, not for its story. It belongs to `ask-strategy`.

## Upkeep

Internal skill, written for the skills installed alongside it. When skills are added, removed or renamed, check every name in the stage map against the installed list. Re-check the trust test in stage 2 if `affinity-mapper` is replaced, and the note on `su-coach` if the StrategyU set changes.