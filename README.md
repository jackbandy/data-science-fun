# 🪩 Data Science the Fun Way 🪩
## Materials for CS 418: Intro to Data Science
### University of Illinois Chicago (UIC)

I'm preparing to teach a section of CS 418 (Intro to Data Science) in Fall 2026. This repository is intended as the main container for materials, including slides, worksheets, references, etc. My goal is to create a library of accessible, high-quality materials, including hand-written / hand-drawn exercises, inspired by [Tom Yeh's "AI by Hand" series](https://www.byhand.ai).

Materials are under active development during Summer 2026. The public-facing site, [DoDataScience.fun](https://dodatascience.fun/), lives at the `docs/` folder, deployed via GitHub Pages.

## Repository layout

```text
data-science-fun/
├── .github/workflows/           # GitHub Actions stuff
├── docs/                        # Public-facing site root
│   ├── index.html               # Landing page
│   ├── css/                     # Shared stylesheets
│   ├── slides/                  # Quarto decks and archived Marp workflow
│   ├── syllabus/                # Generated syllabus output (html, pdf)
│   ├── worksheets/              # Generated worksheet PDFs
│   ├── ethics-in-data-science/  # Quarto mini-book
│   └── CNAME                    # domain config
├── syllabus_source/             # Syllabus source and helpers
├── worksheets_source/           # Worksheet source and build script
├── sandbox/                     # Quarantine for LLM-modified or experimental content
├── source-materials/            # Reference and upstream source files
├── NOTES.md                     # Working notes and planning
├── package.json                 # Dependencies for slides
└── README.md                    # This file
```

## GitHub Actions

Using GitHub Actions workflows for some materials. The goal is to keep things more portable, accessible, and easily editable. This usually means putting "raw content" in a markdown file somewhere, which gets assembled and served automatically any time there is a push.

### Slide build

I'm trying to avoid Google Slides, and the current markdown-based slide workflow uses Quarto to generate Reveal.js decks.

```text
 [docs/slides/week0.qmd ... week12.md]
                    |
          +---------+---------+
          |                   |
          v                   v
 [Reveal.js HTML]          [PDF]
```

**Building slides:**

All slide builds are now **manual** (CI pipeline removed).

To build all slides:

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
- SVGs and other vector formats whenever possible.
- The previous Marp experiment is archived in `docs/slides/marp_archive/`. Run `docs/slides/marp_archive/build_all_marp.sh` to rebuild its HTML and PDF outputs.
- More complicated than Google Slides? Yes. Worth it for freedom, portability, accessibility, etc.? For now, yes.

**Theme:**

The slide theme uses Big Shoulders for title headings and a Franklin-style sans stack for body and footer text. The repo self-hosts Libre Franklin from `impallari/Libre-Franklin` as the libre body-font asset used across the decks.

### Syllabus build

This is somewhat over-engineered (with help from LLMs), but the result is that I can easily edit the schedule (in a .csv) and/or text in the syllabus (in a .md), and the changes automatically propagate.

The markdown workflow is in `syllabus_source/`, and the generated files are published under `docs/syllabus/`:

```text
       [syllabus_source/schedule.csv]
                     |
                     v
       [sync_schedule.py] --> [docs/index.html schedule table]
                     |
                     v
       [syllabus_source/syllabus.md]
                     |
          +----------+----------+
          |     (pandoc)        |
          v                     v
  [template.html]         [template.tex]
          |                     |
          v                     v
[docs/syllabus/index.html]  [docs/syllabus/syllabus.pdf]
```

- Run `syllabus_source/build.sh`. It syncs the schedule, then compiles the markdown to both HTML and PDF (via latex).
- The upstream source is `syllabus_source/syllabus.md`. Its YAML block holds the header (course title, college, credit hours); the templates render it.
- The shared course schedule is `syllabus_source/schedule.csv`. `sync_schedule.py` writes it into both the syllabus table and the homepage table, between `SCHEDULE_*` marker comments (so do not hand-edit either table).
- `underline.lua` handles `[...]{.underline}` spans, schedule table's column widths, etc.
- The build needs `pandoc`, `xelatex`, `rsvg-convert`, and `python3`.
- The UIC logo comes from `docs/assets/branding/uic-black-logo.svg`, converted to PDF for the LaTeX header at build time.
- Both templates carry a WORK IN PROGRESS watermark: the `AddToShipoutPictureBG` block in `template.tex` and the `body::before` rule in `template.html`.
- Only `index.html` and `syllabus.pdf` are published under `docs/syllabus/`.
- The output is served directly at `dodatascience.fun/syllabus/`.

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
                            [upload docs/ as Pages artifact]
                                          |
                                          v
                                [deploy to GitHub Pages]
                                          |
                                          v
                  [dodatascience.fun/ethics-in-data-science/book/]
```

- On pushes to `main`, the workflow renders the book with `quarto render docs/ethics-in-data-science`.
- It uploads the full `docs/` directory as a GitHub Pages artifact.
- GitHub Pages serves that artifact directly, so the generated `docs/ethics-in-data-science/book/` output is no longer tracked in git.
- This keeps Quarto output separate from version control
- Any change to a .md file will automatically propagate. You can also preview changes with `quarto render`

### FAQ build

The FAQ source is `docs/faq.md`.

- Run `cd docs/scripts && ./build_faq.sh` to generate `docs/faq.html`.
- The Pages deployment workflow rebuilds the FAQ before uploading `docs/`.

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

The "ground truth" for the week-by-week schedule is [`syllabus_source/schedule.csv`](syllabus_source/schedule.csv). It is intended to be the single source for the schedule on the [course homepage](https://dodatascience.fun/) and in the [syllabus](https://dodatascience.fun/syllabus/).


## Note on LLM use

The `sandbox/` folder is a quarantine zone for anything modified by an LLM. My philosophy on LLM usage is [here](https://jackbandy.com/text/llm-code-philosophy.html), but in short: I use them sparingly, and with caution, sort of like a credit card. If I do not have sufficient "money" (understanding) to "pay back" (explain, modify, rewrite, etc.) what I "buy" (generate), I probably should use a different tool, or do some learning.

In some cases, I move things out of the sandbox after editing and  testing and verification. In practice, these means that LLMs may be adjusting or improving some workflows that would otherwise require lots of time/tedium (e.g. the syllabus build workflow). This allows me to focus more on writing/thinking, planning, and teaching (at least that is the theory, and has mostly been my experience so far).

Files that were substantially modified by LLMs will say so in the header, e.g. `NOTICE: This file modified by an LLM coding system...` or something like that

All other materials hand-typed with 🩵 in Chicago, IL.
