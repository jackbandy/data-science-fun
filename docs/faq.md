---
layout: default
title: FAQ
nav: faq
show_last_updated: true
---

# FAQ

These include questions that I "frequently ask" myself while making these materials, as well as questions from colleagues, students, friends, etc.


---


## Programming Languages

**Q: Which programming language will this class be using?**

A: Good question. I'm planning a Python-forward course, mostly leaning on [Polars](https://pola.rs). Python still seems to be more widely-used for data science than R, and Polars is much more efficient than Pandas. Still, the course will provide experience/exposure for R, Pandas, and some other common tooling. I happen to think that if you really understand data science, the programming language probably does not matter too much (especially if an LLM is writing your code, but that's another question).


---


## Paper

**Q: Why make exercises/notes/etc. handwritten? Shouldn't data science be on a computer?**

A: One of the most common pitfalls in learning might be referred to as the "illusion of intuition." This is common when reading a book and trying to highlight the important parts, or clicking through a slide deck and nodding along, or reviewing notes that seem to make sense.

But then, you are asked to complete an exercise on a quiz or a test. It all made sense when you were "studying," but now that you must do it yourself, that intuition is not helping.

Handwritten exercises force the learner to really do the thing. Instead of just nodding along to external materials, the learner creates the material themself, proving to themselves that they can do this.

---

## Google Slides

**Q: Why not just use Google Slides?**

A: The short answer is that I think Google sucks. This is not to say anything about the people at Google - they have made some amazing technology over the years! But they have pulled the rug out from under us a few too many times. Gmail, Google Photos, and Google Drive have all seen substantial decay, and unfortunately I cannot trust that Google Slides will be protected. It might be a few years down the road, but I expect the company will move forward with limited storage, proprietary formatting, restricted portability, etc.

