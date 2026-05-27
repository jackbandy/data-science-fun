# Slides

Run `./build_all_marp.sh` in this folder to generate Marp slide output files (`.html` and `.pdf`) for every Marp Markdown file.

If updated .md, the repository will use `package.json` to install the Marp CLI dependency and run GitHub Actions, though it still uses the same `build_all_marp.sh` build path for slide outputs.

Run `./build_all_quarto.sh` to generate Quarto revealjs output files (`.html` and `.pdf`) for every `.qmd` file.

Quarto revealjs HTML depends on the generated `*_files/` support directories for CSS and JavaScript. Those directories must be committed for GitHub Pages; otherwise the deployed HTML loads without its Reveal/Quarto styles.
