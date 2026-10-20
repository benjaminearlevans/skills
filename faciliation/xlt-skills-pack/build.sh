#!/usr/bin/env bash
# Syncs shared references into every skill and rebuilds both zips.
# Run from the pack root:  bash build.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
for s in participant/xlt-prework participant/outcome-modeling organizer/xlt-synthesize organizer/xlt-board organizer/xlt-readback; do
  mkdir -p "$s/references"
  cp shared/reference-pack.md shared/schema.md shared/config.md "$s/references/"
done
rm -rf organizer/outcome-modeling
cp -R participant/outcome-modeling organizer/outcome-modeling
mkdir -p dist
rm -f dist/xlt-prework.zip dist/xlt-organizer.zip
(cd participant && zip -qr ../dist/xlt-prework.zip README.md install.sh xlt-prework facilitating outcome-modeling -x '*/__pycache__/*')
(cd organizer && zip -qr ../dist/xlt-organizer.zip README.md xlt-synthesize xlt-board xlt-readback outcome-modeling test-fixtures -x '*/__pycache__/*')
echo "Built dist/xlt-prework.zip and dist/xlt-organizer.zip"
