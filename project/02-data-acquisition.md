---
summary: Find, obtain, and describe datasets your group will work with
topic: Obtaining data
due: Wednesday, September 23
ai_policy: red-yellow
---

# Checkpoint Two: Data Acquisition

At this point, you hopefully have your team assembled around a topic of shared interest, and ideally even some initial research questions. The next step: go get some data!

For right now, you are encouraged to look at any datasets that could potentially address your topic of interest. This checkpoint is about *obtaining* the data and *knowing what is available*, so you might obtain datasets which you later decide are not worth analyzing.

This checkpoint is intentionally early, to help you figure out if you might have a "dead end" research question with no available datasets. Some groups might discover their questions are answerable exactly as written with datasets already available. More often, groups will discover that the available data "nudges" their questions into a different shape. 


## What you'll do

1. State your group's research questions in their current form.
2. Identify at least two primary datasets that seem to address the question(s)
3. Identify at least two secondary datasets you expect to join or compare against
4. Obtain the data! download it, pull it from an API, or scrape it... and load it into a dataframe.
5. Report the basic shape of what you have: number of rows, number of columns, what one row represents, the columns you care about and their types, and the time span and geography covered, etc.

## Where to look

- The [datasets pre-curated for this class](https://github.com/jackbandy/data-science-fun/tree/main/datasets).
- [Chicago Data Portal](https://data.cityofchicago.org/), [data.gov](https://data.gov/), and other government open data portals.
- The data behind a study you read: many papers link a replication package or a public repository.

## What to submit

One PDF submission per group in Canvas. (TODO setup submission)

## Rubric

Five points available, one for each of the five prompts above:

1. Your group's research questions are stated in their current form, clearly enough that a reader can tell what data would address them.
2. At least two primary datasets are identified, each with a source and a link.
3. At least two secondary datasets are identified, with a sentence on what you would join or compare them against.
4. Confirm that the data has actually been obtained and loaded into a dataframe
5. The shape of what you have is described: rows, columns, what one row represents, the columns you care about and their types, and the coverage.

## AI/LLM policy

**Red/yellow — proceed with caution on the main route.**

🟡 You may use AI/LLM-based tools to search for candidate datasets, and for the mechanics of getting a file into a dataframe, e.g. reading an API's documentation, working out the right `read_csv` arguments for an awkward file, browsing the web for relevant datasets, etc.

🔴 You may not use AI/LLM-based tools to write the memo, and you may not report a dataset's shape or contents from what a tool told you. Every number you report should come from data you actually loaded and looked at. Chatbots will happily invent a plausible-sounding dataset that does not exist, so you need to verify!
