# Contributing to this Repo

Thanks for your interest in contributing! This repo holds the materials for a section of CS 418 (Intro to Data Science) at UIC — slides, worksheets, the syllabus, and the ethics mini-book.

## Before you start

If you're fixing a typo, correcting a fact, repairing a broken link, or improving an explanation, go right ahead.

If you want to make a larger change, consider opening a GitHub issue first.

**Note:** contributions are especially welcome from people using these materials — i.e. students in the course and TAs. Mention this in your issue or pull request.

## Setup

[Fork the repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo), then clone your fork.

What you need depends on what you're editing:

| Editing | You need |
| --- | --- |
| Slides (`docs/slides/week*.qmd`) | [Quarto](https://quarto.org/docs/get-started/) |
| Ethics mini-book (`docs/ethics-in-data-science/`) | Quarto |
| Site pages, FAQ, schedule | Ruby + Bundler (for Jekyll) |
| Syllabus (`syllabus_source/`) | `pandoc`, `xelatex`, `rsvg-convert` |
| Worksheets (`worksheets_source/`) | LaTeX |

Prose-only fixes usually need none of this — GitHub's web editor is fine.

## Development

Preview the site:

```bash
cd docs
bundle install          # first time only
bundle exec jekyll serve # http://localhost:4000
```

Build the slides:

```bash
cd docs/slides
./build_all_quarto.sh                   # HTML only
BUILD_PDFS=true ./build_all_quarto.sh   # include PDFs
```

Quarto output (slides, mini-book) is served as-is, so `quarto preview` works for those.

A few conventions worth knowing before you edit:

- **The `.qmd` is the slide source.** Don't edit `docs/slides/week*.html` (it is generated and gitignored)
- **Parts of `docs/slides/index.html` are generated.** The per-deck bullets and the slide-count table are written by `docs/slides/sync_slide_index.py`. To change a topic's wording, edit that deck's `{.section-header}` heading, and it will get propagated.
- **The schedule lives in just one place:** `docs/_data/schedule.csv`. Both the homepage table and the syllabus read from it.
- **Check citations against a primary source.** For anything with a DOI, `https://api.crossref.org/works/<doi>`; otherwise the publisher or proceedings page.

## Opening a pull request

We follow [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow):

- Work on a branch, not `main`, and start from a recent `main`
- Use meaningful commit messages — `fix week 4 histogram axis label`, not `fix`.
- In the PR description, say what changed and why.
- If you used an LLM to write a significant part of the change, please disclose it. This repo tracks that deliberately: LLM-modified files carry a `NOTICE:` header, and `sandbox/` is intended as a quarantine for LLM-generated and experimental work.
	- See the "Note on LLM use" section of the [README](README.md) for more details
- Link any issue your PR resolves so it closes on merge.

The checks in `.github/workflows/repo-checks.yml` run on every PR: the slide index generator must match what's committed, Python and shell scripts must pass a lint for real errors, and no new duplicate files under `docs/`. These are currently non-blocking but please look at the output.

## After your change is merged

Woohoo! Thanks for contributing! Your GitHub profile should now show up under the 'Contributors' portion of the repo page.

Pushes to `main` that touch `docs/` or `syllabus_source/` trigger `.github/workflows/deploy-pages.yml`, which renders the Quarto decks and mini-book, builds the syllabus, runs Jekyll, and publishes to [dodatascience.fun](https://dodatascience.fun/). It's usually live a few minutes after the merge.

