# 🪩 Data Science the Fun Way 🪩
## Materials for CS 418: Intro to Data Science
### University of Illinois Chicago (UIC)

I'm preparing to teach a section of CS 418 (Intro to Data Science), in Fall 2026. This repository is intended as the main container for materials, including slides, worksheets, references, etc. My goal is to create a library of practical learning activities, especially hand-written / hand-drawn exercises, inspired by [Tom Yeh's "AI by Hand" series](https://www.byhand.ai).

Materials are under active development during Summer 2026. The public-facing site, [DoDataScience.fun](https://dodatascience.fun/), lives at the `docs/` folder, deployed via GitHub Pages.

## Repository layout

```text
data-science-fun/
├── .github/workflows/           # GitHub Actions stuff
├── docs/                        # Public-facing site root
│   ├── index.html               # Landing page
│   ├── css/                     # Shared stylesheets
│   ├── slides/                  # Marp slides (md, pdf, html)
│   ├── syllabus/                # Generated syllabus output (html, pdf)
│   ├── ethics-in-data-science/  # Quarto mini-book
│   └── CNAME                    # domain config
├── syllabus/                    # Syllabus source and helpers
├── sandbox/                     # Quarantine for LLM-modified or experimental content
├── source-materials/            # Reference and upstream source files
├── worksheets/                  # Worksheet source files
├── NOTES.md                     # Working notes and planning
├── package.json                 # Dependencies for slides
└── README.md                    # This file
```

## GitHub Actions

Using GitHub Actions workflows for some materials. The goal is to make things more portable, accessible, and easily editable. This usually means putting "raw content" in a markdown somewhere, which gets assembled and served automatically.

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

### Slide build

I'm trying to avoid google slides, and this is the current markdown-based slide workflow, which lives in `.github/workflows/build-slides.yml`.

```text
                 [docs/slides/*.md]
                        |
             +----------+----------+
             |                     |
             v                     v
   [docs/slides/*.html]   [docs/slides/*.pdf]
```

- E.g. week0.md will automatically be compiled to create week0.html and week0.pdf
- On pushes that touch slide sources or Marp config, the workflow first checks whether the slide outputs are already up to date.
- If a rebuild is needed, it installs Node dependencies and runs `docs/slides/build_all_marp.sh`.
- It commits the generated slide HTML and PDF files back into the repository under `docs/slides/`.
- Those compiled slide files are then included in the Pages site because the site is deployed from the `docs/` artifact.

### Syllabus build

The syllabus uses a markdown workflow in `syllabus/`, and the generated files are published under `docs/syllabus/`.

```text
                    [syllabus/syllabus.md]
                              |
                   +----------+----------+
                   |                     |
                   v                     v
      [docs/syllabus/index.html]   [docs/syllabus/syllabus.pdf]
```

- The upstream source is `syllabus/syllabus.md`.
- Run `syllabus/build_syllabus_from_markdown.sh` to compile the markdown to both HTML and PDF (via latex).
- The output in `docs/syllabus/` is served directly at `dodatascience.fun/syllabus/`.

## Course topics

Still working on this 🙂 there are too many possibilities... But main units will probably include:
* Basic prob/stats/sampling
* Data frame fundamentals
* Visualizations
* Uncertainty
* Linear modeling
* Networks and network analysis
* Machine-learning models

## Note on LLM use

The `sandbox/` folder is a quarantine zone for anything modified by an LLM. My philosophy on LLM usage is [here](https://jackbandy.com/text/llm-code-philosophy.html), but in short: I use them sparingly, with extreme caution, sort of like a credit card.

In some cases, I move things out of the sandbox after editing and  testing and verification. In practice, these means that LLMs are often adjusting or improving some workflows that would otherwise require lots of tedium, which in turn allows me to focus on writing and planning.

Files that were substantially modified by LLMs will say so in the header, e.g. `NOTICE: This file modified by an LLM coding system...`

All other materials hand-typed with 🩵 in Chicago, IL.
