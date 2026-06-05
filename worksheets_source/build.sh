#!/usr/bin/env bash
# Compiles all worksheet.tex files and copies PDFs to docs/worksheets/.
# Run from anywhere in the repo: ./worksheets_source/build.sh

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PDF_OUT="$REPO_ROOT/docs/worksheets"

if ! command -v latexmk &>/dev/null; then
  echo "Error: latexmk not found."
  echo "  macOS:  brew install --cask mactex"
  echo "  Linux:  sudo apt install latexmk"
  exit 1
fi

SUCCESS=0
FAIL=0

for tex_file in "$SCRIPT_DIR"/*/worksheet.tex; do
  folder_name="$(basename "$(dirname "$tex_file")")"
  tex_dir="$(dirname "$tex_file")"
  pdf_name="${folder_name}.pdf"

  echo ""
  echo "[$folder_name]"

  # Run latexmk from within the worksheet directory so state files stay consistent
  (
    cd "$tex_dir"
    latexmk -C worksheet.tex &>/dev/null
    echo "  Cleared any previous build artifacts"

    latexmk -pdf -f -interaction=nonstopmode -halt-on-error worksheet.tex &>/dev/null || exit 1
    echo "  Compiled worksheet.tex successfully"

    # Check page count
    page_count=$(pdfinfo worksheet.pdf 2>/dev/null | grep "Pages:" | awk '{print $2}' || echo "0")
    if [[ $page_count -gt 2 ]]; then
      echo "  📄 WARNING: PDF is $page_count pages (expected ≤ 2)"
    fi

    mkdir -p "$PDF_OUT"
    cp worksheet.pdf "$PDF_OUT/$pdf_name"
    echo "  Copied to $PDF_OUT/$pdf_name"

    latexmk -C worksheet.tex &>/dev/null
    echo "  Cleared auxiliary files"
  )

  if [[ $? -eq 0 ]]; then
    ((SUCCESS++))
  else
    echo "  ERROR: compilation failed. Re-running with full output:" >&2
    (cd "$tex_dir" && latexmk -pdf -f -interaction=nonstopmode worksheet.tex) >&2 || true
    ((FAIL++))
  fi
done

echo ""
echo "Done: $SUCCESS compiled, $FAIL failed."
[[ $FAIL -eq 0 ]]
