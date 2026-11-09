# Glossary

**[← Back to Course Homepage](../../index.html)**

## Key Terms

⬜ *Section Status: early development. Some entries are still placeholders.*

TK: terms used throughout the book, with definitions and pointers to relevant chapter(s).

[Access frame]{#access-frame}
: "the collection of elements that are accessible to you for measurement and observation." Ideally the access frame and the [target population](#target-population) consist of the same elements. See also [coverage gap](#coverage-gap). [Source: @lau_learning_2023, sec. 2.2]

Accuracy
: The fraction of observations a classifier labels correctly: $\frac{TP + TN}{TP + FP + TN + FN}$. Accuracy can mislead when some error types matter more; see [precision](#precision) and [recall](#recall). [Source: [Week 9 Slides](../../slides/week9.html); [Week 10 Slides](../../slides/week10.html)]

Adjacency matrix
: A matrix that describes a [graph](#graph): "The entry in row $i$ and column $j$ is 1 if there is an edge between nodes $i$ and $j$, and 0 otherwise." [Source: @leskovec_social_network_graphs_2020, sec. 10.9]

Alternative hypothesis ($H_a$)
: The hypothesis that contradicts the null hypothesis.

[Aristotle's four causes]{#four-causes}
: TK — four different ways that one thing can explain another thing: the *material cause*, *formal cause*, *efficient cause*, and *final cause* [Source: @sep-aristotle-causality]


Bayes' theorem
: A rule relating a conditional probability to its reverse: $P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}$. [Source: [Week 2 Slides](../../slides/week2.html)]

Bipartite graph
: A [graph](#graph) with two groups of nodes, and edges only between the groups. It is the $k = 2$ case of a $k$-partite graph, which "consists of $k$ disjoint sets of nodes, with no edges between nodes of the same set." See also [complete bipartite graph](#complete-bipartite). [Source: @leskovec_social_network_graphs_2020, sec. 10.1.4]

Campbell's Law
: The notion that social indicator metrics often become corrupt and unreliable when used for high-stakes social decision-making. Examples include standardized test scores (Campbell's example), mortality scorecards for surgeons [@dranove_report_cards_2003], and sales quotas tied to compensation [@cfpb_wells_fargo_consent_order_2016]. See @sec-campbells-law. [Source: @campbell1979assessing]

Causation without pattern
: Occasions when one-time causes and effects cannot be replicated, e.g. the meteor which caused the dinosaur extinction. See @sec-statistical-worldviews. [Source: @sep-causation-regularity]

Clique
: "a set of nodes with edges between any two of them," e.g. five friends who all know one another. [Source: @leskovec_social_network_graphs_2020, sec. 10.3.1]

[Cohesion]{#cohesion}
: How similar the observations within a cluster are to one another. [Source: [Week 10 Slides](../../slides/week10.html)]

Common causes
: Cases in which an underlying third factor is driving two effects, e.g. summer weather, ice cream sales, drownings. See @sec-statistical-worldviews. [Source: @sep-causation-regularity]

Common knowledge
: Shared awareness about what other people know. That is, not just knowing a proposition/fact, but also having awareness that others know that proposition/fact too (as well as others knowing that *you* know that proposition/fact). Often conflated with mutual knowledge. [Source: @sep-common-knowledge]

Community
: A small set of nodes in a graph with "a much higher density of edges than the average density." Communities often overlap; see [overlapping communities](#overlapping-communities). [Source: @leskovec_social_network_graphs_2020, sec. 10.9]

Complementary events
: Two events where one occurs if and only if the other does not, e.g. heads and tails on a single coin flip. [Source: [Week 2 Slides](../../slides/week2.html)]

[Complete bipartite graph ($K_{s,t}$)]{#complete-bipartite}
: A graph that "has two groups of nodes, all possible edges between pairs of nodes chosen one from each group, and no edges between nodes of the same group." $K_{s,t}$ has $s$ nodes in one group and $t$ in the other. [Source: @leskovec_social_network_graphs_2020, sec. 10.9]

Conditional probability
: The probability of an event $A$ given that another event $B$ has already happened: $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$.

Consent
: Permission that is freely given, reversible, informed, enthusiastic, and specific. [Source: @lee_building_consentful_2017]

Covariate
: A variable used to help predict an outcome, e.g. enrollment, weekday, holiday, or weather when predicting daily transit ridership. @lau_learning_2023 list "response and covariate" as one of several name pairs for an outcome and its predictor. [Source: [Week 6 Slides](../../slides/week6.html); @lau_learning_2023, sec. 15.1]

[Coverage gap]{#coverage-gap}
: The part of the [target population](#target-population) that the [access frame](#access-frame) cannot reach. See also [sampling gap](#sampling-gap). [Source: [Week 2 Slides](../../slides/week2.html)]

Data
: Multiple datum.

Data Science
: See @sec-defining-data-science.

Data science lifecycle
: The stages of a data science project. @lau_learning_2023 divide it into four stages: "Ask a Question, Obtain Data, Understand the Data, and Understand the World." This book adds a fifth stage for reports, decisions, and solutions; see the [Preface](index.md). [Source: @lau_learning_2023, sec. 1.1]

Data triangulation
: TK

Data visceralization
: an attempt to make data sensory, bodily, or experientially felt in some way. [Source: @mit_media_lab_dobson_2014; @wernimont_pandemic_death_counts_2022]

Datum
: A single data point, such as a number or symbol.

Degree
: The number of edges at a node. A [self-loop](#self-loop) adds 2 to its node's degree. See also [in-degree](#in-degree) and [out-degree](#out-degree). [Source: [Week 12 Slides](../../slides/week12.html)]

Degree matrix
: "The degree matrix for a graph has $d$ in the $i$th diagonal entry if $d$ is the degree of the $i$th node. Off the diagonal, all entries are 0." [Source: @leskovec_social_network_graphs_2020, sec. 10.9]

[Dendrogram]{#dendrogram}
: A tree diagram of the nested clusters found by [hierarchical clustering](#hierarchical-clustering). Cutting the tree at any height gives a [partitional clustering](#partitional-clustering). [Source: [Week 10 Slides](../../slides/week10.html)]

Density
: The fraction of possible edges that are present in a graph, that is, the number of edges present divided by the total number of possible edges. [Source: [Week 12 Slides](../../slides/week12.html)]

Descriptive statistics
: Statistics that summarize real data (e.g. through measures of center, spread, and position)

[Designed data]{#designed-data}
: Data collected for your question, e.g. through surveys, sensors, experiments, or instruments you control. Contrast with [found data](#found-data). [Source: [Week 2 Slides](../../slides/week2.html)]

DIKW pyramid
: The data-information-knowledge-wisdom hierarchy, which stacks data, information, knowledge, and wisdom as successive layers. See @fig-dikw-pyramid. [Source: @rowley_wisdom_2007]

[Directed graph]{#directed-graph}
: A graph in which each edge has a direction, $u \to v$. @leskovec_social_network_graphs_2020 call directed edges "arcs": "A directed graph has a set of nodes and a set of arcs; the latter is a pair of nodes written $u \to v$." See also [in-degree](#in-degree) and [out-degree](#out-degree). [Source: @leskovec_social_network_graphs_2020, sec. 10.8.1]

Directionality
: Relevant when determining which of two correlated things is the cause and which is the effect, e.g. train's speed and its speedometer needle. See @sec-statistical-worldviews. [Source: @sep-causation-regularity]

Disparate impact
: TK [@barocas_selbst_big_data_disparate_impact_2016]

Documentation debt
: TK

Edge
: A connection joining two nodes in a [graph](#graph).

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

Event
: A subset of the sample space $S$, i.e. a set of one or more outcomes we care about, e.g. heads on the first of 14 coin flips. 

Experiment
: A procedure or process with more than one possible outcome.

Final cause
: TK — a thing's purpose or end, what it is good for. One of [Aristotle's four causes](#four-causes). [Source: @sep-aristotle-causality]

Formal cause
: TK — a thing's real-world essence. E.g. for a bronze statue, the actual shape of the bronze. One of [Aristotle's four causes](#four-causes). [Source: @sep-aristotle-causality]

[Found data]{#found-data}
: Data that someone else collected, such as logs, scrapes, or administrative records. Found data are cheap, but they may answer a different question. Contrast with [designed data](#designed-data).

Goodhart's Law
: The notion that a measure can stop being a helpful measure when it becomes a target. E.g. see @sec-college-rankings: acceptance rates, student-teacher ratios, and reported SAT scores can all be moved directly once they are ranked on (but may or may not improve the actual school quality). See @sec-goodharts-law. [Source: @goodhart1984problems]

Granularity
: What each record in a dataset represents, e.g. one tap-in, one station-day, or one line-month. @lau_learning_2023 "use the term granularity to describe what each row in the table represents." Two tables need the same granularity before they can be merged. [Source: @lau_learning_2023, sec. 8.6; [Week 3 Slides](../../slides/week3.html)]

[Graph]{#graph}
: A set of nodes (vertices) $V$ and a set of edges $E$, each edge joining two nodes, written $G = (V, E)$.

Ground truth
: The correct label for each observation, recorded by someone who checked, e.g. the species recorded for each penguin at Palmer Station.

[Hierarchical clustering]{#hierarchical-clustering}
: Clustering that finds a set of nested clusters, which can be drawn as a tree (a [dendrogram](#dendrogram)). Contrast with [partitional clustering](#partitional-clustering).

[In-degree]{#in-degree}
: In a [directed graph](#directed-graph), the number of edges pointing into a node.

Inferential statistics
: Statistics that use a sample to conclude something about the population it was drawn from, e.g. through hypothesis testing and confidence intervals.

Information
: TK

Intercept
: In simple linear regression, $\hat{y} = \theta_0 + \theta_1 x$, the intercept $\theta_0$ is the predicted value of $y$ when $x$ is zero.

[Jaccard similarity]{#jaccard}
: A similarity score for binary features: $\frac{N_{11}}{N_{01} + N_{10} + N_{11}}$, where $N_{11}$ counts attributes where both $a$ and $b$ are 1 and $N_{10}$, $N_{01}$ count the attributes where they disagree. Attributes where both are 0 ($N_{00}$) do not count. Compare the [simple matching coefficient](#smc). 

Knowledge
: TK

[Long format]{#long-format}
: A table layout with one row per measurement, using key and value columns (e.g. `id`, `year`, `value`). In Polars, `df.unpivot()` turns [wide format](#wide-format) into long format.

Material cause
: What a thing is made of. E.g. for a bronze statue, the bronze. One of [Aristotle's four causes](#four-causes). [Source: @sep-aristotle-causality]

Multimodal
: Describes a distribution with multiple modes (peaks).

Multiple necessary conditions
: Describes when several conditions are required for a given outcome (which one counts as "the" cause?). E.g. a fire needs heat, fuel, and oxygen.

Mutual knowledge
: A proposition is mutual knowledge among people when each person knows that proposition. Often conflated with common knowledge. [Source: @sep-common-knowledge]

[Neighborhood of radius $d$]{#neighborhood}
: "The neighborhood of radius $d$ for a node $v$ in a directed or undirected graph is the set of nodes reachable from $v$ along paths of length at most $d$." [Source: @leskovec_social_network_graphs_2020, sec. 10.9]

Node
: One of the entities in a [graph](#graph), also called a vertex.

Null hypothesis ($H_0$)
: The hypothesis assumed true unless the evidence says otherwise.

[Out-degree]{#out-degree}
: In a [directed graph](#directed-graph), the number of edges pointing out of a node.

Outcome
: A single possible result of an experiment.


Overdetermination
: Describes situations in which two sufficient causes may occur at once, e.g. two people each empty a full bucket of water onto a campfire.

[Overlapping communities]{#overlapping-communities}
: Communities that share members. In social networks, "Typically, individuals are members of several communities." Some community detection algorithms (e.g. the Louvain algorithm) still put each node in exactly one community. [Source: @leskovec_social_network_graphs_2020, sec. 10.9)]

$p$-value
: The probability of seeing evidence at least as extreme as the observed evidence, if the null hypothesis $H_0$ were true. A result is often considered "statistically significant" when its $p$-value falls below the significance level $\alpha$.

[Partitional clustering]{#partitional-clustering}
: Clustering that divides the observations into one flat set of non-overlapping clusters, as k-means does. Contrast with [hierarchical clustering](#hierarchical-clustering).

Pasteur's quadrant
: Donald Stokes's 2×2 grid that classifies research by two questions: is it a quest for fundamental understanding, and does it consider use? Pasteur's quadrant (yes to both) is use-inspired basic research; Bohr's quadrant is pure basic research, and Edison's is pure applied research.

Percentile
: One of 100 equal divisions of a dataset; i.e. $n$% of the data is at or below the $n$th percentile.

Population
: The entire group that a statistical sample is drawn from and used to make inferences about. See also [target population](#target-population).

[Precision]{#precision}
: The fraction of positive predictions that are correct: $\frac{TP}{TP + FP}$.

[Predictor variable]{#predictor-variable}
: The variable used to predict the [response](#response-variable) in a regression, also called the explanatory variable. @lau_learning_2023 recommend avoiding the independent/dependent names, noting that many such name pairs "connote a causal relationship." [Source: @lau_learning_2023, sec. 15.1]

Presupposition
: A background claim that must be true in order for a question to have a meaningful answer. [Source: @sep-questions]

Provenance
: Tracing data through the lifecycle, back to where each value came from. See "Licensing and provenance" in [Chapter 3](03-ethics-in-obtaining-data.md). [Source:  @buneman_why_and_where_2001]

Proxy
: TK [@barocas_selbst_big_data_disparate_impact_2016]

Quartile
: One of four equal divisions of a dataset — $Q_1$ (25th percentile), $Q_2$ (50th, the median), and $Q_3$ (75th percentile).


Reachable
: "A node $v$ can reach node $u$ if $u$ is in the neighborhood of $v$ for some radius." See [transitive closure](#transitive-closure). [Source: @leskovec_social_network_graphs_2020, sec. 10.9]

[Recall]{#recall}
: The fraction of positive observations that are classified correctly: $\frac{TP}{TP + FN}$. Also called sensitivity or the true positive rate.

[Response variable]{#response-variable}
: The variable being modeled or predicted in a regression, also called the outcome. See [predictor variable](#predictor-variable).

[Sample]{#sample}
: The actual data at hand, as opposed to the population it is drawn from. @lau_learning_2023 define it as "the subset of units taken from the access frame to observe and measure." [Source: @lau_learning_2023, sec. 2.2]

Sample space
: The set of all possible outcomes of an experiment. (TODO - add garden of forking data explanation)

[Sampling gap]{#sampling-gap}
: The part of the [access frame](#access-frame) that could be reached but was not measured. See also [coverage gap](#coverage-gap).

[Self-loop]{#self-loop}
: An edge from a node to itself. A self-loop adds 2 to its node's degree.

Sensitive information
: TK [@nissenbaum_privacy_contextual_integrity_2004]

[Separation]{#separation}
: How distinct a cluster is from other clusters.

Significance level ($\alpha$)
: The threshold, typically 0.05, below which a p-value is considered statistically significant.

[Simple matching coefficient (SMC)]{#smc}
: A similarity score for binary features that counts agreements of both kinds: $\frac{N_{00} + N_{11}}{N_{00} + N_{01} + N_{10} + N_{11}}$. Compare [Jaccard similarity](#jaccard), which leaves out $N_{00}$.

Situated knowledge
: TK [@dignazio_klein_data_feminism_2020]

Skewed
: Describes a distribution where one tail is longer than the other (right-skewed or left-skewed).

Slope
: In simple linear regression, $\hat{y} = \theta_0 + \theta_1 x$, the slope $\theta_1$ is how much the predicted value of $y$ changes for every one-unit increase in $x$.

Specificity
: The fraction of negative observations classified correctly: $\frac{TN}{TN + FP}$. Also called the true negative rate.

Spurious regularities
: Used to describe when things consistently occur together without one causing the other, e.g. rooster crows every morning before sunrise. See @sec-statistical-worldviews. [Source: @sep-causation-regularity]


Statistically significant
: Describes a result whose p-value falls below the significance level.

Statistics
: Learning from data under uncertainty. (TODO- cross-reference)

[Supervised learning]{#supervised-learning}
: Predicting the value of a particular variable (the target) based on the values of other variables. Contrast with [unsupervised learning](#unsupervised-learning).

Symmetric
: Describes a distribution that looks the same on the left and right sides.

[Target population]{#target-population}
: "the collection of elements comprising the population that you ultimately intend to describe and draw conclusions about." See also [access frame](#access-frame) and [sample](#sample). [Source: @lau_learning_2023, sec. 2.2]

Tech Debt
: TK

Teleology
: Explanation of something based on its end or purpose, not what came before it to "cause" it. "Nature is a cause, a cause that operates for a purpose" [@aristotle_physics, *Physics* II.8, 199b]. Rosenblueth, Wiener, and Bigelow - what does a model or metric "aim" at [@rosenblueth_wiener_bigelow_teleology_1943]. TK — connect to @sec-goodharts-law.

[Telos]{#telos}
: The "end," "goal," or "completion" toward which a thing is directed (root of *teleology*). Another name for the "final cause," the fourth of [Aristotle's four causes](#four-causes): "in the sense of end or 'that for the sake of which' a thing is done, e.g. health is the cause of walking about" [@aristotle_physics, *Physics* II.3, 194b].

Testing set
: Labeled observations held back from training and used only to measure how well a model predicts new data. See also [training set](#training-set).

Tidy data
: Data arranged so that "1. Each variable forms a column. 2. Each observation forms a row. 3. Each type of observational unit forms a table." [Source: @wickham_tidy_data_2014]

[Training set]{#training-set}
: Labeled observations that a model learns from. [Source: [Week 8 Slides](../../slides/week8.html)]

[Transitive closure]{#transitive-closure}
: "The transitive closure of a graph is the set of pairs of nodes $(v, u)$ such that $v$ can reach $u$." It "can have a number of facts equal to the square of the number of nodes of a graph." [Source: @leskovec_social_network_graphs_2020, sec. 10.9]

Triadic closure
: The tendency for two nodes that share a neighbor to gain an edge between them, e.g. two people with a mutual friend becoming friends. [Source: @leskovec_social_network_graphs_2020, sec. 10.1.1]

Type I error
: Rejecting $H_0$ when it is true: a false positive, with probability $\alpha$. E.g. calling a fair coin biased, or thinking there is a wolf when there's actually no wolf.

Type II error
: Failing to reject $H_0$ when it is false: a false negative, with probability $\beta$. E.g. missing a coin that is biased, or thinking there is no wolf when there actually is a wolf. 

Unimodal
: Describes a distribution with a single mode (peak).

[Unsupervised learning]{#unsupervised-learning}
: Learning that aims to identify patterns and relationships in data, with no target variable and no explicit feedback about whether outputs are correct. [Cluster analysis](#cluster-analysis) is one example.

Weighted graph
: A [graph](#graph) in which each edge carries a number.

[Wide format]{#wide-format}
: A table layout that spreads repeated measurements across columns, e.g. one column per year. In Polars, `df.pivot()` turns [long format](#long-format) into wide format.

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
