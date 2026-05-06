# Data Science Foundations

1. Introduction to Data Science

1.1 Historical overview

Data science
Data science is an interdisciplinary field focused on discovering patterns and describing relationships using data.
Aside
Learn to:

P
Animation
1.1.1 Comparing data science, computer science, and statistics.

P
Question Set
1.1.2 Data science.

P
Animation
1.1.3 Data science timeline.

P
Question Set
1.1.4 Early years of data science.

P
Animation
1.1.5 Data science timeline (continued).

P
Question Set
1.1.6 Data science in the 21st century.

P
Animation
1.1.7 Methods in data science.

P
Question Set
1.1.8 Methods in data science.
1.2 Why data science?

dataset
A dataset is a collection of information.
feature
A feature, or variable, is a characteristic that can be measured or observed on an observational unit.
instances
Features are recorded for individual instances, or observational units, in the dataset. Instances are also called data points or observations.
Big data
Big data describes datasets with large volume, created and updated with high velocity, that have variety in structure and format.
Aside
Learn to:

P
Animation
1.2.1 Features and instances.

P
Question Set
1.2.2 Features and instances.

P
Animation
1.2.3 Big data at Twitter.

P
Question Set
1.2.4 Big data in healthcare.

P
Animation
1.2.5 How big is big data?

P
Question Set
1.2.6 Big data volume.

P
Animation
1.2.7 Reproducible analysis.

P
Question Set
1.2.8 Big data velocity.

P
Animation
1.2.9 Your day in big data.

P
Question Set
1.2.10 Big data variety.
1.3 Careers in data science

Aside
Learn to:

P
Animation
1.3.1 Data science demand by industry.

P
Question Set
1.3.2 Data science career demand.
Table
1.3.1 Data science job descriptions.

P
Animation
1.3.3 Data professionals: engineers, analysts, and scientists.

P
Question Set
1.3.4 Jobs in data science.
1.4 Data science lifecycle

data science lifecycle
The data science lifecycle is a five-step process for completing a research project using data.
Structured data
Structured data is stored in a pre-defined format, typically with features stored in columns and instances in rows.
database
A database is a collection of organized information stored in a computer system.
Unstructured data
Unstructured data does not have a predefined format and is difficult for humans to interpret. Instead, unstructured data points may contain multiple pieces of information that are converted to a structured form before analysis.
supervised models
Models that predict a feature with known values in the original dataset are supervised models.
Classification models
Classification models predict categorical features.
Regression models
Regression models predict numerical features.
Unsupervised models
Unsupervised models look for hidden groups or patterns in the dataset rather than predicting a known feature.
Aside
Learn to:
Table
1.4.1 Data science lifecycle.

P
Animation
1.4.1 Applying the data science lifecycle.

P
Question Set
1.4.2 Data science lifecycle.

P
Animation
1.4.3 Types of data.

P
Question Set
1.4.4 Types of data.

P
Animation
1.4.5 Cleaning data.

P
Question Set
1.4.6 Cleaning data.

P
Animation
1.4.7 Exploring data.

P
Question Set
1.4.8 Exploring data.

P
Animation
1.4.9 Modeling data.

P
Question Set
1.4.10 Modeling data.

P
Animation
1.4.11 Interpreting data.

P
Question Set
1.4.12 Interpreting data.

C
Progression
1.4.1 Data science lifecycle.
1.5 Ethics in data science

Data ethics
Data ethics is the field of ethical conduct in data science.
Data anonymization
Data anonymization occurs when identifying information such as names and emails is removed before beginning data analysis to protect individual privacy.
Algorithmic bias
Algorithmic bias occurs when a model predicts outcomes that would be considered unfair, such as unintentionally privileging one category over the other.
Aside
Learn to:

P
Animation
1.5.1 Electronic health records.

P
Question Set
1.5.2 Data ethics.
Aside
Individual data rights under GDPR

P
Animation
1.5.3 Data anonymization.

P
Question Set
1.5.4 Data privacy.
Aside
Data privacy in online dating

P
Animation
1.5.5 Algorithmic bias in hiring.

P
Question Set
1.5.6 Algorithmic bias.

P
Animation
1.5.7 Collecting personal data from Facebook users.

P
Question Set
1.5.8 Cambridge Analytica scandal.

P
Animation
1.5.9 Impact of data centers in Ireland.

P
Question Set
1.5.10 Energy use in data centers.
1.6 Case study: Netflix

Aside
Learn to:

P
Animation
1.6.1 CineMatch ratings.

P
Question Set
1.6.2 CineMatch predictions.

P
Animation
1.6.3 Gathering and cleaning Netflix data.

P
Question Set
1.6.4 Netflix Prize dataset.

P
Animation
1.6.5 Declaring a winner of the Netflix Prize.

P
Question Set
1.6.6 Winning the Netflix Prize.

P
Animation
1.6.7 RMSE for CineMatch.

P
Question Set
1.6.8 A replacement for CineMatch?

P
Animation
1.6.9 De-anonymizing Netflix ratings.

P
Question Set
1.6.10 Ethics of the Netflix Prize.
2. Probability and Statistics

2.1 Data collection

population
A population is the entire set of all individuals, items, or events of interest.
observational unit
An observational unit is an individual, item, or event of the population on which data can be recorded.
sample
A sample is the subset of observational units from the population from which data will be collected. The number of observational units in the sample is denoted by .
sampling method
A sampling method is a process by which observational units are selected from the population to be included in the sample.
random sampling
In random sampling, observational units are selected at random from the population in which each subset of  units is equally likely.
stratified sampling
In stratified sampling, the population is first divided into groups, called strata, based on a meaningful feature, then observational units are selected from each stratum.
cluster sampling
In cluster sampling, the population is first divided into groups, called clusters, based on a feature, then a random sample of some clusters is selected.
systematic sampling
In systematic sampling, from a randomly selected starting point of the population, every  observational unit is selected.
convenience sampling
In convenience sampling, observational units from the population that are easier to include are selected.
observational study
In an observational study, data is collected by recording the responses as they occur without any direct influence on the observed data.
experiment
In an experiment, treatments are first assigned to observational units and then responses are recorded.
causal conclusions
With random assignment of treatments to observational units, causal conclusions, or concluding the treatments are likely to be the cause of the observed responses, can be made.
Aside
Learn to:

P
Animation
2.1.1 Statistics in a data science project.

P
Question Set
2.1.2 Statistics and data science.

P
Animation
2.1.3 Passenger satisfaction in Australia.

P
Question Set
2.1.4 Passenger satisfaction in Australia.

P
Animation
2.1.5 Sampling methods for the passenger satisfaction project.

P
Question Set
2.1.6 Sampling methods.

P
Animation
2.1.7 Collecting fuel efficiency data.

P
Question Set
2.1.8 Observational studies and experiments.

C
Progression
2.1.1 Data collection.
2.2 Descriptive statistics

feature
A feature, or variable, is a characteristic that can be measured or observed on an observational unit.
Descriptive statistics
Descriptive statistics are methods to summarize and describe a feature's important characteristics.
distribution
The distribution of a feature is the possible values the feature can take on and a measure of how often each value occurs.
cluster
A cluster is a distinct group of neighboring values in a distribution that occur noticeably more often than the values on either side of the group.
tails
The tails of a distribution are the end values of the distribution. The left tail refers to the lowest values of the distribution, and the right tail refers to the highest values of the distribution.
mean
The mean, or average, of a numerical feature is the sum of all values divided by the total number of values.
median
The median of a numerical feature is the middle value of the ordered data.
range
The range is the distance from the minimum value to the maximum value of a numerical feature.
interquartile range
The interquartile range (IQR) is the range of the middle 50% of the distribution of a numerical feature.
variance
The variance is the average squared distance a numerical feature's values lie from the distribution's mean.
standard deviation
The standard deviation is the square root of the variance and describes how far a numerical feature's values lie, on average, from the distribution's mean.
quantile
A quantile is a value for which a specified proportion of the distribution falls at or below the value.
standardized score
A standardized score, or z-score, describes how many standard deviations—and in which direction—a value lies from the distribution's mean. The equation to find a value's standardized score is .
symmetric
A distribution is symmetric when the right side of center and the left side of center are roughly mirror images.
skewed
A distribution is skewed if the distribution's values extend farther to one side of the distribution's center.
Skewness
Skewness is a measure of the amount and direction of skew, or departure from symmetry.
Kurtosis
Kurtosis is a measure of tail heaviness. Larger values of kurtosis indicate a greater presence of extreme values in the distribution.
Aside
Learn to:

P
Animation
2.2.1 Summarizing Australian train passenger survey data.

P
Question Set
2.2.2 Describing the total travel time feature.
Aside
Types of features

P
Animation
2.2.3 Comparing measures of center.

P
Question Set
2.2.4 Measures of center.
Aside
Calculating variance

P
Animation
2.2.5 Measures of spread.

P
Question Set
2.2.6 Measures of spread.

P
Animation
2.2.7 Measures of position.

P
Question Set
2.2.8 Measures of position.

P
Animation
2.2.9 Comparing distribution shapes in terms of skewness.

P
Question Set
2.2.10 Measures of shape.

C
Progression
2.2.1 Descriptive statistics.
2.3 Probability

Probability
Probability is a measure of likelihood between 0 and 1. Probabilities near 0 correspond to unlikely events and probabilities near 1 correspond to almost certain events.
random process
A random process is an action or process which results in an outcome determined by chance.
outcome
An outcome is one possible result from a random process.
sample space
The sample space is the set of all possible outcomes of a random process and denoted as .
event
An event is an outcome or collection of outcomes from a sample space. Events are typically denoted by , , or .
probability of an event A
The probability of an event A, denoted , is measured as the number of outcomes in  divided by the total number of equally likely outcomes in the sample space, . The probability of an event can also be understood as the long-run proportion of times event  occurs if the random process is observed many times.
complement
The complement of event , denoted , is the event consisting of all outcomes in the sample space  that are not in event .
union
The union of two events,  and , denoted , is the event consisting of all outcomes in  or , including outcomes in both  and .
intersection
The intersection of two events,  and , denoted , is the event consisting of only the outcomes in both and .
disjoint / mutually exclusive
Two events,  and , are considered disjoint, or mutually exclusive, if the two events have no outcomes in common. In other words, the event  is empty or contains no outcomes.
independent
Two events are considered independent if knowing one event has occurred does not affect the probability of the other event.
conditional probability
A conditional probability is a measure of the likelihood of one event occurring, given another event has occurred. The conditional probability of event  given event  has occurred, denoted as , is .
Bayes' rule
Bayes' rule for finding the conditional probability of  given  is .
Aside
Learn to:

P
Animation
2.3.1 Prize wheel probability example.

P
Question Set
2.3.2 Probability.

P
Animation
2.3.3 Event operations.

P
Question Set
2.3.4 Event operations.

P
Animation
2.3.5 Probability rules.

P
Question Set
2.3.6 Probability rules.

P
Animation
2.3.7 Conditional probability.

P
Question Set
2.3.8 Conditional probability.

P
Animation
2.3.9 Bayes' rule.

P
Question Set
2.3.10 Bayes' rule.

C
Progression
2.3.1 Probability.
2.4 Probability distributions

