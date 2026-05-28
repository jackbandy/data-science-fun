# ACM Data Science Competencies Outline

ACM areas include data acquisition, ethics, communication, computing systems, and reproducible workflows.

Public copy of ACM competencies: https://docs.google.com/document/d/1Ia3Xf1EnC_RSpp0cbtUoB2Rya76flaba/edit#heading=h.w51qynfff8be

## Basic Probability, Statistics, Sampling, and Distributions

- Probability foundations
  - Sets, events, sample spaces
  - Counting, permutations, combinations
  - Probability and odds
  - Conditional probability
  - Independence
  - Bayes' theorem
  - Simpson's paradox
- Random variables and distributions
  - Discrete and continuous random variables
  - Probability density functions and cumulative distribution functions
  - Bernoulli, binomial, Poisson, uniform, exponential, and normal distributions
  - Optional extensions: geometric, negative binomial, hypergeometric, chi-squared, t, F, gamma, beta
- Moments and distribution summaries
  - Expectation
  - Variance
  - Covariance
  - Central tendency and dispersion
  - Robust statistics
  - Skewness, modality, percentiles, quartiles, and five-number summaries
- Sampling and study design
  - Purpose of sampling
  - Random sampling and random assignment
  - Target populations and sampling frames
  - Random, stratified, convenience, and other sampling methods
  - Undercoverage, nonresponse bias, overgeneralization, and other sampling pitfalls
  - Sampling weights
  - Sample size calculation
  - Observational vs experimental studies

## Uncertainty, Inference, and Experimental Reasoning

- Uncertainty quantification
  - Randomness and uncertainty
  - Sampling variability
  - Margin of error
  - Confidence intervals and confidence levels
  - Bootstrapping
  - Central Limit Theorem
  - Law of large numbers
  - Credible intervals as a Bayesian extension
- Statistical inference
  - Null and alternative hypotheses
  - Assumptions and conditions
  - CLT-based and randomization-based hypothesis testing
  - p-values and significance levels
  - Type I and Type II errors
  - Effect size and practical significance
  - Multiple testing
  - Scope of inference
  - Estimation
  - Power analysis
  - Bayesian inference: priors, posteriors, Bayesian hypothesis testing
- Research methods and experimental design
  - Scientific method and iterative inquiry
  - Hypothesis, theory, law, falsifiability, and reproducibility
  - Control groups, independent variables, and dependent variables
  - Treatments, blocks, covariates, confounding, local control, and bias control
  - Randomization and replication
  - A/B testing
  - ANOVA and ANCOVA
  - Factorial and fractional factorial designs
  - Survey question formats, survey flow, missing-data planning, and threats to validity

## Data Frame Fundamentals and Data Wrangling

- Tabular data fundamentals
  - Rows, columns, observations, variables, and records
  - Structured, semi-structured, and unstructured data
  - Numeric, categorical, text, time, geographic, and network data
  - Data dictionaries and metadata
  - Primary vs secondary data sources
  - Observational, experimental, survey, and administrative data
- Core data frame operations
  - Selecting columns
  - Filtering rows
  - Sorting
  - Grouping
  - Aggregating and summarizing
  - Creating and transforming variables
  - Cross-tabulations and pivot tables
  - Reshaping between wide and long formats
  - Text and string manipulation
  - Date/time parsing, indexing, and resampling
- Joining and merging
  - Schemas and keys
  - Primary keys and foreign keys
  - One-to-one, one-to-many, and many-to-many relationships
  - Inner, left, right, and full joins
  - Join validation, row-count checks, duplicate-key checks
  - Harmonizing identifiers and categories across datasets
  - Spatial joins and overlays as an advanced extension
- Data cleaning and quality assurance
  - Missing data detection
  - Missing data imputation
  - Duplicate records
  - Inconsistent labels, spellings, units, and formats
  - Outliers and anomalies
  - Data transformation validation
  - Data quality: accuracy, completeness, consistency, reliability, representativeness, timeliness
  - Bias, fairness, and completeness of data
  - Data provenance and transformation documentation

## Data Acquisition, Storage, and Querying

- Data acquisition
  - APIs
  - Web scraping
  - Database queries
  - Surveys
  - Experiments
  - Sensor and IoT data
  - Streaming and real-time data
- Database fundamentals
  - Relational models: tables, keys, and relationships
  - Entity-relationship modeling
  - Constraints and integrity rules
  - Normalization
  - SQL and NoSQL
  - JSON, XML, and semi-structured data
  - Object-oriented databases as an extension
- Data integration and pipelines
  - Data harmonization
  - ETL: extract, transform, load
  - Data warehousing
  - Distributed databases and cloud data management
  - Streaming data and real-time querying
  - Indexing, performance, scalability, and cost awareness

## Exploratory Data Analysis

- EDA goals and workflow
  - Understanding data structure
  - Detecting patterns, anomalies, and data quality issues
  - Testing assumptions informally before formal modeling
  - Generating hypotheses for later analysis
  - Connecting EDA findings to cleaning, feature engineering, and modeling decisions
