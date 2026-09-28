#!/usr/bin/env python3
"""Fit the Week 6 UIC-Halsted ridership model once and save its posterior, so the slides load it instead of sampling on every render.

The data prep and model match the "A Bayesian Ridership Model" slide in docs/slides/week6.qmd; keep the two in sync.
Run from docs/slides with its venv: PYTENSOR_FLAGS=mode=NUMBA .venv/bin/python ../../datasets/cta-ridership/fit_uic_halsted_posterior.py
(NUMBA mode avoids PyTensor's C compiler, which fails to link on recent Xcode.)
"""

from pathlib import Path

import polars as pl
import pymc as pm

HERE = Path(__file__).resolve().parent
OUT = HERE / "uic_halsted_posterior.nc"

cta = pl.read_csv(HERE / "Station_Entries_-_Daily_Totals_20260527.csv")
uic = (
    cta.filter(pl.col("stationname") == "UIC-Halsted")
    .with_columns(
        pl.col("date").str.to_date("%m/%d/%Y"),
        pl.col("rides").str.replace_all(",", "").cast(pl.Int64),
    ).sort("date").filter(pl.col("date") >= pl.date(2016, 1, 1))
)

recent = uic.filter(pl.col("date") >= pl.date(2023, 1, 1)).with_columns(
    (pl.col("date").dt.weekday() - 1).alias("dow"),   # 0=Mon … 6=Sun
    (pl.col("date").dt.month() - 1).alias("month"),    # 0=Jan … 11=Dec
)
dow   = recent["dow"].to_numpy()
month = recent["month"].to_numpy()
y     = recent["rides"].to_numpy().astype(float)

with pm.Model() as model:
    intercept = pm.Normal("intercept", mu=y.mean(), sigma=2000)
    dow_eff   = pm.ZeroSumNormal("dow_eff", sigma=1500, shape=7)
    month_eff = pm.ZeroSumNormal("month_eff", sigma=1500, shape=12)
    sigma     = pm.HalfNormal("sigma", 2000)
    mu = intercept + dow_eff[dow] + month_eff[month]
    pm.Normal("obs", mu=mu, sigma=sigma, observed=y)
    idata = pm.sample(500, tune=500, chains=2, cores=1,
                      random_seed=0, progressbar=False)

# Only the posterior is used downstream; dropping the rest keeps the file small.
# The scipy engine (netCDF3) needs no extra packages beyond what PyMC already installs.
idata.posterior.to_netcdf(OUT, engine="scipy")
print(f"wrote {OUT} ({OUT.stat().st_size / 1024:.0f} KB)")
