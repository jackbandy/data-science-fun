#!/usr/bin/env bash
# NOTICE: This file modified by an LLM coding system on 2026-07-26.

set -euo pipefail

SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="$SOURCE_DIR/../docs/syllabus"
INPUT="$SOURCE_DIR/syllabus.md"
LOGO_SVG="$SOURCE_DIR/../docs/assets/branding/uic-black-logo.svg"
CREATED="$(TZ=America/Chicago date '+%m/%d/%Y, %H:%M')"

for command in pandoc xelatex rsvg-convert python3; do
  if ! command -v "$command" >/dev/null 2>&1; then
    echo "Error: $command is required to build the syllabus." >&2
    exit 1
  fi
done

python3 "$SOURCE_DIR/sync_schedule.py"

mkdir -p "$OUTPUT_DIR"

# UIC brand guidance prefers Theinhardt; use Arial when the licensed font is absent.
MAIN_FONT="Arial"
if fc-list 2>/dev/null | grep -qi theinhardt; then
  MAIN_FONT="Theinhardt"
fi

# The LaTeX header needs the logo as a PDF; the SVG stays the single source.
LOGO_PDF="$(mktemp "${TMPDIR:-/tmp}/uic-black-logo.XXXXXX.pdf")"
trap 'rm -f "$LOGO_PDF"' EXIT
rsvg-convert -f pdf -o "$LOGO_PDF" "$LOGO_SVG"

pandoc "$INPUT" \
  --from markdown+smart \
  --lua-filter "$SOURCE_DIR/underline.lua" \
  --template "$SOURCE_DIR/template.tex" \
  --pdf-engine=xelatex \
  --metadata created="$CREATED" \
  --metadata logo_pdf="$LOGO_PDF" \
  --metadata main_font="$MAIN_FONT" \
  --resource-path "$SOURCE_DIR" \
  -o "$OUTPUT_DIR/syllabus.pdf"

pandoc "$INPUT" \
  --from markdown+smart \
  --lua-filter "$SOURCE_DIR/underline.lua" \
  --template "$SOURCE_DIR/template.html" \
  --standalone \
  --metadata created="$CREATED" \
  -o "$OUTPUT_DIR/index.html"

echo "Published $OUTPUT_DIR/index.html"
echo "Published $OUTPUT_DIR/syllabus.pdf"
