# Ethics in Reporting, Decision-Making, and Problem-Solving

**[← Back to Course Homepage](../../index.html)**

::: {#fig-ds-lifecycle-reports-decisions-solutions}
<img src="../../assets/lifecycle/ds-lifecycle-v5.svg" alt="The data science lifecycle with Reports, decisions, solutions highlighted." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Reports, decisions, and solutions, in the context of the data science lifecycle.
:::

*This chapter is in-progress.*

A data scientist may do a lot of work by themselves. Even a data science *team* may work within an organization for extended periods of time, and not interact with other teams.

But eventually, any valuable data science project will involve some kind of communication to the outside world. The reference textbook calls this phase of the lifecycle "reports, decisions, and solutions," and it usually requires the data scientist(s) to share results in some way.

For example, data scientists may often be asked to develop and/or analyze "key performance indicators" (KPIs) for an organization. KPIs (or simply "performance indicators") are metrics intended to evaluate progress toward a specific goal, kind of like a grade on a report card.

As another example, a data scientist may be asked to evaluate a specific change or intervention at an organization. "We put more native plants in the ground, did it reduce soil erosion?" "We gave employees a raise, did that boost morale?" When tasked with such questions, data scientists eventually report back about their findings.

This chapter explores some of the ethical considerations in the "reporting" phase of the data science lifecycle. When data scientists are making a specific decision, proposing a solution, or simply reporting about a previous decision/solution, there is vast potential for unintended consequences. In general, data scientists must take care at this phase of the lifecycle in order to avoid what Muller describes as a "tyranny of metrics" [@muller_tyranny_2018] - the overuse and/or misuse of measurement to justify certain decisions or behaviors.

This is especially important when predictive systems are used to shape the messages people see, how resources are allocated, and/or which choices are offered to people. In that sense, every prediction is an intervention: a forecast does not merely describe the future, but can help bring about the future it predicts [@veliz2026prophecy].

## Measuring What?

To ground this chapter, we will start exploring the ethics of reporting with a concrete example of college rankings.

### Example: College Rankings

Cathy O'Neil's book, *Weapons of Math Destruction* [@oneil_weapons_2017], describes a compelling case study of metrics around college rankings.

The U.S. News & World Report began with a straightforward question: what makes a good college, and how can we measure it? Notably, this was a deliberate attempt to save the U.S. News & World Report magazine, which had been struggling financially. In 1983, they realized that a ranking of 1,800 colleges and universities in the U.S. could be a valuable resource for millions of parents and high-schoolers approaching college decisions. I

So, beginning in 1988, U.S. News & World Report tried using data to 

This led to a trap. U.S. News & World Report could only develop their rankings based on measurable data. This may seem obvious, and many of the metrics seem like good proxies for what makes a good school:

* student-teacher ratios
* acceptance rates
* SAT scores
* percentage of freshmen who make it to sophomore year
* percentage of freshman who graduate

But consider some of the aspects of life which are left out of these metrics:

* a picnic table in shady spot on campus
* a fun intramural ultimate frisbee league
* a Friday night lecture series with free cookies
* a professor who recognizes you and waves hello on campus
* easy access to a nearby park
* ergonomic chairs in the library for long study periods
* a ten-minute walk to get a frozen dessert

### Measurement Scales

TK

* as an example of subjectivity / situated knowledge

### Goodhart's Law

TK

A measure can stop being a good measure when it becomes a target [@goodhart1984problems].

### Campbell's Law

TK

Social indicators become more vulnerable to corruption when used for high-stakes decision-making [@campbell1979assessing].

### Example: Bayesian Diagnostic Testing

Consider another classic case study in measurement and reporting concerns diagnostic testing in medicine. Veritasium's video *The Bayesian Trap* [@muller_bayesian_trap_2017] describes a version of this scenario: a disease affects 0.1% of the population, and a test for the disease is 99% accurate. Start with a random sample of 1,000 people.

::: {#fig-bayes-1000-people}
<img src="../../assets/bayes-diagnostic/01-bayes-diagnostic.svg" alt="A grid of 1,000 gray dots on a white background, representing a population of 1,000 people." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

1,000 people.
:::

At a 0.1% prevalence rate, we assume one person in this sample carries the disease.

::: {#fig-bayes-infected-one}
<img src="../../assets/bayes-diagnostic/02-bayes-diagnostic.svg" alt="The same grid of dots with one red dot highlighted by two concentric rings, representing a single infected person." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

0.1% carry the disease — that is 1 person.
:::

When everyone in the population takes the test how does the 99% accuracy play out?

::: {#fig-bayes-11-positives}
<img src="../../assets/bayes-diagnostic/03-bayes-diagnostic.svg" alt="The grid with 989 light gray dots faded back, 10 dark dots for false positives, and one red dot for the true positive." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

A test with 99% accuracy returns 11 positives.
:::

The test correctly identifies the one sick person, and it also returns a false positive for roughly 1% of the 999 healthy people — about 10 people. Those 11 positive results can be labeled — one is real, ten are not.

::: {#fig-bayes-true-false}
<img src="../../assets/bayes-diagnostic/04-bayes-diagnostic.svg" alt="The same grid with arrows pointing to each positive dot: one red arrow labeled 'true +' and ten dark arrows labeled 'false +'." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

11 people test positive, only 1 has the disease.
:::

Zooming in on just the 11 who tested positive: if you are one of them, what is the probability you actually have the disease?

::: {#fig-bayes-zoom-11}
<img src="../../assets/bayes-diagnostic/05-bayes-diagnostic.svg" alt="Eleven large dots in a scattered arrangement matching their positions in the grid above: one red dot and ten dark gray dots." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Testing positive: only a 1-in-11 (~9%) chance of having the disease.
:::

This answer (roughly 9%, or 1 in 11) is often surprising. Think about it: you took a test with 99% accuracy, it gave you a result, and there is only a 1 in 11 chance the result is correct. How can this be??

It is useful to put some names/labels on the associated "traps" to which our imperfect human cognition sometimes leads us:

* **base rate neglect** (i.e. fixating on the accuracy (99%) and overlooking the rarity of the disease (0.1%) - Bayes' theorem helps).
* ** accuracy vs. reliability** consider *positive predictive value* of a test, not just accuracy, to account for prevalence

Notes:

* generalizes to mammograms, HIV screening, drug testing, and security-threat detection, etc. (scenarios with a rare condition and an imperfect test)
* dot-grid (hopefully) visualization makes the base-rate problem legible to a general audience without heavy formulas [@muller_bayesian_trap_2017].


## Interventions and Predictions

### Interventions

TK

### Tech debt and documentation debt

TK

### Prediction as Influence

TK. Cite [@veliz2026prophecy].

## Towers, Pyramids, Cathedrals, Bazaars

Data scientists work in a variety of different organizational contexts, with different structures and workflows. These different contexts are particularly relevant to the reporting stage of the lifecycle, which involves actively contributing to the larger organization.

Still, before a data science project reaches the reporting stage, it is worth considering what kind of contributions will be expected at that stage, and how those expectations might shape work at every other stage.

[Chapter 1](01-working-toward-wisdom.md) framed data science work as contributing to the DIKW pyramid, while also hinting at the limitations of that metaphor and the possibility of other paradigms for knowledge creation. Architecture offers a few such paradigms, and each one implies a different answer to the question of who sees the work, and when.

TK [@raymond_cathedral_bazaar_1999]

* cathedral - central planning, construct based on the blueprint, often for worship
* pyramid - one layer at a time, construct what can be supported. Also tombs/monuments.
* bazaar - public view, exploratory, invite feedback and community contribution
* tower/ziggurats - restricted access (?), solid mass, purpose was...

::: {#fig-escher-tower-of-babel}
<img src="../../assets/art/escher_tower_of_babel_1928.jpg" alt="M.C. Escher's woodcut Tower of Babel (1928), depicting the unfinished biblical tower viewed from above, with tiny figures working on terraces." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

M.C. Escher, *Tower of Babel* (1928). Woodcut. [Source](https://en.wikipedia.org/wiki/File:Babel-escher.jpg)
:::

::: {#fig-bruegel-tower-of-babel}
<img src="../../assets/art/bruegel_tower_of_babel_1563.jpg" alt="Pieter Bruegel the Elder's oil painting The Tower of Babel (c. 1563), showing the vast unfinished spiral tower rising against a clouded sky, with workers and machinery at its base." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Pieter Bruegel the Elder, *The Tower of Babel* (c. 1563). Oil on panel. Kunsthistorisches Museum, Vienna. [Source](https://commons.wikimedia.org/wiki/File:Pieter_Bruegel_the_Elder_-_The_Tower_of_Babel_(Vienna)_-_Google_Art_Project_-_edited.jpg)
:::

::: {#fig-rozsda-tower-of-babel}
<img src="../../assets/art/rozsda_tower_of_babel_1958.jpg" alt="Endre Rozsda's 1958 painting La tour de Babel, a dense, fragmented composition in warm ochres and reds evoking accumulated layers of human history and industry." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Endre Rozsda, *La tour de Babel* (1958). [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). [Source](https://commons.wikimedia.org/wiki/File:Endre_Rozsda_-_La_tour_de_Babel_(1958).jpg)
:::

::: {#fig-pococke-pyramid-section}
<img src="../../assets/art/pococke_great_pyramid_section_1743.jpg" alt="Richard Pococke's 1743 engraving showing a cross-sectional diagram of the interior passages and chambers of the Great Pyramid, and below it a frontal view of the head of the Great Sphinx." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Richard Pococke, *A Section of the Great Pyramid, and a View of the Head of the Sphynx* (1743). Engraving from *A Description of the East* (London: W. Bowyer, 1743–1745). [Source](https://commons.wikimedia.org/wiki/File:A_Section_of_the_Great_Pyramid,_and_a_View_of_the_Head_of_the_Sphynx_-_Pococke_Richard_-_1743.jpg)
:::

::: {#fig-monet-rouen-cathedral}
<img src="../../assets/art/monet_rouen_cathedral_1894.jpg" alt="Claude Monet's 1894 painting of Rouen Cathedral's west facade in sunlight, rendered in thick impasto strokes of gold, cream, and blue-grey that dissolve the stone surface into light and atmosphere." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Claude Monet, *Rouen Cathedral, West Facade, Sunlight* (1894). Oil on canvas. National Gallery of Art, Washington, D.C. [Source](https://commons.wikimedia.org/wiki/File:Claude_Monet_-_Rouen_Cathedral,_West_Facade,_Sunlight.jpg)
:::

::: {#fig-mahane-yehuda-market}
<img src="../../assets/art/mahane_yehuda_market_2018.jpg" alt="Photograph of Mahane Yehuda market in Jerusalem, showing vendors and shoppers along a covered lane lined with stalls of produce, spices, and goods." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Emilio García, *Mahane Yehuda* (2018). Photograph of Mahane Yehuda Market, Jerusalem. [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/). [Source](https://commons.wikimedia.org/wiki/File:Mahane_Yehuda_(I)_(45298221191).jpg)
:::

## Communication

### Common Knowledge

Something profound happens when multiple people "read" (look at, watch, draw, view, etc.) information together. In brief, this is the phenomenon of common knowledge: shared awareness about what other people know, and/or what others have contributed to the pyramid.

Common knowledge is often confused with mutual knowledge. If we both know that there is only one more ice cream bar in the freezer, that is mutual knowledge. But if we both know *that the other person knows* that there is only one ice cream bar in the freezer, that is common knowledge, or awareness about what other people know.

Perhaps the best way to explain common knowledge is to recognize its use in storytelling methods which create suspense in film and television. For example, Alfred Hitchcock described the distinction between "surprise" and "suspense" as a difference in common knowledge: in a surprise, the audience discovers an important fact at the same time as the characters. The information is withheld from everyone [@hitchcock_interview_1973].

But suspense depends on *partially* shared information. For example, when the audience knows that there is a bomb under the dining table, but they also know that Bob was gone when the bomb was placed under the table. In Hitchcock's framing, this scenario creates suspense because the audience anticipates danger from the bomb, and also knows that Bob does not anticipate the same danger.

A data scientist can benefit from understanding and leveraging common knowledge (or lack thereof). When communicating results, for example, it may not be sufficient just to know what the audience knows. You may also want to know what audience members know *about what other audience members know*. The intricacies of common knowledge are fascinating, and two classic puzzles show how it can coordinate action [@fagin_reasoning_about_knowledge_1995].

In "the hat puzzle," row of people each wear a hat they cannot see, and no one is allowed to move until they deduce their own hat color. The line stays frozen. Then, a *public* announcement states "at least one of you wears a red hat." The announcement adds no new visible fact, yet it converts mutual knowledge into common knowledge — and that is what finally allows the line move.

A related puzzle, **the muddy children puzzle**, is described by @sep-dynamic-epistemic as follows:

> Three children are playing in the mud. Father calls the children to the house, arranging them in a semicircle so that each child can clearly see every other child. "At least one of you has mud on your forehead", says Father. The children look around, each examining every other child's forehead. Of course, no child can examine his or her own. Father continues, "If you know whether your forehead is dirty, then step forward now." No child steps forward. Father repeats himself a second time, "If you know whether your forehead is dirty, then step forward now." Some but not all of the children step forward. Father repeats himself a third time, "If you know whether your forehead is dirty, then step forward now." All of the remaining children step forward. How many children have muddy foreheads?

The father's announcement adds no new *visible* fact — every child could already see the others' foreheads — yet it creates the common knowledge that enables the deductions. Each round of silence carries information, and counting those silences lets each muddy child infer their own state.

### Audience

TK

test citations for communicating data with attention to emotion, embodiment, and audience - *Data Feminism for Data Visualization* [@klein_dignazio_data_feminism_visualization].

### Researcher Degrees of Freedom

TK

* many small choices shape the result
* same data, different analysts, different conclusions [@silberzahn2018]
* p-hacking definition
* p-values pile up suspiciously just below .05 [@masicampo2012]
* other fingerprints of p-hacking

### Retractions and Corrections

* so you made a mistake...
* scientific community has norms around acknowledging and correcting errors
* examples:
	* misunderstood the data source
	* discovered a coding error after publication
	* identified another flaw of some kind
* What you do next matters!

#### How to approach a mistake in your report

Good practices:
* **Assess severity.**
* **Contact publication venues.**
* **Write/publish a clear explanation.**
	* **Formal correction or retraction.** Follow publication guidelines.
		* A **correction** fixes specific factual or computational errors while keeping the work in the record.
		* A **retraction** withdraws the entire work (conclusions no longer supported).
* **Update downstream usage.** If/when findings were used by others.

#### Standards

Committee on Publication Ethics (COPE) has guidelines for retractions and corrections [@cope_retraction_2019].

Test citation for Retraction Watch [@van_noorden_2011_reality] (public database showing patterns in retraction)

### Test

classic studies in dubious data science - Facebook's political mobilization experiment [@bond_social_influence_2012], emotional contagion study [@kramer_emotional_contagion_2014], Target's pregnancy prediction marketing [@duhigg_companies_secrets_2012], Google Flu Trends [@lazer_google_flu_2014]...

test citations for ethical debriefs of the Facebook experiments - the PNAS editorial expression of concern [@verma_editorial_expression_2014], Grimmelmann's letter to the PNAS editor [@grimmelmann_letter_pnas_2014], and later research-ethics analyses [@kahn_learning_2014; @boyd_untangling_2016].

## References
