#!/usr/bin/env bash
# NOTICE: This file modified by an LLM coding system on 2026-05-26.

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INPUT_MD="${1:-$ROOT_DIR/syllabus.md}"
OUT_DIR="${2:-$ROOT_DIR/../docs/syllabus}"

python3 "$ROOT_DIR/sync_schedule.py" --no-render

mkdir -p "$OUT_DIR"

BASE_NAME="$(basename "$INPUT_MD")"
BASE_NAME="${BASE_NAME%.*}"

PDF_OUT="$OUT_DIR/syllabus.pdf"
HTML_OUT="$OUT_DIR/index.html"

# America/Chicago local timestamp (24h)
CREATED_TS="$(TZ=America/Chicago date '+%m/%d/%Y, %H:%M')"
SYLLABUS_CSS="$(<"$ROOT_DIR/syllabus.css")"

# UIC brand guidance prefers Theinhardt; use Arial when the licensed font is unavailable.
MAIN_FONT="Arial"
if command -v fc-list >/dev/null 2>&1; then
  if fc-list 2>/dev/null | rg -qi '(^|[: ])Theinhardt'; then
    MAIN_FONT="Theinhardt"
  fi
fi

# Build a temporary PDF logo for the LaTeX header.
LOGO_SVG_SRC="$ROOT_DIR/../docs/images/uic-black-logo.svg"
LOGO_PDF_OUT="$(mktemp "${TMPDIR:-/tmp}/uic-black-logo.XXXXXX.pdf")"
trap 'rm -f "$LOGO_PDF_OUT"' EXIT
if [[ -f "$LOGO_SVG_SRC" ]]; then
  if command -v rsvg-convert >/dev/null 2>&1; then
    rsvg-convert -f pdf -o "$LOGO_PDF_OUT" "$LOGO_SVG_SRC"
  elif command -v magick >/dev/null 2>&1; then
    magick "$LOGO_SVG_SRC" "$LOGO_PDF_OUT"
  else
    echo "Error: rsvg-convert or magick is required to convert $LOGO_SVG_SRC to PDF." >&2
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
  --variable "syllabus_css=$SYLLABUS_CSS" \
  --metadata created="$CREATED_TS" \
  --toc \
  -o "$HTML_OUT"

echo "Wrote:"
echo "  $PDF_OUT"
echo "  $HTML_OUT"
