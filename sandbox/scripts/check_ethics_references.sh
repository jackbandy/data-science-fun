#!/usr/bin/env bash
# NOTICE: This file was modified by an LLM coding system
# Validates the ethics-in-data-science bibliography with RefChecker.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
INPUT="$REPO_ROOT/../docs/ethics-in-data-science/references.bib"
UV_CACHE_DIR="${UV_CACHE_DIR:-${TMPDIR:-/tmp}/uv-cache}"

if [[ ! -f "$INPUT" ]]; then
  echo "Error: bibliography file not found: $INPUT" >&2
  exit 1
fi

if ! command -v uv >/dev/null 2>&1; then
  echo "Error: uv is not installed or not on PATH." >&2
  echo "  Install it with: curl -LsSf https://astral.sh/uv/install.sh | sh" >&2
  exit 127
fi

REPORT_FILE="$(mktemp "${TMPDIR:-/tmp}/ethics-references-refchecker.XXXXXX.json")"
trap 'rm -f "$REPORT_FILE"' EXIT

mkdir -p "$UV_CACHE_DIR"

echo "Using: uv (cache: $UV_CACHE_DIR)"

UV_CACHE_DIR="$UV_CACHE_DIR" \
  uv run --isolated --no-project --with academic-refchecker academic-refchecker \
  --paper "$INPUT" \
  --report-file "$REPORT_FILE" \
  --report-format json

python3 - "$REPORT_FILE" <<'PY'
import json
import sys
from pathlib import Path

report_path = Path(sys.argv[1])
data = json.loads(report_path.read_text())
summary = data.get("summary", {})

total_refs = summary.get("total_references_processed", 0)
total_errors = summary.get("total_errors_found", 0)
total_warnings = summary.get("total_warnings_found", 0)
total_unverified = summary.get("total_unverified_refs", 0)
flagged_records = summary.get("flagged_records", 0)
flagged_papers = summary.get("flagged_papers", 0)

print(
  "Summary: "
  f"{total_refs} references, "
  f"{total_errors} errors, "
  f"{total_warnings} warnings, "
  f"{total_unverified} unverified, "
  f"{flagged_records} flagged records, "
  f"{flagged_papers} flagged papers"
)

if any(
  count > 0
  for count in (
    total_errors,
    total_warnings,
    total_unverified,
    flagged_records,
    flagged_papers,
  )
):
  sys.exit(1)
PY
