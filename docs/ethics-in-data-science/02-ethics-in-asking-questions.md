# Ethics in Asking Questions

**[← Back to Course Homepage](../../index.html)**

::: {#fig-ds-lifecycle-ask-question}
<img src="../../assets/lifecycle/ds-lifecycle-v1.svg" alt="The data science lifecycle with Ask a question highlighted." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Asking a question, in the context of the data science lifecycle.
:::

> "There are naïve questions, tedious questions, ill-phrased questions, questions put after inadequate self-criticism. But every question is a cry to understand the world."

-- Carl Sagan in *The Demon-Haunted World* [@sagan_demon-haunted_1995, p. 303]

> "The 'technique,' or treatment, of a problem begins with its first expression as a question. The way a question is asked limits and disposes the ways in which any answer to it — right or wrong — may be given."

-- Susanne Langer in *Philosophy in a New Key* [@langer_philosophy_1942]

🟡 *Chapter Status: early working draft. Most sections drafted, some parts still need polish and/or filling in..*


You may have heard that you should "never ask a woman her age, or a man his salary..." The idea has become a [meme template](https://knowyourmeme.com/memes/all-three-are-going-to-lie-to-you-never-ask-a-woman-her-age) for identifying questions that should (or should not) be posed to certain people.

The basic principle underlying this meme template is that some questions are more appropriate than others. Put another way, questions have varying levels of "appropriateness," and it is worthwhile to consider the appropriateness of a question when working through the data science lifecycle.

In the context of education we appreciate all questions. The only bad question, as the teacher's saying goes, is the question you do not ask. And yet, some questions certainly seem more responsible, worthwhile, and/or appropriate than other questions. We might refer to this as the *Quality* of a question, or how good of a question it is.

To make this more concrete, consider a pair of example questions from *The Craft of Research* [@booth_craft_of_research_2024]:
* "Are there ultimate particles?"
* "Was Abraham Lincoln's right thumb longer than his nose?"

Which of these questions is better than the other? How do we know?

This particular example from @booth_craft_of_research_2024 is meant to illustrate the importance of problems entailed by questions. That is, answering a good question will solve a problem, whereas a good question unanswered leaves a problem unsolved.

If we cannot answer whether Lincoln's right thumb was longer than his nose, we may be slightly less-equipped for trivia night, but there is no open problem from having no answer^[Out of curiosity, I typed this question into Google in August 2026. Google's AI summary responded "No, Abraham Lincoln's right thumb was not longer than his nose," claiming his nose was 2.25 inches and his thumb was 2 inches. Of course, it also added "AI can make mistakes, so double-check responses."] to the question.

On the other hand, if we cannot answer whether ultimate particles exist, we lack some fundamental knowledge about reality. In this example, the question about ultimate particles is the better, higher-Quality question. Good questions present a corresponding problem, such that answering the question solves that problem .

What else helps us know which questions are high-Quality? How do we go about identifying "good" or "better" questions?

This chapter responds to those questions, in part by drawing on the work of philosophers who have studied questions in considerable depth [@sep-questions], including their origins, structures, categories, pitfalls, and more. It will also survey common pitfalls of questions in the data science lifecycle, as identified by related texts.

Although a question can make or break the data science lifecycle, there is no requirement or expectation to ask a perfect question at the very beginning a project. The "Ask a question" step of the lifecycle actually includes four arrows pointing to it, because other steps in the lifecycle often lead back to revising and improving the original questions.

You can always go back and refine your question, however, you do have to start somewhere.


## Where Questions Come From

The data science lifecycle which this book adapts from @lau_learning_2023 suggests "ask a question" as one of two possible starting points in the lifecycle (the other being "obtain data"). In *Doing Data Science*, O'Neil and Schutt note the data science lifecycle can be thought of "as an extension or variation of the scientific method," a method which begins with "ask a question" [@oneil_2013_doing]. O'Neil and Schutt also suggest that this initial question is often connected to identifying some kind of problem, similar to Susanne Langer's observation quoted at the beginning of this chapter: "The way a question is asked limits and disposes the ways in which any answer to it... may be given." *The Craft of Research* [@booth_craft_of_research_2024] makes similar observations: your question(s) will shape your answer(s).

The data science lifecycle may start with asking a question, but not every question makes it through the full lifecycle. If you ask the score of a tennis match, or the current time, or the temperature outside, or someone's name, you will probably not work through the lifecycle as exhaustively as you would when answering other questions (e.g. how does the weather influence voter turnout).

as data scientists learn from experience, there are various checks, heuristics, and conventions that can help identify the kinds of questions which make for good data science work.

Still, when you *only* have the question, it can be difficult to know whether the question is well-suited for the data science lifecycle. That is one reason why the "Ask a question" step of the lifecycle includes *four* arrows pointing to it: other steps in the lifecycle can often lead data scientists back to revise their question(s) and restart the process anew.

In *The Craft of Research*, Booth and colleagues observe that research usually does not begin with a big question that attracts everyone in a field, but with a "mental itch" about a small question that only a single researcher wants to scratch [@booth_craft_of_research_2024].

Topic vs. question:

* a topic only becomes research when it provokes a specific question
* what is lost if a question goes unanswered — the "so what?" test [@booth_craft_of_research_2024]


## Basic Types of Questions

One part of identifying high-Quality questions is identifying what *type* of question you have. The Stanford Encyclopedia of Philosophy [@sep-questions] offers a helpful taxonomy, dividing questions into several main types: "whether," "which," and "why" questions, as well as indirect or "embedded" questions, as summarized in the following table.

| Question Type | Description | Example | Answers |
| --- | --- | --- | --- |
| "Whether" | Presents a finite number of direct answers. May be yes-or-no questions, or "multiple choice" questions that name a finite number of possible direct answers. | Was there a quorum at the meeting? | a. There was a quorum at the meeting.<br>b. There was no quorum at the meeting. |
|  |  | Does Alice live in Chicago, in New York City, or in Los Angeles? | a. Alice lives in Chicago.<br>b. Alice lives in New York City.<br>c. Alice lives in Los Angeles. |
| "Which" | Seeks a specific person, thing, or value. May have an indefinite *or infinite* number of possible direct answers. | Who was the President of the USA in 1978? | a. Jimmy Carter<br>b. Gerald Ford  |
|  |  | What is the smallest prime number greater than 12? | a. 13 is the smallest prime number greater than 12. |
|  |  | Who was elected Pope in 2013? | a. Cardinal Angelo Scola<br>b. Cardinal Odilo Scherer<br>c. Jorge Mario Bergoglio |
| "Why" | Asks for an explanation (not just a fact). Closely tied to causal, data-informed, or interpretive explanation. | Why do the planets move in elliptical orbits with the sun at one focus? | a. The gravitational pull of the sun causes the planets to move in elliptical orbits. |
| "How" | Usually can be rephrased to one of the above types, using a paraphrase test: if "how" can be reworded as "in what way," it is an explanation-seeking question (a "why" question that asks for a *way* rather than a *reason*). Otherwise it asks for a value, and is a "which" question. | How does screen time influence mental health? ("in what way" — explanation-seeking) | a. Screen time may displace sleep, and sleep loss may worsen mood.<br>b. Screen time may reduce in-person contact, which may influence mental health.<br>c. Screen time may influence mental health through a combination of factors.<br>d. Screen time may have no influence on mental health. |
|  |  | How far is it from Chicago to Cleveland? (asks for a distance) | a. It is approximately 350 miles from Chicago to Cleveland. |
| Indirect ("Embedded") | Comes from embedded predicates, such as `know` or `wonder`. Indirect questions are inferred from larger statements. | Bob knows who spoke to Mary. | a. Carol spoke to Mary.<br>b. Dave spoke to Mary. |
|  |  | Alice wonders whether there was a quorum at the meeting. | a. There was a quorum at the meeting.<br>b. There was no quorum at the meeting. |
|  |  | The analyst discovered which neighborhoods were undercounted. | a. Humboldt Park was undercounted.<br>b. Bridgeport was undercounted.<br>... |

(TODO explain/define Answer space)

"How" questions deserve a note, because they do not necessarily get their own category. While many "how" questions can be rephrased as "in what way" questions (i.e. explanation-seeking, why questions) Charles B. Cross [@cross_explanation_questions_1991, p. 248] observed that not *every* how-question requests an explanation. For example, "How far is it to Cleveland?" asks for a distance, not an explanation.

Similarly, "how many households were undercounted?" is a actually a "which" question, since it seeks a value. But "how does screen time influence mental health?" can be rephrased as, "in what way does screen time influence mental health?"), which makes it an explanation-seeking question: a "why" question.

