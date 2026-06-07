# Slides

Run `./build_all_quarto.sh` to generate Quarto revealjs output files (`.html` and `.pdf`) for every slide source in this directory. Set `BUILD_PDFS=false` to rebuild HTML only.

Quarto revealjs HTML depends on the generated `*_files/` support directories for CSS and JavaScript. Those directories must be committed for GitHub Pages; otherwise the deployed HTML loads without its Reveal/Quarto styles.

The slide theme uses Big Shoulders for title headings and a Franklin-style sans stack for body and footer text. The repo self-hosts Libre Franklin from `impallari/Libre-Franklin` as the libre body-font asset used across the decks.
