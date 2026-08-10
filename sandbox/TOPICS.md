# Topics Missing by Week

What's needed in order to match the coverage in Zheleva's (Z) and
Bello's (B) materials.

Sources: `source-materials/slides-elena-pdf/`, `source-materials/belo CS 418 (Spring 2026)/`.

---

## Week 1 — Course introduction; statistics review / Data science lifecycle

- Measures of center and spread with the robustness argument (mean vs. median under outliers) — B 02
- Harmonic mean and geometric mean vs. arithmetic mean
	- rates/ratios, multiplicative growth, other demo scenarios
- Percentiles, quartiles, five-number summary, box plots — B 02
- Probability basics: sample space, complement, mutually exclusive, conditional, independence — B 03
- Bayes' theorem with the disease-test / spam worked example — B 03
- Random variables, PMFs, the normal distribution, empirical rule, CLT — B 03
- The lifecycle as a *recurring* frame — Z reopens the same diagram at the top of every lecture
- Flint water crisis (Z) or an equivalent case walked end-to-end through all five stages

## Week 2 — Python foundations; dataframes and Polars / Obtaining data

- DataFrame / Series / Index; `[]` return-type semantics; `.loc` vs. `.iloc` — Z pandas
- Boolean masking and multi-condition filtering — Z pandas
- Why rectangular data: regular structure is what makes manipulation tractable — Z pandas
- Four acquisition methods: direct download, DB query, API call, web scraping — Z wrangling, B 05
- HTTP requests and REST statelessness (credentials with every call) — Z wrangling2, B 05
- Web scraping: HTML structure, parsing out a field — B 05
- Sampling for collection: with/without replacement, stratified, convenience — B 05
- Common collection problems: selection bias, non-response, measurement error — B 05

## Week 3 — Wrangling data; filtering data / Data formats

- Granularity: what one row represents; mixed-granularity records; how coarse data was aggregated — Z wrangling2
- Split-apply-combine (`groupby`) and `pivot_table` as reshaping tools — Z wrangling2, B 06
- Tidy data and the four classic violations, with `melt` / `split` / `pivot` fixes — B 06
- Joins: inner/left/right/outer, and the missing values joins create — B 06
- Data quality checklist: impossible values, dependency violations, curb-stoning, unit inconsistency — Z wrangling2
- Missing-value handling: drop vs. impute, and how each biases conclusions — B 06
- Temporality: timezones, UTC/Unix time, DST, date parsing — Z wrangling2
- Scope and faithfulness: too narrow vs. too broad; what filtering does to a sample — Z wrangling2

## Week 4 — Exploratory analysis / Descriptive statistics

- Outlier detection by the $Q_3 + 1.5\,IQR$ rule  — B 06
- Standardization vs. normalization, and when scale matters for distance-based methods — B 06
- Aggregation as a variable transform (reduce variability, enable expensive algorithms) — B 06
- Dimensionality reduction preview: curse of dimensionality, feature selection vs. extraction — B 06
- EDA as an *open-ended* practice: be willing to be surprised; hypotheses discovered here need care — Z viz

## Week 5 — Visualization

- needs the general grammar first, before deep dives
- Plot-type taxonomy by data type: quantitative, categorical, and the pairwise combinations — Z viz, B 07
- Bivariate categorical–quantitative: side-by-side box, violin, overlaid density — Z viz
- Conditioning: normalizing within a group to make a comparison honest — Z viz2
- Scale choices: log transforms, shared vs. dual axes — Z viz2
- Perception ranking: length beats angle beats area beats volume — Z viz2, B 07
- Avoid stacking when comparisons matter; grouped bars instead — B 07 Ex 7.2
- Line plots only for ordered data — B 07 Ex 7.3–7.4

## Week 6 — Visualization