Cross also notes that the "ways" a how-question can request come in a variety of kinds, such that a how-question "could safely be rephrased in some such way as" the following [@cross_explanation_questions_1991, pp. 248-249]:

1. By what road (How did you get here?)
2. In what manner (How did you behave at the party?)
3. By what argument (How will you justify this?)
4. By what method (How do you perform an appendectomy?)
5. By what means (How did you get that money?)
6. In what respect (How do these differ?)
7. By what process (How do DNA molecules replicate?)

In short, a "why" question asks for a reason or explanation, such that its answers are worded with "because", whereas a "how" question can be answered with "by" or "in this way." Cross argues that this difference in wording is the only real difference, and that how- and why-questions are both explanatory questions.

Indirect questions are not explicitly asked the way that "whether," "which," or "why" questions are asked. Rather, they come from sentences with incomplete or implied information. This is why the "Answers" column above lists answers to the *embedded* question, i.e. the answer that Bob knows or that Alice wonders about.

Indirect questions also depend on who posed them - they are subjective. For instance, in the "Bob knows who spoke to Mary" example, Bob does not have a question. And Bob might not be the only person with knowledge about who spoke to Mary. Thus, when asking or addressing indirect questions, it is important to consider who knows certain facts, as well as *what others know* about who knows certain facts. Further discussion of this phenomena, **common knowledge**, is in chapter X.

