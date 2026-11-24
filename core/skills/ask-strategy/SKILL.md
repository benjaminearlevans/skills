---
name: "ask-strategy"
description: "Orchestrates the building and stress-testing of a strategy: frames the problem, names the crux, makes the choices, sets the pillars as things to do and things to stop, and audits the result before it is told. Always asks its routing questions first, then triages to the right installed skill or chain of skills, runs stages in sequence or in parallel, and spawns specialist sub-agents when the work divides. Hands the reading of a pile and the telling of the story to ask-story. Use when the user types /ask-strategy, or asks to write, build, choose, review, grade or stress-test a strategy, a strategy memo or a set of strategic pillars. Finding a through line in scattered material, or writing the brief that tells a settled strategy, belongs to ask-story. Product, growth, hiring and career questions with no strategy in view belong to ask-pm."
---

# Ask Strategy

Takes a strategy ask and runs it as a workflow: frame the problem, make the choices, test them hard, and hand a strategy that holds to the telling.

This file routes and coordinates. The loaded skills carry the method, so a stage run from this file alone is a guess. Reading a pile of documents and writing the finished piece belong to `ask-story`. This skill owns what sits between them: the strategy itself.

## Run this every time

1. **Read before asking.** Read the ask and skim everything attached or pointed at. The questions must be about this ask, not a generic intake form.
2. **Ask before routing. Always.** Do not route, load a skill or spawn anything first, even when the ask looks clear.
   - Pick from "Questions that change the route" the three or four whose answers would change which stages run, in what order, with which skill, or who decides.
   - Drop any question the ask or the material already answers. If fewer than two remain, ask the two with the highest stakes as a check on your reading.
   - For a multiple-choice question, give each option a short paragraph first: what it leads to, what it gains, what it costs. Keep each to two sentences. Use the session's question tool when it has one.
   - One round, then wait. A second round only when an answer opens a fork that could not be foreseen.
   - If nobody can answer (an unattended run), write the assumed answers at the top of the work and carry on to the first checkpoint.
3. **State the route in five lines or fewer:** the stages that will run and the ones skipped, the skill for each, what runs in parallel, the agent setup (one agent, or which specialists), and where the user decides. Then start. Do not wait for approval of the route.
   - Save the same lines as `route.md`, one line per stage with its output file. Tick a stage when its file exists.
   - Re-read `route.md` after every skill load and every checkpoint. A loaded skill brings its own instructions and its own ending, and the route is how you find the way back.
4. **Run the stages** from the stage map. Load each skill with the Skill tool before using it. Names vary between sessions: a skill may be listed bare (`affinity-mapper`), behind its bundle (`awesome-pm-skills:strategy`), or under a shortened name. Match on the skill's name and call it exactly as this session lists it.
   - You own the run from the first question to the delivered piece. Calling `ask-story` is a stage, not a hand-over: when its files exist, go on to the next stage on the route in the same turn.
5. **Stop at the checkpoint.** The diagnosis and the choices are the user's to make. Do not build actions on a diagnosis the user has not confirmed.
   - The only planned stops are this checkpoint and, when `ask-story` reads a pile, its two checkpoints. Between and after them, keep going: a finished stage is a reason to start the next one, not to report.
6. **Audit with fresh eyes before delivering.** The audit is run by an agent that did not write the strategy. With no sub-agents, re-read as a hostile reviewer and label the result "self-audited".
7. **Deliver.** Conclusion first. A long artefact goes in a document, with a few lines in chat. Never overwrite an earlier version: write a new one beside it. End with one line starting `Skills used:` and, when anything was skipped or missing, one line starting `Not done:`.

## Questions that change the route

Each line says what the answer decides. Ask only the ones that matter for this ask.

- **What kind of strategy is it?** Product or market (compete, win customers), internal (operating model, tooling, organisation, AI adoption), or a set of AI bets. Decides the plays in stage 2. Internal strategies skip the moat tests.
- **Where are you starting from?** A pile of notes and documents, a through line already found, an existing strategy to review, or nothing. Decides whether `ask-story` runs first and which stages follow.
- **Is the problem agreed?** If people disagree about what the problem is, stage 1 runs in full. If it is agreed, stage 1 is a check.
- **Which choices are open, and which are already made?** Decides what the strategy may change and what it must take as given.
- **Who decides, and what do you need from them?** Approve, fund, choose between options. Decides whether `decide` runs and what the telling must achieve.
- **How strict is the evidence?** Every claim traceable to a named document, or judgement allowed. Default when unanswered: traceable.
- **How deep?** A fast single pass, or the full workflow with specialists and an independent audit. Decides the agent setup.
- **Do you want it told as well as built?** A strategy file only, or a finished brief or deck outline. Decides whether stage 4 runs.

