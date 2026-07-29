# Ethics in Asking Questions

**[← Back to Course Homepage](../../index.html)**

::: {#fig-ds-lifecycle-ask-question}
<img src="../../assets/lifecycle/ds-lifecycle-v1.svg" alt="The data science lifecycle with Ask a question highlighted." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Asking a question, in the context of the data science lifecycle.
:::

> "There are naïve questions, tedious questions, ill-phrased questions, questions put after inadequate self-criticism. But every question is a cry to understand the world." (Carl Sagan)
>
> [@sagan_demon-haunted_1995, p. 303]

> "The 'technique,' or treatment, of a problem begins with its first expression as a question. The way a question is asked limits and disposes the ways in which any answer to it — right or wrong — may be given." (Susanne Langer)
>
> [@langer_philosophy_1942]

*This chapter is in-progress.*

There is a [meme template](https://knowyourmeme.com/memes/all-three-are-going-to-lie-to-you-never-ask-a-woman-her-age) that begins, "Never ask a woman her age, a man his salary..."

The basic principle underlying this meme is that some questions are more appropriate than others. Put another way, questions have varying levels of "appropriateness," and it is worthwhile to consider the quality of a question as part of the data science lifecycle.

In educational contexts, we appreciate all questions. The only bad question, as the saying goes, is the question you do not ask. And yet, as the aforementioned template suggests, some questions are more responsible, worthwhile, and/or appropriate than other questions. How might we distinguish these questions?

[@sep-questions]

As observed in The Craft of Research (Booth et al.), good questions usually present a corresponding problem, such that answering the question solves that problem.

I will use some modified examples from The Craft of Research to discuss the characteristics of high-quality (and low-quality) questions.


## Where Questions Come From

The data science lifecycle which this book adapts from @lau_learning_2023 suggests "ask a question" as one of two possible starting points in the lifecycle (the other being "obtain data"). In *Doing Data Science*, O'Neil and Schutt note the data science lifecycle can be thought of "as an extension or variation of the scientific method," a method which begins with "ask a question" [@oneil_2013_doing]. O'Neil and Schutt also suggest that this initial question is often connected to identifying some kind of problem, similar to Susanne Langer's observation quoted at the beginning of this chapter, and Booth et al.'s observation in The Craft of Research.

The data science lifecycle may start with asking a question, but not every question makes it through the full lifecycle. If you ask the score of a tennis match, or the current time, or the temperature outside, or someone's name, you will not proceed through the lifecycle as exhaustively as you would to answer other questions.

So, how do we know when a question is well-suited for the data science lifecycle? On the one hand, you can never be certain when you only have the question. That is one reason why the "Ask a question" step of the lifecycle includes four arrows pointing to it: other steps in the lifecycle can often lead data scientists back to revise their original question and begin the process anew.

On the other had, as data scientists learn from experience, there are some checks and heuristics that can help identify the kinds of questions which make for good data science.

In *The Craft of Research*, Wayne Booth observes that 'not with a big question that attracts everyone in a field, but with a mental itch about a small question that only a single researcher wants to scratch.

topic vs question
* a topic only becomes research when it provokes a specific question
* what is lost if a question goes unanswered — the "so what?" test [@booth_craft_of_research_2024]


## Basic Types of Questions
| Question Type | Description | Example | Answers |
| --- | --- | --- | --- |
| "Whether" | Presents a finite number of direct answers. May be yes-or-no questions, or questions that name two or more possible direct answers. | Was there a quorum at the meeting? | a. There was a quorum at the meeting.<br>b. There was no quorum at the meeting. |
|  |  | Does Alice live in Chicago, in New York City, or in Los Angeles? | a. Alice lives in Chicago.<br>b. Alice lives in New York City.<br>c. Alice lives in Los Angeles. |
| "Which" | Seeks a specific person, thing, or value. May have an indefinite or infinite number of direct answers. | Who was the President of the USA in 1978? | a. Jimmy Carter<br>b. Gerald Ford  |
|  |  | What is the smallest prime number greater than 12? | a. 13 is the smallest prime number greater than 12. |
|  |  | Which cardinal was elected Pope in 2013? | a. Cardinal Angelo Scola<br>b. Cardinal Odilo Scherer<br>c. Jorge Mario Bergoglio |
| "Why" | Asks for an explanation (not just a fact). Closely tied to causal, data-informed, or interpretive explanation. | Why do the planets move in elliptical orbits with the sun at one focus? | a. The gravitational pull of the sun causes the planets to move in elliptical orbits. |
| Indirect ("Embedded") | Comes from the complement of a clause-embedding predicate, such as `know` or `wonder`. These questions appear inside larger statements rather than standing alone. | Bob knows who spoke to Mary. | TK |


### Presuppositions
Many questions involve a *presupposition*: a background claim that must be true in order for the question to have a correct answer. If someone denies that background claim (i.e. the presupposition), they are correcting the question itself, and may not be able to answer the original question.

Below are some examples of presuppositions associated with example questions, as drawn from [@sep-questions].

| Question | Answer(s) | Presupposition(s) |
| --- | --- | --- |
| Who was the President of the USA in 1978? | a. Jimmy Carter<br>b. Gerald Ford | The USA had exactly one President in 1978. |
| Was there a quorum at the meeting? | a. There was a quorum at the meeting.<br>b. There was no quorum at the meeting. | The meeting occurred. |
| Does Alice live in Chicago, in New York City, or in Los Angeles? | a. Alice lives in Chicago.<br>b. Alice lives in New York City.<br>c. Alice lives in Los Angeles. | The question presupposes that Alice lives in one of the listed places. A corrective answer could reject that assumption, perhaps suggesting that Alice lived somewhere else, or in multiple cities. |
| Which cardinal was elected Pope in 2013? | a. Cardinal Angelo Scola<br>b. Cardinal Odilo Scherer<br>c. Jorge Mario Bergoglio | Someone was elected Pope in 2013. |
| Why do the planets move in elliptical orbits with the sun at one focus? | a. The gravitational pull of the sun causes the planets to move in elliptical orbits. | The planets do move in elliptical orbits with the sun at one focus. |


## Common Pitfalls
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
* empirical question can be separate from judgment, to some extent (?)

### Leading questions

* usually implies a preferred answer
	* e.g. "everything tasting good over here?"
	* e.g. "
* i.e. ad-hoc support of suspect decision-making
* ask before answering
* might actually be good to be more naïve
	* ask as if you knew less

### Tedious questions

* effort required to answer a question may be disproportional to what the answer would teach us.
* measurable details are not always meaningful
* triangle/pixel example from first chapter

### Invasive questions

If a potential employer were to ask my weight during a job interview, it would be inappropriate. However, when I visit the Department of Motor Vehicles (DMV) to obtain my driver’s license, I am required to provide an answer. I have consented to the requirements of the system if I wish to obtain their permission to drive cars in the state (i.e. to get my driver's license).

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

* Deirdre McCloskey - notes on "objective" analysis as rhetorical/persuasive; questions embed values/narratives.
* good to assume you might've missed something
* data hubris

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

## Test

Test citations for question framing, rhetoric, and situated perspectives: the Stanford Encyclopedia overview of questions [@sep-questions] and *Data Feminism for Data Visualization* [@klein_dignazio_data_feminism_visualization].

## This is actually the hard part

> "In my opinion, the social sciences are the hard sciences" (Michael Shermer)
>
> [@shermer_mind_market_2008]

Crafting a high-quality research question for the data science lifecycle can be unexpectedly difficult and time-consuming.




## References
