# Repository TODO

- [ ] **Make a demo of Closeread.** Try out https://closeread.dev (Quarto extension for scrollytelling) and build a sample page
~~note to self - check mobile version of slides~~ (done — see mobile fix below)

---

## Slide spillover at 16:10 (October 22, 2026)

Checked every slide of all 13 decks (1,018 slides) in headless Chrome at two 16:10 projector sizes, 1280×800 and 1920×1200, with all fragments shown, plus 1280×720 (16:9) as a baseline. Reveal scales the 1280×720 slide to fit and letterboxes it on 16:10, so **nothing spills only because of 16:10**: every problem below is also there at 16:9 unless noted. Most of the real ones are `.split` slides, which `autofit-after-body.html` skips on purpose (grid layout), so a long left column pushes the figure down and runs under the footer. Fix by trimming text, moving it to notes, or splitting the slide. The check scripts are in `sandbox/slide-spill-check/` (see its README); re-run them after edits. Hidden elements can cause false flags, so confirm a flag with `shoot.mjs` before editing.

### Real spillover (text or figure under the footer or off the slide)

- [ ] `week0.qmd`, slide 44 of 55, "Text + Figure": content runs 96 px past the slide edge, 14 px under the footer.
- [ ] `week1.qmd`, slide 115 of 154, "Map": content runs 32 px past the slide edge, 20 px under the footer.
- [ ] `week2.qmd`, slide 4 of 153, "Map for Week 2 (LaSalle/Van Buren)": content runs 28 px past the slide edge, 17 px under the footer.
- [ ] `week5.qmd`, slide 81 of 148, "Map: Day 2": content runs 91 px past the slide edge, 10 px under the footer.
- [ ] `week5.qmd`, slide 111 of 148, "Can we conclude that one causes the other?": content runs 76 px past the slide edge, 65 px under the footer. Confirmed by screenshot.
- [ ] `week5.qmd`, slide 136 of 148, "Recreating the FIFA Chart: Polished": content runs 117 px past the slide edge, 117 px under the footer.
- [ ] `week6.qmd`, slide 42 of 115, "Airline Passengers: What Do You Notice?": content runs 24 px past the slide edge, 36 px under the footer. (flagged at only one 16:10 size, so may be a timing artifact)
- [ ] `week6.qmd`, slide 83 of 115, "A Bayesian Ridership Model": content runs 30 px past the slide edge, 15 px under the footer.
- [ ] `week10.qmd`, slide 24 of 106, "Nested Clusters": content runs 242 px past the slide edge, 78 px under the footer.
- [ ] `week10.qmd`, slide 34 of 106, "Choosing Eps": content runs 80 px past the slide edge, 78 px under the footer.
- [ ] `week10.qmd`, slide 36 of 106, "Where Condos Sell": content runs 277 px past the slide edge, 84 px under the footer. Confirmed by screenshot.
- [ ] `week10.qmd`, slide 67 of 106, "The Precision–Recall Tradeoff": content runs 49 px past the slide edge, 47 px under the footer.
- [ ] `week10.qmd`, slide 78 of 106, "Silhouette Coefficient": content runs 283 px past the slide edge, 106 px under the footer. Confirmed by screenshot.
- [ ] `week10.qmd`, slide 82 of 106, "When You Have the Answer Key": content runs 80 px past the slide edge, 78 px under the footer.
- [ ] `week10.qmd`, slide 103 of 106, "Counting Sentiment Words": content runs 316 px past the slide edge, 123 px under the footer. Confirmed by screenshot.

### Checked by screenshot, looks fine (false positives)

- [x] `week4.qmd`, slide 72 of 80, "Anatomy: the Probability of B": flagged 196 px, but the screenshot looks fine; the flag is the hidden MathML copy of the equation.
- [x] `week5.qmd`, slide 6 of 148, "The Datasaurus Dozen: Why Visualize?": flagged 200 px, but the screenshot looks fine; probably a hidden stacked image.

### Minor (20 px or less) or possibly intentional

