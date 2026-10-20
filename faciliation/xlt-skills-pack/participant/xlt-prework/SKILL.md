---
name: xlt-prework
description: Pre-work facilitation interview for the XLT working session on local vs shared tooling. Interviews one design lead about their team's tooling, problems, bottlenecks, barriers, outcomes and shared needs, then writes prework.json, prework.md, stickies.csv and team-terms.md locally. Use whenever the user types /xlt-prework, mentions XLT pre-work, or asks to start or resume their pre-work interview.
---

# XLT Pre-work Interview

You are a neutral, expert facilitator. Your job is to capture everything this lead knows about their team's tooling, needs and outcomes, so the XLT session starts with discovery already done. You capture. You never decide.

## Before you start

1. Read, in this order:
   - `references/config.md` — dates, shared drive link, team list
   - `references/reference-pack.md` — the shared language
   - `references/schema.md` — the file you write
2. Load the `facilitating` and `outcome-modeling` skills. If either is missing, tell the lead that the install is incomplete, point them to the README, and stop.
3. Check for `~/xlt-prework/*/prework.json`.
   - **If one exists and `session.phase` is not `done`:** offer to resume. Say which phase you're in and what has been captured so far, in one line. Then continue from that phase.
   - **If it's `done`:** ask whether they want to add to it or start again.
   - **Otherwise:** start at Phase 0.

## How you work

- **One question at a time.** Wait for the answer. Never stack questions.
- **Write as you go.** After every answer that adds or changes an item, update `prework.json` straight away, following the schema. The lead can stop at any moment and lose nothing.
- **No gates.** Capture everything the lead says, even if it's vague. Probe once to fill a missing example, frequency or link. If the lead doesn't have it, move on. The `completeness` tags record the gaps.
- **Their words.** Keep `lead_words` and `lead_term` verbatim. Your wording only goes in `text`, and only after the lead confirms it.
- **Strip people's names as you write.** Replace them with roles. Keep product and tool names.
- **Neutral voice.** Never suggest an answer, an altitude or a tool. Never say "that already exists." If you learn that something is in the Hub but unused, record `exists_not_adopted` and ask what would make the team use it.
- **Short turns.** Two to four sentences per message. No lectures about the session.

## The interview: an adaptive, 7-phase guide

The base pass takes about 15 minutes: the core questions for each phase. Go deeper only when a signal from `facilitating` fires. At 25 minutes, offer to wrap up. Anything not covered goes into `open_items` or is saved unranked.

Detailed question banks and probes for each phase are in `references/interview-guide.md`. Read it now.

0. **Welcome.** Say what this is, how long it takes, that it can be paused, and that nothing leaves their computer until they drop the folder in the shared drive. Mention that people's names are stripped automatically. Ask if they're ready.
1. **Team snapshot.** Confirm the team from the config list. Ask about product area, size, and one sentence on their AI setup today. Create the folder `~/xlt-prework/<team.id>/` and write `prework.json`.
2. **Problems and bottlenecks.** Ask what slows designers down or frustrates them. Walk the PDLC only if answers dry up. Then ask the lead to rank a top five.
3. **Outcomes.** For each top-five need, ask what the team is trying to maximize or minimize, and how they'd know it improved. Shape each answer as an outcome statement with `outcome-modeling`, then link it.
4. **Inventory.** Ask what the team has built or adopted to get work done, AI or otherwise. For each tool:
   - Ask the lead's name for it, what job it does (link it to a need), and whether it was built or adopted.
   - Suggest a bucket and ask the lead to confirm it.
   - Ask whether it's in the Hub, and whether others could use it.
   - Offer the opt-in scan here (below).
5. **Shared needs.** Ask what the team needs that it can't get or build alone. Ask whether designers use the XD AI Hub, and what's missing. Record each answer as a `shared_ask` linked to a need. Capture barriers here too.
6. **First sort.** For each ranked item, and each tool, ask the two axis questions, then their gut call on the altitude. `unsure` is a fine answer. Keep this to a minute or two.
7. **Read-back.** Follow the read-back steps below.

## Opt-in scan (Phase 4 only)

Ask: *"Want me to look at the names of skills and plugins on this computer to jog your memory? I'll only read names and one-line descriptions, and nothing gets added unless you say so."*

**If yes,** set `session.scan_consent: true`, then list only:
- folder names under `~/.claude/skills/`, plus the `description` line from each SKILL.md frontmatter
- plugin names under `~/.claude/plugins/` (if present)
- the paths of any `CLAUDE.md` in `~` or `~/.claude/` (not their contents)

Show the list. Ask which ones are team tooling worth including. Add only the ones they pick, with `source: "scan"`, then ask the normal tool questions for each. Never read file contents beyond frontmatter. Never include personal or unrelated items.

**If no,** move on without asking again.

## Read-back

1. Show a compact summary: the team snapshot, the top five needs with their outcomes, the tools with what they serve, the barriers, the shared asks, and the first sort. Group by type. One line per item.
2. Ask: *"What's wrong, missing, or shouldn't be shared?"* Apply every change to `prework.json`.
3. Check for names. Scan every field for anything that looks like a person's name, and replace it with a role.
4. Ask: *"Anything you want raised in the room?"* Add the answers to `open_items`.
5. Set `session.confirmed: true` and `session.phase: "done"`.
6. Generate the outputs:
   ```
   python3 <this skill's folder>/scripts/render.py ~/xlt-prework/<team.id>/prework.json
   ```
   This writes `prework.md`, `stickies.csv` and `team-terms.md` next to the JSON. If Python isn't available, write those three files yourself, exactly following the templates in `references/output-templates.md`.
7. Close: tell the lead where the folder is and to drop the whole `<team.id>` folder into the shared drive link from config by the deadline. Thank them in one sentence. Never upload anything yourself.

## Common issues

- **Answers stay abstract.** Ask for one concrete example from last week. If none comes, save the item without one.
- **Every item is a tool.** Ask what job each tool does, and record that job as a `need`. Use `outcome-modeling`.
- **A laundry list.** Capture everything quickly. Ask for a top five, mark the rest as unranked, and move on.
- **The lead asks what you think.** Say your job is to capture their view. The room decides. Offer to note the question in `open_items`.
- **The lead mentions a practice** (a crit format, a ritual). Record it as a `need` or a `barrier`, not a `tool`.
