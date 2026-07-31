---
title: "Week 1 (CS 418 @ UIC)"
format:
  revealjs:
    footer: '<img src="../assets/branding/uic-black-logo.svg" alt="UIC logo"> <img src="../assets/branding/cc-by-nc-sa-small.svg" alt="CC BY-NC-SA"> <span class="footer-text">CS 418, Intro to Data Science, Week 1</span><span class="footer-text"><a href="https://dodatascience.fun/slides/week1.html">dodatascience.fun/slides/week1</a></span>'
---

# Week 1, Day 1 {.course-title .photo-title data-state="photo-title" background-image="../assets/orange-line-stops-better/stop01-harold-washington-library-a.jpg" background-size="cover"}

## Intro; Data Science Lifecycle

Jack Bandy
2026

---


# {.photo-only data-state="photo-only" background-image="../assets/orange-line-stops-better/stop01-harold-washington-library-a.jpg" background-size="cover"}

---

# Demo Content Slide

Week 1.

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

---

# How Big Is a Terabyte?

::: {style="border:3px dashed #f9461c; border-radius:12px; padding:0.8em 1em; margin-top:0.4em;"}
[TODO]{style="background:#f9461c; color:#fff; font-weight:bold; letter-spacing:2px; font-size:0.55em; border-radius:4px; padding:2px 10px;"}

::: {style="font-size:0.8em; margin-top:0.5em;"}
- **TK**
:::
:::

<!-- TODO: add 1 TB visual before the 400M TB/day slide -->

---

# What is Data Science? {.image-frame-slide}

<img src="../assets/week1-intro-data-science/role-of-data-science.svg" alt="Hub-and-spoke diagram: data science at the center linked to healthcare, transportation, finance, climate science, public safety, and scientific research" class="r-stretch" style="border:none; box-shadow:none; background:transparent;">

---

# What is Data Science? (Yet Another Metaphor)

::::: {.columns}

:::: {.column width="44%"}
::: {.incremental}
- Many fields "share the same track" (i.e. methods, tools, etc.)
- Data science makes up much of that shared track
- Data science can also go in its own direction
:::
::::

:::: {.column width="56%"}
<img src="../assets/week1-intro-data-science/role-of-data-science-cta-remix-v2.svg" alt="A transit map of data science. Grey rail lines are labelled journalism, politics, sports, transportation, finance, general scientific research, education, public health, and climate science; the Orange Line, still in color, is labelled data science, runs up into the Loop, and ends in the southwest at &quot;your own project(s)&quot;." style="max-height:400px; width:auto; max-width:100%; display:block; margin:0 auto;">
::::

:::::

---


# So what Do Data Scientists Do?

::: {.incremental}
1. **Ask good questions** — turn a vague goal into something measurable
2. **Obtain & clean the data** — collect, merge, and fix messy real-world data
3. **Explore & visualize** — search and discover patterns, outliers, and surprises
4. **Model & predict** — build something that explains and/or forecasts
5. **Communicate** — turn results into stories, decisions
:::

---

# Example Questions

::: {.incremental}
- Do guests like the new cold brew recipe?
- Is the running plan helping people run faster?
- Do people sleep better with noise machines?
- Did the advertising campaign make a difference?
- 
- **No real, curious human wants just "yes" or "no."**
- Data scientists can *explain* answers in detail.
- (See mini-book, [Chapter 1: Working Toward Wisdom](../ethics-in-data-science/book/01-working-toward-wisdom.html)).
:::

---

# Data Science Lifecycle {.section-header}

---

# The Data Science Lifecycle {.image-frame-slide}

<img src="../assets/lifecycle-steps/ds-lifecycle-step0.svg" alt="Blank data science lifecycle scaffold: five unlabeled boxes connected by arrows in a cycle">

---

# The Data Science Lifecycle {.image-frame-slide}

<img src="../assets/lifecycle-steps/ds-lifecycle-step1.svg" alt="Data science lifecycle with the first stage highlighted and labeled 'ask a question'; the remaining boxes are still blank">

---

# The Data Science Lifecycle {.image-frame-slide}

<img src="../assets/lifecycle-steps/ds-lifecycle-step2.svg" alt="Data science lifecycle with the second stage highlighted and labeled 'obtain data'; 'ask a question' is labeled but no longer highlighted">

---

# The Data Science Lifecycle {.image-frame-slide}

<img src="../assets/lifecycle-steps/ds-lifecycle-step3.svg" alt="Data science lifecycle with the third stage highlighted and labeled 'understand the data'; the first two stages are labeled">

