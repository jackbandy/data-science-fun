# Preface {.unnumbered}

**[← Back to Course Homepage](../../index.html)**

*This mini-book is a work-in-progress.*

::: {#fig-ds-lifecycle}
<img src="../../assets/lifecycle/ds-lifecycle-v0.svg" alt="The full data science lifecycle." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

A rendition of the data science lifecycle, slightly modified from [*Learning Data Science*](https://learningds.org/ch/01/lifecycle_cycle.html).
:::

How can data be collected responsibly? Which data are considered private or sensitive? What makes some questions inappropriate? When and how can data be published? How does one responsibly handle the persuasive power of data?

The purpose of this mini-book is to introduce data scientists to ethical considerations that arise throughout the data science lifecycle. There are many versions of the lifecycle, and this book is organized around the one described in *Learning Data Science*, which divides data work into four broad stages [@lau_learning_2023].

Broadly, the lifecycle stages correspond to the chapters in this book, with three exceptions: first, I have added a framing chapter, and second, there is an "extra" chapter since @lau_learning_2023 does not include a dedicated chapter about reporting, decision-making, and problem-solving. The third exception is that I have written a combined chapter about "understanding the data" and "understanding the world," rather than separating them. Many of the ethical considerations related to these two steps have to do with differences between "understanding the data" and "understanding the world," so I have written about them in the same chapter.

Thus, the correspondence between @lau_learning_2023 and this book is as follows:

::: {tbl-colwidths="[55,45]"}
| *Learning Data Science* | Corresponding material in this book |
| --- | --- |
|  | Introduction (this chapter) |
|  | [1 Working Toward Wisdom](01-working-toward-wisdom.md) |
| [Ask a Question](https://learningds.org/ch/01/lifecycle_cycle.html) | [2 Ethics in Asking Questions](02-ethics-in-asking-questions.md) |
| [Obtain Data](https://learningds.org/ch/01/lifecycle_cycle.html) | [3 Ethics in Obtaining Data](03-ethics-in-obtaining-data.md) |
| [Understand the Data](https://learningds.org/ch/01/lifecycle_cycle.html) | [4 Ethics in Understanding](04-ethics-in-understanding.md) |
| [Understand the World](https://learningds.org/ch/01/lifecycle_cycle.html) | [4 Ethics in Understanding](04-ethics-in-understanding.md) |
| Reports, decisions, solutions| [5 Ethics in Reporting, Decision-Making, and Problem-Solving](05-ethics-in-reporting-decisions-solutions.md) |
|  | [6 Conclusion](06-conclusions.md) |
:::


When relevant, I have also written some sections to align with some of the ACM Data Science Task Force's "Competencies for Data Science," including the 2021 release as well as the 2026 work-in-progress [@acm_dstf_ccdsc_2021]. Here are a few samples of mapping from this book to the ACM competency areas:

::: {tbl-colwidths="[55,45]"}
| ACM competency area | Supporting material in this book |
| --- | --- |
| **Data Acquisition (DA).** A graduate can "proactively collect, integrate, and manage data from diverse sources while ensuring data quality, provenance, privacy, and regulatory compliance." | [3.1 Where do data come from?](03-ethics-in-obtaining-data.md#where-do-data-come-from)<br>[3.4 What "obtaining data" includes](03-ethics-in-obtaining-data.md#what-obtaining-data-includes)<br>[3.7 Maintaining Data](03-ethics-in-obtaining-data.md#maintaining-data)<br>[3.8 Example: How the Census Obtains Data](03-ethics-in-obtaining-data.md#example-how-the-census-obtains-data) |
| **Professionalism and Ethics (PE) — Data Stewardship.** A graduate can "diagnose stewardship risks (e.g., leakage, improper access) in real DS workflows and propose mitigations based on evidence." | [3.5.1 Defining Sensitive Information](03-ethics-in-obtaining-data.md#defining-sensitive-information)<br>[3.5.2 Handling Sensitive Information](03-ethics-in-obtaining-data.md#handling-sensitive-information)<br>[3.6 Risks from data triangulation](03-ethics-in-obtaining-data.md#risks-from-data-triangulation)<br>[3.9 Example: Facebook Profile](03-ethics-in-obtaining-data.md#example-facebook-profile) |
| **Research Methods and Experimental Design (RM).** A graduate can "design, conduct, document, and evaluate ethical and reproducible empirical investigations by formulating testable hypotheses." | [2.1 Where Questions Come From](02-ethics-in-asking-questions.md#where-questions-come-from)<br>[2.2.1 Presuppositions](02-ethics-in-asking-questions.md#presuppositions)<br>[2.6 Questions for your questions](02-ethics-in-asking-questions.md#questions-for-your-questions)<br>[5.4.5 Researcher Degrees of Freedom](05-ethics-in-reporting-decisions-solutions.md#researcher-degrees-of-freedom) |
| **Exploratory Data Analysis (EDA).** A graduate can "analyze and evaluate complex datasets... to identify patterns, anomalies, and data quality issues, and can communicate findings responsibly and transparently." | [4.2.1 The Model is not the World](04-ethics-in-understanding.md#the-model-is-not-the-world)<br>[4.3.1 Understanding the data](04-ethics-in-understanding.md#understanding-the-data)<br>[4.3.1.1 Proxies](04-ethics-in-understanding.md#proxies)<br>[4.3.2 Understanding the world](04-ethics-in-understanding.md#understanding-the-world) |
| **Machine Learning (ML).** A graduate can "assess model performance, fairness, robustness, and interpretability" and "design scalable, ethical, and responsible machine learning solutions." | [4.1 Your Model is Always Wrong](04-ethics-in-understanding.md#your-model-is-always-wrong)<br>[4.2.2 Multiple Correct Models](04-ethics-in-understanding.md#multiple-correct-models)<br>[4.2.3 Patterns are not Laws](04-ethics-in-understanding.md#patterns-are-not-laws)<br>[4.3.5 Validity, overfitting, generalization](04-ethics-in-understanding.md#validity-overfitting-generalization) |
| **Data Storytelling (DS).** A graduate can "design, evaluate, and deliver clear, accurate, and ethically responsible data stories... tailored to diverse audiences and support informed decision-making." | [2.5 Framing and rhetoric](02-ethics-in-asking-questions.md#framing-and-rhetoric)<br>[4.3.3 Uncertainty](04-ethics-in-understanding.md#uncertainty)<br>[4.3.4 Explanation as persuasion](04-ethics-in-understanding.md#explanation-as-persuasion)<br>[5.4.1 Common Knowledge](05-ethics-in-reporting-decisions-solutions.md#common-knowledge)<br>[5.4.2 Audience](05-ethics-in-reporting-decisions-solutions.md#audience)<br>[5.4.3 Statistical arguments as rhetoric](05-ethics-in-reporting-decisions-solutions.md#statistical-arguments-as-rhetoric)<br>[5.4.4 Visual rhetoric](05-ethics-in-reporting-decisions-solutions.md#visual-rhetoric) |
| **Professionalism and Ethics (PE).** A graduate can "apply ethical reasoning, legal awareness, and professional standards to the responsible acquisition, analysis, deployment, and communication of data-driven solutions, demonstrating accountability, transparency, and respect for individuals, organizations, and society." | [1.1 What is wisdom?](01-working-toward-wisdom.md#what-is-wisdom)<br>[2.3.5 Invasive questions](02-ethics-in-asking-questions.md#invasive-questions)<br>[3.2 The rhetoric of "raw" data](03-ethics-in-obtaining-data.md#the-rhetoric-of-raw-data)<br>[5.1.3 Goodhart's Law](05-ethics-in-reporting-decisions-solutions.md#sec-goodharts-law)<br>[5.4.6 Retractions and Corrections](05-ethics-in-reporting-decisions-solutions.md#retractions-and-corrections)<br>[5.4.6.2 Standards](05-ethics-in-reporting-decisions-solutions.md#standards) |
:::

This is not the only book to include these topics and competencies, and it is definitely not the only book to discuss ethics in data science more broadly. Many of the topics discussed in the book have been described elsewhere, in books and articles and essays which often serve as source material. These sources include (but are not limited to):

* Alberto Cairo, *How Charts Lie* [@cairo_how_charts_lie_2019]
* Catherine D'Ignazio and Lauren Klein, *Data Feminism* [@dignazio_klein_data_feminism_2020]
	* Lauren Klein and Catherine D'Ignazio, *Data Feminism for Data Visualization* [@klein_dignazio_data_feminism_visualization]
* Solon Barocas and Andrew Selbst, "Big Data's Disparate Impact" [@barocas_selbst_big_data_disparate_impact_2016]
* Cathy O'Neil, *Weapons of Math Destruction* [@oneil_weapons_2017]
* Luciano Floridi and Mariarosaria Taddeo, "What is data ethics?" [@floridi_taddeo_what_is_data_ethics_2016]
* Benjamin S. Baumer, Daniel T. Kaplan, and Nicholas J. Horton, "Data science ethics" in *Modern Data Science with R* [@baumer_kaplan_horton_data_science_ethics_2021]
* Rachel Thomas, *Practical Data Ethics* [@thomas_practical_data_ethics_2020]


**Why not just read those?**

I recommend that you do read them! Still, what is intended to be distinctly useful about this book is its alignment with the "data science lifecycle" from *Learning Data Science* [@lau_learning_2023], as well as its alignment with ACM competencies. Especially when combined, the lifecycle model and the ACM competencies offer a helpful way to organize the wide array of topics and methods that arise in the vast body of activity we call data science work.

Before exploring ethical implications of these lifecycle stages and competencies through [Ethics in Asking Questions](02-ethics-in-asking-questions.md), [Ethics in Obtaining Data](03-ethics-in-obtaining-data.md), [Ethics in Understanding](04-ethics-in-understanding.md), and [Ethics in Reporting Decisions & Solutions](05-ethics-in-reporting-decisions-solutions.md), I have taken the liberty to include a framing chapter, [Working Toward Wisdom](01-working-toward-wisdom.md), which zooms out and considers a somewhat audacious question: why are we doing any of this at all?

## References
