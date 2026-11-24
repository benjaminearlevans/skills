#!/usr/bin/env bash
# Builds one uploadable .plugin file per plugin into dist/.
# Run in the root of this repo:  bash scripts/build-plugins.sh
# Re-run after changing any skill, then upload the changed file again.
set -euo pipefail
cd "$(dirname "$0")/.."

# name:folder — keep in step with .claude-plugin/marketplace.json
PLUGINS=(
  "core:core"
  "strategyu-skills:strategy/strategyu-skills-claude"
  "awesome-pm-skills:product-management/awesome-pm-skills"
  "product-skills:product-management/product-skills"
  "execution-skills:product-management/execution-skills"
  "lenny-skills:product-management/lenny-skills"
)

mkdir -p dist
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
for entry in "${PLUGINS[@]}"; do
  name="${entry%%:*}"; dir="${entry#*:}"; out="$tmp/$name.plugin"
  if [ ! -f "$dir/.claude-plugin/plugin.json" ]; then
    echo "missing $dir/.claude-plugin/plugin.json" >&2; exit 1
  fi
  (cd "$dir" && zip -q -r -X "$out" . -x '*.DS_Store')
  cp "$out" "dist/$name.plugin"
  printf '%-22s %5s skills  %s\n' "$name" "$(find "$dir" -name SKILL.md | wc -l | tr -d ' ')" "$(du -h "$out" | cut -f1)"
done
echo "Built ${#PLUGINS[@]} plugin files in dist/"
