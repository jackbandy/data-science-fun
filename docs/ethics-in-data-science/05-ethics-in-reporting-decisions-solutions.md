# Ethics in Reporting, Decision-Making, and Problem-Solving

**[← Back to Course Homepage](../../index.html)**

::: {#fig-ds-lifecycle-reports-decisions-solutions}
<img src="../../assets/lifecycle/ds-lifecycle-v5.svg" alt="The data science lifecycle with Reports, decisions, solutions highlighted." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Reports, decisions, and solutions, in the context of the data science lifecycle.
:::

*This chapter is in-progress.*

A data scientist may do a lot of work by themselves. Even a data science *team* may work within an organization for extended periods of time, and not interact with other teams.

But eventually, data science projects usually involve some kind of communication to the outside world. The reference textbook calls this phase of the lifecycle "reports, decisions, and solutions," and it usually requires the data scientist(s) to share results in some way.

For example, data scientists may often be asked to develop and/or analyze "key performance indicators" (KPIs) for an organization. KPIs (or simply "performance indicators") are metrics intended to evaluate progress toward a specific goal, kind of like a grade on a report card.

As another example, a data scientist may be asked to evaluate a specific change or intervention at an organization. "We put more native plants in the ground, did it reduce soil erosion?" When given such a task, data scientists must eventually report back about their findings.

This chapter explores some of the ethical considerations in the "reporting" phase of the data science lifecycle. When data scientists are making a specific decision, proposing a solution, or simply reporting about a previous decision/solution, there is vast potential for unintended consequences. In general, data scientists must take care at this phase of the lifecycle in order to avoid what Muller describes as a "tyranny of metrics" [@muller_tyranny_2018] - the overuse and/or misuse of measurement.

This is especially important when predictive systems are used to shape what people see, how resources are allocated, or which options are made available. In that sense, every prediction is an intervention: a forecast does not merely describe the future, but can help bring about the future it predicts [@veliz2026prophecy].

## Measuring What?

We will start exploring the ethics of reporting with a concrete example of college rankings.

### Example: College Rankings

Cathy O'Neil's book, *Weapons of Math Destruction* [@oneil_weapons_2017], sets up an excellent case study around college rankings.

What makes a good college? Beginning in 1988, U.S. News & World Report tried to answer this question using data. (footnote: notably, this was a deliberate attempt to save the magazine, which had been struggling financially. In 1983, they decided ranking 1,800 colleges and universities in the U.S. could provide a useful resource for millions of young people).

This led to a trap. U.S. News & World Report could only develop their rankings based on measurable data. This may seem obvious, and many of the metrics seem like good proxies for what makes a good school:

* student-teacher ratios
* acceptance rates
* SAT scores
* percentage of freshmen who make it to sophomore year
* percentage of freshman who graduate

But consider what is left out of these metrics:

* a picnic table in shady spot on campus
* a fun intramural ultimate frisbee league
* a Friday night lecture series with free cookies
* a professor who recognizes you and waves hello on campus
* easy access to a nearby park
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

## Communication and Accountability

### Communication and audience

TK

* (Another spot to draw on Deirdre McCloskey, i.e. statistical/economic arguments being rhetorical acts; obligations when persuading with models, metrics, etc.)

test citations for communicating data with attention to emotion, embodiment, and audience - *Data Feminism for Data Visualization* [@klein_dignazio_data_feminism_visualization].

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
