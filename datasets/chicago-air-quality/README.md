# Chicago Air Quality

Measurements taken by the Open Air Chicago sensor network during July 2026, prepared from the City of Chicago's public data portal. For educational purposes.

Open Air Chicago is a citywide network of low-cost air sensors installed in summer 2025 by the Chicago Department of Public Health and the UIC School of Public Health. Each sensor reports fine particulate matter (PM2.5) and nitrogen dioxide (NO2) roughly every six minutes. **These are non-regulatory sensors and the data are not suitable for regulatory or compliance purposes.**

## Quickstart

```python
import polars as pl

df = (
    pl.read_csv("chicago-air-quality-2026-07.csv.gz")           # 2.1M measurements
    .join(pl.read_csv("chicago-air-quality-sensors.csv"), on="sensor_id")
    .with_columns(                                              # UTC -> Chicago time
        pl.col("time_utc")
        .str.to_datetime()
        .dt.replace_time_zone("UTC")
        .dt.convert_time_zone("America/Chicago")
        .alias("time_chicago")
    )
)

df.group_by("community_area").agg(pl.col("pm2_5").median()).sort("pm2_5", descending=True)
```


The time zone conversion is important (see [Things to know](#things-to-know))

## Files

- `chicago-air-quality-2026-07.csv.gz`: 2,107,068 measurements, one row per sensor reading, 2026-07-01 through 2026-07-31 (UTC). 9 columns, 44 MB compressed / 152 MB uncompressed — **see [Size](#size)**.

  - `sensor_id`: sensor identifier, e.g. `DUXLQ7589`. Joins to `chicago-air-quality-sensors.csv`
  - `time_utc`: timestamp of the reading (`YYYY-MM-DDTHH:MM:SS`), **in UTC, not Chicago time** — see [Things to know](#things-to-know)
  - `pm2_5`: PM2.5 mass concentration (µg/m³), calibrated
  - `pm2_5_raw`: the same reading straight off the sensor, before calibration
  - `no2`: NO2 concentration (ppb), calibrated
  - `no2_raw`: the same reading before calibration
  - `pm2_5_number`: PM2.5 *number* concentration (particles/cm³), calibrated — a count of particles rather than their mass
  - `temperature_c`: internal sensor temperature (°C)
  - `relative_humidity`: internal relative humidity (%)

  `pm2_5`, `pm2_5_raw` and `pm2_5_number` are empty together on 19,547 rows (0.9%); `no2` and `no2_raw` on 161 rows.

- `chicago-air-quality-sensors.csv`: 283 sensors, one row each. The fields that never change during the month, pulled out of the measurements file so they are not repeated two million times.

  - `sensor_id`: joins to the measurements file
  - `sensor_name`: community area plus that sensor's number within it, e.g. `Albany Park 3`
  - `community_area`: `sensor_name` with the trailing number stripped — all 77 Chicago community areas appear, plus 3 collocation sites (see below)
  - `latitude`, `longitude`: sensor location (WGS84), rounded to 5 decimals (about 1 m)
  - `measurements`: number of rows this sensor contributes to the July file

- `update_chicago_air_quality.py`: rebuilds both files from the city's open data API. Set `MONTH` at the top to build a different month.

## Notes

**Timestamps are UTC, and Chicago is 5 hours behind in July.** This is the single easiest way to get a wrong answer from this file. Grouping `time_utc` by hour and calling the result "time of day in Chicago" shifts every diurnal pattern by five hours, and grouping by date puts the evening of July 4 into July 5.

E.g. for Independence Day fireworks, network-wide median PM2.5 by UTC hour:

| UTC hour | Chicago time | Median PM2.5 |
|---|---|--:|
| Jul 4 23:00 | Jul 4, 6 pm | 11.5 |
| Jul 5 01:00 | Jul 4, 8 pm | 19.0 |
| **Jul 5 02:00** | **Jul 4, 9 pm** | **60.4** |
| Jul 5 03:00 | Jul 4, 10 pm | 50.6 |
| Jul 5 06:00 | Jul 5, 1 am | 19.9 |
| Jul 5 12:00 | Jul 5, 7 am | 9.3 |


**July 2026 was not a typical month.** e.g. see July 16 and 17

**Raw and calibrated columns.** The `.value` columns (`pm2_5`, `no2`) have Clarity's global correction model applied; the `_raw` columns are the sensor's own output

**Sensors are unevenly distributed.** 283 sensors cover 77 community areas, ranging from 1 sensor to 9.

**Three "community areas" are not community areas.** `Mayfair Collocation`, `Schiller Park Collocation` and `Washington HS Collocation` are sets of three sensors each, installed at federal regulatory monitoring sites so the city can compare its sensors against reference instruments. Their nine sensors sit at three physical locations (Schiller Park is not even in Chicago).
	* good for analyzing how much two identical sensors in the same spot disagree
	* should be dropped before mapping anything by neighborhood

**Temperature and humidity are internal** They describe conditions inside the sensor housing

**Black carbon is missing.** The source dataset has sixteen black carbon columns but they are empty (the modules were offline at launch?)

**The upstream file lags by about a week.** Days near the end of the source dataset are still filling in: the first time this was built, July 27 onward showed only 165 of 283 sensors reporting, while every earlier day showed 282–283.

**Only quality-controlled data is here.** The city publishes this dataset already filtered to measurements that passed Clarity's automated QC checks. Readings that failed are not in the source, (so this is not a complete record of what the sensors reported)


## Sources

- **Open Air Chicago - Individual Measurements**, Chicago Data Portal: https://data.cityofchicago.org/Health-Human-Services/Open-Air-Chicago-Individual-Measurements/xfya-dxtq/about_data

The portal also publishes hourly and daily aggregations of the same network, which are much smaller and are a better starting point if you do not need individual readings.

Background on the calibration models applied to the `.value` columns:

- PM2.5: https://www.clarity.io/blog/v2-1-pm2-5-global-calibration
- NO2: https://www.clarity.io/blog/introducing-claritys-global-no2-calibration-model
- Quality control: https://click.clarity.io/knowledge/quality-control

## Reproduction

```bash
python3 update_chicago_air_quality.py
```

Requires Python 3.9+ and `requests`. A month takes roughly 15 minutes to download, since the API is paged 50,000 rows at a time, and the script holds the month in memory before sorting it.

Re-running rebuilds both files from live city data, so the output may differ from the committed files wherever records have been added or corrected since August 2026.

## Disclaimers

- For educational purposes only.
- Accuracy, completeness, etc. not guaranteed.
- These are low-cost, non-regulatory sensors. The data are not suitable for regulatory, compliance, health-advisory, or legal purposes, and individual readings should not be used to characterize anyone's personal exposure.
- The CSVs are derived files, filtered and reshaped from the source above, and are not an official city product.
- Files were created in August 2026 and may be incomplete, outdated, transformed, filtered, or inconsistent with current official records by the time you use it.
- Usually best to avoid reusing or redistributing, but if you do, please review upstream terms, licensing, and source documentation.
