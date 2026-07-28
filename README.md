# 🪩 Data Science the Fun Way 🪩
## Materials for CS 418: Intro to Data Science
### University of Illinois Chicago (UIC)

These are in-progress materials for a section of CS 418 (Intro to Data Science) in Fall 2026. This repository is intended as the main container for reference materials, including slides, worksheets, demo code, etc. The goal is to create a library of accessible, high-quality materials, including hand-written / hand-drawn exercises, inspired by [Tom Yeh's "AI by Hand" series](https://www.byhand.ai).

Materials are under active development during Summer 2026. The public-facing site, [DoDataScience.fun](https://dodatascience.fun/), lives at the `docs/` folder, deployed via GitHub Pages.

## Repository layout

```text
data-science-fun/
├── .github/workflows/           # GitHub Actions stuff
├── docs/                        # Public-facing site root
│   ├── index.html               # Landing page
│   ├── faq.md                   # FAQ source (Jekyll renders it to /faq.html)
│   ├── _config.yml              # Jekyll config
│   ├── _data/                   # schedule.csv (the one copy) + stations.yml
│   ├── _includes/               # The one copy of the site header/nav and footer
│   ├── _layouts/default.html    # Layout for Markdown pages
│   ├── Gemfile                  # Local Jekyll preview only
│   ├── css/                     # Shared stylesheets
│   ├── slides/                  # Quarto decks and archived Marp workflow
│   ├── syllabus/                # Generated syllabus output (gitignored, built in CI)
│   ├── worksheets/              # Generated worksheet PDFs
│   ├── ethics-in-data-science/  # Quarto mini-book
│   └── CNAME                    # domain config
├── datasets/                    # Datasets used in class materials
├── syllabus_source/             # Syllabus markdown, pandoc templates, lua filters
├── worksheets_source/           # Worksheet source and build script
├── sandbox/                     # Quarantine for LLM-modified or experimental content
├── source-materials/            # Reference and upstream source files
├── NOTES.md                     # Working notes and planning
└── README.md                    # This file
```

## GitHub Actions

The goal of the setup is to make materials very portable, accessible, and **easily editable**. This usually means putting "raw content" in a markdown file somewhere, which gets assembled and served automatically any time there is a push (via GitHub Actions workflows).

Although it feels over-engineered in some cases, the setup allows quick editing of slide materials, syllabus text, and/or the mini-book. Simply edit a markdown file, commit/push the changes, and let GitHub handle the rest.

### Slide build

I'm trying to avoid Google Slides, and the current markdown-based slide workflow uses Quarto to generate Reveal.js decks in html:

```text
 [docs/slides/week0.qmd ... week12.md]
                    |
          +---------+---------+
          |                   |
          v                   v
 [Reveal.js HTML]          [PDF]
```

**Building slides:**

`deploy-pages.yml` renders the decks on every push, caching the output and re-rendering only the decks whose sources changed. HTML is required (a failure fails the deploy); the PDF export is sort of a best-effort (non-blocking if it fails). To build locally:

```bash
cd docs/slides
./build_all_quarto.sh       # HTML only (default)
BUILD_PDFS=true ./build_all_quarto.sh  # Include PDFs
```

The script generates Quarto revealjs output files (`.html` and `.pdf`) for every slide source (`.qmd` or `.md`) in the slides directory. Executable Python code is converted to Jupyter notebooks and saved in `code_from_slides/`.

**Notes:**

- The decks are `docs/slides/week0.md` through `docs/slides/week12.md`, with `.qmd` files using Quarto's extended markdown. Each file contains Quarto Reveal.js configuration.
- Each compiled deck produces an HTML file, PDF, and `_files/` support directory (containing CSS, JavaScript, and other assets).
- Quarto revealjs HTML depends on the `*_files/` directories for styles to load properly on GitHub Pages.
- Slides use SVGs and other vector formats whenever possible.
- The previous Marp experiment is archived in `docs/slides/marp_archive/`. Run `docs/slides/marp_archive/build_all_marp.sh` to rebuild its HTML and PDF outputs.
- More complicated than Google Slides? Yes. Worth it for freedom, portability, accessibility, etc.? For now, yes.

**Theme:**

The slide theme uses Big Shoulders for title headings and a Franklin-style sans stack for body and footer text. The repo self-hosts Libre Franklin from `impallari/Libre-Franklin` as the libre body-font asset used across the decks.

### Syllabus build

Again, this is somewhat over-engineered (with help from LLMs), but the result is that I can edit the schedule (in a .csv) and/or the text of the syllabus (in a .md), and the changes propagate everywhere on the next push.

Sources are in `syllabus_source/`; outputs land in `docs/syllabus/` and are gitignored, so a push is the whole workflow:

```text
push to main
     |
     v
[GitHub Actions: deploy-pages.yml]
     |
     |  1. syllabus_source/build.sh
     |       [docs/_data/schedule.csv] --(schedule.lua)--> [syllabus.md]
     |                                                          |
     |                                             +------------+------------+
     |                                             |         (pandoc)        |
     |                                             v                         v
     |                                      [template.html]           [template.tex]
     |                                             v                         v
     |                              [docs/syllabus/index.html]  [docs/syllabus/syllabus.pdf]
     |
     |  2. jekyll build docs/ -> _site/
     |       [docs/_data/schedule.csv] --(Liquid loop)--> homepage schedule table
     |       [docs/syllabus/index.html] -> masthead include expanded in place
     |
     v
[upload _site/ -> GitHub Pages]
```

- **The schedule lives in one place: `docs/_data/schedule.csv`.** Jekyll reads it as `site.data.schedule` for the homepage table; `schedule.lua` expands the empty ` ```schedule ` block in `syllabus.md` into the same rows for Pandoc.
	- There is no sync script and no generated table committed anywhere.
	- Week-to-station labels for the homepage dots are in `docs/_data/stations.yml`.
- The text source is `syllabus_source/syllabus.md`. Its YAML block holds the header (course title, college, credit hours); the templates render it. `underline.lua` handles its `[...]{.underline}` spans.
- The build needs `pandoc`, `xelatex`, and `rsvg-convert`. The workflow apt-installs them and caches `docs/syllabus/`, so unrelated pushes skip the TeX Live install and keep the existing "created" timestamp.
- The UIC logo comes from `docs/assets/branding/uic-black-logo.svg`, converted to PDF for the LaTeX header at build time.
- Both templates currently have a WORK IN PROGRESS watermark: `AddToShipoutPictureBG` in `template.tex`, `body::before` in `template.html`.
- To preview locally, run `syllabus_source/build.sh` before `jekyll serve` — a fresh clone will have no `docs/syllabus/` until running the build script

### Worksheet build

Still early, but worksheet LaTeX sources and build support live in `worksheets_source/`.

- Run `worksheets_source/build.sh` to compile every `worksheet.tex`.
- Compiled PDFs are published under `docs/worksheets/`.
- Source directories do not retain generated worksheet PDFs.

### Quarto mini-book build

The Quarto mini-book for "Ethics in Data Science" lives at `docs/ethics-in-data-science/` and is published with `.github/workflows/deploy-pages.yml`.

```text
[edit Quarto source]
        |
        v
[quarto preview on device]
        |
        v
[git commit] --> [git push to main] --> [GitHub Action: deploy-pages.yml]
                                          |
                                          v
                            [quarto render docs/ethics-in-data-science]
                                          |
                                          v
                            [jekyll build docs/ -> _site/]
                              (book output has no front matter,
                               so it is copied through untouched)
                                          |
                                          v
                             [upload _site/ as Pages artifact]
                                          |
                                          v
                                [deploy to GitHub Pages]
                                          |
                                          v
                  [dodatascience.fun/ethics-in-data-science/book/]
```

- On pushes to `main`, the GitHub workflow renders the book with `quarto render docs/ethics-in-data-science`.
- Jekyll then builds `docs/` into `_site/`, which is uploaded as the Pages artifact.
- GitHub Pages serves that artifact directly, so the generated `docs/ethics-in-data-science/book/` output is not tracked in git.
- This keeps Quarto output separate from version control
- Any change to a .md file will automatically propagate. You can also preview changes locally with `quarto render`
- **The book stays independent of Jekyll.** Its `.md` sources are listed in `docs/_config.yml`'s `exclude`, so Jekyll does not try to render them. Editing and previewing the book is pure Quarto.

### FAQ build

The FAQ source is `docs/faq.md`. There is no build script: its front matter sets `layout: default`, so Jekyll renders it to `/faq.html` during the Pages build.

Again, to edit this page, simply edit `docs/faq.md` Markdown and push.

### masthead, footer, layout

The site header/nav and the GitHub footer each live in exactly one file: `docs/_includes/masthead.html` (styles in `docs/css/masthead.css`) and `docs/_includes/footer.html`. The `<h1>` text and the nav links are hardcoded there, so every page reads the same.

Most pages use `_layouts/default.html` by setting `layout: default`. That is how `docs/faq.md` and `docs/slides/index.html` work, and it is the default choice for a new page:

```yaml
---
layout: default
title: Slides   # feeds <title> via jekyll-seo-tag
nav: slides     # optional; marks the active nav link
---
```

Two pages skip that layout:

- `docs/index.html` — hand-written social/OG meta for the landing page.
- `syllabus_source/template.html` — a Pandoc template that emits front matter and `{% include masthead.html %}` into `docs/syllabus/index.html` (Jekyll expands it)

`nav` accepts `home`, `slides`, `book`, `syllabus`, `faq`, or `timer`, and adds `aria-current="page"` to that link.

### Previewing the site locally

The includes and the FAQ are assembled by Jekyll, so a plain static file server will show `{% include ... %}` as literal text. To preview the actual site:

```bash
cd docs
bundle install          # first time only
bundle exec jekyll serve
```

That serves the site at <http://localhost:4000> and rebuilds on save.

Quarto output (slides, mini-book) is served as-is, so use `quarto preview` for those.


## Course topics

Still working on this 🙂 there are too many possibilities... But main units will probably include:
* Basic prob/stats/sampling/distributions
	* Data science lifecycle
	* common distributions: Bernoulli, binomial, Poisson, normal, exponential
	* Central Limit Theorem
	* Estimation, sampling, and randomness
	* Simple random samples
* Data frame fundamentals
	* Python foundations and polars
	* Obtaining data; data formats
	* Data types
	* Wrangling and filtering
	* Joining/merging datasets
	* Wide data vs long data
* Exploratory analysis and descriptive stats
	* Anscombe's quartet / datasaurus dozen
* Visualizations (weeks 5-6)
* Hypothesis testing
	* statistical significance 
	* Uncertainty (i.e. confidence intervals, errors, confidence levels, etc.)
	* More on estimation/sampling/randomness
		* stratified samples
		* systematic sampling
		* cluster sampling
		* voluntary sampling
		* snowball sampling
	* determining sample size
* Linear modeling (week 8)
	* Simple and multiple linear regression
	* Bayesian linear regression
* Machine-learning models (weeks 8-11)
	* Classification
	* Decision trees
	* SVMs and kernels
	* Clustering and PCA
	* Train/test splits
	* Evaluation metrics
	* Feature-based recommendation systems
	* A/B testing
* Network analysis (week 12)
	* Matrices as networks
	* Network measures
	* Network-based recommendation systems
* Group presentations (weeks 14-15)

The "ground truth" for the week-by-week schedule is [`docs/_data/schedule.csv`](docs/_data/schedule.csv) — see the [Syllabus build](#syllabus-build) section above.


## Note on LLM use

The `sandbox/` folder is a quarantine zone for anything modified by an LLM. My philosophy on LLM usage is [here](https://jackbandy.com/text/llm-code-philosophy.html), but in short: I use them sparingly, and with caution, sort of like a credit card. If I do not have sufficient "money" (understanding) to "pay back" (explain, modify, rewrite, etc.) what I "buy" (generate), I probably should use a different tool, or do some learning.

In some cases, I move things out of the `sandbox/` after editing and testing and verification. In practice, this means that LLMs may be adjusting or improving some workflows that would otherwise require lots of time/tedium (e.g. the syllabus build workflow and other GitHub action setups). This allows me to focus more on writing/thinking, planning, and teaching (at least that is the theory, and has mostly been my experience so far).

I willingly take responsibility for what is in this repository, including those files which were modified by LLMs. Please contact me if you notice any issues - those are my fault.

Files that were substantially modified by LLMs will say so in the header, e.g. `NOTICE: This file modified by an LLM coding system...` or something like that.

All other materials hand-typed with 🩵 in Chicago, IL.
