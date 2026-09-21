---
summary: Wrangle flight data with pandas; web scraping; ethics reflection
topic: Data wrangling and web scraping
due: Wednesday, September 30
ai_policy: double-yellow
---

# Exercise One - Gate Check

`Note that the starter code and other supporting files are only available in Canvas`

This exercise has four parts. You will work through a set of `pandas` operations on real flight data, collect data from an API and from web pages, answer a few questions about data collection ethics, and document your usage of AI tools.

## What you'll do

1. **Part 1 (40%)**: Data processing with `pandas`: slicing, filtering, grouped counts, joins, and missing values, then three questions on the Department of Transportation's January 2016 "On-Time" flight data for flights out of SFO and OAK.
2. **Part 2 (50%)**: Web scraping and data collection: HTTP requests, the Yelp Fusion API (authentication, parameterization, pagination), parsing JSON and HTML, and crawling paginated pages with BeautifulSoup.
3. **Part 3 (5%)**: Data science ethics: read the SmartSpecs/KnowItAll scenario and answer three questions about harms, benefits, rights, and obligations, 100-150 words each.
4. **Part 4 (5%)**; Write your statement on the use of AI tools.

Note that Part 1 uses `pandas`, not the `polars` we used in Exercise Zero. Both are worth knowing, and you will see plenty of `pandas` code in the wild.

## Environment

This exercise is autograded in a fixed environment, so your library versions need to match. Install [Anaconda](https://www.anaconda.com/download) for Python 3.13, then create and activate the course environment:

```sh
conda create -n cs418env python=3.13 anaconda
conda activate cs418env
jupyter notebook
```

Full setup instructions, including what to do if you already have an older Anaconda, are in the `README.md` inside the starter zip.

## Starter code

**Download the starter zip from Canvas.** Unlike Exercise Zero, the starter files for this exercise are distributed only through Canvas, not through the course repository.

The zip folder contains:

- `hw1.ipynb`: the notebook with all of the instructions and the cells you fill in
- `warmup.ipynb`: an ungraded warm-up on Python and Jupyter basics; do this first if you are new to either
- `hw1part1.py`, `hw1part2.py`: skeleton functions you copy your Part 1 and Part 2 answers into, which is what the autograder runs
- `airports.dat`, `flights.dat`, `parse_page_test1.html`, `parse_page_test2.html`: the data files
- `run_tests_sample.py`, `tests_sample_part1/`, `tests_sample_part2/`: a sample of the autograder's tests, which you can run locally
- `html_to_pdf.py`: a fallback for producing a clean PDF if your browser's print-to-PDF cuts things off

Run the sample tests from the exercise directory:

```sh
python run_tests_sample.py part1
python run_tests_sample.py part2
```

## What to submit

Two separate Gradescope submissions:

1. **01 Coding Exercise (Written)** (60%): `hw1.ipynb` saved as a PDF, with all cells executed and *all outputs visible*. Save to PDF from your browser, or use `jupyter nbconvert hw1.ipynb --to html` followed by `python html_to_pdf.py` if the browser's output is cut off. Check the PDF before you submit it.
2. **01 Coding Exercise (Code)** (40%): a zip containing `hw1part1.py`, `hw1part2.py`, and `hw1.ipynb`. Zip the *files*, not the folder that contains them, so they land at the root of the archive.

You can submit to Gradescope as many times as you like; only the last submission counts, and if that one is late, the late policy applies to the whole exercise. All four parts are due at the same time.

## How it's graded

The written submission is graded on completion: having run everything, shown the output, and answered the questions in Parts 3 and 4. The Part 3 answers are PASS/FAIL: you pass as long as the answer makes a serious attempt, stays on topic, and shows you understand the concepts.

The code submission is graded by the autograder, which runs tests against `hw1part1.py` and `hw1part2.py` (not the notebook). The sample tests in `tests_sample_part1/` and `tests_sample_part2/` are a subset; the rest are hidden.

Point values within the notebook: Questions 1.1-1.3 are 12%, 13%, and 5%; Questions 2.1-2.7 are 5%, 15%, 9%, 7%, 4%, 6%, and 4%; Questions 3.1-3.3 are 1%, 2%, and 2%; Part 4 is 5%.

## AI/LLM policy

**Double yellow: proceed with caution at restricted speed.**

🟡 You choose where AI/LLM tools fit into your workflow on Parts 1 and 2, but every use is at reduced speed and full attention, and you should be prepared to justify it. Document your use in Part 4 of the notebook: which tools, on which parts, what you prompted, whether the answer was any good, and what you changed. That documentation is worth 5% of the exercise.

🔴 Part 3, the ethics questions, is yours to think through. Using an AI/LLM tool there defeats the point of the exercise.

The three phases are in the [syllabus](/syllabus/) and the [FAQ](/faq.html#double-red-no-aillm-based-tools).

## Note on usage counting

The starter folder keeps an anonymous count of how often AI coding tools are opened on this exercise. If you start a session with Claude Code, Codex, Gemini CLI, Cursor, or Copilot CLI in that folder, one line is appended to `.ai-usage.log`: tool name, whether the session started or ended, the time, and a random id generated in that folder. No name, username, email, hostname, file path, code, or prompt text is recorded or transmitted, and none of it is used for grading or for academic-integrity decisions. The class totals are published at [dodatascience.fun/meta-analytics/](/meta-analytics/).

To opt out, you can create an empty file named `.ai-usage/opt-out` in the folder, or set `CS418_NO_AI_USAGE_LOG=1` in your environment. Opting out has no effect on your grade.
