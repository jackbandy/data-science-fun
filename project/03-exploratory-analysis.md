---
summary: Explore your datasets with summary statistics and descriptive visualizations, and let what you find sharpen your questions
topic: Exploratory analysis
due: Monday, October 12
ai_policy: yellow-over-red
---

# Checkpoint Three: Exploratory Analysis

Your group now has data loaded into dataframes. This checkpoint is about exploring the data: getting familiar with them before you try to infer or confirm anything.

In [Tukey's words](https://www.stat.berkeley.edu/~brill/Papers/EDASage.pdf), exploratory data analysis (EDA) is "an attitude, a state of flexibility, a willingness to look for those things that we believe are not there, as well as those we believe to be there."

For effective EDA you should expect the unexpected. That is, don't be surprised if you find some surprises. There is still time to adjust your questions and/or your datasets, so take advantage of these surprises now rather than later!

## What to do

Work in the same GitHub repository as the data acquisition checkpoint.

1. **Profile each primary dataset.** For each one, report `df.shape`, `df.glimpse()` (or `df.schema`), `df.null_count()`, and `df.describe()`, and write about anything that stands out.
2. **Make note of anomalies.** Look for missing values, duplicates, inconsistent formatting, wrong data types, invalid values, and mixed units. For each one you find, note what it is, how many rows it affects, and what you did about it (fixed it, dropped the rows, or left it and flagged it).
3. **Look at distributions.** Make at least one plot of the distribution of each feature that matters to your research questions (histogram, box plot, bar chart of counts, etc.), and describe its shape: center, spread, skew, outliers, etc.
4. **Look at relationships.** Make at least three plots that relate two or more features, chosen with your research questions in mind: a scatter plot, a comparison across subgroups, a time series, or a correlation matrix. If you have a secondary dataset, at least one of these should use the join or comparison you described in the last checkpoint.
5. **Answer "so what?"** For each plot in step 4, write a few sentences on what it shows and why it matters for your research questions. Did you have reason to expect what you see? Note if  a given pattern was expected or unexpected (or somewhere in between).
6. **Answer "what next?"** For each plot in step 4, name the question it points to next: an additional comparison, a subgroup to split out, another dataset to join, or a domain expert to ask. Then restate your research questions, revised if the data has nudged them, and say what changed and why.

The [guiding questions from week 4](/slides/week4.html#/questions-to-guide-exploration) are a good place to start:

- How are the values of feature X distributed?
- How do X and Y relate to each other?
- Is the distribution of X the same across subgroups defined by Z?
- Are there unusual observations in X? In the pair (X, Y)? In X within a subgroup of Z?

A few reminders from week 5: label your axes at a readable size, watch for overplotting on large datasets, and remember that a chart showing two things moving together does not show that one causes the other.

## What to turn in (i.e. what to put in the repo)

- A notebook, `eda.ipynb`, that runs from top to bottom and produces every table and plot. Keep the code, outputs, and your written notes together, with a markdown cell next to each plot.
	- You are not limited to one notebook! In fact, it's a good idea for each team member to run their own exploratory analysis, before writing a unified `eda.ipynb`
- An `EDA.md` document that summarizes all six steps above: a profile of each primary dataset, the anomalies you found and what you did about them, the shapes of the key distributions, the relationships you plotted, and the "so what?" and "what next?" for each, with the notebook plots each point comes from.
- An update to `README.md` with a short "Exploratory analysis" section. Include basics about the datasets, your revised research questions, the anomaly notes from step 2 (a table works), as well as any particularly significant findings.

As before, every group member should have at least one commit for this checkpoint.

## What to submit

One submission per group in Canvas: the **URL of your group's GitHub repository**. Any group member can submit.

## Rubric

Six points available (one for each step above):

1. Dataset profiles: each primary dataset has its shape, types, missing values, and summary statistics reported, with a note on what stands out.
2. Anomalies: each anomaly is noted with what it is, how many rows it affects, and what was done about it.
3. Distributions: each feature that matters to the research questions has a distribution plot with readable labels and a description of its shape.
4. Relationships: at least three plots relate two or more features, chosen with the research questions in mind, including the join or comparison with a secondary dataset if you have one.
5. So what: each relationship plot has a written explanation of what it shows and why it matters for the research questions.
6. What next: each relationship plot names the question it points to next, and the research questions are restated, with any revisions explained.

## AI/LLM policy

**Yellow over red. Proceed with caution on the main route. Stop ahead.**

🟡 You may use AI/LLM-based tools for the mechanics of plotting and data handling. For example, looking up the right polars or plotting functions, parsing columns, augmenting columns, fixing axis labels, etc.

🔴 You may not use AI/LLM-based tools to update your README.md or write your EDA.md. The "so what?" and "what next?" notes, the anomaly notes, and the revised research questions should come from the your own squishy, fleshy, bloody brains.

Furthermore, as with the data acquisition checkpoint, do not use statistics or plot descriptions from an LLM. Every number and every observation should come from verifiable code that can be traced. For example, don't ask ChatGPT "how many rows are in this dataset" - use `df.shape`.
