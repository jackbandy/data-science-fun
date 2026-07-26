---
title: "Week 4 (CS 418 @ UIC)"
format:
  revealjs:
    footer: '<img src="../assets/branding/uic-black-logo.svg" alt="UIC logo"> <img src="../assets/branding/cc-by-nc-sa-small.svg" alt="CC BY-NC-SA"> <span class="footer-text">CS 418, Intro to Data Science, Week 4</span><span class="footer-text"><a href="https://dodatascience.fun/slides/week4.html">dodatascience.fun/slides/week4</a></span>'
---

# Week 4 Slide Deck {.course-title}

## Exploratory Analysis; Descriptive Stats

Jack Bandy
2026

---

# Exploratory Data Analysis {.course-title .photo-title data-state="photo-title" background-image="../assets/orange-line-stops-better/stop04-washington-wells-b.jpg" background-size="cover"}

CS 418 · Week 4 · 🟠 Washington/Wells 🟠

---

# Demo Content Slide

Placeholder content for Week 4.

- Exploratory analysis
- Descriptive statistics
- Initial data questions

---

# What is Exploratory Data Analysis? {.smaller}

- Exploratory Data Analysis (EDA) is the process of exploring and analyzing data to better understand it, discover patterns, identify potential issues, and determine the best approach for building predictive models.


- The main tools of exploratory data analysis are:
  - **Summary Statistics** (mean, median, spread, counts)
  - **Visualization** (histograms, box plots, scatter plots)

---

# Why Exploratory Data Analysis matters?

::: {.incremental}
- Identify trends patterns 
- Discover relationship between variables
- Test underlying assumptions
- Ensure the data is suitable for further analysis
:::

---

# Steps
- The steps of exploratory data analysis are:
  1. Data Collection and Loading (setting up your environment)
  2. Summary Statistics (*describe()* using pandas)
  3. Handling anomalies (e.g missing data)
  4) Understanding the shape of the data 
  5) Detecting outliers
  6) Correlation Analysis

---

# Discovering and handling anomalies {.smaller}
This is one of the crucial steps in EDA, because if not handled properly can introduce bias.

- Categories:
  - Missing value (e.g nulls, N/A, NaN)
  - Duplicates (multiple rows with same values)
  - Incosistent formatig (e.g "yyyy/dd/mm" vs "mm/dd/yyyy")
  - Wrong data types (dates stored as strings, numbers stores as string)
  - Invalid values (e.g age = 350)
  - Structure issues (mixed units: miles vs km)

---

# Descriptive Statistics

::: {.incremental}
- Summarize and describe what's in the data.
- **Center:** Mean, median, mode.
- **Spread:** Maximum, Minimum, Range, Standard deviation, Variance.
- **Position:** Quartiles and percentiles.
:::

---

# Measures of Center

- **Mean** — the average of all the values.
- **Median** — the middle value of the sorted data.
- **Mode** — the most frequent value (can be more than one).

**Example** A = {7, 9, 9, 12, 13}

**Mean =** (7 + 9 + 9 + 12 + 13) / 5 = 10  
**Median =** 9  
**Mode =** 9

---

# Measures of Center

::: {style="font-size:0.6em; font-style:normal; color:#1f8a9b; font-weight:700; margin-top:-0.3em;"}
Using Python
:::

With a pandas DataFrame, each measure is one method call:

- `DataFrame.mean()` — the mean
- `DataFrame.median()` — the median
- `DataFrame.mode()` — the mode

---

# Measures of Spread

:::: {.columns}
::: {.column width="20%"}

<table style="border-collapse:collapse; margin:0.2em 26px 0 auto;">
<tr><td style="border:2px solid #f9461c; background:#f9461c; color:#fff; font-weight:bold; padding:6px 22px; text-align:center;">Grades</td></tr>
<tr><td style="border:2px solid #f9461c; padding:6px 30px; text-align:center;">24</td></tr>
<tr><td style="border:2px solid #f9461c; padding:4px 30px; text-align:center;"><span style="display:inline-block; border:3px solid #1f2d3d; border-radius:50%; width:50px; height:50px; line-height:50px; font-weight:bold;">35</span></td></tr>
<tr><td style="border:2px solid #f9461c; padding:6px 30px; text-align:center;">32</td></tr>
<tr><td style="border:2px solid #f9461c; padding:4px 30px; text-align:center;"><span style="display:inline-block; border:3px solid #1f2d3d; border-radius:50%; width:50px; height:50px; line-height:50px; font-weight:bold;">21</span></td></tr>
<tr><td style="border:2px solid #f9461c; padding:6px 30px; text-align:center;">28</td></tr>
</table>

::: {style="font-size:0.5em; text-align:center; margin-top:0.6em; line-height:1.6;"}
[Maximum = 35]{style="color:#1f2d3d; font-weight:bold;"}<br>
[Minimum = 21]{style="color:#1f2d3d; font-weight:bold;"}
:::

:::
::: {.column width="80%"}

::: {style="font-size:0.82em;"}
**Maximum** — The largest value in the data set.

**Minimum** — The smallest value in the data set.

