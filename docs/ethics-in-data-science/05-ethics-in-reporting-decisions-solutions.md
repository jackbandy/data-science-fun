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

We will start exploring this with a concrete example of college rankings.

## Case Study: College Rankings
Cathy O'Neil's excellent book, *Weapons of Math Destruction* [@oneil_weapons_2017], sets up an excellent case study around college rankings.

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



## Goodhart's Law


A measure can stop being a good measure when it becomes a target [@goodhart1984problems].

## Campbell's Law

Social indicators become more vulnerable to corruption when used for high-stakes decision-making [@campbell1979assessing].


## What "reporting, decisions, & solutions" includes

TK

## Interventions

TK

## Tech debt and documentation debt

TK

## Prediction as Influence

TK. Cite [@veliz2026prophecy].

## Communication and audience

TK

* (Another spot to draw on Deirdre McCloskey, i.e. statistical/economic arguments being rhetorical acts; obligations when persuading with models, metrics, etc.)


## Retractions and Corrections

* so you made a mistake...
* scientific community has norms around acknowledging and correcting errors
* examples:
	* misunderstood the data source
	* discovered a coding error after publication
	* identified another flaw of some kind
* What you do next matters!

### How to approach a mistake in your report

Good practices:
* **Assess the severity.**
* **Contact any publication venue.**
* **Write/publish a clear explanation.**
	* **Formal correction or retraction if appropriate.** Follow the publication's guidelines. A **correction** fixes specific factual or computational errors while keeping the work in the record. A **retraction** withdraws the entire work (conclusions no longer supported).
* **Update downstream usage.** If/when findings were used by others.

### Standards

Committee on Publication Ethics (COPE) has guidelines for retractions and corrections [@cope_retraction_2019].

Test citation for Retraction Watch [@van_noorden_2011_reality] (public database showing patterns in retraction)



## Test
classic studies in dubious data science - Facebook's political mobilization experiment [@bond_social_influence_2012], emotional contagion study [@kramer_emotional_contagion_2014], Target's pregnancy prediction marketing [@duhigg_companies_secrets_2012], Google Flu Trends [@lazer_google_flu_2014]...

test citations for ethical debriefs of the Facebook experiments - the PNAS editorial expression of concern [@verma_editorial_expression_2014], Grimmelmann's letter to the PNAS editor [@grimmelmann_letter_pnas_2014], and later research-ethics analyses [@kahn_learning_2014; @boyd_untangling_2016].

test citations for communicating data with attention to emotion, embodiment, and audience - *Data Feminism for Data Visualization* [@klein_dignazio_data_feminism_visualization].


## References