- [ ] `week0.qmd`, slide 30 of 55, "Auto-Animate: Grow and Center": auto-animate demo; the growing element is meant to overflow mid-animation; check it reads as intended.
- [ ] `week2.qmd`, slide 80 of 153, "Map for Week 2 (LaSalle/Van Buren)": body ends just past the slide edge or into the footer, 15 px.
- [ ] `week2.qmd`, slide 98 of 153, "How “Wide-format” Dataframes Grow": the table runs off the right edge on purpose? (slide is about wide data growing); check it reads as intended.
- [ ] `week5.qmd`, slide 7 of 148, "Map: Day 1": body ends just past the slide edge or into the footer, 18 px.
- [ ] `week5.qmd`, slide 92 of 148, "The Same Four Numbers, One Scale": title sits slightly above the slide top (body is tall), 11 px.
- [ ] `week5.qmd`, slide 93 of 148, "Or Plot the Quantity in Dispute": title sits slightly above the slide top (body is tall), 11 px.
- [ ] `week5.qmd`, slide 95 of 148, "Grouped Bars": title sits slightly above the slide top (body is tall), 11 px.
- [ ] `week5.qmd`, slide 97 of 148, "Same Numbers, Less Ink": title sits slightly above the slide top (body is tall), 8 px.
- [ ] `week5.qmd`, slide 114 of 148, "Nearly 25,000 Points": title sits slightly above the slide top (body is tall), 11 px.
- [ ] `week5.qmd`, slide 116 of 148, "Two Fixes for Overplotting": title sits slightly above the slide top (body is tall), 8 px.
- [ ] `week5.qmd`, slide 117 of 148, "The Conditional Center": title sits slightly above the slide top (body is tall), 11 px.
- [ ] `week10.qmd`, slide 49 of 106, "How Many Components?": body ends just past the slide edge or into the footer, 5 px.
- [ ] `week10.qmd`, slide 53 of 106, "PCA on PCA: The Data": body ends just past the slide edge or into the footer, 17 px.
- [ ] `week10.qmd`, slide 100 of 106, "Turning Reviews into Two Numbers": body ends just past the slide edge or into the footer, 5 px.

### Probably fine: long code lines clipped inside a scrolling code block

- [ ] `week2.qmd`, slide 74 of 153, "Why describe() Exists": a code line runs 44 px past the slide edge, hidden inside its scrolling code block.
- [ ] `week3.qmd`, slide 19 of 28, "CSV": a code line runs 332 px past the slide edge, hidden inside its scrolling code block.
- [ ] `week3.qmd`, slide 20 of 28, "TSV": a code line runs 490 px past the slide edge, hidden inside its scrolling code block.
- [ ] `week5.qmd`, slide 41 of 148, "Setup: Chicago ‘L’ ridership, 2019": a code line runs 19 px past the slide edge, hidden inside its scrolling code block.
- [ ] `week5.qmd`, slide 44 of 148, "Setup: Cook County home sales, 2025": a code line runs 69 px past the slide edge, hidden inside its scrolling code block.
- [ ] `week5.qmd`, slide 137 of 148, "What do you think of this code? (Python)": a code line runs 526 px past the slide edge, hidden inside its scrolling code block.
- [ ] `week5.qmd`, slide 143 of 148, "What do you think of this code? (R)": a code line runs 326 px past the slide edge, hidden inside its scrolling code block.
- [ ] `week6.qmd`, slide 44 of 115, "Rolling Average": a code line runs 44 px past the slide edge, hidden inside its scrolling code block.
- [ ] `week6.qmd`, slide 57 of 115, "Load UIC-Halsted Daily Ridership": a code line runs 19 px past the slide edge, hidden inside its scrolling code block. (not flagged at 16:9; flagged at only one 16:10 size, so may be a timing artifact)
- [ ] `week6.qmd`, slide 60 of 115, "Weekday variation": a code line runs 6 px past the slide edge, hidden inside its scrolling code block.
- [ ] `week6.qmd`, slide 62 of 115, "Period=7 Decomposition: What’s Still There?": a code line runs 120 px past the slide edge, hidden inside its scrolling code block.
- [ ] `week6.qmd`, slide 63 of 115, "Monthly Variation(s) for UIC-Halsted Stop": a code line runs 44 px past the slide edge, hidden inside its scrolling code block.
- [ ] `week6.qmd`, slide 69 of 115, "Washington/Wabash Daily Patterns": a code line runs 107 px past the slide edge, hidden inside its scrolling code block.
- [ ] `week6.qmd`, slide 70 of 115, "Two Stations, Two Rhythms? (Daily)": a code line runs 196 px past the slide edge, hidden inside its scrolling code block.
- [ ] `week6.qmd`, slide 71 of 115, "Two Stations, Two Rhythms? (Monthly)": a code line runs 234 px past the slide edge, hidden inside its scrolling code block.
- [ ] `week6.qmd`, slide 84 of 115, "Posterior: Weekday Effects": a code line runs 196 px past the slide edge, hidden inside its scrolling code block.
- [ ] `week8.qmd`, slide 12 of 42, "Setup: Cook County Home Sales, 2025": a code line runs 69 px past the slide edge, hidden inside its scrolling code block.