random variable
A random variable defines numerical values for a random process's outcomes. Random variables are typically denoted by , , or .
discrete random variable
A discrete random variable takes on a countable number of distinct values.
continuous random variable
A continuous random variable takes on all values within an interval.
probability distribution
A random variable's probability distribution gives the probability of occurrence for the random variable's possible numerical values.
Bernoulli distribution
A discrete random variable in which the only possible values are 0 and 1 follows a Bernoulli distribution.
parameters
The parameters of a probability distribution determine the distribution's shape and probabilities.
binomial distribution
A random variable describing the number of "successes" from  independent observations of a random process in which the probability of a success is  follows a binomial distribution. The binomial distribution, binomial(), is specified by two parameters: the number of outcomes observed, , and the probability of a "success", .
normal distribution
The normal distribution, normal(), is a symmetric, bell-shaped distribution and is determined by two parameters: the mean, , and the standard deviation, .
standard normal distribution
The standard normal distribution is the normal distribution with mean  = 0 and standard deviation  = 1.
Aside
Learn to:

P
Animation
2.4.1 Probability distributions for random variables.

P
Question Set
2.4.2 Random variables.

P
Animation
2.4.3 Bernoulli distribution.

P
Question Set
2.4.4 Bernoulli distribution.

P
Animation
2.4.5 Binomial distribution.

P
Question Set
2.4.6 Binomial distribution.

P
Animation
2.4.7 Normal distribution.

P
Question Set
2.4.8 Normal distributions.

P
Animation
2.4.9 -distribution.

P
Question Set
2.4.10 -distribution.

C
Progression
2.4.1 Normal distribution and z-scores.
2.5 Inferential statistics

Inferential statistics
Inferential statistics are methods that result in conclusions and estimates about the population based on a sample.
parameter
A numerical quantity of the population, such as the population mean or population proportion, is called a parameter.
sampling distribution
The sampling distribution of a statistic describes the statistic's possible values and a measure of how likely the values are to occur.
Central Limit Theorem
The Central Limit Theorem (CLT) states that if random samples of size  are drawn from a large population and  is large enough, then the sampling distribution of the sample mean will follow approximately a normal distribution.
hypothesis test
A hypothesis test is a method for evaluating a claim, or hypothesis, about a population parameter by examining the statistical evidence against the claim based on a sample.
null hypothesis / alternative hypothesis
State null and alternative hypotheses about parameters. The null hypothesis, , is typically the by-chance or no-effect explanation, and the alternative hypothesis, , is typically the explanation of an effect, or difference.
p-value
Determine the p-value, or likelihood, of obtaining a statistic at least as extreme as the observed statistic when the null hypothesis is true.
significance level
The significance level, , of a hypothesis test is how small the p-value must be to conclude the data provide enough statistical evidence to reject the null hypothesis.
type I error
A type I error is rejecting the null hypothesis in favor of the alternative when in reality the null hypothesis is true.
type II error
A type II error is failing to reject the null hypothesis when in reality the alternative hypothesis is true.
confidence interval
A confidence interval provides an interval of possible values for the parameter being estimated. A confidence interval is constructed using the general equation . The estimate is a statistic calculated from the sample data and gives an initial best guess for the parameter's value.
margin of error
The margin of error measures the precision of the estimate and includes:
the standard error, or measure of sampling variability, which comes from the statistic's sampling distribution, and
the confidence level, or measure of interval reliability.
.
Aside
Learn to:

P
Animation
2.5.1 Inferential statistics for estimating compost moisture content.

P
Question Set
2.5.2 Descriptive and inferential statistics.

P
Animation
2.5.3 Sampling distribution of a sample mean.

P
Question Set
2.5.4 Sampling distribution of a sample mean.

P
Question Set
2.5.5 Sampling distributions of counts and proportions.

P
Animation
2.5.6 Central Limit Theorem.

P
Question Set
2.5.7 Central Limit Theorem.

P
Animation
2.5.8 Can a dog detect cancer by smell?

P
Question Set
2.5.9 Hypothesis testing.

P
Animation
2.5.10 Type I and type II errors.

P
Question Set
2.5.11 Type I and type II errors.

P
Animation
2.5.12 Constructing a confidence interval.

P
Question Set
2.5.13 Confidence Interval for a population mean.
2.6 Inference for proportions and means

Aside
Learn to:

P
Animation
2.6.1 Northwest Iowa radon one-proportion hypothesis test.

P
Question Set
2.6.2 Northwest Iowa radon one proportion inference example.

P
Animation
2.6.3 Two-proportion hypothesis test.

P
Question Set
2.6.4 One-sided vs. two-sided hypothesis test for two proportions.
Aside
Statistical vs. practical difference

P
Animation
2.6.5 One mean hypothesis test.

P
Question Set
2.6.6 One mean hypothesis test.

P
Animation
2.6.7 Comparison of two population means.

P
Question Set
2.6.8 Inference for two means.

C
Progression
2.6.1 Inference for proportions and means.
2.7 Case study: Flight delays

practically significant
A difference between two groups is practically significant if the difference is large enough to have a real-life consequence.
Aside
Learn to:

P
Animation
2.7.1 New York City airports.

P
Question Set
2.7.2 Flight traffic in 2013.

P
Question Set
2.7.3 Are flight delays more likely at JFK or LaGuardia?

P
Question Set
2.7.4 Are delays longer at JFK or LaGuardia?

P
Question Set
2.7.5 Is the difference in delays practically significant?
3. Data Wrangling

3.1 Data wrangling

Data wrangling
Data wrangling is the process of preparing source data for efficient and accurate analysis.
data munging / data preparation
Data wrangling is sometimes called data munging or data preparation.
Extract, Transform, Load / ETL
Extract, Transform, Load (ETL) is a process that extracts data from transactional databases, transforms the data, and loads the data into an analytic database.
staging area
ETL transforms data in a staging area, such as a temporary database, prior to loading data to the analytic database.
Extract, Load, Transform / ELT
Extract, Load, Transform (ELT) is a variant of ETL that loads raw data directly to the analytic database and transforms the data in place.
data integration
ETL tools, also called data integration tools, extract and merge data from many different database systems.
Aside
Learn to:
Table
3.1.1 Steps of data wrangling.

P
Animation
3.1.1 Data wrangling steps.

P
Question Set
3.1.2 Data wrangling steps.
Table
3.1.2 Leading ETL tool vendors.

P
Question Set
3.1.3 Data wrangling vs. ETL.
3.2 Exploring data

Data exploration
Data exploration is the first step of the data wrangling process, which includes exploring patterns and trends within a dataset.
Grouping
Grouping is used to separate a dataframe into subsets based on levels of a categorical feature.
frequency table
A frequency table is a table containing group sizes for a categorical feature.
pivot table
A pivot table calculates and displays descriptive statistics after grouping based on values of two categorical features.
contingency table
A contingency table is a special case of a pivot table in which the descriptive statistic is the number of instances in each combination of categorical features.
Aside
Learn to:

P
Animation
3.2.1 Discovering data.

P
Question Set
3.2.2 Data exploration.

P
Animation
3.2.3 Data summaries using group, calculate, combine.

P
Question Set
3.2.4 Grouping data.

P
Animation
3.2.5 Pivot tables.

P
Question Set
3.2.6 Pivot table.

C
Progression
3.2.1 Discovering data.
3.3 Structuring data

Feature scaling
Feature scaling converts numeric features to uniform ranges.
Standardization / z-score
Standardization converts features to a range centered at 0, with 1 representing a standard deviation:

 is the mean and  is the standard deviation of feature . The standardized value is called a z-score.
Normalization
Normalization converts features to the range [0,1]:

.
overloaded feature
An overloaded feature encodes multiple types of data.
simple feature
A simple feature contains only one type of data.
Aside
Learn to:

P
Animation
3.3.1 Formatting data.

P
Question Set
3.3.2 Formatting data.
Aside
Terminology

P
Animation
3.3.3 Feature scaling.

P
Question Set
3.3.4 Standardization.

P
Question Set
3.3.5 Normalization.

P
Animation
3.3.6 Vehicle Identification Number (VIN).

P
Question Set
3.3.7 Unpacking data.

C
Progression
3.3.1 Structuring data.
3.4 Cleaning data

Missing data
Missing data is an unknown or inapplicable value. In a database, missing data is represented as NULL.
Outlier data
Outlier data is a numeric value that is much larger or smaller than other values in the same feature.
Duplicate data
Duplicate data are two or more identical instances in a dataset.
dirty data
Missing, outlier, and duplicate data are collectively called dirty data.
dirty instance / dirty feature
A dirty instance and a dirty feature contain dirty data.
Discarding instances / listwise deletion / complete case removal
Discarding instances, also called listwise deletion or complete case removal, removes dirty instances from the dataset.
Discarding features
Discarding features removes dirty features that contain a high percentage of missing values, such as 60% or more.
Pairwise discarding
Pairwise discarding retains dirty instances for some analyses and discards dirty instances for others. Instances are discarded only when an analysis uses a dirty feature.
Imputing data
Imputing data replaces missing and outlier data with new values.
Hot-deck / cold-deck imputation
Hot-deck and cold-deck imputation replace missing and outlier data with a value from a randomly selected instance. In hot-deck imputation, the value is selected from other instances in the same dataset. In cold-deck imputation, the value is selected from a different dataset.
Mean imputation
Mean imputation replaces missing and outlier data with the mean value of the feature. Missing and outlier data are excluded from the computation of the mean.
Regression imputation / Stochastic regression imputation
Regression imputation replaces missing and outlier data with a value computed from a regression model. In the regression model, the dependent variable is the dirty feature and the independent variables are other features. Stochastic regression imputation introduces uncertainty by adding or subtracting the regression variance to the new value. Regression models are discussed elsewhere in this material.
Aside
Learn to:

P
Animation
3.4.1 Dirty data.

P
Question Set
3.4.2 Dirty data.

P
Animation
3.4.3 Discarding data.

P
Question Set
3.4.4 Discarding data.

P
Animation
3.4.5 Imputing data.

P
Question Set
3.4.6 Imputing data.

C
Progression
3.4.1 Cleaning data.
3.5 Enriching data

Aside
Learn to:
Table
3.5.1 Leading public datasets.

P
Animation
3.5.1 Appending data.

P
Question Set
3.5.2 Appending data.

P
Animation
3.5.3 Deriving data.

P
Question Set
3.5.4 Data wrangling activities.

C
Progression
3.5.1 Enriching data.
3.6 Data engineering

Data engineering
Data engineering is a subset of software engineering focused on systems for collecting, storing, and accessing data.
database
A database is a collection of organized information stored in a computer system.
data warehouse
A data warehouse combines data from multiple data sources, optimized for data analysis and processing.
data lake
A data lake is a main repository for data stored in multiple formats.
Data lakehouses
Data lakehouses combine features of data lakes and data warehouses for improved big data storage.
Distributed file systems
Distributed file systems (DFS) allow users to store and access data across multiple computers or servers.
Hadoop
Hadoop is an open-source framework for storing and processing big data.
MapReduce
MapReduce is the processing model for Hadoop, which processes data using batches.
data platform
A data platform is a software solution for storing, accessing, and analyzing data.
Spark
Apache Spark is an open-source framework for large-scale data processing using parallel processing and distributed file storage.
Snowflake
Snowflake is a cloud storage platform.
Databricks
Databricks is an online data platform that uses data lakehouses for more flexible storage.
Aside
Learn to:

