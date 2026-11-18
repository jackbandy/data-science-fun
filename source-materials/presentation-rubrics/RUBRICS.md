# Five example presentation rubrics for group data-science projects

_Note: this file was drafted by an LLM coding system and has not yet been reviewed._

Collected 2026-11-18 as reference material for the presentation checkpoint (`project/07-presentation.md`). Every quotation below was copied from the page or PDF it is attributed to, fetched directly from the publisher on that date, not from a search summary. The point of the collection is the range of decisions other courses made about scope, timing, evidence, and what to grade, so the checkpoint page can make those decisions explicitly rather than by default.

| Source | Course | Talk length | Scale |
|:--|:--|:--|:--|
| University of Chicago Data Science Clinic | Clinic mid-quarter talks | 3–5 min | 60 points, two headings |
| University of Toronto | APS360, applied deep learning | 6–8 min | 25 points, six criteria, 1–4 levels |
| Michigan State University | CMSE 202, computational modeling | 10 min max | 25 points, four named levels |
| University of Washington | GDA (data science minor), winter 2025 | ~5–7 min | 20 points, per-section weights |
| Cornell University | INFO 2951, data science for social science | 5 min max | five categories, three levels |

## 1. University of Chicago, Data Science Clinic

"Mid-Quarter Presentation Grading Rubric." <https://clinic.ds.uchicago.edu/rubrics/mid-quarter-presentation-rubric.html>

The strictest and shortest of the five, and the one that is most opinionated about what a talk is for.

> The purpose of the mid-quarter presentation is to share what you are working on with the rest of the clinic. These are "quick" lightning talks that are designed to share basic information about the project. The goal isn't to focus on the specifics, but to describe the general parameters of the problem and highlight interesting aspects.

> When planning your talk keep focused on the core of your project. This presentation is not a catalog, but a high-level map of the project.

Audience calibration is stated as an assumption the presenters must adopt:

> You should assume that your audience is like you:
> - Has a grounding, but isn't an expert in statistics / programming / machine learning techniques, etc.
> - Isn't that interested in the nitty-gritty details, derivations, etc.

Time is a hard limit with a stated reason, and the rubric says shorter is better:

> There is a strict time limit on the presentation (3-5 minutes). Historically the best presentations tends to be about 4 minutes long because they focus the project down to a manageable level. Presentations that go the entire five minutes (usually) are too long, not specific enough and are more poorly received, grade-wise.

Graded out of 60, in two headings only: *Slides* (20 points) asks "Are there obvious grammar errors, spelling problems or formatting issues?" and "Are the slides at the appropriate understanding level?"; *Presentation* (40 points) asks "Are the presenters speaking loudly and clearly?", "Are the presenters showing enthusiasm?", "Are the presenters looking at the crowd or staring at the slides?", "Were questions answered?", and "Was the problem well framed? Was the detail level appropriate?"

The dos and don'ts carry most of the practical guidance:

> - Do not read lists of numbers from the slides.
> - No screenshots of tables or code. There should be no code.
> - No videos. To ease the logistics all presentations will be done from a single laptop that may not be able to display it correctly. Assume that the presentation will be static.
> - Do not try to teach. Explaining how a neural network or deep learning works, mathematically defining multiple accuracy measures, etc. are beyond the scope of this presentation. You are trying to meet the audience where they are, not teach.

Also worth copying: "Groups that miss their designated presentation day will receive a grade of zero," and the rehearsal instruction, "Rehearse your presentation 2-3 times, making sure that you stay within the allotted time."

## 2. University of Toronto, APS360 (applied deep learning)

"APS360. Project Presentation Handout and Rubric." <https://www.cs.toronto.edu/~lczhang/360/files/rubric_presentation.pdf>

The most useful structural idea in the collection: the rubric is written from the audience's side of the room.

> To help you keep your audience in mind, the rubric is written in terms of the effect that your presentation should have on the audience.

Every level of every criterion is then a statement about what the audience ends up knowing. For example, from *Problem* (out of 4):

> Excellent (4/4): – Within the first couple minutes of the presentation, the audience can clearly understand why the problem is interesting or important. – The audience has a clear picture of the kind and amount of data you're working with, and any potential limitations of your data. – A TA or good student in the audience should be able to come up with rudimentary ideas of how to solve your problem based on the information presented in the first couple minutes.

and from *Results* (out of 4), the demand that a talk be auditable rather than merely persuasive:

> The audience knows how you chose which qualitative results to display, and has the sense that the group is forthcoming in the presentation.

Time is handled twice, once as a rule for who speaks and once as a penalty:

> Each presentation will be 6-8 minutes in length. To ensure that every student has the opportunity to practice their presentation skills, each team member should speak for at least 1.5 minutes.

> There will be a 10% penalty for a presentation that exceeds 8 minutes.

The presentation is graded out of 25 across six criteria: Problem (4), Data Processing (4), Model (4), Results (4), Discussion (4), Presentation Flow (5). Each has five levels (Excellent, Good, Fair, Poor, and Marginal for flow), and the criteria are fixed while the content order is not: "The content don't have to be covered in that precise order."

The stated bar for a good talk is social, not just technical:

> A successful presentation should draw further interest to your work. An excellent presentation will encourage your classmates to talk to you after class.

## 3. Michigan State University, CMSE 202

"CMSE 202 Final Project: Requirements and Grading Rubric," Fall 2026. <https://msu-cmse-courses.github.io/cmse202-Fall2026/course_materials/CMSE202_FinalProjectRequirementsAndGradingRubric.html>