---

## Social preview cards (August 16, 2026)

Jekyll-rendered pages now carry the full Open Graph + Twitter Card set, icons, manifest and
`theme-color`, via `docs/_includes/social-meta.html` and `docs/_includes/icons.html`. Pages
built by other toolchains get none of it, because no Jekyll include reaches them:

- [ ] **Syllabus.** Add the tags to `syllabus_source/template.html`, then rerun
  `syllabus_source/build.sh` (needs pandoc + xelatex + rsvg-convert; also regenerates the PDF).
- [ ] **Slide decks (`docs/slides/week*.html`, 13 of them).** Add an `include-in-header` to the
  Quarto deck config and re-render. Shared deck links currently unfurl bare.
- [ ] **Ethics mini-book (`docs/ethics-in-data-science/book/`).** Same fix in the book's
  `_quarto.yml`, then re-render.

Copy the tag block from a built page (`_site/timer/index.html` is the smallest example); the
image URLs are absolute, so it is portable as static HTML with no Liquid.

Also worth doing once the above is live:

- [ ] **Re-scrape the previews** so the platforms drop their cached copies of the old card:
  Facebook Sharing Debugger, LinkedIn Post Inspector, and posting the link once in Slack.

---

## LLM audit performed July 2, 2026

Scope: general setup, performance, and workflow simplification (slides/syllabus content excluded).

### Recently Completed

- [x] **PDF padding.** Slide PDFs now export with a white margin ring (reveal `margin=0.1` query param + 0.25in print margins) instead of content flush to the page edge.
- [x] **PDF slide numbers.** Exported PDFs rewrite reveal's bare sequence numbers to the "N of total" format matching the live decks.
- [x] **Mobile fix.** Mobile slide-number alignment corrected in the responsive footer theme.

### Next up (from last session)

- [ ] **Rebuild weeks 1–12** so the theme fixes (padding, slide numbers, mobile footer) apply to every deck, then review and commit.
- [x] **Decide the future of the week5 R+Python deck (`week5.qmd`).** *(July 2, 2026: publishing the R deck — CI now installs R plus `knitr`/`rmarkdown`/`reticulate`/`here`/`ggplot2`/`ggtext`/`patchwork`, and the deck falls back to system `python3` when `.venv` is absent. `week5.md` is now stale and can be deleted whenever convenient.)*

### High-impact: repo size & assets

- [x] **Delete `docs/assets/orange-line-stops-photos/`.** *(July 28, 2026: deleted the whole directory — 108 MB, 43 files. Verified first that no deck referenced it (only its own `SOURCES.md` did), that `orange-line-stops-better/` carries its own complete `SOURCES.md` so CC attribution is preserved, and that only one image differed by content (`stop01-harold-washington-library-a.jpg`, where `better/` holds the curated version). The 27 photos with no counterpart in `better/` went with it; they remain recoverable from git history if any are wanted later.)*
- [ ] **Web-optimize the large JPGs that ship to Pages.** 22 tracked images under `docs/` are still over 5 MB (`orange-line-stops-better/stop05-clark-lake-a.jpg` 18.5 MB, several `near-orange-line-stops/` and `art/` files 8–13 MB). Slides load these full-size, which is a real accessibility problem for students on phones or campus wifi. Resize to ~2000px max dimension at quality ~80 (typically <500 KB each); keep originals in `sandbox/ignore/` if provenance matters. `docs/` tracked content is ~337 MB against GitHub Pages' 1 GB soft limit.
- [x] **Git history is 1.0 GB, mostly dead slide PDFs.** *(July 2, 2026: rewrote history with `git filter-repo --path-glob 'docs/slides/*.pdf' --invert-paths` and force-pushed. Any old clones must be re-cloned; commit hashes changed.)*
- [x] **Untrack `sandbox/scripts/ethics-reference-check-cache.json` (6.9 MB).** *(July 2, 2026: added to root `.gitignore` — but the `git rm --cached` half was never committed, so the file stayed tracked and the ignore rule had no effect. August 15, 2026: actually untracked.)*

### CI / deploy workflow (`.github/workflows/deploy-pages.yml`)

