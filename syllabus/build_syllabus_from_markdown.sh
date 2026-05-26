#!/usr/bin/env bash
# NOTICE: This file modified by an LLM coding system on 2026-05-26.

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INPUT_MD="${1:-$ROOT_DIR/syllabus.md}"
OUT_DIR="${2:-$ROOT_DIR/../docs/syllabus}"

mkdir -p "$OUT_DIR"

BASE_NAME="$(basename "$INPUT_MD")"
BASE_NAME="${BASE_NAME%.*}"

PDF_OUT="$OUT_DIR/syllabus.pdf"
HTML_OUT="$OUT_DIR/index.html"
CSS_OUT="$OUT_DIR/syllabus.css"
LOGO_PDF_OUT="$OUT_DIR/uic-black-logo.pdf"
LOGO_SVG_OUT="$OUT_DIR/uic-black-logo.svg"

# America/Chicago local timestamp (24h)
CREATED_TS="$(TZ=America/Chicago date '+%m/%d/%Y, %H:%M')"

# UIC brand guidance prefers Theinhardt; use Arial when the licensed font is unavailable.
MAIN_FONT="Arial"
if command -v fc-list >/dev/null 2>&1; then
  if fc-list 2>/dev/null | rg -qi '(^|[: ])Theinhardt'; then
    MAIN_FONT="Theinhardt"
  fi
fi

# Copy CSS next to HTML for GitHub Pages
cp "$ROOT_DIR/syllabus.css" "$CSS_OUT"

# Build a PDF logo from the repo's SVG (for LaTeX header)
LOGO_SVG_SRC="$ROOT_DIR/../docs/images/uic-black-logo.svg"
if [[ -f "$LOGO_SVG_SRC" ]]; then
  cp "$LOGO_SVG_SRC" "$LOGO_SVG_OUT"
  if command -v rsvg-convert >/dev/null 2>&1; then
    rsvg-convert -f pdf -o "$LOGO_PDF_OUT" "$LOGO_SVG_SRC"
  else
    echo "Error: rsvg-convert not found (needed to convert $LOGO_SVG_SRC to PDF)." >&2
    exit 1
  fi
else
  echo "Error: logo SVG not found at $LOGO_SVG_SRC" >&2
  exit 1
fi

pandoc "$INPUT_MD" \
  --from markdown+smart \
  --lua-filter "$ROOT_DIR/filters/underline.lua" \
  --template "$ROOT_DIR/pandoc-syllabus-template.tex" \
  --pdf-engine=xelatex \
  --metadata created="$CREATED_TS" \
  --metadata logo_pdf="$LOGO_PDF_OUT" \
  --metadata main_font="$MAIN_FONT" \
  --resource-path "$ROOT_DIR" \
  -V secnumdepth=0 \
  -o "$PDF_OUT"

pandoc "$INPUT_MD" \
  --from markdown+smart \
  --lua-filter "$ROOT_DIR/filters/underline.lua" \
  --template "$ROOT_DIR/syllabus_html_template.html" \
  --standalone \
  --metadata created="$CREATED_TS" \
  --toc \
  -o "$HTML_OUT"

echo "Wrote:"
echo "  $PDF_OUT"
echo "  $HTML_OUT"
