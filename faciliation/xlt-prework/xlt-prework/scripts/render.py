#!/usr/bin/env python3
"""Render prework.md, stickies.csv and team-terms.md from prework.json.

Usage: python3 render.py <path/to/prework.json>
Standard library only. Writes the three files next to the JSON.
"""
import csv
import json
import sys
from pathlib import Path

TYPES = {"need", "outcome", "tool", "barrier", "shared_ask"}
COLORS = {
    "need": "yellow",
    "outcome": "green",
    "requirement": "orange",
    "tool": "blue",
    "barrier": "pink",
    "shared_ask": "purple",
}
TIERS = {"xd_wide", "xd_standards_local", "local_only", "unsure", None}
BUCKETS = {"knowledge", "instructions", "automation", "environment", "other", None}


def dash(v):
    return "—" if v in (None, "", []) else str(v)


def derive_completeness(item, outcome_ids_linked_to):
    links = item.get("links") or []
    linked = bool(links)
    if item.get("type") == "outcome" and item["id"] in outcome_ids_linked_to:
        linked = True
    return {
        "example": bool(item.get("example")),
        "grounded": bool(item.get("frequency") or item.get("cost")),
        "linked": linked,
    }


def validate(data):
    problems = []
    if data.get("schema_version") != "1.0":
        problems.append("schema_version should be 1.0")
    team = data.get("team") or {}
    if not team.get("id"):
        problems.append("team.id is missing")
    ids = set()
    for it in data.get("items", []):
        iid = it.get("id")
        if not iid:
            problems.append(f"item without id: {it.get('text')!r}")
            continue
        if iid in ids:
            problems.append(f"duplicate id {iid}")
        ids.add(iid)
        if it.get("type") not in TYPES:
            problems.append(f"{iid}: unknown type {it.get('type')!r}")
        if it.get("tier_guess") not in TIERS:
            problems.append(f"{iid}: unknown tier_guess {it.get('tier_guess')!r}")
        if it.get("type") == "tool" and it.get("bucket") not in BUCKETS:
            problems.append(f"{iid}: unknown bucket {it.get('bucket')!r}")
        if len((it.get("text") or "").split()) > 15:
            problems.append(f"{iid}: text over 15 words (sticky will be truncated)")
    for it in data.get("items", []):
        for l in it.get("links") or []:
            if l not in ids:
                problems.append(f"{it.get('id')}: links to unknown id {l}")
    return problems


