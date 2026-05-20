#!/usr/bin/env bash
set -euo pipefail

# build_all_marp.sh — compile all .md files under this docs directory to HTML and PDF using Marp CLI
# Usage: ./build_all_marp.sh [output-dir]
# If MARP_CMD environment variable is set, it will be used as the marp CLI command.
# Otherwise the script prefers a locally installed 'marp' binary, falling back to 'npx @marp-team/marp-cli'.

OUTPUT_DIR=${1:-.}

# Resolve theme file path relative to this script's location
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
THEME_FILE="$SCRIPT_DIR/../css/marp-theme.css"
if [[ -f "$THEME_FILE" ]]; then
  THEME_ARG="--theme-set $THEME_FILE"
else
  THEME_ARG=""
  echo "Warning: theme file not found at $THEME_FILE" >&2
fi

# Find marp executable or fallback to npx
if [[ -n "${MARP_CMD:-}" ]]; then
  MARP_CMD="$MARP_CMD"
elif command -v marp >/dev/null 2>&1; then
  MARP_CMD="marp"
else
  MARP_CMD="npx --no-install @marp-team/marp-cli"
fi

echo "Using Marp command: $MARP_CMD"

# Gather all markdown files under current directory (recursive)
# Use find + read -d '' loop for macOS bash compatibility (no mapfile, no realpath)
found=0
while IFS= read -r -d '' md; do
  found=1
  # strip leading ./ from find output for relative path
  rel="${md#./}"
  out_base="$OUTPUT_DIR/${rel%.*}"
  out_dir=$(dirname "$out_base")
  mkdir -p "$out_dir"

  html_out="$out_base.html"
  pdf_out="$out_base.pdf"

  echo "[marp] Generating HTML: $html_out from $md"
  $MARP_CMD "$md" -o "$html_out" --allow-local-files $THEME_ARG || { echo "HTML generation failed for $md" >&2; continue; }

  echo "[marp] Generating PDF: $pdf_out from $md"
  $MARP_CMD "$md" --pdf -o "$pdf_out" --allow-local-files $THEME_ARG || { echo "PDF generation failed for $md" >&2; continue; }

done < <(find . -type f -name "*.md" -not -path "./node_modules/*" -print0)

if [[ $found -eq 0 ]]; then
  echo "No markdown files found." >&2
  exit 1
fi

echo "All done."