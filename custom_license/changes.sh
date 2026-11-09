#!/usr/bin/env bash
# Regenerate CHANGES.txt: a word-level diff of LICENSE.txt against the version
# in the last commit. Before LICENSE.txt has ever been committed, the baseline
# is openrail_template.txt (the unmodified OpenRAIL template, note header
# excluded). Run from anywhere:  custom_license/changes.sh
set -u
cd "$(dirname "$(readlink -f "$0")")"

tmp=$(mktemp); trap 'rm -f "$tmp"' EXIT
if git cat-file -e HEAD:custom_license/LICENSE.txt 2>/dev/null; then
    git show HEAD:custom_license/LICENSE.txt > "$tmp"
    base="LICENSE.txt as committed in $(git log -1 --format='%h (%ad, "%s")' --date=short -- LICENSE.txt)"
else
    awk 'c>=2 {print; next} /^={80}$/ {c++; next}' openrail_template.txt | sed '1{/^$/d}' > "$tmp"
    base="openrail_template.txt (unmodified OpenRAIL template, note header excluded)"
fi

diff=$(git diff --no-index --word-diff=plain -U2 "$tmp" LICENSE.txt \
       | sed '1,/^+++ /d' \
       | sed -E 's/^@@ -([0-9]+)[^@]*@@ ?(.*)$/---- line \1 ---- \2/')
{
    printf 'Changes in LICENSE.txt relative to: %s\n' "$base"
    printf 'Generated %s by changes.sh. Markup: [-removed-] {+added+}\n\n' "$(date -I)"
    if [ -n "$diff" ]; then printf '%s\n' "$diff"; else echo "(no changes)"; fi
} > CHANGES.txt
echo "wrote $(pwd)/CHANGES.txt"
