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
- **Add packages:** `uv pip install <package>` (if using venv)


## Structure

- `index.md` - Book home page
- `_quarto.yml` - Book configuration
- `references.bib` - Bibliography (BibTeX)
- `book/` - Built HTML output for local preview and Pages deployment


## Resources

- [Quarto Books Guide](https://quarto.org/docs/books/)
- [Pandoc Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown)