- set up connection to time series
- Plot critique as a practiced skill: the Chaffetz/Planned Parenthood chart, dual-scale deception — Z viz2
- Correlation ≠ causation via spurious-correlation examples (tylervigen) — Z viz2
- Large-$N$ scatter plots: overplotting and smoothing (local averaging, KDE, 2-D density) — Z viz2
- Kernel choice and bandwidth as the visualization analogue of bin width — Z viz2, Z eda
- Labels over color for many categories; accessible encodings — B 07 Ex 7.5
- If the time-series material stays: connect it to Bello's L18 (stationarity, AR/MA/ARIMA, ACF/PACF)

## Week 7 — Hypothesis testing / Estimation and sampling; randomness

- add basic p-value mechanics
- Inferential vs. descriptive statistics; population parameter vs. sample statistic — Z hypothesis
- The seven-step testing procedure ($H_0$, $\alpha$, data, statistic, $p$, compare, decide) — Z hypothesis, B 04
- Type I / Type II error, significance level, power, and which error costs more — Z hypothesis, B 04
- z-test: assumptions, statistic, one- vs. two-tailed, `st.norm.cdf` — Z hypothesis, B 04
- t-test: when $\sigma$ is unknown, degrees of freedom, `st.t.cdf` — Z estimation, B 04
- Two-sample and unpaired tests (observed − hypothesized difference over SE) — B 04
- Statistical vs. practical significance — Z hypothesis
- Estimation framing: data-generating process → model → estimated model; loss functions (L1/L2);
  mean minimizes L2, median minimizes L1 — Z estimation

## Week 8 — Linear regression / Intro to classification

- Least squares derivation: residuals, RSS/ESS/TSS, partial derivatives set to zero — B 10
- $R^2$ as $ESS/TSS = r_{XY}^2$; assessing model fit — B 10
- The four regression assumptions and diagnosing them from residual plots — B 10
- Multiple regression, categorical predictors as dummies, adjusted $R^2$ / AIC / BIC — B 11
- Gradient descent: step size, convergence, local minima, SGD — B 11, Z linear
- Regularization: ridge, lasso, elastic net; why overfit models have large coefficients — B 11
- Classification setup: target variable, supervised vs. unsupervised — B 09
- Confusion matrix, accuracy, error, precision, recall, F1; k-NN with distance metrics — B 12, B 13

## Week 9 — Decision trees / Support vector machines; kernels

- Tree anatomy (root, internal, leaf, branches) and classifying by traversal — B 12
- Top-down induction; entropy and information gain as splitting criteria — B 12
- Non-binary and continuous attributes; stopping criteria; pruning and Occam's razor — B 12, Z classification2
- Tree advantages/disadvantages and `sklearn` construction — B 12
- Naïve Bayes: conditional independence assumption, worked classification — B 13
- Max-margin hyperplanes: why the widest margin generalizes — B 13
- Soft-margin SVM and the role of $C$ — B 13, Z classification3
- The kernel trick (polynomial, RBF) and multiclass strategies (OVR, OVO) — B 13, Z ensembles

## Week 10 — Clustering; PCA / Model evaluation

- Holdout vs. k-fold cross-validation; the train/validation/test split and what each tunes — B 09, Z classification2
- Overfitting vs. underfitting diagnosed from train/test error; the bias–variance tradeoff — B 09
- Supervised cluster evaluation: contingency matrix, cluster precision/recall/F1, entropy — B 14
- K-medoids and DBSCAN core/border/noise points (my deck has k-means and hierarchical only) — B 15
- Class imbalance: why accuracy misleads; F1, sensitivity/specificity, ROC/AUC — B Bonus, Z ensembles
- Ensembles: bagging, boosting, random forest, XGBoost — B Bonus, Z ensembles
- Precision/recall at a ranking cutoff; the precision–recall tradeoff curve — Z ensembles

## Week 11 — Recommendation systems / A/B testing

