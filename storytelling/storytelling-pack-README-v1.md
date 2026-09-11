# Storytelling Pack — Scaffold v1

**Status:** scaffold only. No skill is written. Every SKILL.md below is a skeleton: real frontmatter, real section headers, and bullet notes on what each section must cover and which evidence it draws on. Nothing inside is final until Benjamin has reviewed the flagship and the tier map.

Assumed layout: **Option B** (plugin of independent tactical skills sharing one philosophy reference). If you go with Option A instead, the `skills/storytelling-for-*` folders collapse into `references/` under a single `storytelling` skill; everything else stays.

## Tree

```
storytelling-pack/
├── README.md                          ← this file
├── references/                        ← shared, loaded on demand only
│   ├── philosophy.md                  ← T0 canonical text (every skill points here)
│   ├── evidence-index.md              ← every research item, tag, and which skills use it
│   ├── story-shapes.md                ← Reagan's six arcs, Vonnegut, Story Spine
│   ├── executive-forms.md             ← Minto/SCQA, BLUF, Amazon memo + PR/FAQ, Monroe
│   ├── mayer-multimedia.md            ← the 12 principles, near-verbatim
│   ├── data-ink-preattentive.md       ← Tufte + Knaflic
│   ├── design-artefact-mapping.md     ← Dahlström: narrative term → design artefact
│   └── worked-examples.md             ← Airbnb Snow White, your own case studies as exemplars
└── skills/
    ├── storytelling/                  ← T0 flagship
    ├── storytelling-for-designers/    ← T1 sub-flagship (the one to build first)
    ├── storytelling-for-engineers/    ← T1 placeholder
    ├── storytelling-for-researchers/  ← T1 placeholder
    ├── find-the-throughline/          ← T2 — build first
    ├── narrate/                       ← T2
    ├── need-vision-insight/           ← T2
    ├── audience-calibration/          ← T2
    ├── review-narrative/              ← T2
    ├── slide-design-system/           ← T2
    ├── pick-story-structure/          ← T2
    ├── storytelling-vocabulary/       ← T2 (cross-cutting)
    ├── audit-deck/                    ← T2 (later)
    └── find-story-opportunities/      ← T2 (later)
```

## How the skills work together (the intended flow)

1. **find-story-opportunities** — scan raw material; is there a story here at all, and what gets left out
2. **find-the-throughline** — many ideas → one ABT sentence; names what's cut or demoted
3. **pick-story-structure** — choose the shape (arc) the throughline needs for this audience/time
4. **narrate** or **need-vision-insight** — build the beat skeleton (narrate = case study/talk; need-vision-insight = strategic pitch)
5. **audience-calibration** — reshape the same skeleton for executives / peers / panel / Q&A
6. **slide-design-system** — turn beats into slides under the locked visual grammar
7. **review-narrative** — strict critique against fixed rules, table output
8. **audit-deck** — whole-deck/whole-portfolio prioritized fix plan for another agent
9. **storytelling-vocabulary** — cross-cutting; used whenever someone needs the right word to brief with

Every T2 skill opens by pointing at `references/philosophy.md`; T1 skills add the domain lens on top before any T2 skill runs.

## Open decisions for Benjamin before drafting
- Option A vs B (see above)
- Naming convention: current noun/verb phrases vs Anthropic's suggested gerunds (`finding-the-throughline`) — pick one, apply to all
- Where canonical philosophy lives: `references/philosophy.md` (as scaffolded) or inline in `skills/storytelling/SKILL.md` with the reference file as a pointer
- Which of the [T]-tagged items (Sinek, StoryBrand, Mehrabian) you want in the vocabulary skill at all
