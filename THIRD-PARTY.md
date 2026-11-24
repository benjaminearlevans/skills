# Third-party skills

Skills in this repo that Benjamin did not write, where each came from, and what was changed. Everything else is his.

## core/skills/

- **`minto-pyramid`** — Millwright Labs, MIT. https://github.com/millwright-labs/minto-pyramid-skill. `SKILL.md` and `LICENSE` copied unchanged on 2026-11-24. The upstream `evals/` folder and README are not included.
- **`brief-from-pile`** — Mohit Aggarwal, MIT. https://github.com/mohitagw15856/pm-claude-skills (`skills/brief-from-pile`). `SKILL.md` copied unchanged, with the repo's `LICENSE` beside it. It links to a sibling skill, `repo-map`, that is not included here.
- **`affinity-mapper`** — copied unchanged from the skill installed on Benjamin's Claude account. Source and licence not recorded.

## strategy/

- **`strategyu-skills`** (5 skills) — StrategyU, Paul Millerd. https://strategyu.co/strategy-consulting-aiskills/. A paid product, kept here for personal use. Content unchanged. In `strategyu-skills-claude/` the five skill folders moved under `skills/` and a `.claude-plugin/plugin.json` was added, so the folder installs as a plugin.

## product-management/

- **`awesome-pm-skills`** (25 skills) — Udi Menkes, MIT, version 2.0.0. https://github.com/menkesu/awesome-pm-skills. Kept: `.claude-plugin/plugin.json`, `LICENSE` and `skills/`. Removed: the 25 `assets/card.png` images (about 70 MB) and the one line in each `SKILL.md` that displayed that image. Nothing else changed.
- **`product-skills`** (20 skills) and **`execution-skills`** (6 skills) — Amplitude, version 1.0.0, MIT according to the repo's `plugin.json` (the archive holds no `LICENSE` file). https://github.com/amplitude/builder-skills. Both plugin folders copied unchanged. The repo's other six plugins are not included. `product-skills/skills/draft-spec/SKILL.md` has no frontmatter upstream, so it does not load as a skill.
- **`lenny-skills`** (76 skills) — built from Lenny's Podcast and Newsletter guest insights. Copied unchanged from the copies installed on Benjamin's Claude account, which came from a local folder. Source repository and licence not recorded. Personal use only until they are.

## Not included

- **`management-consultant`** — DogInfantry, Apache-2.0. https://github.com/DogInfantry/claude-skill-management-consultant-B1. `ask-strategy` uses two of its reference files when it is installed. Install it from its own repo.
- Amplitude's `growth-skills` and `analytics-skills`. `ask-strategy` names them and skips them unless the Amplitude connector is connected.
