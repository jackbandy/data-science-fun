# Ethics in Data Science

A Quarto mini-book that lives in `docs/ethics-in-data-science/` and renders to `book/`.


## Quick Start

```bash
# Preview locally with live reload
quarto preview

# Build the book
quarto render
```


## Development

- **Preview locally:** `quarto preview` (opens at http://localhost:3000)
- **Build static HTML:** `quarto render`
- **Output location:** `book/` folder
- **Deployment:** GitHub Pages re-renders this book during the site deploy workflow


## Structure

- `index.md` - Book home page
- `_quarto.yml` - Book configuration
- `references.bib` - Bibliography (BibTeX)
- `book/` - Built HTML output for local preview; generated output and not source material
- `assets/` - Book-specific assets that still live alongside this mini-book


## Assets and Output

- Reusable shared assets for this book live in `docs/assets/` (for example `lifecycle/`, `triangles/`, `subpixels/`, and `art/`).
- The local `book/` directory is generated output from Quarto, intended for preview/build artifacts rather than hand-edited source content.
- Book source files live in `docs/ethics-in-data-science/`; update those files rather than editing generated HTML in `book/`.


## Resources

- [Quarto Books Guide](https://quarto.org/docs/books/)
- [Pandoc Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown)
