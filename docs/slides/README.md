# Slides

Run `./build_all_quarto.sh` to generate Quarto revealjs output files (`.html` and `.pdf`) for every `.qmd` and `.md` slide file.

Quarto revealjs HTML depends on the generated `*_files/` support directories for CSS and JavaScript. Those directories must be committed for GitHub Pages; otherwise the deployed HTML loads without its Reveal/Quarto styles.

The slide theme uses Big Shoulders for title headings and an ITC Franklin Gothic stack for body and footer text. ITC Franklin Gothic is commercial, so the repo self-hosts Libre Franklin from `impallari/Libre-Franklin` as the permissively licensed fallback.
