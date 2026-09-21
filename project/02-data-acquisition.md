---
summary: Find, obtain, and describe datasets your group will work with
topic: Obtaining data
due: Sunday, September 27
ai_policy: yellow-over-red
---

# Checkpoint Two: Data Acquisition

At this point, you hopefully have your team assembled around a topic of shared interest, and ideally even some initial research questions. The next step: go get some data!

For right now, you are encouraged to look at any datasets that could potentially address your topic of interest. This checkpoint is about obtaining datasets and knowing what is (and/or is not) available. You might obtain datasets which you later decide are not worth analyzing.

This checkpoint is intentionally early, to help you figure out if you might have a "dead end" research question with no available datasets. Some groups might discover their questions are answerable exactly as written with datasets already available. Other groups might discover that the available data "nudges" their questions.


## What to do

0. Set up a GitHub repo with your group
1. In the README, state your group's research questions in their current form.
2. Identify at least two primary datasets that seem to address the question(s)
3. Identify at least two secondary datasets you expect to join or compare against
4. Obtain the data! download it, pull it from an API, or scrape it... and load it into a dataframe.
5. Report the basic shape of what you have: number of rows, number of columns, what one row represents, the columns you care about and their types, and the time span and geography covered, etc.

## Where to look

- The [datasets pre-curated for this class](https://github.com/jackbandy/data-science-fun/tree/main/datasets).
- [Chicago Data Portal](https://data.cityofchicago.org/), [data.gov](https://data.gov/), and other government open data portals.
- The data behind a study you read: many papers link a replication package or a public repository.

## How to set up your group's GitHub repository

Each group turns this checkpoint in from a shared GitHub repository, which you will also use for future checkpoints. Set it up:

1. **One person creates the repo.** On [github.com](https://github.com/), click *New repository*, name it something recognizable (e.g. `cs418-chicago-transit`), and initialize it with a README.
	* A public is fine; private also works as long as you add the instructor and TAs as collaborators.
2. **Add your teammates as collaborators.** In the repo, go to *Settings -> Collaborators -> Add people* and add every group member by their GitHub username, so everyone can push.
3. **Everyone clones it locally**, e.g. `git clone https://github.com/<owner>/<repo>.git`, and commits their own work. Each group member should have at least one commit by the time you submit -- I look at the commit history to see that the work was shared.
4. **Put the data-acquisition work in the repo.** At minimum: a notebook (`data_acquisition.ipynb`) or script that loads each dataset into a dataframe and prints its shape, and a `README.md` that answers the five prompts above.
5. **Keep large raw files out of the repo.** GitHub rejects files over 100 MB and gets slow well before that. If a dataset is big, commit the download/API code plus a small sample, and note in the README where the full file comes from.
	* You will probably also want to add a `.gitignore` with the data directory in it.

## What to submit

One submission per group in Canvas: the **URL of your group's GitHub repository**. Any group member can submit; list every member's name the repo README.

## Rubric

Five points available (one for each of the five prompts above):

1. Your group's research questions are stated in their current form, clearly enough that a reader can tell what data would address them. These should be in README.md
2. At least two primary datasets are identified, each with a source and a link (also in README.md)
3. At least two secondary datasets are identified, with a sentence on what you would join or compare them against (also in README.md)
4. Confirm that the data has actually been obtained and loaded into a dataframe, (include the Python script, notebook, or whatever was used to do so)
5. A few notes about the shape of what you have: rows, columns, what one row represents, the columns you care about and their types, coverage, etc. (also in README.md)

## AI/LLM policy

**Yellow over red. Proceed with caution on the main route.**

🟡 You may use AI/LLM-based tools to search for candidate datasets, and for the mechanics of getting a file into a dataframe, e.g. reading an API's documentation, working out the right `read_csv` arguments for an awkward file, browsing the web for relevant datasets, etc.

🔴 You may not use AI/LLM-based tools to write the memo, and you may not report a dataset's shape or contents from what a tool told you. Every number you report should come from data you actually loaded and looked at with code of your own (note that LLMs will happily invent datum, data, metadata, etc. that do not exist)