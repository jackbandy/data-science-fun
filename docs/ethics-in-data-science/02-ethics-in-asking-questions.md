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


You may have heard that you should "never ask a woman her age, or a man his salary..." The idea has become a [meme template](https://knowyourmeme.com/memes/all-three-are-going-to-lie-to-you-never-ask-a-woman-her-age) for framing questions that should (or should not) be posed to certain people.

The basic principle underlying this meme is that some questions are more appropriate than others. Put another way, questions have varying levels of "appropriateness," and it is worthwhile to consider the quality and appropriateness of a question when working through the data science lifecycle.

In educational contexts, we appreciate all questions. The only bad question, as the saying goes, is the question you do not ask. And yet, as the aforementioned template suggests, some questions are more responsible, worthwhile, and/or appropriate than other questions. How might we distinguish these "good" or "better" questions?

As observed in *The Craft of Research*, good questions usually present a corresponding problem, such that answering the question solves that problem [@booth_craft_of_research_2024]. Generally, this chapter agrees, and it uses some modified examples from *The Craft of Research* to discuss the characteristics of high-quality (and low-quality) questions.

This chapter draws on the work of philosophers who have studied questions in considerable depth [@sep-questions], including their origins, structures, categories, pitfalls, and more.

Although a question can make or break the data science lifecycle, there is no requirement or expectation to ask a perfect question at the very beginning. The "Ask a question" step of the lifecycle includes four arrows pointing to it because other steps in the lifecycle often lead to revised and improved questions.

You can always go back and refine your question. Still, you have to start somewhere.


## Where Questions Come From

The data science lifecycle which this book adapts from @lau_learning_2023 suggests "ask a question" as one of two possible starting points in the lifecycle (the other being "obtain data"). In *Doing Data Science*, O'Neil and Schutt note the data science lifecycle can be thought of "as an extension or variation of the scientific method," a method which begins with "ask a question" [@oneil_2013_doing]. O'Neil and Schutt also suggest that this initial question is often connected to identifying some kind of problem, similar to Susanne Langer's observation quoted at the beginning of this chapter: "The way a question is asked limits and disposes the ways in which any answer to it... may be given." *The Craft of Research* [@booth_craft_of_research_2024] makes similar observations: your question(s) will shape your answer(s).

The data science lifecycle may start with asking a question, but not every question makes it through the full lifecycle. If you ask the score of a tennis match, or the current time, or the temperature outside, or someone's name, you will probably not proceed through the lifecycle as exhaustively as you would when answering other questions (e.g. how does the weather influence voter turnout).

So, how do we know when a question is well-suited for the data science lifecycle? On the one hand, you can never be certain when you only have the question. That is one reason why the "Ask a question" step of the lifecycle includes *four* arrows pointing to it: other steps in the lifecycle can often lead data scientists back to revise their original question and restart the process anew.

On the other had, as data scientists learn from experience, there are some checks, heuristics, and conventions that can help identify the kinds of questions which make for good data science work.

In *The Craft of Research*, Booth and colleagues observe that research usually begins not with a big question that attracts everyone in a field, but with a "mental itch" about a small question that only a single researcher wants to scratch [@booth_craft_of_research_2024].

Topic vs. question:

* a topic only becomes research when it provokes a specific question
* what is lost if a question goes unanswered — the "so what?" test [@booth_craft_of_research_2024]


## Basic Types of Questions

One part of identifying good questions is identifying what type of question you have. The Stanford Encyclopedia of Philosophy [@sep-questions] offers a helpful taxonomy, dividing questions into several main types: "whether," "which," and "why" questions, as well as indirect or "embedded" questions, as summarized in the following table.

| Question Type | Description | Example | Answers |
| --- | --- | --- | --- |
| "Whether" | Presents a finite number of direct answers. May be yes-or-no questions, or "multiple choice" questions that name a finite number of possible direct answers. | Was there a quorum at the meeting? | a. There was a quorum at the meeting.<br>b. There was no quorum at the meeting. |
|  |  | Does Alice live in Chicago, in New York City, or in Los Angeles? | a. Alice lives in Chicago.<br>b. Alice lives in New York City.<br>c. Alice lives in Los Angeles. |
| "Which" | Seeks a specific person, thing, or value. May have an indefinite, or infinite, number of possible direct answers. | Who was the President of the USA in 1978? | a. Jimmy Carter<br>b. Gerald Ford  |
|  |  | What is the smallest prime number greater than 12? | a. 13 is the smallest prime number greater than 12. |
|  |  | Who was elected Pope in 2013? | a. Cardinal Angelo Scola<br>b. Cardinal Odilo Scherer<br>c. Jorge Mario Bergoglio |
| "Why" | Asks for an explanation (not just a fact). Closely tied to causal, data-informed, or interpretive explanation. | Why do the planets move in elliptical orbits with the sun at one focus? | a. The gravitational pull of the sun causes the planets to move in elliptical orbits. |
| Indirect ("Embedded") | Comes from embedded predicates, such as `know` or `wonder`. Indirect questions are inferred from larger statements. | Bob knows who spoke to Mary. | a. Carol spoke to Mary.<br>b. Dave spoke to Mary. |
|  |  | Alice wonders whether there was a quorum at the meeting. | a. There was a quorum at the meeting.<br>b. There was no quorum at the meeting. |
|  |  | The analyst discovered which neighborhoods were undercounted. | a. Humboldt Park was undercounted.<br>b. Bridgeport was undercounted. |


Indirect questions are not explicitly asked the way that "whether," "which," or "why" questions are asked. Rather, they come from sentences with incomplete or implied information. The "Answers" column above lists answers to the *embedded* question — the answer that Bob knows, Alice wonders about, or the analyst discovered.

Indirect questions are also subjective. For instance, in the "Bob knows who spoke to Mary" example, Bob does not have a question. And Bob might not be the only person with knowledge about who spoke to Mary. Thus, when asking or addressing indirect questions, it is important to consider who knows certain facts, as well as *what others know* about who knows certain facts. Further discussion of this phenomena, common knowledge, is in chapter X.

### Presuppositions

To assess the quality of different questions, it is also helpful to recognize presuppositions. A *presupposition* can be defined as a background claim that must be true in order for the question to have a meaningful or correct answer. If someone denies that background claim (i.e. the presupposition), they are correcting the question itself, and it may not be possible to answer the original question.

As an introductory example, consider the question "Who was the the Roman emperor in 2020?" It presupposes that the Roman Empire was active in 2020, and that an emperor was in place. Neither presupposition is true, so the question has no meaningful answer.

Below are some examples of presuppositions associated with example questions, drawn from the Stanford Encyclopedia of Philosophy [@sep-questions].

| Question | Answer(s) | Presupposition(s) |
| --- | --- | --- |
| Who was the President of the USA in 1978? | a. Jimmy Carter<br>b. Gerald Ford | The USA had exactly one President in 1978. |
| Was there a quorum at the meeting? | a. There was a quorum at the meeting.<br>b. There was no quorum at the meeting. | The meeting occurred. |
| Does Alice live in Chicago, in New York City, or in Los Angeles? | a. Alice lives in Chicago.<br>b. Alice lives in New York City.<br>c. Alice lives in Los Angeles. | The question presupposes that Alice lives in one of the listed places. A corrective answer could reject that assumption, perhaps suggesting that Alice lived somewhere else, or in multiple cities. |
| Which cardinal was elected Pope in 2013? | a. Cardinal Angelo Scola<br>b. Cardinal Odilo Scherer<br>c. Jorge Mario Bergoglio | Someone was elected Pope in 2013. |
| Why do the planets move in elliptical orbits with the sun at one focus? | a. The gravitational pull of the sun causes the planets to move in elliptical orbits. | The planets do move in elliptical orbits with the sun at one focus. |


## Common Pitfalls

A data scientist who can recognize what type of question they are working with, as well as the presuppositions of that question, is well on their way to good work.

### Naïve questions

* naïve about a particular context/setting
* can reveal assumptions that "experts" have stopped considering
* protect the "cry to understand" by improving the question
	* increase specificity
	* incorporate established knowledge

### Ill-phrased questions

* terms, scope, or possible answers unclear.
* may include a loaded presupposition or judgment (e.g. "Why did the new policy fail?")
* "Are students doing better this year?" - which students, compared with when, and according to which measure of "better."

### Leading questions

* usually implies a preferred answer
	* e.g. "everything tasting good over here?"
	* e.g. TK
* i.e. ad-hoc support of suspect decision-making
* ask before answering
* might actually be good to be more naïve
	* ask as if you knew less

### Tedious questions

* effort required to answer a question may be disproportional to what the answer would teach us.
* measurable details are not always meaningful
* triangle/pixel example from first chapter

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
* More TK

### Questions whose answers would be dead ends

* answerable, but the answer leads nowhere
* fails the "so what?" test described earlier [@booth_craft_of_research_2024]
* related to tedious questions, but the problem is more about the destination
* More TK

### Invasive questions

If a potential employer were to ask my weight during a job interview, it would be inappropriate. However, when I visit the Department of Motor Vehicles (DMV) to obtain my driver's license, I am required to provide an answer. I have consented to the requirements of the system if I wish to obtain their permission to drive cars in the state (i.e. to get my driver's license).

* asks for information whose sensitivity exceeds the purpose of the interaction.
* can become coercive
	* e.g. when people must answer to access grades, employment, housing, healthcare, public services, etc.
* "What medications are you taking?" may be appropriate in a medical intake, but not in a classroom survey.
* try to ask for the least sensitive data that can address the question

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
	* What are their goals and incentives?
* Who else may have asked this question?
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

Crafting a high-quality research question for the data science lifecycle can be unexpectedly difficult and time-consuming.

* specificity


# Conclusion

* know what kind of question you are asking
* state questions early
* revise and clarify questions often
	* get specific about metrics

Test citations for question framing, rhetoric, and situated perspectives: the Stanford Encyclopedia overview of questions [@sep-questions] and *Data Feminism for Data Visualization* [@klein_dignazio_data_feminism_visualization].


## References
