#!/usr/bin/env bash
# Installs the XLT pre-work skills into ~/.claude/skills/
# Run from the unzipped folder:  bash install.sh
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
DEST="$HOME/.claude/skills"
mkdir -p "$DEST"
for s in xlt-prework facilitating outcome-modeling; do
  if [ -d "$DEST/$s" ]; then
    mv "$DEST/$s" "$DEST/$s.backup-$(date +%Y%m%d%H%M%S)"
  fi
  cp -R "$HERE/$s" "$DEST/$s"
done
mkdir -p "$HOME/xlt-prework"
echo "Installed. Open Claude Code and type:  /xlt-prework"
