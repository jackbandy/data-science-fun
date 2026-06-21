# Galton's Vox Populi (1907): Wisdom of Crowds

Quantile summary of 787 weight estimates from Francis Galton's 1907 "wisdom of crowds" experiment, as published in *Nature*. For educational purposes only.

## Study

In 1906, at a livestock fair in Plymouth, England, 800 people paid to guess the slaughtered and dressed weight of an ox on display. The guesses included experienced farmers and butchers as well as townspeople with no special knowledge. Galton collected 787 valid tickets, computed the distribution, and published the results in *Nature* (1907) under the title "Vox Populi" (Voice of the People).

The median guess was 1,207 lbs, within **0.8%** of the actual weight of 1,198 lbs. Galton had expected the crowd to be wrong but found the aggregate estimate to be more accurate than most individual experts. The paper has become a classic in collective intelligence / "wisdom of crowds" research.

## Files

- `vox-populi-quantiles.csv` — 19-row quantile summary of the 787 weight estimates, as Galton published them
- `vox-populi-synthetic.csv` — synthetic list of 787 individual estimates (lbs) reconstructed from the quantile table; all 19 quantiles match the source exactly
- `generate-synthetic.py` — script used to generate `vox-populi-synthetic.csv`

## Columns

- `quantile` — percentile (5, 10, 15, … 95)
- `estimate` — estimated dressed weight in pounds at that percentile
- `observed` — deviation from the median (estimate minus 1207)
- `normal` — expected deviation at that percentile under a normal distribution
- `excess` — observed deviation minus normal deviation (leptokurtosis measure)

## Data format

- Galton did not publish individual ticket values, only the 19-row quantile table in the 1907 *Nature* paper. 
- The `estimate` column represents percentiles of the distribution of 787 guesses, not individual guesses.
- The actual weight was **1,198 lbs**; the median guess (p50) was **1,207 lbs**.
- Galton noted the crowd's distribution was slightly leptokurtic (heavier tails than normal), as shown in the `excess` column.

## Sources

- Original paper (open access): https://doi.org/10.1038/075450a0
- Data reproduced in: jrnold/datums R package, https://github.com/jrnold/datums
- CSV downloaded from: https://raw.githubusercontent.com/jrnold/datums/master/data-raw/VoxPopuli.csv

## Disclaimers

- For educational purposes only.
- Accuracy, completeness, etc. not guaranteed.
- File was downloaded in June 2026 and may be outdated or inconsistent with current upstream records.
- Should not be treated as a complete or official record.