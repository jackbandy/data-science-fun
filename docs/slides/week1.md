---
title: "Week 1 (CS 418 @ UIC)"
format:
  revealjs:
    footer: '<img src="../assets/branding/uic-black-logo.svg" alt="UIC logo"> <img src="../assets/branding/cc-by-nc-sa-small.svg" alt="CC BY-NC-SA"> <span class="footer-text">CS 418, Intro to Data Science, Week 1</span><span class="footer-text"><a href="https://dodatascience.fun/slides/week1.html">dodatascience.fun/slides/week1</a></span>'
---

# Week 1 Slide Deck {.course-title}

## Intro, Stats Review; Data Science Lifecycle

Jack Bandy
2026

---


# {.photo-only data-state="photo-only" background-image="../assets/orange-line-stops-better/stop01-harold-washington-library-a.jpg" background-size="cover"}

---

# Demo Content Slide

Placeholder content for Week 1.

- Course introduction
- Statistics review
- Data science lifecycle

---

# What is Data Science?

[**Data science**]{style="color:#001E62;"} is an [**interdisciplinary**]{style="color:#f9461c;"} field that studies and applies tools and techniques for [**deriving useful insights from data**]{style="color:#f9461c;"}.

::::: {.columns}

:::: {.column width="26%"}
::: {style="font-size:0.7em; text-align:center; margin-top:1.4em;"}
It uses techniques from [**computer science**]{style="color:#c0392b;"} and [**statistics**]{style="color:#c0392b;"}…
:::
::::

:::: {.column width="48%"}
<img src="../assets/week1-intro-data-science/venn-rgb.svg" alt="Venn diagram: computer science, math and statistics, and domain knowledge overlapping at data science" style="max-height:350px; width:auto; max-width:100%; display:block; margin:0 auto;">
::::

:::: {.column width="26%"}
::: {style="font-size:0.7em; text-align:center; margin-top:1.4em;"}
…to find patterns and explain relationships using data from different [**domains**]{style="color:#c0392b;"}.
:::
::::

:::::

::: {style="text-align:center; font-size:0.5em; color:#565a5c; margin-top:0.3em;"}
Source: Drew Conway, The Data Science Venn Diagram (2010)
:::

---

# Why Data Science?

:::: {style="max-width:88%; margin:0 auto; height:100%; display:flex; flex-direction:column; justify-content:flex-start; padding-top:2%;"}

::: {style="background:#001E62; border-radius:20px; padding:1.2em 0.9em; text-align:center;"}
[~400 million]{style="display:block; font-size:3em; font-weight:800; color:#f9461c; line-height:1.05;"}
[terabytes of data created — every single day]{style="font-size:1.1em; color:#ffffff;"}
:::

::: {style="text-align:center; font-size:0.5em; color:#565a5c; margin-top:0.4em;"}
Source: [Exploding Topics](https://explodingtopics.com/blog/data-generated-per-day)
:::

::: {style="text-align:center; margin-top:0.6em; font-size:0.7em;"}
**Data science is how we turn that flood into answers and insights**
:::

::::

# Why Data Science? {.image-frame-slide}

<img src="../assets/week1-intro-data-science/role-of-data-science.svg" alt="Hub-and-spoke diagram: data science at the center linked to healthcare, transportation, finance, climate science, public safety, and scientific research" class="r-stretch" style="border:none; box-shadow:none; background:transparent;">

---

# What Do Data Scientists Do?

::: {.incremental}
1. **Ask the right question** — turn a vague goal into something measurable
2. **Get & clean the data** — collect, merge, and fix messy real-world data
3. **Explore & visualize** — hunt for patterns, outliers, and surprises
4. **Model & predict** — build something that explains or forecasts
5. **Communicate** — turn results into decisions people can act on
:::

---

# Statistics review {.section-header}

---

# Our Roadmap

Five things we'll cover:

::: {.incremental}
1. **Role of statistics in data science**
2. **Descriptive statistics**
3. **Probability**
4. **Distributions**
5. **Sampling**
:::

---

# Role of Statistics in Data Science

::: {.incremental}
- Statistics is the science of learning from data under uncertainty.
- It turns raw numbers into evidence we can actually trust.
- It tells us what a sample says about the whole population.
- It underpins every stage of the data science lifecycle.
:::

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

# Data Science Lifecycle {.section-header}

---

# The Data Science Lifecycle {.image-frame-slide}

<img src="../assets/lifecycle/ds-lifecycle-v0.svg" alt="Data science lifecycle diagram: ask a question, obtain data, understand the data, understand the world, and reports/decisions/solutions, connected by arrows in a cycle">

---

# The Data Science Lifecycle {.image-frame-slide}

<img src="../assets/lifecycle/ds-lifecycle-v1.svg" alt="Data science lifecycle with the 'ask a question' stage highlighted">

---

# The Data Science Lifecycle {.image-frame-slide}

<img src="../assets/lifecycle/ds-lifecycle-v2.svg" alt="Data science lifecycle with the 'obtain data' stage highlighted">

---

# The Data Science Lifecycle {.image-frame-slide}

<img src="../assets/lifecycle/ds-lifecycle-v3.svg" alt="Data science lifecycle with the 'understand the data' stage highlighted">

---

# The Data Science Lifecycle {.image-frame-slide}

<img src="../assets/lifecycle/ds-lifecycle-v4.svg" alt="Data science lifecycle with the 'understand the world' stage highlighted">

---

# The Data Science Lifecycle {.image-frame-slide}

<img src="../assets/lifecycle/ds-lifecycle-v5.svg" alt="Data science lifecycle with the 'reports, decisions, solutions' stage highlighted">

---

# The DIKW Pyramid {.section-header}


---

# The DIKW Pyramid {.image-frame-slide}

<img src="../assets/pyramid/01-dikw-pyramid-blank.svg" alt="A blank pyramid outline for the data–information–knowledge–wisdom hierarchy">

---

# The DIKW Pyramid {.image-frame-slide}

<img src="../assets/pyramid/02-dikw-pyramid-divided.svg" alt="The DIKW pyramid divided into four horizontal layers">

---

# The DIKW Pyramid {.image-frame-slide}

<img src="../assets/pyramid/03-dikw-pyramid-data.svg" alt="The DIKW pyramid with the bottom 'data' layer labeled">

---

# The DIKW Pyramid {.image-frame-slide}

<img src="../assets/pyramid/04-dikw-pyramid-data-info.svg" alt="The DIKW pyramid with the 'data' and 'information' layers labeled">

---

# The DIKW Pyramid {.image-frame-slide}

<img src="../assets/pyramid/05-dikw-pyramid-data-info-knowledge.svg" alt="The DIKW pyramid with the 'data', 'information', and 'knowledge' layers labeled">

---

# The DIKW Pyramid {.image-frame-slide}

<img src="../assets/pyramid/06-dikw-pyramid-full.svg" alt="The full DIKW pyramid with all four layers labeled: data, information, knowledge, and wisdom">

---

# Sources {.sources}

1. GitHub source: <https://github.com/jackbandy/data-science-fun/blob/main/docs/slides/week1.md>.
2. Slides developed using materials from [Elena Zheleva](https://www.cs.uic.edu/~elena/) and [Gonzalo Bello Lander](https://cs.uic.edu/profiles/gonzalo-bello/), the Berkeley DS 100 team, Marine Carpuat, and Brian Ziebart.
3. Slide deck built with [Quarto](https://quarto.org/) revealjs.
4. Title font is Big Shoulders; Body font is [Libre Franklin](https://en.wikipedia.org/wiki/Franklin_Gothic#Libre_Franklin).
