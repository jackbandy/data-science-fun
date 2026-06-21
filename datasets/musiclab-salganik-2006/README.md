# MusicLab: Social Influence and Cultural Markets

Data from "Experimental Study of Inequality and Unpredictability in an Artificial Cultural Market," *Science* 2006, by Matthew J. Salganik, Peter Sheridan Dodds, and Duncan J. Watts. For educational purposes only.

## Study

14,341 participants were invited to listen to and download previously unknown songs from unknown bands. They were randomly assigned to one of two conditions:

- **Independent condition** — participants saw only the songs and band names, with no information about others' choices. This serves as a baseline for "true" quality.
- **Social influence condition** — participants also saw how many times each song had been downloaded by earlier participants in their group. The song list was sorted by download count (most popular first).

Crucially, the social influence condition was run as **8 separate parallel "worlds"** — each starting fresh with the same songs. Because the worlds evolved independently from the same random starting point, any divergence between worlds reflects the amplifying effect of social influence rather than differences in song quality.

Key findings:
- Social influence increased *inequality* — popular songs became far more popular than in the independent condition.
- Social influence increased *unpredictability* — the same songs hit or flopped differently across worlds, showing that success is partly arbitrary.
- The best songs rarely failed, and the worst rarely succeeded — but for everything in between, social influence made outcomes hard to predict.

## Data access

The data are publicly available via the Princeton Research Data Commons:

- **URL**: https://datacommons.princeton.edu/discovery/catalog/doi-10-34770-y56c-ym90

The archive includes download counts per song per world per time period, song metadata, and participant-level records. Place any downloaded files in this folder (they are gitignored and not redistributed here).

## Expected data structure

Based on the paper, the dataset contains:
- ~14,341 participant records
- 48 songs rated in each world
- 8 social-influence worlds + 1 independent condition
- Variables: song, world, position_in_list, listens, downloads, timestamp

## Sources

- Paper: https://doi.org/10.1126/science.1121066
- Data archive: https://datacommons.princeton.edu/discovery/catalog/doi-10-34770-y56c-ym90
- Author's data page: http://www.princeton.edu/~mjs3/musiclab.shtml
- Supplementary materials: https://www.princeton.edu/~mjs3/salganik_dodds_watts06_som.pdf

## Disclaimers

- For educational purposes only.
- Accuracy, completeness, etc. not guaranteed.
- Best to avoid reusing or redistributing; if you do, review upstream terms and licensing.