- Data-type-guided exploration
  - Quantitative vs qualitative data
  - Numerical and categorical summaries
  - Survey data exploration
  - Text frequency analysis
  - Topic modeling and word embeddings as advanced text extensions
  - Graph and network data
  - Time series, cross-sectional, and longitudinal data
  - Geospatial data, coordinate systems, projections, and maps
- EDA for specialized structures
  - Time series trend, seasonality, and noise decomposition
  - Lag analysis and autocorrelation
  - Rolling statistics and smoothing
  - High-dimensional exploration
  - Dimensionality reduction visuals
  - Responsible use of predictive or generative AI for EDA brainstorming

## Visualization and Data Storytelling

- Visualization fundamentals
  - Matching visualization type to data type and question
  - Dot plots, line plots, scatterplots, bar charts, histograms, box plots, heatmaps, bubble charts, tables, and maps
  - Distribution, comparison, relationship, trend, composition, and geographic views
  - Scaling, axes, labels, color, shading, and visual encoding
  - Full axes, honest scales, and other accurate-presentation principles
  - Misleading visualizations and misleading communication choices
- Exploratory visualization
  - Univariate visualizations
  - Bivariate visualizations
  - Multivariate visualizations
  - Correlation and categorical relationship plots
  - Clustering visualizations
  - Time-series visualizations
  - Geospatial visualizations
- Explanatory communication
  - Audience and persona identification
  - Communication purpose and context
  - Appropriate level of technical detail
  - Static vs dynamic visuals
  - Dashboards
  - Presentations and reports
  - Effective communication of uncertainty, limitations, and assumptions
  - Story structure, pacing, and feedback-driven revision
  - Accessibility, ADA/EAA awareness, alt text, color accessibility, and user-interface accessibility
  - Ethical use of AI-generated text, images, summaries, and visual ideas

## Linear Modeling and Statistical Modeling

- Linear modeling
  - Simple linear regression
  - Multiple linear regression
  - Interpretation of coefficients
  - Prediction vs explanation
  - Residual analysis
  - Lack of fit
  - Assumption checking
  - Multicollinearity
- Generalized and regularized models
  - Logistic regression
  - Generalized linear models
  - Ridge regression
  - Lasso regression
  - Elastic net
- Model selection and diagnostics
  - Cross-validation
  - k-fold cross-validation
  - Hyperparameter tuning
  - AIC and BIC
  - Variable importance
  - SHAP and other interpretability tools
  - Overfitting and underfitting
  - Assumption validation
  - Model limitations and communication of uncertainty
- Broader statistical and optimization models
  - Decision trees
  - Ensemble models
  - Decision analysis
  - Linear programming
  - Integer programming
  - Nonlinear optimization
  - Time series models
  - Queueing models and stochastic processes as extensions

## Machine Learning Models

- ML foundations
  - Supervised, unsupervised, semi-supervised, and reinforcement learning
  - Data preparation and feature identification
  - Feature engineering and feature selection
  - Training/test splits
  - Cross-validation
  - Choice and representativeness of training and testing data
  - Bias and limitations of training data
  - Model contexts and intended uses
- Classification and regression
  - Classification definitions and decision boundaries
  - Binary, multi-class, and hierarchical classification
  - k-nearest neighbors
  - Decision trees
  - Random forests
  - Boosting
  - Support vector machines
  - Linear and logistic regression
  - Regression error measures
  - Confusion matrices
  - Accuracy, sensitivity, specificity, precision, recall, F1, F-beta, ROC/AUC
- Unsupervised learning and data mining
  - Clustering
  - Dimensionality reduction
  - Association rule mining
  - Outlier detection
  - Proximity and distance metrics
  - Cluster hypothesis formulation and testing
  - Mining text, web, spatial, temporal, and time-series data
- ML systems and deployment awareness
  - Online vs offline systems
  - Transfer learning
  - TensorFlow and similar frameworks
  - GPUs vs CPUs
  - Cloud platforms and compute cost
  - Environmental cost of large compute jobs
  - Evaluation of ML outcomes
  - Feedback loops, monitoring, and maintenance

## Recommendation Systems

- Feature-based recommendation systems
  - Content-based recommendation
  - Feature representation for users and items
  - Similarity metrics and distance measures
  - Ranking and top-k recommendation
  - Feature engineering for recommendation
- Collaborative recommendation
  - User-item matrices
  - User-user and item-item collaborative filtering
  - Matrix factorization
  - SVD and low-rank representations
  - Missing ratings and sparse matrices
  - Cold-start problems
- Network-based recommendation systems
  - Bipartite user-item graphs
  - Link prediction
  - Path-based similarity
  - Community-aware recommendation
  - Popularity bias and long-tail recommendation
- Responsible recommendation
  - Evaluation metrics
  - Filter bubbles and feedback loops
  - Fairness and exposure bias
  - Transparency and explanation
  - Privacy and consent

## Network Analysis and Graphs