## Stage map

Run only the stages the answers call for. Each stage hands a file to the next.

**Stage 0. Gather.** Output: `ledger.md` and, when the material is scattered, `pyramid.md`.
- `prior-art`, when listed, to surface what already exists on the topic.
- A pile of documents, notes or transcripts: load `ask-story` and run its stages 0 to 3 as a called stage, under its "From `ask-strategy`" rules. It asks only what the routing questions left open, keeps its two checkpoints, and writes `ledger.md`, `clusters.md`, `pyramid.md` and `audience.md`. It builds no storyline and delivers nothing.
- When the user has confirmed the idea and the pillars, come back here and run stage 1. The confirmed pillars are the input to the strategy, not the strategy.
- If `ask-story` is not listed: read the pile against written questions, record each finding with its document and an exact quote, cluster with `affinity-mapper`, and reduce with `strategyu-skills:su-structure`.

**Stage 1. Frame the problem.** Output: `diagnosis.md`. The situation, what makes it hard, the question, and the crux.
- `strategyu-skills:su-frame` for the situation, complication and question, and for an issue tree when the problem has several parts.
- The diagnosis play in `awesome-pm-skills:strategy`: ask what makes it hard until the obstacle is named, then find the crux.
- `management-consultant`, loading only `references/issue-hypothesis-trees.md`, when the tree needs more depth.
- **Checkpoint, diagnosis.** Show the diagnosis in three sentences, with the one or two rival readings it beat. The user confirms or corrects it.

**Stage 2. Make the choices.** Output: `strategy.md`. Guiding policy, pillars, what stops, leading indicators.
- `awesome-pm-skills:strategy` is the default. Internal strategy: its action-agenda and team-process plays. Product or market strategy: add its choice cascade and moat test.
- `product-skills:playing-to-win` when the core question is where to play.
- `product-skills:7-powers-analysis` when a claimed advantage must be tested.
- `awesome-pm-skills:ai-product-bets` when the strategy is a set of AI features to build, delay or kill.
- `awesome-pm-skills:prioritize` to turn pillars into a sequenced roadmap and goals.
- `awesome-pm-skills:metrics` for the leading indicator on each pillar.
- `awesome-pm-skills:decide` when the strategy turns on one decision.
- A domain question inside the strategy (pricing, growth, hiring, organisation design): hand that question to `ask-pm` and bring the answer back.
- Test each pillar as a choice: it names something to do and something to stop, a reasonable person could disagree with it, it does not overlap another pillar, and together the pillars answer the diagnosis. Three at most; a fourth needs a stated reason.

**Stage 3. Stress-test.** Output: `audit.md`, findings ranked, each tied to a line in `strategy.md`.
- `product-skills:good-strategy-bad-strategy` to check the kernel and name any hallmark of bad strategy.
- The grading rubric in `awesome-pm-skills:strategy`, scored out of 40.
- `product-skills:pre-mortem` for how it fails.
- `execution-skills:yes-and` when the risk is thinking too small.
- `management-consultant` with `references/hypothesis-invalidation-discipline.md` when one assumption carries the whole strategy.
- Fix what the audit finds, in a new version of `strategy.md`, and say what was left unfixed and why.

**Stage 4. Tell it.** Output: the piece the user asked for, as a file, and its audit. Load `ask-story` and run its stages 4 to 6 on `strategy.md`, `ledger.md` and the reader's details, again as a called stage.
- A storyline is a working file, not the piece. The stage is finished when the memo, brief or deck outline exists and has been audited.
- If `ask-story` is not listed: `strategyu-skills:su-storyline` for the storyline and the piece, then `strategyu-skills:su-writing` as a check.
- When a meeting follows and stakeholders must be won over first: `awesome-pm-skills:influence` for the stakeholder map and the likely pushback.

**Stage 5. File.** `file-and-name`, when listed, to put the final version in its place.

## Common asks and their routes

- "Write our strategy", from an idea or from nothing: 1, 2, 3, then 4 if it must be told.
- "Turn these documents into a strategy": 0, 1, 2, 3, 4.
- "Review this strategy": 3 only, with the audit lenses in parallel, then a ranked fix list.
- "Are these the right pillars?": the pillar test in stage 2, then 3.
- "We cannot agree what the problem is": 1 only, stopping at the checkpoint.
- One skill covers it: load that skill and stop. A route of one is complete.

