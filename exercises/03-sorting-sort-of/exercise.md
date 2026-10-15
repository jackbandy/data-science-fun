---
summary: Classify tweets with NLTK and scikit-learn SVMs; compare against an LLM; ethics reflection
topic: Supervised machine learning
due: Wednesday, October 28
ai_policy: yellow-over-red
---

# Exercise Three - Sorting, Sort Of

`Note that the starter code and other supporting files are only available in Canvas`

This exercise sorts tweets from six political accounts into two parties. You will process and featurize the text, train and select a support vector machine classifier, compare it against predictions from the Gemini API, answer a few data ethics questions, and document your usage of AI tools.

## Starter code

**Download `cs418-fa26-ce03.zip` from Canvas.** As with the earlier exercises, the starter files are distributed only through Canvas, not through the course repository. Open `hw3.ipynb` and follow the instructions there, which cover the environment, what to submit to Gradescope, and how each question is graded.

You are welcome to work together with other students on this exercise if you want to, but **everyone must submit their own copy**.

## AI/LLM policy

**Yellow over red. Proceed with caution, stop ahead.**

🟡 You may use AI/LLM-based tools on the text processing, feature construction, classification, and LLM questions (Q1-Q14). Part D asks you to use the Gemini API directly. Work carefully and be prepared to justify any use. Document any other use in Q16 of the notebook: which tools, on which parts, what you prompted, whether the answer was any good, and what you changed. That documentation is worth 5% of the exercise.

🔴 You may not use AI/LLM-based tools on Q15, the ethics and machine learning questions. Those are yours to think through with your own brain.

The three phases are in the [syllabus](/syllabus/) and the [FAQ](/faq.html#double-red-no-aillm-based-tools).

## Note on tool counting

As in Exercise Two, the starter folder keeps an anonymous count of the tools used on it: AI coding agents starting a session, VS Code and its relatives opening the folder, and the notebook's kernel starting. No name, username, email, hostname, file path, code, or prompt text is recorded or transmitted, and none of it is used for grading or for academic-integrity decisions. The class totals are published at [dodatascience.fun/meta-analytics/](/meta-analytics/), and the full details, including how to opt out, are in the `README.md` inside the starter zip.
