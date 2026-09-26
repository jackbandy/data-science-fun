# Sources — `newspaper-ad-revenue`

> _Note: this file was drafted with an LLM. Data pulled 2026-09-26._

`make_newspaper_ad_revenue.py` plots U.S. newspaper advertising revenue against Google's and Meta's advertising revenue, 1956–2022, in billions of 2022 dollars. It writes `newspaper-ad-revenue-blank.svg` (axes only), `newspaper-ad-revenue-newspapers.svg` (newspaper line only), and `newspaper-ad-revenue-complete.svg` (all three lines). All charts and data here are original to this repo; only public figures are reused.

**Caveat worth saying out loud in class:** the newspaper line is U.S.-only; the Google and Meta lines are worldwide. Roughly half of each platform's revenue is from the U.S. (Alphabet 10-K FY2022: U.S. = 48% of total revenue).

## Data

### `data/pew-newspaper-ad-revenue.csv`

Pew Research Center, [Newspapers Fact Sheet](https://www.pewresearch.org/journalism/fact-sheet/newspapers/), chart "Estimated advertising and circulation revenue of the newspaper industry," advertising column. Pew's source line, verbatim: "News Media Alliance, formerly Newspaper Association of America (through 2012); Pew Research Center analysis of year-end SEC filings of publicly traded newspaper companies (2013-2022)." Rows from 2013 on are Pew's estimates (`estimated = true`) and are drawn dashed. Values are nominal U.S. dollars. Pew calls this "total estimated advertising revenue for the newspaper industry"; a companion chart on the same page gives the digital share (48% in 2022).

### `data/sec-tech-ad-revenue.csv`

Advertising revenue as printed in each company's SEC filings, in millions of nominal U.S. dollars; the `sec_filing` column names the filing and accession number for every row. Filings were read on [EDGAR](https://www.sec.gov/edgar/search/); rows marked `(XBRL)` come from the `us-gaap:AdvertisingRevenue` fact in EDGAR's [company-facts API](https://www.sec.gov/search-filings/edgar-application-programming-interfaces).

- **Google / Alphabet**: "Total advertising revenues" (Google web sites + Google Network web sites) through 2014; "Google advertising" (Search & other + YouTube ads + Network) from 2015, after the Alphabet reorganization. The first year of ads is 2001 (S-1, 2004).
- **Meta / Facebook**: "Advertising revenue," 2009–2022. 2009–2011 from the 2012 S-1.

### `data/fred-CPIAUCSL.csv`

BLS Consumer Price Index for All Urban Consumers (CPI-U), via FRED [CPIAUCSL](https://fred.stlouisfed.org/series/CPIAUCSL). The script takes the calendar-year mean and rescales every series to 2022 dollars.

