---
name: file-and-name
description: "File an output into the right place under the right name with exactly one authoritative version — covers intake, the naming convention, project folder shape, and superseding older material."
---

# File and name

Use when something has been produced and needs to land somewhere, when a new project needs its shape, or when older material needs bringing into the structure.

Work that cannot be found again was not worth doing.

## Naming

    Descriptive-Name_vN_YYYY-MM-DD.ext

Version numbers rise and never reset. Prior versions stay where they are — never overwritten, never deleted. Folders lowercase and hyphenated. No spaces in anything created from here on.

The name should say what the thing is without the folder path. `Schedule-1-Pre-Existing-Materials_v6_2026-09-04.md` survives being emailed. `final-v2-USE-THIS.md` does not.

## Project shape

    <project>/
      README.md        what this is, who it is for, current state, next step
      source/          inputs, references, raw material
      working/         drafts and versions
      final/           the current shipped version, one file per artefact

`final/` holds exactly one authoritative copy of each artefact. Two files claiming to be the same thing is a defect — resolve it or escalate.

The README is the point of the structure. Someone opening this folder cold should know within twenty seconds what it is and what happens next.

## Intake

Unfiled material lands in `_inbox/`. Work it down; do not let it accumulate.

For each item: identify what it is → search for an existing version → file, supersede, or archive.

When superseding, move the old version to `_archive/` with its date intact and note the supersession in the new file's README. When archiving, never delete — the archive is the evidence base for what was created when, which has legal weight where IP ownership is concerned.

When refactoring older material, move, rename and index. Do not rewrite content — that belongs to whoever owns the surface.

## Canonical sources

`library/` holds the single authoritative version of anything referenced repeatedly. Maintain `library/INDEX.md`: what exists, one line each, and where.

When a fact appears in two places, `library/` wins and the copy gets flagged for deletion.

## Rules

Report what moved, as a short list.

Never move something that may be in active use without asking.

When duplication turns up — the same capability built twice under different names — surface it. That is the single most useful thing this skill produces.