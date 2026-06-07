# Repository TODO

note to self - check mobile version of slides

LLM review performed June 5, 2026:

## Quick Tasks

Each item should fit in a focused 5-10 minute pass.

- [ ] **Publish the FAQ at the linked route.** `docs/index.html` links to `faq.html`, but the deployed URL currently returns `404` because `docs/faq.md` is not rendered by the custom Pages workflow. Generate `docs/faq.html` or change the link and publishing approach.

- [ ] **Verify the worksheet URL after the next deployment.** Confirm that `https://dodatascience.fun/worksheets/00-worksheet-template.pdf` returns `200`, then check that no public page still references the old `worksheet-pdfs/` path.

- [ ] **Correct dataset filenames in three READMEs.** Update `datasets/chicago-l-stations/README.md`, `datasets/chicago-tall-buildings/README.md`, and `datasets/cta-ridership/README.md` so their documented CSV names match the files actually present.

- [ ] **Restore the missing subpixel generator input.** `docs/assets/subpixels/make_pixel_assets.py` expects `lcd-pixel-macro-2023.jpg`, which is absent. Restore the source image or update the script to use an existing canonical input, then run it once.

- [ ] **Fix the lifecycle font source path.** `docs/assets/lifecycle/make_lifecycle_figures.py` still checks the pre-move path `../../../slides/...`; change it to the current shared font location under `docs/slides/theme/fonts/`.

- [ ] **Remove transient files from shared assets.** Delete `docs/assets/lifecycle/__pycache__/` and `docs/assets/triangles/.DS_Store`, then confirm `.gitignore` continues to exclude both patterns.

- [ ] **Resolve the remaining ethics-book asset exceptions.** Move `cc-by-nc-sa.svg` and `dikw-pyramid.svg` out of `docs/ethics-in-data-science/assets/`, remove unused files, or revise `NOTE.md` to document why they remain.

- [ ] **Refresh the slide workflow section in `README.md`.** Replace the stale “Marp slides” directory description and nonexistent `week0quarto.qmd` example with the current Quarto decks plus archived Marp workflow.

- [ ] **Clean up the ethics mini-book README.** Remove the unsupported `uv pip install` guidance and document that reusable assets live in `docs/assets/` while generated `book/` output is ignored.

- [ ] **Decide whether the standalone Orange Line page is still needed.** `docs/orange-line-schedule.html` and its CSS/JS are no longer linked because the homepage iframe is commented out. Restore a visible link or remove the orphaned page and support files.

## Big-Picture Work

- [ ] **Unify build and deployment automation.** Decide whether GitHub Actions should build the book, slides, syllabus, and worksheets from source, rather than mixing automated builds with committed generated outputs.

- [ ] **Choose one generated-output policy for slides.** Slides currently keep Markdown, HTML, PDF, and large Quarto support directories together under `docs/`; define which artifacts are source-controlled and which are generated during deployment.

- [ ] **Create a release-readiness pass for course content.** Track and replace syllabus `TK` fields, placeholder worksheet content, draft schedule entries, and unfinished ethics-book sections before Fall 2026.

- [ ] **Establish reproducibility and provenance rules for assets and datasets.** Require source URLs/licenses, canonical inputs for generator scripts, and documented regeneration commands for shared images and derived datasets.

- [ ] **Set a repository-size strategy.** Review large datasets, PDFs, generated slide support files, and the multi-gigabyte sandbox; decide what belongs in Git, Git LFS, release archives, or ignored local storage.

## Link Audit Notes

- Confirmed dead: `https://dodatascience.fun/faq.html` returns `404`.
- Pending deployment: the new worksheet URL returns `404`, while the old `worksheet-pdfs/` URL still returns `200`.
- Published HTML external-link scan: all other checked links returned `200`; `data-feminism.mitpress.mit.edu` returned `403`, which appears to be automated-request blocking rather than a confirmed dead page.
