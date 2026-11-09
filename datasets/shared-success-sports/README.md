# Prior Shared Success in Team Sports

"Prior shared success predicts victory in team competitions," *Nature Human Behaviour* 3(1), 74–81 (2019), by Satyam Mukherjee, Yun Huang, Julia Neidhardt, Brian Uzzi, and Noshir Contractor. For educational purposes only.

This folder is a pointer: the data are in the authors' GitHub repository and are **not redistributed here**.

## Study

The paper asks whether a team wins more often when its players have succeeded together before ("prior shared success"). It builds a network for each team from co-play records and tests that measure on NBA basketball, English Premier League soccer, Major League Baseball, Indian Premier League cricket, and Dota 2 matches.

## Data access

From the paper's data availability statement:

> "Raw data of NBA, EPL and MLB games are available from the ESPN website. IPL data are available from the Cricinfo website. Derived data used in the study are available at GitHub: https://github.com/smukherjee0305/Skills_Shared_Success_Sports."

To get a local copy, clone it into this folder (`upstream/` is gitignored):

```bash
git clone https://github.com/smukherjee0305/Skills_Shared_Success_Sports.git datasets/shared-success-sports/upstream
```

About 104 MB in total (last updated September 2018). The repository has no README, so column meanings come from file headers and the authors' code.

## What's there

- `Data/NBA/` (43 MB), `Data/MLB/` (47 MB), `Data/EPL/` (13 MB), `Data/IPL/` (0.3 MB), `Data/Dota2/` (0.1 MB)
- `Data/<league>/flatfiles/`: match scores, and one row per player per match (match ID, player, team, home/away, date), plus per-player stats. The EPL player-per-match file starts in the 2003–04 season.
- `Data/<league>/seasons/<season>/`: the paper's per-season variables. The `*_relational_succesful_per_season_*.txt` files give, for each match, both teams' scores and summary statistics of their prior-shared-success network (mean, standard deviation, and median), pipe-delimited.
- `Codes/Python/code_data_analysis_sports.py` builds the variables; `Codes/Stata/*.do` runs the regressions.
- Several files are Stata `.dta`; `pandas.read_stata` and `polars` (via pandas) can read them.

The player-per-match files are the natural starting point for a network exercise: players are nodes, and an edge joins two players who appeared in the same match for the same team.

## Sources

- Paper: https://doi.org/10.1038/s41562-018-0460-y
- Data and code: https://github.com/smukherjee0305/Skills_Shared_Success_Sports
- Nature article page: https://www.nature.com/articles/s41562-018-0460-y

## Disclaimers

- For educational purposes only.
- Accuracy, completeness, etc. not guaranteed.
- The upstream repository has no license, and its raw data were collected from ESPN and Cricinfo; review their terms before reusing or redistributing anything.
