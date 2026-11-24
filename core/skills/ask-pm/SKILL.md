---
name: "ask-pm"
description: "Routes a product, growth, leadership, founder or career goal to the one to four Lenny skills that fit, loads them, and combines their guidance into one answer. Use when the user types /ask-pm, says ask PM or ask Lenny, asks what Lenny's guests would say, or brings a goal that spans several Lenny skills or does not clearly belong to one. A request that plainly matches a single Lenny skill goes straight to that skill."
---

# Ask PM

Turns one goal into a route through the Lenny skill library (76 skills built from Lenny's Podcast and Newsletter guest insights): pick the few skills that fit, load them, work the goal with them, give one answer.

The index in this file only routes. The loaded skills carry the substance, so an answer written from the index alone is a guess with a citation on it.

## Run this every time

1. **Pin the goal.** State it in one sentence: the outcome wanted, the situation (stage, B2B or consumer, role, team size) and any deadline. Take these from the conversation first. Ask only when the answer changes the route, for example before or after product-market fit, founder or employee, self-serve or sales-led. Ask one question with at most three options, and say in a sentence what each option leads to before asking.
2. **Route.** Name the decision the goal turns on. Choose one primary skill for that decision and up to three supporting skills. Route on the decision, not on shared words: copy for a pricing page is `positioning` or `written-communication`, not `pricing-strategy`. Use "Look-alikes" when two skills seem to fit and "Common routes" when the goal is broad.
3. **Order the skills** the way the work runs: diagnose, decide, plan, communicate.
4. **Load each chosen skill with the Skill tool before using it.** Skills are listed either bare (`pricing-strategy`) or behind the name of the bundle that installed them (`lenny-skills:pricing-strategy`). Match on the last segment and call the name exactly as this session lists it.
5. **Open a skill's `references/` files only for a specific need**: a named framework or template (`artifacts.md`) or what a particular guest said (`guest-insights.md`). These files run to hundreds of kilobytes, so search them for the term instead of reading them whole.
6. **Work the goal.** Apply each skill's "How to Help" steps and principles to the user's own facts and numbers. Summarising a skill back to the user is not help.
7. **Give one answer.** Conclusion first, then the plan or decision in the order the user will act on it. Where two skills or two guests pull in different directions, say so, pick one for this situation and give the reason. The user's standing format preferences win over this skill's defaults.
8. **End with one line starting `Skills used:`**, naming each loaded skill and, in a few words, what it contributed.

## Limits that keep the answer honest

- **Four skills at most per answer.** More than that produces a survey, not advice. If the goal needs more, split it into phases, do the first phase now and name the later ones.
- **One skill is a complete route.** When a single skill covers the goal, load that one and stop.
- **A missing skill is named, not imitated.** If a routed skill is not installed in this session, say which one, carry on with the rest, and do not rebuild its content from memory.
- **No fit is a valid result.** If nothing in the index covers the goal, say so in one line and answer without the library.
- **Quotes come from loaded files only.** Attribute a line to a guest only when it appears in a skill or reference file loaded in this conversation, copied exactly. Otherwise describe the idea without a name.
- **Speak as the assistant.** The library is built from Lenny's Podcast and Newsletter. Do not write as Lenny Rachitsky or as any guest.

## Before sending

Check the draft against these and fix it before it goes out:

- every skill on the `Skills used:` line was loaded with the Skill tool in this conversation
- no more than four skills, and each one changed something in the answer
- every guest quote can be found in a loaded file
- the conclusion is the first line

## Routing index

One line per skill. Load it when the goal turns on the thing named.

### Strategy and direction

- `product-vision`: describing the future state a team is building toward, so teams align without being told what to do
- `defining-product-strategy`: diagnosing the real challenge and choosing how to win in a market
- `competitive-strategy`: durable advantage, a competitor threat, being different instead of slightly better
- `positioning`: which alternatives the product is compared with, why it is the obvious pick, and for which segment
- `ai-product-strategy`: where AI belongs in the product, and defensibility when everyone has the same models
- `evaluating-trade-offs`: weighing competing priorities, build or buy, technical debt, explaining a trade-off upward
- `high-stakes-decisions`: a large decision that is hard to reverse; reducing bias while keeping momentum
- `product-taste`: judging quality, saying why something works, deciding before data exists

### Discovery and validation

- `customer-interviews`: running one interview that gets past feature requests to the cause of a problem
- `continuous-discovery`: making customer contact a weekly team habit
- `analyzing-user-feedback`: turning a large pile of feedback into decisions
- `defining-icp`: naming the specific customer to build and sell for
- `idea-validation`: testing the riskiest assumptions of a bet cheaply before engineering commits
- `evaluating-startup-ideas`: whether an idea or market is worth pursuing at all: timing, business math, demand
- `measuring-pmf`: how close an existing product is to product-market fit
- `recovering-from-failure`: a product or launch that failed; diagnose, then pivot, persist or stop

### Planning and execution

- `goal-setting-okrs`: goals for a period that link company direction to daily work
- `north-star-metrics`: choosing and validating the one metric that ties customer value to business results
- `planning-cadence`: the rhythm of annual, quarterly and weekly planning
- `roadmap-prioritization`: what gets resources and in what order; scoring and portfolio balance
- `writing-prds`: turning an idea into a spec with the problem and success metrics clear
- `product-reviews`: reviews that go deep on the work instead of reporting status
- `shipping-velocity`: shipping faster through scoping, rituals and guardrails
- `product-experiments`: designing and reading one experiment correctly; incremental impact and statistical traps
- `launch-planning`: planning and coordinating a launch, from internal alignment to distribution
- `product-tool-stack`: choosing and setting up the team's product tools
- `engineering-health`: engineering productivity and health, technical debt, developer workflow

### Building with AI

- `ai-assisted-prototyping`: building a working prototype yourself with AI coding tools
- `ai-native-ux`: interface design for probabilistic output: intent, control, agency
- `ai-evals`: measuring and monitoring the quality of an AI feature
- `building-with-ai-agents`: running development through AI agents: direction, parallel work, automated review

### Growth

- `growth-model`: mapping the loops that drive growth and finding the constraint
- `acquisition-channels`: which channels to bet on and where each is in its life
- `user-onboarding-activation`: getting new users to first value
- `retention-engagement`: why users stay or leave; retention curves and habit mechanics
- `referrals-word-of-mouth`: referral programmes and viral loops
- `growth-experimentation`: running many growth tests: velocity, prioritisation, learning culture
- `seo-strategy`: search as a channel: technical health, programmatic content, AI discovery
- `plg-fundamentals`: making the product the main driver of adoption and revenue
- `plg-sales-integration`: adding a sales team on top of self-serve to win large accounts
- `pricing-strategy`: willingness to pay, value metric, packaging and price changes
- `international-expansion`: which countries to enter and how to adapt
- `building-growth-team`: when to hire for growth, who first, how to structure the team

### Marketing and brand

- `naming-and-branding`: a name or a brand identity
- `pr-and-press`: press tied to a business goal: funding, users, credibility
- `marketing-org-and-stack`: marketing team structure and tooling

### B2B sales

- `founder-sales`: a founder learning to sell and shaping a repeatable motion
- `first-b2b-customers`: finding and closing the first few customers through network and design partners
- `enterprise-sales-motion`: large deals: discovery, procurement, governance requirements

### Marketplaces

- `marketplace-fundamentals`: cold start, quality and leakage in a two-sided business
- `supply-demand-balance`: which side constrains growth and what to do about it
- `marketplace-liquidity-take-rates`: defining liquidity metrics and setting the take rate

### Founding and funding

- `fundraising`: bootstrap or raise, running a round, an exit
- `founding-exec-team`: choosing a co-founder and sequencing early leadership hires
- `founder-psychology`: the mental load of leading: resilience, reframing failure

### Team and organisation

- `org-design`: reporting lines, team size, how product, design and engineering pair up
- `hiring-product-talent`: finding, attracting and closing strong PMs and engineers
- `interviewing-evaluating-candidates`: designing an interview loop and judging candidates on real work
- `team-culture`: building and keeping the norms of a high-performing team
- `coaching-development`: growing people over time; moving from doing the work to coaching
- `giving-feedback`: one feedback conversation that changes behaviour and keeps the relationship
- `fixing-underperforming-teams`: a struggling team: find the cause, run a recovery plan
- `leading-org-change`: a reorganisation, a crisis, a new business unit, AI adoption across an organisation
- `running-meetings`: making meetings produce decisions

### Influence and communication

- `managing-up`: working with your own manager or founder for autonomy and resources
- `stakeholder-alignment`: getting agreement from people you do not manage
- `executive-communication`: executive reviews, board meetings, a high-stakes ask
- `written-communication`: memos, narratives and async writing as a leader
- `public-speaking`: a talk or presentation; delivery and presence

### Career and self

- `pm-career-growth`: the path from PM to senior leadership
- `building-a-promotion-case`: making the case for one specific promotion
- `breaking-into-product`: getting a first PM role
- `career-transitions`: weighing a new role or a change of professional identity
- `negotiating-compensation`: an offer: recruiter calls, equity, closing
- `personal-brand-network`: building a network and a public audience
- `time-energy-management`: personal focus, energy and boundaries

## Look-alikes

Skills that share words but answer different questions. Pick by the question.

- Is the idea worth pursuing at all: `evaluating-startup-ideas`. Is this specific bet right before we build: `idea-validation`. The product exists, do we have fit: `measuring-pmf`.
- One conversation with a customer: `customer-interviews`. The team's standing habit: `continuous-discovery`. A pile of feedback already collected: `analyzing-user-feedback`.
- Where we are going: `product-vision`. How we win: `defining-product-strategy`. What we fund first: `roadmap-prioritization`. What we commit to this period: `goal-setting-okrs`.
- The one metric: `north-star-metrics`. The goals for a period: `goal-setting-okrs`. The planning rhythm itself: `planning-cadence`.
- One experiment done properly: `product-experiments`. A programme of many tests: `growth-experimentation`.
- How buyers see us against alternatives: `positioning`. Whether the advantage lasts: `competitive-strategy`. What it is called and looks like: `naming-and-branding`.
- A trade-off that can be revisited: `evaluating-trade-offs`. A decision that cannot: `high-stakes-decisions`.
- The founder learning to sell: `founder-sales`. Landing the first few accounts: `first-b2b-customers`. Large accounts with procurement: `enterprise-sales-motion`. Sales added to a self-serve product: `plg-sales-integration`.
- Getting users to first value: `user-onboarding-activation`. Keeping them: `retention-engagement`.
- The whole growth system: `growth-model`. Choosing channels: `acquisition-channels`. One channel in depth: `seo-strategy` or `referrals-word-of-mouth`.
- A two-sided business in general: `marketplace-fundamentals`. Which side is short: `supply-demand-balance`. Metrics and fees: `marketplace-liquidity-take-rates`.
- Attracting and closing candidates: `hiring-product-talent`. Assessing them: `interviewing-evaluating-candidates`.
- One conversation: `giving-feedback`. One person over time: `coaching-development`. A whole team off track: `fixing-underperforming-teams`.
- Structure: `org-design`. Norms: `team-culture`. Getting from one state to another: `leading-org-change`.
- Your manager: `managing-up`. Your peers: `stakeholder-alignment`. The executive room: `executive-communication`.
- A spec: `writing-prds`. Any other leadership writing: `written-communication`.
- Entering product: `breaking-into-product`. Rising within it: `pm-career-growth`. One promotion: `building-a-promotion-case`. A move elsewhere: `career-transitions`. The offer: `negotiating-compensation`.
- The product failed: `recovering-from-failure`. The person is worn down: `founder-psychology`.
- Where to apply AI: `ai-product-strategy`. How it should feel to use: `ai-native-ux`. Whether it works: `ai-evals`. Prototyping it yourself: `ai-assisted-prototyping`. Your own build workflow: `building-with-ai-agents`.

## Common routes

Starting points for broad goals, in working order. Drop any step the user has already done and swap in a better fit when the situation calls for it.

- Is this worth building: `evaluating-startup-ideas`, `customer-interviews`, `idea-validation`, `ai-assisted-prototyping`
- Do we have product-market fit: `measuring-pmf`, `analyzing-user-feedback`, `defining-icp`, `retention-engagement`
- Set direction for the year: `product-vision`, `defining-product-strategy`, `goal-setting-okrs`, `roadmap-prioritization`
- Bring a product to market: `positioning`, `pricing-strategy`, `launch-planning`, `pr-and-press`
- Growth has stalled: `growth-model`, `retention-engagement`, `user-onboarding-activation`, `growth-experimentation`
- First B2B revenue: `defining-icp`, `founder-sales`, `first-b2b-customers`, `pricing-strategy`
- Ship an AI feature: `ai-product-strategy`, `ai-native-ux`, `ai-evals`
- A team is slow or struggling: `fixing-underperforming-teams`, `shipping-velocity`, `giving-feedback`, `team-culture`
- Win a decision from leadership: `stakeholder-alignment`, `executive-communication`, `written-communication`
- Get promoted: `pm-career-growth`, `building-a-promotion-case`, `managing-up`
- Change jobs: `career-transitions`, `negotiating-compensation`, `personal-brand-network`
- Start or fix a marketplace: `marketplace-fundamentals`, `supply-demand-balance`, `marketplace-liquidity-take-rates`

## Worked routes

These double as the checks for this skill: run them after any change to it.

**Several skills.** "We launch a B2B scheduling tool in eight weeks. Help me price it and plan the launch." The decision is price, and price depends on what the buyer compares the tool with. Route: `positioning`, then `pricing-strategy` (primary), then `launch-planning`. The answer ends with a `Skills used:` line naming all three. Without this skill the same prompt tends to load one skill at most and gives no such line, which is the difference to look for.

**One skill.** "I need to tell a senior engineer their design reviews are too harsh." One conversation, so `giving-feedback` alone. `coaching-development` shares the subject but answers a different question. A plain request like this, made without /ask-pm, belongs to `giving-feedback` directly and should not load this skill.

**No fit.** "/ask-pm why is my database query slow?" Nothing in the index covers it. Say so in one line and answer without the library.

## Upkeep

Internal skill, written for one installed library. The index lists the 76 skills in the local lenny-skills folder. When skills are added, removed or renamed, rebuild the index from the installed skill list so every line points at a skill that exists.