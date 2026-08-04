# Ethics in Obtaining Data

**[← Back to Course Homepage](../../index.html)**

::: {#fig-ds-lifecycle-obtain-data}
<img src="../../assets/lifecycle/ds-lifecycle-v2.svg" alt="The step of obtaining data, in the context of the data science lifecycle." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Obtaining data, in the context of the data science lifecycle.
:::

> "'Raw data' is an oxymoron."

-- Lisa Gitelman and Virginia Jackson [@gitelman_jackson_introduction_2013]

> "Every standard and each category valorizes some point of view and silences another."

-- Geoffrey Bowker and Susan Leigh Star in *Sorting Things Out* [@bowker_star_sorting_things_out_1999]

🔴 *Chapter Status: in development. Some sections drafted, mostly incomplete.*

<!-- TODO: write the **Overview:** box to match Chapters 1 and 2. -->

The process of obtaining data is perhaps the aspect of data science with the most concrete and direct ethical implications.

## Where do data come from?

Do you generate it?
Do you collect it?
Do you obtain it?
Are data "given" or "taken?" [@barrowman_data_never_raw_2018]
* "Data collection itself already is a form of processing."
* every dataset has "residue" of choices: who counted, what counted, what got left out [@bowker_star_sorting_things_out_1999]
* same phenomenon, different data depending on instrument, protocol, and category scheme (cf. the pixel/triangle examples in Ch. 1)
* "found" data (logs, scrapes, administrative records) were collected for someone else's purpose, not yours [@boyd_untangling_2016]
* provenance —where a value came from — as data [@buneman_why_and_where_2001]

## The rhetoric of "raw" data

* calling data "raw" is a persuasive move [@gitelman_jackson_introduction_2013]
	* implies untouched, natural, pre-interpretive, indisputable
* cooking metaphor: data are always already cooked, the question is by whom and with what recipe [@gitelman_jackson_introduction_2013]
* related moves: "the data speak for themselves," "just the numbers," "objective measurement" (cf. the "view from nowhere," @nagel_view_from_nowhere_1986; @haraway_situated_knowledges_1988)
* when working with a "raw" dataset, try to name
	* the collection instrument
	* the collector
	* discarded alternatives

## Sidebar: Can you start/end with data?

* the lifecycle allows two entry points: "ask a question" and "obtain data" (see Ch. 2)
* starting with data is common, reuse, secondary analysis, instrumentation that already exists
* inverted inference: letting the available data choose the question (streetlight effect)
* another risk at the other end: ending with data (a dashboard, a release) and never reaching a decision or an interpretation (Ch. 5)

## What "obtaining data" includes

* **primary** collection — surveys, sensors, experiments, instrumentation you control
* **secondary** sources — administrative records, public datasets, purchased data, etc.
* **scraping and APIs** — collection from other systems as data sources
* **synthetic data** — generated from a model rather than measured from the world
* **human labor** — annotation, crowdwork, labeling
* consider who was in a position to say no?

### Consent

* research consent (IRB / Common Rule / Belmont) and product consent (terms of service) are different instruments doing different work [@belmont_report_1979; @metcalf_crawford_human_subjects_2016]
* clicking "I agree" is not informed consent: not voluntary, not specific, not revocable in practice
* the "public data" defense — publicly visible is not publicly consented [@zook_ten_simple_rules_2017]
* consent does not scale: aggregate inference reaches people who never consented [@barocas_nissenbaum_end_run_2014]
* "consentful" design as an alternative frame: consent should be freely given, reversible, informed, enthusiastic, and specific [@lee_building_consentful_2017]
* case cross-reference: Facebook emotional contagion and voter mobilization (Appendix C)

### Scraping

* three separate questions, often conflated: is it *legal*, does it violate *terms of service*, is it *in the public interest*
* U.S. law has narrowed the Computer Fraud and Abuse Act: authorization means access limits, not use limits [@van_buren_v_us_2021; @hiq_v_linkedin_2022]
* social platforms - scraping terms are inconsistent across platforms [@fiesler_no_robots_2020]
* questions survive legality: expectations of the people in the data, aggregation harms, re-identification, burden on the host, etc.
* practical minimums: rate limits, robots.txt, no circumvention of authentication, no redistribution of raw personal data

### Licensing and provenance

* a dataset's license governs *reuse*, and is often incompatible with the license of the work you are building
* try not to break provenance chains
* documentation artifacts that carry provenance forward: datasheets for datasets [@gebru_datasheets_2021]
* stewardship principles: FAIR (findable, accessible, interoperable, reusable) [@wilkinson_fair_2016]
* CARE for Indigenous data governance [@carlisle_indigenous_care_2020]
* minimum record for any obtained dataset: source, date obtained, license, collection method, known exclusions

### Synthetic data

* pitched as a privacy fix — no real people, therefore no disclosure risk
* still can have biases and gaps from generator's training data
* privacy protection is not automatic: generative models can memorize and leak; formal guarantees require explicit mechanisms [@bellovin_privacy_synthetic_datasets_2019]
* useful for testing pipelines and sharing schemas
* less useful as evidence about the world
* disclosure obligation: synthetic provenance must travel with the data so it is not treated as measurement

## Sensitive information

### Defining Sensitive Information

* category-based definitions: GDPR "special categories" — race/ethnicity, political opinions, religion, union membership, genetic and biometric data, health, sex life, sexual orientation [@eu_gdpr_2016]
* U.S. sectoral definitions instead of a general one: HIPAA (health), FERPA (education), GLBA (finance), COPPA (children)
* the category approach fails because sensitivity is *contextual*, not intrinsic: a fact is sensitive depending on where it flows [@nissenbaum_privacy_contextual_integrity_2004]
* Nissenbaum contextual integrity — information flows carry norms attached to the context of collection
	* a violation is a flow that breaks those norms, even when the data are "public"
* worked example: ZIP code, birth date, and sex are individually innocuous and jointly identify most Americans [@sweeney_simple_demographics_2000]

### Handling Sensitive Information

* collect less: data you never obtained cannot leak - "data minimization"
* separate identifiers from attributes; store linkage keys apart from analysis tables
* access control by role, with logging — most breaches are internal over-access, not intrusion
* retention limits and deletion obligations, including the right to erasure [@eu_gdpr_2016]
* de-identification techniques and their limits: k-anonymity [@sweeney_k_anonymity_2002], and formal guarantees via differential privacy [@dwork_differential_privacy_2006]
* the 2020 U.S. Census as the largest deployment of differential privacy, and the accuracy/privacy tradeoff it forced into public view [@abowd_census_differential_privacy_2018]
* publication decisions : aggregation thresholds, suppression of small cells, refusal to release

## Risks from data triangulation

* triangulation: combining several non-identifying sources until they jointly identify someone
* the anonymization failure is general, not incidental — "anonymized" datasets are re-identifiable given any auxiliary information [@ohm_broken_promises_2010]
* Netflix Prize: sparse ratings de-anonymized against public IMDb reviews [@narayanan_shmatikov_deanonymization_2008]
* Massachusetts GIC hospital records re-identified by joining a public voter roll on ZIP, birth date, and sex [@sweeney_simple_demographics_2000]
* inference is a form of triangulation: attributes never collected can be predicted from those that were (see the Target pregnancy case, Appendix C)
* implication for release: privacy is a property of the *combination* of datasets in the world, not of any one dataset you control
* implication for obtaining: careful joining datasets !

## Maintaining Data

Although not formally captured in the data science lifecycle figure(s), data scientists are often responsible for maintaining the data they obtain and analyze.

* "data stewardship" — someone is accountable for a dataset over its whole life, not just at collection
* documentation as maintenance: schema, collection protocol, known defects, version history [@gebru_datasheets_2021]
* backups and retention — and the tension between them: backups defeat deletion promises unless retention policy covers them
* deletion obligations: legal (erasure requests, retention maxima), contractual, and promissory (what you told subjects at collection)
* deletion is harder than it looks — derived tables, caches, exports, and trained models all carry the data forward
* drift: datasets decay as the world they describe changes; a stale dataset is a correctness problem, not just a tidiness one
* stewardship standards - FAIR [@wilkinson_fair_2016] and CARE [@carlisle_indigenous_care_2020]

## Example: How the Census Obtains Data

The U.S. census offers a helpful example of ethical decision-making in the data science lifecycle. It has been explored in *Data Feminism* [@dignazio_klein_data_feminism_2020], in Kenneth Prewitt's *What Is Your Race?* [@prewitt_what_is_your_race_2013], in G. Cristina Mora's *Making Hispanics* [@mora_making_hispanics_2014], and in Bowker and Star's *Sorting Things Out* [@bowker_star_sorting_things_out_1999]. It is included here in brief as a canonical example of subjectivity in the process of obtaining data.

### Census form in 1790

[Massachusetts printed schedule used in the 1790 census](../../assets/census/1790-massachusetts-printed-schedule.pdf).

Categories in the 1790 census: free White males 16 and over, free White males under 16, free White females, all other free persons, and slaves.

::: {#fig-census-1790}
<img src="../../assets/census/1790-massachusetts-printed-schedule.png" alt="Massachusetts printed schedule used in the 1790 census." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Massachusetts printed schedule used in the 1790 census. Source: Census Bureau questionnaire page [@census_1790_questionnaire] and National Archives scan hosted by Census.gov [@national_archives_1790_schedule].
:::

### Census form in 1850

[Free Inhabitants schedule](../../assets/census/1850-free-inhabitants-schedule.png).

Categories: name, age, sex, color, occupation, value of real estate, birthplace, married within the year, school attendance, literacy, deafness, dumbness, blindness, insanity, idiocy, pauper status, and conviction.

::: {#fig-census-1850}
<img src="../../assets/census/1850-free-inhabitants-schedule.png" alt="1850 Free Inhabitants schedule." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

The 1850 Free Inhabitants schedule. Source: Census Bureau questionnaire page [@census_1850_questionnaire] and direct image file from Census.gov [@census_1850_free_inhabitants_image].
:::

### Census form in 1940

[Population questionnaire](../../assets/census/1940-population-questionnaire.pdf).

Categories: name, relationship, personal description, residence, birthplace, citizenship, education, employment, occupation, income, veteran status, Social Security, and selected supplemental questions for sample respondents.

::: {#fig-census-1940}
<img src="../../assets/census/1940-population-questionnaire.png" alt="1940 population questionnaire." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

The 1940 population questionnaire. Source: Census Bureau questionnaire page [@census_1940_questionnaire] and direct PDF from Census.gov [@census_1940_population_pdf].
:::

### Census form in 2020

[Informational bilingual questionnaire](../../assets/census/2020-informational-questionnaire.pdf).

Categories: household count, ownership or tenure, phone number, name, sex, age and date of birth, Hispanic/Latino/Spanish origin, race, relationship, and whether the person usually lives or stays elsewhere.

::: {#fig-census-2020}
<img src="../../assets/census/2020-informational-questionnaire.png" alt="2020 informational bilingual questionnaire." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color); padding: 10px;" />

The 2020 informational bilingual questionnaire. Source: Census Bureau questionnaire page [@census_2020_questionnaire] and direct PDF from Census.gov [@census_2020_informational_pdf].
:::

### Survey Design decisions

Federal statistical categories are set by the Office of Management and Budget, not by the Census Bureau alone:

* the 1997 standards (Statistical Policy Directive No. 15) treated Hispanic or Latino origin as an *ethnicity* asked separately from race, and required that respondents be allowed to select more than one race [@omb_race_ethnicity_standards_1997]
	* race totals can exceed the total population
	* counts are not directly comparable across censuses before and after 2000
* the separate-question design produced a persistent mismatch — large numbers of Hispanic/Latino respondents selected "Some other race," because the offered categories did not describe them [@omb_spd15_revision_2024]
* the "Hispanic" category itself came from activist /bureaucratic / media coordination in the 1970s [@mora_making_hispanics_2014]
* in 2024 OMB revised SPD 15: a single combined race-and-ethnicity question, and a new Middle Eastern or North African (MENA) category [@omb_spd15_revision_2024]
* these counts drive apportionment, redistricting, civil-rights enforcement, funding formulas, and more [@prewitt_what_is_your_race_2013]

### Privacy in the 2020 census

* the Census Bureau adopted differential privacy for the 2020 release, replacing prior swapping-based disclosure avoidance [@abowd_census_differential_privacy_2018]
* motivation: reconstruction and re-identification attacks on published tabulations
	* the triangulation risk above, at national scale
* injected noise protects respondents but degrades small-area counts 
	* used by tribal governments, school districts, and redistricting
*  accuracy/privacy tradeoff of obtaining data discussed publicly

## Example: Facebook Profile

Similar dynamics can be observed in the Facebook signup process: the process of "obtaining data" involved numerous subjective decisions. Until 2014, the signup process for Facebook offered three options in the gender field: male, female, or no answer. On February 13, 2014, Facebook substantially expanded its gender fields, with 58 different options, custom fields, and additional pronoun settings.

Sources: ABC News [@abcn_news_facebook_gender_2014] and CNN [@kelly_facebook_gender_2014].

Parallels to the census example:

* both are *category design* problems: the form determines what can be said / what can be counted [@bowker_star_sorting_things_out_1999]
* both changed their categories in response to political pressure, not new measurement technology
* both create the same comparability break — pre-2014 and post-2014 gender data are not the same variable
* residual category problem: "no answer" and "Some other race" are where the scheme's failures accumulate

Differences:

* the census publishes its category rationale in the Federal Register; the platform does not
* despite 58 front-end options, Facebook reportedly continued to resolve users into a binary for advertising purposes
	* i.e. the *stored* category vs the *displayed* category [@bivens_gender_binary_facebook_2017]
* a field offered as self-expression
	* became used for targeting
	* a contextual-integrity violation with no breach / scraping 

## Conclusion


* data are obtained, not found
* every dataset has fingerprints of its collection
* data collection may be where it is cheapest to fix
	* but also easiest to skip
* the next chapter (Ch. 4) asks what these obtained data can and cannot be understood to mean

## References
