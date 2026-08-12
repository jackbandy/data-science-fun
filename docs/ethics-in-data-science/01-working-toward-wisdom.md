---
title: Working Toward Wisdom
subtitle: Introduction to Ethics in Data Science
---


**[← Back to Course Homepage](../../index.html)**


> "Those analysis droids you've got over there only focus on symbols. Hagh! I should think you Jedi would have more respect for the difference between knowledge and, hu-hu-hu... *wisdom*."

-- Dexter Jettster in *Attack of the Clones*, written by George Lucas and Jonathan Hales [@lucas_hales_aotc_2000, p. 35]


> "Where is the Life we have lost in living? Where is the wisdom we have lost in knowledge? Where is the knowledge we have lost in information?"

-- T. S. Eliot in *The Rock* [@eliot_rock_1934]


> "Wisdom cannot be passed on... Knowledge can be conveyed, but not wisdom. It can be found, it can be lived... but it cannot be expressed in words and taught."

-- Siddhartha in Hermann Hesse's *Siddhartha* [@hesse_siddhartha_1922]


> **Overview:** This chapter describes the DIKW pyramid — data, information, knowledge, wisdom — and its relevance to the data science lifecycle. The pyramid offers a way to consider the fundamental goals and purposes of data science work, i.e. to develop information, knowledge, and wisdom. The chapter also discusses concepts of *understanding* and *common knowledge*, and describes their relevance to data science. It closes with a brief discussion of statistical worldviews (e.g. Bayesian versus Frequentist), explaining why data scientists cannot simply "just do the math" - they often must choose particular beliefs about math and the world at large.

