#!/usr/bin/env bash
# NOTICE: This file modified by an LLM coding system on 2026-07-26.

set -euo pipefail

SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="$SOURCE_DIR/../docs/syllabus"
INPUT="$SOURCE_DIR/syllabus.md"
LOGO_SVG="$SOURCE_DIR/../docs/assets/branding/uic-black-logo.svg"
CREATED="$(TZ=America/Chicago date '+%m/%d/%Y, %H:%M')"

for command in pandoc xelatex rsvg-convert; do
  if ! command -v "$command" >/dev/null 2>&1; then
    echo "Error: $command is required to build the syllabus." >&2
    exit 1
  fi
done

mkdir -p "$OUTPUT_DIR"

# UIC brand guidance prefers Theinhardt; Liberation Sans is the metric-compatible
# stand-in for Arial on the CI runner, which has neither of the first two.
# macOS ships no fc-list, but xelatex finds Arial through CoreText, so that is
# the fallback when we cannot enumerate fonts.
MAIN_FONT="Arial"
if command -v fc-list >/dev/null 2>&1; then
  for font in Theinhardt Arial "Liberation Sans"; do
    if fc-list 2>/dev/null | grep -qiF "$font"; then
      MAIN_FONT="$font"
      break
    fi
  done
fi
echo "Syllabus main font: $MAIN_FONT"

# The LaTeX header needs the logo as a PDF; the SVG stays the single source.
LOGO_PDF="$(mktemp "${TMPDIR:-/tmp}/uic-black-logo.XXXXXX.pdf")"
trap 'rm -f "$LOGO_PDF"' EXIT
rsvg-convert -f pdf -o "$LOGO_PDF" "$LOGO_SVG"

pandoc "$INPUT" \
  --from markdown+smart \
  --lua-filter "$SOURCE_DIR/schedule.lua" \
  --lua-filter "$SOURCE_DIR/underline.lua" \
  --lua-filter "$SOURCE_DIR/signal.lua" \
  --lua-filter "$SOURCE_DIR/indent.lua" \
  --template "$SOURCE_DIR/template.tex" \
  --pdf-engine=xelatex \
  --metadata created="$CREATED" \
  --metadata logo_pdf="$LOGO_PDF" \
  --metadata main_font="$MAIN_FONT" \
  --resource-path "$SOURCE_DIR:$OUTPUT_DIR" \
  -o "$OUTPUT_DIR/syllabus.pdf"

pandoc "$INPUT" \
  --from markdown+smart \
  --lua-filter "$SOURCE_DIR/schedule.lua" \
  --lua-filter "$SOURCE_DIR/underline.lua" \
  --lua-filter "$SOURCE_DIR/signal.lua" \
  --lua-filter "$SOURCE_DIR/indent.lua" \
  --template "$SOURCE_DIR/template.html" \
  --standalone \
  --metadata created="$CREATED" \
  -o "$OUTPUT_DIR/index.html"

echo "Published $OUTPUT_DIR/index.html"
echo "Published $OUTPUT_DIR/syllabus.pdf"
