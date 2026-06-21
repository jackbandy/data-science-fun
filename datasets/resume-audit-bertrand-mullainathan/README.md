# Resume Audit: Race and Callbacks in the Labor Market

Replication data for "Are Emily and Greg More Employable Than Lakisha and Jamal? A Field Experiment on Labor Market Discrimination," *American Economic Review* 2004. For educational purposes only.

## Study

Bertrand and Mullainathan sent 4,870 fictitious resumes to real help-wanted ads in Boston and Chicago newspapers. Each resume was randomly assigned either a distinctively white-sounding name (e.g., Emily, Greg) or a distinctively Black-sounding name (e.g., Lakisha, Jamal). Everything else was held constant or varied systematically (e.g. experience). White names received 50% more callbacks for interviews, persistent across industries, job types, and cities.

## Files

- `resume.csv` — one row per resume sent; 4,870 observations, 30 variables

## Columns

- `job_ad_id` — identifier for the job ad the resume was sent to
- `job_city` — Chicago or Boston
- `job_industry` — industry of the job posting
- `job_type` — type of role (manager, supervisor, secretary, etc.)
- `job_equal_opp_employer` — whether the employer listed an equal opportunity statement
- `received_callback` — **outcome variable** — 1 if the resume received a callback, 0 otherwise
- `firstname` — first name assigned to the resume
- `race` — inferred race signal of the name (`white` or `black`)
- `gender` — inferred gender signal of the name (`f` or `m`)
- `resume_quality` — whether the resume was constructed as high or low quality
- `years_experience` — years of work experience listed
- `college_degree` — whether the resume listed a college degree
- `honors` — whether the resume listed academic honors
- `computer_skills` — whether computer skills were listed
- `special_skills` — whether special skills were listed
- `volunteer` — whether volunteer experience was listed
- `military` — whether military experience was listed
- `employment_holes` — whether the resume showed gaps in employment

## Sources

- Original paper: https://doi.org/10.1257/0002828042002561
- ICPSR replication archive: https://doi.org/10.3886/E116023V1
- CSV downloaded from OpenIntro: https://www.openintro.org/data/index.php?data=resume

## Disclaimers

- For educational purposes only.
- Accuracy, completeness, etc. not guaranteed.
- File was downloaded in June 2026 and may be outdated or inconsistent with current upstream records.
- Should not be treated as a complete or official record.
- Best to avoid reusing or redistributing; if you do, review upstream terms and licensing.
