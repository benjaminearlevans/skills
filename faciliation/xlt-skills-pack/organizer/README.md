# XLT Organizer Skills

For Ben, Patrick and the facilitation team. Leads never install these.

## The chain
`xlt-prework` (each lead) → submissions in the shared drive → **`/xlt-synthesize`** → Ben and Patrick review → **`/xlt-board`** → v0 map to leads → session → **`/xlt-readback`**

## Install
Copy these four folders into `~/.claude/skills/`:
- `xlt-synthesize`
- `xlt-board`
- `xlt-readback`
- `outcome-modeling` (shared with the participant pack)

`xlt-board` and `xlt-readback` also need the Figma connection, plus the Figma skills `figma-use` and `figma-use-figjam`.

## Before you distribute the participant pack
1. Fill in `shared/config.md`: the session date, shared drive link, contact, and team list.
2. Run `bash build.sh` from the pack root. It copies the shared references into every skill, so they all match, and rebuilds both zips.
3. Send `xlt-prework.zip` to leads.

## Run
1. **Synthesize.** Download the shared drive folder, then run:
   ```
   /xlt-synthesize ~/Downloads/xlt-submissions ~/xlt-synthesis
   ```
   Review `merge-report.md` first, then `v0-map.md`, `contested.md` and `glossary-proposal.md`.
2. **Build the board** after the review, with `/xlt-board <FigJam URL>`.
3. **After the session,** run `/xlt-readback <FigJam URL>`.
4. **When the top-down list arrives,** run `/xlt-synthesize --reconcile <list>`.

## Test
`test-fixtures/` holds three synthetic submissions: an advanced team, an earlier team, and a laundry list. To try the chain without real data:
```
python3 xlt-synthesize/scripts/merge.py test-fixtures /tmp/xlt-test
```