def main(path):
    p = Path(path).expanduser()
    data = json.loads(p.read_text())
    problems = validate(data)
    items = data.get("items", [])
    by_id = {i["id"]: i for i in items if i.get("id")}

    # Outcomes that some item links to
    linked_targets = {l for i in items for l in (i.get("links") or [])}
    for it in items:
        it["completeness"] = derive_completeness(it, linked_targets)

    def linked_of(item, typ):
        return [by_id[l] for l in (item.get("links") or []) if l in by_id and by_id[l]["type"] == typ]

    def linking_to(item, typ):
        return [i for i in items if i["type"] == typ and item["id"] in (i.get("links") or [])]

    def needs_outcome(it):
        return it["type"] == "need" and not linked_of(it, "outcome") and not linking_to(it, "outcome")

    team = data.get("team", {})
    sess = data.get("session", {})
    out = []
    out.append(f"# XLT Pre-work — {team.get('name', team.get('id', ''))}\n")
    out.append(
        f"*{dash(team.get('product_area'))} · {dash(team.get('size'))} · AI position: "
        f"{dash(team.get('ai_position'))} · completed {dash(sess.get('updated'))}*\n"
    )
    out.append(f"**AI setup:** {dash(team.get('ai_setup'))}\n")

    needs = [i for i in items if i["type"] == "need"]
    ranked = sorted([n for n in needs if n.get("rank")], key=lambda n: n["rank"])
    unranked = [n for n in needs if not n.get("rank")]

    out.append("## Top five needs")
    for n in ranked:
        outcomes = linked_of(n, "outcome") + linking_to(n, "outcome")
        barriers = linking_to(n, "barrier") + linked_of(n, "barrier")
        out.append(f"{n['rank']}. **{n['text']}** — {dash(n.get('pdlc_moment'))}")
        out.append(f"   - Example: {dash(n.get('example'))}")
        out.append(f"   - Frequency / cost: {dash(n.get('frequency'))} / {dash(n.get('cost'))}")
        out.append(f"   - Outcome: {'; '.join(o['text'] for o in outcomes) if outcomes else 'needs an outcome'}")
        out.append(f"   - Barriers: {dash('; '.join(b['text'] for b in barriers))}")
        out.append(
            f"   - First sort: {dash(n.get('tier_guess'))} (common {dash(n.get('axis_common'))}/5, "
            f"source of truth {dash(n.get('axis_context'))}/5)"
        )
    if not ranked:
        out.append("- —")
    out.append("")

    out.append("## Other needs (unranked)")
    out += [f"- {n['text']} — {dash(n.get('pdlc_moment'))}" for n in unranked] or ["- —"]
    out.append("")

    out.append("## Outcomes")
    for o in [i for i in items if i["type"] == "outcome"]:
        serves = linking_to(o, "need") + linked_of(o, "need")
        out.append(f"- {o['text']}  ← serves: {dash('; '.join(s['text'] for s in serves))}")
    out.append("")

    if out[-1] == "" and out[-2].startswith("## "):
        out.insert(-1, "- —")
    out.append("## Tools")
    for t in [i for i in items if i["type"] == "tool"]:
        serves = linked_of(t, "need")
        out.append(
            f"- **{t.get('lead_term') or t['text']}** ({dash(t.get('bucket'))}, {dash(t.get('built_or_adopted'))}, "
            f"Hub: {dash(t.get('hub_status'))}) — {t['text']}. Serves: {dash('; '.join(s['text'] for s in serves))}. "
            f"First sort: {dash(t.get('tier_guess'))}"
        )
    out.append("")

    if out[-1] == "" and out[-2].startswith("## "):
        out.insert(-1, "- —")
    out.append("## Barriers")
    for b in [i for i in items if i["type"] == "barrier"]:
        out.append(f"- {b['text']} — blocks: {dash('; '.join(s['text'] for s in linked_of(b, 'need')))}")
    out.append("")

    if out[-1] == "" and out[-2].startswith("## "):
        out.insert(-1, "- —")
    out.append("## Shared asks")
    for s in [i for i in items if i["type"] == "shared_ask"]:
        out.append(
            f"- {s['text']} — for: {dash('; '.join(x['text'] for x in linked_of(s, 'need')))}. "
            f"First sort: {dash(s.get('tier_guess'))}"
        )
    out.append("")

    if out[-1] == "" and out[-2].startswith("## "):
        out.insert(-1, "- —")
    out.append("## Open items for the room")
    out += [f"- {o}" for o in data.get("open_items", [])] or ["- —"]
    out.append("")

    (p.parent / "prework.md").write_text("\n".join(out))

    # stickies.csv
    cols = ["id", "type", "color", "text", "team", "pdlc_moment", "rank", "bucket", "links",
            "tier_guess", "axis_common", "axis_context", "completeness", "hub_status", "needs_outcome"]
    with open(p.parent / "stickies.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for it in items:
            c = it["completeness"]
            color = "gray" if it.get("hub_status") == "exists_not_adopted" else COLORS.get(it["type"], "yellow")
            w.writerow([
                it["id"], it["type"], color, it.get("text", ""), team.get("id", ""),
                it.get("pdlc_moment") or "", it.get("rank") or "", it.get("bucket") or "",
                ";".join(it.get("links") or []), it.get("tier_guess") or "",
                it.get("axis_common") or "", it.get("axis_context") or "",
                ("E" if c["example"] else "-") + ("G" if c["grounded"] else "-") + ("L" if c["linked"] else "-"),
                it.get("hub_status") or "", "true" if needs_outcome(it) else "false",
            ])

    # team-terms.md
    terms = list(data.get("terms", []))
    known = {t["term"].lower() for t in terms if t.get("term")}
    for t in [i for i in items if i["type"] == "tool" and i.get("lead_term")]:
        if t["lead_term"].lower() not in known:
            terms.append({"term": t["lead_term"], "meaning": t.get("detail") or t["text"], "bucket": t.get("bucket")})
            known.add(t["lead_term"].lower())
    lines = [f"# Team terms — {team.get('name', team.get('id', ''))}\n"]
    lines += [f"- **{t['term']}** ({dash(t.get('bucket'))}): {dash(t.get('meaning'))}" for t in terms] or ["- —"]
    (p.parent / "team-terms.md").write_text("\n".join(lines) + "\n")

    # Write derived completeness back so the JSON stays truthful
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False))

    print(f"Wrote prework.md, stickies.csv, team-terms.md to {p.parent}")
    print(f"{len(items)} items: " + ", ".join(
        f"{sum(1 for i in items if i['type'] == t)} {t}" for t in sorted(TYPES)))
    if problems:
        print("\nCheck these before submitting:")
        for pr in problems:
            print(f"  - {pr}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