**Range** — How far the data stretches, end to end.
:::

::: {style="text-align:center; margin-top:1.2em;"}
$$\text{Range} = \text{Max} - \text{Min} = 35 - 21 = 14$$
:::

:::
::::

---

# Measures of Spread

:::: {.columns}
::: {.column width="20%"}

<table style="border-collapse:collapse; margin:0.2em 26px 0 auto;">
<tr><td style="border:2px solid #f9461c; background:#f9461c; color:#fff; font-weight:bold; padding:6px 22px; text-align:center;">Grades</td></tr>
<tr><td style="border:2px solid #f9461c; padding:6px 30px; text-align:center;">24</td></tr>
<tr><td style="border:2px solid #f9461c; padding:6px 30px; text-align:center;">35</td></tr>
<tr><td style="border:2px solid #f9461c; padding:6px 30px; text-align:center;">32</td></tr>
<tr><td style="border:2px solid #f9461c; padding:6px 30px; text-align:center;">21</td></tr>
<tr><td style="border:2px solid #f9461c; padding:6px 30px; text-align:center;">28</td></tr>
</table>

::: {style="font-size:0.5em; text-align:right; margin-top:0.6em; line-height:1.6;"}
[Variance = 32.5]{style="color:#000000; font-weight:bold;"}<br>
[Standard Deviation ≈ 5.7]{style="color:#000000; font-weight:bold;"}
:::

:::
::: {.column width="80%"}

::: {style="font-size:0.82em;"}
**Standard deviation** — The typical distance from the mean, in the data's own units.

**Variance** — The variance of a dataset is the square of the standard deviation.

Mean $\bar{x} = 28$.
:::

::: {style="text-align:center; margin-top:1.2em;"}
$$\begin{aligned}
s^2 &= \frac{\sum (a_i-\bar{x})^2}{n-1} = \frac{130}{4} = 32.5 \\[6pt]
s &= \sqrt{32.5} \approx 5.7
\end{aligned}$$
:::

:::
::::

---

# Measures of Position 

:::: {.columns}

::: {.column width="32%"}
<table style="border-collapse:collapse; margin:0.4em auto 0;">
<tr><td style="border:2px solid #f9461c; background:#f9461c; color:#fff; font-weight:bold; padding:6px 24px; text-align:center;">Grades (sorted)</td></tr>
<tr><td style="border:2px solid #f9461c; padding:6px 24px; text-align:center;">21</td></tr>
<tr><td style="border:2px solid #f9461c; padding:4px 24px; text-align:center;"><span style="display:inline-block; border:3px solid #001E62; border-radius:50%; width:50px; height:50px; line-height:50px; color:#1f2d3d; font-weight:bold;">24</span></td></tr>
<tr><td style="border:2px solid #f9461c; padding:4px 24px; text-align:center;"><span style="display:inline-block; border:3px solid #001E62; border-radius:50%; width:50px; height:50px; line-height:50px; color:#1f2d3d; font-weight:bold;">28</span></td></tr>
<tr><td style="border:2px solid #f9461c; padding:4px 24px; text-align:center;"><span style="display:inline-block; border:3px solid #001E62; border-radius:50%; width:50px; height:50px; line-height:50px; color:#1f2d3d; font-weight:bold;">32</span></td></tr>
<tr><td style="border:2px solid #f9461c; padding:6px 24px; text-align:center;">35</td></tr>
</table>
:::

::: {.column width="68%"}

::: {style="font-size:0.8em;"}
**Percentiles** divide a dataset into 100 equal parts such that n% of the data is less than or equal to the nth percentile.

**Quartiles** divide a dataset into quarters.

- First quartile (Q1) = 25% or less of the data.
- Second quartile (Q2) = 50% or less of the data / Median.
- Third quartile (Q3) = 75% or less of the data.
:::

<div style="text-align:center; margin-top:0.6em;">
<span style="display:inline-block; border:2px solid #001E62; border-radius:6px; padding:6px 18px; margin:0 6px; font-weight:bold; color:#1f2d3d;">Q1 = 24</span>
<span style="display:inline-block; border:2px solid #001E62; border-radius:6px; padding:6px 18px; margin:0 6px; font-weight:bold; color:#1f2d3d;">Q2 = 28</span>
<span style="display:inline-block; border:2px solid #001E62; border-radius:6px; padding:6px 18px; margin:0 6px; font-weight:bold; color:#1f2d3d;">Q3 = 32</span>
</div>
:::

::::

---

# Sources {.sources}

1. GitHub source: <https://github.com/jackbandy/data-science-fun/blob/main/docs/slides/week4.md>.
2. Slides developed using materials from [Elena Zheleva](https://www.cs.uic.edu/~elena/) and [Gonzalo Bello Lander](https://cs.uic.edu/profiles/gonzalo-bello/), the Berkeley DS 100 team, Marine Carpuat, and Brian Ziebart.
3. Slide deck built with [Quarto](https://quarto.org/) revealjs.
4. Title font is Big Shoulders; Body font is [Libre Franklin](https://en.wikipedia.org/wiki/Franklin_Gothic#Libre_Franklin).
