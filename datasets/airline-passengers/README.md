# Airline Passengers (1949–1960)

Monthly totals of international airline passengers from January 1949 through December 1960, as published by Box and Jenkins (1976). A classic time series benchmark dataset.

## Study

George Box and Gwilym Jenkins introduced this dataset in *Time Series Analysis: Forecasting and Control* (1976) as an example for seasonal ARIMA modeling. The data were originally collected by the airline industry and represent total monthly international passenger counts (in thousands) for a major U.S. airline. The series has become one of the most widely used benchmarks in time series analysis, illustrating strong multiplicative seasonality and an upward trend.

## Files

- `airline-passengers.csv` — 144 monthly observations from January 1949 to December 1960

## Columns

- `Month` — first day of the month in ISO 8601 format (YYYY-MM-DD)
- `Passengers` — total international airline passengers that month, in thousands

## Data format

- 144 rows (12 years × 12 months), no missing values
- Passenger counts are in thousands (e.g., 112 means 112,000 passengers)
- The series exhibits multiplicative seasonality: seasonal swings grow in proportion to the trend level

## Sources

- Box, G.E.P., Jenkins, G.M. (1976). *Time Series Analysis: Forecasting and Control.* Holden-Day. ISBN 978-0-8162-1104-3. ([Internet Archive scan](https://archive.org/details/timeseriesanalys0000boxg)) ([5th edition via Wiley](https://www.wiley.com/en-us/Time+Series+Analysis:+Forecasting+and+Control,+5th+Edition-p-9781118675021))
- Dataset in R's base `datasets` package: [`AirPassengers`](https://rdrr.io/r/datasets/AirPassengers.html) — official R documentation with column definitions and citation
- Rdatasets mirror (CSV download): https://vincentarelbundock.github.io/Rdatasets/doc/datasets/AirPassengers.html

## Disclaimers

- For educational purposes only.
- Accuracy, completeness, etc. not guaranteed.
- File was downloaded in June 2026 and may be outdated or inconsistent with current upstream records.
- Should not be treated as a complete or official record.
