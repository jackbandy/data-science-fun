# Test Plan for data-science-fun

<!-- NOTICE: This file was drafted by an LLM coding system on 2026-07-02. -->

A plan for basic automated checks in GitHub Actions to keep the repo — especially student-facing materials (syllabus, slides, worksheets, ethics book, FAQ) — stable, accessible, and fast.

## Guiding principles

- **Test the built site as well as the sources.** Students will use `docs/` (via dodatascience.fun), so most checks should run against rendered HTML/PDF output.
- **Split checks into two tiers:**
  - **Blocking** (fail the PR/push): broken builds, broken internal links, missing student-facing artifacts. These are "a student hits a 404" problems.
  - **Advisory** (report but don't block, at least initially): accessibility audits, performance budgets, external-link rot. These need human judgment and would otherwise cause alert fatigue.
- **Start advisory, promote to blocking.** Run each new check in report-only mode for a few weeks; once the baseline is clean, flip it to required.

## Proposed workflows

### 1. `site-checks.yml` — link integrity + artifact presence (blocking)

Runs on: every push/PR touching `docs/**`, plus a weekly cron (to catch external link rot without blocking anyone's push).

**a. Internal link check — [lychee](https://github.com/lycheeverse/lychee)** (Rust, MIT; has an official action `lycheeverse/lychee-action`).

- Check all links in `docs/**/*.html` and `docs/**/*.md` with `--offline` mode for internal links on push/PR — fast, deterministic, no network flakiness.
- The weekly cron run drops `--offline` to also verify external links (syllabus policy links, dataset sources, reading links in slides). External failures open a GitHub issue (lychee-action supports this) rather than failing the build.
- Exclusions to configure up front: `localhost`, DOI redirects that block bots, and anything behind UIC login.

**b. Student-facing artifact presence (simple shell script)**

The deploy workflow can silently ship a `docs/` that's missing rendered output (e.g., a cache restore gone wrong, or the PDF step failing non-blockingly). A small script asserts the contract:

- `docs/syllabus/index.html` and `docs/syllabus/syllabus.pdf` exist and are non-empty (say, > 10 KB for the PDF).
- For every `docs/slides/weekN.qmd` / `weekN.md` source, a matching `weekN.html` exists. Report (advisory) when `weekN.pdf` is missing, since PDF export is already treated as best-effort in `deploy-pages.yml`.
- `docs/index.html`, `docs/faq.html`, and the ethics book landing page exist.
- No build cruft shipped: fail if `.venv/`, `.quarto/`, or `.DS_Store` appear in the upload (mirrors the prune step, but as a check instead of a hope).

**c. Syllabus/schedule consistency**

`syllabus_source/sync_schedule.py` keeps `schedule.csv` and `schedule.md` in sync. Add a check that runs it in a dry-run/`--no-render` mode and fails if it would produce changes — i.e., someone edited one file and forgot to regenerate. This catches the classic "syllabus says week 5, schedule says week 6" drift before students see it.

### 2. `accessibility.yml` — a11y audit of built pages (advisory → blocking)

Student materials should meet WCAG 2.1 AA; UIC also has institutional accessibility obligations, so this is worth real investment.

**Tool: [pa11y-ci](https://github.com/pa11y/pa11y-ci)** (open source, uses axe-core and/or HTML_CodeSniffer under the hood) against the built `docs/` served locally (`python -m http.server` in the workflow — no deploy needed).

- Page list to audit: landing page, syllabus HTML, FAQ, ethics book chapters, and each slide deck's HTML.
- Reveal.js decks need special handling: audit with `pa11y --runner axe` and expect noise from off-screen slides. Start with a scoped ruleset — color contrast, image alt text, heading order, document language — rather than the full WCAG set.
- **Highest-value early wins to enforce:**
  - every `<img>` has meaningful `alt` text (slides are image-heavy; hand-drawn exercises especially need descriptions),
  - color contrast on the custom slide theme (`docs/slides/shared/theme/`) and `syllabus.css`,
  - `<html lang="en">` present on all generated pages (worth verifying the pandoc and Quarto templates emit it).
- PDFs: automated PDF/UA checking is weak everywhere; as a proxy, keep the HTML versions canonical and label PDFs as "print version" on the site. (A future manual pass with [veraPDF](https://verapdf.org/) is the open-source option if PDF accessibility becomes a requirement.)

### 3. `performance.yml` — speed budget (advisory)

Slides and the landing page should load fast on a phone on campus wifi.

**Tool: [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci)** — it is Google-authored but fully open-source, self-hosted in CI, and phones home to nothing when used with `--upload.target=filesystem` or temporary public storage disabled. If avoiding Google projects entirely is preferred, the leaner alternative is a **page-weight budget script**: fail if any student-facing HTML page plus its local assets exceeds a size budget (e.g., 3 MB per slide deck).

- Run against locally-served `docs/` on PRs that touch `docs/**`.
- Budgets to start with (loose, then tighten):
  - Performance score ≥ 80 on landing page and syllabus.
  - Total transfer per slide deck ≤ ~5 MB (decks embed images; `weekN_files/` directories are the thing to watch).
  - No single image over ~500 KB — a simple `find docs -name '*.png' -size +500k` check is a good zero-dependency companion, pointing at candidates for compression (e.g., `oxipng`/`cwebp`, both open source).

### 4. `build-checks.yml` — source hygiene (blocking, cheap)

Fast checks on push/PR, no site build required:

- **Quarto/YAML sanity:** `quarto check` and a YAML lint of `_quarto.yml`, `_metadata.yml`, and workflow files (`yamllint`).
- **Notebook execution (optional, heavier):** the `weekN.ipynb` files are student-downloadable; a matrix job running `jupyter nbconvert --execute` on changed notebooks catches broken code before students do. Gate it on changed files only, since executing all decks each push is slow.
- **Shell scripts:** `shellcheck` on `build_all_quarto.sh`, `build_syllabus_from_markdown.sh`, `worksheets_source/build.sh`.
- **Spell check (advisory):** [typos](https://github.com/crate-ci/typos) (Rust, MIT) on `*.qmd`, `*.md` sources — it's conservative by design, so false positives are rare. Student-facing typos are cheap to prevent here.

## Suggested rollout order

1. **Artifact presence + internal links** (workflow 1a/1b) — biggest stability win, trivial to implement, immediately blocking.
2. **Schedule consistency check** (1c) — small script, protects the single most date-sensitive student document.
3. **Shellcheck + yamllint + typos** (4) — near-zero maintenance.
4. **Accessibility audit, advisory mode** (2) — expect an initial cleanup pass (alt text, contrast) before making it required.
5. **External link cron + performance budgets** (1a-cron, 3) — advisory indefinitely; review the weekly issue/report.

## Notes / open questions

- The deploy workflow's slide cache (`restore-keys: slides-`) can serve stale decks if the render step is skipped incorrectly; workflow 1b's "source has matching HTML" check is deliberately downstream of that cache logic and would catch a fully missing deck, but not a *stale* one. If staleness becomes a problem, embed the source git hash in rendered HTML (via `postprocess_slides.py`) and compare.
- The deploy workflow already has a TODO about verifying `weekN.ipynb` files are reachable on the deployed site — fold that into the artifact-presence script.
- Decide whether checks should run against the `docs/` tree as committed (fast, tests what's in git) or a fresh render (slow, tests the build). Recommendation: committed tree for the checks above, since the deploy workflow itself is the render test; a scheduled full-render job could be added later as a canary.
