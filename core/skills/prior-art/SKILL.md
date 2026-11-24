---
name: prior-art
description: "Before starting anything, surface what already exists on it — built artefacts, parked ideas, prior research, applicable prompts. Runs on demand when opening a roadmap item, and weekly against the whole roadmap."
---

# Prior art

The corpus is large and the retrieval is the problem. Roughly 300 named artefacts, 33 project folders, a knowledge vault, and years of parked thinking. The failure is not a shortage of material. It is that the relevant piece is not present at the moment it would be useful, so the work starts from zero and the same thing gets built again under a different name.

This runs before work starts, not after.

## Two triggers

**On demand.** Whenever a roadmap or queue item is picked up, before any work on it begins. Also whenever a new idea arrives that sounds like it might already exist.

**Weekly.** Friday, before the review. Runs in the reverse direction: which parked ideas has this week's roadmap made relevant.

## What it scans

**The repo.** `ops/` for parked ideas, decisions and prior queue entries. `library/` for canonical material. `products/`, `clients/`, `writing/`, `build/`, `business/` for built artefacts. `_archive/` for superseded versions — an old version often solves the current problem.

**The knowledge vault.** The Sentient knowledge base, through its MCP when connected, or as files if the folder is attached. It holds context the repo does not: history, relationships, prior projects, preferences. If it is unavailable this session, say so in the output rather than silently returning a thinner result.

Do not scan the whole of `~/Projects` unless asked. It is large, mostly stale, and the Librarian owns the consolidation of it.

## How to search

Do not keyword-match the item's title. Titles are the least stable thing in this corpus — the same idea appears under four names.

Search on:

- **The problem**, not the artefact. "Measuring whether AI changed the work" finds more than "assessment".
- **The nouns inside it.** Extract the two or three concrete objects and search each.
- **The adjacent concept.** What is this a version of? Search the parent idea.
- **The audience.** Something built for the same reader often transfers.

## What to return

At most seven items, ranked by usefulness, each one line with its path. Grouped:

**Already built.** This exists. Path, state, and whether it needs updating rather than rebuilding.

**Parked and now relevant.** From `ops/IDEAS.md` or a project README.

**Research already done.** Do not re-research what is already in the corpus.

**Applies here.** A prompt, skill or method that fits this task.

Then one line: **start from** — the single most useful thing to open first.

If nothing relevant exists, say that in one sentence. A clean result is a useful result and should not be padded.

## Rules

When the same capability is found built twice under different names, hand it to the Critic. That is its duplication trigger and this skill is its best source.

Never return more than seven. The point is to reduce the search, not to reproduce it.

Paths, not summaries. He can open the file.