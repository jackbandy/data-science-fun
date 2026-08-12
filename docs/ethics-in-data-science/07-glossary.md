# Glossary

**[← Back to Course Homepage](../../index.html)**

## Key Terms

⬜ *Section Status: early development. Most entries are still placeholders.*

TK: terms used throughout the book, with definitions and pointers to relevant chapter(s).

[Aristotle's four causes]{#four-causes}
: TK — four different ways that one thing can explain another thing: the *material cause*, *formal cause*, *efficient cause*, and *final cause* [Source: @sep-aristotle-causality]

Campbell's Law
: The notion that social indicator metrics often become corrupt and unreliable when used for high-stakes decision-making. Examples include standardized test scores (Campbell's example), mortality scorecards for surgeons [@dranove_report_cards_2003], and sales quotas tied to compensation [@cfpb_wells_fargo_consent_order_2016]. See @sec-campbells-law. [Source: @campbell1979assessing]

Causation without pattern
: Occasions when one-time causes and effects cannot be replicated, e.g. the meteor which caused the dinosaur extinction. See @sec-statistical-worldviews. [Source: @sep-causation-regularity]

Common causes
: Cases in which an underlying third factor is driving two effects, e.g. summer weather, ice cream sales, drownings. See @sec-statistical-worldviews. [Source: @sep-causation-regularity]

Common knowledge
: Shared awareness about what other people know. That is, not just knowing a proposition/fact, but also having awareness that others know that proposition/fact too (as well as others knowing that *you* know that proposition/fact). Often conflated with mutual knowledge. [Source: @sep-common-knowledge]

Consent
: Permission that is freely given, reversible, informed, enthusiastic, and specific. [Source: @lee_building_consentful_2017]

Data
: Multiple datum.

Data Science
: See @sec-defining-data-science.

Data science lifecycle
: TK

Data triangulation
: TK

Data visceralization
: an attempt to make data sensory, bodily, or experientially felt in some way. [Source: @mit_media_lab_dobson_2014; @wernimont_pandemic_death_counts_2022]

Datum
: A single data point, such as a number or symbol.

Directionality
: Relevant when determining which of two correlated things is the cause and which is the effect, e.g. train's speed and its speedometer needle. See @sec-statistical-worldviews. [Source: @sep-causation-regularity]

Disparate impact
: TK [@barocas_selbst_big_data_disparate_impact_2016]

Documentation debt
: TK

Efficient cause
: TK — the source of change or rest, e.g. for a bronze statue, the art of bronze-casting. One of [Aristotle's four causes](#four-causes). [Source: @sep-aristotle-causality]

Ethics
: Acting well in the world. [Source: @burton_computing_2023]

Eudaimonia
: TK
Often translated "happiness" or "flourishing"
The highest human good, the [telos](#telos) which Aristotle argues is the aim of all human activity: "Every art and every inquiry, and similarly every action and pursuit, is thought to aim at some good" [@aristotle_nicomachean_ethics, *Nicomachean Ethics* I.1, 1094a].
More than pleasure or satisfaction or a specific state of feeling.
"human good turns out to be activity of soul in accordance with virtue" [@aristotle_nicomachean_ethics, *Nicomachean Ethics* I.7, 1097b–1098a]. 

Final cause
: TK — a thing's purpose or end, what it is good for. One of [Aristotle's four causes](#four-causes). [Source: @sep-aristotle-causality]

Formal cause
: TK — a thing's real-world essence. E.g. for a bronze statue, the actual shape of the bronze. One of [Aristotle's four causes](#four-causes). [Source: @sep-aristotle-causality]

Goodhart's Law
: The notion that a measure can stop being a helpful measure when it becomes a target. E.g. see @sec-college-rankings: acceptance rates, student-teacher ratios, and reported SAT scores can all be moved directly once they are ranked on (but may or may not improve the actual school quality). See @sec-goodharts-law. [Source: @goodhart1984problems]

Information
: TK

Knowledge
: TK

Material cause
: What a thing is made of. E.g. for a bronze statue, the bronze. One of [Aristotle's four causes](#four-causes). [Source: @sep-aristotle-causality]

Multiple necessary conditions
: Describes when several conditions are required for a given outcome (which one counts as "the" cause?). E.g. a fire needs heat, fuel, and oxygen.

Mutual knowledge
: A proposition is mutual knowledge among people when each person knows that proposition. Often conflated with common knowledge. [Source: @sep-common-knowledge]

Overdetermination
: Describes situations in which two sufficient causes may occur at once, e.g. two people each empty a full bucket of water onto a campfire.

Presupposition
: A background claim that must be true in order for a question to have a meaningful answer. [Source: @sep-questions]

Provenance
: TK

Proxy
: TK [@barocas_selbst_big_data_disparate_impact_2016]

Sensitive information
: TK [@nissenbaum_privacy_contextual_integrity_2004]

Situated knowledge
: TK [@dignazio_klein_data_feminism_2020]

Spurious regularities
: Used to describe when things consistently occur together without one causing the other, e.g. rooster crows every morning before sunrise. See @sec-statistical-worldviews. [Source: @sep-causation-regularity]

Tech Debt
: TK

Teleology
: Explanation of something based on its end or purpose, not what came before it to "cause" it. "Nature is a cause, a cause that operates for a purpose" [@aristotle_physics, *Physics* II.8, 199b]. Rosenblueth, Wiener, and Bigelow - what does a model or metric "aim" at [@rosenblueth_wiener_bigelow_teleology_1943]. TK — connect to @sec-goodharts-law.

[Telos]{#telos}
: The "end," "goal," or "completion" toward which a thing is directed (root of *teleology*). Another name for the "final cause," the fourth of [Aristotle's four causes](#four-causes): "in the sense of end or 'that for the sake of which' a thing is done, e.g. health is the cause of walking about" [@aristotle_physics, *Physics* II.3, 194b].

Wisdom
: TK

Worldview
: TK [@taves_worldview_studies_2019; @sep-statistics]

## Defining Data Science {#sec-defining-data-science}

One of the dilemmas I encountered when first working on this course was settling on a basic definition: _what exactly is data science?_ I have compiled some key reference points here, in case they may be useful to others.

Given the plurality of definitions for "data," as well as the plurality of definitions for "science," it is perhaps unsurprising that "data science" lacks a clear, singular definition. Still, there are some key points for clarification.

One crucial point is that **data science is more than just the study of data** (or the "science of data").

In a 1991 paper, Michael R. Fellows wrote that "Computer Science is not about machines, in the same way that astronomy is not _about telescopes_" [@fellows_cs_1991]. Computer Science is more about the study of what can be computed, and the various methods which Computer Scientists use to approach questions about computability (e.g. analysis, design, theory, experimentation).

Similarly, Data Science is about more than just studying data: it necessarily involves such questions as: What are data useful for? What methods allow us to learn from data? What are the limits of learning from data? What exactly is (and/or is not) captured in data? Data scientists must be aware of data's limitations, and how these limitations may affect the information and knowledge built on top of data (recall the DIKW pyramid from [Chapter 1](01-working-toward-wisdom.md).

Here are some approaches to define data science:

- **Vasant Dhar (2013)**: gives a concise, prediction-oriented definition: "data science is the study of the generalizable extraction of knowledge from data" [@dhar_data_science_2013].

- **Drew Conway (2010)** offered a visual definition: the Data Science Venn Diagram, which locates data science at the intersection of _hacking skills_, _math and statistics knowledge_, and _substantive (domain) expertise_ [@conway_venn_2010].

  ::: {#fig-data-science-venn}
  <img src="../../assets/data-science-venn/data_science_venn_remix_v2.svg" alt="Venn diagram with three overlapping circles labeled Hacking Skills, Math &amp; Statistics Knowledge, and Substantive Expertise. Their intersections are labeled Machine Learning, Traditional Research, and Danger Zone, with Data Science at the center." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

  A remix of Drew Conway's Data Science Venn Diagram, showing the intersection of hacking skills, math/statistics knowledge, and domain expertise. Based on [Conway's original blog post](http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram).
  :::

- **Cathy O'Neil and Rachel Schutt (2013)** ask a fun question "can we use data science to define data science?" [@oneil_2013_doing]. They analyze… TK.

- **William S. Cleveland (2001)** used "data science" to name an expansion/extension of "the technical areas of the field of statistics," toward work with data and computing. Specifically, he proposed that "the altered field will be called 'data science'" [@cleveland_data_science_2001].
	- "technical areas of data science should be judged by the extent to which they enable the analyst to learn from data"

- **Foster Provost and Tom Fawcett (2013)**: offer a high-level definition of data science as "a set of fundamental principles that support and guide the principled extraction of information and knowledge from data" [@provost_fawcett_data_science_2013], thus aligning with the concept of the DIKW pyramid.
	- "Possibly the most closely related concept to data science is data mining—the actual extraction of knowledge from data via technologies that incorporate these principles."

- **David Donoho (2017)**: in the essay "50 Years of Data Science," Donoho takes the view of "greater data science" and defines it as "the science of learning from data; it studies the methods involved in the analysis and processing of data and proposes technology to improve methods in an evidence-based manner" [@donoho_50_years_2017].
	- "I present a vision of data science based on the activities of people who are 'learning from data', and I describe an academic field dedicated to improving that activity in an evidence-based manner"

- **Hadley Wickham and Garrett Grolemund (2017)** offer an informal definition in the _R for Data Science_ textbook: "Data science is an exciting discipline that allows you to turn raw data into understanding, insight, and knowledge" [@wickham_grolemund_r4ds_2017]. Here we see another nod toward the DIKW pyramid, with "understanding" and "insight" also incorporated.

- **NIST Big Data Interoperability Framework (2019)**: The National Institute of Standards and Technology, formerly known as the National Bureau of Standards, knows a thing or two about standardizing definitions. They suggest that "Data science is the extraction of actionable knowledge directly from data through a process of discovery, or hypothesis formulation and hypothesis testing" [@nist_big_data_definitions_2019].

- The **ACM Data Science Task Force (2021)** characterized data science as an interdisciplinary field spanning computing, statistics, machine learning, and domain sciences, which "situates computing-specific competencies within the broader interdisciplinary space" [@acm_dstf_ccdsc_2021]. It defines data science through _competencies_ (i.e. knowledge, skills, and dispositions) that computing students should develop.

### From Venn Diagrams to Mastodons

There is a helpful parable for understanding different attempts to define such a complex and multifaceted topic. In one version of the parable, a king invites a group of blind men into his palace, and brings in an elephant. The king asks the blind men to describe the elephant.

Each man shares a different definition: the one who touched the tusk says "an elephant is like the sharp part of the plow," while the one who touched the leg says "an elephant is like a sturdy column, a pillar." Another touched the tip of the tail and claims "an elephant is like a paintbrush or a broom!" There is some meta-irony in the fact that the parable has many versions and adaptations.

Here, I will add yet another version, in a humble attempt to give a pluralistic definition of data science: the data science elephantidae.

Elephantidae is a biological family (of the taxonomic order of Proboscidea, the class mammalia, the phylum chordata, within the animal kingdom). I will not stretch the metaphor across the entire phylogenetic tree of the elephant, however, I do think the elephantidae family is helpful.

For one, it preserves the relevance of the blind men and the elephant, or the elephant in the dark, or whichever version you prefer. The specific part(s) of the elephant which one touches will lead them to a different definition of the data science elephant.

Taking it a step further, data scientists are also often trying to define slightly different species which all belong to a common family - elephantidae. This captures the notion of data science as a "big tent" field, or perhaps a post-discipline.

And to go just one step further, the elephantidae family includes mammoths and mastodons, which lived about 50,000 years ago during the ice age, alongside massive glaciers https://nhmu.utah.edu/articles/mammoths-and-mastodons-made-great-ice-age-team

Mammoths and mastodons did not actually live directly on glaciers, and in some cases, glaciers actually trapped mammoths and led to their death https://en.wikipedia.org/wiki/Snowmastodon_site but their proximity to icebergs allows me to draw one final point from the elephantidae metaphor, which is essentially this: it all goes much deeper. Data science is much larger than one method or one textbook, and even when viewed as a "family" of methods or topics or fields, it is still just one family of scholarship. In other words, the iceberg is very deep, and data science will only take you so far.

Especially when viewed as a family, the data science elephantidae are strong. A mastodon can take us very far, particularly when traveling in herds. At the same time, data scientists may find ourselves surrounded by icebergs. Some icebergs entrap us. Others are too weak or too melted for a mastodon to stand on. And other icebergs may be sturdy enough for herd to cross, and yet, they go far deeper than a mammoth could ever reach or comprehend.

In short, data scientists do not have a monopoly on human knowledge, even when viewed as a wide family. We would do well to collaborate with and learn from other families in the vast ecosystems of human knowledge and wisdom.

::: {.content-visible when-format="html"}
## References
:::
