# Slides

Run `./build_all_quarto.sh` to generate Quarto revealjs output files (`.html` and `.pdf`) for every `.qmd` and `.md` slide file.

Quarto revealjs HTML depends on the generated `*_files/` support directories for CSS and JavaScript. Those directories must be committed for GitHub Pages; otherwise the deployed HTML loads without its Reveal/Quarto styles.
