<!-- NOTICE: This file was modified by an LLM coding system. -->

# Python Yard: specs

The Python Yard is a Colab-style notebook for the site, reached from the More menu. It launches as a **beta**, labelled "(beta)" in the menu link, the app name (browser tab) and the starter notebook's title and intro. See [PLAN.md](PLAN.md) for the build steps.

- **Engine:** JupyterLite (`jupyterlite-core` 0.8.x) with the Pyodide kernel (`jupyterlite-pyodide-kernel` 0.8.6, which pins Pyodide 314.0.6 / Python 3.14). All code runs in the browser. There is no server and no account.
- **Hosting:** static files on the existing GitHub Pages site at `https://dodatascience.fun/yard/`. The only external services are GitHub (Pages, Actions, raw dataset files) and, unless it is self-hosted, the jsDelivr CDN for Pyodide.
- **Source vs. output:** `docs/yard/` holds only sources (config, build script, starter notebook, these notes). Datasets are not bundled: notebooks read them straight from the repo's `datasets/` folder on GitHub (`raw.githubusercontent.com`), so a dataset must be pushed to `main` before the Yard can read it. The JupyterLite build is generated in CI into `_site/yard/` and is never committed.
- **Entry point:** the "Python Yard" link in the More menu opens the Notebook view (the closest to Colab) on a starter notebook in a new tab, like Timer and Mini-Book do.
- **Libraries that must work:** `polars` (1.33.1 in this Pyodide), `numpy`, `pandas`, `matplotlib`, `scipy`, `statsmodels`, `scikit-learn` and `networkx`, all with a plain `import`.
- **Libraries that should work:** `plotnine` and `seaborn` via `%pip install` (pure Python, from PyPI at runtime). `pymc` is out of scope.
- **Content shipped:** a starter notebook, course CSVs read by URL from `datasets/` (keep the ones notebooks use small; the demo uses `datasets/cta-ridership/Station_Entries_UIC-Halsted_2025.csv`, 17 KB) and the executed `docs/slides/weekN.ipynb` notebooks copied in at build time.
	- the default should be a short welcome notebook with an  imports cell and a hello world cell
	- below those, a collapsed demo section (reads UIC-Halsted's 2025 daily entries from GitHub and plots them), then a "tinker zone" of empty cells
	- it should be easy to load any weekN notebook
- **Persistence:** edits are saved in the student's own browser storage only. Students download `.ipynb` files to keep their work, and the starter notebook says so.
- **Performance:** the first visit downloads roughly 30+ MB of wheels (polars alone is about 18 MB). Later visits load from the browser cache.
- **Browsers:** it must work in current Safari, Firefox and Chrome on desktop. On phones it only needs to load and run a cell.
- **Upkeep:** pin both JupyterLite packages in one requirements file and bump them once per semester.