P
Animation
3.6.1 Data engineers vs. data scientists.

P
Question Set
3.6.2 Data engineering vs. data wrangling.

P
Animation
3.6.3 Electronic health records.

P
Question Set
3.6.4 Big data storage.

P
Animation
3.6.5 Distributed file systems vs. local storage.

P
Question Set
3.6.6 Distributed file systems.
Table
3.6.1 Features of data platforms.

P
Question Set
3.6.7 Data platforms.

C
Progression
3.6.1 Data engineering.
3.7 Case study: Diamond prices

Aside
Learn to:

P
Animation
3.7.1 Measuring diamond quality.

P
Question Set
3.7.2 What makes a diamond high quality?

P
Question Set
3.7.3 Discovering the diamonds data.
Figure
3.7.1 Histograms of price, width, and table from the diamonds dataset.

P
Question Set
3.7.4 Restructuring the diamonds data.
Table
3.7.1 Number of instances with recorded values for features in the diamonds dataset.
Figure
3.7.2 Histograms of depth, price, length, and carat from the diamonds dataset.

P
Question Set
3.7.5 Cleaning the diamonds data.
Table
3.7.2 Descriptive statistics for ratio = length/width.

P
Question Set
3.7.6 Enriching the diamonds data.
3.8 Case study: App reviews

Text mining
Text mining is the process of identifying meaningful insights and patterns from text data.
Tokenization
Tokenization splits text into individual tokens, usually a word or phrase.
Stop word removal
Stop word removal removes common words from text that do not contribute to the text's meaning.
Stemming
Stemming reduces a word into the corresponding base or root form by removing prefixes and suffixes.
Lemmatization
Lemmatization reduces a word into the corresponding base or root form by using a dictionary to learn the meaning of the root.
Sentiment analysis
Sentiment analysis is a specific case of text classification that applies a sentiment label to a sequence of text.
Aside
Learn to:

P
Question Set
3.8.1 Understanding the app review dataset.

P
Question Set
3.8.2 Structuring the reviews dataset.

P
Question Set
3.8.3 Text processing the reviews dataset.

P
Question Set
3.8.4 Sentiment scores.
4. Data Visualization

4.1 Visualizing data with one feature

categorical feature
A categorical feature divides the dataset into different groups or categories.
bar chart
A bar chart has the groups on one axis and then rectangles with heights that represent the number of individuals in that group.
relative frequency bar chart
A relative frequency bar chart is a bar chart, but the height of each bar corresponds to the proportion of the dataset in each group.
numerical feature
A numerical feature contains numbers that vary over many values.
Aside
Learn to:
Table
4.1.1 Features of the country dataset.

P
Question Set
4.1.1 Interpreting bar charts.

P
Question Set
4.1.2 Relative frequency bar charts.
Table
4.1.2 Numerical feature visualizations.

P
Animation
4.1.3 Making histograms and box plots.

P
Question Set
4.1.4 Interpreting numerical feature visualizations.

C
Progression
4.1.1 Visualizing data with a single feature.
4.2 Visualizing data with multiple features

scatter plot
A scatter plot displays an instance in a dataset as a point in a two-dimensional plane. The point's coordinates are the two features' values.
Faceting
Faceting is the practice of displaying multiple plots side by side in an array where one feature changes from plot to plot.
Aside
Learn to:
Table
4.2.1 Features of the tips dataset.

P
Animation
4.2.1 Making a scatter plot.

P
Question Set
4.2.2 Interpreting scatter plots.
Table
4.2.2 Visualizations for two categorical features.

P
Animation
4.2.3 Grouped bar charts.

P
Question Set
4.2.4 Interpreting bar charts.
Table
4.2.3 Categorical and numerical feature visualizations.

P
Question Set
4.2.5 Interpreting categorical and numerical visualizations.
Table
4.2.4 Attributes for displaying more features.

P
Question Set
4.2.6 Visualizing multiple features.

C
Progression
4.2.1 Visualizing data with multiple features.
4.3 Best practices for visualizing data

Contrast
Contrast is the difference between the brightness of two colors.
pie chart
A pie chart is a circle made of wedges, one wedge for each group. The size of each wedge illustrates the proportion of the dataset in each group.
Aside
Learn to:

P
Animation
4.3.1 Guidelines for selecting plots.

P
Question Set
4.3.2 Determining the type of plot based on feature type.

P
Animation
4.3.3 Bad bar charts.

P
Question Set
4.3.4 Identifying issues with scales.

P
Question Set
4.3.5 Picking visual designs.

P
Animation
4.3.6 Making pie charts.

P
Question Set
4.3.7 Interpreting proportion charts.

C
Progression
4.3.1 Best practices for visualizing data.
4.4 Tools for visualizing data

spreadsheet
A spreadsheet is an application that displays data in a grid and allows calculations and edits within that grid.
Aside
Learn to:
Video
4.4.1 Visualizing data with spreadsheets.

P
Question Set
4.4.1 Spreadsheet visualization.
Video
4.4.2 Visualizing data with PowerBI.

P
Question Set
4.4.2 Interpreting the plot from PowerBI.
4.5 Performing exploratory data analysis

Exploratory data analysis / EDA
Exploratory data analysis or EDA is the process of investigating a dataset to understand what is in the dataset.
Correlation
Correlation describes the strength and direction of a linear relationship between numerical features.
missing completely at random / MCAR
Values that are missing completely at random or MCAR have the same probability of being missing for all cases.
missing at random / MAR
Values that are missing at random or MAR have the same probability of being missing for specific observable cases.
missing not at random / MNAR
Values that are missing not at random or MNAR have different probabilities of being missing due to unknown reasons.
Aside
Learn to:
Process
4.5.1 Exploratory data analysis.

P
Animation
4.5.1 Simulated data on 289 individuals.

P
Question Set
4.5.2 Exploratory data analysis steps.

P
Animation
4.5.3 Identifying relationships between features.

P
Question Set
4.5.4 Energy consumption in a home.

P
Animation
4.5.5 Describing the shape of data.

P
Question Set
4.5.6 Describing the shape of data.

P
Animation
4.5.7 Survivorship bias.

P
Question Set
4.5.8 Identify the type of missing data.

C
Progression
4.5.1 Performing exploratory data analysis.
4.6 Detecting outliers

outlier
An outlier is an instance that is separated from the rest of the dataset. This separation can be in a single dimension or a combination of dimensions.
leverage
The leverage of an instance describes that instance's ability to single-handedly change the parameters of a model.
high leverage point
A high leverage point is an instance with an input value that is far out in at least one feature's distribution.
influential point
An influential point is a high leverage point whose presence changes a model a lot.
Aside
Learn to:

P
Animation
4.6.1 Detecting outliers.

P
Question Set
4.6.2 Detecting outliers using graphs.

P
Animation
4.6.3 Leverage points and linear models.

P
Question Set
4.6.4 Leverage and influence.
Table
4.6.1 Outlier detection.

P
Animation
4.6.5 Detecting outliers using Tukey's fences.

P
Question Set
4.6.6 Parametric outlier detection.
Table
4.6.2 Dealing with outliers.

P
Animation
4.6.7 Causes of outliers in solar data.

P
Question Set
4.6.8 Types of outliers.

C
Progression
4.6.1 Detecting outliers.
4.7 Case study: Palmer penguins

data dictionary
A data dictionary contains feature names and descriptions for all features in a dataset.
Aside
Learn to:

P
Animation
4.7.1 Studying penguins in the Antarctic.

P
Question Set
4.7.2 Exploratory data analysis.
Table
4.7.1 Data dictionary for the Palmer penguins dataset.

P
Question Set
4.7.3 Understanding the penguins dataset.

P
Question Set
4.7.4 Identifying relationships in the penguins dataset.

P
Question Set
4.7.5 Describing the shape of features in the penguins dataset.
Table
4.7.2 Penguins with missing values for bill length.
Table
4.7.3 Penguins with missing values for sex.

P
Question Set
4.7.6 Missing values in the penguins dataset.
Table
4.7.4 Penguins with the largest bills.
Figure
4.7.1 Scatter plot of bill length and bill depth for Gentoo penguins.

P
Question Set
4.7.7 Detecting outliers in the penguins dataset.
4.8 Case study: World stock market indices

Aside
Learn to:

P
Animation
4.8.1 World stock market indices.

P
Question Set
4.8.2 Comparing NASDAQ and DOW performance in 2024.

P
Question Set
4.8.3 Comparing SSE and Nikkei performance in 2024.
Table
4.8.1 Data dictionary for the indices 2024 dataset.

P
Question Set
4.8.4 Scatter plots for the Indices 2024 data.
Figure
4.8.1 A scatter plot matrix of the indices 2024 data.

P
Question Set
4.8.5 Scatter plot matrix for the Indices 2024 data.
5. Regression

5.1 Introduction to regression

input feature
An input feature takes values without being impacted by any other features.
output feature
An output feature has values that vary in response to variation in some other feature(s).
direction
The direction of the relationship is positive if larger values of one feature correspond to larger values of the other feature. The direction of the association is negative if larger values of one feature correspond to smaller values of the other feature.
form
The form of the relationship indicates if the scatter plot follows a linear pattern or a nonlinear pattern, such as a parabola. Sometimes two features may not have an obvious form.
strength
The strength of the relationship association indicates how closely the instances in a scatter plot follow the form's pattern.
unusual instance
An unusual instance is any instance that does not follow the overall pattern.
model
A model for an output feature  using input feature(s)  is a function  that predicts an expected value of  for a given value of  as .
regression model
A regression model is a model that uses numeric output features.
residual
The residual of an instance  is the difference between the observed and predicted value .
extrapolation
An extrapolation is a prediction for a value far beyond the range of the original data and is often misleading or inaccurate.
Aside
Learn to:

P
Question Set
5.1.1 Another pair of input and output features in the cars dataset.

P
Animation
5.1.2 Properties of the horsepower and acceleration relationship.

P
Question Set
5.1.3 Describing scatter plots from the cars data.

P
Animation
5.1.4 Predicting acceleration from horsepower.

P
Question Set
5.1.5 A regression predicting miles per gallon from weight.
5.2 Simple linear regression

simple linear regression
A simple linear regression is a mathematical model of the form .
sum of squared errors
The sum of squared errors () is the sum of the squares of all residuals.
least-squares regression line
A least-squares regression line is a simple linear regression  that minimizes the sum of squared errors.
correlation coefficient
The correlation coefficient  measures the direction and strength of a linear relationship as a unitless value between -1 and 1.
Aside
Learn to:
Figure
5.2.1 Do fiddler crabs that live in higher latitudes tend to be bigger?

P
Animation
5.2.1 A simple linear regression for fiddler crabs.

P
Question Set
5.2.2 A simple linear regression for fiddler crabs.

P
Animation
5.2.3 Evaluating the fiddler crab least-squares regression.

P
Question Set
5.2.4 Another fiddler crab regression.

P
Animation
5.2.5 Examining the fiddler crab least-squares regression in more detail.

