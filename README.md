# 🪩 Data Science the Fun Way 🪩
## Materials for CS 418: Intro to Data Science
### University of Illinois Chicago (UIC)

I'm preparing to teach a section of CS 418 (Intro to Data Science), in Fall 2026. This repository is intended as the main container for materials, including slides, worksheets, references, etc. My goal is to create a library of accessible, high-quality materials, including hand-written / hand-drawn exercises, inspired by [Tom Yeh's "AI by Hand" series](https://www.byhand.ai).

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

I'm trying to avoid Google Slides, and the current markdown-based slide workflow lives in `.github/workflows/build-slides.yml`. It uses quarto.

```text
 [docs/slides/week0.md ... week12.md(or .qmd)]
                    |
          +---------+---------+
          |                   |
          v                   v
 [Reveal.js HTML]          [PDF]
```

- The decks are `docs/slides/week0.md` through `docs/slides/week12.md`, with `docs/slides/week11.qmd` using Quarto's `.qmd` extension. Each file contains Quarto Reveal.js configuration and compiles to a matching HTML file, PDF, and `_files/` support directory.
- SVGs and other vector formats whenever possible!
- Run `docs/slides/build_all_quarto.sh` locally to build all current decks. It builds HTML and PDF by default; set `BUILD_PDFS=false` for HTML only.
- On pushes that touch slide sources or build support files, GitHub Actions builds HTML for both the current Quarto decks and archived Marp decks, then commits the generated HTML and Quarto support directories.
- Compiled slide files are included in the GitHub Pages site (deployed from the `docs/` artifact).
- The previous Marp experiment is in `docs/slides/marp_archive/`. Run `docs/slides/marp_archive/build_all_marp.sh` to rebuild its HTML and PDF outputs.
- More complicated than google slides? Maybe. Worth it for freedom, portability, accessibility, etc.? For now, yes.

### Syllabus build

The syllabus uses a markdown workflow in `syllabus_source/`, and the generated files are published under `docs/syllabus/`.

```text
                [syllabus_source/syllabus.md]
                              |
                   +----------+----------+
                   |                     |
                   v                     v
      [docs/syllabus/index.html]   [docs/syllabus/syllabus.pdf]
```

- The upstream source is `syllabus_source/syllabus.md`.
- The shared course schedule is `syllabus_source/schedule.csv`.
- Run `python3 syllabus_source/sync_schedule.py` to sync the schedule into the homepage and syllabus, then rebuild both outputs.
- Run `syllabus_source/build_syllabus_from_markdown.sh` to compile the markdown to both HTML and PDF (via latex).
- Only `index.html` and `syllabus.pdf` are published under `docs/syllabus/`.
- The output is served directly at `dodatascience.fun/syllabus/`.

### Worksheet build

Worksheet LaTeX sources and build support live in `worksheets_source/`.

- Run `worksheets_source/build.sh` to compile every `worksheet.tex`.
- Compiled PDFs are published under `docs/worksheets/`.
- Source directories do not retain generated worksheet PDFs.

### Quarto mini-book deploy

The Quarto mini-book at `docs/ethics-in-data-science/` is published with `.github/workflows/deploy-pages.yml`.

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

### FAQ build

The FAQ source is `docs/faq.md`.

- Run `cd docs/scripts && ./build_faq.sh` to generate `docs/faq.html`.
- The Pages deployment workflow rebuilds the FAQ before uploading `docs/`.

## Course topics

Still working on this 🙂 there are too many possibilities... But main units will probably include:
* Basic prob/stats/sampling/distributions
	* Uncertainty (i.e. confidence intervals, errors, confidence levels, etc.)
	* common distributions: Bernoulli, binomial, Poisson, normal, exponential
	* Central Limit Theorem
* Data frame fundamentals
	* Data types
	* Joining/merging datasets
	* Wide data vs long data
* Visualizations
* Linear modeling
* Machine-learning models
	* Clustering
	* Train/test splits
	* Evaluation metrics
	* Feature-based recommendation systems
* Network analysis
	* Matrices as networks
	* Network-based recommendation systems

| Week | Topic |
| --- | --- |
| Week 1 | Intro, stats review; Data Science lifecycle |
| Week 2 | Python, dataframes, polars; obtaining data |
| Week 3 | Wrangling, filtering; formats |
| Week 4 | Exploratory analysis; descriptive stats |
| Week 5 | Visualizations |
| Week 6 | Visualizations |
| Week 7 | Hypothesis testing; estimation/sampling/randomness |
| Week 8 | Linear regression; intro to classification |
| Week 9 | Decision trees; SVMS and kernels |
| Week 10 | Clustering, PCA; model evaluation |
| Week 11 | Recommendation systems; A/B testing |
| Week 12 | Network analysis |
| Week 13 | TBD |
| Week 14 | Group presentations |
| Week 15 | Group presentations |


## Note on LLM use

The `sandbox/` folder is a quarantine zone for anything modified by an LLM. My philosophy on LLM usage is [here](https://jackbandy.com/text/llm-code-philosophy.html), but in short: I use them sparingly, with extreme caution, sort of like a credit card. If I do not have sufficient "money" (understanding) to "pay back" (explain, modify, rewrite, etc.) what I "buy" (generate), I probably should use a different tool, or do some learning.

In some cases, I move things out of the sandbox after editing and  testing and verification. In practice, these means that LLMs are often adjusting or improving some workflows that would otherwise require lots of tedium, which in turn allows me to focus on writing and planning.

Files that were substantially modified by LLMs will say so in the header, e.g. `NOTICE: This file modified by an LLM coding system...` or something like that

All other materials hand-typed with 🩵 in Chicago, IL.
