#!/usr/bin/env python3
"""Merge all prework.json submissions into combined.json + merge-report.md.

Usage: python3 merge.py <submissions-folder> <output-folder>
Finds every prework.json under the submissions folder (any depth).
Standard library only.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path

TYPES = ["need", "outcome", "tool", "barrier", "shared_ask"]
STOP = set("a an the to of for and or in on with our we is are it be by from that this at as".split())


def norm(t):
    return " ".join(w for w in re.findall(r"[a-z0-9]+", (t or "").lower()) if w not in STOP)


def sim(a, b):
    return SequenceMatcher(None, norm(a), norm(b)).ratio()


def main(src, dst):
    src, dst = Path(src).expanduser(), Path(dst).expanduser()
    dst.mkdir(parents=True, exist_ok=True)
    subs, invalid = [], []
    for f in sorted(src.rglob("prework.json")):
        try:
            d = json.loads(f.read_text())
            if not (d.get("team") or {}).get("id"):
                raise ValueError("team.id missing")
            subs.append((f, d))
        except Exception as e:  # noqa: BLE001
            invalid.append((f, str(e)))

    items, teams = [], {}
    for f, d in subs:
        tid = d["team"]["id"]
        if tid in teams:
            invalid.append((f, f"second submission for team {tid}; kept the first"))
            continue
        teams[tid] = {**d["team"], "confirmed": d.get("session", {}).get("confirmed", False),
                      "open_items": d.get("open_items", []), "terms": d.get("terms", [])}
        for it in d.get("items", []):
            it = dict(it)
            it["team"] = tid
            c = it.get("completeness") or {}
            rank = it.get("rank")
            it["weight"] = (6 - rank if isinstance(rank, int) and 1 <= rank <= 5 else 0) + sum(bool(v) for v in c.values())
            items.append(it)

    by_id = {i["id"]: i for i in items}
    linked_targets = {l for i in items for l in (i.get("links") or [])}
    for i in items:
        if i["type"] == "need":
            has = any(by_id.get(l, {}).get("type") == "outcome" for l in i.get("links") or []) or any(
                o["type"] == "outcome" and i["id"] in (o.get("links") or []) for o in items)
            i["needs_outcome"] = not has

    # Likely duplicates, across and within teams, per type
    dups = []
    for t in TYPES:
        pool = [i for i in items if i["type"] == t]
        for a_idx in range(len(pool)):
            for b_idx in range(a_idx + 1, len(pool)):
                a, b = pool[a_idx], pool[b_idx]
                s = sim(a.get("text"), b.get("text"))
                if t == "tool":
                    s = max(s, sim(a.get("lead_term"), b.get("lead_term")))
                if s >= 0.6:
                    dups.append((round(s, 2), t, a, b))
    dups.sort(key=lambda x: -x[0])

    combined = {"teams": teams, "items": items}
    (dst / "combined.json").write_text(json.dumps(combined, indent=2, ensure_ascii=False))

    r = ["# Merge report\n", f"- Submissions merged: **{len(teams)}** ({', '.join(sorted(teams))})"]
    unconfirmed = [t for t, v in teams.items() if not v["confirmed"]]
    if unconfirmed:
        r.append(f"- Not confirmed at read-back: {', '.join(unconfirmed)}")
    if invalid:
        r.append("- Problems:")
        r += [f"  - `{f}`: {e}" for f, e in invalid]
    r.append("\n## Counts by team and type\n")
    counts = defaultdict(Counter)
    for i in items:
        counts[i["team"]][i["type"]] += 1
    for tid in sorted(counts):
        r.append(f"- **{tid}**: " + ", ".join(f"{counts[tid][t]} {t}" for t in TYPES))
    tiers = Counter(i.get("tier_guess") or "none" for i in items)
    buckets = Counter(i.get("bucket") or "none" for i in items if i["type"] == "tool")
    hub = Counter(i.get("hub_status") or "none" for i in items if i["type"] in ("tool", "shared_ask"))
    r.append("\n## Distributions\n")
    r.append("- Tier guesses: " + ", ".join(f"{k} {v}" for k, v in tiers.most_common()))
    r.append("- Tool buckets: " + ", ".join(f"{k} {v}" for k, v in buckets.most_common()))
    r.append("- Hub status: " + ", ".join(f"{k} {v}" for k, v in hub.most_common()))
    r.append("\n## Needs missing an outcome\n")
    r += [f"- {i['id']}: {i['text']}" for i in items if i.get("needs_outcome")] or ["- none"]
    r.append("\n## Likely duplicates (text similarity ≥ 0.6, check by hand)\n")
    r += [f"- {s} · {t}: `{a['id']}` {a.get('lead_term') or a['text']!r} ≈ `{b['id']}` {b.get('lead_term') or b['text']!r}"
          for s, t, a, b in dups[:60]] or ["- none"]
    r.append("\n## Exists, not adopted\n")
    r += [f"- {i['id']}: {i['text']} — {i.get('detail') or ''}" for i in items if i.get("hub_status") == "exists_not_adopted"] or ["- none"]
    (dst / "merge-report.md").write_text("\n".join(r) + "\n")
    print(f"Merged {len(teams)} submissions, {len(items)} items -> {dst}")
    if invalid:
        print(f"{len(invalid)} problem(s); see merge-report.md")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    sys.exit(main(sys.argv[1], sys.argv[2]))
