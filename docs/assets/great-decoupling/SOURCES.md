# Sources — `great-decoupling`

> _Note: this file was drafted with an LLM. Images are third-party copyrighted
> material, collected here for classroom discussion (fair use); do not
> redistribute._

"The Great Decoupling" is Erik Brynjolfsson and Andrew McAfee's argument that U.S. labour productivity and real GDP per capita kept climbing after the early 1980s while median family income and private employment fell away

---

## Images

### 1. When Workers Began Falling Behind

**File:** `when-workers-began-falling-behind-1398px.png` (PNG, 1398 × 1036)
**Chart credit:** © HBR.org, June 2015
**Data source (as printed):** Federal Reserve Bank of St. Louis; Erik Brynjolfsson and Andrew McAfee

Labour productivity, real GDP per capita, private employment and median family income for the U.S., indexed to 1947 = 100, roughly 1947–2012.

---

### 2. As Profits Climb, Wages Plummet

**File:** `as-profits-climb-wages-plummet-1400px.png` (PNG, 1400 × 1070)
**Chart credit:** © HBR.org, June 2015
**Data source (as printed):** Federal Reserve Bank of St. Louis; Erik Brynjolfsson and Andrew McAfee

The article's second chart

---

## Links

- Article — Erik Brynjolfsson & Andrew McAfee, "The Great Decoupling," *Harvard
  Business Review*, June 2015: <https://hbr.org/2015/06/the-great-decoupling>
- Fred Wilson, "The Great Decoupling," *AVC*, 25 May 2015:
  <https://avc.com/2015/05/the-great-decoupling/>
- Direct image, chart 1 (full resolution), hosted by AVC:
  <https://avc.com/content/uploads/2015/05/decoupling.png>
- Archived copies of the HBR article (archive.today), which still carry the
  full-size chart assets: <https://archive.ph/zFnxf> (30 May 2015) ·
  <https://archive.ph/yRUQa> (24 May 2015) · <https://archive.ph/zkylw> (2023)

---

## Recreation (for the Week 6 slides)

_Drafted with an LLM; data pulled 2026-09-26._

`make_great_decoupling.py` rebuilds chart 1 from the underlying public series and writes `great-decoupling-blank.svg` (axes only) and `great-decoupling-complete.svg` (with the four lines). Each series is a calendar-year mean, indexed to 1947 = 100, for 1947–2012. Current data vintages end close to the printed chart (2012 values: productivity 423, real GDP per capita 366, private employment 293, median family income 235), but not identical.

| Series | File in `data/` | Source |
| --- | --- | --- |
| Labor productivity | `fred-OPHNFB.csv` | BLS, Nonfarm Business Sector: Real Output Per Hour of All Persons, via FRED [OPHNFB](https://fred.stlouisfed.org/series/OPHNFB) (quarterly) |
| Real GDP per capita | `fred-A939RX0Q048SBEA.csv` | BEA, Real gross domestic product per capita, via FRED [A939RX0Q048SBEA](https://fred.stlouisfed.org/series/A939RX0Q048SBEA) (quarterly) |
| Private employment | `fred-USPRIV.csv` | BLS, All Employees, Total Private, via FRED [USPRIV](https://fred.stlouisfed.org/series/USPRIV) (monthly) |
| Median family income | `census-f7-median-family-income.csv` | U.S. Census Bureau, CPS ASEC [Historical Income Table F-7](https://www2.census.gov/programs-surveys/cps/tables/time-series/historical-income-families/f07ar.xlsx), "All Families," median income in 2025 dollars. FRED's version (MEFAINUSA672N) starts in 1953, so the Census table is used to reach 1947. Where Census lists a year twice (survey redesigns, e.g. 2013, 2017) the first-listed row is kept. |
