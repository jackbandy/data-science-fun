# Ethics in Obtaining Data

**[← Back to Course Homepage](../../index.html)**

::: {#fig-ds-lifecycle-obtain-data}
<img src="../../assets/lifecycle/ds-lifecycle-v2.svg" alt="The step of obtaining data, in the context of the data science lifecycle." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Obtaining data, in the context of the data science lifecycle.
:::

🔴 *Chapter Status: in development. Some sections drafted, mostly incomplete.*

The process of obtaining data is perhaps the aspect of data science with the most concrete and direct ethical implications.

## Where do data come from?

> "'Raw data' is an oxymoron."

-- Lisa Gitelman and Virginia Jackson [@gitelman_jackson_introduction_2013]

Do you generate it?
Do you collect it?
Do you obtain it?
Are data "given" or "taken?" [@barrowman_data_never_raw_2018]
* "Data collection itself already is a form of processing."

## The rhetoric of "raw" data

* calling data "raw" is itself a persuasive move [@gitelman_jackson_introduction_2013]
* More TK

## Sidebar: Can you start/end with data?
TK

## What "obtaining data" includes

TK
* primary and secondary data sources
* synthetic data

## Sensitive information

TK

### Defining Sensitive Information

### Handling Sensitive Information

## Risks from data triangulation

TK

## Maintaining Data

Although not formally captured in the data science lifecycle figure(s), data scientists are often responsible for maintaining the data they obtain and analyze.

* "data stewardship"
* backups and retention

## Example: How the Census Obtains Data

The U.S. census offers a helpful example of ethical decision-making in the data science lifecycle. It has been explored in Data Feminism, as well as X and Y and other materials. It is included here in brief as a canonical example of subjectivity in the process of obtaining data.

### Census form in 1790

[Massachusetts printed schedule used in the 1790 census](../../assets/census/1790-massachusetts-printed-schedule.pdf).

Categories in the 1790 census: free White males 16 and over, free White males under 16, free White females, all other free persons, and slaves.

::: {#fig-census-1790}
<img src="../../assets/census/1790-massachusetts-printed-schedule.png" alt="Massachusetts printed schedule used in the 1790 census." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

Massachusetts printed schedule used in the 1790 census. Source: Census Bureau questionnaire page [@census_1790_questionnaire] and National Archives scan hosted by Census.gov [@national_archives_1790_schedule].
:::

### Census form in 1850

[Free Inhabitants schedule](../../assets/census/1850-free-inhabitants-schedule.png).

Categories: name, age, sex, color, occupation, value of real estate, birthplace, married within the year, school attendance, literacy, deafness, dumbness, blindness, insanity, idiocy, pauper status, and conviction.

::: {#fig-census-1850}
<img src="../../assets/census/1850-free-inhabitants-schedule.png" alt="1850 Free Inhabitants schedule." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

The 1850 Free Inhabitants schedule. Source: Census Bureau questionnaire page [@census_1850_questionnaire] and direct image file from Census.gov [@census_1850_free_inhabitants_image].
:::

### Census form in 1940

[Population questionnaire](../../assets/census/1940-population-questionnaire.pdf).

Categories: name, relationship, personal description, residence, birthplace, citizenship, education, employment, occupation, income, veteran status, Social Security, and selected supplemental questions for sample respondents.

::: {#fig-census-1940}
<img src="../../assets/census/1940-population-questionnaire.png" alt="1940 population questionnaire." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

The 1940 population questionnaire. Source: Census Bureau questionnaire page [@census_1940_questionnaire] and direct PDF from Census.gov [@census_1940_population_pdf].
:::

### Census form in 2020

[Informational bilingual questionnaire](../../assets/census/2020-informational-questionnaire.pdf).

Categories: household count, ownership or tenure, phone number, name, sex, age and date of birth, Hispanic/Latino/Spanish origin, race, relationship, and whether the person usually lives or stays elsewhere.

::: {#fig-census-2020}
<img src="../../assets/census/2020-informational-questionnaire.png" alt="2020 informational bilingual questionnaire." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color); padding: 10px;" />

The 2020 informational bilingual questionnaire. Source: Census Bureau questionnaire page [@census_2020_questionnaire] and direct PDF from Census.gov [@census_2020_informational_pdf].
:::

Notes from Wikipedia's "Race and ethnicity in the United States census," section "Relation between ethnicity and race in census results" [@wikipedia_race_ethnicity_census]:

* treats `Hispanic or Latino` as ethnicity, not race, so it asks as separate questions.
* In `2000`, a large share of Hispanic/Latino respondents selected `Some other race`, showing a mismatch between official categories and how respondents describe themselves.
* Since `2000`, respondents have been allowed to select more than one race, so race totals can exceed the total population (not directly comparable with older censuses).

## Example: Facebook Profile

Similar dynamics can be observed in the Facebook signup process: the process of "obtaining data" involved numerous subjective decisions. Until 2014, the signup process for Facebook offered three options in the gender field: male, female, or no answer. On February 13, 2014, Facebook substantially expanded its gender fields, with 58 different options, custom fields, and additional pronoun settings.

Sources: ABC News [@abcn_news_facebook_gender_2014] and CNN [@kelly_facebook_gender_2014].

## References
