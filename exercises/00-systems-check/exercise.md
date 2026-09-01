---
summary: Get Python, Jupyter, and Polars running on your own machine
topic: Setup
due: Wednesday, September 16
ai_policy: double-red
---

# Exercise Zero - Systems Check

This exercise is a systems to check to make sure you can set up a Python environment (which you control), run a Jupyter notebook in that environment, and load dataframes via Polars.

## Overview

What you'll do:

1. Create an isolated Python environment (with `uv` or with `venv`) (not required but strongly recommended)
2. Install Jupyter and Polars into that environment.
3. Open a notebook, read in a dataset, and run `.describe()` and a filter on it.
4. Add a text cell that says `nine pizzas`.
5. Restart the kernel, run the whole notebook top to bottom, and submit your `.ipynb` file

## Environments

If you install everything into the one Python that came with your computer, every project shares one pile of libraries, and package versions will collide. You might upgrade something for another project/class and break your setup for another project/class.

A **virtual environment** is just a directory that contains its own Python interpreter and its own site-packages / library installations. Generally, it is advised to create one per project and install packages into it.

There are two common ways to do this:

**[venv](https://docs.python.org/3/library/venv.html)** is part of the Python standard library. You create the environment, *activate* it (which puts its `python` and `pip` first on your shell's `PATH`), and install packages with `pip`. The [Python tutorial's chapter on virtual environments](https://docs.python.org/3/tutorial/venv.html) is the authoritative walkthrough.

**[uv](https://docs.astral.sh/uv/)** is a newer tool that does essentially the same thing, plus package installing, Python version management, lockfiles, and a few other things. It is also supposed to be faster. You do not activate anything, just run `uv add` to record a dependency and `uv run` to run a command inside the project's environment, and uv creates and updates that environment for you. Start with the [installation guide](https://docs.astral.sh/uv/getting-started/installation/) and the [working on projects guide](https://docs.astral.sh/uv/guides/projects/).

I recommend `uv` as it seems to be what most new Python projects are moving to.

### uv basics

```sh
uv init cs418-exercise-0
cd cs418-exercise-0
uv add polars jupyterlab
uv run jupyter lab
```

Line by line:

- `uv init` creates a project folder with a `pyproject.toml` in it.
- `cd` moves you into that folder.
- `uv add` writes the specified dependencies into `pyproject.toml` (plus resolves it into `uv.lock`, and installs it into a `.venv/` directory inside the project)
- `uv run` launches Jupyter inside that environment, and guarantees the command has all the dependencies for that environment


## Tool Overview

**Jupyter** is the notebook interface. Install and launch instructions are at [jupyter.org/install](https://jupyter.org/install); the full documentation lives at [docs.jupyter.org](https://docs.jupyter.org/en/latest/), and [JupyterLab's own installation page](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) covers the lab interface specifically.

	* One habit worth building now is to run **Kernel → Restart Kernel and Run All Cells** to make sure your notebook works before you submit anything. In some cases, your notebook may only "work" because you ran the cells in a specific order, which can make it difficult to grade.

**Polars** is the dataframe library we will use throughout the semester (in place of pandas). It is [pola.rs](https://pola.rs/); the [installation page](https://docs.pola.rs/user-guide/installation/) and the [getting started guide](https://docs.pola.rs/user-guide/getting-started/) are the places to begin, and the [Python API reference](https://docs.pola.rs/api/python/stable/reference/index.html) is what you might want to keep open while working. This exercise only uses three calls: [read_csv](https://docs.pola.rs/api/python/stable/reference/api/polars.read_csv.html), [DataFrame.describe](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.describe.html), and [DataFrame.filter](https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.filter.html).

## Getting a dataset

Use anything in the [datasets folder of the course repository](https://github.com/jackbandy/data-science-fun/tree/main/datasets), or any other dataset you are curious about and have (legal) access to :-)

## Starter code

[`starter.ipynb`](/exercises/00-systems-check/starter/starter.ipynb) ([view on GitHub](https://github.com/jackbandy/data-science-fun/blob/main/exercises/00-systems-check/starter/starter.ipynb)) has one section per graded item, each with a `TODO`.

Here is some code you can use for these items:

```python
import polars as pl

df = pl.read_csv("https://raw.githubusercontent.com/jackbandy/data-science-fun/refs/heads/main/datasets/national-parks-info/us-national-parks.csv")

df.select("latitude", "longitude").describe()

df.filter(pl.col("state") == "UT")
```

Be sure to point `read_csv` to a complete URL or a complete file path to a csv.

## What to submit

One `.ipynb` file, uploaded to Canvas. Submit the notebook *with its outputs saved* — save the file after your final run-all, so we can see what your cells produced.

## Rubric

Six points available. You will get them if:

1. You turned in a `.ipynb` that runs end to end without errors.
2. Your notebook reads a dataset into a dataframe. The dataset can be either a csv from the `datasets/` folder of the course repo, or something else you were interested in looking at.
3. You ran `.describe()` on one or more columns of the data frame.
4. You ran a filter of some kind on the dataframe.
5. You included a text cell that says `nine pizzas`.
6. A free point because it's your first coding exercise.

That is the whole rubric for this "systems check," warm-up exercise. I expect you to get 6 out of 6!

## AI/LLM policy

**Double red — stop and stay.** No AI/LLM use on this exercise. It will be helpful for you to be comfortable setting up a Jupyter notebook "from scratch" for future data science projects. Also, all the code you need is here in this project description.