- [x] **Slides cache can restore stale sources over the fresh checkout.** *(July 2, 2026: cache path narrowed to outputs only — `docs/slides/week*.html`, `week*_files`, `_libs` — so tracked sources can no longer be clobbered by a stale restore.)*
- [x] **Stop cloning full history on every deploy.** *(July 2, 2026: added `filter: blob:none` to the checkout step; full commit graph is kept for the changed-files diff but historic blobs are no longer downloaded.)*
- [x] **Python deps installed twice in CI.** *(July 2, 2026: `build_all_quarto.sh` now honors `SKIP_VENV=true`, and both CI render steps set it, so CI uses the system-wide `uv pip install` only.)*
- [x] **Pin `docs/slides/shared/requirements.txt`.** Only two loose upper bounds (`matplotlib<3.9`, `arviz<0.20`); everything else floats, so CI renders can drift between runs. Pin exact versions (or commit a `uv lock` / `requirements.lock`) for reproducible deck output. *(October 23, 2026: CI and local builds install `requirements.lock`, written by `shared/lock_requirements.sh` with the shared libraries pinned to the Python Yard's Pyodide versions.)*
- [ ] **Bump actions off deprecated Node.js 20.** `actions/cache@v4`, `actions/checkout@v4`, `actions/configure-pages@v5`, `actions/deploy-pages@v4`, `actions/setup-node@v4`, `actions/setup-python@v5`, `actions/upload-artifact@v4`, and `browser-actions/setup-chrome@v1` all target Node 20, which GitHub is deprecating; they're currently being force-run on Node 24. Upgrade to the latest major versions that target Node 24 before GitHub stops forcing the runtime. See https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/ *(July 28, 2026: Dependabot now watches `.github/workflows/` weekly and will open these bumps as PRs, but major-version bumps still need a human to review and merge.)*

---

## Automated checks — added July 28, 2026

Set up in this pass: PR builds + a required `build` check on `main` (with admin/write
bypass so direct pushes still work), an internal link check inside the build, a weekly
external link check that files a tracking issue, Dependabot, and `repo-checks.yml`
(generated-file drift, `ruff`/`shellcheck`, duplicate-file ratchet).

### Still to add

- [ ] **Guard against new oversized files.** Fail a PR that adds a file over ~2 MB, with a label to override for genuine datasets. This only stops things getting worse — it does nothing about the 22 images already over 5 MB (see "Web-optimize the large JPGs" above), and nothing about git history, which still carries every deleted blob.
- [ ] **Alt-text ratchet for accessibility.** 34 of 43 markdown images use empty alt text (`![](...)`) and 30 `<img>` tags have no `alt` at all, which cuts against the repo's stated accessibility goal. This can't blanket-fail: empty alt is *correct* for purely decorative images. Build it as a count that must not increase, then work the number down. Considered and deferred: a full `pa11y`/`axe` sweep, which is more thorough but much noisier on Reveal.js decks (theme contrast warnings on every slide).
- [ ] **Secret scanning.** Two layers, both free on public repos: enable GitHub secret scanning + push protection in repo settings (blocks at push time, no workflow needed), and add `gitleaks` in CI as a backstop. The realistic risk here isn't an API key — it's a student name, grade, or Canvas token pasted into a notebook cell or a file under `datasets/`.
- [ ] **Validate `docs/_data/schedule.csv` on PRs.** It's the single source of truth for both the Jekyll homepage table and `schedule.lua`'s syllabus expansion, so a malformed row silently produces a wrong table in two places. Check column count, parseable dates, chronological order, and no duplicate weeks.
- [ ] **Consider making `repo-checks.yml` required.** Currently advisory. Note the trap if you do: required checks deadlock with `paths:` filters — see the header comment in `deploy-pages-skip.yml` for why that companion workflow exists.

### Simplification / cruft

- [x] **Retire the Marp dependency.** *(August 15, 2026: `package.json`/`node_modules` were already gone, and `docs/slides/marp_archive/` is now deleted — it is still in git history if the retired experiment is ever wanted back.)*
- [ ] **Fix stale README claims.** README says "All slide builds are now manual (CI pipeline removed)" and that notebooks go to `code_from_slides/` — but `deploy-pages.yml` renders slides on push, and notebooks are saved as `docs/slides/week*.ipynb`. The layout diagram also lists `source-materials/`, which doesn't exist.
- [ ] **Local disk reclaim (not git).** `sandbox/stanford-109-questions/` downloads are 3.7 GB and `docs/slides/.venv` is 717 MB — both gitignored and regenerable; delete whenever disk pressure matters.
- [ ] **Resolve the CI notebook-reachability TODO.** The prune step in `deploy-pages.yml` carries a TODO to verify `dodatascience.fun/slides/week0.ipynb` is reachable after deploy. Check once and delete the comment.

---

## LLM review performed June 5, 2026

### Recently Completed

- [x] **Correct dataset filenames in three READMEs.** Updated `datasets/chicago-l-stations/README.md`, `datasets/chicago-tall-buildings/README.md`, and `datasets/cta-ridership/README.md` so their documented CSV names match the files actually present.

- [x] **Clean up the ethics mini-book README.** Removed the unsupported `uv pip install` guidance and documented that reusable assets live in `docs/assets/` while generated `book/` output is not source material.

- [x] **Archive the old Orange Line standalone page.** The earlier Orange Line page and its support files now live under `sandbox/orange-line-v1/` instead of remaining as an active docs page.

### Quick Tasks

Each item should fit in a focused 5-10 minute pass.

- [ ] **Verify the published FAQ route after the next deploy.** `docs/faq.html` now exists locally; confirm that `https://dodatascience.fun/faq.html` returns `200` after deployment and that the homepage link resolves correctly in production.

- [ ] **Verify the worksheet URL after the next deployment.** Confirm that `https://dodatascience.fun/worksheets/00-worksheet-template.pdf` returns `200`, then check that no public page still references the old `worksheet-pdfs/` path.

- [ ] **Restore the missing subpixel generator input.** `docs/assets/subpixels/make_pixel_assets.py` expects `lcd-pixel-macro-2023.jpg`, which is absent. Restore the source image or update the script to use an existing canonical input, then run it once.

- [x] **Fix the lifecycle font source path.** *(July 2, 2026: checked — the script already points at the current shared location, `docs/assets/fonts/libre-franklin/LibreFranklin.woff2`, and reran cleanly with no diff. This TODO's description was stale, not the code.)*

- [x] **Remove transient files from shared assets.** *(July 2, 2026: deleted `docs/assets/lifecycle/__pycache__/`, `docs/assets/triangles/__pycache__/`, and `docs/assets/triangles/.DS_Store`; root `.gitignore` already excludes both patterns, so they were never tracked.)*

- [ ] **Resolve the remaining ethics-book asset exceptions.** Move `cc-by-nc-sa.svg` and `dikw-pyramid.svg` out of `docs/ethics-in-data-science/assets/`, remove unused files, or revise `NOTE.md` to document why they remain.

- [ ] **Trim stale link-audit notes after verification.** Once the FAQ and worksheet routes are confirmed after deployment, update or remove the outdated notes at the bottom of this file.

### Big-Picture Work

- [ ] **Unify build and deployment automation.** Decide whether GitHub Actions should build the book, slides, syllabus, and worksheets from source, rather than mixing automated builds with committed generated outputs.

- [ ] **Choose one generated-output policy for slides.** Slides currently keep Markdown, HTML, PDF, and large Quarto support directories together under `docs/`; define which artifacts are source-controlled and which are generated during deployment.

- [ ] **Create a release-readiness pass for course content.** Track and replace syllabus `TK` fields, placeholder worksheet content, draft schedule entries, and unfinished ethics-book sections before Fall 2026.

- [ ] **Establish reproducibility and provenance rules for assets and datasets.** Require source URLs/licenses, canonical inputs for generator scripts, and documented regeneration commands for shared images and derived datasets.

- [ ] **Set a repository-size strategy.** Review large datasets, PDFs, generated slide support files, and the multi-gigabyte sandbox; decide what belongs in Git, Git LFS, release archives, or ignored local storage. (See the July 2026 audit above for concrete numbers.)

### Discoverability

- [ ] **Add basic SEO metadata across public HTML pages.** Ensure each page has a distinct `<title>`, meta description, canonical URL, and Open Graph tags.

- [ ] **Create crawl/indexing primitives.** Add `sitemap.xml`, `robots.txt`, and structured internal links for slides, worksheets, FAQ, and syllabus pages.

- [ ] **Publish LLM-friendly summaries for major sections.** Add short page-level summaries and clear section headings so course materials are easier for AI search and answer engines to parse.

- [ ] **Add structured data where it helps.** Evaluate `Course`, `CreativeWork`, `FAQPage`, and `BreadcrumbList` schema for the homepage, FAQ, and course materials.

- [ ] **Tighten naming for search intent.** Review page titles, headings, and URLs so they explicitly target queries like `UIC intro to data science`, `CS 418`, `data science worksheets`, and `ethics in data science`.

### Link Audit Notes

- FAQ route status is now a deployment verification task, since `docs/faq.html` exists locally.
- Pending deployment: the new worksheet URL returns `404`, while the old `worksheet-pdfs/` URL still returns `200`.
- Published HTML external-link scan: all other checked links returned `200`; `data-feminism.mitpress.mit.edu` returned `403`, which appears to be automated-request blocking rather than a confirmed dead page.
