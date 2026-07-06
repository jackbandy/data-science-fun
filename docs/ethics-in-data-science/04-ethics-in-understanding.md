# Ethics in Understanding

**[← Back to Course Homepage](../../index.html)**

::: {#fig-ds-lifecycle-v0}
<img src="../../assets/lifecycle/ds-lifecycle-v0.svg" alt="The full data science lifecycle diagram." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

The data science lifecycle. Although each stage of the lifecycle requires some degree of human understanding, this chapter focuses on the two stages that explicitly include "understanding."
:::

> "When we try to pick out anything by itself, we find it hitched to everything else in the Universe."
>
> -- John Muir, as quoted by the Sierra Club John Muir Exhibit [@wood_john_muir_misquoted]

> "All models are wrong."
>
> -- [George E. P. Box]

> "A map is not the territory it represents, but, if correct, it has a similar structure to the territory, which accounts for its usefulness."
>
> -- Alfred Korzybski [@korzybski_non_aristotelian_1931]

*This chapter is in-progress.*

## Your Model is Always Wrong

The two previous chapters discussed limits in asking questions and obtaining data, which tend to be the starting points for data science lifecycles. Once equipped with question(s) and data, however limited both may be, the next step is to pursue understanding.

In the ideal lifecycle, data scientists will be able to understand the data in ways that also help them understand the world. This is much easier said than done, for reasons that will be explored in this chapter.

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

## What "understanding" includes
TK.


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

### Uncertainty
TK

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

## References
