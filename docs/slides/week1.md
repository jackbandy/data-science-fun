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
<img src="../assets/data-science-venn/data_science_venn_remix_v2.svg" alt="Venn diagram with three overlapping circles labeled Hacking Skills, Math and Statistics Knowledge, and Substantive Expertise. Their intersections are labeled Machine Learning, Traditional Research, and Danger Zone, with Data Science at the center." style="max-height:350px; width:auto; max-width:100%; display:block; margin:0 auto;">
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

# What is Data Science? {.image-frame-slide}

<img src="../assets/week1-intro-data-science/venn-rgb.svg" alt="Venn diagram: computer science, math and statistics, and domain knowledge overlapping at data science">

::: {style="text-align:center; font-size:0.5em; color:#565a5c; margin-top:0.3em;"}
Source: Drew Conway, [The Data Science Venn Diagram](http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram) (2010)
:::

---

# A Data Science Elephant? {.image-frame-slide}

<img src="../assets/art/itcho_blind_monks_examining_elephant_1888.jpg" alt="Blind monks examining an elephant, each touching a different part and describing it differently, a 1888 woodblock print reproduction of a work by Hanabusa Itchō">

::: {style="text-align:center; font-size:0.4em; color:#565a5c; margin-top:0.3em;"}
Hanabusa Itchō, *Blind Monks Examining an Elephant* (1888 woodblock print reproduction), public domain. [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Blind_monks_examining_an_elephant.jpg).
:::

---

# My Take: The Data Science Elephantidae

::::: {.columns}

:::: {.column width="44%"}
::: {.incremental}
- Data scientists often define the field by the part they touched
- **Elephantidae**: biological family that includes elephants, mammoths, mastodons
- Data science as a "family" of related methods, topics, questions
:::
::::

:::: {.column width="52%"}
<img src="../assets/phylogeny/elephantidae-cladogram.svg" alt="Cladogram of Elephantidae within Proboscidea, showing Loxodonta and Palaeoloxodon as sister genera, and Mammuthus and Elephas as sister genera" style="max-height:600px; width:auto; max-width:100%; display:block; margin:0 auto; border:1px solid rgba(0, 0, 0, 0.12); box-shadow:0 10px 28px rgba(0, 0, 0, 0.12);">

