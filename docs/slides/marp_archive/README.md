# Marp Archive

Archived Marp slide decks. Build outputs (HTML, PDF, `*_files/`) are not tracked.

## Rebuild

**Prerequisites:** [Marp CLI](https://github.com/marp-team/marp-cli) (`npm install -g @marp-team/marp-cli`) or `npx`.

```bash
cd docs/slides/marp_archive
./build_all_marp.sh
```

HTML and PDF files will be written next to their source `.md` files.
Set `BUILD_PDFS=false` to skip PDFs.
