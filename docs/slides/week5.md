---
title: "Week 5 (CS 418 @ UIC)"
format:
  revealjs:
    footer: '<img src="../assets/branding/uic-black-logo.svg" alt="UIC logo"> <img src="../assets/branding/cc-by-nc-sa-small.svg" alt="CC BY-NC-SA"> <span class="footer-text">CS 418, Intro to Data Science, Week 5</span><span class="footer-text"><a href="https://dodatascience.fun/slides/week5.html">dodatascience.fun/slides/week5</a></span>'
---

# Week 5 Slide Deck {.course-title}

## Visualizations

Jack Bandy
2026

---

# Topic Title Placeholder {.course-title .photo-title data-state="photo-title" background-image="../assets/orange-line-stops-better/stop05-clark-lake-a.jpg" background-size="cover"}

CS 418 · Week 5 · 🟠 Clark/Lake 🟠

---

# {.photo-only data-state="photo-only" background-image="../assets/orange-line-stops-better/stop05-clark-lake-a.jpg" background-size="cover"}

---

# Demo Content Slide

Placeholder content for Week 5.

- Visualization goals
- Encodings
- Chart selection

---

# Pie & Donut Charts {.section-header}

---

# Pie Charts: The Intuition

- A pie chart encodes **proportion** as **angle** (and area)
- Humans are decent at judging "roughly half" or "roughly a quarter"
- We're much worse at comparing two slices that aren't adjacent

---

# Pie vs. Bar: Three Comparisons {.image-frame-slide}

::: {.content-visible when-format="html"}
![](../assets/pi-donut-demos/Piecharts.svg)
:::

::: {.content-visible when-format="pdf"}
![](../assets/pi-donut-demos/Piecharts.svg)
:::

---

# Pie vs. Bar: Case A {.image-frame-slide}

::: {.content-visible when-format="html"}
![](../assets/pi-donut-demos/piecharts-remix01.svg)
:::

::: {.content-visible when-format="pdf"}
![](../assets/pi-donut-demos/piecharts-remix01.svg)
:::

---

# Pie vs. Bar: Cases B & C {.image-frame-slide}

::: {.content-visible when-format="html"}
![](../assets/pi-donut-demos/piecharts-remix02.svg)
:::

::: {.content-visible when-format="pdf"}
![](../assets/pi-donut-demos/piecharts-remix02.svg)
:::

---

# The Donut Chart

- A **donut chart** is a pie chart with the center cut out
- The hole doesn't change the encoding — it's still angle/area
- Common argument for donuts: center space can carry a label or summary stat
- Common argument against: harder to judge angles without the center reference point

---

# Donut in the Wild: FIFA World Cup 2026 {.image-frame-slide}

::: {.content-visible when-format="html"}
![](../assets/pi-donut-demos/fifa-possession-example.jpeg)
:::

::: {.content-visible when-format="pdf"}
![](../assets/pi-donut-demos/fifa-possession-example.jpeg)
:::

---

# Recreating the FIFA Chart: Setup

```python
import matplotlib.pyplot as plt

sizes  = [63, 27, 10]
labels = ['COL', 'COD', 'In Contest']
colors = ['#f5c800', '#0057a8', '#00a896']

fig, ax = plt.subplots(figsize=(4, 4))
```

---

# Recreating the FIFA Chart: Draw

```python
ax.pie(sizes, labels=labels, autopct='%1.0f%%',
       colors=colors, startangle=90, counterclock=False,
       wedgeprops=dict(width=0.5), pctdistance=0.75)
ax.set_title('Possession', fontweight='bold')
plt.tight_layout()
plt.show()
```

---

# Sources {.sources}

1. GitHub source: <https://github.com/jackbandy/data-science-fun/blob/main/docs/slides/week5.md>.
2. Slides developed using materials from [Elena Zheleva](https://www.cs.uic.edu/~elena/) and [Gonzalo Bello Lander](https://cs.uic.edu/profiles/gonzalo-bello/), the Berkeley DS 100 team, Marine Carpuat, and Brian Ziebart.
3. Slide deck built with [Quarto](https://quarto.org/) revealjs.
4. Title font is Big Shoulders; Body font is [Libre Franklin](https://en.wikipedia.org/wiki/Franklin_Gothic#Libre_Franklin).
