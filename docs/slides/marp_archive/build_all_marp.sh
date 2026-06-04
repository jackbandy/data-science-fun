#!/usr/bin/env bash
set -euo pipefail

# build_all_marp.sh — compile all slide .md files to HTML and PDF using Marp CLI
# Usage: ./build_all_marp.sh [output-dir]
# If MARP_CMD environment variable is set, it will be used as the marp CLI command.
# Otherwise the script prefers a locally installed 'marp' binary, falling back to 'npx @marp-team/marp-cli'.
# Set BUILD_PDFS=false to render HTML only.

OUTPUT_DIR=${1:-.}
BUILD_PDFS="${BUILD_PDFS:-true}"

# Resolve paths relative to this script's location
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CONFIG_FILE="$SCRIPT_DIR/.marprc.yml"
THEME_FILE="$SCRIPT_DIR/marp-theme.css"

if [[ ! -f "$CONFIG_FILE" ]]; then
  echo "Error: Marp config not found at $CONFIG_FILE" >&2
  exit 1
fi

if [[ ! -f "$THEME_FILE" ]]; then
  echo "Error: theme file not found at $THEME_FILE" >&2
  exit 1
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
echo "Using Marp config: $CONFIG_FILE"
echo "Using Marp theme: $THEME_FILE"

if [[ -n "${MARP_BROWSER_PATH:-}" ]]; then
  echo "Using Marp browser: $MARP_BROWSER_PATH"
fi

run_marp() {
  if [[ -n "${MARP_BROWSER_PATH:-}" ]]; then
    $MARP_CMD --browser-path "$MARP_BROWSER_PATH" "$@"
  else
    $MARP_CMD "$@"
  fi
}

# Gather all Marp slide markdown files under this slides directory (recursive)
# Use find + read -d '' loop for macOS bash compatibility (no mapfile, no realpath)
found=0
failed=0
cd "$SCRIPT_DIR"

while IFS= read -r -d '' md; do
  # Only build actual Marp slide sources, not notes like README.md.
  if ! grep -Eq '^marp:[[:space:]]*true([[:space:]]|$)' "$md"; then
    echo "[marp] Skipping non-slide markdown: $md"
    continue
  fi

  found=1
  # strip leading ./ from find output for relative path
  rel="${md#./}"
  out_base="$OUTPUT_DIR/${rel%.*}"
  out_dir=$(dirname "$out_base")
  mkdir -p "$out_dir"

  html_out="$out_base.html"
  pdf_out="$out_base.pdf"

  echo "[marp] Generating HTML: $html_out from $md"
  run_marp \
    --config "$CONFIG_FILE" \
    --theme-set "$THEME_FILE" \
    --allow-local-files \
    "$md" \
    -o "$html_out" \
    </dev/null || { echo "HTML generation failed for $md" >&2; failed=1; continue; }

  if [[ "$BUILD_PDFS" != "false" ]]; then
    echo "[marp] Generating PDF: $pdf_out from $md"
    run_marp \
      --config "$CONFIG_FILE" \
      --theme-set "$THEME_FILE" \
      --allow-local-files \
      --pdf \
      "$md" \
      -o "$pdf_out" \
      </dev/null || { echo "PDF generation failed for $md" >&2; failed=1; continue; }
  fi

done < <(find . -type f -name "*.md" -not -path "./node_modules/*" -print0)

if [[ $found -eq 0 ]]; then
  echo "No Marp slide markdown files found." >&2
  exit 1
fi

if [[ $failed -ne 0 ]]; then
  echo "One or more Marp slide conversions failed." >&2
  exit 1
fi

echo "All done."