---

# The Data Science Lifecycle {.image-frame-slide}

<img src="../assets/lifecycle-steps/ds-lifecycle-step4.svg" alt="Data science lifecycle with the fourth stage highlighted and labeled 'understand the world'; the first three stages are labeled">

---

# The Data Science Lifecycle {.image-frame-slide}

<img src="../assets/lifecycle-steps/ds-lifecycle-step5.svg" alt="Data science lifecycle with the final stage highlighted and labeled 'reports, decisions, solutions'; all five stages are now labeled">

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

# Is the Pyramid Upside Down?

::::: {.columns}

:::: {.column width="52%"}
::: {.incremental}
- Tuomi (1999): "data emerges only after we have information, and that information emerges only after we already have knowledge"
- You need knowledge to decide what is even worth measuring
- Frické (2009): a data-first pyramid "encourages the mindless and meaningless collection of data in the hope that one day it will ascend to information"
:::
::::

:::: {.column width="44%"}
<img src="../assets/pyramid/upside-down-pyramid-bratislava.jpg" alt="The Slovak Radio Building in Bratislava, an inverted pyramid resting on its point" style="max-height:520px; width:auto; max-width:100%; display:block; margin:0 auto; border:1px solid rgba(0, 0, 0, 0.12); box-shadow:0 10px 28px rgba(0, 0, 0, 0.12);">