- A/B testing is absent.
- Collaborative filtering mechanics: user–item matrix, similarity, predicted rating — Z syllabus (recsys week)
- Content-based filtering and hybrid systems; the cold-start problem
- Causal inference framing: treatment, potential outcomes, counterfactuals — Z causality
- Fundamental problem of causal inference; ATE and CATE as the workaround — Z causality
- Pearl's ladder: association / intervention / counterfactual, and what each needs — Z causality
- A/B test design: treatment vs. control, randomization, balance on pre-treatment covariates — Z abtesting
- Sample size planning from minimum detectable lift and target power (80%) — Z abtesting
- When RCTs aren't possible (ethics, cost, immutable traits) and what to do instead — Z causality

## Week 12 — Network analysis / Graphs and relationships; network measures

- align to Bello's L20 — community detection, modularity,
Louvain, SIS/SIR/SIRS/SEIV, epidemic threshold, NetShield
- Basic centrality and degree measures worked numerically (my deck jumps to community detection) — B 20
- Weighted and directed graph representation; adjacency matrix conventions — B 20
- Network dependence as a threat to contagion findings (Christakis–Fowler obesity study) — Z causality

## Week 13 — TBD ×2

Potential topics, i.e. uncovered blocks from other classes:

- **SQL / relational databases**: relational model, physical data independence, declarative querying, `SELECT/WHERE/GROUP BY/HAVING/ORDER BY`, clause evaluation order — Z db, B 19
- **Joins**: cartesian product, inner join, cross join, and query-optimizer reality — Z db2
- **Text analysis**: inverted index, tokenization/stemming, TF-IDF, vector space model, cosine similarity, IR precision/recall — B 16, B 17
- **Big data storage**: NoSQL (key-value, document), schema-on-write vs. -on-read, sharding, replication, CAP theorem, Hadoop/HDFS — B 19
- **Big data processing**: MapReduce, SCV principle, data streams, Hoeffding trees — B 19
- **Data warehousing**: star schema, ETL, OLTP vs. OLAP, metadata — Z bigdata
- **Time series**: stationarity, differencing, AR/MA/ARMA/ARIMA/SARIMA, ACF/PACF — B 18
	- (`week6.qmd` covers decomposition and Bayesian forecasting but not the ARIMA family)
- **Privacy-preserving data science**: not in Z or B — a genuinely new block, so it needs
  building from scratch rather than porting. Fits here as a TBD week; the natural alternative
  homes are Week 2 (what you're allowed to collect) and Week 3 (aggregation and granularity
  as de-identification), which could each carry a one-slide pointer forward.
	- Re-identification as the motivating failure: the Netflix Prize and AOL search-log
	  de-anonymizations, and Sweeney's ZIP + birthdate + sex ≈ 87% of the US population
	- PII vs. quasi-identifiers vs. sensitive attributes; why "we removed the names" is not privacy
	- $k$-anonymity via generalization and suppression, worked on a small table by hand
	- Where $k$-anonymity breaks: homogeneity and background-knowledge attacks, and the
	  $\ell$-diversity / $t$-closeness patches that follow from them
	- Differential privacy as a *property of the mechanism*, not of the released data:
	  the neighboring-datasets definition and $\varepsilon$ as a privacy budget
	- Randomized response as the intuition pump — students can run it on themselves in class
	- The Laplace mechanism: sensitivity of a query, noise scale $b = \Delta f / \varepsilon$,
	  and the privacy–utility tradeoff shown on a real count/mean
	- Composition: budgets add up across queries, which is why repeated analysis is the hard part
	- Deployments worth naming: the 2020 US Census, Apple/Google telemetry, and the
	  criticism each drew
	- Encryption basics only as much as the story needs: symmetric vs. public-key, hashing and
	  salting (and why hashed identifiers are still identifiers), plus a conceptual look at
	  homomorphic encryption, secure multiparty computation, and federated learning
	- Lab option: `diffprivlib` or hand-rolled Laplace noise on a dataset from an earlier week,
	  sweeping $\varepsilon$ and plotting the error it buys

## Weeks 14–15 — Presentations

Content coverage is not the issue; scaffolding is. Both sources stage the project.
- Individual contribution tracked via git history — Z abtesting
