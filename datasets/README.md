# Datasets for CS 418

Many of these are from the [Chicago Data Portal](https://data.cityofchicago.org/). All are pre-processed and intended only for educational purposes.

### Datasets

- [chicago-air-quality](chicago-air-quality/) — every PM2.5 and NO2 measurement from the 283-sensor Open Air Chicago network during July 2026
- [chicago-l-stations](chicago-l-stations/) — CTA L stop records with station names, service flags, and location data
- [chicago-maps](chicago-maps/) — Chicago city and ward boundaries, water polygons, and ward-level ACS household income, as plain GeoJSON and CSV
- [chicago-movies-in-parks](chicago-movies-in-parks/) — City of Chicago "Movies in the Parks" event listings
- [chicago-street-names](chicago-street-names/) — Chicago street names with suffix and address range fields
- [chicago-tall-buildings](chicago-tall-buildings/) — Buildings with 10 or more stories in Chicago
- [cook-county-home-sales-2025](cook-county-home-sales-2025/) — Residential property sales recorded in Cook County during 2025, de-identified
- [cta-ridership](cta-ridership/) — CTA annual ridership totals
- [datasaurus-dozen](datasaurus-dozen/) — thirteen two-variable datasets with near-identical summary statistics and wildly different shapes (Matejka & Fitzmaurice, CHI 2017)
- [fake-news-twitter-2016-election](fake-news-twitter-2016-election/) — Replication archive for Vosoughi et al., *Science* 2019 study on fake news spread on Twitter
- [galton-vox-populi-1907](galton-vox-populi-1907/) — Quantile summary of 787 weight estimates from Galton's 1907 "wisdom of crowds" experiment
- [icd-10-cm](icd-10-cm/) — FY2026 ICD-10-CM code descriptions from the CDC
- [illinois-prairie-path](illinois-prairie-path/) — Trail segment and mile post data for the Illinois Prairie Path and DuPage County bikeway network
- [joke-retrieval](joke-retrieval/) — JokesCorpus archives from Mihalcea & Strapparava, CIKM 2008
- [metra-lines-stations](metra-lines-stations/) — Metra line and station attributes
- [movies-from-imdb](movies-from-imdb/) — Movie datasets drawn from IMDb public data files
- [musiclab-salganik-2006](musiclab-salganik-2006/) — Replication data for Salganik, Dodds & Watts, *Science* 2006 study on social influence and cultural markets
  - Raw data not included; download from the [Princeton Research Data Commons](https://datacommons.princeton.edu/discovery/catalog/doi-10-34770-y56c-ym90)
- [national-parks-info](national-parks-info/) — The 63 U.S. national parks
- [resume-audit-bertrand-mullainathan](resume-audit-bertrand-mullainathan/) — Replication data for Bertrand & Mullainathan, *AER* 2004 field experiment on racial discrimination in hiring
- [us-presidential-elections](us-presidential-elections/) — Popular vote totals and shares for every U.S. presidential candidate, 1824–2024, from the Berkeley Data 100 course notes
- [world-inequality-database](world-inequality-database/) — Pre-tax national income share time series for 9 countries, from the World Inequality Database

### Guidelines

* prefer file sizes `< 50 MB` (for GitHub and general portability); document any exception in the dataset README
* use CSV or other plain-text formats
* include a short README in each dataset folder
* note the source(s) for each file
