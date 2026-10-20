---
name: xlt-synthesize
description: Organizer-side synthesis for the XLT local vs shared tooling session. Reads every lead's prework.json from the submissions folder and drafts the v0 map — cleaned items, need clusters, outcome scorecard, draft requirements by altitude, duplicates, exists-not-adopted flags, contested items, a glossary proposal and a board manifest. Use when the user types /xlt-synthesize, says pre-work submissions are in, or asks to build the v0 map; also use with --reconcile when a top-down requirements list arrives.
---

# XLT Synthesize

Turn every lead's pre-work into one draft map that Ben and Patrick can review in a single sitting.

## Inputs

- **A submissions folder** holding one `<team>/prework.json` per lead, copied down from the shared drive. Ask for the path if it wasn't given.
- **`references/reference-pack.md`, `references/schema.md` and `references/config.md`.** Read all three first.
- **Optional:** `--reconcile <top-down-list>`, a markdown or CSV list of top-down requirements.

Load `outcome-modeling` to keep wording consistent.

## Steps

### 1. Merge
```
python3 <this skill's folder>/scripts/merge.py <submissions-folder> <output-folder>
```
This writes:
- **`combined.json`:** every item, namespaced by team
- **`merge-report.md`:** counts per team and type, submissions that are missing or invalid, likely duplicates by text similarity, and items missing an outcome

Read `merge-report.md` and fix anything invalid before going on. Check the config team list against who submitted, and list who's missing.

### 2. Clean
Nothing was filtered at capture, so cleanup happens here:
- **Merge near-duplicates within a team.** Keep the clearest `text`, and union the links.
- **Weight items** with `weight = rank_bonus + completeness_count`. Rank 1–5 gives a bonus of 5 down to 1, and unranked gives 0. `completeness_count` is the number of true tags, 0–3.
- **Mark** needs with no outcome link as `needs_outcome`. Keep them.

### 3. Cluster needs
- **Group by PDLC moment first**, then by the outcome the needs serve.
- **Size:** aim for 6–12 clusters across the whole org. A cluster needs needs from at least 2 teams, or one team's rank-1 need.
- **Name:** give each cluster a plain name as a job ("Turning research into decisions"), not a tool name.
- **Record:** for each cluster, its member needs, its teams, its total weight, and its outcomes.

### 4. Build the outcome scorecard
- **Merge outcomes** that say the same thing, keeping the clearest wording.
- **List each outcome** with the clusters it serves, the number of teams naming it, and any measure leads mentioned.

### 5. Draft requirements
For each cluster, draft 1–4 requirements. Each one should:
- **Say what's needed,** not which tool. For example: "Designers can turn a research readout into ranked insights in under an hour."
- **Name the outcome it moves.** No outcome, no requirement. Hold it in the "needs an outcome" lane instead.
- **Carry a draft altitude:** `xd_wide`, `xd_standards_local` or `local_only`. Base it on:
  - the median `axis_common` and `axis_context` of its members
  - the teams' `tier_guess` values
  - how many teams have it (threshold 1: breadth ≥ 3)
- **List the thresholds it passes:** breadth, outcome and shared value, in brief. Leave stability and ownership for the room.

Draft requirements only from items with `weight ≥ 2`, or that appear in ≥ 2 teams. Everything else stays on the board as stickies.

### 6. Map the tooling
- **Place every tool** beneath the need, and so the cluster, it serves.
- **Duplicates:** flag tools from 2+ teams serving the same cluster.
- **Exists, not adopted:** list every `exists_not_adopted` item with the teams' reasons, from `detail`.
- **Shortlist:** draft a retire / transform / adopt shortlist, and mark it as draft.

### 7. Pre-mark contested items
An item is contested when:
- teams' tier guesses for it split across two or more altitudes, or
- its axes point one way and its tier guesses another, or
- it sits right at a threshold (for example, exactly 3 teams).

Aim for 5–15 contested items. If there are more, keep the highest-weight ones.

### 8. Propose glossary v1
- **Collect** every `lead_term` and `terms` entry under its seed bucket.
- **Propose changes:**
  - **splits:** a bucket holding clearly different kinds of thing
  - **merges:** different words for the same thing across teams
  - **new buckets:** from items marked `other`
- **Flag terms used differently** by different teams.

Ben and Patrick ratify it.

### 9. Reconcile with top-down (only with `--reconcile`)
Match each requirement against the top-down list, and tag it:
- `both`: high confidence
- `bottom_up_only`: a ground-level find
- `top_down_only`: validate with leads

Without the flag, leave a "Top-down reconciliation: pending" section in `v0-map.md`.

## Outputs (in the output folder)

1. **`v0-map.md`**, using the template in `references/v0-map-template.md`.
2. **`contested.md`:** each contested item, why it's contested, and the teams on each side.
3. **`glossary-proposal.md`**
4. **`board-manifest.json`**, using the schema in `references/board-manifest.md`.

## Rules

- **Never invent items.** Everything traces to a submission ID.
- **Never resolve an altitude.** Draft it and mark it as draft. The room decides.
- **Cap each team at 5 ranked items** in draft requirements. Extras go in a parking-lot section, so long lists don't dominate.
- **Use "teams", never "towers".** Use American spelling.

## Signs it's working

- Every requirement names an outcome.
- The duplicates list is short and specific.
- `contested.md` holds 5–15 items.
- Every sticky in the manifest traces to a submission ID.