P
Question Set
5.2.6 A simple linear regression for the bad drivers dataset.

P
Question Set
5.2.7 The correlation coefficient.

C
Progression
5.2.1 Correlation and linear relationships.
5.3 Linear regression assumptions

fitted vs. residuals plot
A fitted vs. residuals plot displays the predicted values  on the horizontal axis and the residuals  on the vertical axis along with a horizontal line at .
normal Q-Q plot
A normal Q-Q plot displays the theoretical quantiles assuming normal residuals on the horizontal axis, the actual observed quantiles from the sample's residuals on the vertical axis, and a diagonal line where .
Aside
Learn to:

P
Animation
5.3.1 Linearity of the fiddler crab dataset.

P
Question Set
5.3.2 The linearity assumption for weight and miles per gallon.

P
Animation
5.3.3 Independence of residuals for the fiddler crab dataset.

P
Question Set
5.3.4 Independence of residuals for weight and miles per gallon.

P
Animation
5.3.5 Checking the constant variance assumption for the fiddler crab dataset.

P
Question Set
5.3.6 Mean and variance of residuals for weight and miles per gallon.

P
Animation
5.3.7 Normality of residuals for fiddler crab dataset.

P
Question Set
5.3.8 Normality of residuals for weight and miles per gallon.

C
Progression
5.3.1 Linear regression assumptions.
5.4 Multiple linear regression

multiple linear regression
A multiple linear regression is a mathematical model of the form .
simple polynomial regression
A simple polynomial regression is a mathematical model of the form .
polynomial regression
A polynomial regression is a mathematical model of input features that includes all powers and interaction terms of the input features up to a fixed degree.
interaction term
An interaction term is a term in a regression model that contains multiple input features, such as .
Aside
Learn to:

P
Animation
5.4.1 A multiple linear regression predicting miles per gallon.

P
Question Set
5.4.2 Interpreting the multiple linear regression predicting miles per gallon.

P
Animation
5.4.3 A simple polynomial regression predicting miles per gallon.

P
Question Set
5.4.4 Interpreting the simple polynomial regression predicting miles per gallon.

P
Animation
5.4.5 A polynomial regression predicting miles per gallon.

P
Question Set
5.4.6 Interpreting the polynomial regression predicting miles per gallon.

C
Progression
5.4.1 Multiple linear regression.
5.5 Logistic regression

logistic regression
A logistic regression is a model that predicts the probability of an outcome in a binary category using an equation of the form , where  and  are values estimated using the data.
Hot encoding
Hot encoding is transforming a categorical feature into numeric feature that equals 0 when an instance is not in the category and 1 when the instance is.
log-odds
The log-odds function is obtained by taking the natural logarithm, denoted , of the odds for the positive outcome of an experiment or study.
odds ratio
The odds ratio compares the relative odds of an outcome given a feature.
Aside
Learn to:

P
Animation
5.5.1 Parameters of the breast cancer logistic regression.

P
Question Set
5.5.2 Interpreting logistic regression parameters.
Table
5.5.1 Hot encoding the diagnosis feature from the Wisconsin breast cancer diagnosis dataset.

P
Question Set
5.5.3 Predicting whether a tumor is malignant or benign using a logistic regression model.

P
Animation
5.5.4 Logistic regression and log-odds.

P
Question Set
5.5.5 Log-odds.

C
Progression
5.5.1 Logistic regression.
5.6 Case study: Energy consumption

Aside
Learn to:
Figure
5.6.1 Visualizing natural gas use.

P
Question Set
5.6.1 Residential natural gas use.
Figure
5.6.2 Modeling natural gas use.

P
Question Set
5.6.2 Modeling natural gas use.
Figure
5.6.3 Residual plots for the natural gas model.

P
Question Set
5.6.3 Evaluating the natural gas model.

P
Question Set
5.6.4 Multiple regression for gas usage.
5.7 Case study: Customer churn

Aside
Learn to:

P
Question Set
5.7.1 Exploring customer churn.
Figure
5.7.1 Logistic regression models for customer churn.

P
Question Set
5.7.2 Logistic regression model.
Figure
5.7.2 Scatterplots of account balance, age, and credit score by churn.

P
Question Set
5.7.3 Multiple logistic regression model.
6. Evaluating Model Performance

6.1 Model error

underfit
A model is underfit if the model is too simple to fit the data well.
overfit
A model is overfit if the model is too complex, fitting the data too closely and incorporating too much noise (meaningless variation).
total error
The total error of a model is how much the observed values differ from predicted values.
Bias
Bias is how much the model's prediction differs from the observed values due to the assumptions built into the model.
Variance
Variance is a measure of how spread out predictions from the model are.
Irreducible error
Irreducible error is error inherent to the situation modeled.
metric
A metric is a numeric value that evaluates how closely a model fits the sample data.
Aside
Learn to:

P
Animation
6.1.1 Overfitting and underfitting the tortoise data.

P
Question Set
6.1.2 Overfits and underfits.
Figure
6.1.1 Bias and variance.

P
Question Set
6.1.3 Breaking down total error.

P
Animation
6.1.4 Bias-variance tradeoff.

P
Question Set
6.1.5 Bias-variance tradeoff.

C
Progression
6.1.1 Model error.
6.2 Training, validation, and test sets

Machine learning algorithms
Machine learning algorithms use data to build a model that makes predictions.
Model training
Model training is the process of estimating model parameters used to make a prediction.
Training data
Training data is used to fit a model.
Validation data
Validation data is used to evaluate model performance, adjust parameters or model settings, and conduct feature selection.
Test data
Test data is used to evaluate final model performance and compare different models.
Aside
Learn to:

P
Animation
6.2.1 Model training.

P
Question Set
6.2.2 Model training.

P
Animation
6.2.3 Splitting the bad drivers data into training, validation, and test sets.

P
Question Set
6.2.4 Splitting data.
Figure
6.2.1 Two different ratios for the training-validation-test split.

P
Question Set
6.2.5 Determining the data split ratio.

C
Progression
6.2.1 Training, validation, and test sets.
6.3 Loss functions for regression

loss function
A loss function quantifies the difference between a model's predictions and the observed values.
regression metric
A regression metric is the observed value of a loss function for a fitted regression model.
mean squared error
The mean squared error () is the average of the squared differences between observed and predicted values.
root mean squared error
The root mean squared error () is the square root of the average of the squared differences between observed and predicted values.
mean absolute error
The mean absolute error () is the average of the absolute values of the differences between observed and predicted values.
Aside
Learn to:
Table
6.3.1 Common loss functions for regression.

P
Animation
6.3.1 Comparing model performance using a loss function.

P
Question Set
6.3.2 Loss functions for regression.

P
Animation
6.3.3 Comparing  and  for two tortoise regressions.

P
Question Set
6.3.4 Exploring  and  for the linear and quadratic models.

P
Animation
6.3.5  and unusual instances.

P
Question Set
6.3.6 Exploring the values of  and  for the linear and quadratic models.

C
Progression
6.3.1 Loss functions for regression.
6.4 Loss functions for classification

classification metric
A classification metric is the observed value of a loss function for a fitted classification model.
log loss
The log loss is the negative log-likelihood of a probability predicted by a logistic model.
Aside
Learn to:

P
Animation
6.4.1 Interpreting loss in classification tasks.

P
Question Set
6.4.2 Interpreting loss in classification tasks.

P
Animation
6.4.3 Absolute loss of the breast cancer logistic regression.

P
Question Set
6.4.4 Interpreting and calculating absolute loss.

P
Animation
6.4.5 Log loss of the breast cancer logistic regression.

P
Question Set
6.4.6 Calculating the log loss.
6.5 Binary classification metrics

true positive
A true positive () is an outcome that was correctly identified as positive.
true negative
A true negative () is an outcome that was correctly identified as negative.
false positive
A false positive () is an outcome that was identified as positive but was actually negative.
false negative
A false negative () is an outcome that was identified as negative but was actually positive.
confusion matrix
A confusion matrix is a table that summarizes the combinations of predicted and actual values.
accuracy
The accuracy of a classifier is the proportion of predictions that were correct.
precision
The precision of a classifier is the proportion of positive predictions that were correct.
recall
The recall of a classifier is the proportion of positives that were correctly predicted.
ROC curve
An ROC curve measures how well a classification model distinguishes between binary classes at various probability cutoffs by plotting the true positive rate (recall) vs the false positive rate.
area under the ROC curve / AUC
The area under the ROC curve or AUC is a metric used to compare the performance between two binary classification models.
Aside
Learn to:
Table
6.5.1 Results from a rapid COVID-19 test.

P
Question Set
6.5.1 Results from the rapid COVID-19 test.

P
Animation
6.5.2 Accuracy, precision, and recall for the rapid COVID-19 test.

P
Question Set
6.5.3 Calculating accuracy, precision, and recall.

P
Question Set
6.5.4 Comparing two rapid COVID-19 tests.

P
Question Set
6.5.5 Precision-recall tradeoff for the breast cancer logistic regression.

P
Animation
6.5.6 ROC and AUC of a logistic model classifying a tumor as malignant or benign.

P
Question Set
6.5.7 ROC and AUC.

C
Progression
6.5.1 Binary classification metrics.
6.6 Cross-validation

Cross-validation
Cross-validation refers to resampling methods that use different portions of the sample data to train and validate a model.
-fold cross-validation
-fold cross-validation is a method of evaluating model performance where, after separating out test data, sample data is split into  groups (folds) and the model is trained and validated repeatedly using these groups.
leave-one-out cross-validation (LOOCV)
A -fold cross-validation where  is called a leave-one-out cross-validation (LOOCV).
exhaustive cross-validation
An exhaustive cross-validation uses every possible way to divide the sample into training and validation sets of desired sizes.
non-exhaustive cross-validation
A non-exhaustive cross-validation does not use every possible way to divide the sample into training and validation sets of desired sizes.
Aside
Learn to:

P
Animation
6.6.1 A 5-fold cross-validation.

P
Question Set
6.6.2 A 10-fold cross validation for the bad drivers data.

P
Animation
6.6.3 -fold cross-validation for two different values of .

P
Question Set
6.6.4 Comparing choices of .

P
Animation
6.6.5 A 10-fold cross-validation is non-exhaustive for the bad drivers data.

P
Question Set
6.6.6 Exhaustive vs. non-exhaustive cross-validations.

P
Question Set
6.6.7 Other types of cross-validations.

C
Progression
6.6.1 Cross-validation.
6.7 Bootstrap method

Bootstrapping
Bootstrapping is the process of generating simulated samples by repeatedly drawing with replacement from an existing sample.
bootstrap method of model evaluation
The bootstrap method of model evaluation is a method in which repeated sampling with replacement is used to generate a distribution of errors estimating how well a model fits the overall population.
Aside
Learn to:

P
Animation
6.7.1 Bootstrap sampling.

P
Question Set
6.7.2 Bootstrapping.
Process
6.7.1 Bootstrap method of model evaluation.

P
Animation
6.7.3 Bootstrap method for the bad drivers data.

P
Question Set
6.7.4 The bootstrap method.

C
Progression
6.7.1 Bootstrap method.
6.8 Comparing models