As one works through the various stages of the [data science lifecycle](https://learningds.org/ch/01/lifecycle_cycle.html), it is helpful to consider how each stage relates to what is often called the data-information-knowledge-wisdom "hierarchy," or the "DIKW pyramid" for short [@rowley_wisdom_2007]. The DIKW framing has a long history across systems thinking and information science (e.g., @ackoff_data_1989; @vance_information_1997; @bernstein_data-information-knowledge-wisdom_2011). As argued by this chapter and other sources, the definitive hierarchy implied by the DIKW pyramid is somewhat misleading [@fricke_knowledge_2009], however, the intuitions around the metaphor offer helpful framing for data science work.

::: {#fig-dikw-pyramid}
<img src="../../assets/pyramid/06-dikw-pyramid-full.svg" alt="The DIKW pyramid with four labeled layers: data, information, knowledge, and wisdom." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

A rendition of the DIKW pyramid, with data at the base supporting successive layers of information, knowledge, and wisdom.
:::

The basic premise of the DIKW pyramid is as follows. To build a pyramid, start with a brick: a datum. Use multiple bricks to create a large organized layer of bricks: data. Upon a solid foundation of data, we can begin to construct information, and upon a solid layer of information, we can construct knowledge.

Like all metaphors, the DIKW pyramid eventually breaks down. Knowledge creation is not always simply a matter of assembling data into information and then assembling that information into knowledge. And wisdom is not *literally* the top layer of a pyramid, nor is it the guaranteed product of assembling data, information, and knowledge.

Still, the DIKW model accurately suggests that one purpose of data (i.e. data science) is, generally, to point us toward wisdom. "Wisdom" may be a surprising word to see in a data science book, but it is helpful to consider it as an end goal, or *telos*, in data science work.

## What is wisdom?

To answer the question "what is wisdom," one would benefit from also being able to answer the question, "what is a triangle?"[^triangle-spinoza]

To start, let us try to display a perfect equilateral triangle on your screen, or at least get as close as we can.

::: {#fig-triangle-ideal}
<img src="../../assets/triangles/00-triangle-best.svg" alt="An equilateral triangle on a golden-ratio canvas." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

An attempt to display a perfect equilateral triangle.
:::

Figure @fig-triangle-ideal looks like a pretty good triangle! It uses scalable vector graphics (i.e. an svg file) to make the lines look as crisp as they possibly can on a computer screen. The image only uses a few pieces of information: the size of the frame, the location of the three points for an equilateral triangle within that frame, and the color and width of the line to connect those dots. This particular image uses a black line with a width of "six."

The entire image thus comes from just a few lines of code:

``` {.xml filename="00-triangle-best.svg"}
<svg
  xmlns="http://www.w3.org/2000/svg"
  width="1600"
  height="989"
  viewBox="0 0 1600 989"
>
  <rect width="100%" height="100%" fill="white" />
  <polygon
    points="364.84,871.36 800.00,117.64 1235.16,871.36"
    fill="none"
    stroke="black"
    stroke-width="6"
    stroke-linejoin="round"
  />
</svg>
```

Is there really a triangle in the image? Is there a *perfect* triangle in the image? Similar questions can be asked about various shapes, such as the existence of perfect circles [@payne_perfect_circles_2019], or perfect spheres [@muller_roundest_object_2013]. One way to find out if a shape is truly "perfect" is to zoom in on a small portion of it. We will zoom in by a power of ten, inspired by the Eames films [@eames_powers_of_ten_1968; @eames_powers_of_ten_1977].

::: {#fig-triangle-frame}
<img src="../../assets/triangles/01-triangle-frame.svg" alt="An equilateral triangle with a highlighted rectangular frame around its left edge." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

The red rectangular frame will be the outer frame for the next image.
:::

The red rectangle represents another golden-ratio rectangle, this one being 1/10th the size of the original rectangle (e.g. 160 pixels of the original 1600 pixels). This red frame will form the outer border of the next image.

::: {#fig-triangle-edge}
<img src="../../assets/triangles/02-triangle-edge.svg" alt="A cropped and enlarged view of the triangle's left edge." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

The left edge of the "perfect" equilateral triangle, which may not be perfect after all.
:::

Although the original picture may have looked like a perfect triangle at first, closer inspection shows the left edge of the triangle is not even a straight line. The edges are quite jagged, and indeed, that is the way to draw "lines" on a computer screen - with blocky, square pixels. We can look even closer to see how these pixels work, zooming in by another factor of ten.

::: {#fig-triangle-edge-frame}
<img src="../../assets/triangles/03-triangle-edge-frame.svg" alt="An enlarged edge view with a smaller frame marking the next crop." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

The red rectangular frame will be the outer frame for the next zoomed-in image.
:::

::: {#fig-triangle-edge-zoom}
<img src="../../assets/triangles/04-triangle-edge-zoom.svg" alt="An enlarged crop of the triangle's edge." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

The left edge of the "perfect" equilateral triangle breaks down even further.
:::

Now, the flaws of the triangle are even closer and more apparent. Zooming in, we have laid bare its imperfections (or at least some of its imperfections). Then again, those imperfections have been there all along: the square pixels (picture elements) in the original, perfect-looking triangle were always *there*, they were just too small to see.

Even now, this image of the black squares is not really showing you the pixels. Here is what those "black" pixels actually look like up close:

::: {#fig-lcd-pixel-macro}
<img src="../../assets/subpixels/lcd-pixel-macro-2023-golden.jpg" alt="Microscopic close-up of an LCD display showing red, green, and blue subpixels." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

A microscopic image of an LCD display showing subpixels. Source: Jacek Halicki, [*2023 Mikroskopowy obraz matrycy LCD*](https://commons.wikimedia.org/wiki/File:2023_Mikroskopowy_obraz_matrycy_LCD.jpg), licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
:::

And even this statement about "what pixels look like" is somewhat inaccurate - this is not *exactly* what pixels look like. There is no way to show a zoomed-in picture of *your* screen at this very moment, although you could go get a magnifying glass if you are curious. And if you looked through that magnifying glass, zooming in further, you might even see "subpixels" of red, blue, and green in your screen.

::: {#fig-lcd-pixel-macro-zoom}
<img src="../../assets/subpixels/lcd-pixel-macro-2023-golden-zoom-10x.jpg" alt="Ten-times zoomed view of the LCD subpixel pattern." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

A 10x zoom into the LCD subpixel image, showing rectangular subpixels. Source: Jacek Halicki, [*2023 Mikroskopowy obraz matrycy LCD*](https://commons.wikimedia.org/wiki/File:2023_Mikroskopowy_obraz_matrycy_LCD.jpg), licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
:::


Furthermore, at the subpixel level, the subpixels on your screen might not be the same shape as the subpixels on another screen. Subpixels look different when it shows up on a standard definition CRT television, a CRT computer monitor, or LCD laptop screens, as shown in figure @fig-pixel-geometries.

::: {#fig-pixel-geometries}
<img src="../../assets/subpixels/pixel-geometries.jpg" alt="Microscopic photos comparing pixel geometries from CRT and LCD displays." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Up-close pixel geometries from CRT and LCD displays. Source: Peter Halasz (Pengo), [*Pixel geometry 02 Pengo.jpg*](https://commons.wikimedia.org/wiki/File:Pixel_geometry_02_Pengo.jpg), licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
:::

We could go on for quite a while with this repeated zoom-in effect. The Eames films about "powers of ten" zoom in all the way until "a single proton fills our scene," describing it as "the edge of present understanding." We will formally end our triangle journey with one more zoom, filling the scene with a single red subpixel.

::: {#fig-lcd-subpixel-fill}
<img src="../../assets/subpixels/lcd-pixel-macro-2023-golden-subpixel.jpg" alt="Extreme close-up of a single red LCD subpixel filling the entire frame." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

A single red subpixel, zoomed in to fill the frame. Cropped from the same source image by Jacek Halicki, [*2023 Mikroskopowy obraz matrycy LCD*](https://commons.wikimedia.org/wiki/File:2023_Mikroskopowy_obraz_matrycy_LCD.jpg), licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
:::

Taken as a metaphor, the triangle journey contains several lessons about working toward wisdom in data science. We began by asking "what is a triangle?" - a seemingly simple quest for understanding, yet it took us all the way to a single red subpixel. It would take several degrees of clear description to explain how the red sub pixel in figure @fig-lcd-subpixel-fill is connected to the triangle in figure @fig-triangle-ideal.

Analogously to the "what is a triangle" journey, data scientists will often start with deceptively simple questions:

* How does screen time affect mental health?
* How much does stretching help reduce injuries?
* Do people sleep better with noise machines?
* Is the cafe serving more customers than it was last year?
* Was there a reduction in theft from adding security cameras?
* Did the flyers bring more people to the restaurant?

The curious humans asking these questions ultimately want more than a one-word or one-sentence answer. Even the yes-or-no questions beg for a story. The task of a data scientist, therefore, is not merely to extract or produce concrete answers to these types of questions.

This is the second point for which the triangle journey is relevant. The real value of a (competent) data scientist is to understand, in detail, how the "subpixels" of data can become "images" of information. That is, a data scientist will continually explore and explain the decision-making required to turn data into information and/or knowledge. A data scientist will be ready to describe the story that unfolds from those decisions, and, in some cases, provide a brief concrete answer.

Practically, this means data scientists benefit from a strong understanding of data acquisition processes, sampling processes, inference processes, and other decisions made in the lifecycle. In short, data scientists will pay attention to the *provenance* of data, information, and knowledge.

A strong grasp of provenance is an important component of "data science wisdom." When traced back to its origins, data are always limited. George Box's famous aphorism that "all models are wrong, but some are useful" [@box_draper_empirical_model_building_1987] might therefore be amended: all *data* are wrong, too. That is, all data are imperfect representations of the real world (or what we call the real world). Some data are very useful for understanding the world, but all data are limited snapshots. Chapter 4 calls this the "treachery of data" and discusses it in more detail.

The "triangle" journey has thus illustrated several dimensions of "data science wisdom." Wisdom involves being able to explain why the triangle in figure @fig-triangle-ideal was not *exactly* a perfect triangle. Wisdom requires *understanding the process* of going from subpixels to pixels to (an appearance of) lines to an imperfect representation of a triangle. This was a journey and a lesson in *provenance* - tracing the (appearance of) a triangle all the way to its origins in subpixels (and one could go even further).

Wisdom also involves a willingness to say why figure @fig-triangle-ideal was, in some sense, a triangle. One must occasionally bow to the consensus and accept "equilateral triangle" as the best available, most recognizable name for the shape that appears. As will be discussed in Chapter 5, this kind of wisdom requires an awareness of goals, audience knowledge, and other contextual factors which can improve communication.


## Understanding

Notably missing from the DIKW pyramid is the word "understanding." This points to another limitation of the metaphor: fixed, static data are not automatically converted to information and/or knowledge and/or wisdom. The existence of the DIKW pyramid thus implies human understanding. Some human(s) must have built the pyramid.

Here is another way to make the point, using the words of Ursula Le Guin: "What good are all the objects in the universe, if there is no subject?" [@leguin_mrs_brown_1979]. And to rephrase this sentiment in the context of the DIKW pyramid, "what good are all the data, if there is no data scientist?"

To construct the DIKW pyramid, there must be some human subject that transforms data into information and information into knowledge. If and when these transformations happen, they happen through the effort of human attention.

For example, what makes Wikipedia a source of knowledge is not merely the text on the page(s), but the coordination process of the many Wikipedia editor communities which iteratively write, review, and update Wikipedia pages. Furthermore, the information captured on Wikipedia pages can only "spread" and become knowledge when people read and trust that information. And a person trusts the information because of the subjects who crafted and re-crafted the language, ensuring its coherence and alignment with existing language.

This construction process is what we might call understanding. Information is more than compiled data, it is *understood* data. This means information is not a guaranteed property of data. And knowledge is not just stored information, it is *understood* information. @zeleny_management_1987 applies a similar principle, describing knowledge as a "network of relations through which humans coordinate their actions," adding that "knowledge brings (through language) coherence and coordination to the otherwise turbulent and chaotic world of human action."

This activity, exemplified by the continuous editing of Wikipedia editor communities, is the essence of understanding. The DIKW pyramid does not build itself: it is built by the human activity of devoting attention to gain understanding, which is often done in community.

Human relations can often complicate things. Different people and organizations do not all construct knowledge in the same way(s), and Chapter 5 revisits the pyramid metaphor along with some of the alternative metaphors for knowledge construction - e.g. cathedrals and bazars.

Furthermore, when it comes to understanding among multiple people, we broach the phenomenon of *common knowledge* — shared awareness not just of facts, but awareness of the facts other people know. This phenomenon has direct implications for how data scientists communicate results, and is also discussed in Chapter 5. Effective communication in building the DIKW pyramid also requires a distinction between "understanding the data" and "understanding the world" - discussed further in Chapter 4.


## Statistical worldviews {#sec-statistical-worldviews}

One final component of wisdom for the data scientist is an awareness of different worldviews and their relevance to various steps in the data science lifecycle. Although some may view data scientists as having a neutral, objective, "view from nowhere" [@nagel_view_from_nowhere_1986; @haraway_situated_knowledges_1988; @dignazio_klein_data_feminism_2020], there are many "researcher degrees of freedom" exercised throughout the lifecycle. Data scientists make decisions within these degrees of freedom, which entails a degree of subjectivity. This means data scientists bring situated humanity into their work: their prior experiences, tastes, distastes, habits of mind, and other aspects of their worldview.

To help demonstrate the relevance of worldviews in data science, we will conclude the chapter with the example of frequentist versus Bayesian statistics.

Consider a simple scenario from [@ipeirotis_bayesian_frequentist_2008]:

* You have a coin that, when flipped, ends up head with probability *p* (and ends up tail with probability *1−p*)
* The value of *p* is unknown, and you want to know it
* You flip the coin 14 times and get 10 heads
* A stranger walks by after the 14th flip and offers a bet: will  the next two flips yield two heads?
* You must choose whether to take the bet.

While the mathematical details are worked out in the original source, what matters here is that different mathematical conclusions are reached through different statistical worldviews.

In this particular example, a *frequentist* would estimate *p* from the 14 observations, estimating a 51% chance of two consecutive heads. A *Bayesian* reaches a different estimate, 48.5% (by treating *p* as a distribution, incorporating prior beliefs, and using Bayes' theorem to account for the 14 observations).

There are underlying beliefs supporting these numbers: frequentists treat probability as long-run frequency/percentages, and judge procedures by their error rates across repeated trials [@sep-statistics]. Bayesians, on the other hand, treat probability as a degree of belief (or "credence") that is updated as evidence arrives [@sep-epistemology-bayesian]. In this case, Bayesians start with the prior belief that coins are expected to land on tails 50% of the time and head 50% of the time.

So, do you take the bet? One might expect there to be a single answer to the statistical question: "just do the math!" But this example demonstrates multiple paradigms upon which we might base our math. This is a case where a data scientist must choose which math to use, and to some extent, what to believe about the world.

The value of data scientists is not that they "just do the math," but that they have well-informed views about which math to do and why.

The Bayesian/Frequentist statistical debate actually seems to have settled down. In a widely-cited 1986 paper, Bradley Efron asked "Why Isn't Everyone a Bayesian?" and implied the choice as an active contest [@efron_why_isnt_bayesian_1986]. More recently, however, Richard McElreath suggests that the Bayesian-versus-frequentist debate has essentially been subsumed by the question of causal inference [@mcelreath_statistical_rethinking_2020]. That is, the main question has become: what can we expect to happen from a given intervention?

Even if "everyone is a Bayesian," it would not settle the matter or eliminate the existence of subjective statistical worldviews. A particularly relevant dilemma is sometimes called the "problem of the priors" in Bayesian epistemology [@sep-epistemology-bayesian]. Bayesians may agree to treat probability as a degree of belief, but how exactly does one form a belief before data are available? Different camps of Bayesians (i.e. "subjective Bayesians" or "objective Bayesians") will have different answers to this question.

Bayesians also disagree on a number of other questions [@sep-epistemology-bayesian], for example, about whether a prior/credence must be a single number (or a range), whether a given body of evidence permits exactly one rational "credence" (or several), and how to update credences/beliefs. These are cases in which a (Bayesian) data scientist must make a choice (e.g. when choosing a prior), and cannot simply "do the math."

This is *not* to say the process is unscientific. There are well-justified norms, standards, and conventions throughout the data science lifecycle, including the lifecycle itself. But not every norm, standard, or convention is one that all data scientists agree upon. And whenever there is a lack of consensus, it is helpful to understand how people reach different viewpoints which prevent the consensus.

In other words, the rise of the causal inference paradigm described by @mcelreath_statistical_rethinking_2020 does not imply a conclusion to subjective decision-making in data science. Causal modeling may offer more regularity in asking questions (i.e., "what would happen after an intervention?") and helpful standards in structural modeling via causal graphs (specifically, directed acyclic graphs, or DAGs) [@sep-causal-models]. But causal modeling also opens up additional cans of worms and subjective decision-making, beginning with the question of what it actually means for one thing to "cause" another thing. Chapter 4 takes up that question in detail, working through the recurring structures — forks, colliders, pipes, and descendants — that make causal claims difficult to pin down.

## Conclusion

The purpose of this chapter is to introduce the DIKW pyramid, and describe the meaning of "working toward wisdom" as a data scientist. And yet, as the epigraph of this chapter suggests, "wisdom" cannot necessarily be passed to a reader. The same goes for knowledge: one must do their own work in order to truly learn, to gain real *understanding*.

This makes data science - the human process of assembling data into information and knowledge - a subjective process. The data science lifecycle is scientifically justified, yet it also has contingencies at every step: what data to collect, how to collect it, which statistical worldview to adopt, which analyses to apply, which findings to communicate, and so on. While wisdom cannot be directly transmitted, understanding these subjectivities and the resultant multiverse of data science is a crucial foundation for the work that follows.

## References

[^triangle-spinoza]: The triangle example was inspired by a memorable lecture I attended as an undergraduate student at Wheaton College. The speaker drew a triangle on a chalkboard and asked "what is that?" When the audience answered "it's a triangle," he responded: "that's not a triangle, let's talk about Spinoza." See [Spinoza's *Ethics*, Part 1](https://en.wikisource.org/wiki/Ethics_(Spinoza)/Part_1).