### Presuppositions

To assess the Quality of different questions, it is also helpful to recognize presuppositions. A *presupposition* can be defined as a background claim that must be true in order for the question to have a meaningful or correct answer. If someone denies that background claim (i.e. the presupposition), they are correcting the question itself, and it may not be possible to answer the original question.

As an introductory example, consider the question "Who was the the Roman emperor in 2020?" It presupposes that the Roman Empire was active in 2020, and that an emperor was in place. Neither presupposition is true, so the question has no meaningful answer.

Below are some examples of presuppositions associated with example questions, drawn from the Stanford Encyclopedia of Philosophy [@sep-questions].

| Question | Answer(s) | Presupposition(s) |
| --- | --- | --- |
| Who was the President of the USA in 1978? | a. Jimmy Carter<br>b. Gerald Ford | The USA had exactly one President in 1978. |
| Was there a quorum at the meeting? | a. There was a quorum at the meeting.<br>b. There was no quorum at the meeting. | The meeting occurred. |
| Does Alice live in Chicago, in New York City, or in Los Angeles? | a. Alice lives in Chicago.<br>b. Alice lives in New York City.<br>c. Alice lives in Los Angeles. | The question presupposes that Alice lives in one of the listed places. A corrective answer could reject that assumption, perhaps suggesting that Alice lived somewhere else, or in multiple cities. |
| Which cardinal was elected Pope in 2013? | a. Cardinal Angelo Scola<br>b. Cardinal Odilo Scherer<br>c. Jorge Mario Bergoglio | Someone was elected Pope in 2013. |
| Why do the planets move in elliptical orbits with the sun at one focus? | a. The gravitational pull of the sun causes the planets to move in elliptical orbits. | The planets do move in elliptical orbits with the sun at one focus. |

#### Contrast classes

Explanatory questions ("why" and "how") also carry a second presupposition which is sometimes referred to as a *contrast class*, or the set of alternatives the question is implicitly comparing against. Cross [@cross_explanation_questions_1991] explains that the contrast class can be presupposed in two different ways:

* **Only a single topic is true.** "How do DNA molecules (in contrast to benzene and hexane) replicate?" Benzene and hexane do not replicate at all, so a good answer will highlight the qualities DNA has, which benzene and hexane lack. Only DNA replicates.
* **Every member of the class is true.** "How do reptiles (in contrast to mammals and birds) reproduce?" All three reproduce, so a good answer will explain how reptile reproduction *differs* from the others. The question could be reworded: "I know how mammals and birds reproduce, but how do reptiles reproduce?"

Returning to the question, "how does screen time influence mental health?" An explicit contrast class would add "compared to what" — no screen time at all? Compared to how *sleep* influences mental health? Compared to how screen time influences health in general? Each contrast class implies a different comparison group, a different study design, and a different dataset. 

The distinction can help data scientists improve the clarity of their research question because... TK


## Common Pitfalls

A data scientist who can recognize what type of question they are working with, as well as the presuppositions of that question, is well on their way to doing good work. In addition to the common types of questions (whether, which, why, indirect), there are common pitfalls in questions which can serve as heuristics for identifying high-Quality questions. These common pitfalls (naïve, ill-phrased, leading, tedious, invasive, etc.) are described here, drawing on the epigraph quote from Carl Sagan.

A **naïve** question...

A **tedious** question...

An **ill-phrased** question...

A **leading** question...

An **invasive** question...

### Naïve questions

* naïve about a particular context/setting
* can reveal assumptions that "experts" have stopped considering
* protect the "cry to understand" by improving the question
	* increase specificity
	* incorporate established knowledge
* e.g. "Which NBA players are the best scorers?" — arguably naïve about the domain, like possession-level context, true shooting percentage, measures of efficiency beyond raw points per game
	* https://pudding.cool/2026/06/ethical-champions/

### Ill-phrased questions

* terms, scope, or possible answers unclear.
* may include a loaded presupposition or judgment (e.g. "Why did the new policy fail?")
* "Are students doing better this year?" - which students, compared with when, and according to which measure of "better."
* e.g. "Is our museum's collection diverse?" — diverse in artist nationality, gender, medium, era? measured by number of works held, or by wall space actually on view?
* e.g. "How did the wildfire affect air quality?" — over what radius, what averaging window, and against which baseline season?
* e.g. "Is news coverage biased?" — bias in story selection, in sourcing, word choice, topic coverage, etc.

