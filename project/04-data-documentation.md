---
summary: Write a formal "datasheet" for your dataset(s)
topic: Documenting data
due: Wednesday, October 28
ai_policy: yellow-over-red
---

# Checkpoint Four: Data Documentation

Your group has obtained its data and explored it, so at this point, you should be ready to make some decisions about what you will use going forward.

To help cement this decision, this checkpoint asks for more formal documentation about your dataset(s). It is similar to the initial data acquisition checkpoint, but it should include more details regarding where the dataset came from, what one row means, who and what the dataset covers, what the dataset leaves out, how a stranger could rebuild the dataset (from scratch!), and more.

You might think of your "audience" as a group of students in CS 418 in the year 3026. Although your GitHub profile is no longer active in 3026, the group has recovered your repository from the [arctic code vault](https://archiveprogram.github.com/arctic-vault/), and they want to know whether they can trust and reuse your data for historic research.

Most of you are documenting data that someone else collected, and some questions can only be answered by others. In such cases, try to find their documentation, cite it, and quote it in as much detail as possible. Write "not documented by the publisher" when appropriate.

## What to do

Work in the same GitHub repository as the previous checkpoints.

1. **Write a datasheet for each primary dataset.** Follow the seven sections from Gebru et al.'s ["Datasheets for Datasets"](https://doi.org/10.1145/3458723), answering the questions that apply to your data:
	- *Motivation*: Why was the dataset created? Who created it, and who funded it?
	- *Composition*: What does one row represent? How many rows are there? Is it every possible instance, or a sample? What is missing, and why?
	- *Collection process*: How was the data gathered (sensors, surveys, administrative records, scraping)? Over what time frame? If it is about people, did they know or consent?
	- *Preprocessing*: What cleaning or labeling did the publisher do before you got it? Is the raw data available?
	- *Uses*: What has it been used for already? What should it *not* be used for?
	- *Distribution*: How is it published, and under what license or terms of use?
	- *Maintenance*: Who maintains it? Is it updated, and how would you know?
2. **Define the scope.** For each research question, name the target population, the access frame, and the sample, as in [*Learning Data Science*, Section 2.2](https://learningds.org/ch/02/data_scope_construct.html) and the [week 3 scope slides](/slides/week3.html#/is-the-data-in-scope).
	- This will help readers know who or what is in your question but missing from the data, and what that limits you from claiming.
3. **Write a codebook.** Following Ellis and Leek's ["How to Share Data for Collaboration"](https://doi.org/10.1080/00031305.2017.1375987), make a table with one row for every column you use, including columns you created: name, data type, units, what it means, the range or allowed values, how missing values are coded, and where it comes from (the raw source or the code that derives it). A markdown table in `DATASHEET.md` works.
4. **Share the recipe.** List, in order, every step that turns the raw files into the dataframe you analyze: downloads, filters, type fixes, dropped rows, and joins with your secondary datasets. Each step should point to the code that does it. For each join, give the key, and report how many rows matched and how many did not. Someone with only your repository should be able to rebuild your data by following the list.
5. **Document access and reuse.** Using the [FAIR principles](https://doi.org/10.1038/sdata.2016.18) (findable, accessible, interoperable, reusable) as a checklist, record for each dataset: a persistent link, the version or date you accessed it, the file format, the license or terms of use, and whether others may reuse the processed data you are producing.
6. **Consider any people in the data.** If your datasets capture people in any way, even indirectly, describe the representation as well as which groups could be (mis)represented by the data.
	* The [CARE principles](https://doi.org/10.5334/dsj-2020-043) (collective benefit, authority to control, responsibility, ethics) were written for Indigenous data governance and are a useful lens. If your data does not describe people, consider anyone who may be affected by decisions made using the data.

## Formatting Note

I recommend putting your datasheet in a "nutrition label" style, based on Holland et al.'s [Dataset Nutrition Label](https://arxiv.org/abs/1805.03677). This makes for a very readable summary, including written metadata with statistics and plots. Alternative formats are listed in the sources section below.

For example, here is the summary card from Bandy and Vincent's [retrospective datasheet for BookCorpus](https://arxiv.org/abs/2105.05241) ([PDF](/assets/datasheets/bookcorpus-data-card.pdf), and an [Overleaf template](https://www.overleaf.com/read/dqwhpqnvftky) you can copy and modify):

![Summary data card for BookCorpus, in the style of a nutrition label](/assets/datasheets/bookcorpus-data-card.svg){: width="400"}

The [Data Nutrition Project](https://datanutrition.org/label/) publishes more labels in this style, including:

- [ASL Citizen](https://labelmaker.datanutrition.org/label/d3e1b747-7306-4cbf-8bef-f4422749e8d8), crowdsourced videos of American Sign Language signs, collected with consent.
- [2024 ISIC Challenge SLICE-3D](https://labelmaker.datanutrition.org/label/6167d533-9d94-4afd-8e74-b3187175bc19), de-identified images of skin lesions.
- [Measuring Massive Multitask Language Understanding](https://labelmaker.datanutrition.org/label/2d5e0059-94ae-40c5-b65a-f7abc6d13e7f), a multiple-choice benchmark for language models.

## Sources

- Timnit Gebru et al., ["Datasheets for Datasets"](https://doi.org/10.1145/3458723), *Communications of the ACM* 64(12), 2021.
	- Motivation, composition, collection process, preprocessing, uses, distribution, and maintenance.
- Sarah Holland et al., ["The Dataset Nutrition Label: A Framework To Drive Higher Data Quality Standards"](https://arxiv.org/abs/1805.03677), arXiv, 2018.
- Sam Lau, Joey Gonzalez, and Deb Nolan, *Learning Data Science*, [Chapter 2: Questions and Data Scope](https://learningds.org/ch/02/data_scope_intro.html).
	- Target population, access frame, and sample.
- Mark D. Wilkinson et al., ["The FAIR Guiding Principles for Scientific Data Management and Stewardship"](https://doi.org/10.1038/sdata.2016.18), *Scientific Data* 3, 2016.
	- Findable, accessible, interoperable, reusable.
- Stephanie Russo Carroll et al., ["The CARE Principles for Indigenous Data Governance"](https://doi.org/10.5334/dsj-2020-043), *Data Science Journal* 19, 2020.
	- Collective benefit, authority to control, responsibility, ethics.
- Shannon E. Ellis and Jeffrey T. Leek, ["How to Share Data for Collaboration"](https://doi.org/10.1080/00031305.2017.1375987), *The American Statistician* 72(1), 2018.
	- Raw data, tidy data, a codebook, and an explicit recipe from one to the other.
- Emily M. Bender and Batya Friedman, ["Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science"](https://doi.org/10.1162/tacl_a_00041), *Transactions of the Association for Computational Linguistics* 6, 2018.
- Mahima Pushkarna, Andrew Zaldivar, and Oddur Kjartansson, ["Data Cards: Purposeful and Transparent Dataset Documentation for Responsible AI"](https://doi.org/10.1145/3531146.3533231), FAccT 2022. Dataset documentation as practiced at Google.

## What to turn in (i.e. what to put in the repo)

- A `DATASHEET.md` document with all six parts above
- An update to `README.md` with a short "Data documentation" section that links to `DATASHEET.md`, lists each dataset with its source and license, and states the biggest limitation of your data in a sentence or two.

As before, every group member should have at least one commit for this checkpoint.

## What to submit

One submission per group in Canvas: the **URL of your group's GitHub repository**. Any group member can submit.

## Rubric

Six points available (one for each step above):

1. Datasheets: each primary dataset has a datasheet covering the seven sections, with answers cited to the publisher's documentation, and gaps marked as undocumented.
2. Scope: each research question has its target population, access frame, and sample named, with a statement of who or what is missing and what that limits.
3. Codebook: every column used in the analysis, including derived columns, has its type, units, meaning, range or allowed values, missing-value coding, and origin.
4. Recipe: the steps from raw files to the analysis dataframe are listed in order, each linked to code, with the key and the matched and unmatched row counts for every join.
5. Access and reuse: each dataset has a persistent link, access date or version, format, license or terms of use, and a statement of whether others may reuse your processed data.
6. People in the data: the document describes how people are represented in the data and which groups could be (mis)represented, or, if the data does not describe people, who may be affected by decisions made using it.

## AI/LLM policy

**Yellow over red. Proceed with caution on the main route.**

🟡 You may use AI/LLM-based tools to help locate a publisher's documentation, license, or methodology page, and for the mechanics of formatting, e.g. turning your notes into a markdown table.

🔴 You may not use AI/LLM-based tools to write `DATASHEET.md` or the README section. Do not take any fact about a dataset (who made it, how it was collected, what a column means, what the license allows) from an LLM's answer. Every claim should trace to the publisher's own documentation, which you cite, or to code you ran. LLMs will confidently describe collection methods and column definitions that do not exist, and documentation is exactly where that does the most damage.

## Example

TODO an example `DATASHEET.md`. Coming soon.
