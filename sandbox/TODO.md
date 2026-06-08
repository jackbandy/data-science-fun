# Repository TODO

note to self - check mobile version of slides

LLM review performed June 5, 2026:

## Recently Completed

- [x] **Correct dataset filenames in three READMEs.** Updated `datasets/chicago-l-stations/README.md`, `datasets/chicago-tall-buildings/README.md`, and `datasets/cta-ridership/README.md` so their documented CSV names match the files actually present.

- [x] **Clean up the ethics mini-book README.** Removed the unsupported `uv pip install` guidance and documented that reusable assets live in `docs/assets/` while generated `book/` output is not source material.

- [x] **Archive the old Orange Line standalone page.** The earlier Orange Line page and its support files now live under `sandbox/orange-line-v1/` instead of remaining as an active docs page.

## Quick Tasks

Each item should fit in a focused 5-10 minute pass.

- [ ] **Verify the published FAQ route after the next deploy.** `docs/faq.html` now exists locally; confirm that `https://dodatascience.fun/faq.html` returns `200` after deployment and that the homepage link resolves correctly in production.

- [ ] **Verify the worksheet URL after the next deployment.** Confirm that `https://dodatascience.fun/worksheets/00-worksheet-template.pdf` returns `200`, then check that no public page still references the old `worksheet-pdfs/` path.

- [ ] **Restore the missing subpixel generator input.** `docs/assets/subpixels/make_pixel_assets.py` expects `lcd-pixel-macro-2023.jpg`, which is absent. Restore the source image or update the script to use an existing canonical input, then run it once.

- [ ] **Fix the lifecycle font source path.** `docs/assets/lifecycle/make_lifecycle_figures.py` still checks the pre-move path `../../../slides/...`; change it to the current shared font location under `docs/slides/theme/fonts/`.

- [ ] **Remove transient files from shared assets.** Delete `docs/assets/lifecycle/__pycache__/` and `docs/assets/triangles/.DS_Store`, then confirm `.gitignore` continues to exclude both patterns.

- [ ] **Resolve the remaining ethics-book asset exceptions.** Move `cc-by-nc-sa.svg` and `dikw-pyramid.svg` out of `docs/ethics-in-data-science/assets/`, remove unused files, or revise `NOTE.md` to document why they remain.

- [ ] **Trim stale link-audit notes after verification.** Once the FAQ and worksheet routes are confirmed after deployment, update or remove the outdated notes at the bottom of this file.

## Big-Picture Work

- [ ] **Unify build and deployment automation.** Decide whether GitHub Actions should build the book, slides, syllabus, and worksheets from source, rather than mixing automated builds with committed generated outputs.

- [ ] **Choose one generated-output policy for slides.** Slides currently keep Markdown, HTML, PDF, and large Quarto support directories together under `docs/`; define which artifacts are source-controlled and which are generated during deployment.

- [ ] **Create a release-readiness pass for course content.** Track and replace syllabus `TK` fields, placeholder worksheet content, draft schedule entries, and unfinished ethics-book sections before Fall 2026.

- [ ] **Establish reproducibility and provenance rules for assets and datasets.** Require source URLs/licenses, canonical inputs for generator scripts, and documented regeneration commands for shared images and derived datasets.

- [ ] **Set a repository-size strategy.** Review large datasets, PDFs, generated slide support files, and the multi-gigabyte sandbox; decide what belongs in Git, Git LFS, release archives, or ignored local storage.

## Discoverability

- [ ] **Add basic SEO metadata across public HTML pages.** Ensure each page has a distinct `<title>`, meta description, canonical URL, and Open Graph tags.

- [ ] **Create crawl/indexing primitives.** Add `sitemap.xml`, `robots.txt`, and structured internal links for slides, worksheets, FAQ, and syllabus pages.

- [ ] **Publish LLM-friendly summaries for major sections.** Add short page-level summaries and clear section headings so course materials are easier for AI search and answer engines to parse.

- [ ] **Add structured data where it helps.** Evaluate `Course`, `CreativeWork`, `FAQPage`, and `BreadcrumbList` schema for the homepage, FAQ, and course materials.

- [ ] **Tighten naming for search intent.** Review page titles, headings, and URLs so they explicitly target queries like `UIC intro to data science`, `CS 418`, `data science worksheets`, and `ethics in data science`.

## Link Audit Notes

- FAQ route status is now a deployment verification task, since `docs/faq.html` exists locally.
- Pending deployment: the new worksheet URL returns `404`, while the old `worksheet-pdfs/` URL still returns `200`.
- Published HTML external-link scan: all other checked links returned `200`; `data-feminism.mitpress.mit.edu` returned `403`, which appears to be automated-request blocking rather than a confirmed dead page.
