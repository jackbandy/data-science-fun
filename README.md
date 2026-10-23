# 🪩 Data Science the Fun Way 🪩
## Materials for CS 418: Intro to Data Science
### University of Illinois Chicago (UIC)

These are in-progress materials for a section of [CS 418 (Intro to Data Science)](https://catalog.uic.edu/search/?P=CS%20418) in Fall 2026. This repository is intended as the main container for reference materials, including slides, worksheets, demo code, etc. 

The public-facing site, [DoDataScience.fun](https://dodatascience.fun/), lives at the `docs/` folder, deployed via GitHub Pages.

For in-class worksheets, the goal is to create a library of accessible, hand-written / hand-drawn exercises, inspired by [Tom Yeh's "AI by Hand" series](https://www.byhand.ai).

## Overview

This repo holds the raw files (mostly markdown files) that are assembled and published automatically on every push to `main`. The goal is to make materials portable, accessible, and **easily editable**: edit a text file, commit, and push, then everything else happens automatically.

| What | Edit this | Shows up at |
| --- | --- | --- |
| Slides | `docs/slides/week*.qmd` | [/slides/](https://dodatascience.fun/slides/) |
| Syllabus text | `syllabus_source/syllabus.md` | [/syllabus/](https://dodatascience.fun/syllabus/) |
| Week-by-week schedule | `docs/_data/schedule.csv` | homepage table + syllabus + [/schedule.html](https://dodatascience.fun/schedule.html) |
| What happens each day, and its source materials | `docs/_includes/schedule-topics.md` | [/schedule.html](https://dodatascience.fun/schedule.html) |
| Ethics mini-book | `docs/ethics-in-data-science/*.qmd` | [/ethics-in-data-science/book/](https://dodatascience.fun/ethics-in-data-science/book/) |
| FAQ | `docs/faq.md` | [/faq.html](https://dodatascience.fun/faq.html) |
| Worksheets | `worksheets_source/*/worksheet.tex` | `/worksheets/` |

Technical details of each build are in the collapsible sections below.

## Note on LLM use

The `sandbox/` folder is a quarantine zone for anything modified by an LLM. Some philosophy on LLM usage is [here](https://jackbandy.com/text/llm-code-philosophy.html), but in short: I use them sparingly, and with caution, sort of like a credit card. If I do not have sufficient "money" (understanding) to "pay back" (explain, modify, rewrite, etc.) what I "buy" (generate), I probably should use a different tool, or do some learning.

In some cases, I move things out of the `sandbox/` after editing and testing and verification. In practice, this means that LLMs may be adjusting or improving some workflows that would otherwise require lots of time/tedium (e.g. the syllabus build workflow and other GitHub action setups). This allows me to focus more on writing/thinking, planning, and teaching (at least that is the theory, and has mostly been my experience so far).

I willingly take responsibility for what is in this repository, including those files which were modified by LLMs. Please contact me if you notice any issues - those are my fault.

Files that were substantially modified by LLMs will say so in the header, e.g. `NOTICE: This file modified by an LLM coding system...` or something like that.

All other materials hand-typed with 🩵 in Chicago, IL.

## License

By default, the materials here are licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/) (CC BY-NC-SA 4.0). The full legal code is in [`CC-BY-NC-SA-4.0.txt`](CC-BY-NC-SA-4.0.txt).

Their purpose is to educate, so feel free to use them, remix them, teach with them, etc., given:

- **Attribution** — credit the source, e.g. *"Data Science the Fun Way," https://github.com/jackbandy/data-science-fun*
	- Of course, credit the upstream source if you're using something that this repo got from somewhere else
- **NonCommercial** — not for commercial or profit-driven use. plz.
- **ShareAlike** — distribute your adaptations under this license

**Third-party material.** The decks include some photos, figures, and diagrams from other people under their own licenses (various CC BY-SA versions, a few images used under fair use). Those are credited on each deck's Sources slide.

**Code.** The website and other public-facing materials are CC BY-NC-SA, but Creative Commons says "We recommend against using Creative Commons licenses for software" ([CC FAQ](https://creativecommons.org/faq/)), so all the code in this repo is under the [MIT License](LICENSE) instead. That includes scripts, build tooling, workflows, and the code in slides, exercises, and notebooks. Third-party code keeps its own license.

Note that a good portion of the code here (e.g. build scripts, figure generators, etc.) was drafted by LLM-based coding tools. You're welcome to it under the MIT License, but most of it is less-than-great code that was simply used as a means to an end, where my end goal was to create a specific element or demo or visual. See also the [Note on LLM use](#note-on-llm-use) above.

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
│   ├── schedule.md              # Full-schedule page (Jekyll renders it to /schedule.html)
│   ├── _data/                   # Site data: files Jekyll parses, addressed as site.data.*
│   │   ├── schedule.csv         # The one copy of the course schedule, incl. the unit each day belongs to
│   │   └── stations.yml         # Orange Line stop metadata
│   ├── _includes/               # Site header/nav and footer, plus files pasted in as raw text
│   │   └── schedule-topics.md   # Per-day topics and source materials for /schedule.html
│   ├── _layouts/default.html    # Layout for Markdown pages
│   ├── _layouts/schedule.html   # Layout for /schedule.html
│   ├── Gemfile                  # Local Jekyll preview only
│   ├── css/                     # Shared stylesheets
│   ├── js/                      # Site scripts (schedule tooltips)
│   ├── assets/                  # Images, figures, and figure-generating scripts
│   ├── slides/                  # Quarto decks (week*.qmd) + shared/ build tooling and theme
│   ├── syllabus/                # Generated syllabus output (gitignored, built in CI)
│   ├── worksheets/              # Generated worksheet PDFs
│   ├── ethics-in-data-science/  # Quarto mini-book
│   ├── timer/, spectrogram/      # Small in-class web tools
│   ├── security.md, robots.txt  # Privacy/security page and crawler rules
│   └── CNAME                    # domain config
├── datasets/                    # Datasets used in class materials
├── syllabus_source/             # Syllabus markdown, pandoc templates, lua filters
├── worksheets_source/           # Worksheet source and build script
├── sandbox/                     # Quarantine for LLM-modified or experimental content
├── CONTRIBUTING.md              # How to report issues / suggest changes
├── CC-BY-NC-SA-4.0.txt          # License for materials
├── LICENSE                      # MIT (code)
├── NOTES.md                     # Working notes and planning
└── README.md                    # This file
```

</details>

<details>
<summary><strong>Dependencies</strong></summary>

Every build tool is installed by `.github/workflows/deploy-pages.yml` on each run, so that workflow is the ground truth for versions.

| Tool | Version pinned in CI | Needed for | Declared in |
| --- | --- | --- | --- |
| Ruby | `>= 3.0, < 4.0` | Jekyll site build | `docs/Gemfile` |
| Jekyll (via `github-pages` gem) | whatever `github-pages` resolves to | masthead/includes, `/schedule.html`, homepage table | `docs/Gemfile` |
| Python | 3.12 | executing slide code chunks | `deploy-pages.yml`, `repo-checks.yml` |
| Python packages | see file (several deliberate caps) | slide figures and models | `docs/slides/shared/requirements.txt` |
| `uv` | latest | installs the Python packages | `deploy-pages.yml`, `shared/build_all_quarto.sh` |
| Quarto | `release` (latest) | renders every deck and the mini-book | `deploy-pages.yml` |
| R | `release` | **week 5 only** — it uses `engine: knitr` and shells out to `Rscript` | `deploy-pages.yml` |
| R packages | unpinned, latest | `knitr`, `rmarkdown`, `reticulate`, `here`, `ggplot2`, `ggtext`, `patchwork`, `svglite` | `deploy-pages.yml` (inline `Rscript -e`) |
| Node | 22 | Quarto tooling | `deploy-pages.yml` |
| Chromium | latest | slide PDF export only — non-blocking, `continue-on-error` | `deploy-pages.yml` |
| pandoc, `librsvg2-bin`, fontconfig, `fonts-liberation`, `texlive-xetex`, `texlive-latex-recommended`, `texlive-latex-extra`, `texlive-fonts-recommended`, `texlive-plain-generic` | Ubuntu runner's apt | syllabus HTML + PDF | `deploy-pages.yml` (apt-get step) |
| `latexmk` | local install | worksheet PDFs — **not built in CI**, run by hand | `worksheets_source/build.sh` |
| `ruff` | latest | lint check (`E9,F63,F7,F82`, `sandbox/` excluded) | `repo-checks.yml` |
| `lychee` | `lycheeverse/lychee-action@v2` | link checking | `deploy-pages.yml`, `link-check-external.yml` |

**Notes:**

- The Python caps in `requirements.txt` are: `numpy<2.5`
  (numba/arviz), `matplotlib<3.11` (arviz's `style.core` import), `arviz<1.3`. Lifting one
  without reading its comment will break a slide render.
- R is the odd one out. Quarto's setup action does not bundle it, and only week 5 needs it as of right now —
  `build_all_quarto.sh` *skips* any knitr deck when `Rscript` is missing rather than failing,
  so a local build without R produces one fewer deck.
- Locally, `build_all_quarto.sh` makes its own `docs/slides/.venv` with `uv`. CI sets
  `SKIP_VENV=true` and installs into the runner's Python instead.

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
- More complicated than Google Slides? Yes. Worth it for freedom, portability, accessibility, etc.? For now, yes, I think...
- `deploy-pages.yml` renders the decks on every push (cache output and re-render only changed sources)
- Each compiled deck produces an HTML file, a `_files/` support directory (CSS, JavaScript, other assets), and usually a PDF: HTML is required, PDF export is best-effort (non-blocking)
- Jupyter-engine decks keep their executed notebook as `docs/slides/weekN.ipynb` - makes it easy to download and run the code
	- **knitr**-engine decks (R + Python combos like Week 5) can't produce a notebook, so they link their `weekN.qmd` source instead
- `shared/sync_slide_index.py` owns four regions of `docs/slides/index.html`, and pulls each from a different source. **Nothing it writes should ever be hand-edited** — `repo-checks.yml` re-runs the script and fails the build on any drift.
	- **the topic bullets** ← the deck's own `{.section-header}` headings, one bullet each, deep-linked to that slide (add `.no-index` to a header to leave it off the list)
	- **the "More:" bullet** ← the PDF, plus a notebook link if one exists, else the deck source
	- **the parenthetical after each "Week N Slide Deck" title, and the Topics column of the slide-count table** ← `docs/_data/schedule.csv`, *not* the deck. This catches people out: to reword a deck's parenthetical you edit the CSV's `Topic` cells, and a stale `index.html` will look like the script is inventing changes when it is really just propagating a CSV edit you already made.
	- the slide counts in that table are counted from the deck sources, so they move whenever you add or remove a slide
	- **the "Click to jump to week" row at the top** ← one cell per week that has an index entry, linking to the `id="weekN"` the script puts on each title link
	- run it after editing any deck heading **or** `schedule.csv`: `python3 docs/slides/shared/sync_slide_index.py docs/slides`
	- the hand-written bullets it replaced are archived in `docs/slides/shared/0-old-outline.md`
- The workflow should copy `docs/slides/week*.qmd` into `_site/slides/` after Jekyll runs
	- (`docs/_config.yml` excludes `slides/*.qmd` from Jekyll)

**To build slides locally:**

```bash
cd docs/slides
shared/build_all_quarto.sh       # HTML only (default)
BUILD_PDFS=true shared/build_all_quarto.sh  # Include PDFs
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
     |
     |       [docs/_data/schedule.csv] -------------+
     |                                              +--(Liquid loop)--> /schedule.html
     |       [docs/_includes/schedule-topics.md] ---+
     |
     |       [docs/syllabus/index.html] -> masthead include expanded in place
     |
     v
[upload _site/ -> GitHub Pages]
```

- **The schedule lives in one place: `docs/_data/schedule.csv`.** Jekyll reads it as `site.data.schedule` for the homepage table and for /schedule.html; `schedule.lua` expands the empty ` ```schedule ` block in `syllabus.md` into the same rows for Pandoc.
	- Jekyll and the syllabus read it at build time, so neither commits a generated table. The one exception is `docs/slides/index.html`, where `sync_slide_index.py` bakes the `Topic` cells into committed HTML — so a `schedule.csv` edit is not fully propagated until that script is re-run.
	- **Add new columns only at the end.** `schedule.lua` validates the header positionally for the first five columns (`Week`, `Class Day`, `Topic`, `Before Class`, `In Class`) and renders only those; Jekyll addresses columns by name. Trailing columns like `Date`, `Notes`, and `Unit` are carried in the CSV and ignored by both tables (they feed /schedule.html instead). Inserting a column before `In Class` fails the syllabus build.
	- Week-to-station labels for the homepage dots (and the /schedule.html week headings) are in `docs/_data/stations.yml`.
	- **Units come from the CSV's `Unit` column,** one value per class day. /schedule.html groups weeks under a heading per unit and lists each unit's week span at the top of the page; both are derived from the column, so moving a unit boundary is a CSV edit.
	- **The two schedule sources sit in different folders on purpose.** `_data/` is for files Jekyll parses for you: it reads `schedule.csv` and `stations.yml` into `site.data.schedule` and `site.data.stations`, which is why no template has to split CSV lines or read YAML by hand. `_includes/` is for files pasted in as raw text, which is the only way a template can get at the *unrendered* markdown of `schedule-topics.md` — Jekyll's data loader ignores `.md` outright. Moving either file into the other folder means hand-parsing it in Liquid, so they stay put.
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
- Worksheets are the one output with no CI path: `worksheets_source/build.sh` runs on your machine and the PDFs under `docs/worksheets/` are committed.
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

- GitHub Pages serves that artifact directly, so the generated `docs/ethics-in-data-science/book/` output is not tracked in git.
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

`nav` accepts `home`, `slides`, `book`, `syllabus`, `faq`, or `timer`, and adds `aria-current="page"` to that link.

Two pages skip that layout:

- `docs/index.html` — hand-written social/OG meta for the landing page.
- `syllabus_source/template.html` — a Pandoc template that emits front matter and `{% include masthead.html %}` into `docs/syllabus/index.html` (Jekyll expands it)

</details>

<details>
<summary><strong>Local Preview</strong></summary>

To preview the site locally:

```bash
python3 exercises/build-exercises-data.py  # required: see note below
cd docs
bundle install          # first time only
bundle exec jekyll serve
```

Run the exercises script first on a fresh clone. It writes `docs/_data/exercises.yml`, `docs/_includes/exercises-about.html` and `docs/exercises/`, all generated from `exercises/*/exercise.md` and all gitignored, and Jekyll aborts with `Liquid error: Cannot sort a null object` if they are absent.

Quarto output (slides, mini-book) is served as-is, so use `quarto preview` for local previews.

The includes and the FAQ are assembled by Jekyll, so a plain static file server will show `{% include ... %}` as literal text — use `bundle exec jekyll serve`, which serves the site at <http://localhost:4000> and rebuilds on save.

</details>