Model selection
Model selection is the process of choosing a model that best generalizes a population or process from a list of candidate models.
one-standard error method
The one-standard error method for model selection is to find the model with the minimum mean score, then select the simplest model whose mean score falls within one standard deviation.
Information criterion
Information criterion is a numerical measure of a model that considers how well the model fits the data and the complexity of the model.
adjusted R-squared
The adjusted R-squared () is a modified version of the coefficient of determination () that takes the number of features into account, losing the proportion interpretation in exchange.
Aside
Learn to:

P
Animation
6.8.1 Selecting a model using the 1SE method.

P
Question Set
6.8.2 Selecting a model from an errorbar plot.

P
Question Set
6.8.3 Model selection.

P
Animation
6.8.4 Selecting a multiple regression using alternative methods.

P
Question Set
6.8.5 Selecting a bad drivers model using information criteria.

C
Progression
6.8.1 Comparing models.
6.9 Case study: Home prices

Aside
Learn to:
Figure
6.9.1 Home prices for the training and test sets.

P
Question Set
6.9.1 Training and test split for home prices.
Figure
6.9.2 Fitted simple linear regression model on training and test sets.
Table
6.9.1 Metrics for simple linear regression on training and test sets.

P
Question Set
6.9.2 Evaluating the simple linear regression model.
Figure
6.9.3 Predicted vs. observed home prices for simple linear regression model and multiple linear regression model.
Table
6.9.2 Metrics for multiple linear regression on training and test set.

P
Question Set
6.9.3 Evaluating the multiple linear regression model.
Table
6.9.3 Evaluation metrics for simple linear regression model and multiple linear regression model.

P
Question Set
6.9.4 Comparing models.
Figure
6.9.4 Cross-validation mean squared error for linear and multiple regression models.

P
Question Set
6.9.5 Cross-validation for predicting home prices.
6.10 Case study: Credit risk

penalty matrix
A penalty matrix allows the metric to assign different penalties for each type of error.
Aside
Learn to:

P
Question Set
6.10.1 The German credit dataset.
Figure
6.10.1 Accuracy plot.

P
Question Set
6.10.2 Accuracy.
Figure
6.10.2 Penalty matrix.
Figure
6.10.3 Average penalty plot.

P
Question Set
6.10.3 Penalty matrix.
Figure
6.10.4 Confusion matrix.

P
Question Set
6.10.4 Final model.

P
Question Set
6.10.5 Final model performance.
7. Supervised Learning

7.1 Introduction to supervised learning

labeled
An instance is labeled if the output feature's value is known for that instance.
Supervised learning
Supervised learning is training a model to predict a labeled output feature based on input features.
Regression
Regression is the supervised learning process of training a model to predict a numerical output.
Classification
Classification is the supervised learning process of training a model to predict a categorical output feature.
interpretable
A model is interpretable if the relationship between input and output features in the model are easy to explain.
predictive
A model is predictive if the outputs produced by the model match the actual outputs with new data.
Aside
Learn to:

P
Animation
7.1.1 Supervised learning.

P
Question Set
7.1.2 Output or input feature.

P
Animation
7.1.3 Regression to predict house prices.

P
Question Set
7.1.4 Identifying regression problems.

P
Animation
7.1.5 Classification to predict the condition of houses.

P
Question Set
7.1.6 Identifying classification problems.

P
Animation
7.1.7 Choosing algorithms for interpretability.

P
Question Set
7.1.8 Interpretability requirements.

C
Progression
7.1.1 Supervised learning.
7.2 K-nearest neighbors

k-nearest neighbors
K-nearest neighbors (kNN) is a supervised learning algorithm that predicts the output feature of a new instance using other instances that are close for certain input features.
metric
A metric is a method of determining the distance between two instances.
Aside
Learn to:

P
Animation
7.2.1 Identifying beans using dimensions.

P
Question Set
7.2.2 Identifying groups from nearby points.

P
Animation
7.2.3 Finding the nearest neighbors.

P
Question Set
7.2.4 Finding the nearest neighbors.
Algorithm
7.2.1 Classification with k-nearest neighbors.

P
Animation
7.2.5 Classifying beans with kNN.

P
Question Set
7.2.6 Classifying with k-nearest neighbors.

P
Question Set
7.2.7 Classifying beans with kNN.
Algorithm
7.2.2 Regression with k-nearest neighbors.

P
Animation
7.2.8 Predicting a bean's area.

P
Question Set
7.2.9 kNN regression.

C
Progression
7.2.1 K-nearest neighbors.
7.3 Naive Bayes classification

Naive Bayes classification
Naive Bayes classification is a supervised learning classifier that uses the number of times a category occurs in each possible class to estimate the likelihood an instance is in the class.
likelihood
The top of these expressions is called the likelihood and is proportional to the conditional probability for each class.
Laplace smoothing
Laplace smoothing adds one fictional occurrence to each proportion when calculating the likelihood.
Aside
Learn to:
Table
7.3.1 Advantages and disadvantages of a naive Bayes classification.

P
Animation
7.3.1 Using naive Bayes to identify poster.

P
Question Set
7.3.2 Identifying posting patterns.

P
Animation
7.3.3 Naive Bayes calculation visually.

P
Question Set
7.3.4 Estimating naive Bayes likelihood.
Algorithm
7.3.1 Classification with naive Bayes.

P
Animation
7.3.5 Naive Bayes classifying a post.

P
Question Set
7.3.6 Calculating likelihoods.

P
Animation
7.3.7 Naive Bayes with Laplace smoothing.

P
Question Set
7.3.8 Calculating likelihoods with Laplace smoothing.

P
Animation
7.3.9 Naive assumption impacts.

P
Question Set
7.3.10 Effects of the naive assumption.

C
Progression
7.3.1 Naive Bayes for spam detection.
7.4 Support vector machines

support vector machine
A support vector machine (SVM) is a supervised learning algorithm that uses hyperplanes to divide data into different classes.
hyperplane
A hyperplane is a flat surface that is one dimension lower than the input feature space.
well-separated
A dataset is well-separated if a hyperplane can divide the dataset so that all the instances of one class fall on one side of the hyperplane, and all instances not in that class fall on the other side.
margin
The margin is the space between the hyperplanes parallel to the dividing hyperplane that go through the dividing hyperplane's closest instances.
support vectors
The closest instances to the hyperplane are the hyperplane's support vectors.
hinge function
A hinge function is zero on one side of an input threshold and increases linearly on the other side.
kernel
A kernel is a special mapping that works well with the optimization algorithms to find the best hyperplane in the higher dimensional space.
Aside
Learn to:
Table
7.4.1 Advantages and disadvantages of support vector machine classification.

P
Animation
7.4.1 Classifying penguins by species using SVM.

P
Question Set
7.4.2 Identifying hyperplanes.

P
Animation
7.4.3 SVM for separating Gentoo penguins.

P
Question Set
7.4.4 Maximizing the margin.

P
Animation
7.4.5 SVM when classes overlap.

P
Question Set
7.4.6 Support vector machine terminology.
Table
7.4.2 Commonly used kernels.

P
Animation
7.4.7 Mapping up to higher dimensions.

P
Question Set
7.4.8 Support vector machine kernel boundaries.

C
Progression
7.4.1 Support vector machines.
7.5 Case study: Classifying cells

decision boundary
The decision boundary of a classification model is the edge or edges separating the classes.
hyperparameter
A hyperparameter is a value that defines a specific variant on a machine learning model.
Aside
Learn to:

P
Animation
7.5.1 Benign cells vs. malignant cells.

P
Question Set
7.5.2 Cell classifications.
Figure
7.5.1 Boxplots of cell type by cell radius, smoothness, and area.

P
Question Set
7.5.3 Exploring features in the breast cancer dataset.

P
Question Set
7.5.4 Effect of k on a decision boundary.
Table
7.5.1 Accuracy, precision, and recall on training data for support vector classifiers with linear, radial, and polynomial kernels.

P
Question Set
7.5.5 Support vector classification.
Table
7.5.2 Accuracy and recall on the testing dataset for six classification models.

P
Question Set
7.5.6 Comparing classification models on the testing dataset.
7.6 Case study: Estimating annual precipitation

Great-circle distance
Great-circle distance calculates the distance between two geographic locations using longitude and latitude, accounting for the Earth's curvature.
Aside
Learn to:

P
Animation
7.6.1 Annual precipitation data.

P
Question Set
7.6.2 Average annual precipitation in the US.
Figure
7.6.1 Nearest neighbors for Gainesville, FL, Ames, IA, and Moorhead, MN.

P
Question Set
7.6.3 Predicting average annual precipitation with k-nearest neighbors.
Table
7.6.1 Nearest neighbors using Euclidean vs. great-circle distance.

P
Question Set
7.6.4 k-nearest neighbors using Euclidean vs. great-circle distance.
Figure
7.6.2 Predicted average annual precipitation using different values of k.
Table
7.6.2 Summary statistics for predicted average annual precipitation using different values of k.

P
Question Set
7.6.5 Comparing values of k.
8. Unsupervised Learning

8.1 Introduction to unsupervised learning

Unsupervised learning
Unsupervised learning uses machine learning techniques to identify patterns in data without any prior knowledge about the data.
clustering algorithm
A clustering algorithm groups instances with similar features.
outlier detection algorithm
An outlier detection algorithm identifies deviations within data.
latent variable model
A latent variable model relates observable features to a set of latent or unobservable variables.
Aside
Learn to:
Table
8.1.1 Types of unsupervised learning algorithms.

P
Animation
8.1.1 Unsupervised learning.

P
Question Set
8.1.2 Identifying types of unsupervised learning algorithms.

P
Animation
8.1.3 Customer segmentation.

P
Question Set
8.1.4 Customer segmentation.

P
Animation
8.1.5 Outliers in housing data.

P
Question Set
8.1.6 Outliers in housing data.

P
Animation
8.1.7 Latent variables that model overall well-being.

P
Question Set
8.1.8 Latent variables that model overall well-being.

C
Progression
8.1.1 Introduction to unsupervised learning.
8.2 K-means clustering

cluster
A cluster is a set of instances with similar characteristics.
clustering
Grouping instances into classes with similar characteristics is called clustering.
centroid
A centroid is a point that represents the center of each cluster.
elbow method / within-cluster sum of squares / WCSS
The elbow method plots the sum of the square distances of instances to the closest centroid, known as within-cluster sum of squares or WCSS, for each value of .
Aside
Learn to:

P
Animation
8.2.1 Centroid clustering.

P
Question Set
8.2.2 Clustering.

P
Animation
8.2.3 Old Faithful eruption times.

P
Question Set
8.2.4 Old Faithful eruption times.
Algorithm
8.2.1 -means clustering.

P
Animation
8.2.5 -means clustering.

P
Question Set
8.2.6 -means clustering.

P
Animation
8.2.7 Using the elbow method on the Old Faithful data.

P
Question Set
8.2.8 Elbow method.

C
Progression
8.2.1 K-means clustering.
8.3 Hierarchical clustering

