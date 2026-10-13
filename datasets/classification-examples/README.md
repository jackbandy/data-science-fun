# Classification Examples

Five small datasets, each used in the Week 8 slides as a yes/no question answered from two numeric inputs. Rebuild them with `uv run collect_classification_examples.py` (or name one, e.g. `uv run collect_classification_examples.py cook-county`). For educational purposes only.

| File | Question in the slides | Two inputs | Yes/no output |
|---|---|---|---|
| `college-scorecard.csv` | Is this university public or private? | `UGDS`, `TUITIONFEE_IN` | `CONTROL` (1 public, 2 private nonprofit) |
| `spambase.csv` | Is this email spam? | `char_freq_!`, `capital_run_length_average` | `spam` |
| `penguins.csv` | Is this penguin an Adélie or a Gentoo? | `bill_length_mm`, `bill_depth_mm` | `species` |
| `wdbc.csv` | Is this tumor malignant? | `radius_mean`, `texture_mean` | `diagnosis` (M or B) |
| `cook-county-sales-density.csv` | Is this home in Chicago or the suburbs? | `land_sqft`, `housing_units_per_sq_mi` | `in_chicago` |

## Files

- `college-scorecard.csv`: 6,273 institutions, eight columns kept from the College Scorecard "most recent cohorts" institution file. Definitions from the [Scorecard data dictionary](https://collegescorecard.ed.gov/files/CollegeScorecardDataDictionary.xlsx):
  - `UNITID`, `INSTNM`, `STABBR`: IPEDS id, name, state
  - `CONTROL`: 1 public, 2 private nonprofit, 3 private for-profit
  - `PREDDEG`: predominant undergraduate degree; 3 is "Predominantly bachelor's-degree granting"
  - `UGDS`: "Enrollment of undergraduate certificate/degree-seeking students"
  - `TUITIONFEE_IN`: "In-state tuition and fees"
  - `ENDOWEND`: "Value of school's endowment at the end of the fiscal year" (`NA` when not reported; for-profits never report one)
- `spambase.csv`: 4,601 emails, 57 features plus `spam` (1 spam, 0 not), with column names taken from `spambase.names`. `char_freq_!` is the percentage of characters that are `!`; `capital_run_length_average` is the "average length of uninterrupted sequences of capital letters."
- `penguins.csv`: 344 penguins (Adélie, Chinstrap, Gentoo), the `penguins` table from the palmerpenguins R package, unchanged. Missing values are `NA`.
- `wdbc.csv`: 569 breast tumor biopsies, `id`, `diagnosis` (M malignant, B benign), and 30 features: the mean, standard error, and "worst" of ten measurements of the cell nuclei in a digitized image of a fine needle aspirate. Column names follow the order in `wdbc.names`.
- `cook-county-sales-density.csv`: one row per sale in `../cook-county-home-sales-2025/cook-county-home-sales-2025.csv`, same order, with the columns needed to repeat the Week 5 filter (`property_group`, `is_multisale`, `sale_price`, `building_sqft`) plus:
  - `land_sqft`: lot size in square feet, copied from the sales file
  - `in_chicago`: `municipality` is `CITY OF CHICAGO`
  - `tract_geoid`, `tract_population_2020`, `tract_housing_units_2020`, `tract_land_sq_mi`: the 2020 census tract the sale's coordinates fall in, with its 2020 census population (`POP100`), housing units (`HU100`), and land area
  - `people_per_sq_mi`, `housing_units_per_sq_mi`: tract population and housing units divided by tract land area
  - `miles_to_nearest_l_stop`: straight-line (haversine) miles from the sale to the nearest stop in `../chicago-l-stations/`
  - Sale coordinates are rounded to about 110 m in the source file, so a sale near a tract boundary can land in the neighboring tract; 11 filtered single-family sales fall in no tract and have empty tract columns.
- `collect_classification_examples.py`: downloads the sources and writes the five CSVs. Only the Cook County step needs third-party packages (numpy, matplotlib), declared inline for `uv run`.

## Sources

- U.S. Department of Education, [College Scorecard](https://collegescorecard.ed.gov/data/), `Most-Recent-Cohorts-Institution_06102026.zip` (institution data from IPEDS). U.S. government work.
- Mark Hopkins, Erik Reeber, George Forman, and Jaap Suermondt, "Spambase" [Dataset], UCI Machine Learning Repository (1999), <https://doi.org/10.24432/C53G6X>. CC BY 4.0.
- Allison Horst, Alison Hill, and Kristen Gorman, palmerpenguins v0.1.0 (2020), <https://doi.org/10.5281/zenodo.3960218>, file `inst/extdata/penguins.csv` from <https://github.com/allisonhorst/palmerpenguins>. CC0. Data originally from Kristen B. Gorman, Tony D. Williams, and William R. Fraser, "Ecological Sexual Dimorphism and Environmental Variability within a Community of Antarctic Penguins (Genus *Pygoscelis*)," *PLoS ONE* 9(3): e90081 (2014), <https://doi.org/10.1371/journal.pone.0090081>.
- William Wolberg, Olvi Mangasarian, Nick Street, and W. Street, "Breast Cancer Wisconsin (Diagnostic)" [Dataset], UCI Machine Learning Repository (1993), <https://doi.org/10.24432/C5DW2B>. CC BY 4.0.
- U.S. Census Bureau, [TIGERweb](https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Census2020/MapServer/6), 2020 Census Tracts layer (`POP100`, `HU100`, `AREALAND`, tract polygons). U.S. government work.
- Cook County home sales and CTA 'L' stops: see `../cook-county-home-sales-2025/README.md` and `../chicago-l-stations/README.md`.

## Disclaimers

- For educational purposes only.
- Accuracy, completeness, etc. not guaranteed.
- Files were created in October 2026 and may be incomplete, outdated, transformed, filtered, or inconsistent with current official records by the time you use them.
- The tumor data are medical measurements; a two-feature classifier on them is a teaching example, not a diagnostic tool.
- Review upstream terms, licensing, and source documentation before reusing or redistributing.
