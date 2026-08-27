# U.S. Presidential Elections, 1824–2024

One row per candidate per presidential election, from the first election with a
recorded popular vote (1824) through 2024.

### Files

- `elections.csv` — columns `Year`, `Candidate`, `Party`, `Popular vote`, `Result`, `%`.
  `Result` is `win` or `loss` (the winner of the *election*, not of the popular
  vote — 1824, 1876, 1888, 2000, and 2016 differ). `%` is the candidate's share
  of the popular vote, carried to full floating-point precision.

### Source

The `elections.csv` shipped with the UC Berkeley Data 100 course notes:
<https://github.com/DS-100/course-notes/blob/main/content/pandas_1/data/elections.csv>.
Data 100 compiled it from Wikipedia's per-election popular-vote tables.

Used in the Week 2 slides to introduce Polars, mirroring the dataframe
examples in the Data 100 `pandas` lecture.