Hierarchical clustering
Hierarchical clustering groups instances into a hierarchy of clusters where one end is a single cluster that contains all instances and at the other end are clusters that contain just one instance.
Agglomerative hierarchical clustering
Agglomerative hierarchical clustering is a clustering method where each instance is treated as an individual cluster, and two clusters are combined iteratively until all instances belong to a single cluster. Since agglomerative clustering is less computationally complex, this section will primarily focus on this technique.
Divisive hierarchical clustering
Divisive hierarchical clustering is a clustering method where all instances belong to a single cluster, and each cluster is split into two clusters iteratively until all clusters just contain a single instance.
single linkage
The single linkage method calculates the distance between a pair of instances, one from each cluster, that are the most similar.
complete linkage
The complete linkage method calculates the distance between a pair of instances, one from each cluster, that are the most different.
centroid linkage
The centroid linkage method calculates the distance between the centroids of two clusters.
dendrogram
A dendrogram is a tree that shows the order in which clusters are grouped together and the distances between clusters.
clade
A clade is a branch of a dendrogram or a vertical line.
link
A link is a horizontal line that connects two clades, whose height gives the distance between clusters.
leaf
A leaf is the terminal end of each clade in a dendrogram, which represents a single instance.
Aside
Learn to:

P
Animation
8.3.1 Agglomerative vs. divisive clustering.

P
Question Set
8.3.2 Introduction to hierarchical clustering.

P
Animation
8.3.3 Computing similarity.

P
Question Set
8.3.4 Measuring similarity.
Figure
8.3.1 Parts of a dendrogram.

P
Animation
8.3.5 Forming a dendrogram.

P
Question Set
8.3.6 Interpreting a dendrogram.

P
Animation
8.3.7 Determining the number of clusters using a threshold.

P
Question Set
8.3.8 Determining the number of clusters given a threshold.

P
Animation
8.3.9 Forming a dendrogram for the amino acid differences in the cytochrome c protein between species.

P
Question Set
8.3.10 Interpreting the dendrogram for the cytochrome c amino acid sequence data.

C
Progression
8.3.1 Hierarchical clustering.
8.4 Detecting outliers using DBSCAN

Density-based spatial clustering of applications with noise / DBSCAN
Density-based spatial clustering of applications with noise, or DBSCAN, is an algorithm that groups together points in high-density, connected regions.
epsilon neighborhood / ε-neighborhood
An epsilon neighborhood, or ε-neighborhood, of a point is a spherical region of radius  centered at that point.
core point
A core point is a point whose ε-neighborhood contains a given minimum number of points.
border point
A border point is a point that is not a core point but is contained in an ε-neighborhood of a core point.
outlier
An outlier is a point that is neither a core point, nor a border point.
Aside
Learn to:
Table
8.4.1 Advantages and disadvantages of DBSCAN.

P
Animation
8.4.1 DBSCAN vs. k-means clustering.

P
Question Set
8.4.2 Density-based clustering.

P
Animation
8.4.3 DBSCAN terminology.

P
Question Set
8.4.4 DBSCAN terminology.
Algorithm
8.4.1 DBSCAN.

P
Animation
8.4.5 DBSCAN algorithm.

P
Question Set
8.4.6 DBSCAN algorithm.

P
Animation
8.4.7 Outliers in housing data.

P
Question Set
8.4.8 Outliers in housing data.

C
Progression
8.4.1 Clustering with DBSCAN.
8.5 Analyzing factors

Factor analysis / factors / components
Factor analysis is a statistical method that explains the variance of observable data using a set of potentially fewer latent variables, also called factors or components.
factor loading
The factor loading  is a coefficient indicating the influence that factor  has on the feature .
Common variance
Common variance is the amount of variance in a given feature explained by all of the factors.
Communality / 
Communality, or , is the term used when the common variance is between  and  and is equal to the sum of the square factor loadings.
Unique variance
Unique variance is the amount of variance that is not shared between a set of observed features and may come from measurement error or reasons specific to the feature.
Aside
Learn to:
Figure
8.5.1 Rock permeability in petroleum engineering.

P
Animation
8.5.1 Correlation between features in the rocks dataset.

P
Question Set
8.5.2 Correlation between features in the rock dataset.

P
Animation
8.5.3 Model representation.

P
Question Set
8.5.4 Model representation for the rock dataset.

P
Animation
8.5.5 Communality and unique variance for area.

P
Question Set
8.5.6 Variance in the rock factor model.

C
Progression
8.5.1 Analyzing factors.
8.6 Analyzing factors using PCA

Factor extraction
Factor extraction transforms features into uncorrelated factors with corresponding loadings.
Factor rotation
Factor rotation rotates the axes to make subsequent analysis easier.
Principal component analysis / PCA
Principal component analysis, or PCA, is a factor analysis technique used to find orthogonal components and factor loadings so that each successive component contains the maximum possible variability.
eigenvalue
An eigenvalue for a factor gives the variability in all features explained by that factor.
eigenvector
An eigenvector is a vector formed by the coefficients of the input features.
scree plot
A scree plot is a line plot of eigenvalues used to select which factors should be used in a model.
Aside
Learn to:

P
Animation
8.6.1 Principal component analysis.

P
Question Set
8.6.2 Principal component analysis.

P
Animation
8.6.3 Eigenvalues associated with the factors in the rock dataset.

P
Question Set
8.6.4 Eigenvalues for the factors in the rock dataset.

P
Animation
8.6.5 Eigenvectors and loadings in the factor model for the rock dataset.

P
Question Set
8.6.6 Eigenvectors.

P
Animation
8.6.7 Using a scree plot to select the number of factors to model the rock data.

P
Question Set
8.6.8 Using scree plots to select factors in a model.

C
Progression
8.6.1 Principal components.
8.7 Case study: Travel reviews

Aside
Learn to:

P
Animation
8.7.1 Personal bias in average travel ratings.

P
Question Set
8.7.2 Learning from travel ratings.
Table
8.7.1 Eigenvalues for travel ratings.
Table
8.7.2 Correlation matrix for destination types and first two principal components (PC1 and PC2).

P
Question Set
8.7.3 Principal components for travel ratings.

P
Question Set
8.7.4 Interpreting travel rating clusters.
Figure
8.7.1 Scatter plot of restaurant ratings and beach ratings grouped by outlier status.

P
Question Set
8.7.5 Identifying outliers in the travel ratings dataset.
8.8 Case study: Cardiovascular health

silhouette method
The silhouette method calculates the silhouette coefficient for each instance, and the value of  with the highest mean silhouette score gives the optimal number of clusters.
Aside
Learn to:

P
Animation
8.8.1 Overview of the NHANES data.

P
Question Set
8.8.2 NHANES data.

P
Animation
8.8.3 Creating the cardioFinal dataset.

P
Question Set
8.8.4 NHANES data.
Table
8.8.1 Features of the cardioFinal dataset.

P
Question Set
8.8.5 Applying k-means clustering.
Figure
8.8.1 Elbow and silhouette plots.

P
Question Set
8.8.6 Selecting .

P
Question Set
8.8.7 Understanding clusters.
9. Decision Trees

9.1 Introduction to decision trees

decision tree
A decision tree is a set of questions that check if a condition is met and flow from one into the other to make a decision.
Decision node
Decision node: where a feature of the data is tested.
Root node
Root node: the first decision node in the tree.
Branch
Branch: a connection between decision nodes in the tree.
Layer
Layer: all of the decision nodes that are the same distance from the root node.
Leaf node
Leaf node: a node that does not test a feature and so is where a decision is made.
Depth
Depth: the number of layers in a decision tree.
binary decision tree
A binary decision tree is a decision tree in which each node has two branches.
classification tree
A classification tree is a decision tree used for classifying an object or event into a categorical feature.
regression tree
A regression tree is a decision tree used to estimate or predict the value of a numerical feature.
Aside
Learn to:

P
Animation
9.1.1 Decision tree for accepting a current job offer.

P
Question Set
9.1.2 Decision tree.

P
Animation
9.1.3 Classification tree for mobile ads.

P
Question Set
9.1.4 Interpreting classification trees.

P
Animation
9.1.5 Real estate price estimation.

P
Question Set
9.1.6 Decision tree applications.

C
Progression
9.1.1 Decision trees.
9.2 Regression trees

regression tree
A regression tree is a model to predict a numerical value from a decision tree.
Classification and Regression Tree algorithm (CART)
Classification and Regression Tree algorithm (CART) is a method used to build trees by repeatedly splitting data with a threshold into two regions.
threshold
A threshold is a numerical value that divides a feature into two parts: values above the threshold and below.
Aside
Learn to:
Table
9.2.1 Advantages of a regression tree over linear regression.

P
Animation
9.2.1 Predicting house prices based on house size.

P
Question Set
9.2.2 Predicting house prices based on house size.
Algorithm
9.2.1 CART algorithm for regression.

P
Animation
9.2.3 Building a regression tree using CART.

P
Question Set
9.2.4 Interpreting a regression tree.

P
Animation
9.2.5 Regression tree depth and housing prices.

P
Question Set
9.2.6 Predicting house price based on year.
Example
9.2.1 Predicting penguin weights with a regression tree.

P
Question Set
9.2.7 Interpreting a regression tree.

P
Question Set
9.2.8 Penguin body feature regression tree.

C
Progression
9.2.1 Regression trees.
9.3 Classification trees

classification tree
A classification tree is a model used to predict a categorical value from a decision tree.
Gini index
The Gini index is a measure of misclassification that varies between 0 and 1, where 0 implies a pure split and 0.5 implies an equal distribution of instances among different classes.
Classification and Regression Tree (CART)
Classification and Regression Tree (CART) is a method used to build trees by repeatedly splitting data into two regions.
Aside
Learn to:
Table
9.3.1 Advantages and disadvantages of a classification tree.

P
Animation
9.3.1 Classification tree for Cali and Sira beans.

P
Question Set
9.3.2 Classifying Sira and Cali beans.

P
Animation
9.3.3 Classification tree for dry beans.

P
Question Set
9.3.4 Classification trees with more than two categories.

P
Animation
9.3.5 Calculating the Gini index.

P
Question Set
9.3.6 Calculating the Gini index.
Algorithm
9.3.1 CART algorithm.

P
Animation
9.3.7 Selecting a threshold based on Gini index.

P
Question Set
9.3.8 Classification based on the Gini index.

P
Animation
9.3.9 Classification with CART algorithm.

P
Question Set
9.3.10 Interpreting a classification tree.

P
Question Set
9.3.11 Penguin classification trees.

C
Progression
9.3.1 Classification trees.
9.4 Random forests

random forest
A random forest is a collection of many decision trees.
Aside
Learn to:

P
Animation
9.4.1 Constructing a random forest classifier.

P
Question Set
9.4.2 Understanding random forest classifiers.

P
Animation
9.4.3 Constructing a random forest regressor.

P
Question Set
9.4.4 Random forest regressor.

C
Progression
9.4.1 Random forests.
9.5 Case study: Marijuana legalization

Feature importance
Feature importance is a measure of the average impurity decrease within each decision tree of a random forest.
Aside
Learn to:

P
Animation
9.5.1 History of marijuana legalization in the General Social Survey.

P
Question Set
9.5.2 Marijuana legalization in the United States.
Figure
9.5.1 Exploring the GSS dataset.

P
Question Set
9.5.3 Exploring the GSS dataset.
Figure
9.5.2 Decision tree (depth=2) for supporting marijuana legalization.

