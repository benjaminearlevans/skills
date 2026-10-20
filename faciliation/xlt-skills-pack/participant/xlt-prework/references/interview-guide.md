# Interview Guide

For each phase: the core questions (the base pass), the deeper probes (only when a signal fires), and what to write.

---

## Phase 0 — Welcome

**Say (adapt naturally, keep it short):**
> "This is the pre-work for the XLT session on what tooling XD should provide for everyone, and what's better local. AI or otherwise. I'll ask you questions about your team. It takes about 15 minutes, longer if you have more to say, and you can stop and pick it up later. Everything stays on your computer until you drop the folder into the shared drive. I'll replace anyone's name with their role. Ready?"

**Write:** create `session` with `phase: "0-welcome"`.

---

## Phase 1 — Team snapshot

**Core questions**
1. "Which team are you answering for?" Offer the list from `config.md`.
2. "What product area does the team cover, and roughly how many designers?"
3. "In one sentence, how would you describe your team's AI setup today?"

**Deeper probe** (only if the setup answer is rich): "What does a typical designer on your team actually open in a day?"

**Write:**
- `team`
- `ai_position`: inferred, using early / building / established / leading / unsure. Confirm it: "Sounds like you'd call the team *building*. Fair?"
- Create the folder and `prework.json`.

---

## Phase 2 — Problems and bottlenecks

**Core questions**
1. "What slows your designers down, or frustrates them most, right now? Not just AI. Anything."
2. Repeat "What else?" until they slow down. Capture each answer as a `need`.
3. "If you could fix only five of these, which five, in order?" Set `rank`.

**If answers dry up,** walk the PDLC, one moment at a time, and only until something lands:
- "Early on: understanding the problem, discovery, defining what to build?"
- "Building and testing with engineering, handoff, launch?"
- "After launch: spotting issues, investigating, starting the next round?"
- "Admin and coordination across all of it?"

**Deeper probes,** for ranked needs only, one at a time:
- "Give me an example from the last couple of weeks." → `example`
- "How often does that happen?" → `frequency`
- "What does it cost when it happens? Time, quality, rework?" → `cost`
- "What breaks downstream?" → `detail`

**Watch for**
- **A tool named as a need** ("we need a Figma plugin for…"). Ask "What job would it do?" and record that job.
- **A practice** ("our crits are messy"). Record it as a need, never as a tool.
- **A barrier** ("we're not allowed to…", "no one has time to…"). Record it as a `barrier` linked to the need.

---

## Phase 3 — Outcomes

**Core questions,** for each ranked need:
1. "When this goes well, what gets better? What are you trying to maximize or minimize?"
2. "How would you know it improved?"

**Shape** each answer with `outcome-modeling` into: "We do [task] to achieve [outcome]" or "We need [something] to achieve [outcome]". Read it back: "So: *we need faster synthesis to achieve decisions in days, not weeks.* Right?" If they agree, set `agent_drafted: true`.

**Write:** an `outcome` item, plus a link from the need to it. One outcome can serve several needs, so reuse it rather than duplicating it.

**Deeper probe:** "Is there anything you measure today that would show it?"

---

## Phase 4 — Inventory

**Core questions**
1. "What has your team built or adopted to get work done? Skills, prompts, templates, plugins, setups, docs, AI or not."
2. For each one:
   - "What do you call it?" → `lead_term`
   - "Which of the problems we talked about does it help with?" → `links`. If none, ask "What job does it do?" and add a need.
   - "Did the team build it, or adopt it?" → `built_or_adopted`
   - Suggest a bucket ("Sounds like *instructions*, a reusable way to do a task. Right?") → `bucket`
   - "Is it in the XD AI Hub? Could another team use it?" → `hub_status`, and a note in `detail`

**Then offer the opt-in scan** (see SKILL.md).

**Deeper probes,** only for tools the lead lights up about:
- "Why did you build it rather than use something that exists?" This reveals gaps.
- "How many people on the team use it?"
- "What would it take for another team to use it?"

---

## Phase 5 — Shared needs

**Core questions**
1. "What does your team need that it can't get, or can't build, on its own? Standards, shared context, guidance, access?"
2. "Do your designers use the XD AI Hub? Which parts? What's missing or out of date?"

**Write:**
- a `shared_ask` for each, linked to a need
- `barrier` items for anything blocking
- for Hub items they don't use: `exists_not_adopted`, plus "What would make your team use it?" in `detail`

**Deeper probe:** "What would a shared version give you that you couldn't get by building it yourselves?"

---

## Phase 6 — First sort

For each ranked need, shared ask and tool, keep it quick:
1. "Is this specific to your team, or do you think most teams have it?" → `axis_common`, 1–5
2. "Does it depend on your team's own product knowledge, or on XD-wide sources of truth like the design system or standards?" → `axis_context`, 1–5
3. "Gut call: XD-wide, XD standards with local implementation, local only, or unsure?" → `tier_guess`

Never argue with the answer. If they're unsure about everything, record `unsure` and move on.

---

## Phase 7 — Read-back

See SKILL.md. The summary format is one line per item:
`[type] text — rank · PDLC moment · links to …`

---

## Signals that open a deeper loop

- A long, specific or energetic answer
- A tool named without a need
- A barrier named ("we can't", "we're not allowed", "no time")
- A Hub item that exists but isn't used
- An item that fits no bucket. Ask: "How would you describe what this is?"

## Pacing

- **Base pass:** about 15 minutes.
- **At 25 minutes,** say: "We've covered the core. Want to keep going on anything, or wrap up?"
- **If the lead is in a hurry:** do phases 1–3 and 7, plus a one-question version of phase 4 ("List anything your team built or adopted"). Mark the remaining phases in `open_items`.