So, for now I am using a markdown-to-html pipeline via [Quarto](https://quarto.org/), which is open source and free (as in freedom). I plan to keep content mostly in markdown text and svg images, so the slides should be easy to recreate or port over if the need ever arises. If you have other ideas or suggestions on this front, please let me know.

The slide theme uses Big Shoulders for title headings and an ITC Franklin Gothic stack for body and footer text. ITC Franklin Gothic is commercial, so the repository also includes Libre Franklin from the upstream `impallari/Libre-Franklin` project as a permissively licensed fallback.

---

## New Materials

**Q: Why make new materials when there is already so much out there?**

A: Various reasons, including: (1) making materials can be fun, (2) I think students probably learn better when materials are "handmade" by their instructors in some way, rather than generic mass-distributed textbooks, and (3) some of the materials I really want/need to be able to teach data science effectively do not seem to exist yet.

---

## Defining Data Science

**Q: What is data science, exactly?**

A: This is a simple question without a simple answer. At least, I do not yet have a simple answer, but I do appreciate that data science seems to be a "big tent" for many different genres of scholarship. Another version of this question might be, "what is _not_ data science?"

For some reference points, check out the "ethics in data science" mini-book, which has a section on ["Defining Data Science"](ethics-in-data-science/book/07-glossary.html#sec-defining-data-science).

---

## Jobs

**Q: Will data science be obsolete soon? Will anyone hire human data scientist? Won't AI take all the data science jobs?**

A: Wow, three questions! From my point of view: **no**, data science will not be obsolete soon, **yes**, organizations will still hire human data scientists, and **no**, AI will not take over all the data science jobs. Some AI tools seem very useful for writing code, which can be helpful in the data science workflow. But LLMs on their own cannot make data useful and meaningful for humans -- much less for organizations. There are deeper discussions to be had here, more than I can fit into an FAQ page, but here are some high-level points.

Any data "insights" shared by an AI will not have the same level of explainability as insights from a human. Humans can reason together about their intuitions, expectations, and surprises, discussing questions and building mutual understanding in real-time dialogue. LLMs, on the other hand, output things like "you're absolutely right, thanks for catching my mistake," before flip-flopping on a major point with no further explanation. This is because LLMs have been trained for the purpose of generating plausible next words that essentially just make people feel good. The resulting system is not a great match for data science, where real insights and rigorous findings can be uncomfortable.

Also, in most cases, any "data science" outsourced to an AI/LLM system will be under the purview of a large technology company, which owns and operates the system that analyzed the data and generated "insights." The extent to which this alters the workflow may change, but it certainly opens the door for big tech to put their thumbs on the scale.
 
I think if organizations truly want evidence-based, data-informed decisions, they will need human data scientists who can make sense of data *with other humans.* By themselves, code and statistics have limited usefulness. Only with other humans can we construct real knowledge from data -- knowledge which is socially meaningful, relevant, and useful. I have more to say on this, but I am not sure if this soapbox can hold me much longer...

---

## Instructor AI Use

**Q: Did the instructor(s) use AI to make these materials?**

A: My philosophy on AI usage is [here](https://jackbandy.com/text/llm-code-philosophy.html).

Although I have many concerns about large technology companies, their owners, and the future(s) they are trying to create, I do not consider myself "anti-AI." I also don't consider myself "pro-autotune" or "anti-autotune," and I don't consider myself "pro-autofocus" or "anti-autofocus." In high school I drove a manual transmission car, and even then I did not identify as "pro-auto-transmission" or "anti-auto-transmission."

This is because I find some automation quite useful, which is perhaps unsurprising given my training in computer science. And while I do not find LLMs at all useful for generating material out of thin air, when I have something in mind to convert or translate or build out, I have found LLMs helpful. And yes, I have used various LLM-based tools to draft and modify some of the materials in this repo.

To give an idea of what this look like in practice, here are some examples of the kinds of prompts I sometimes give to LLM coding tools:
* "draft a quarto markdown slide based on slide X from my other class"
* "add three placeholder slides about linear regression after slide X"
* "write code to recreate this figure in ggplot, plotting, and matplotlib" 
* "extract Figure 2 from this pdf and save it in the assets folder"
* "draft a slide template based on week X, slide Y, and save it in week0"
* "draft the alt-text for the figure in slide X"

Importantly, I take responsibility for everything in the repo, and I make a sincere effort to ensure that I can explain, modify, and/or fix things myself. I also deliberately avoid using LLMs for "writing" material (such as this FAQ answer).

My ideas/opinions on this topic continue to evolve - I would love to hear your thoughts!

---

## Student AI Use

**Q: Will students be allowed to use AI in this class?**

A: As of right now (August 1, 2026), I am planning three phases of the class: (1) a no-AI phase, (2) a "guided AI usage" phase, and (3) a "choose your own AI adventure" phase. I have also seen these phases called red light, yellow light, green light, but that could ruin the rail metaphors...

Basically, in my view and the view of many other educators, there are some concepts that should be fully learned and absorbed. As with many other tools, one needs a foundational understanding of some domain in order to have the [discernment necessary for effectively using AI](https://pluralistic.net/2026/07/28/hitl-ers/). Hence the "red light" phase - a few weeks with no AI usage (although I have no means or intent to police this).

Then, the yellow light phase. Go ahead and try it out for a few carefully-scoped tasks. Take the marshmallow test and see how you do. See how the tool fails, and decide if/when you find it useful, and pay close attention!

Finally, it's the green light phase: do whatever you want, and be prepared to justify it. This phase is important because it seems to be the default setup in the real-world. It thus seems important to have some experience with the free-for-all in a communal learning environment - let's talk about it and think about it together before you go out into the real world.

As with the "instructor AI use" section, my ideas/opinions on this topic continue to evolve, and I am especially curious about any evidence-based viewpoints on this one.



---

## CTA Theme

**Q: Why the Chicago Transit Authority (CTA) theme?**

A: I'm a nerd and I like public transit and I am teaching in Chicago. The Computer Science building (the [CDRLC](https://lmnarchitects.com/project/computer-design-research-and-learning-center-university-of-illinois-chicago)) at UIC uses orange exterior highlights. The CTA Orange line currently has fifteen open stations (State/Lake is closed), and the UIC semester is fifteen weeks long (plus finals week), so the organization works out well.

The [CTA Trademark Guidelines](https://www.transitchicago.com/developers/branding/) encourage using proper CTA 'L' route colors, incorporating CTA styles from the official style guide, and mentioning that the project is inspired by Chicago's transit system (hence this blurb). This site uses the official CTA Orange Line color (#f9461c) and Sign Grey (#565a5c) from the [CTA Branding Guidelines for Developers](https://www.transitchicago.com/developers/branding/#branding).

I do not claim that this project is official, authorized, or endorsed by CTA, and I do not intend to use logos, names, or marks in a way that suggests an official CTA affiliation. It might not always be the case, but for now, this site is an educational project and not a CTA product or service.