P
Question Set
9.5.4 Decision tree for marijuana support.

P
Question Set
9.5.5 Expanded decision tree for marijuana support.
Figure
9.5.3 Feature importance plot for supporting marijuana legalization.

P
Question Set
9.5.6 Feature importance in a random forest.
10. Artificial Neural Networks

10.1 Introduction to artificial neural networks

neuron
A neuron is a nerve cell that carries messages throughout the body.
cell body
The cell body contains the nucleus, which has genetic information, maintains cellular function, and provides energy to the neuron.
axon
The axon is the long, thin part of the neuron in which electrical signals travel.
dendrite
The dendrite receives chemical information and determines whether an electrical signal is produced.
action potential
An action potential is an electrical signal that travels through a single neuron.
neurotransmitter
A neurotransmitter is a chemical released at the axon terminals of one neuron to the receptors of another neuron.
threshold potential
The threshold potential is the electric potential needed to initiate an action potential.
artificial neural network / ANN
An artificial neural network or ANN is a collection of neurons or nodes arranged in multiple layers.
input layer
The input layer takes data from different input features or features to other layers.
hidden layer
A hidden layer assigns weights to inputs and produces numerical outputs from a function.
output layer
The output layer produces an output such as a class or an alphanumeric character.
Aside
Learn to:

P
Animation
10.1.1 Parts of a neuron.

P
Question Set
10.1.2 Parts of a neuron.

P
Animation
10.1.3 How neurons send electrical and chemical signals.

P
Question Set
10.1.4 Action potentials and neurotransmitters.

P
Animation
10.1.5 Determining whether to go to the beach.

P
Question Set
10.1.6 Determining whether to go to the beach.

P
Animation
10.1.7 Layers of an artificial neural network.

P
Question Set
10.1.8 Layers of an artificial neural network.

C
Progression
10.1.1 Artificial neural networks.
10.2 Single-layer perceptron

single-layer perceptron
A single-layer perceptron is a neural network used for binary classification.
binary classifier
A binary classifier groups data into one of two classes.
Bias
Bias is a term added to the weighted sum to improve the perceptron's accuracy.
activation function
An activation function gives the output for a perceptron.
epoch
An epoch is an iteration of weight updates over all instances in the training data.
Aside
Learn to:

P
Animation
10.2.1 Parts of a perceptron.

P
Question Set
10.2.2 Perceptrons.

P
Animation
10.2.3 Interpretation of the weighted sum.

P
Question Set
10.2.4 Perceptron model for an AND gate.
Figure
10.2.1 Perceptron that has a bias term.

P
Animation
10.2.5 Interpretation of a bias term.

P
Question Set
10.2.6 Perceptron model with a bias term for an AND gate.

P
Animation
10.2.7 Unit step function.

P
Question Set
10.2.8 Applying the unit step function to a weighted sum for an AND gate.
Algorithm
10.2.1 Algorithm for training a perceptron.

P
Animation
10.2.9 Training a perceptron model for an AND gate.

P
Question Set
10.2.10 Training a perceptron model for an AND gate.

C
Progression
10.2.1 Single-layer perceptron.
10.3 Nonlinear activation functions

sigmoid
A sigmoid is a function that takes in any real value as input and returns a real number between 0 and 1 as output.
hyperbolic tangent
A hyperbolic tangent is a function that takes in any real value as input and returns a real number between -1 and 1 as output.
rectified linear unit / ReLU
The rectified linear unit, or ReLU, is a function that takes in any real value as input and returns either 0 or the input, whichever is greater.
leaky ReLU
The leaky ReLU is a function with a small slope when the input value is negative.
softmax
A softmax function takes in a vector and returns a vector with the same number of components as output.
Aside
Learn to:

P
Animation
10.3.1 Why use nonlinear activation functions?

P
Question Set
10.3.2 Multilayer perceptron with nonlinear activation functions.

P
Animation
10.3.3 Sigmoid.

P
Question Set
10.3.4 Sigmoid.

P
Animation
10.3.5 Hyperbolic tangent.

P
Question Set
10.3.6 Hyperbolic tangent.

P
Animation
10.3.7 ReLU and leaky ReLU.

P
Question Set
10.3.8 ReLU and leaky ReLU.

P
Animation
10.3.9 Using the softmax function.

P
Question Set
10.3.10 Softmax.

P
Animation
10.3.11 Determining which activation function to use.

P
Question Set
10.3.12 Determining which activation function should be used.

C
Progression
10.3.1 Nonlinear activation functions.
10.4 Multilayer perceptron

feed-forward network
A feed-forward network is a network where connections between neurons do not form a cycle.
multilayer perceptron
A multilayer perceptron is a type of feed-forward neural network with at least one hidden layer containing multiple neurons.
Forward propagation
Forward propagation is the step where inputs are fed into the neural network, and outputs from neurons are passed in one direction from one layer to each successive layer.
Backward propagation / backpropagation
Backward propagation or backpropagation is the process of iteratively adjusting the weights in the network to minimize prediction errors.
loss function
A loss function measures the error in a neural network.
loss curve
A loss curve measures the model error as the training of the neural network progresses.
Aside
Learn to:

P
Animation
10.4.1 Multilayer perceptron model.

P
Question Set
10.4.2 Multilayer perceptron.

P
Animation
10.4.3 Using loss curves to diagnose model performance.

P
Question Set
10.4.4 Loss functions and curves.

C
Progression
10.4.1 Multilayer perceptron.
10.5 Case study: Bike share demand

Time series data
Time series data is collected over an extended time period and is affected by changes over time.
Seasonal effects
Seasonal effects describe patterns that repeat over time.
confounded
Features in a dataset are confounded if the features measure the same information but in a slightly different way.
Aside
Learn to:

P
Animation
10.5.1 Predicting bike share demand.

P
Question Set
10.5.2 Exploring bike share demand.
Figure
10.5.1 Day, month, and season features in the bike share dataset.

P
Question Set
10.5.3 Exploring features in the bike share dataset.
Figure
10.5.2 Multilayer perceptron predictions vs. actual values.

P
Question Set
10.5.4 Evaluating the multilayer perceptron.
Figure
10.5.3 Confusion matrices for classifiers on training dataset.
Figure
10.5.4 Confusion matrices for classifiers on testing dataset.

P
Question Set
10.5.5 Evaluating activation functions.
11. Ensemble Techniques

11.1 Introduction to ensemble models

ensemble model
An ensemble model combines predictions from different models, often with a single input feature, to create a stronger combined model.
base models
The individual models used in an ensemble model are called base models.
Sequential ensemble models
Sequential ensemble models fit base models one at a time, updating the dataset and predictions after each iteration.
Parallel ensemble models
Parallel ensemble models fit base models separately before combining predictions into a final ensemble model.
Aside
Learn to:

P
Animation
11.1.1 Visualizing an ensemble model.

P
Question Set
11.1.2 Ensemble models.

P
Animation
11.1.3 Types of ensemble models.

P
Question Set
11.1.4 Types of ensemble models.

P
Animation
11.1.5 Making predictions using ensemble models.

P
Question Set
11.1.6 Ensemble classification models.

C
Progression
11.1.1 Ensemble models.
11.2 Boosting

Boosting
Boosting is a sequential ensemble technique. In boosting, predictions from each base model are used to update weights in the dataset before fitting the next base model.
AdaBoost
AdaBoost, or adaptive boosting, is a sequential boosting technique that does not require a specific number of base models. Instead, AdaBoost repeats until a maximum number of base models has been used or the error function no longer changes.
Aside
Learn to:
Table
11.2.1 Advantages and disadvantages of boosting.

P
Animation
11.2.1 Boosting application: hepatitis C.

P
Question Set
11.2.2 Boosting model for flight delays.
Algorithm
11.2.1 Adaptive boosting algorithm.

P
Animation
11.2.3 Calculating weights in AdaBoost for classification.

P
Question Set
11.2.4 Calculating and updating weights in AdaBoost.

C
Progression
11.2.1 Adaptive boosting.
11.3 Bagging

Bagging
Bagging is an ensemble technique that fits and combines multiple base models with the same structure in parallel.
Bootstrapping
Bootstrapping is the generation of simulated samples by repeatedly drawing with replacement from an existing sample.
Out-of-bag instances
Out-of-bag instances are instances that are not included in a bootstrap random sample.
Aside
Learn to:
Table
11.3.1 Advantages and disadvantages of bagging.

P
Animation
11.3.1 Bagging application: hepatitis C.

P
Question Set
11.3.2 Bagging application.
Algorithm
11.3.1 Bagging algorithm.

P
Animation
11.3.3 Bootstrapping and bagging.

P
Question Set
11.3.4 Bagging, bias, and variance.

P
Animation
11.3.5 Out-of-bag accuracy.

P
Question Set
11.3.6 Out-of-bag prediction error.
11.4 Stacking

Stacking
Stacking is an ensemble method that uses multiple types of base models instead of a single type.
meta model
The predictions from each base model in stacking are combined using a meta model to produce a final prediction.
Aside
Learn to:

P
Animation
11.4.1 Stacking application: classification.

P
Question Set
11.4.2 Stacked ensemble models.

P
Animation
11.4.3 Stacking application: regression.

P
Question Set
11.4.4 Meta models.
Table
11.4.1 Base model options for stacking ensembles.

P
Animation
11.4.5 Base models and meta models.

P
Question Set
11.4.6 Selecting base models.
11.5 Case study: Bob Ross

Aside
Learn to:

P
Question Set
11.5.1 Bob Ross dataset.

P
Question Set
11.5.2 Decision tree stump.

P
Question Set
11.5.3 Boosting model performance.

P
Question Set
11.5.4 Bagging model performance.
Figure
11.5.1 Accuracy based on the training and testing datasets using boosting and bagging.

P
Question Set
11.5.5 Selecting a model.
12. Artificial Intelligence

12.1 Artificial intelligence

Artificial intelligence
Artificial intelligence (AI) is the development and use of algorithms and models to mimic human thought.
Machine learning
Machine learning uses algorithms and models to make predictions and discover patterns in data.
Computer vision
Computer vision uses algorithms and models to extract meaning from images and video.
Natural language processing
Natural language processing uses algorithms and models to understand and interpret human language and text.
Knowledge representation
Knowledge representation is a framework for representing how knowledge is stored and processed.
Automated reasoning
Automated reasoning uses algorithms to reason or solve conceptual problems, such as proofs.
Robotics
Robotics is the design, construction, operation, and programming of robots.
Deep learning
Deep learning describes a group of complex models with many parameters.
Aside
Learn to:

P
Animation
12.1.1 Everyday applications of artificial intelligence.

P
Question Set
12.1.2 Artificial intelligence.

P
Animation
12.1.3 Domains of artificial intelligence.

P
Question Set
12.1.4 Artificial intelligence domains.

P
Animation
12.1.5 Deep learning.

P
Question Set
12.1.6 Deep learning.

P
Animation
12.1.7 Guidelines for using artificial intelligence.

P
Question Set
12.1.8 Using artificial intelligence.

C
Progression
12.1.1 Artificial intelligence.
12.2 Machine learning

