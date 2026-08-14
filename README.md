# 🪩 Data Science the Fun Way 🪩
## Materials for CS 418: Intro to Data Science
### University of Illinois Chicago (UIC)

These are in-progress materials for a section of CS 418 (Intro to Data Science) in Fall 2026. This repository is intended as the main container for reference materials, including slides, worksheets, demo code, etc. The goal is to create a library of accessible, high-quality materials, including hand-written / hand-drawn exercises, inspired by [Tom Yeh's "AI by Hand" series](https://www.byhand.ai).

Materials are under active development during Summer 2026. The public-facing site, [DoDataScience.fun](https://dodatascience.fun/), lives at the `docs/` folder, deployed via GitHub Pages.

## Overview

This repo holds the raw files (mostly markdown files) that are assembled and published automatically on every push to `main`. The goal is to make materials portable, accessible, and **easily editable**: edit a text file, commit, and push, then everything else happens automatically.

| What | Edit this | Shows up at |
| --- | --- | --- |
| Slides | `docs/slides/week*.qmd` | [/slides/](https://dodatascience.fun/slides/) |
| Syllabus text | `syllabus_source/syllabus.md` | [/syllabus/](https://dodatascience.fun/syllabus/) |
| Week-by-week schedule | `docs/_data/schedule.csv` | homepage table + syllabus |
| Ethics mini-book | `docs/ethics-in-data-science/*.qmd` | [/ethics-in-data-science/book/](https://dodatascience.fun/ethics-in-data-science/book/) |
| FAQ | `docs/faq.md` | [/faq.html](https://dodatascience.fun/faq.html) |
| Worksheets | `worksheets_source/*/worksheet.tex` | `/worksheets/` |


To preview the site locally:

```bash
cd docs
bundle install          # first time only
bundle exec jekyll serve
```

Quarto output (slides, mini-book) is served as-is, so use `quarto preview` for local previews.

Technical details of each build are in the collapsible sections below.

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

The "ground truth" for the week-by-week schedule is [`docs/_data/schedule.csv`](docs/_data/schedule.csv) — see the Syllabus build section below.

## Note on LLM use

The `sandbox/` folder is a quarantine zone for anything modified by an LLM. My philosophy on LLM usage is [here](https://jackbandy.com/text/llm-code-philosophy.html), but in short: I use them sparingly, and with caution, sort of like a credit card. If I do not have sufficient "money" (understanding) to "pay back" (explain, modify, rewrite, etc.) what I "buy" (generate), I probably should use a different tool, or do some learning.

In some cases, I move things out of the `sandbox/` after editing and testing and verification. In practice, this means that LLMs may be adjusting or improving some workflows that would otherwise require lots of time/tedium (e.g. the syllabus build workflow and other GitHub action setups). This allows me to focus more on writing/thinking, planning, and teaching (at least that is the theory, and has mostly been my experience so far).

I willingly take responsibility for what is in this repository, including those files which were modified by LLMs. Please contact me if you notice any issues - those are my fault.

Files that were substantially modified by LLMs will say so in the header, e.g. `NOTICE: This file modified by an LLM coding system...` or something like that.

All other materials hand-typed with 🩵 in Chicago, IL.

## License

By default, the materials here are licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/) (CC BY-NC-SA 4.0). The full legal code is in [`LICENSE`](LICENSE).

Their purpose is to educate, so feel free to use them, remix them, teach with them, etc., given:

- **Attribution** — credit the source, e.g. *"Data Science the Fun Way," https://github.com/jackbandy/data-science-fun*
	- Of course, credit the upstream source if you're using something that this repo got from somewhere else
- **NonCommercial** — not for commercial or profit-driven use. plz.
- **ShareAlike** — distribute your adaptations under this license

**Third-party material keeps its own terms.** The decks include some photos, figures, and diagrams from other people under their own licenses (various CC BY-SA versions, a few images used under fair use). Those are credited on each deck's Sources slide and are not covered by the blanket license above.

---

# Technical details

<details>
<summary><strong>Repository layout</strong></summary>

```text
data-science-fun/
├── .github/workflows/           # GitHub Actions stuff
├── docs/                        # Public-facing site root
│   ├── index.html               # Landing page
│   ├── faq.md                   # FAQ source (Jekyll renders it to /faq.html)
│   ├── _config.yml              # Jekyll config
│   ├── _data/                   # Site data
│   │   ├── schedule.csv         # The one copy of the course schedule
│   │   └── stations.yml         # Orange Line stop metadata
│   ├── _includes/               # The one copy of the site header/nav and footer
│   ├── _layouts/default.html    # Layout for Markdown pages
│   ├── Gemfile                  # Local Jekyll preview only
│   ├── css/                     # Shared stylesheets
│   ├── js/                      # Site scripts (schedule tooltips)
│   ├── assets/                  # Images, figures, and figure-generating scripts
│   ├── slides/                  # Quarto decks and archived Marp workflow
│   ├── syllabus/                # Generated syllabus output (gitignored, built in CI)
│   ├── worksheets/              # Generated worksheet PDFs
│   ├── ethics-in-data-science/  # Quarto mini-book
│   ├── timer/, spectogram/      # Small in-class web tools
│   ├── security.md, robots.txt  # Privacy/security page and crawler rules
│   └── CNAME                    # domain config
├── datasets/                    # Datasets used in class materials
├── syllabus_source/             # Syllabus markdown, pandoc templates, lua filters
├── worksheets_source/           # Worksheet source and build script
├── sandbox/                     # Quarantine for LLM-modified or experimental content
├── CONTRIBUTING.md              # How to report issues / suggest changes
├── LICENSE                      # CC BY-NC-SA 4.0
├── NOTES.md                     # Working notes and planning
└── README.md                    # This file
```

</details>

<details>
<summary><strong>Slide build</strong></summary>

I'm trying to avoid Google Slides, and the current markdown-based slide workflow uses Quarto to generate Reveal.js decks in html:

```text
 [docs/slides/week0 ... week12  (.md / .qmd)]
                    |
          +---------+---------+
          |                   |
          v                   v
 [Reveal.js HTML]          [PDF]
```

**Notes:**

- The decks are `docs/slides/week0.qmd` through `docs/slides/week12.qmd`, written in Quarto's extended markdown. Each file carries its own Reveal.js configuration.
- Every deck opens each class day the same way: a `# Week N, Day 1` / `# Week N, Day 2` title slide, the full-bleed stop photo, then a `# Map {.split}` slide whose left column lists that day's `{.section-header}` topics and whose right column is the week's stop from `docs/assets/orange-line-map-stops/`.
- Quarto revealjs HTML depends on the `*_files/` directories for styles to load properly on GitHub Pages.
- Slides use SVGs and other vector formats whenever possible.
- The previous Marp experiment is archived in `docs/slides/marp_archive/`. Run `docs/slides/marp_archive/build_all_marp.sh` to rebuild its HTML and PDF outputs.
- More complicated than Google Slides? Yes. Worth it for freedom, portability, accessibility, etc.? For now, yes.
- `deploy-pages.yml` renders the decks on every push (cache output and re-render only changed sources)
- Each compiled deck produces an HTML file, a `_files/` support directory (CSS, JavaScript, other assets), and usually a PDF: HTML is required, PDF export is best-effort (non-blocking)
- Jupyter-engine decks keep their executed notebook as `docs/slides/weekN.ipynb` - makes it easy to download and run the code
	- **knitr**-engine decks (R + Python combos like Week 5) can't produce a notebook, so they link their `weekN.qmd` source instead
- `sync_slide_index.py` rewrites the per-deck bullets in `docs/slides/index.html` after rendering
	- one topic bullet per `{.section-header}` heading, deep-linked to that slide (add `.no-index` to a header to leave it off the list)
	- plus the "Supporting … code" bullet (notebook link if one exists, else source link)
	- edit the wording by editing the deck's section header, not `index.html` — `repo-checks.yml` fails on hand edits. The bullets it replaced are archived in `docs/slides/0-old-outline.md`
- The workflow should copy `docs/slides/week*.qmd` into `_site/slides/` after Jekyll runs
	- (`docs/_config.yml` excludes `slides/*.qmd` from Jekyll)

**To build slides locally:**

```bash
cd docs/slides
./build_all_quarto.sh       # HTML only (default)
BUILD_PDFS=true ./build_all_quarto.sh  # Include PDFs
```

**Slide Theme:**

The slide theme uses Big Shoulders for title headings and a Franklin-style sans stack for body and footer text. The repo self-hosts Libre Franklin from `impallari/Libre-Franklin` (body-font asset used across the decks).

</details>

<details>
<summary><strong>Syllabus build</strong></summary>

This is somewhat over-engineered (with help from LLMs), but the result is that I can edit the schedule (in a .csv) and/or the text of the syllabus (in a .md), and everything else follows from those two files.

Sources are in `syllabus_source/`; outputs go to `docs/syllabus/` and are gitignored, so a push looks like this:

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
	- **Add new columns only at the end.** `schedule.lua` validates the header positionally for the first five columns (`Week`, `Class Day`, `Topic`, `Before Class`, `In Class`) and renders only those; Jekyll addresses columns by name. Trailing columns like `Date` and `Notes` are carried in the CSV and ignored by both tables. Inserting a column before `In Class` fails the syllabus build.
	- Week-to-station labels for the homepage dots are in `docs/_data/stations.yml`.
- The text source is `syllabus_source/syllabus.md`. Its YAML block holds the header (course title, college, credit hours); the templates render it. `underline.lua` handles its `[...]{.underline}` spans.
- The build needs `pandoc`, `xelatex`, and `rsvg-convert`. The workflow apt-installs them and caches `docs/syllabus/`, so unrelated pushes skip the TeX Live install and keep the existing "created" timestamp.
- The UIC logo comes from `docs/assets/branding/uic-black-logo.svg`, converted to PDF for the LaTeX header at build time.
- Both templates currently have a WORK IN PROGRESS watermark: `AddToShipoutPictureBG` in `template.tex`, `body::before` in `template.html`.
- To preview locally, run `syllabus_source/build.sh` before `jekyll serve` — a fresh clone will have no `docs/syllabus/` until running the build script

</details>

<details>
<summary><strong>Worksheet build</strong></summary>

Still early, but worksheet LaTeX sources and build support live in `worksheets_source/`.

- Run `worksheets_source/build.sh` to compile every `worksheet.tex`.
- Compiled PDFs are published under `docs/worksheets/`.
- Source directories do not retain generated worksheet PDFs.

</details>

<details>
<summary><strong>Quarto mini-book build</strong></summary>

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
- You can preview changes locally with `quarto render`
- **The book stays independent of Jekyll.** Its `.md` sources are listed in `docs/_config.yml`'s `exclude`, so Jekyll does not try to render them. Editing and previewing the book is pure Quarto.

</details>

<details>
<summary><strong>FAQ build</strong></summary>

The FAQ source is `docs/faq.md`. There is no build script: its front matter sets `layout: default`, so Jekyll renders it to `/faq.html` during the Pages build.

</details>

<details>
<summary><strong>Masthead, footer, layout</strong></summary>

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

</details>

<details>
<summary><strong>Previewing the site locally</strong></summary>

The includes and the FAQ are assembled by Jekyll, so a plain static file server will show `{% include ... %}` as literal text — use `bundle exec jekyll serve` (see the Overview above), which serves the site at <http://localhost:4000> and rebuilds on save.

</details>
