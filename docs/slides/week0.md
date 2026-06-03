---
format:
  revealjs:
    theme: theme/uic-orange-reveal.scss
    width: 1280
    height: 720
    margin: 0
    slide-number: c
    controls: true
    progress: true
    include-in-header:
      text: |
        <style>
        .reveal .footer p {
          gap: 40px;
        }
        .reveal .footer .footer-text {
          font-size: 0.94em;
          font-weight: 400;
        }
        .reveal .footer .footer-text a {
          font: inherit !important;
          color: inherit !important;
        }
        </style>
    include-after-body:
      text: |
        <script>
        (() => {
          let installed = false;
          let observer = null;

          function updateSlideNumber() {
            if (!window.Reveal) return;
            const slideNumber = document.querySelector(".reveal .slide-number");
            if (!slideNumber) return;
            const current = Reveal.getSlidePastCount() + 1;
            const total = Reveal.getTotalSlides();
            const expectedText = `${current} of ${total}`;
            if (
              slideNumber.textContent.trim() === expectedText &&
              slideNumber.querySelector(".slide-number-current")
            ) {
              return;
            }
            slideNumber.innerHTML = `<span class="slide-number-current">${current}</span> <span class="slide-number-of">of</span> <span class="slide-number-total">${total}</span>`;
          }

          function scheduleSlideNumberUpdate() {
            window.requestAnimationFrame(updateSlideNumber);
            window.setTimeout(updateSlideNumber, 0);
            window.setTimeout(updateSlideNumber, 80);
          }

          function observeSlideNumber() {
            const slideNumber = document.querySelector(".reveal .slide-number");
            if (!slideNumber || observer) return;
            observer = new MutationObserver(scheduleSlideNumberUpdate);
            observer.observe(slideNumber, { childList: true, subtree: true, characterData: true });
          }

          function installSlideNumberFormatter() {
            if (!window.Reveal) {
              window.setTimeout(installSlideNumberFormatter, 50);
              return;
            }
            observeSlideNumber();
            if (!installed) {
              installed = true;
              Reveal.on("ready", scheduleSlideNumberUpdate);
              Reveal.on("slidechanged", scheduleSlideNumberUpdate);
              Reveal.on("fragmentshown", scheduleSlideNumberUpdate);
              Reveal.on("fragmenthidden", scheduleSlideNumberUpdate);
              window.addEventListener("hashchange", scheduleSlideNumberUpdate);
            }
            scheduleSlideNumberUpdate();
          }

          document.addEventListener("DOMContentLoaded", installSlideNumberFormatter);
          window.addEventListener("load", installSlideNumberFormatter);
        })();
        </script>
    footer: '<img src="../images/uic-black-logo.svg" alt="UIC logo"> <img src="../images/cc-by-nc-sa-small.svg" alt="CC BY-NC-SA"> <span class="footer-text">CS 418, Intro to Data Science, Week 0</span><span class="footer-text"><a href="https://dodatascience.fun/slides/week0.html">dodatascience.fun/slides/week0</a></span>'
slide-level: 1
---

# Week 0 Slide Deck {.course-title}

## An Experiment With Quarto

Jack Bandy
2026

This is a demo slide deck for reference and experimentation.

---

# Content Slide

Testing content slide.

- Lorem ipsum dolor sit amet
- Consectetur adipiscing elit
- Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua
- Test quote

> "The greatest value of a picture is when it forces us to notice what we never expected to see." — John Tukey

---

# Incremental Bullets

::: {.incremental}
* display this first
* display this second
* display this third
* display this fourth
* display this fifth
:::

---

# Tabsets

::: {.panel-tabset}

### Tab A

Content for `Tab A`

### Tab B

Content for `Tab B`

:::

---

# Pretty Code {auto-animate="true"}

- Syntax highlighting works in revealjs slides
- Code uses the theme's Courier stack

```python
import polars as pl


def summarize_ridership(stations: pl.DataFrame) -> pl.DataFrame:
    return (
        stations
        .group_by("line")
        .len(name="station_count")
        .sort("station_count", descending=True)
    )
```

---

# Line Highlighting

```{.python code-line-numbers="3-4|6|7-10|12"}
import numpy as np
import polars as pl

stations = pl.read_csv("cta_stations.csv")
orange = stations.filter(pl.col("line") == "Orange")

by_access = orange.group_by("accessible").len(name="station_count")
share = np.round(
    by_access["station_count"] / by_access["station_count"].sum(),
    2,
)

print(by_access.with_columns(accessible_share=share))
```

---

# Column Layout {.smaller}

::: columns
::: {.column width="42%"}
### Course Pattern

- Ask a data question
- Find the relevant table
- Check the units
- Make a readable view
:::

::: {.column width="58%"}
| Week | Focus |
|---:|---|
| 0 | Setup and orientation |
| 1 | Blah blah |
| 2 | Blah blah blah |
| 3 | Blah blah blah blah |
:::
:::


---

# Auto-Animate {auto-animate="true" auto-animate-easing="ease-in-out"}

::: r-hstack
::: {data-id="box1" style="background: #f9461c; width: 260px; height: 56px; margin: 10px;"}
:::
::: {data-id="box2" style="background: #565a5c; width: 180px; height: 56px; margin: 10px;"}
:::
:::

---

# Auto-Animate {auto-animate="true" auto-animate-easing="ease-in-out"}

::: r-stack
::: {data-id="box1" style="background: #f9461c; width: 360px; height: 360px; border-radius: 220px;"}
:::
::: {data-id="box2" style="background: #565a5c; width: 190px; height: 190px; border-radius: 120px;"}
:::
:::

---

# Florence Nightingale's Mortality Diagram (1858) {.image-slide}

<img src="../images/Nightingale-mortality.jpg" alt="Florence Nightingale, &quot;Diagram of the causes of mortality in the army in the East&quot; (1858) — a polar area chart showing deaths from preventable disease (blue), wounds (red), and other causes (black)">

---

# {.image-only footer=false}

<img src="../images/Nightingale-mortality.jpg" alt="Florence Nightingale, &quot;Diagram of the causes of mortality in the army in the East&quot; (1858) — a polar area chart showing deaths from preventable disease (blue), wounds (red), and other causes (black)">

---

# {.split}

::: {.split-content}

::: {}
- Lorem ipsum dolor sit amet, consectetur adipiscing elit
- Sed do eiusmod tempor incididunt ut labore et dolore magna
- Ut enim ad minim veniam, quis nostrud exercitation
- Duis aute irure dolor in reprehenderit in voluptate
- Excepteur sint occaecat cupidatat non proident
:::

<img src="../images/Nightingale-mortality.jpg" alt="Florence Nightingale, &quot;Diagram of the causes of mortality in the army in the East&quot; (1858)">

:::

---

# Sources {.sources}

1. Nightingale, Florence. "Diagram of the causes of mortality in the army in the East." *Notes on Matters Affecting the Health, Efficiency, and Hospital Administration of the British Army*, 1858. Image via Wikimedia Commons: <https://commons.wikimedia.org/wiki/File:Nightingale-mortality.jpg>. Public domain.
2. Slide deck built with [Quarto](https://quarto.org/) revealjs.