## Sequence and parallel

- **In sequence** wherever a stage consumes the one before: 0, 1, 2.
- **In parallel** wherever the pieces are independent:
  - two or three rival diagnoses before the checkpoint
  - the audit lenses in stage 3
  - the roadmap and the indicators, once the pillars are fixed
- Never run in parallel two steps that write the same file.

## Specialists

Spawn sub-agents only when the session has a tool for it and at least one of these holds: the user chose the full workflow, rival diagnoses are wanted, or the audit must be independent of the author. Otherwise run the stages yourself in order and say "one agent" in the route. Run at most four at once.

- **Framer**, one per rival diagnosis. Stage 1.
- **Strategist.** The stage 2 skills the route names. Writes `strategy.md`.
- **Sceptic.** One audit lens each from stage 3. Receives only the strategy and the ledger, never the drafting conversation.
- **Fact-checker.** Checks every claim in the strategy against the ledger and returns the unsupported ones.

A specialist starts with no memory of this conversation, so its brief carries everything:

- the goal in one sentence, and the user's answers to the routing questions
- the exact skill names to load with the Skill tool, and for a reference file, its path inside the skill
- the input files by path, and the one file it must write
- the report to return: ten lines at most, with the file path, the main result and any open questions
- the rules: add no fact that is not in the ledger, quote exactly, ask the user nothing, contact nobody, spawn no further agents

The orchestrator keeps the conversation with the user and the checkpoint. It merges the specialists' files, settles disagreements between them by the evidence in the ledger, and brings any it cannot settle to the user.

## Limits

- **A missing skill is named, and its fallback used.** `ask-story` has fallbacks above. Put anything else missing on the `Not done:` line.
- **Skills that need a connector are skipped unless it is connected:** `growth-skills:north-star-metric`, `growth-skills:build-metric-tree` and the `analytics-skills` set need Amplitude.
- **`management-consultant` is broad.** Load it for a named reference file, not as a general adviser. It may be listed as `management-consultant:management-consultant` or `management-consultant:skill`.
- **Do not load `strategyu-skills:su-coach` beside the other StrategyU skills.** It holds the same methods in one file.
- **Where two skills do the same job, use the first:**
  - `awesome-pm-skills:strategy` before `defining-product-strategy`
  - `awesome-pm-skills:prioritize` before `product-skills:prioritize`
  - The lenny-skills versions remain the source for guest quotes and principles.
- **Facts come from the user's material or a named source.** Quotes are copied exactly, with the document named.
- **Speak as the assistant.** Do not write as a named guest, author or consultant.
- **The user's standing format preferences win** over any skill's output template.

## Before delivering

Check these and fix what fails:

- the questions were asked first, and the answers shaped the route
- every stage in `route.md` has its output file, or is on the `Not done:` line with the reason
- the piece the user asked for exists as a file; a through-line note or a storyline is not the piece
- if the user chose the full workflow and no specialist ran, the `Not done:` line says why
- the diagnosis was confirmed by the user, or is marked "proposed, not confirmed"
- every pillar names something to do and something to stop
- every factual claim maps to a ledger row, and every quote is exact
- the audit came from an agent that did not write the strategy, or is labelled "self-audited"
- every skill on the `Skills used:` line was loaded in this session, by you or by a specialist
- the conclusion is the first line, and no earlier version was overwritten

## Worked routes

These double as the checks for this skill. Run them after any change to it.

**Questions first.** "/ask-strategy we need a tooling strategy for the design organisation." Before any skill loads, the reply asks whether the problem is agreed, which choices are still open, who decides, and how deep to go, each with its options explained. Without this skill the same prompt tends to produce a strategy document at once, which is the difference to look for.

**Full route with specialists.** After the answers "internal strategy, problem not agreed, leadership approves funding, full workflow": two Framers in parallel on rival diagnoses, then the checkpoint, then a Strategist, then three Sceptics and a Fact-checker in parallel, then the hand-off to `ask-story` for the brief.

**No stall at the hand-off.** "Turn these documents into one strategy and write the memo", with the answers given: the run ends with `strategy.md`, its audit and the memo. A run that ends on a through-line note or a storyline, with no strategy skill on the `Skills used:` line, has stalled inside `ask-story`.

**Not this skill.** "Here are my notes from the offsite, find the thread" has no strategy to build yet. It belongs to `ask-story`.

## Upkeep

Internal skill, written for the skills installed alongside it. When skills are added, removed or renamed, check every name in the stage map against the installed list.