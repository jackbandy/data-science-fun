---
title: "Week 8 (CS 418 @ UIC)"
format:
  revealjs:
    footer: '<img src="../assets/branding/uic-black-logo.svg" alt="UIC logo"> <img src="../assets/branding/cc-by-nc-sa-small.svg" alt="CC BY-NC-SA"> <span class="footer-text">CS 418, Intro to Data Science, Week 8</span><span class="footer-text"><a href="https://dodatascience.fun/slides/week8.html">dodatascience.fun/slides/week8</a></span>'
---

# Week 8 Slide Deck {.course-title}

## Linear Regression; Intro to Classification

Jack Bandy
2026

---

# Topic Title Placeholder {.course-title .photo-title data-state="photo-title" background-image="../assets/orange-line-stops-better/stop09-roosevelt-c.jpg" background-size="cover"}

CS 418 · Week 8 · 🟠 Roosevelt 🟠

---

# {.photo-only data-state="photo-only" background-image="../assets/orange-line-stops-better/stop09-roosevelt-c.jpg" background-size="cover"}

---

# Demo Content Slide

Placeholder content for Week 8.

- Linear regression
- Prediction
- Intro to classification

---

# Linear Regression {.smaller}
Linear regression models a linear relationship between two variables.

:::: {.columns}

::: {.column width="55%"}

- The variable being modeled or predicted is called the response variable.
- The variable used to predict the response is called the predictor variable.
- One predictor gives a line; several predictors give a plane.

:::

::: {.column width="45%"}

![](images/linearRegression.png
)


:::

::::

---

# Linear regression equation {.smaller}
A fitted model uses this regression line equation:

$$\hat{y} = b_0 + b_1 x$$

where

- $\hat{y}$ — the response variable, which we are trying to predict based on $x$
- $x$ — the predictor variable
- $b_0$ — the intercept, the predicted value of $y$ when $x$ is zero
- $b_1$ — the slope, how much the predicted value of $y$ changes for every one-unit increase in the value of $x$

---

# Sources {.sources}

1. GitHub source: <https://github.com/jackbandy/data-science-fun/blob/main/docs/slides/week8.md>.
2. Slides developed using materials from [Elena Zheleva](https://www.cs.uic.edu/~elena/) and [Gonzalo Bello Lander](https://cs.uic.edu/profiles/gonzalo-bello/), the Berkeley DS 100 team, Marine Carpuat, and Brian Ziebart.
3. Slide deck built with [Quarto](https://quarto.org/) revealjs.
4. Title font is Big Shoulders; Body font is [Libre Franklin](https://en.wikipedia.org/wiki/Franklin_Gothic#Libre_Franklin).
