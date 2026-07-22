
# Old Stuff

### Zoom-in

For one, during the work of data science, you may find yourself (or your team) in a "repeated zoom-in" cycle, and it is useful to be able to recognize them. These repeated loops can be useful to support exploration, but infuriating when they seem to go on forever (as the saying goes, they make "helpful servants but terrible masters").

Data scientists will do well to recognize when they are "losing the forest for the trees," or when "mighty contests rise from trivial things" [@pope_rape_of_the_lock_1714, Canto I].

Then again, who gets to decide what is trivial?

### Frequentist worldview (long-run behavior)

* Probability as long-run frequency across repeated trials
* Confidence intervals and p-values as procedures with guaranteed long-run error rates
* The reference-class problem
* Statistics links data to hypotheses by using probability distributions over possible data sets [@sep-statistics].
* Classical statistics treats probabilities as chances attached to repeatable events, not as probabilities that hypotheses themselves are true [@sep-statistics].
* Frequentist procedures provide long-run error guarantees, but they also face a reference-class problem when reasoning about individual cases [@sep-statistics].

### Bayesian worldview (degrees of belief)

* Probability as a measure of uncertainty (belief) given information
* Parameters are treated as uncertain
* Data update beliefs ( Bayes' rule )
* Bayesian epistemology treats belief as coming in degrees, often called credences [@sep-epistemology-bayesian].
* Bayesian norms ask both how credences should fit together and how they should change with new evidence [@sep-epistemology-bayesian].
* Data update beliefs through conditionalization, but the result depends on the prior credences brought into the analysis [@sep-epistemology-bayesian].
* The problem of the priors matters because coherent starting points can still support different inductive conclusions [@sep-epistemology-bayesian].
* In Bayesian statistics, parameters are treated as uncertain, and posterior distributions support estimates and credibility intervals [@sep-statistics].

### Causal inference worldview (effects of interventions)

* Core question: what would happen if we intervened?
* Potential outcomes / counterfactuals, causal graphs (DAGs)
* A causal model represents causal relationships within a system or population so that statistical data can support causal inference [@sep-causal-models].
* Directed acyclic graphs make assumptions about dependence, independence, and causal direction explicit [@sep-causal-models].
* Observed probabilities alone may identify only a Markov equivalence class, so causal claims often require background assumptions or interventions [@sep-causal-models].
* The core causal question is interventionist: what would happen if we changed one part of the system? [@sep-causal-models]
* Regularity theories begin from the idea that causes are regularly followed by effects, but accidental regularities are not enough [@sep-causation-regularity].
* Millian regularity approaches treat causes as lawlike combinations of present positive factors and absent negative factors [@sep-causation-regularity].
* Inferential theories analyze causation through what effects can be inferred from causes within an appropriate background theory [@sep-causation-regularity].


## Test
These are test citations for @ackoff_data_1989, @vance_information_1997, @bernstein_data-information-knowledge-wisdom_2011, @rowley_wisdom_2007, @fricke_knowledge_2009, @zeleny_management_1987, and @payne_perfect_circles_2019.

The data-information-knowledge-wisdom (DIKW) framing is commonly discussed in the literature (e.g., @ackoff_data_1989; @vance_information_1997; @bernstein_data-information-knowledge-wisdom_2011).

The central premise is that ethical judgment is not a separate task for data scientists to work on after "technical" work is finished. Ethical decision-making shapes how data scientists frame questions, define project scopes, collect and prepare data, interpret patterns, develop understanding, and communicate new understanding to audiences.

---

## Chapter-by-chapter

### Chapter 1: Working Toward Wisdom

* Ethical frameworks as worldview lenses[@thomas_practical_data_ethics_2020].
* Explain "situated knowledge" and the "view from nowhere" [@dignazio_klein_data_feminism_2020]
* Data ethics sometimes considered a branch of ethics?
	* studies moral problems related to data, algorithms, and corresponding practices [@floridi_taddeo_what_is_data_ethics_2016].
* "Data visceralization" — making data sensory or bodily felt — alternative to purely abstract, detached representations of information [@wernimont_pandemic_death_counts_2022].

### Chapter 2: Ethics in Asking Questions

* questions for your questions
* Data Feminism - "who is missing?" — questions that can only be answered with available data implicitly exclude what was never counted [@dignazio_klein_data_feminism_2020].
* "what can be predicted" is different from "what should be predicted"
	* ask whose interests are served by the prediction [@veliz2026prophecy].

### Chapter 3: Ethics in Obtaining Data

* Consent as freely given, reversible, informed, enthusiastic, and specific (FRIES framework) [@lee_building_consentful_2017].
* "Datasheets for datasets" documentation practice
	* motivation, composition, collection process, and recommended uses, analogous to nutrition labels [@thomas_practical_data_ethics_2020].
* Data triangulation creates re-identification risks
	* individually innocuous data points (zip code, birthdate, sex) can be combined to uniquely identify people
* The Cambridge Analytica case as "control creep" — data collected for one purpose (Facebook profile enrichment) repurposed without explicit user consent [@wiki-data-ethics].
* labor behind datasets is often invisible: data annotation, cleaning, curation, etc. [@dignazio_klein_data_feminism_2020].

### Chapter 4: Ethics in Understanding

* Proxies
	* a variable that appears neutral (e.g., ZIP code, educational credential) may correlate tightly with protected characteristics [@barocas_selbst_big_data_disparate_impact_2016].
* Google Flu Trends overfit to search behavior, drifted badly in production
	* understanding search data is not the same as understanding influenza [@lazer_google_flu_2014].
* Types of bias to watch for in modeling [@thomas_practical_data_ethics_2020]
	* historical bias (in the real world before data collection)
	* representation bias (who is in the sample)
	* measurement bias (how variables are recorded)
	* aggregation bias (collapsing distinct groups) 
* Situated knowledge: acknowledge who did the analysis, with what data, and under what constraints, etc.[@dignazio_klein_data_feminism_2020]

### Chapter 5: Ethics in Reporting, Decisions, and Solutions

* Statistical and economic arguments as rhetorical acts (Deirdre McCloskey).
* Model cards as example transparency practice: intended uses, performance across groups, known limitations [@thomas_practical_data_ethics_2020]
* Predictions as interventions
	* e.g. a recommendation system that surfaces content changes what gets read. "Forecasts help produce futures" [@veliz2026prophecy].
* deficit-focused visualizations (showing what groups lack) vs. asset-based framings [@klein_dignazio_data_feminism_visualization].

### Chapter 6: Conclusions

* data ethics vs. data justice? [@dignazio_klein_data_feminism_2020].
* enduring ethical frameworks pre-date computing: consequentialist, deontological, and virtue-based reasoning each illuminate different aspects of data science decisions
	* none is sufficient alone
	* 