### Leading questions

* usually implies a preferred answer
	* e.g. "everything tasting good over here?"
	* e.g. "How much did the tutoring program raise test scores?" — presupposes it raised them
* e.g. "Do voters prefer the status quo of rising costs?"
* i.e. ad-hoc support of suspect decision-making
* ask before answering
* might actually be good to be more naïve
	* ask as if you knew less

### Tedious questions

* effort required to answer a question may be disproportional to what the answer would teach us.
* measurable details are not always meaningful
* triangle/pixel example from first chapter
* e.g. counting how many times each city council member says the word "budget," ignoring how they voted

### Questions with settled answers

* questions that have already been answered "well enough" [@booth_craft_of_research_2024]
* distinct from *replication*, where re-asking a settled question is the point
* worth asking anyway when the "settled" answer rests on data or assumptions that have since changed
* More TK

### Questions with speculative answers

* no evidence could realistically settle the question
* i.e. any answer stays a matter of opinion
* often signaled by counterfactuals far outside the data (e.g. "what would this city look like if the highway had never been built?")
* speculations versus findings 
* e.g. "Would the 2000 presidential election have gone differently with social media?" — no control world, no way to intervene
* e.g. "Which students would have succeeded if they'd chosen a different major?" — the counterfactual student is unobservable
* More TK

### Questions whose answers would be dead ends

* answerable, but the answer leads nowhere
* fails the "so what?" test described earlier [@booth_craft_of_research_2024]
* related to tedious questions, but the problem is more about the destination
* e.g. "How many of the city's bus stops face north?" — answerable and precise. But not connected to real decisions
* e.g. "Do students with longer last names take longer to finish homework?" - what would follow?
* e.g. "which jersey number has scored the most points?" - answerable and precise, but nothing to act on
* More TK

### Invasive questions

If a potential employer were to ask my weight during a job interview, it would be inappropriate. However, when I visit the Department of Motor Vehicles (DMV) to obtain my driver's license, I am required to provide an answer. I have consented to the requirements of the system if I wish to obtain their permission to drive cars in the state (i.e. to get my driver's license).

* asks for information whose sensitivity exceeds the purpose of the interaction.
* can become coercive
	* e.g. when people must answer to access grades, employment, housing, healthcare, public services, etc.
* e.g. "What medications are you taking?" may be appropriate in a medical intake, but not in a classroom survey.
* e.g. a transit fare app collecting continuous location history
* try to ask for the least sensitive data that can address the question
* more in obtaining data

## Temporality in questions

* categories: descriptive, predictive, counterfactual [@hernan_chance_2019]
* self-reinforcing feedback loops [@oneil_weapons_2017]
* embedded values in optimization targets [@eubanks_automating_2018]
* example - "behavioral futures markets" sold to third parties [@zuboff_surveillance_2019]
* More TK

## Framing and rhetoric

TK

* More notes on "objective" analysis as rhetorical/persuasive
* questions embed values/narratives [@mccloskey_rhetoric_of_economics_1998].
* good to assume you might've missed something
* data hubris

### Ethos, pathos, logos

* More TK

### The rhetoric of "just asking questions"

* More TK

## Questions for your questions

* Who asked this question?
	* What are their goals?
	* What are their incentives?
* Who else may have already asked this question?
	* Have they shared results anywhere?
* Are there existing data to address this question?
* What assumptions does the question make before any data are collected?
* Who might be harmed if this question is answered poorly?
* What kind of answer would actually change a decision?
* Could a less invasive or more precise question serve the same purpose?
* What can and cannot (should/should not) be predicted?
* Whose perspective(s) may be missing?
* Booth's "so what" section
	* What would be lost if this question is not answered?
	* Why would others think this question is worth asking?


## This is actually the hard part

> "In my opinion, the social sciences are the hard sciences."

-- Michael Shermer in *The Mind of the Market* [@shermer_mind_market_2008]

Crafting a high-quality research question for the data science lifecycle can be unexpectedly difficult and time-consuming. There is a delicate balance to high-Quality questions which are specific enough to be meaningfully answerable in a limited amount of time, yet general enough to be useful and interesting to a given audience.

* specificity


# Conclusion

* know what kind of question you are asking
* state questions early
* revise and clarify questions often
	* get specific about metrics

Test citations for question framing, rhetoric, and situated perspectives: the Stanford Encyclopedia overview of questions [@sep-questions] and *Data Feminism for Data Visualization* [@klein_dignazio_data_feminism_visualization].


::: {.content-visible when-format="html"}
## References
:::
