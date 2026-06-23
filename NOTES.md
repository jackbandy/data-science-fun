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

Mostly Richard McElreath videos

### 'Garden of Forking Data' (Statistical Rethinking)
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
* "statistics is not for giving you the answer you want, but to tell you what the data justify"
* posterior probability distributions
	* probability densities
	* probability masses
	* posterior distribution vs. posterior predictive
* bayesian clinical trials: stop the trial as soon as you're sure there's therapeutic benefit. Therefore, always update with new data.
	* More important when data is expensive/priceless
* "the estimate is the distribution" - point estimates only when requested / needed for communication
* 1: no minimum sample size
* 2: shape embodies sample size
* 3: no point estimate
* 4: no 'one true interval'
	* infinite possible ranges
	* 50% central: same mass on the left and right
	* nothing magical about 95%
* "always summarize last"
	* do all calculations with full distributions

### Geocentric models (Statistical Rethinking)
* analogy - geocentric models as linear regression
	* it might not be structurally/scientifically accurate, but it can still be predictive
* 'theoria motvs corporvm coelestivm' - gauss' approach to normal error and least-squares estimation ("1809 Bayesian argument")
* "useful family of estimators"
	* "useful when handled with care"
	* special cases: ANOVA, ANCOVA, t-test
* linear models are not mechanistic
* gaussian distribution = mean, dispersion
* "just keep swimming" - fine/good to be a little confused, experience some resistance
* creating a generative model
	* "which variables listen to other variables?"
* weight/height example
	* H -> W
	* W = f(H)
	* height influences weight
	* weight is some function of height
* weight/height with other factors
	* W = f(H, U)
	* W = BH + U
	* U from normal
	* H from uniform
* example priors:
	* weight is more as height goes up
* each data point constrains the distribution

### Categories and Causes (Statistical Rethinking)
https://www.youtube.com/watch?v=GIdwLrW2nNo
* "scientifically justifiable workflow"
* "first law of statistical interpretation"
	* the parameters in a posterior distribution are not independent - they have joint information
* categories defined: discrete, unordered types
	* distinct from ordered types!
* causality: "if you intervene on a variable, which other variables change?"

### Data Science in Government (Monica G. Bobra)
* try to select projects that "measurably improve a business process or service"
* emphasis on interpretable models ("models that people can understand and explain")
* social services example - model to help reduce benefit theft (CDSS - case study and technical paper)
* running examples: social services, clean water
* curricula suggestions
	* "think like a journalist"
	* interpretable, auditable models

### Estimands and Estiplans (Statistical Rethinking)
* https://www.youtube.com/watch?v=sYE8a95x-0E&list=PLDcUM9US4XdNOlqSyhe38US8mFgmqzI14&index=5
* estimand is a goal of what you want
	* estimator some way to figure out how to construct the estimand
	* in a bayesian workflow, a generative model
	* what you get might not be what you wanted - reconsider assumptions, models, etc.
* synthetic data and estimates can be helpful to build confidence in models
* posterior means are distributions
* "always be contrasting" - the overlapping distributions don't tell us about the expected difference
	* add a distribution/curve to show the difference - compute the contrast
* "I'm a scientist, I hate statistics, but there is no other way out but through"
* "the goal is to say, for each height, imagine manipulating sex, holding height constant, what's the change in weight?"
* posterior bowtie
	* distribution of weight differences from women and men at different heights
* vast majority of weight differences can be attributed to height
* a pipeline is not a workflow

### Elemental Confounds / Causal Inference
* https://www.youtube.com/watch?v=lGR7D45Ww38&list=PLDcUM9US4XdNOlqSyhe38US8mFgmqzI14&index=6

## Misc. TODO

* Add a side-by-side variant of the `.code-figure-slide` template (code and figure
  left/right instead of stacked top/bottom).
* Polish the PDF rendering.
* Check overflow on slide templates (i.e. spilling into footer).
* clean up ipynb headers
* another data science lifecycle - https://medium.com/swlh/complete-life-cycle-of-a-data-science-machine-learning-project-13df81bbd8eb
	* connection to design thinking / design workflow? https://www.nngroup.com/articles/design-thinking/
* ethics in data science mini-book - preregistration process - before "understanding"
* "linear models do not 'assume' anything"
	* e.g. residuals can take whatever shape they want
	* assumption is not a prior (?)
	* strong inference requires strong assumptions
	* "inference without assumptions is like an opinion without evidence"

## Running examples
* globe toss: estimate % of water
* voter turnout estimate/forecast
* water/electricity/utility usage
* estimate CTA ridership on a given day
* determine if a drug is effective
* which movie to watch with friends
	* which movies have they seen
* which book(s)/article(s) to read next
* population dynamics: births, marriages, deaths, etc.

## Etc.


[Data Scientist: The Sexiest Job of the 21st Century](https://hbr.org/2012/10/data-scientist-the-sexiest-job-of-the-21st-century)

Study to reproduce: [Did Taylor Swift kill a bunch of people?](https://statmodeling.stat.columbia.edu/2026/04/21/did-taylor-swift-kill-a-bunch-of-people/)

Data Science Origins? John Tukey's 1962 work, [The Future of Data Analysis](https://www.jstor.org/stable/2237638)

https://cs.uic.edu/undergraduate/data-science-major/

"Is this data safe to release?"