Machine learning
Machine learning is a subset of artificial intelligence that uses algorithms and models to predict outcomes and find patterns in data.
model
A model is a mathematical function that describes the relationship between input and output features using training data.
algorithm
An algorithm is a set of steps used to perform a machine learning task.
Supervised learning
Supervised learning predicts a known output feature based on input features.
Unsupervised learning
Unsupervised learning describes patterns in a dataset without a known output feature.
Reinforcement learning
Reinforcement learning describes algorithms that make and update decisions based on the result of the previous action.
Regression
Regression predicts the value of a continuous numerical feature.
Classification
Classification predicts the label for a categorical feature.
Clustering
Clustering groups observations based on similar features.
Dimensionality reduction
Dimensionality reduction selects a smaller set of features that best represent the original features.
Aside
Learn to:

P
Animation
12.2.1 Machine learning process.

P
Question Set
12.2.2 Machine learning.

P
Animation
12.2.3 Types of machine learning.

P
Question Set
12.2.4 Types of machine learning.

P
Animation
12.2.5 Supervised vs. unsupervised learning.

P
Question Set
12.2.6 Supervised vs. unsupervised learning.

P
Animation
12.2.7 Reinforcement learning.

P
Question Set
12.2.8 Reinforcement learning.

C
Progression
12.2.1 Machine learning.
12.3 Computer vision

Computer vision
Computer vision refers to the use of algorithms and models to extract information from images and video.
Image classification
Image classification categorizes an image into a set of labels.
Image segmentation
Image segmentation groups pixels in an image into separate regions.
Object detection
Object detection draws a boundary around elements in an image, then assigns each bounded region a label.
Image captioning
Image captioning creates a text description of an image.
Text-to-image generation
Text-to-image generation creates a new image from a text prompt.
Image-to-image generation
Image-to-image generation creates a new image from an image prompt.
Convolutional neural networks
Convolutional neural networks (CNNs) use at least one convolution layer in the neural network to filter inputs, such as an image.
Convolution layers
Convolution layers apply mathematical operations that act as filters to small regions in the image to detect high-level features such as edges or color changes.
Aside
Learn to:

P
Animation
12.3.1 Early computer vision: the MNIST database.

P
Question Set
12.3.2 Computer vision.

P
Animation
12.3.3 Using computer vision tasks on a dog photo.

P
Question Set
12.3.4 Computer vision applications.

P
Animation
12.3.5 Convolutional neural networks.

P
Question Set
12.3.6 Convolutional neural networks on a dog photo.

P
Animation
12.3.7 Using computer vision to diagnose skin lesions.

P
Question Set
12.3.8 Limitations of computer vision.

C
Progression
12.3.1 Computer vision.
12.4 Natural language processing

Natural language processing (NLP)
Natural language processing (NLP) is a subfield of artificial intelligence (AI) focused on using algorithms to analyze and recognize patterns in language and text, and generate new text.
Text classification
Text classification assigns a label to a sequence of text.
Sentiment analysis
Sentiment analysis is a specific case of text classification that applies a sentiment label to a sequence of text, like "positive" or negative".
Text summarization
Text summarization generates a summary of the most important ideas from a long passage of text.
Text generation
Text generation creates new text in response to a prompt.
Language translation
Language translation converts text from one language to another.
Tokenization
Tokenization splits text into individual tokens, usually a word or phrase.
Stemming
Stemming reduces a word into the corresponding base or root form by removing prefixes and suffixes.
Lemmatization
Lemmatization reduces a word into the corresponding base or root form by using a dictionary to learn the meaning of the root.
Part-of-speech tagging
Part-of-speech tagging categorizes words according to a part of speech such as nouns or verbs.
Transformers
Transformers analyze all words simultaneously and adjust each word's significance throughout the model's operation.
self-attention mechanism
A self-attention mechanism captures the relationships between words within an input sequence.
positional encoder
A positional encoder embeds the position of each word in an input sequence, which allows the model to learn word order during model training.
encoder-decoder architecture / encoder / decoder
An encoder-decoder architecture contains an encoder that creates a contextual representation of an input sequence and a decoder that uses this representation to perform tasks like question answering and sentiment analysis.
BERT (Bidirectional Encoder Representation from Transformers)
BERT (Bidirectional Encoder Representation from Transformers) uses multiple layers of encoders to obtain a rich contextual understanding of language.
graph neural network (GNN)
A graph neural network (GNN) is a neural network used to process data that can be represented by a graph.
Large language models (LLMs)
Large language models (LLMs) are advanced artificial intelligence systems designed to analyze and generate human-like text.
Aside
Learn to:

P
Animation
12.4.1 Yelp reviews.

P
Question Set
12.4.2 Natural language processing applications.
Figure
12.4.1 Syntax tree example.

P
Animation
12.4.3 Extracting structured information from unstructured text.

P
Question Set
12.4.4 Natural language processing workflow.

P
Animation
12.4.5 BERT model.

P
Question Set
12.4.6 Transformers and the BERT model.

P
Animation
12.4.7 Graph neural networks.

P
Question Set
12.4.8 Natural language processing with graph neural networks.

P
Animation
12.4.9 Transformers and large language models.

P
Question Set
12.4.10 Large language models.

C
Progression
12.4.1 Natural language processing.
12.5 Risks and ethics in AI

Algorithmic bias
Algorithmic bias occurs when an AI system results in unfair outcomes, like unintentional privilege or harm.
Hallucinations
Hallucinations occur when large language models output nonsensical or inaccurate information.
AI transparency
AI transparency involves disclosing information about how models are trained and used, like the data sources, algorithms, decision-making processes, and applications.
Deepfakes
Deepfakes are manipulated audio, images, or videos of people, with one person's face or likeness swapped for another using artificial intelligence.
Aside
Learn to:

P
Animation
12.5.1 Algorithmic bias in gender classification.

P
Question Set
12.5.2 Algorithmic bias in artificial intelligence.

P
Animation
12.5.3 Hallucination rates in legal cases.

P
Question Set
12.5.4 Hallucinations in artificial intelligence.

P
Animation
12.5.5 AI-assisted X-ray reading.

P
Question Set
12.5.6 AI transparency.

P
Animation
12.5.7 Deepfakes in political ads.

P
Question Set
12.5.8 Deepfakes.

P
Animation
12.5.9 Data center electricity consumption.

P
Question Set
12.5.10 Environmental impact.

P
Animation
12.5.11 Training data for GPT-3.

P
Question Set
12.5.12 Copyright infringement in artificial intelligence.
Table
12.5.1 Types of risk under the EU Artificial Intelligence Act.

P
Question Set
12.5.13 Regulations and guidelines for artificial intelligence.

C
Progression
12.5.1 Risks and ethics in AI.
12.6 Generative AI

Generative artificial intelligence (Generative AI or GenAI)
Generative artificial intelligence (Generative AI or GenAI) uses algorithms and models to create content based on patterns learned from training data.
Modality
Modality is the type of data that an AI system can process as input and can generate as output.
Unimodal AI
Unimodal AI can process and generate only one modality.
Multimodal AI
Multimodal AI can process and generate multiple types of data simultaneously, creating connections between different modalities.
transformer
A transformer architecture has encoder and decoder neural networks with a self-attention mechanism.
diffusion
A diffusion architecture has a neural network that performs a forward process to iteratively add noise to data and a reverse process to remove noise.
Generative Adversarial Network (GAN)
A Generative Adversarial Network (GAN) architecture has two neural networks: a generator to create data and a discriminator to distinguish between original and generated data.
Variational Autoencoder (VAE)
A Variational Autoencoder (VAE) architecture has an encoder network that compresses and maps data to a latent space using a probability distribution. A decoder network restores data from the latent space.
Adversarial training
Adversarial training makes generator and discriminator networks compete with each other.
Contrastive learning
Contrastive learning compares sample data points and differentiates between similar and dissimilar points by grouping similar points together and maximizing the distance between dissimilar points.
Likelihood-based training
Likelihood-based training iteratively adjusts model parameters to maximize the probability of generating output that matches the training data.
Reinforcement learning from human feedback (RLHF)
Reinforcement learning from human feedback (RLHF) uses human feedback to train or optimize AI models using a reward system for output that aligns with human preferences.
Aside
Learn to:

P
Animation
12.6.1 GenAI within the AI hierarchy.

P
Question Set
12.6.2 GenAI basics.
Table
12.6.1 Sample applications of GenAI tools.

P
Animation
12.6.3 GenAI example: Text generation.

P
Question Set
12.6.4 Using GenAI tools.
Table
12.6.2 Comparing unimodal and multimodal AI.

P
Animation
12.6.5 Multimodal GenAI examples.

P
Question Set
12.6.6 Exploring multimodal GenAI.
Table
12.6.3 Common GenAI architectures.

P
Animation
12.6.7 Diffusion and VAE architectures.

P
Question Set
12.6.8 Describing GenAI architectures.
Table
12.6.4 GenAI training method details.

P
Animation
12.6.9 Adversarial training and contrastive learning.

P
Question Set
12.6.10 Identifying training methods.

C
Progression
12.6.1 Generative AI.
12.7 Prompt engineering

prompt
A prompt is the request given to an AI system.
Prompt engineering
Prompt engineering is the process of developing effective prompts.
explicit task
An explicit task clearly states what content the AI should create.
implicit task
Ex: "Write a Python script to compute the mean of a list of numbers." An implicit task requires the AI to infer what content is desired based on the information provided.
Chain-of-Thought (CoT)
Chain-of-Thought (CoT) reasoning and prompting explain step-by-step reasoning for a complex task.
Zero-shot prompting
Zero-shot prompting describes a task to AI but gives no examples.
One-shot prompting
One-shot prompting gives a single example to AI when defining a task.
Few-shot prompting
Few-shot prompting gives multiple examples to AI when defining a task.
Role-based prompting
Role-based prompting gives the AI a role to fill when carrying out a task.
Persona-based prompting
Persona-based prompting extends role-based prompting to include personality, background or other details about the character with the given role.
Iterative refinement
Iterative refinement is a cycle of giving a prompt to AI, evaluating the AI's output, and adjusting the prompt to improve the output.
Progressive refinement
Progressive refinement is an iterative process of giving feedback to improve the AI's response to an initial prompt.
Prompt chaining
Prompt chaining is a technique where an AI is given a sequence of simple steps, and the AI's output for one step is used as input for the next step.
Temperature
Temperature is a parameter that governs the randomness and range of data the AI uses when generating a response.
Aside
Learn to:

P
Animation
12.7.1 Improving a prompt.

P
Question Set
12.7.2 Prompt engineering basics.
Table
12.7.1 Elements of a prompt.

P
Animation
12.7.3 Explicit and implicit tasks.

P
Question Set
12.7.4 Identifying elements of a prompt.

P
Animation
12.7.5 Zero, one, and few-shot prompting.

P
Question Set
12.7.6 Exploring prompting methods.

P
Animation
12.7.7 Role-based prompting.

P
Question Set
12.7.8 Exploring persona and role-based prompting.

P
Animation
12.7.9 Progressive refinement.

P
Learning tool
12.7.10 Prompt chaining.
Table
12.7.2 Temperatures for sample tasks.

P
Animation
12.7.11 Setting the AI temperature.

P
Question Set
12.7.12 Selecting an appropriate temperature.

C
Progression
12.7.1 Prompt engineering.