- Graph fundamentals
  - Nodes and edges
  - Directed and undirected graphs
  - Weighted and unweighted graphs
  - Bipartite graphs
  - Paths, components, and connectivity
  - Trees and graph data structures
- Network measures and algorithms
  - Degree and degree distributions
  - Centrality measures
  - Shortest paths
  - Community detection
  - Graph traversal
  - Tree and graph algorithms
  - Complexity and scalability of graph algorithms
- Network applications
  - Social networks
  - Web and information networks
  - Infrastructure networks
  - Recommendation networks
  - Network visualization
  - Network-based prediction
  - Ethical implications of network data and inference

## Mathematical and Algorithmic Foundations

- Discrete mathematics
  - Logic and truth tables
  - Predicate calculus
  - Induction
  - Recurrence relations
  - Graph theory
  - Error propagation
  - Sensitivity analysis
  - Big-O notation and orders of magnitude
- Linear algebra
  - Vectors and matrices
  - Matrix operations
  - Dot products and projections
  - Norms and distance metrics
  - Matrix factorization: SVD, QR, NMF, Cholesky, LU
  - Eigenvalues and eigenvectors
  - Systems of linear equations
  - Sparse matrices and tensor algebra as extensions
- Calculus and optimization
  - Differentiation
  - Gradients
  - Gradient descent
  - Optimization for model fitting
  - Constrained optimization
- Algorithms and data structures
  - Iteration and recursion
  - Sorting and searching
  - Hashing
  - Arrays, lists, tuples, dictionaries, sets, trees, graphs, networks
  - Time complexity and space complexity
  - MapReduce and big-data algorithms

## AI, NLP, and Generative AI Extensions

- AI foundations
  - Search algorithms
  - Heuristics
  - Search evaluation metrics
  - Search system design
  - Logic-based approaches
  - Knowledge representation
- Natural language processing
  - Syntax and semantics
  - Context
  - Text classification
  - Named entity recognition
  - Sentiment analysis
  - Topic modeling
  - Language models and large language models
  - Transformers
  - Loss functions and alternative accuracy measures
- Deep learning and generative AI
  - Neural networks
  - Backpropagation
  - Gradient descent
  - Multi-level neural networks
  - Convolutional neural networks
  - Generative AI foundations
  - Synthetic data generation and data augmentation
  - Prompt engineering as an elective
  - Trustworthy AI: interpretability, fairness, privacy preservation, robustness

## Computing Systems, Security, and Scale

- Computer systems
  - Operating systems
  - Bits, bytes, and data representation
  - Computer arithmetic
  - CPUs and GPUs
  - Storage systems: registers, cache, RAM, virtual memory
  - Backups
  - Virtual systems and cloud services
- Networking
  - Internet organization
  - Cloud and web services
  - Intranet vs internet
  - DNS, IP addresses, URIs
  - TCP, IP, HTTPS
  - Network security and monitoring
- High-performance and scalable computing
  - Problems of scale
  - Parallel and distributed computing
  - Multi-core and GPU architectures
  - Storage growth and storage hierarchy
  - Fast I/O
  - Big-data processing
  - Cloud scalability, performance, and cost
- Security and privacy
  - Threats, vulnerabilities, and attack vectors
  - Authentication and authorization
  - Encryption at rest and in transit
  - Access control
  - Security governance and management
  - Data collection, backup, and retention policies
  - Tensions among security, privacy, and performance

## Reproducible Workflows and Project Practice

- Workflow practices
  - Reproducibility
  - Version control for code, data, models, and experiments
  - Automation
  - Experiment tracking
  - Documented assumptions and decisions
  - Traceable data cleaning and modeling pipelines
  - Responsible use of AI tools for automation and documentation
- Project planning and governance
  - Project scope
  - Work breakdown structure
  - Resources and timelines
  - Monitoring and success metrics
  - Legal and ethical compliance
  - Bias, privacy, fairness, and regulatory planning
- Documentation and collaboration
  - Data source documentation
  - Model documentation
  - Project reports
  - Project visualizations
  - DevOps awareness
  - Team roles and coordination
  - Conflict management
  - Internal and external stakeholder communication

## Ethics, Law, and Professional Responsibility

- Data stewardship
  - Responsible data collection
  - Consent and transparency
  - Data privacy
  - Data security
  - Data governance
  - Data protection regulations
  - Data bias
  - Data retention and lifecycle management
- Ethical and legal reasoning
  - Codes of ethics
  - Ethical reasoning frameworks
  - Legal frameworks and international standards such as GDPR
  - Research integrity
  - Stakeholder engagement
  - Decision framing
  - Accountability and transparency
  - FAIR and CARE principles
  - Belmont principles and human-subjects protections
- Intellectual property
  - Copyright, patents, and trademarks
  - Open-source software licenses
  - Data licensing and usage agreements
  - Institutional IP policies
  - Attribution and ownership
- Professional practice
  - Collaboration and teamwork
  - Leadership
  - Evidence-based advocacy
  - Communication to diverse audiences
  - Anticipating impacts on individuals, communities, economies, and environments
  - Sustainability and environmental impact of large-scale computation
