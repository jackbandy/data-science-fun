---
layout: schedule
title: Full Schedule
nav: schedule
description: Day-by-day schedule for Introduction to Data Science (CS 418), Fall 2026 with slides, worksheets, and source materials.
subtitle: Each week links to its slides; each meeting day links to its in-class worksheet and source materials.
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

**Schedule is a draft / work-in-progress.**

## Schedule Overview

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
      <td>{{ row["Class Day"] | escape }}</td>
      <td>{{ row["Topic"] | escape }}</td>
      <td>{{ row["Before Class"] | escape }}</td>
      <td>{{ row["In Class"] | escape }}</td>
    </tr>
    {%- endfor -%}
  {%- endfor %}
  </tbody>
</table>
</div>
<div id="schedule-tooltip" aria-hidden="true"></div>
<script src="{{ '/js/schedule-tooltip.js' | relative_url }}"></script>

## Full Schedule