::: {style="text-align:center; font-size:0.4em; color:#565a5c; margin-top:0.3em;"}
Slovak Radio Building, Bratislava. Thomas Ledl, [*Upside down Pyramid, Bratislava 02*](https://commons.wikimedia.org/wiki/File:Upside_down_Pyramid,_Bratislava_02.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
:::
::::

:::::

---

# Is the Pyramid Upside Down?

::::: {.columns}

:::: {.column width="52%"}
::: {.incremental}
- Does wisdom sit at the top of the pyramid?
- Or does wisdom hold up the whole thing?
- Or is this metaphor missing something else?
:::
::::

:::: {.column width="44%"}
<img src="../assets/pyramid/upside-down-pyramid-bratislava.jpg" alt="The Slovak Radio Building in Bratislava, an inverted pyramid resting on its point" style="max-height:520px; width:auto; max-width:100%; display:block; margin:0 auto; border:1px solid rgba(0, 0, 0, 0.12); box-shadow:0 10px 28px rgba(0, 0, 0, 0.12);">

::: {style="text-align:center; font-size:0.4em; color:#565a5c; margin-top:0.3em;"}
Slovak Radio Building, Bratislava. Thomas Ledl, [*Upside down Pyramid, Bratislava 02*](https://commons.wikimedia.org/wiki/File:Upside_down_Pyramid,_Bratislava_02.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
:::
::::

:::::

---

# What else is Missing?

::::: {.columns}

:::: {.column width="52%"}
::: {.incremental}
- **Understanding** — no layer of the pyramid 
- The pyramid does not build itself
- "What good are all the objects in the universe, if there is no subject?" — Ursula K. Le Guin
- Knowledge as a "network of relations through which humans coordinate their actions" (Zeleny, 1987)
:::
::::

:::: {.column width="44%"}
<img src="../assets/pyramid/06-dikw-pyramid-full.svg" alt="The full DIKW pyramid with all four layers labeled: data, information, knowledge, and wisdom" style="max-height:520px; width:auto; max-width:100%; display:block; margin:0 auto;">
::::

:::::

::: {style="text-align:center; font-size:0.5em; color:#565a5c; margin-top:0.3em;"}
See [Chapter 1: Working Toward Wisdom](../ethics-in-data-science/book/01-working-toward-wisdom.html).
:::

---

# Ursula K. Le Guin {.quote-slide}

> What good are all the objects in the universe, if there is no subject?

::: {.attribution}
Ursula K. Le Guin
:::

::: {.quote-source}
"Science Fiction and Mrs. Brown" (1975), in *[The Language of the Night](https://openlibrary.org/books/OL4100441M/The_language_of_the_night)* (1979).
:::

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
An equilateral triangle — or is it? See [Chapter 1: Working Toward Wisdom](../ethics-in-data-science/book/01-working-toward-wisdom.html).
:::

---

# Let's Zoom In (Powers of Ten) {.image-frame-slide}

<img src="../assets/triangles/01-triangle-frame.svg" alt="An equilateral triangle with a red rectangular frame around its left edge, marking the next crop">

::: {style="text-align:center; font-size:0.5em; color:#565a5c; margin-top:0.3em;"}
The red frame is 1/10th the size of the original canvas (160px vs. 1600px).
:::

---

# 10× {.image-frame-slide}

<img src="../assets/triangles/02-triangle-edge.svg" alt="A cropped and enlarged view of the triangle's left edge, showing a jagged rather than straight line">

::: {style="text-align:center; font-size:0.5em; color:#565a5c; margin-top:0.3em;"}
The "straight" edge is jagged — the only way to draw a line with square pixels.
:::

---

# 10× {.image-frame-slide}

<img src="../assets/triangles/03-triangle-edge-frame.svg" alt="An enlarged view of the triangle's edge with a smaller red frame marking the next crop">

::: {style="text-align:center; font-size:0.5em; color:#565a5c; margin-top:0.3em;"}
Again, the red frame marks where we zoom next.
:::

---

# 100× {.image-frame-slide}

<img src="../assets/triangles/04-triangle-edge-zoom.svg" alt="A further enlarged crop of the triangle's edge, resolving into individual square blocks">

::: {style="text-align:center; font-size:0.5em; color:#565a5c; margin-top:0.3em;"}
The pixels were there the whole time — they were just too small to see.
:::

---

# ...these aren't pixels {.image-frame-slide}

<img src="../assets/subpixels/lcd-pixel-macro-2023-golden.jpg" alt="Microscopic close-up of an LCD display showing red, green, and blue subpixels">

::: {style="text-align:center; font-size:0.4em; color:#565a5c; margin-top:0.3em;"}
Jacek Halicki, [*2023 Mikroskopowy obraz matrycy LCD*](https://commons.wikimedia.org/wiki/File:2023_Mikroskopowy_obraz_matrycy_LCD.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
:::

---

# Subpixels {.image-frame-slide}

<img src="../assets/subpixels/lcd-pixel-macro-2023-golden-zoom-10x.jpg" alt="Ten-times zoomed view of the LCD subpixel pattern, showing rectangular red, green, and blue subpixels">

::: {style="text-align:center; font-size:0.4em; color:#565a5c; margin-top:0.3em;"}
Jacek Halicki, [*2023 Mikroskopowy obraz matrycy LCD*](https://commons.wikimedia.org/wiki/File:2023_Mikroskopowy_obraz_matrycy_LCD.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
:::

---

# Different Screens {.image-frame-slide}

<img src="../assets/subpixels/pixel-geometries.jpg" alt="Microscopic photos comparing pixel geometries from CRT television, CRT monitor, and LCD displays">

::: {style="text-align:center; font-size:0.4em; color:#565a5c; margin-top:0.3em;"}
Peter Halasz (Pengo), [*Pixel geometry 02*](https://commons.wikimedia.org/wiki/File:Pixel_geometry_02_Pengo.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
:::

---

# Provenance {.image-frame-slide}

::: {style="font-size:0.72em; line-height:1.45; margin-bottom:0.5em;"}
- **Wisdom** = being able to explain *why* the figure was not a perfect triangle
- and being willing to say why it *is*, in some sense, a triangle
- understand how "subpixels of data" become "images of information"
- "All models are wrong" (Box)
	- All **data** are wrong too!
	- Or at least incomplete
:::

<img src="../assets/pyramid/06-dikw-pyramid-full.svg" alt="The full DIKW pyramid with all four layers labeled: data, information, knowledge, and wisdom" style="max-height:300px;">

::: {style="text-align:center; font-size:0.5em; color:#565a5c; margin-top:0.3em;"}
See [Chapter 1: Working Toward Wisdom](../ethics-in-data-science/book/01-working-toward-wisdom.html).
:::

---

# Week 1, Day 2 {.course-title .photo-title data-state="photo-title" background-image="../assets/orange-line-stops-better/stop01-harold-washington-library-a.jpg" background-size="cover"}

## Statistics Review

Jack Bandy
2026

---

# Statistics Review {.section-header}

---

# Roadmap

Four things we'll cover:

::: {.incremental}
1. **Role of statistics in data science**
2. **Probability**
3. **Distributions**
4. **Sampling**
:::

---

# Statistics in Data Science

::: {.incremental}
- Statistics: the science of learning from data under uncertainty.
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

# Key Terminology

::: {style="font-size:0.85em; line-height:1.5;"}
- **Experiment** — a process or action with an uncertain result
- **Outcome** — a single possible result of an experiment
- **Event** — a set of one or more outcomes we care about
- **Sample space** — the set of all possible outcomes
- **Complementary events** — two events where one occurs if and only if the other does not
	- E.g. coin flip
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

# Coin Flip Odds

::::: {.columns}

:::: {.column width="56%"}
::: {.incremental}
- **14 flips, 10 heads.**
- Will the next two both be heads?
- [FREQUENTIST]{style="color:#001E62; font-weight:bold; letter-spacing:2px;"} — **51%**
- [BAYESIAN]{style="color:#f9461c; font-weight:bold; letter-spacing:2px;"} — **48.5%**
- **Same data, opposite sides of the bet?!**
:::
::::

:::: {.column width="40%"}
<img src="../assets/slides-misc/coin-toss.jpg" alt="A coin in mid-air above a thumb that has just flipped it" style="max-height:480px; width:auto; max-width:100%; display:block; margin:0 auto; border:1px solid rgba(0, 0, 0, 0.12); box-shadow:0 10px 28px rgba(0, 0, 0, 0.12);">

::: {style="text-align:center; font-size:0.4em; color:#565a5c; margin-top:0.3em;"}
ICMA Photos, [*Coin Toss*](https://commons.wikimedia.org/wiki/File:Coin_Toss_(3635981474).jpg), [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/).
:::
::::

:::::

::: {style="text-align:center; font-size:0.5em; color:#565a5c; margin-top:0.3em;"}
Example from Panos Ipeirotis, ["Are You a Bayesian or a Frequentist?"](https://www.behind-the-enemy-lines.com/2008/01/are-you-bayesian-or-frequentist-or.html) (2008). See [Chapter 1: Working Toward Wisdom](../ethics-in-data-science/book/01-working-toward-wisdom.html).
:::

---

# "Just Do the Math"

::: {.incremental}
- **Frequentist**: probability = long-run frequency; judge procedures by error rates
- **Bayesian**: probability = degree of belief, updated as evidence arrives
- Efron (1986) asked "Why Isn't Everyone a Bayesian?" — an active contest at the time
- McElreath (2020): the debate has largely been **subsumed by causal inference**
- Even so: you still have to pick a prior. There is not always a "correct option"
:::

::: {style="text-align:center; font-size:0.5em; color:#565a5c; margin-top:0.3em;"}
See [Chapter 1: Working Toward Wisdom](../ethics-in-data-science/book/01-working-toward-wisdom.html).
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
8. LCD subpixel micrographs by Jacek Halicki, [*2023 Mikroskopowy obraz matrycy LCD*](https://commons.wikimedia.org/wiki/File:2023_Mikroskopowy_obraz_matrycy_LCD.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
9. Pixel geometry comparison by Peter Halasz (Pengo), [*Pixel geometry 02*](https://commons.wikimedia.org/wiki/File:Pixel_geometry_02_Pengo.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
10. The zoom sequence, DIKW discussion, and frequentist/Bayesian coin bet draw on [Chapter 1: Working Toward Wisdom](../ethics-in-data-science/book/01-working-toward-wisdom.html); the coin-bet example is from [Panos Ipeirotis (2008)](https://www.behind-the-enemy-lines.com/2008/01/are-you-bayesian-or-frequentist-or.html).
11. "Powers of ten" zoom framing after Charles and Ray Eames, *Powers of Ten* (1968/1977).
12. Ilkka Tuomi, ["Data Is More than Knowledge: Implications of the Reversed Knowledge Hierarchy for Knowledge Management and Organizational Memory"](https://doi.org/10.1080/07421222.1999.11518258), *Journal of Management Information Systems* 16(3), 1999, pp. 103–117.
13. Martin Frické, ["The Knowledge Pyramid: A Critique of the DIKW Hierarchy"](https://doi.org/10.1177/0165551508094050), *Journal of Information Science* 35(2), 2009, pp. 131–142.
14. Slovak Radio Building photo by Thomas Ledl, [*Upside down Pyramid, Bratislava 02*](https://commons.wikimedia.org/wiki/File:Upside_down_Pyramid,_Bratislava_02.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
15. Bradley Efron, ["Why Isn't Everyone a Bayesian?"](https://doi.org/10.1080/00031305.1986.10475342), *The American Statistician* 40(1), 1986, pp. 1–5.
16. Richard McElreath, *[Statistical Rethinking: A Bayesian Course with Examples in R and Stan](https://xcelab.net/rm/statistical-rethinking/)*, 2nd ed., Chapman and Hall/CRC, 2020.
17. Coin toss photo by ICMA Photos, [*Coin Toss*](https://commons.wikimedia.org/wiki/File:Coin_Toss_(3635981474).jpg), [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/).
