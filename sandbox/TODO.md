# Repository TODO

~~note to self - check mobile version of slides~~ (done — see mobile fix below)

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

- [ ] **Delete `docs/assets/orange-line-stops-photos/` (remaining ~29 files).** Nothing references it except its own `SOURCES.md`; all decks use `orange-line-stops-better/` instead. Removing it further shrinks the deployed Pages artifact. If any photos are worth keeping for later, move them to `sandbox/ignore/`. *(July 2, 2026: the 14 byte-identical duplicates of `orange-line-stops-better/` files were deleted.)*
- [ ] **Web-optimize the large JPGs that ship to Pages.** A dozen tracked images are 6–19 MB (`orange-line-stops-better/stop05-clark-lake-a.jpg` 18.5 MB, several `near-orange-line-stops/` and `art/` files 8–13 MB). Slides load these full-size. Resize to ~2000px max dimension at quality ~80 (typically <500 KB each); keep originals in `sandbox/ignore/` if provenance matters. `docs/` tracked content is currently ~446 MB against GitHub Pages' 1 GB soft limit.
- [x] **Git history is 1.0 GB, mostly dead slide PDFs.** *(July 2, 2026: rewrote history with `git filter-repo --path-glob 'docs/slides/*.pdf' --invert-paths` and force-pushed. Any old clones must be re-cloned; commit hashes changed.)*
- [ ] **Untrack `sandbox/scripts/ethics-reference-check-cache.json` (6.9 MB).** It's a script cache, not source; `git rm --cached` it and add to `.gitignore`.

### CI / deploy workflow (`.github/workflows/deploy-pages.yml`)

- [x] **Slides cache can restore stale sources over the fresh checkout.** *(July 2, 2026: cache path narrowed to outputs only — `docs/slides/week*.html`, `week*_files`, `_libs` — so tracked sources can no longer be clobbered by a stale restore.)*
- [x] **Stop cloning full history on every deploy.** *(July 2, 2026: added `filter: blob:none` to the checkout step; full commit graph is kept for the changed-files diff but historic blobs are no longer downloaded.)*
- [x] **Python deps installed twice in CI.** *(July 2, 2026: `build_all_quarto.sh` now honors `SKIP_VENV=true`, and both CI render steps set it, so CI uses the system-wide `uv pip install` only.)*
- [ ] **Pin `docs/slides/requirements.txt`.** Only two loose upper bounds (`matplotlib<3.9`, `arviz<0.20`); everything else floats, so CI renders can drift between runs. Pin exact versions (or commit a `uv lock` / `requirements.lock`) for reproducible deck output.

### Simplification / cruft

- [ ] **Retire the Marp dependency.** `package.json`'s only dependency is `@marp-team/marp-cli` (124 MB `node_modules`), used solely by the archived `docs/slides/marp_archive/build_all_marp.sh`. Remove `package.json`/`package-lock.json`/`node_modules` and document `npx @marp-team/marp-cli` in the archive README for the rare rebuild. Also consider moving `marp_archive/` (11 MB, tracked) out of `docs/` so it stops deploying to the public site.
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

- [ ] **Fix the lifecycle font source path.** `docs/assets/lifecycle/make_lifecycle_figures.py` still checks the pre-move path `../../../slides/...`; change it to the current shared font location under `docs/slides/theme/fonts/`.

- [ ] **Remove transient files from shared assets.** Delete `docs/assets/lifecycle/__pycache__/` and `docs/assets/triangles/.DS_Store`, then confirm `.gitignore` continues to exclude both patterns.

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
