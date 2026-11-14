---
layout: schedule
title: Intro to Data Science (CS 418)
heading: Schedule Overview
nav: schedule
description: Day-by-day schedule for Introduction to Data Science (CS 418), Fall 2026 with slides, worksheets, and source materials.
alert: Stations open during construction
alert_detail: Hello! This is the first semester of running this site for the course. Please bear with me as I iron out the wrinkles.
extra_css:
  - /css/schedule.css
---

<!-- The schedule itself lives in two files, the source of truth for this page:
     _data/schedule.csv (weeks, class days, dates, notes) and
     _includes/schedule-topics.md (what happens each day, and its sources).
     Edit those; the layout (_layouts/schedule.html) renders them. Anything
     typed below this comment appears above the week links on the published
     page. -->

<div class="schedule-table-wrap">
{%- assign weeks = site.data.schedule | group_by: "Week" %}
<table class="schedule-table">
  <thead>
    <tr>
      <th scope="col">Week</th>
      <th scope="col">Class Day</th>
      <th scope="col">Topic</th>
      <th scope="col">Before Class</th>
      <th scope="col">In Class</th>
    </tr>
  </thead>
  <tbody>
  {%- for week in weeks -%}
    {%- assign station = site.data.stations[week.name] -%}
    {%- if station -%}
      {%- assign dot = "Week " | append: week.name | append: ", " | append: station -%}
    {%- else -%}
      {%- assign dot = "Week " | append: week.name -%}
    {%- endif -%}
    {%- for row in week.items %}
    <tr>
      {%- if forloop.first %}
      <th scope="row" rowspan="{{ week.items | size }}"><span class="schedule-week-dot" data-label="{{ dot | escape }}" aria-label="{{ dot | escape }}" tabindex="0">{{ week.name | escape }}</span></th>
      {%- endif %}
      <td>{{ row["Class Day"] | escape }}<span class="schedule-day-date">({{ row["Date"] | date: "%b %-d" | replace: "Sep ", "Sept " }})</span></td>
      <td>{{ row["Topic"] | escape }}</td>
      {%- comment -%} A Before Class cell can hold two due items ("Homework 8 Due; project checkpoint: EDA"), so each one gets its own line. {%- endcomment %}
      <td>{{ row["Before Class"] | escape | replace: "; ", "<br>" }}</td>
      <td>{{ row["In Class"] | escape }}</td>
    </tr>
    {%- endfor -%}
  {%- endfor %}
  </tbody>
</table>
</div>
<div id="schedule-tooltip" aria-hidden="true"></div>
<script src="{{ '/js/schedule-tooltip.js' | relative_url }}"></script>

## Final Exam Details

**CS 418 – 44033** (3:30 PM, MW)

Our final exam will take place on **Monday, December 7th, 2026, at 9am**. We have Lecture Center C1 reserved from 8am-10am; however, the final will only be one hour, and students voted (in class on November 11) to take the exam from 9am-10am. Scheduling follows the registrar's [schedule of final exams](https://apps.registrar.uic.edu/current_students/calendars/final-exams.php) and [exam policies](https://registrar.uic.edu/current_students/calendars/final_exam_schedule.html).

You are allowed **one reference sheet** for the final exam. It can contain anything you wish, but it must fit on a single page of printer paper (8.5in x 11in), front and back.

The final exam will use questions from PrairieLearn. Approximately 80% of the questions will be variants of questions you have seen on homeworks and quizzes, while the remaining 20% will be applications of the same concepts.

Please email [jxb@uic.edu](mailto:jxb@uic.edu) with any questions or concerns.

## Full Schedule
