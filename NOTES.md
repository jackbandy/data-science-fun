# Notes

## Unstructured jots on what to include

Course description:
Provides an in-depth overview of data science in engineering. Topics include modeling, storage, manipulation, integration, classification, analysis, visualization, information extraction, and big data in the engineering domain.

Miscellaneous topics:
* Recommender systems
* Evaluation metrics (e.g. https://www.byhand.ai/p/ai-eval-equations-you-must-know)
* Moviepass projection flop
  * Mitch Lowe AMA on Reddit - https://www.reddit.com/r/movies/comments/8u00y3/im_mitch_lowe_ceo_of_moviepass_ama/
  * "A Platform for Burning Cash" - https://d3.harvard.edu/platform-digit/submission/moviepass-a-platform-for-burning-cash/
  * Blog post - https://www.residualthoughts.com/2018/03/15/the-numbers-behind-moviepass-and-why-its-probably-doomed/
  * Slate article - https://archive.ph/IxKa9

Miscellaneous exercise ideas:
* data diorama
* de-anonymization challenge
* portfolio piece - interactive data explainer / data story

What is included in data science?
Learning DS Textbook:
* Data science life cycle
  * ask questions, obtain data, understand data, understand world
* Questions / data scope
  * Instruments protocols
  * Population, access framing, sampling
  * Measurement errors and accuracy
  * Big data pitfalls ("data hubris")
* Simulation and Data Design
* Modeling with Summary Stats
  * Loss minimization
* Dataframes
  * data frames and other common representations
  * subsetting, aggregating, joining, transforming
* Relations and SQL
* Wrangling files
* Wrangling dataframes
* Exploratory data analysis (eDA)
* Data visualizations
* Data sources
  * Text
  * Binary formats
  * Binary formats, APIs, scraping, etc.
* Linear Modeling
* Time series modeling / analysis
  * seasonality
  * stationarity
* Classification

## Lecture notes

### 'Garden of Forking Data'
* https://www.youtube.com/watch?v=R1vcdhPBlXA
* estimate a proportion
* bayesian workflow for an estimator
* estimand: proportion of _ covered by water
	* estimates are always distributions, not points
* sample, e.g. L/W/L/L/W/W/L/W/W
* how should we use the sample? How to produce a summary? How to represent uncertainty?
* Workflow:
	* 1. Define generative model
	* 2. define specific estimated 
	* 3. Design an estimator
	* 4. Test
	* 5. Analyze and summarize
* connect DAG to function
* "explanations with more ways to produce the sample are more plausible"
* Jorge Luis Borges - El Jardin De Senderos Que Se Bifurcan
* Example
	* Four-sided die
	* Five possible globes
	* Assuming the globe is covered 25%, there are three ways to observe "WLW" from three rolls
		* 8 ways (out of 64) if globe is 50% water
		* 9 ways (out of 64) if globe is 75%
	* If water is observed in the sample, the globe can't be all land.
* "things that can happen more ways are more plausible"
* probabilities: non-negative values that sum to one
* 

## TODO

* Add a side-by-side variant of the `.code-figure-slide` template (code and figure
  left/right instead of stacked top/bottom).

## Etc.


[Data Scientist: The Sexiest Job of the 21st Century](https://hbr.org/2012/10/data-scientist-the-sexiest-job-of-the-21st-century)

Study to reproduce: [Did Taylor Swift kill a bunch of people?](https://statmodeling.stat.columbia.edu/2026/04/21/did-taylor-swift-kill-a-bunch-of-people/)

Data Science Origins? John Tukey's 1962 work, [The Future of Data Analysis](https://www.jstor.org/stable/2237638)

"Is this data safe to release?"