Closest to CS 418 in format: a written report, a repository, and a group talk, graded together, at the end of a semester with a November/December deadline.

> Each presentation should be no more than 10 minutes long and should include appropriate visual aids. The presentation should be divided roughly evenly between all group members (i.e. one person shouldn't do all of the talking).

The talk and report share one content list, which keeps the two from drifting apart:

> - The question(s) you set out to answer.
> - Any models, expressed in broad mathematical terms, that you applied to your chosen data or chosen topic.
> - The computational techniques that you used to analyze your data or run your model. This should include an explanation of any pre-existing python-based libraries or packages that you used to aid in your project.
> - The answer(s) you arrived at.
> - The difficulties or complications you ran into with your project and what you did to try to cover overcome these difficulties.

Slide guidance is given as a rate rather than a hard count, plus one line worth stealing for the "no code on slides" case in CS 418:

> You should aim for having a reasonable number of slides – a good rule of thumb is ~1 min of time per slide.

> Only include text and figures that support the presentation (avoid including content "just because").

The presentation and slides are 25% of the project grade, and part of that comes from classmates: "10 of the 25 points will come from a peer-review-based 'score' of your presentation. The remaining 15 points will be an instructor-based assessment." The four level descriptions are behavioral, e.g. "Excellent presentation: student speaks clearly and in a logical manner, and makes their key points clear. They use eye contact and minimally use notes. Slides conform to specifications in final presentation document, including number of slides, adequately addressing all points, legibility." A warning makes the group grade conditional on individual contribution:

> Each student is expected to contribute to all components of the project to receive the group grade in that category. Non-participation could result in loss of points beyond just the collaboration grade!

## 4. University of Washington, GDA (winter 2025)

"Final presentation and repository rubrics," GDA course JupyterBook. <https://gda-wi25-jupyterbook.readthedocs.io/en/latest/resources/project/rubric.html>

The clearest example of weighting the parts of a talk, which is what makes a four-point rubric legible to students: they can see where the points sit.

> **Presentation rubric (20 pts)**
>
> **Problem / Background / Context [3 points]**
> Was there sufficient information presented for the audience to understand what the team is trying to accomplish?
>
> **Datasets / Methods [3 points]**
> Were datasets and methods discussed, and if so did the team effectively convey how they would be used to answer the research question?
>
> **Results / Analysis [5 points]**
> Did the team convey their results effectively?
> Quality visual aids?
>
> **Conclusion / Future Directions [3 points]**
> Did the team describe their interpretation of their results?
> Did they attempt to answer their research question?
> Did they describe shortcomings or next steps in this project were to be continued?
>
> **Overall Organization / Flow / Clarity [3 points]**
> Was the presentation structured well?
> Did the team effectively convey information?
>
> **Within Time Limit [1 points]**
> Did the team finish their presentation in time?
>
> **Q&A [2 points]**
> Were the audience's questions given a good faith attempt to answer?
> Did the group seem knowledgeable on their topic?

Two features worth copying: answers are worth points on the same footing as delivery, and finishing on time is worth a point of its own rather than a penalty that only fires when a group runs over.

## 5. Cornell University, INFO 2951

"Presentation," INFO 2951 course site, January 29, 2026. <https://info2951.infosci.cornell.edu/project/presentation.html>

The only one of the five that grades a small, fixed deck and treats slides as a *support* to speech, with peer evaluation as part of the record.

> The presentation must be no longer than 5 minutes.

> The slide deck should have no more than 6 content slides + 1 title slide.

> These slides should serve as a brief visual addition to your written report and will be graded for content and quality.

A suggested slide order is offered as a suggestion, not a requirement ("Here is a suggested outline as you think through the slides; you do not have to use this exact format for the 6 slides"), and it doubles as a template for any talk that follows the project's checkpoints: introduce the topic and motivation, introduce the data, highlights from EDA, inference/modeling/other analysis, conclusions and future work.

Evaluation is a three-column table, *Less developed projects* / *Typical projects* / *More developed projects*, over five categories: Time management, Professionalism, Slides, Creativity/originality, Content. The *Content* row is the one to borrow, because it grades the limits rather than just the claims:

> - **Less developed:** Research question is unclear. Hypotheses and analysis do not clearly address the research question. Limitations are glossed over or ignored entirely.
> - **Typical:** Research question is stated. Hypotheses and analysis address the research question. Limitations are noted.
> - **More developed:** Research question is clearly stated. Hypotheses and analysis clearly address the research question. Limitations are carefully considered and articulated.

Time management is graded on use of the slot, not just on staying inside it: "Team maximally uses their five minutes. Clearly communicates their objectives and outcomes from the project." Peer feedback runs through a Google Form, and "Students will evaluate their own presentations."

## Also verified, not used

Two more were fetched and read but left out to keep the set at five:

- Duke COMPSCI 526, "Team Project Presentation" (Fall 2024), <https://sites.duke.edu/compsci_526_01_f24/team-project-presentation/>. Eight-minute slots, slides due as a PDF on Gradescope the night before, "All team members must participate in the presentation, with each person focusing on their specific contributions," and the reminder that the period after presenting is for writing, not new analysis.
- UC Berkeley Data 100 (Spring 2020), "Final Project Rubric," <https://ds100.org/sp20/resources/assets/final_proj/New_Grad_DS_100_Final_Project_Rubric.pdf>. A whole-project rubric with a small Presentation row (7.5%) on an Exemplary/Acceptable/Inadequate scale, including the line "Presentation is unprepared, and no visual aid is provided" under Inadequate.
