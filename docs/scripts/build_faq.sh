#!/usr/bin/env bash
# NOTICE: This file was modified by an LLM coding system
# Builds a Markdown-based FAQ page (avoids using Jekyll for the rest of the site)

set -euo pipefail

# Inputs are relative to the docs/scripts working directory.
INPUT="../faq.md"
TEMPLATE="../_layouts/faq-pandoc.html"
OUTPUT="../faq.html"

# Show build time
CREATED_DISPLAY="$(TZ=America/Chicago date '+%B %-d, %Y at %H:%M %Z')"

# Prefer a standalone Pandoc installation (Quarto's bundled Pandoc as fallback)
if command -v pandoc >/dev/null 2>&1; then
  PANDOC=(pandoc)
elif command -v quarto >/dev/null 2>&1; then
  PANDOC=(quarto pandoc)
else
  echo "Error: pandoc or quarto is required to build the FAQ." >&2
  exit 1
fi

# Render the Markdown source into static HTML file, uploaded by GitHub Pages.
"${PANDOC[@]}" "$INPUT" \
  --from markdown+smart \
  --template "$TEMPLATE" \
  --standalone \
  --metadata "created_display=$CREATED_DISPLAY" \
  --output "$OUTPUT"

echo "Wrote $OUTPUT"
