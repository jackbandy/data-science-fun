# Sources — `assets/linear-model-criteria-assumptions`

NOTICE: this file was drafted by an LLM coding system and has not yet been reviewed.

Practice figures for the four LINE conditions on the Week 8 "Assumptions / Criteria" slide, from Mine Çetinkaya-Rundel and Johanna Hardin, ["Inference for Linear Regression with a Single Predictor"](https://openintro-ims.netlify.app/inf-model-slr.html), §24.6 of *Introduction to Modern Statistics*, 2nd ed. (OpenIntro): "The linearity, normality, and equality of variance conditions usually can be assessed through residual plots."

`make_linear_assumption_figures.py` (`python3 make_linear_assumption_figures.py [name ...]`) writes 24 examples, each as three slide builds (72 SVGs, all 1000 × 618, golden ratio):

- `<name>-v0.svg` — the data alone.
- `<name>-v1.svg` — adds the least-squares line and the diagnostic for one assumption on the right. Axis limits match v0, so the points don't move between builds.
- `<name>-v2.svg` — adds a large, semi-transparent theme-orange diagonal stamp across the middle: "Meets criteria" (`positive` files) or "Does not meet criteria" (`negative` files).

v0 and v1 carry no verdict, so they work as "does this assumption hold?" questions; v2 is the answer. Each example is judged only on the assumption in its filename: several also break a different assumption, noted under "Also". The tables below list each example by its base name.

**Titles** read "Linear modeling criteria: <IMS name> (<other name>)": Linearity (linear function); Independent observations (independent errors); Nearly normal residuals (normally distributed errors); Constant or equal variability (homoscedasticity). The first three other names follow Penn State [STAT 462 §6.1, "MLR Model Assumptions"](https://online.stat.psu.edu/stat462/node/145/), which spells out LINE as: the mean response "is a Linear function of the predictors"; "The errors … are Independent"; "Normally distributed"; "have Equal variances". "Homoscedasticity" is the name the Week 8 slide already gives equal variability; IMS, STAT 462, and the NIST e-Handbook pages checked do not use the word, so it has no quoted source here yet.

**Subtitles** quote the condition verbatim (checked against the online text, 2026-10-11). Linearity pairs two separate quotes, each in its own quotation marks: "The data should show a linear trend." (§24.6) and "One purpose of residual plots is to identify characteristics or patterns still apparent in the data after fitting a model." (§7.1.3, [Residuals](https://openintro-ims.netlify.app/model-slr.html)). The rest are from §24.6: Independent observations, "Be cautious about applying regression to data that are sequential observations in time such as a stock price each day."; Nearly normal residuals, "Generally, the residuals should be nearly normal."; Constant or equal variability, "The variability of points around the least squares line remains roughly constant."

**Captions** under the plots name and describe the dataset and credit the quoted section(s).

## Data

- **Cook County home sales, 2025** — `datasets/cook-county-home-sales-2025/` (Cook County Assessor's Office, Cook County Open Data portal). Single-family, single-parcel sales over $10,000, filtered as in the Week 5 and Week 8 slides; a fixed random sample of 300 (`seed=418`).
- **Olympic 100 m winning times** — `assets/olympics-100m/data/`: Tatem et al. (2004), *Nature* 431:525, Supplementary Table S1, plus 2008–2024 from Wikipedia. See `assets/olympics-100m/SOURCES.md`.
- **Airline passengers, 1949–1960** — `datasets/airline-passengers/` (Box and Jenkins, *Time Series Analysis*, 1976; R's `AirPassengers`).
- **CTA ridership** — `datasets/cta-ridership/`: annual boarding totals, all-station daily entries (averaged per station for 2025), and UIC-Halsted daily entries for 2025 (City of Chicago Data Portal).
- **Chicago buildings with 10+ stories** — `datasets/chicago-tall-buildings/` (City of Chicago building footprints). Rows with a recorded unit count above zero.
- **US presidential elections, 1824–2024** — `datasets/us-presidential-elections/` (Data 100 course notes `elections.csv`, compiled from Wikipedia). One row per candidate.
- **IMDb's 1,000 most-rated movies** — `datasets/movies-from-imdb/popular.csv` (IMDb non-commercial datasets, June 2026).
- **Synthetic data A–K** — generated in the script with fixed seeds; each function shows the formula.

## Linearity (residuals vs. x)

| File | Verdict | Data | What to see | Also |
|---|---|---|---|---|
| `linearity-positive-example-a` | holds | Cook County, log sqft vs. log price | No curve left in the residuals | Residuals skew left |
| `linearity-positive-example-b` | holds | Olympic men's vs. women's winning time, same Games, 1928–2024 | Residuals scatter evenly around zero | |
| `linearity-positive-example-c` | holds | Synthetic A: `y = 3 + 1.6x + N(0, 1.8)` | Patternless band | |
| `linearity-negative-example-a` | violated | CTA rail boardings by year, 1988–2025 | Residuals dip, climb, then crash in 2020 | Strongly dependent over time |
| `linearity-negative-example-b` | violated | Synthetic B: quadratic | U-shaped residuals | |
| `linearity-negative-example-c` | violated | Synthetic C: saturating curve | Upside-down U in the residuals | |

## Independence (residuals in collection order)

| File | Verdict | Data | What to see | Also |
|---|---|---|---|---|
| `independence-positive-example-a` | holds | Cook County, log-log, ordered by sale date | No runs or waves across the year | Residuals skew left |
| `independence-positive-example-b` | holds | Tall buildings, stories vs. units, ordered by year built | Neighbors in time don't track each other | Unequal variability |
| `independence-positive-example-c` | holds | Synthetic D: independent normal errors | Jagged, no runs | |
| `independence-negative-example-a` | violated | Airline passengers by month (log scale) | A repeating yearly wave | |
| `independence-negative-example-b` | violated | UIC-Halsted weekday entries, 2025 | Long runs above and below zero that line up with the academic calendar | Not linear |
| `independence-negative-example-c` | violated | Synthetic E: AR(1) errors, `e[i] = 0.85 e[i-1] + N(0, 0.8)` | Slow drifts; each residual near the last | |

## Nearly normal residuals (histogram, normal curve overlaid)

| File | Verdict | Data | What to see | Also |
|---|---|---|---|---|
| `normality-positive-example-a` | holds | Olympic men's 100 m, 1948–2024 | Rough bell shape (only 20 points) | Time-ordered |
| `normality-positive-example-b` | holds | Synthetic F: normal errors, n = 200 | Bell shape | |
| `normality-positive-example-c` | holds | Synthetic G: normal errors, n = 400 | Bell shape | |
| `normality-negative-example-a` | violated | IMDb's 1,000 most-rated movies, release year vs. number of ratings | Strong right skew: a wall just below zero and a long right tail | Unequal variability |
| `normality-negative-example-b` | violated | US presidential elections, year vs. candidate's vote share | Two humps (major-party candidates near 40–60%, third parties near 0) with almost nothing near zero residual | Not linear; shares within one election sum to 100, so not independent |
| `normality-negative-example-c` | violated | Synthetic H: exponential errors shifted to mean zero | Right skew: a pile-up just below zero and a long right tail | |

## Equal variability (residuals vs. fitted values)

| File | Verdict | Data | What to see | Also |
|---|---|---|---|---|
| `equal-variability-positive-example-a` | holds | IMDb, runtime vs. average rating | Roughly even band of residuals | Residuals skew left |
| `equal-variability-positive-example-b` | holds | Synthetic I: constant-variance errors, n = 150 | Even band | |
| `equal-variability-positive-example-c` | holds | Synthetic J: constant-variance errors, n = 60 | Even band | |
| `equal-variability-negative-example-a` | violated | CTA 'L' stations, 2025: average weekday vs. weekend/holiday entries | Tight band for small stations, wide fan for the busiest | |
| `equal-variability-negative-example-b` | violated | Airline passengers by month (raw scale) | Seasonal swings grow with traffic, so the residuals fan out; the log scale in `independence-negative-example-a` is the usual fix | Not independent (yearly wave) |
| `equal-variability-negative-example-c` | violated | Synthetic K: error SD shrinks as x grows | Fan widening with the fitted value | |
