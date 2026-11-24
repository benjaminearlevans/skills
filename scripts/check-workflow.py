#!/usr/bin/env python3
"""Checks that every skill the three orchestrators call is in this repo.

Run in the root of this repo:  python3 scripts/check-workflow.py
Run it after adding, removing or renaming a skill. Exit code 1 means a
plugin is broken or an orchestrator names a skill that is not here.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ORCHESTRATORS = ["ask-strategy", "ask-story", "ask-pm"]
# Called by the orchestrators but installed separately. See README, "Optional extras".
EXTERNAL = {"management-consultant", "growth-skills", "analytics-skills"}

def frontmatter_name(skill_md):
    m = re.search(r'^name:\s*"?([^"\n]+?)"?\s*$', skill_md.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else None

problems, names, qualified = [], set(), set()
market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
for entry in market["plugins"]:
    plugin, folder = entry["name"], ROOT / entry["source"]
    manifest = folder / ".claude-plugin/plugin.json"
    if not manifest.is_file():
        problems.append(f"{plugin}: no .claude-plugin/plugin.json in {entry['source']}"); continue
    if json.loads(manifest.read_text())["name"] != plugin:
        problems.append(f"{plugin}: plugin.json has a different name")
    skills = sorted((folder / "skills").glob("*/SKILL.md"))
    if not skills:
        problems.append(f"{plugin}: no skills/<name>/SKILL.md")
    for s in skills:
        for n in {s.parent.name, frontmatter_name(s)} - {None}:
            names.add(n); qualified.add(f"{plugin}:{n}")
    print(f"{plugin:20} {len(skills):3} skills")

external = set()
for o in ORCHESTRATORS:
    text = (ROOT / "core/skills" / o / "SKILL.md").read_text(encoding="utf-8")
    refs = set(re.findall(r"`([a-z0-9-]+(?::[a-z0-9-]+)?)`", text))
    for ref in sorted(refs):
        plugin = ref.split(":")[0]
        if ":" in ref:
            if plugin in EXTERNAL: external.add(ref)
            elif ref not in qualified: problems.append(f"{o}: calls `{ref}`, which is not in this repo")
        elif ref in EXTERNAL: external.add(ref)
    if o == "ask-pm":  # every line of its routing index must be a Lenny skill
        for ref in re.findall(r"^- `([a-z0-9-]+)`:", text, re.M):
            if f"lenny-skills:{ref}" not in qualified:
                problems.append(f"ask-pm: index lists `{ref}`, which is not in lenny-skills")
    for ref in ("ask-strategy", "ask-story", "ask-pm", "affinity-mapper", "brief-from-pile",
                "minto-pyramid", "prior-art", "file-and-name"):
        if ref in refs and f"core:{ref}" not in qualified:
            problems.append(f"{o}: calls `{ref}`, which is not in core")

if external:
    print("\nInstalled separately (optional):", ", ".join(sorted(external)))
if problems:
    print("\nPROBLEMS"); [print(" -", p) for p in problems]; sys.exit(1)
print("\nOK: every skill the orchestrators call is in this repo.")
