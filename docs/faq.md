---
layout: default
title: FAQ
permalink: /faq.html
---

# FAQ

These include questions that I "frequently ask" myself while making these materials, as well as questions from colleagues, students, friends, etc.


---


## Programming Languages

**Q: Which programming language will this class be using?**

A: Good question. I'm planning a Python-forward course, mostly leaning on [Polars](https://pola.rs). Python still seems to be more widely-used for data science than R, and Polars is much more efficient than Pandas. Still, the course will provide some experience with R, Pandas, and some other common tooling. I happen to think that if you really understand data science, the programming language probably does not matter too much (especially if an LLM is writing your code, but that's another question).


---


## Paper? Really?

**Q: Why make exercises handwritten? Shouldn't data science be on a computer?**

A: One of the most common pitfalls in learning might be referred to as the "illusion of intuition." This is common when reading a book and trying to highlight the important parts, or clicking through a slide deck and nodding along, or reviewing notes that seem to make sense.

But then, you are asked to complete an exercise on a quiz or a test. It all made sense when you were "studying," but now that you must do it yourself, that intuition is not helping.

Handwritten exercises force the learner to really do the thing. Instead of just nodding along to external materials, the learner creates the material themself, proving to themselves that they can do this.

---

## Google Slides

**Q: Why not just use Google Slides?**

A: The short answer is that I think Google sucks. This is not to say anything about the people at Google - they have made some amazing technology over the years! But they have pulled the rug out from under us a few too many times. Gmail, Google Photos, and Google Drive have all seen substantial decay, and unfortunately I cannot trust that Google Slides will be protected. It might be a few years down the road, but I expect the company will move forward with limited storage, proprietary formatting, restricted portability, etc.

So, for now I am using a markdown-to-html pipeline via [marp](https://github.com/marp-team/marp), which is open source and free (as in freedom). I plan to keep content mostly in markdown text and svg images, so the slides should be easy to recreate or port over if the need ever arises. If you have other ideas or suggestions on this front, please let me know.

---

## New Materials

**Q: Why make new materials when there is already so much out there?**

A: Various reasons, including: (1) making materials can be fun, (2) I think students probably learn better when materials are "handmade" by their instructors in some way, rather than generic mass-distributed textbooks, and (3) some of the materials I really want/need to be able to teach data science effectively do not seem to exist yet.

---

## Defining Data Science

**Q: What is data science, exactly?**

A: This is a simple question without a simple answer. At least, I do not yet have a simple answer, but I do appreciate that data science seems to be a "big tent" for many different genres of scholarship. Another version of this question might be, "what is _not_ data science?"

---

## Jobs

**Q: Will data science be obsolete soon? Will anyone hire human data scientist? Won't AI take all the data science jobs?**

A: Wow, three questions! From my point of view: **no**, data science will not be obsolete soon, **yes**, organizations will still hire human data scientists, and **no**, AI will not take over all the data science jobs. Some AI tools seem very useful for writing code, which can be helpful in the data science workflow. But LLMs on their own cannot make data useful and meaningful for humans -- much less for organizations. There are deeper discussions to be had here, more than I can fit into an FAQ page, but here are some high-level points.

Any data "insights" shared by an AI will not have the same level of explainability as insights from a human. Humans can reason together about their intuitions, expectations, and surprises, discussing questions and building mutual understanding in real-time dialogue. LLMs, on the other hand, output things like "you're absolutely right, thanks for catching my mistake," before flip-flopping on a major point with no further explanation. This is because LLMs have been trained for the purpose of generating plausible next words that essentially just make people feel good. The resulting system is not a great match for data science, where real insights and rigorous findings can be uncomfortable.

 Also, in most cases, any "data science" outsourced to an AI/LLM system will be under the purview of a large technology company, which owns and operates the system that analyzed the data and generated "insights." The extent to which this alters the workflow may change, but it certainly opens the door for big tech to put their thumbs on the scale.
 
I think if an organizations truly wants evidence-based, data-informed decisions, they will need human data scientists who can make sense of data *with other humans.* By themselves, code and the statistics have limited usefulness. Only with other humans can we construct real knowledge from data -- knowledge which is socially meaningful and relevant and useful. I have more to say on this, but I am not sure if this soapbox can hold me much longer...

---

## CTA Theme

**Q: Why the Chicago Transit Authority (CTA) theme?**

A: I'm a nerd and I like public transit and I am teaching in Chicago. The CTA Orange line currently has sixteen open stations (State/Lake is closed), and the UIC semester is sixteen weeks long, so the organization works out well. The [CTA Trademark Guidelines](https://www.transitchicago.com/developers/branding/) encourages using proper CTA 'L' route colors, incoprorating CTA styles from the official style guide, mentioning the project is inspired by Chicago's transit system (hence this blurb), and using standard bus and train icons and color schemes from CTA signs. This site uses the official CTA Orange Line color (#f9461c) and Sign Grey (#565a5c) from the [CTA Branding Guidelines for Developers](https://www.transitchicago.com/developers/branding/#branding).

I do not claim that this project is official, authorized, or endorsed by CTA, and I do not intend to use logos, names, or marks in a way that suggests an official CTA affiliation. It might not always be the case, but for now, this site is an educational project and not a CTA product or service.

---

<p class="last-updated">Last updated: <a href="https://github.com/jackbandy/data-science-fun/commits/" id="last-updated-link">{{ site.time | date_to_xmlschema }}</a></p>
<script>
  (function () {
    const t = new Date("{{ site.time | date_to_xmlschema }}");
    const fmt = { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false };
    const chicago = t.toLocaleString('en-US', {
      timeZone: 'America/Chicago',
      year: 'numeric', month: 'long', day: 'numeric',
      ...fmt, timeZoneName: 'short'
    });
    const utc = t.toLocaleString('en-US', { timeZone: 'UTC', ...fmt, timeZoneName: 'short' });
    document.getElementById('last-updated-link').textContent = chicago + ' (' + utc + ')';
  })();
</script>