::: {style="text-align:center; font-size:0.4em; color:#565a5c; margin-top:0.3em;"}
Based on [Wikipedia, "Elephant"](https://en.wikipedia.org/wiki/Elephant#Taxonomy).
:::
::::

:::::

---

# My Take: The Data Science Elephantidae

::::: {.columns}

:::: {.column width="44%"}
::: {.incremental}
- The family runs deeper than any one member
- Data scientists do not have a monopoly on knowledge 
- We are in a much larger ecosystem!
:::
::::

:::: {.column width="52%"}
<img src="../assets/phylogeny/elephantidae-cladogram.svg" alt="Cladogram of Elephantidae within Proboscidea, showing Loxodonta and Palaeoloxodon as sister genera, and Mammuthus and Elephas as sister genera" style="max-height:600px; width:auto; max-width:100%; display:block; margin:0 auto; border:1px solid rgba(0, 0, 0, 0.12); box-shadow:0 10px 28px rgba(0, 0, 0, 0.12);">

::: {style="text-align:center; font-size:0.4em; color:#565a5c; margin-top:0.3em;"}
Based on [Wikipedia, "Elephant"](https://en.wikipedia.org/wiki/Elephant#Taxonomy).
:::
::::

:::::

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
**Data science can help turn the flood of data into information and knowledge**
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

Four things we'll cover:

::: {.incremental}
1. **Role of statistics in data science**
2. **Probability**
3. **Distributions**
4. **Sampling**
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

# Probability {.smaller}

- **Probability** is a measure of the **likelihood** of an event occurring.
- Probability is the language we use to quantify uncertainty in what the data tells us.

:::: {.columns}

::: {.column width="30%"}
<div style="border:1px solid #001E62; border-radius:8px; padding:6px 16px; text-align:center; width:fit-content; margin:0.2em auto;">
$$P(E) = \frac{|E|}{|S|}$$
</div>
:::

::: {.column width="66%"}
<div style="font-size:0.8em; line-height:1.3;">
<b style="color:#f9461c;">E</b> = the event<br>
<b style="color:#f9461c;">S</b> = sample space<br>
<b style="color:#f9461c;">|E|</b> = number of outcomes in event E<br>
<b style="color:#f9461c;">|S|</b> = total number of possible outcomes in S
</div>
:::

::::

- The probability of an event is always between <b>0 and 1</b>.

<div style=border-radius:8px; padding:8px 16px; margin-top:0.4em; font-size:0.72em; line-height:1.3;">
<i><b style="color:#f9461c;">Example:</b></i> A bag has 6 blue, 3 red, and 5 yellow marbles.<br>
What is the probability of drawing a blue or red marble on the first draw? 
<br>
<i><b>P(E) =</b></i>
</div>

---

# Terminology

::: {style="font-size:0.85em; line-height:1.5;"}
- **Experiment** — a process or action with an uncertain result
- **Outcome** — a single possible result of an experiment
- **Event** — a set of one or more outcomes we care about
- **Sample space** — the set of all possible outcomes
- **Complementary events** — two events where one occurs if and only if the other does not
:::
---

# Conditional Probability {.smaller}

- **Conditional probability** is the probability of an event **given that another event has already happened**.
- **P(A | B)** — "the probability of A given B."

:::: {.columns}

::: {.column width="30%"}
<div style="border:2px solid #f9461c; border-radius:8px; padding:2px 7px; text-align:center; width:fit-content; margin:0.3em auto;">
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$
</div>
:::

::: {.column width="62%"}
<div style="font-size:0.72em; line-height:2.5; margin-top:0.4em;">
<b style="color:#f9461c;">P(A | B)</b>   =   probability of A given B<br>
<b style="color:#f9461c;">P(A ∩ B)</b> = probability of both A and B<br>
<b style="color:#f9461c;">P(B)</b> = probability of B (must be &gt; 0)
</div>
:::

::::

---

# Conditional Probability {.smaller}

**Example:** A deck contains 15 distinct cards labeled 1 through 15. Two cards are drawn at random without replacement.

:::: {.columns}

::: {.column width="48%"}
[SET UP]{style="color:#f9461c; font-weight:bold; letter-spacing:2px; font-size:0.8em;"}

::: {.fragment}
**A** = both cards odd &nbsp;&nbsp; **B** = sum is even
:::

::: {.fragment}
*Sum is even if both cards are odd, or both are even.*
:::

::: {.fragment}
**Odd numbers (8)**<br>
<span style="display:inline-block; background:#FDE7E0; border:1px solid #f9461c; color:#f9461c; font-weight:bold; border-radius:5px; padding:3px 8px; margin:2px;">1</span><span style="display:inline-block; background:#FDE7E0; border:1px solid #f9461c; color:#f9461c; font-weight:bold; border-radius:5px; padding:3px 8px; margin:2px;">3</span><span style="display:inline-block; background:#FDE7E0; border:1px solid #f9461c; color:#f9461c; font-weight:bold; border-radius:5px; padding:3px 8px; margin:2px;">5</span><span style="display:inline-block; background:#FDE7E0; border:1px solid #f9461c; color:#f9461c; font-weight:bold; border-radius:5px; padding:3px 8px; margin:2px;">7</span><span style="display:inline-block; background:#FDE7E0; border:1px solid #f9461c; color:#f9461c; font-weight:bold; border-radius:5px; padding:3px 8px; margin:2px;">9</span><span style="display:inline-block; background:#FDE7E0; border:1px solid #f9461c; color:#f9461c; font-weight:bold; border-radius:5px; padding:3px 8px; margin:2px;">11</span><span style="display:inline-block; background:#FDE7E0; border:1px solid #f9461c; color:#f9461c; font-weight:bold; border-radius:5px; padding:3px 8px; margin:2px;">13</span><span style="display:inline-block; background:#FDE7E0; border:1px solid #f9461c; color:#f9461c; font-weight:bold; border-radius:5px; padding:3px 8px; margin:2px;">15</span>
:::

::: {.fragment}
**Even numbers (7)**<br>
<span style="display:inline-block; background:#DCE6F1; border:1px solid #001E62; color:#001E62; font-weight:bold; border-radius:5px; padding:3px 8px; margin:2px;">2</span><span style="display:inline-block; background:#DCE6F1; border:1px solid #001E62; color:#001E62; font-weight:bold; border-radius:5px; padding:3px 8px; margin:2px;">4</span><span style="display:inline-block; background:#DCE6F1; border:1px solid #001E62; color:#001E62; font-weight:bold; border-radius:5px; padding:3px 8px; margin:2px;">6</span><span style="display:inline-block; background:#DCE6F1; border:1px solid #001E62; color:#001E62; font-weight:bold; border-radius:5px; padding:3px 8px; margin:2px;">8</span><span style="display:inline-block; background:#DCE6F1; border:1px solid #001E62; color:#001E62; font-weight:bold; border-radius:5px; padding:3px 8px; margin:2px;">10</span><span style="display:inline-block; background:#DCE6F1; border:1px solid #001E62; color:#001E62; font-weight:bold; border-radius:5px; padding:3px 8px; margin:2px;">12</span><span style="display:inline-block; background:#DCE6F1; border:1px solid #001E62; color:#001E62; font-weight:bold; border-radius:5px; padding:3px 8px; margin:2px;">14</span>
:::
:::

::: {.column width="52%"}
[SOLUTION]{style="color:#f9461c; font-weight:bold; letter-spacing:2px; font-size:0.8em;"}

::: {.fragment}
$$n(B) = \binom{8}{2} + \binom{7}{2} = 28 + 21 = 49$$
:::

::: {.fragment}
$$n(A \cap B) = \binom{8}{2} = 28$$
:::

::: {.fragment}
$$P(A \mid B) = \frac{n(A \cap B)}{n(B)} = \frac{28}{49} = \frac{4}{7}$$
:::

::: {.fragment}
<div style="border-radius:8px; padding:8px 16px; text-align:center; margin-top:0.3em;">
<span style="color:#fff; font-size:0.7em; letter-spacing:2px; font-weight:bold;">ANSWER</span> &nbsp;&nbsp; <span style="font-weight:bold; font-size:1.1em;">P(A | B) = 4/7</span>
</div>
:::
:::

::::

---

# Bayes' Theorem

Conditional probabilities can be reversed using Bayes' theorem, which provides a systematic method for expressing one conditional probability in terms of another.

$$P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}$$

$$P(B) = P(B \mid A)\,P(A) + P(B \mid A')\,P(A')$$

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

# The Treachery of Images {.section-header}

---

# This is not a jersey {.image-frame-slide}

<img src="../assets/art/belgium_2026_away_jersey_collar_tag.jpg" alt="Collar of Belgium's 2026 World Cup away jersey, reading 'Ceci n'est pas un maillot' (This is not a jersey), designed by adidas with the Royal Belgian Football Association as a tribute to Magritte">

::: {style="text-align:center; font-size:0.5em; color:#565a5c; margin-top:0.3em;"}
Belgium's 2026 World Cup away jersey, "Ceci n'est pas un maillot." Photo via [Hyperallergic](https://hyperallergic.com/belgiums-magritte-inspired-soccer-jersey-mirrors-a-surreal-world-cup/).
:::

---

# This is not a pipe {.image-frame-slide}

<img src="../assets/art/magritte_treachery_of_images_1929.webp" alt="René Magritte's painting of a pipe with the caption 'Ceci n'est pas une pipe' (This is not a pipe)">

::: {style="text-align:center; font-size:0.5em; color:#565a5c; margin-top:0.3em;"}
René Magritte, *The Treachery of Images* (1929). [LACMA Collections](https://collections.lacma.org/object/31931).
:::

---

# This is not a triangle {.image-frame-slide}

<img src="../assets/triangles/00-triangle-best.svg" alt="An equilateral triangle on a golden-ratio canvas">

::: {style="text-align:center; font-size:0.5em; color:#565a5c; margin-top:0.3em;"}
An equilateral triangle — or is it? See [Chapter 1: Working Toward Wisdom](../ethics-in-data-science/01-working-toward-wisdom.html).
:::

---

# Sources {.sources}

1. GitHub source: <https://github.com/jackbandy/data-science-fun/blob/main/docs/slides/week1.md>.
2. Slides developed using materials from [Elena Zheleva](https://www.cs.uic.edu/~elena/), [Gonzalo Bello Lander](https://cs.uic.edu/profiles/gonzalo-bello/), the [Berkeley DS 100 team](https://ds100.org/), [Marine Carpuat](https://www.cs.umd.edu/~marine/), and [Brian Ziebart](https://cs.uic.edu/profiles/brian-ziebart).
3. [Elda Shatro](https://github.com/eldashatro4) contributed to these slides.
4. Slide deck built with [Quarto](https://quarto.org/) revealjs.
5. Title font is Big Shoulders; Body font is [Libre Franklin](https://en.wikipedia.org/wiki/Franklin_Gothic#Libre_Franklin).
6. *The Treachery of Images* (1929) by René Magritte, courtesy of [LACMA Collections](https://collections.lacma.org/object/31931); public domain in the United States.
7. Belgium 2026 World Cup away jersey by adidas and the Royal Belgian Football Association, photo via [Hyperallergic](https://hyperallergic.com/belgiums-magritte-inspired-soccer-jersey-mirrors-a-surreal-world-cup/); used under fair use for educational commentary.
