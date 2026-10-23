# Slides

or the build pipeline details, deck conventions, `sync_slide_index.py` rules, and the theme, etc., see the **Slide build** section of the [main README](../../README.md).

Prereqs: Quarto (`brew install --cask quarto`), Python 3.12, [uv](https://docs.astral.sh/uv/). PDFs also need Node ≥ 22 + Chrome; `week5.qmd` also needs R (`Rscript`).

## Build

Use the build script, not a bare `quarto render` — the script syncs `.venv` (Python 3.12) to `shared/requirements.lock`, points `QUARTO_PYTHON` at it, stamps the compile time, and syncs `index.html`.

After editing `shared/requirements.txt` or bumping the Yard's `jupyterlite-pyodide-kernel` pin (`docs/yard/requirements.txt`), run `shared/lock_requirements.sh` to rewrite `shared/pyodide-pins.txt` and `shared/requirements.lock`, and commit all three files.

```bash
cd docs/slides
shared/build_all_quarto.sh                              # every deck, HTML only
RENDER_SLIDES="week3.qmd" shared/build_all_quarto.sh    # just one deck
BUILD_PDFS=true shared/build_all_quarto.sh              # also export PDFs
```

Env vars: `RENDER_SLIDES` (space-separated filenames), `BUILD_PDFS`, `SKIP_HTML=true` (PDF-only from existing HTML), `SKIP_VENV=true` (use the active Python env; CI uses this), `QUARTO_CMD`, `CHROME`.

## Render one deck by hand

```bash
cd docs/slides
uv venv --python 3.12 .venv
uv pip sync --python .venv shared/requirements.lock
QUARTO_PYTHON="$PWD/.venv/bin/python3" quarto render week3.qmd --to revealjs
python3 shared/sync_slide_index.py .                    # required, or repo-checks.yml fails on index drift
```

Most render failures (`Unable to locate an installed version of Python`, `Jupyter kernel not found`, `ModuleNotFoundError` for `polars`/`seaborn`/`plotnine`/`pymc`) mean Quarto picked the wrong interpreter — set `QUARTO_PYTHON` as above, or just use the build script.
