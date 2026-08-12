# Ethics in Understanding

**[← Back to Course Homepage](../../index.html)**

::: {#fig-ds-lifecycle-v0}
<img src="../../assets/lifecycle/ds-lifecycle-v0.svg" alt="The full data science lifecycle diagram." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

The data science lifecycle. Although each stage of the lifecycle requires some degree of human understanding, this chapter focuses on the two stages that explicitly include "understanding."
:::

> "When we try to pick out anything by itself, we find it hitched to everything else in the Universe."

-- John Muir, as quoted by the Sierra Club John Muir Exhibit [@wood_john_muir_misquoted]

> "Essentially, all models are wrong, but some are useful."

-- George E. P. Box and Norman R. Draper [@box_draper_empirical_model_building_1987]

> "A map is not the territory it represents, but, if correct, it has a similar structure to the territory, which accounts for its usefulness."

-- Alfred Korzybski [@korzybski_non_aristotelian_1931]

🔴 *Chapter Status: in development. Opening sections are drafted, others outlined / incomplete.*

## Your Model is Always Wrong

The two previous chapters discussed limits in asking questions and obtaining data, which tend to be the starting points for data science lifecycles. Once equipped with question(s) and data, however limited both may be, the next step is to pursue understanding.

In the ideal lifecycle, data scientists will be able to understand the data in ways that also help them understand the world. But for reasons that will be explored in this chapter, this is much easier said than done -- "the data" and "the model" and "the world" are often disconnected in surprising ways.

The first reason is the one named in this chapter's epigraph. George Box's 1976 paper "Science and Statistics" put it bluntly: "since all models are wrong the scientist cannot obtain a 'correct' one by excessive elaboration" [@box_science_and_statistics_1976]. The aphorism most people quote comes from a later textbook with Norman Draper: "Essentially, all models are wrong, but some are useful" [@box_draper_empirical_model_building_1987].

[Chapter 1](01-working-toward-wisdom.md) noted that the same holds one level down, before any modeling is done: all *data* are wrong. Data are representations of the real world (or what we call the real world), and a representation is never the thing it represents. Again, we might call this the **treachery of data**, after René Magritte's painting of a pipe over the caption *Ceci n'est pas une pipe* — "This is not a pipe."

::: {#fig-treachery-of-images}
<img src="../../assets/art/magritte_treachery_of_images_1929.webp" alt="René Magritte's painting of a pipe with the caption 'Ceci n'est pas une pipe' (This is not a pipe)." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

René Magritte, *The Treachery of Images* (1929). The (image of a) painting of a pipe is not itself a pipe, and data are representations of the world, not the world itself. Source: [LACMA Collections](https://collections.lacma.org/object/31931), public domain in the United States.
:::

This chapter describes how and why data scientists can explore "*which* aspects of the world did some dataset/model capture, which were left out, and how the difference can matter for the questions at hand. The next section explores this through three lessons drawn from a classic puzzle in machine learning: the model is not the world, several models can look equally correct, and a pattern found in data is not a law governing the world.

## Three Lessons from Michalski's Trains

### The Model is not the World

An early version of this idea appears in Alfred Korzybski's 1931 paper, which included the quote from this chapter's epigraph: "A map is not the territory it represents, but, if correct, it has a similar structure to the territory, which accounts for its usefulness" [@korzybski_non_aristotelian_1931].

Chapter 1 described the not-a-triangle, or the attempt to represent a perfect triangle. Perfect triangles and perfect circles only exist as ideals - there is no way to create their true geometry in the world.

Even 3D geometries cannot be rendered perfectly. Achim Leistner's silicon sphere, considered the "[world's roundest object](https://en.wikipedia.org/wiki/Achim_Leistner)" has a verifiable out-of-roundness value - a difference between the measurements of an ideal sphere and the really-existing measured object. It is more like a perfect sphere than any other known object, but it is not a sphere.

Whereas chapter 1 offered a distinction between an ideal and a representation, here, we consider the distinction between a representation and a reality.

The data science lifecycle proposed by *Learning Data Science* wisely splits "understanding" into "understanding the data" and "understanding the world." Following Korzybski's observation, the data and/or models are useful to the extent that they accurately represent reality -- the same way that a map is useful to the extent that it accurately represents territory.


### Multiple Correct Models

::: {#fig-michalski-trains-1980}
<img src="../../assets/michalski-trains/figure4-michalski-ieee-1980.png" alt="Michalski's original trains going East and West, from the 1980 paper introducing the problem." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Original rendering of Michalski's trains going East and West, cropped from [@michalski_pattern_recognition_1980].
:::

::: {#fig-michalski-trains-vlol}
<img src="../../assets/michalski-trains/figure10-michalski-original-trains.png" alt="Michalski's original set of trains, as reproduced in the V-LoL diagnostic dataset paper." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Different rendering of Michalski's trains, cropped from [@helff_vlol_2023].
:::

### Patterns are not Laws
Overfitting etc.

## Developing Real Understanding


### Understanding the data

::: {#fig-ds-lifecycle-understand-data}
<img src="../../assets/lifecycle/ds-lifecycle-v3.svg" alt="The data science lifecycle with Understand the data highlighted." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Understanding the data, in the context of the data science lifecycle.
:::

TK

#### Proxies

TK


### Understanding the world

::: {#fig-ds-lifecycle-understand-world}
<img src="../../assets/lifecycle/ds-lifecycle-v4.svg" alt="The data science lifecycle with Understand the world highlighted." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Understanding the world, in the context of the data science lifecycle.
:::

TK

### Causes and confounds

Understanding the world, more than understanding the data, is where questions of *causation* arise. [Chapter 1](01-working-toward-wisdom.md) noted that the frequentist/Bayesian debate has largely been subsumed by the question of causal inference [@mcelreath_statistical_rethinking_2020]: what can we expect to happen from a given intervention? Causal modeling offers helpful standards for structural modeling via causal graphs (specifically, directed acyclic graphs, or DAGs) [@sep-causal-models], but it also opens up additional cans of worms. Namely, what does it actually mean for one thing to "cause" another thing? Here are some common complications in causal analysis:

* **Spurious regularities**: The rooster crows every morning right before sunrise, but the rooster does not cause the sun to rise. How do we separate real causes from things that just consistently show up at the same time?
	* (Structurally, this is a **fork**: some third factor drives two events without either causing the other.)
* **Multiple necessary conditions**: When a fire needs heat, fuel, and oxygen, which one is considered "the cause" of the fire?
	* (Structurally, this is a **collider**: several independent conditions point into the same effect.)
* **Causation without pattern**: How do we make sense of (or prove) one-time "causes" and effects that we cannot replicate? For example, how do we know the meteor caused dinosaur extinction?
* **Common causes**: Ice cream sales and drownings rise and fall together, but ice cream does not cause drowning (and drowning does not cause ice cream sales). How do we figure out when there is an underlying third factor (in this case summer weather) that drives multiple effects?
	* (Structurally, this is also a **fork**: the third factor points to both measured variables.)

::: {#fig-confound-fork}
<img src="../../assets/confounds/fork.svg" alt="Fork DAG: Z at the top with arrows pointing down to X on the left and Y on the right. Z is filled dark to mark the variable to split the data by." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

The fork: a common cause $Z$ (e.g., summer weather, or the Earth's rotation) drives both $X$ and $Y$, producing a correlation between them even though neither causes the other.
:::

* **Directionality**: A train's speedometer needle turns as the train goes faster, and the train goes faster as the speedometer needle turns. But of course, manually moving the needle will not speed up the train. How do we determine causal directionality in more complicated scenarios?
	* (Structurally, this is a backwards **pipe**. The speedometer needle is a downstream effect of the speed, but the needle does not cause the speed to change.)
* **Overdetermination**: Two people each empty a full bucket of water onto a campfire at the same moment, and either bucket alone may have been enough to put out the fire. Which bucket "caused" the fire to go out?
	* (Structurally, this is also a **collider**: two independent causes converge on one effect.)

::: {#fig-confound-collider}
<img src="../../assets/confounds/collider.svg" alt="Collider DAG: X on the left and Y on the right both point up to Z. Z is filled orange to warn against splitting the data by it." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

The collider: independent causes $X$ and $Y$ (e.g., heat and fuel, or two buckets of water) both point into a shared effect $Z$, so conditioning on $Z$ (e.g., "there is a fire") can make $X$ and $Y$ appear associated even when they are not.
:::

* **Unmeasured causes**: Consider the gas grill described in [@sep-causal-models], where the size of the flame depends on the gas level and the igniter, and how well the meat cooks depends on the flame. Suppose nobody wrote down the flame, and the only record is how the meat came out. Can the doneness of the meat stand in for the flame? Unlike the complications above, this is not necessarily a question about which cause is the "real cause." The question is: when the thing we care about was never directly measured, how do we reason about a trace or proxy of that thing?
	* (Structurally, this is a **descendant**: doneness $D$ is a side effect of the flame $Z$, so $D$ carries some of $Z$'s information but not all of it. Analyzing $D$ is a watered-down version of analyzing $Z$ — which means it also inherits a watered-down version of whatever problems $Z$ would have caused.)

::: {#fig-confound-descendant}
<img src="../../assets/confounds/descendant-collider.svg" alt="Descendant DAG: X on the upper left and Y on the upper right both point down to Z, which points down to D. Z and D are both filled orange to warn against splitting the data by either one." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

The descendant: $D$ (e.g., how well the meat cooked) is a side effect of $Z$ (the flame), which in this case is itself a collider between $X$ and $Y$ (the gas level and the igniter). Because $D$ carries part of $Z$'s information, conditioning on $D$ partially conditions on $Z$, and so leaks in a partial version of the collider bias from @fig-confound-collider.
:::

The unmeasured-cause problem connects directly to the discussion of proxies above: a descendant *is* a proxy, and reasoning about proxies means reasoning about what the proxy inherits from the thing it stands in for. For further discussion of these questions, see [@sep-causation-regularity]. Also, the [Week 6 slides about causal graphs](../slides/week6.qmd) work through elemental confounds — fork, pipe, collider, and descendant — in more depth.

### Uncertainty
TK

### Explanation as persuasion

TK

* when multiple models fit, choosing which to present is a rhetorical act
* More TK

### Validity, overfitting, generalization
TK

- mechanistic models and regression models
- Tanks story: model learned cloudy vs. sunny, not tanks [@dreyfus_what_computers_still_cant_do_1992; @yudkowsky_ai_positive_negative_2008]
- disputed origins of the Tanks story [@branwen_tank_legend_2011]
- Obtaining the right answer via the wrong reason
- Spurious correlations
- Diagnostic datasets to test the difference
- Michalski train problem [@michalski_pattern_recognition_1980]
- Automated train generation [@muggleton_random_train_generator_1998]
- V-LoL: visual version of the same test [@helff_vlol_2023; @ml_research_vlol_dataset_gen]

## Test

Test citations for understanding as situated, embodied interpretation: the Sierra Club John Muir Exhibit discussion of a common misquotation [@wood_john_muir_misquoted] and *Data Feminism for Data Visualization* [@klein_dignazio_data_feminism_visualization].

Transition to communication / decisions / reporting.

## References
