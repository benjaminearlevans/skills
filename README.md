# Skills

Agent skills by Benjamin Evans, and the third-party packs his strategy workflow calls. Six packs: workflow, product management, strategy, typography, storytelling and facilitation.

To put the strategy workflow (`ask-strategy`, `ask-story`, `ask-pm`) on another computer, go to [Install the strategy workflow](#install-the-strategy-workflow).

Each skill is a folder holding a `SKILL.md` (name, description, instructions) plus the references and scripts it needs. They run in Claude Code, Claude, Cursor, Codex and any agent that reads the `SKILL.md` format.

## Packs

- **[Workflow](#workflow)** — `core/` — 8 skills. The three orchestrators and the five skills they call directly. Installs as the plugin `core`.
- **[Product management](#product-management)** — `product-management/` — 127 skills in four third-party plugins. The orchestrators call into them.
- **[Typography](#typography)** — `type/` — 7 skills. Ready to use.
- **[Storytelling](#storytelling)** — `storytelling/` — 14 skills. Draft scaffold, not ready to install.
- **[Facilitation](#facilitation)** — `faciliation/` — 6 skills. Built for one working session; reusable as a pattern.
- **[Strategy](#strategy)** — `strategy/` — 5 skills. StrategyU's consulting skills, v2, in two editions. Installs as the plugin `strategyu-skills`.

Who wrote what, and what was changed in the third-party packs, is in [`THIRD-PARTY.md`](THIRD-PARTY.md).

## Install the strategy workflow

The workflow is six plugins: `core`, `strategyu-skills`, `awesome-pm-skills`, `product-skills`, `execution-skills` and `lenny-skills`. Install all six. `core` alone still runs, but each orchestrator names what it could not find and falls back to a weaker step.

**Same Claude account?** Plugins and skills added in the Claude app are saved to the account, not the computer. If the other computer signs in to the same account, open **Customize > Plugins** there first: they may already be listed.

**In the Claude app, from GitHub.**

1. Open **Customize > Plugins**, then **Add > Add marketplace**.
2. Enter `benjaminearlevans/skills`. For a private repo, connect GitHub when the dialog asks and give the Claude GitHub App access to this repo.
3. Add the six plugins from the list that appears.

**In the Claude app, from files.** Use this when the app cannot reach the repo.

1. Download this repo to the computer.
2. Open **Customize > Plugins**, then **Add > Upload plugin**.
3. Upload each of the six `.plugin` files in `dist/`, one at a time.

**In Claude Code.** Run this in the root of this repo:

```bash
claude plugin marketplace add "$(pwd)"
for p in core strategyu-skills awesome-pm-skills product-skills execution-skills lenny-skills; do
  claude plugin install "$p@benjaminearlevans-skills"
done
```

**Check it worked.** Start a new chat and type `/core:ask-strategy we need a tooling strategy for the design organisation`. In the Claude app, type `/` and pick it from the menu. It should reply with three or four questions before it loads anything else.

**If Add is missing or refused.** On a Team or Enterprise plan an Owner decides whether members can add their own marketplaces and plugins. Ask the Owner, or have them publish the six plugins to the organisation.

**After changing a skill.** Run these in the root of this repo, then push, or upload the changed `.plugin` file again:

```bash
python3 scripts/check-workflow.py   # every skill the orchestrators call is still here
bash scripts/build-plugins.sh       # rebuild dist/
```

## Install one skill or one pack

**With the skills CLI.** Run these in the root of the project you want the skills in. Add `-g` to install for every project instead.

```bash
# See every skill in this repo
npx skills add benjaminearlevans/skills --list

# Install one skill by name
npx skills add benjaminearlevans/skills --skill practical-typography

# Install a whole pack
npx skills add https://github.com/benjaminearlevans/skills/tree/main/type
```

Install by name or by pack, not the whole repo. The facilitation skills appear more than once (source and built copies), so a whole-repo install offers duplicates.

Install the product-management packs as plugins, not this way. `awesome-pm-skills` and `product-skills` each hold a skill named `prioritize`, and the orchestrators tell them apart by plugin name.

**By hand.** Copy a skill folder into `~/.claude/skills/` (every project) or `.claude/skills/` inside one project. Run this in the root of this repo:

```bash
cp -R type/practical-typography ~/.claude/skills/
```

**In the Claude app.** Zip a skill folder and upload it as a skill.

## Workflow

`core/` — the plugin `core`. Three orchestrators that route a request across the other packs, and the five skills they call directly.

**The orchestrators.** Each asks its questions first, states the route, then runs it.

- **`ask-strategy`** — Builds and stress-tests a strategy: frames the problem, makes the choices, sets pillars that each name something to do and something to stop, scores the result and runs a pre-mortem. Hands the reading of a pile and the writing of the piece to `ask-story`, and owns the run until the piece exists.
- **`ask-story`** — Finds the through line in a pile of notes and drafts and turns it into a finished piece for a named audience: read, cluster, reduce to one idea and its pillars, storyline, write, audit.
- **`ask-pm`** — Routes a product, growth, leadership or career question to the one to four `lenny-skills` that fit, and combines them into one answer.

**What they call directly.**

- **`affinity-mapper`** — Clusters observations from the evidence up.
- **`brief-from-pile`** — Reads a folder of documents against written questions and keeps the source of every claim. Third-party.
- **`minto-pyramid`** — Restructures a draft conclusion-first and finds its buried lede. Third-party.
- **`prior-art`** — Surfaces what already exists on a topic before work starts.
- **`file-and-name`** — Files an output under the right name with one authoritative version.

`prior-art` and `file-and-name` were written for Benjamin's own project layout (`ops/`, `library/`, `_inbox/`, `_archive/`) and his Sentient knowledge base. On a computer without them, `prior-art` reports what it could not reach and `file-and-name` applies its naming rule and project shape to whatever folder is in use.

**What they call in the other packs.**

- `ask-strategy` → `strategyu-skills` (frame, structure, storyline, writing), `awesome-pm-skills` (strategy, prioritize, metrics, decide, influence, ai-product-bets), `product-skills` (playing-to-win, 7-powers, good-strategy-bad-strategy, pre-mortem), `execution-skills` (yes-and).
- `ask-story` → `strategyu-skills` (frame, structure, storyline, writing), `awesome-pm-skills` (exec-comms, position, decide), `execution-skills` (meeting-synthesis).
- `ask-pm` → `lenny-skills`, all 76.

**Optional extras, not in this repo.**

- [`management-consultant`](https://github.com/DogInfantry/claude-skill-management-consultant-B1) — `ask-strategy` reads two of its reference files when the problem tree needs more depth. Install it from its own repo.
- The Amplitude connector — `execution-skills` bundles it for its briefing commands and skills. `meeting-synthesis` and `yes-and`, the two the orchestrators call, work without it.

## Product management

`product-management/` — four third-party plugins, kept here so the workflow installs from one place. None is written by Benjamin.

- **`awesome-pm-skills/`** — 25 product management workflows by Udi Menkes, built from Lenny's Podcast. MIT. The card images are removed to keep the repo small.
- **`product-skills/`** — 20 skills by Amplitude: specs, experiments, discovery, and the strategy tests `ask-strategy` uses. MIT.
- **`execution-skills/`** — 6 skills and 3 commands by Amplitude: briefings, meeting synthesis, stakeholder updates, yes-and. MIT.
- **`lenny-skills/`** — 76 skills from Lenny's Podcast and Newsletter guest insights, each with two reference files. Source and licence not recorded, so personal use only.

## Typography

`type/` — seven skills for setting type on the web. Each does one job and names the skill to hand off to.

In the order you would use them on a project:

1. **`define-type-brief`** — Interviews you, extracts properties from reference sites and specimens, and writes `TYPE-BRIEF.md` to the project root. Every other skill loads that file when it exists and judges the work against it.
2. **`choose-web-fonts`** — Recommends typefaces and specifies delivery: licensing, formats, subsetting, variable axes, fallback metrics, payload. At most three directions, one default.
3. **`practical-typography`** — The build skill. Body text first, then scale, roles and spacing, then verification at several widths. Grounded in Butterick's *Practical Typography*, current CSS and WCAG.
4. **`typeset-content`** — Corrects characters in prose: quotes, dashes, ellipses, non-breaking spaces, symbols. Review mode reports; apply mode edits. Never touches code or URLs. Ships a linter at `scripts/lint-composition.mjs`.
5. **`review-typography`** — A strict gate on a diff or rendered page. Reports findings; never redesigns. Runs only when you ask for it by name.
6. **`improve-typography`** — Surveys a whole codebase and returns a few high-leverage improvement plans. Read-only on product code. Runs only when you ask for it by name.

And one that sits beside the sequence:

- **`typography-vocabulary`** — Reverse-lookup glossary. Describe the effect ("a single word stranded at the top of a column") and get the term (widow).

**Shared references.** `type/references/` is the source for ten reference files (foundations, registers, layout, formatting, web platform, accessibility, fonts, composition, anti-slop, review rubric). Each skill carries its own copy of the ones it needs, so any skill installs alone. Edit the source, then re-copy into each skill's `references/` folder — there is no sync script yet.

## Storytelling

`storytelling/` — a pack for moving an audience from one belief to another. **Status: scaffold.** Every `SKILL.md` is a skeleton with real frontmatter, section headers and notes on what each section must cover. All are marked `DRAFT`. Do not install them yet.

Three tiers:

**Tier 0 — the philosophy**
- **`storytelling`** — The entry point. The principles every other skill inherits. The canonical text lives in `references/philosophy.md`.

**Tier 1 — the domain lens**
- **`storytelling-for-designers`** — Case studies, portfolio narratives, design pitches, presenting decisions to executives.
- **`storytelling-for-engineers`** — Placeholder, not yet scoped.
- **`storytelling-for-researchers`** — Placeholder, not yet scoped.

**Tier 2 — the tactical skills, in the order a story gets built**
1. **`find-story-opportunities`** — Scans raw material for stories worth telling and names what to leave out.
2. **`find-the-throughline`** — Forces a pile of ideas down to one sentence and sorts everything else into keep, support, footnote or cut.
3. **`pick-story-structure`** — Chooses the shape the story needs for this audience and time limit.
4. **`narrate`** — Builds the beat skeleton for a case study or talk.
5. **`need-vision-insight`** — Builds the beat skeleton for a strategic pitch: customer need → compelling vision → business insight → ask.
6. **`audience-calibration`** — Reshapes the same story for executives, peers, a hiring panel or Q&A without changing the facts.
7. **`slide-design-system`** — Turns beats into slides: one idea per slide, FROM/TO contrast, monochrome first.
8. **`review-narrative`** — Strict, rule-based critique of a draft.
9. **`audit-deck`** — Audits a whole deck or portfolio and returns a fix plan another agent can execute.
10. **`storytelling-vocabulary`** — Reverse-lookup glossary for narrative moves ("the moment it all turns" → hinge).

**Where it is heading.** `storytelling-pack-overview-v3.md` describes the planned public set: 12 skills grouped by the three Ds — Define, Design, Deliver — with problem-first names such as `finding-the-throughline`. The folders have not been renamed to match yet. Earlier overviews (v1, v2) and philosophy drafts are kept alongside for comparison.

## Facilitation

`faciliation/` — six skills that run a working session end to end: interview each participant beforehand, synthesise the answers, build the board, write up the results. Built for the XLT session on local versus shared tooling.

The chain:

`/xlt-prework` (each lead) → submissions → `/xlt-synthesize` → review → `/xlt-board` → session → `/xlt-readback`

**Participant pack** — `xlt-prework/`
- **`xlt-prework`** — A 15-minute interview about a team's tooling, problems, barriers and outcomes. Writes `prework.json`, `prework.md`, `stickies.csv` and `team-terms.md` locally. Resumable. Names are replaced with roles.
- **`facilitating`** — Interview craft: neutral voice, one question at a time, need before tool. A dependency.
- **`outcome-modeling`** — Turns answers into structured needs, outcomes, tools, barriers and shared asks without overwriting the speaker's words. A dependency.

**Organiser pack** — `xlt-organizer/`
- **`xlt-synthesize`** — Reads every submission and drafts the v0 map: clusters, outcome scorecard, draft requirements, duplicates, contested items, glossary proposal and a board manifest.
- **`xlt-board`** — Builds the pre-placed FigJam board from the manifest.
- **`xlt-readback`** — Reads the worked board after the session and produces the deliverables.
- **`outcome-modeling`** — The same dependency as the participant pack.

`xlt-board` and `xlt-readback` need a Figma connection and the Figma skills `figma-use` and `figma-use-figjam`.

**Source and builds.** `xlt-skills-pack/` is the source: `participant/`, `organizer/` and `shared/` (config, schema, reference pack). `xlt-prework/` and `xlt-organizer/` are the built copies. Before distributing, fill in `xlt-skills-pack/shared/config.md`, then run this in `faciliation/xlt-skills-pack/`:

```bash
bash build.sh
```

It copies the shared references into every skill and writes `dist/xlt-prework.zip` and `dist/xlt-organizer.zip`.

**Try it without real data.** Three synthetic submissions live in `xlt-organizer/test-fixtures/`. Run this in `faciliation/xlt-organizer/`:

```bash
python3 xlt-synthesize/scripts/merge.py test-fixtures /tmp/xlt-test
```

Each pack has its own README with install and run steps.

## Strategy

`strategy/` — the StrategyU AI Skills, version 2, by [StrategyU](https://strategyu.co). Not written by Benjamin; kept here so they install alongside the rest. Built on the Pyramid Principle, MECE and SCQA.

- **`su-frame`** — Messy situation → defined problem: SCQA, hypotheses, issue trees.
- **`su-structure`** — Notes and data → an argument: MECE, Label-Sort-Insight, the pyramid.
- **`su-storyline`** — Gets the argument across as an email, memo, exec summary or deck, and gives feedback on existing slides.
- **`su-writing`** — Writing craft: cuts AI patterns and vague claims.
- **`su-coach`** — All four in one skill, start to finish.

Two editions of the same content:

- `strategyu-skills-claude/` — the plugin `strategyu-skills`: one folder per skill under `skills/`, for agents that load `SKILL.md` files.
- `strategyu-skills-general/` — one `.md` file per skill, to paste into ChatGPT, Gemini or any tool that takes custom instructions. `su-storyline-slides.md` is the deck add-on for `su-storyline`.

Full instructions, including the upgrade path from 1.x, are in `strategy/strategyu-skills-claude/README.md`. That file's copy command expects the `su-*` folders beside it. Here they sit one level down, so run it in `strategy/strategyu-skills-claude/skills/`.

## Layout

```
skills/
├── .claude-plugin/
│   └── marketplace.json         makes this repo a plugin marketplace: six plugins
├── core/                        plugin core: 3 orchestrators and 5 skills they call
│   ├── .claude-plugin/plugin.json
│   └── skills/<skill>/SKILL.md
├── product-management/          4 third-party plugins
│   ├── awesome-pm-skills/       25 skills
│   ├── product-skills/          20 skills, 2 commands
│   ├── execution-skills/        6 skills, 3 commands
│   └── lenny-skills/            76 skills, each with references/
├── dist/                        the six plugins as .plugin files, for upload
├── scripts/
│   ├── build-plugins.sh         rebuilds dist/
│   └── check-workflow.py        checks every skill the orchestrators call is here
├── THIRD-PARTY.md               sources, licences and changes
├── type/                        7 typography skills
│   ├── references/              source for the shared reference files
│   └── <skill>/                 SKILL.md, references/, sometimes scripts/
├── storytelling/                14 draft storytelling skills
│   ├── references/              philosophy, evidence index, story shapes
│   └── skills/<skill>/SKILL.md
├── faciliation/                 6 facilitation skills
│   ├── xlt-skills-pack/         source: participant/, organizer/, shared/, build.sh
│   ├── xlt-prework/             built participant pack
│   └── xlt-organizer/           built organiser pack and test fixtures
└── strategy/                    5 StrategyU skills
    ├── strategyu-skills-claude/     plugin strategyu-skills: skills/<skill>/
    └── strategyu-skills-general/    single-file edition
```

`_archive/` holds original downloads and superseded files. It stays on disk and is not committed.

`type/Weirdness` holds a link to the [weirdness engine](https://github.com/sethjenks/weirdness-engine).

## Conventions

- **One folder per skill.** The folder name is kebab-case and matches `name:` in the frontmatter.
- **The description does the routing.** It says what the skill does, then when to use it, with the phrases a person would actually say.
- **One job per skill.** Each skill says what it does not do and names the skill to hand off to.
- **Self-contained.** A skill carries its own references, so it works when installed alone.
- **Ask-only skills** set `disable-model-invocation: true`, so they run only when named.
- **Unfinished skills** start their description with `DRAFT`.
- **A pack that installs as a plugin** has `.claude-plugin/plugin.json` at its top and its skills under `skills/`. It is listed in `.claude-plugin/marketplace.json` and in `scripts/build-plugins.sh`.
- **Third-party skills stay as their authors wrote them.** Any change is recorded in `THIRD-PARTY.md`.
