---
summary: Plot with matplotlib, seaborn, and plotly; practice EDA; visualization ethics
topic: Exploratory data analysis and visualization
due: Wednesday, October 14
ai_policy: yellow-over-red
---

# Coding Exercise Two: Sights

`Note that the starter code and other supporting files are only available in Canvas`

This exercise has four parts. You will warm up with `matplotlib`, work through a guided exploration of Washington D.C. bikeshare data, explore a Pew Research survey on your own and present your three best findings, and document your usage of AI tools.

## What you'll do

1. **Practice (5%)**: Customize a `matplotlib` plot: axis limits, a title, and a legend.
2. **Part 1 (35%)**: Guided EDA of hourly bikeshare trips: data granularity and time range, then bar charts, histograms with a fitted curve, boxplots, and scatterplots in `seaborn`, and the same boxplot and scatterplot redrawn in `plotly`.
3. **Part 2 (55%)**: Self-directed EDA of Pew Research's 2022 National Public Opinion Reference Survey (NPORS): answer questions about two visualizations and their ethical implications, reverse engineer one of them, run initial exploration, and present your three most significant findings, each with a headline, a visualization, and a 100-150 word description.
4. **Part 3 (5%)**: Write your statement on the use of AI tools.

## Environment

Use the `cs418env` environment you created for Exercise One. Part 2 reads an SPSS `.sav` file, which needs one extra package:

```sh
conda activate cs418env
pip install pyreadstat
jupyter notebook
```

If you install `pyreadstat` with the notebook already open, restart the kernel before loading the data.

## Starter code

**Download the starter zip from Canvas.** As with Exercise One, the starter files for this exercise are distributed only through Canvas, not through the course repository.

The zip folder contains:

- `hw2.ipynb`: the notebook with all of the instructions and the cells you fill in
- `bikeshare.csv`: the bikeshare data for Part 1
- `NPORS-2022-Data-Release/`: the survey data (`NPORS_2022_for_public_release.sav`) and the questionnaire that explains each variable (`2022-NPORS-Online-Questionnaire.pdf`)
- `q1.png`, `q1-4.png`, `q1-5.png`, `q1-6-1.png`, `q1-6-2.png`, `q2-1.png`, `q2-2.png`: the reference plots shown in the notebook
- `html_to_pdf.py`: a fallback for producing a clean PDF if your browser's print-to-PDF cuts things off

## What to submit

Two separate Gradescope submissions:

1. **02 Coding Exercise - Written**: `hw2.ipynb` saved as a PDF, with all cells executed and *all outputs visible*, including every plot. Tag each question when you upload. Save to PDF from your browser, or use `jupyter nbconvert hw2.ipynb --to html` followed by `python html_to_pdf.py` if the browser's output is cut off. Check the PDF before you submit it.
2. **02 Coding Exercise - Code**: your completed `hw2.ipynb`.

If either submission is missing, you lose 50% of the exercise.

You are welcome to work together with other students on this exercise if you want to, but **everyone must submit their own copy**.

**You can submit to Gradescope as many times as you like** and you are encouraged to use this to your benefit. Note that only the last submission counts, and if that one is late, the late policy applies to the whole exercise. All four parts are due at the same time.

## How it's graded

There is no autograder for this exercise. Everything is graded by hand from your PDF, so a plot that does not show up in the PDF does not count.

Part 2 is open-ended and is graded on the completeness of your plots and the insights you draw from them. Questions 2.4-2.6 are graded on whether they offer an interesting insight, follow visualization principles, and have an appropriate headline. A strong plot has a title, labelled and appropriately scaled axes, a legend if applicable, a carefully selected color scheme, and a main point accentuated through design choices. State any assumptions you make.

Point values within the notebook:

| Part | Question | Weight |
|:--|:--|--:|
| Practice — `matplotlib` | Q0 | 5% |
| Part 1 — Bikeshare EDA | 1.1 | 5% |
| | 1.2 | 6% |
| | 1.3 | 6% |
| | 1.4 | 6% |
| | 1.5 | 6% |
| | 1.6 | 6% |
| Part 2 — NPORS EDA | 2.1 (ethics) | 5% |
| | 2.2 | 4% |
| | 2.3 | 4% |
| | 2.4 | 14% |
| | 2.5 | 14% |
| | 2.6 | 14% |
| Part 3 — AI statement | Q3 | 5% |

**Extra credit (+1% to overall course grade)**: the 10 best visualizations and insights from Questions 2.4-2.6 (as judged by the TA) will each earn +1% to the overall course grade. To enter, mark the one visualization you want considered on Gradescope. We will showcase the winners in class.

## AI/LLM policy

**Yellow over red. Proceed with caution, stop ahead.**

🟡 You may use AI/LLM-based tools on the coding and analysis questions (Q0, Part 1, and Questions 2.2-2.6). Work carefully and be prepared to justify any use. Headlines, descriptions, and insights should still be your own. Document any use in Part 3 of the notebook: which tools, on which parts, what you prompted, whether the answer was any good, and what you changed. That documentation is worth 5% of the exercise.

🔴 You may not use AI/LLM-based tools on Question 2.1, the data ethics questions. Those are yours to think through with your own brain (otherwise there is no purpose in "completing" it).

The three phases are in the [syllabus](/syllabus/) and the [FAQ](/faq.html#double-red-no-aillm-based-tools).

## Note on tool counting

The starter folder keeps an anonymous count of tools activated to work on this exercise. One line is appended to `.tool-usage.log` when an AI coding agent (Claude Code, Codex, Gemini CLI, Cursor, Copilot CLI, or Copilot in VS Code) starts a session in that folder, when an editor (VS Code and its relatives, or PyCharm, DataSpell, and IntelliJ) opens the folder, or when the notebook's kernel starts. No name, username, email, hostname, file path, code, or prompt text is recorded or transmitted, and none of it is used for grading or for academic-integrity decisions. The class totals are published at [dodatascience.fun/meta-analytics/](/meta-analytics/). Full details are in the `README.md` inside the starter zip.

To opt out, you can create an empty file named `.tool-usage/opt-out` in the folder, set `CS418_NO_TOOL_USAGE_LOG=1` in your environment, or delete the `cs418_tool_usage` lines from the notebook's first code cell. Opting out has no effect on your grade.
