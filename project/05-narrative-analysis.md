---
summary: Start turning your analysis into a story (with findings, evidence, and limits)
topic: Telling the story
due: Sunday, November 15
ai_policy: yellow-over-red
draft: false
---

# Checkpoint Five: Narrative Analysis

Your group should now have a set of questions, documented data, an exploratory analysis, and tools for testing and modeling. This checkpoint asks you to clarify what you found and develop an evidence-based story.

A narrative analysis is the argument at the center of your project. Ideally, it will include multiple findings, the evidence behind each one, and some account of what might be missing (i.e. limitations).

For now, think of your audience as a skeptical classmate who knows data science, but did not work on your project, and they think their project is stronger than your project.

(The public-facing report (due November 25) and your presentation will retell this same story for a general audience)

As Claus Wilke puts it in [*Fundamentals of Data Visualization*](https://clauswilke.com/dataviz/telling-a-story.html), the goal is "telling a story and making a point." A notebook full of plots will not make a point. For this checkpoint, you must choose which results matter, put them in an order that answers your research questions, and say how sure you are (and why).

## What to do

Work in the same GitHub repository as the previous checkpoints. Your findings will go directly in the README for this checkpoint.

1. **State your findings.** Write two to four findings, each a single sentence that answers (part of) one of your research questions. A finding should be specific enough to be wrong. For example, instead of "Sleep matters for grades," go for something like "Students in our sample who reported fewer than six hours of sleep had lower median GPAs than those who reported seven or more, a gap of about X points." A finding can also be a null result ("We found no difference in..."), or a surprise from your exploratory analysis.
2. **Connect each finding with evidence.** For each finding, name the supporting evidence. This could be a comparison across groups, a hypothesis test, an estimate with an interval, a regression, a classifier, etc. Report the metrics along with their uncertainty (e.g. a confidence interval, a p-value with its test, or the variation across subgroups or models). Interpret each number for the reader, including what it cannot tell you (e.g. a small p-value says the difference is unlikely to be chance alone, but it says nothing about whether the difference is substantial).
	* Make one polished figure per finding, with a title that states the point/story/argument (e.g. "Late-night trips are twice as likely to be cancelled" rather than just "Cancellations by hour").
	* Reserve causal language ("causes," "leads to," "because of") only for analysis that specifically supports causality. Otherwise, describe the association (see [correlation and causality](/slides/week5.html#/correlation-and-causality) and [the elemental confounds](/slides/week6.html#/the-elemental-confounds)).
3. **Try to break each finding.** For each finding, write down at least one alternative explanation: a confounder, a subgroup that could reverse the pattern (see [Simpson's paradox](/slides/week5.html#/correlation-pitfalls-the-simpsons-paradox)), a quirk of how the data was collected, or random chance. Try to run at least one check against it, such as splitting by a subgroup, changing the time window, adding a control variable, or trying a second model. Also, list any analyses you ran that did *not* make it into the story, and why you left them out.
4. **Put the story in order.** Try to order your findings so that each one builds on the last. Note that this may differ from the order in which you did the work. For each finding, write one paragraph that explains it: the evidence from step 2 and the check from step 3. Write it as connected prose, not as a list of answers to these steps.

## What to turn in (i.e. what to put in the repo)

Your findings will go at the very top of `README.md`, above everything else, in a section with this structure:

```markdown
## Main Findings (Narrative Analysis)

- Finding one, in one sentence.
- Finding two, in one sentence.
- ...

### Finding one

One paragraph explaining the finding: the evidence and the check.

![Figure title that states the point](figures/finding-one.png)

### Finding two

...
```

Each finding gets one paragraph and one visualization. Every number and figure in the README should be traceable to code in your repository.

You might also find it helpful to have:

- A notebook, `narrative.ipynb`, that runs from top to bottom and produces every number and figure in the README section. It can import from or build on `eda.ipynb`.
- A `NARRATIVE.md` document for longer notes on your checks, linked from the README.
- A list of the analyses that did not make it into the story, and why (step 3).

Those are optional.

As before, every group member should have at least one commit for this checkpoint.

## What to submit

One submission per group in Canvas: the **URL of your group's GitHub repository**. Any group member can submit.

## Rubric

Eight points available:

1. Findings: two to four findings. Each should be a specific, checkable sentence tied to a research question. Null and negative results count as findings (as long as there is evidence).
2. Evidence: each finding has a named analysis (a comparison, test, estimate, regression, model, etc.) with its numbers reported alongside their uncertainty.
3. Interpretation: each number is interpreted for the reader (including uncertainty), and causal language appears only where the analysis supports it.
4. Figures: each finding has one polished figure with readable labels and a meaningful title.
5. Alternative explanations: each finding has at least one plausible alternative explanation (a confounder, a subgroup, a quirk of data collection, or chance).
6. Checks: at least one check is proposed or run against each alternative explanation
7. Narrative: the README opens with a "Main Findings (Narrative Analysis)" section that lists the findings as one-sentence bullets in a reasonable order (e.g. where each builds on the last), followed by one connected paragraph and one visualization per finding.
8. Reproducibility: every number and figure in the README traces to code in the repository, and every group member has at least one commit for this checkpoint.

## AI/LLM policy

**Yellow over red. Proceed with caution on the main route, prepared to stop at the next signal.**

🟡 You may use AI/LLM-based tools for the mechanics of analysis and plotting. For example, looking up how to run a test or fit a model in Python, fixing a figure's labels and layout, or debugging the notebook.

🔴 You may not use AI/LLM-based tools to write the README section (or `NARRATIVE.md`, if you have one), or to decide what your findings are. Use your own fleshy brains to identify the important findings, the alternative explanations, and the story you want to tell.

As with the earlier checkpoints, every number in the narrative should come from code (e.g. in `narrative.ipynb`) rather than direct output from an LLM.

## Sources

- Claus O. Wilke, *Fundamentals of Data Visualization*, [Chapter 29: Telling a Story and Making a Point](https://clauswilke.com/dataviz/telling-a-story.html).
- Claus O. Wilke, *Fundamentals of Data Visualization*, [Chapter 23: Balance the Data and the Context](https://clauswilke.com/dataviz/balance-data-context.html).
- Jessica Hullman and Nicholas Diakopoulos, ["Visualization Rhetoric: Framing Effects in Narrative Visualization"](https://doi.org/10.1109/TVCG.2011.255), *IEEE Transactions on Visualization and Computer Graphics* 17(12), 2011.
	- Data, visual representation, annotation, and interactivity as editorial layers.
- Roger D. Peng and Elizabeth Matsui, *The Art of Data Science*, [Chapter 10: Communication](https://bookdown.org/rdpeng/artofdatascience/chapter-communication.html).
- UC Berkeley Data 100, [Final Project Rubric](https://ds100.org/sp20/resources/assets/final_proj/New_Undergrad_DS_100_Final_Project_Rubric.pdf), Spring 2020.
- Cornell INFO 2950, [Project Description: Final Report](https://info2950.infosci.cornell.edu/project-description.html#final-report), Spring 2024.
- Kristin Stephens-Martinez, Duke CompSci 216, [Project: Final Report](https://sites.duke.edu/compsci216sp2022/2022/04/07/project-final-report/), Spring 2022.

## Example

TODO an example "Main Findings (Narrative Analysis)" README section. Coming soon.
