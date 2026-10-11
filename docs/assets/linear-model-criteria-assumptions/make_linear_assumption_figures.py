#!/usr/bin/env python3
"""Practice figures for checking the LINE assumptions of simple linear regression.

NOTICE: this file was substantially drafted by an LLM coding system and has not
yet been reviewed. Check every figure (and its positive/negative label) before
it goes on a slide or worksheet.

Four assumptions, after Çetinkaya-Rundel and Hardin, *Introduction to Modern
Statistics* §24.6 (the list on the Week 8 "Assumptions / Criteria" slide):
Linearity, Independence, Nearly normal residuals, Equal variability. Each gets
three positive examples (the assumption holds) and three negative examples (it
is violated), mixing real datasets from this repo with synthetic data.

Every figure is the same two panels on a 1000 x 618 golden-ratio canvas:
  left:  the data with its least-squares line
  right: the diagnostic plot for that assumption
           linearity     residuals vs. x
           independence  residuals in collection order
           normality     histogram of residuals, normal curve overlaid
           equal var.    residuals vs. fitted values
Each title reads "Linear modeling criteria: <IMS name> (<other name>)". The
subtitle quotes the condition directly from IMS (§24.6, plus §7.1.3 for
linearity); the dataset name and description sit below the plots as a caption.

Every example is written as three slide builds:
  <assumption>-<positive|negative>-example-<a|b|c>-v0.svg  the data alone
  ...-v1.svg  + least-squares line and the diagnostic panel
  ...-v2.svg  + a diagonal "Meets criteria" / "Does not meet criteria" stamp
v0 and v1 carry no verdict, so they work as "does this assumption hold?"
questions; v2 is the answer. The verdict comes from the filename.

Color: data are gray ink; the model is orange. That covers the fitted line, the
zero-residual line (the model's own predictions), and the normal curve (the
shape the model assumes), so orange always reads as "what the model claims."
The v2 verdict stamp is also theme orange, semi-transparent so the plots show
through it.

Usage:  python3 make_linear_assumption_figures.py [name ...]
"""

from __future__ import annotations

import sys
import io
import re
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import polars as pl
from matplotlib import font_manager
from matplotlib import patheffects
from matplotlib.ticker import FuncFormatter, MaxNLocator

OUT_DIR = Path(__file__).resolve().parent
REPO_ROOT = OUT_DIR.parents[2]
DATASETS = REPO_ROOT / "datasets"
OLYMPICS = OUT_DIR.parent / "olympics-100m" / "data"
FONT_PATH = OUT_DIR.parent / "fonts" / "libre-franklin" / "LibreFranklin-Regular.ttf"

# STYLE.md palette
INK = "#1A1A1A"
STEEL = "#565A5C"
MUTED = "#777777"
QUIET = "#AAAAAA"
BORDER = "#DDDDDD"
SOFT_GRAY = "#F4F4F2"
PAPER = "#FFFFFF"
ORANGE = "#F9461C"

PHI = (1 + 5**0.5) / 2
WIDTH_PX = 1000
HEIGHT_PX = round(WIDTH_PX / PHI)  # 618
DPI = 100

FIGURES: dict[str, callable] = {}


def figure(name: str):
    """Register a builder under the filename stem it writes."""
    def wrap(fn):
        FIGURES[name] = fn
        return fn
    return wrap


def tidy(ax, *, grid="y"):
    """Two hairline spines, one light grid, steel tick labels."""
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(BORDER)
    if grid:
        ax.grid(axis=grid, color=BORDER, linewidth=0.8, alpha=0.7)
    ax.set_axisbelow(True)
    ax.tick_params(colors=STEEL, labelsize=11, length=0)
    for lbl in (ax.xaxis.label, ax.yaxis.label):
        lbl.set_color(STEEL)
        lbl.set_fontsize(12)
    # Horizontal y-axis label across the top of the axis, so it reads without
    # tilting your head.
    ax.yaxis.label.set(rotation=0, ha="left", va="bottom")
    ax.yaxis.set_label_coords(0, 1.025)
    return ax


def dollars(v, _=None):
    sign = "−" if v < 0 else ""
    v = abs(v)
    if v == 0:
        return "$0"
    return f"{sign}${v / 1e6:g}M" if v >= 1e6 else f"{sign}${v / 1e3:,.0f}k"


def thousands(v, _=None):
    return f"{v / 1e3:g}k" if abs(v) >= 1e3 else f"{v:g}"


# --------------------------------------------------------------------------
# The shared two-panel layout
# --------------------------------------------------------------------------

# The condition each figure checks: IMS's own label, another common name for it,
# its sentence(s) verbatim, and the section(s) quoted.
#   IMS §24.6: https://openintro-ims.netlify.app/inf-model-slr.html
#   IMS §7.1.3: https://openintro-ims.netlify.app/model-slr.html
# Linearity pairs two separate quotes (not one passage), so each sits in its own
# quotation marks. The other names for linearity, independence, and normality
# follow Penn State STAT 462 §6.1 ("LINE": "Linear function", errors
# "Independent", "Normally distributed"); "homoscedasticity" is the name the
# Week 8 slide gives equal variability.
CONDITIONS = {
    "linearity": ("Linearity", "linear function",
                  "“The data should show a linear trend.” “One purpose of residual "
                  "plots is to identify characteristics or patterns still apparent "
                  "in the data after fitting a model.”", "§24.6 and §7.1.3"),
    "independence": ("Independent observations", "independent errors",
                     "“Be cautious about applying regression to data that are "
                     "sequential observations in time such as a stock price each day.”",
                     "§24.6"),
    "normality": ("Nearly normal residuals", "normally distributed errors",
                  "“Generally, the residuals should be nearly normal.”", "§24.6"),
    "equal-variability": ("Constant or equal variability", "homoscedasticity",
                          "“The variability of points around the least squares "
                          "line remains roughly constant.”", "§24.6"),
}
QUOTE_SOURCE = ("Quoted: Çetinkaya-Rundel and Hardin, Introduction to Modern "
                "Statistics, 2nd ed., {sections}.")

DIAGNOSTIC_TITLES = {
    "linearity": "Residuals vs. x",
    "independence": "Residuals in the order collected",
    "normality": "Histogram of residuals",
    "equal-variability": "Residuals vs. fitted values",
}


def panels(*, title, caption, x, y, xlabel, ylabel, check,
           order=None, order_label="Observation order", order_is_date=False,
           x_fmt=None, y_fmt=None, resid_fmt=None, resid_label="Residual",
           log_x=False, log_y=False, x_ticks=None, y_ticks=None):
    """Fit y ~ x by least squares and draw data + line | diagnostic.

    With log_x / log_y the line is fit on log10 scale and both panels are
    drawn on log axes, so the tick labels stay in the data's own units.
    """
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    fx = np.log10(x) if log_x else x
    fy = np.log10(y) if log_y else y
    slope, intercept = np.polyfit(fx, fy, 1)
    fitted = intercept + slope * fx
    resid = fy - fitted

    fig = plt.figure(figsize=(WIDTH_PX / DPI, HEIGHT_PX / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    label, other_name, quote, sections = CONDITIONS[check]
    fig.text(0.055, 0.955, f"Linear modeling criteria: {label} ({other_name})",
             fontsize=18, color=INK, va="top")
    # Room for two lines in every figure, so the panels line up across the set.
    fig.text(0.055, 0.895, textwrap.fill(quote, 100),
             fontsize=13, color=STEEL, va="top", linespacing=1.35)
    fig.text(0.055, 0.025,
             f"{title}. {caption}\n{QUOTE_SOURCE.format(sections=sections)}",
             fontsize=10.5, color=MUTED, va="bottom", linespacing=1.5)
    left = fig.add_axes((0.085, 0.2, 0.385, 0.50))
    right = fig.add_axes((0.585, 0.2, 0.385, 0.50))
    for ax in (left, right):
        ax.set_facecolor(PAPER)

    # Left: data and least-squares line
    small = len(x) < 80
    size, alpha = (44, 0.9) if small else (16, 0.45)
    left.scatter(x, y, s=size, color=INK, alpha=alpha, edgecolor=PAPER,
                 linewidth=0.6 if small else 0.3, zorder=3)
    grid = np.linspace(fx.min(), fx.max(), 200)
    line = intercept + slope * grid
    (fit_line,) = left.plot(10**grid if log_x else grid, 10**line if log_y else line,
                            color=ORANGE, linewidth=2.6, zorder=4)
    if log_x:
        left.set_xscale("log")
    if log_y:
        left.set_yscale("log")
    left.set_xlabel(xlabel)
    left.set_ylabel(ylabel)
    if x_fmt:
        left.xaxis.set_major_formatter(FuncFormatter(x_fmt))
        left.xaxis.set_minor_formatter(FuncFormatter(lambda *_: ""))
    if y_fmt:
        left.yaxis.set_major_formatter(FuncFormatter(y_fmt))
        left.yaxis.set_minor_formatter(FuncFormatter(lambda *_: ""))
    if x_ticks is not None:
        left.set_xticks(x_ticks)
    if y_ticks is not None:
        left.set_yticks(y_ticks)
    left_title = left.set_title("Data and least-squares line", fontsize=14,
                                color=INK, loc="left", pad=30)
    tidy(left)

    # Right: the diagnostic for this assumption
    right.set_title(DIAGNOSTIC_TITLES[check], fontsize=14, color=INK,
                    loc="left", pad=30)
    if check == "normality":
        sd = resid.std(ddof=1)
        bins = int(np.clip(np.sqrt(len(resid)) * 1.3, 8, 32))
        # Range follows the data on each side (at least +/-3.2 SD), so a long
        # tail on one side doesn't squeeze the other into a few bars.
        lo, hi = min(resid.min(), -3.2 * sd), max(resid.max(), 3.2 * sd)
        edges = np.linspace(lo, hi, bins + 1)
        right.hist(resid, bins=edges, density=True, color=QUIET,
                   edgecolor=PAPER, linewidth=0.8, zorder=2)
        g = np.linspace(lo, hi, 400)
        right.plot(g, np.exp(-0.5 * (g / sd) ** 2) / (sd * np.sqrt(2 * np.pi)),
                   color=ORANGE, linewidth=2.6, zorder=3)
        right.set_yticks([])
        right.set_xlabel(resid_label)
        if resid_fmt:
            right.xaxis.set_major_formatter(FuncFormatter(resid_fmt))
        right.xaxis.set_major_locator(MaxNLocator(5))
        right.spines["left"].set_visible(False)
        tidy(right, grid=None)
        right.spines["left"].set_visible(False)
    else:
        if check == "independence":
            rx = order if order is not None else np.arange(1, len(resid) + 1)
            idx = np.argsort(rx)
            rx_sorted = np.asarray(rx)[idx]
            right.plot(rx_sorted, resid[idx], color=QUIET, linewidth=1.0, zorder=2)
            right.set_xlabel(order_label)
        elif check == "linearity":
            rx = x
            right.set_xlabel(xlabel)
            if log_x:
                right.set_xscale("log")
            if x_fmt:
                right.xaxis.set_major_formatter(FuncFormatter(x_fmt))
                right.xaxis.set_minor_formatter(FuncFormatter(lambda *_: ""))
            if x_ticks is not None:
                right.set_xticks(x_ticks)
        else:  # equal-variability
            rx = 10**fitted if log_y else fitted
            right.set_xlabel("Fitted value")
            if log_y:
                right.set_xscale("log")
            if y_fmt:
                right.xaxis.set_major_formatter(FuncFormatter(y_fmt))
                right.xaxis.set_minor_formatter(FuncFormatter(lambda *_: ""))
        right.scatter(rx, resid, s=size if check != "independence" else size * 0.7,
                      color=INK, alpha=alpha, edgecolor=PAPER,
                      linewidth=0.6 if small else 0.3, zorder=3)
        right.axhline(0, color=ORANGE, linewidth=2, zorder=4)
        lim = np.abs(resid).max() * 1.12
        right.set_ylim(-lim, lim)
        right.set_ylabel(resid_label)
        if resid_fmt:
            right.yaxis.set_major_formatter(FuncFormatter(resid_fmt))
        if order_is_date and check == "independence":
            right.xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=6))
            right.xaxis.set_major_formatter(mdates.ConciseDateFormatter(
                right.xaxis.get_major_locator()))
        tidy(right)
    fig.build_parts = {"fit_line": fit_line, "diagnostic": right, "left_title": left_title}
    return fig


# --------------------------------------------------------------------------
# Slide builds
# --------------------------------------------------------------------------

VERDICT_GID = "verdict-stamp"
VERDICT_OPACITY = 0.4


def apply_build(fig, build: int, meets: bool):
    """Turn a full figure into build 0 (data only), 1 (as drawn), or 2 (+ verdict).

    Build 0 hides the line and the diagnostic panel instead of never drawing
    them, so both builds keep identical axis limits and the points don't jump.
    """
    parts = fig.build_parts
    if build == 0:
        parts["fit_line"].set_visible(False)
        parts["diagnostic"].set_visible(False)
        parts["left_title"].set_text("Data")
    if build == 2:
        # Centered in the gutter between the panels, tilted across both.
        # Libre Franklin is vendored in Regular only, so a same-color stroke
        # thickens it to bold; the opacity goes on the whole group in the SVG
        # (see save_svg) so stroke and fill don't stack into darker seams.
        fig.text(0.5275, 0.45, "Meets criteria" if meets else "Does not meet criteria",
                 fontsize=50, color=ORANGE, rotation=18, ha="center", va="center",
                 gid=VERDICT_GID, zorder=10,
                 path_effects=[patheffects.withStroke(linewidth=3.2, foreground=ORANGE)])


def save_svg(fig, out: Path):
    buf = io.StringIO()
    # No bbox_inches="tight": that would crop away the exact 1000 x 618 canvas.
    fig.savefig(buf, format="svg", facecolor=PAPER)
    svg, n = re.subn(f'<g id="{VERDICT_GID}">',
                     f'<g id="{VERDICT_GID}" opacity="{VERDICT_OPACITY}">', buf.getvalue())
    if VERDICT_GID in svg and n != 1:
        raise RuntimeError(f"{out.name}: could not set the verdict stamp's opacity")
    out.write_text(svg)


# --------------------------------------------------------------------------
# Real data
# --------------------------------------------------------------------------

_cache: dict[str, object] = {}


def homes(n=300, seed=418) -> pl.DataFrame:
    """A random sample of Cook County single-family sales, filtered as in Week 5/8."""
    if "homes" not in _cache:
        df = pl.read_csv(
            DATASETS / "cook-county-home-sales-2025" / "cook-county-home-sales-2025.csv",
            ignore_errors=True,
        )
        _cache["homes"] = df.filter(
            (pl.col("property_group") == "Single-Family")
            & (~pl.col("is_multisale"))
            & (pl.col("sale_price") > 10_000)
            & pl.col("building_sqft").is_not_null()
        )
    return _cache["homes"].sample(n, seed=seed)


HOME_SQFT_TICKS = [500, 1000, 2000, 4000]
HOME_PRICE_TICKS = [30_000, 100_000, 300_000, 1_000_000, 3_000_000]


def olympics(event: str, since: int = 1900) -> pl.DataFrame:
    """Olympic 100 m winning times: Tatem et al. (2004) table S1 + 2008-2024."""
    df = pl.concat([
        pl.read_csv(OLYMPICS / "tatem-2004-table-s1.csv", infer_schema_length=0),
        pl.read_csv(OLYMPICS / "olympic-100m-2008-2024.csv", infer_schema_length=0),
    ]).with_columns(pl.all().cast(pl.Float64, strict=False))
    return df.drop_nulls(event).filter(pl.col("year") >= since)


def airline() -> pl.DataFrame:
    return pl.read_csv(DATASETS / "airline-passengers" / "airline-passengers.csv",
                       try_parse_dates=True)


def movies() -> pl.DataFrame:
    return (pl.read_csv(DATASETS / "movies-from-imdb" / "popular.csv",
                        infer_schema_length=0)
            .with_columns(pl.col("startYear", "runtimeMinutes", "averageRating",
                                 "numVotes").cast(pl.Float64, strict=False))
            .drop_nulls(["runtimeMinutes", "averageRating", "numVotes"]))


def tall_buildings() -> pl.DataFrame:
    return (pl.read_csv(DATASETS / "chicago-tall-buildings" / "chicago_tall_buildings.csv",
                        infer_schema_length=0)
            .with_columns(pl.all().cast(pl.Float64, strict=False))
            .drop_nulls(["stories", "number_of_units"])
            .filter(pl.col("number_of_units") > 0))


def elections() -> pl.DataFrame:
    return pl.read_csv(DATASETS / "us-presidential-elections" / "elections.csv")


def cta_station_averages(year: int) -> pl.DataFrame:
    """Each 'L' station's mean daily entries on weekdays and on weekends/holidays.

    daytype is W (weekday), A (Saturday), or U (Sunday/holiday) in the source.
    """
    key = f"cta-stations-{year}"
    if key not in _cache:
        _cache[key] = _cta_station_averages(year)
    return _cache[key]


def _cta_station_averages(year: int) -> pl.DataFrame:
    return (pl.scan_csv(DATASETS / "cta-ridership" / "Station_Entries_-_Daily_Totals_20260527.csv",
                        schema_overrides={"rides": pl.Utf8})
            .with_columns(pl.col("date").str.to_date("%m/%d/%Y"),
                          pl.col("rides").str.replace_all(",", "").cast(pl.Float64))
            .filter(pl.col("date").dt.year() == year)
            .group_by("stationname")
            .agg(pl.col("rides").filter(pl.col("daytype") == "W").mean().alias("weekday"),
                 pl.col("rides").filter(pl.col("daytype") != "W").mean().alias("weekend"))
            .drop_nulls()
            .sort("stationname")
            .collect())


def cta_annual() -> pl.DataFrame:
    return (pl.read_csv(DATASETS / "cta-ridership" / "Annual_Boarding_Totals_20260527.csv",
                        infer_schema_length=0)
            .with_columns(pl.all().str.replace_all(",", "").cast(pl.Float64)))


def uic_halsted() -> pl.DataFrame:
    return (pl.read_csv(DATASETS / "cta-ridership" / "Station_Entries_UIC-Halsted_2025.csv")
            .with_columns(pl.col("date").str.to_date("%m/%d/%Y"),
                          pl.col("rides").str.replace_all(",", "").cast(pl.Float64)))


def millions(v, _=None):
    return f"{v / 1e6:g}M" if v else "0"


def years(v, _=None):
    return f"{v:.0f}"


def seconds(v, _=None):
    return f"{v:.2f}s"


# --------------------------------------------------------------------------
# Synthetic data. Seeds are fixed so the figures rebuild identically.
# --------------------------------------------------------------------------

def rng(seed):
    return np.random.default_rng(seed)


# --------------------------------------------------------------------------
# Linearity
# --------------------------------------------------------------------------

@figure("linearity-positive-example-a")
def linearity_positive_1():
    h = homes()
    return panels(
        title="Cook County home sales, 2025",
        caption="300 single-family sales: building size vs. sale price, both on log scales",
        x=h["building_sqft"], y=h["sale_price"], log_x=True, log_y=True,
        xlabel="Building sqft (log scale)", ylabel="Sale price (log scale)",
        x_fmt=thousands, y_fmt=dollars, resid_label="Residual (log10 dollars)",
        x_ticks=HOME_SQFT_TICKS, y_ticks=HOME_PRICE_TICKS,
        check="linearity")


@figure("linearity-positive-example-b")
def linearity_positive_2():
    df = olympics("women_s").drop_nulls("men_s")
    first, last = int(df["year"].min()), int(df["year"].max())
    return panels(
        title=f"Olympic 100 m winners, {first}–{last}",
        caption="Each point is one Games: men’s vs. women’s winning time",
        x=df["men_s"], y=df["women_s"], xlabel="Men’s winning time",
        ylabel="Women’s winning time", x_fmt=seconds, y_fmt=seconds,
        resid_label="Residual (seconds)", check="linearity")


@figure("linearity-positive-example-c")
def linearity_positive_3():
    r = rng(1)
    x = r.uniform(0, 10, 120)
    y = 3 + 1.6 * x + r.normal(0, 1.8, x.size)
    return panels(
        title="Synthetic data A",
        caption="120 points",
        x=x, y=y, xlabel="x", ylabel="y", check="linearity")


@figure("linearity-negative-example-a")
def linearity_negative_1():
    df = cta_annual()
    return panels(
        title="CTA rail ridership, 1988–2025",
        caption="Total ‘L’ boardings each year, City of Chicago Data Portal",
        x=df["year"], y=df["rail"], xlabel="Year", ylabel="Rail boardings",
        x_fmt=years, y_fmt=lambda v, _=None: f"{v / 1e6:g}M",
        resid_fmt=lambda v, _=None: f"{v / 1e6:g}M",
        resid_label="Residual (boardings)", check="linearity")


@figure("linearity-negative-example-b")
def linearity_negative_2():
    r = rng(2)
    x = r.uniform(-3, 3, 120)
    y = 2 + 0.4 * x + 0.9 * x**2 + r.normal(0, 0.9, x.size)
    return panels(
        title="Synthetic data B",
        caption="120 points",
        x=x, y=y, xlabel="x", ylabel="y", check="linearity")


@figure("linearity-negative-example-c")
def linearity_negative_3():
    r = rng(3)
    x = r.uniform(0, 10, 120)
    y = 10 * (1 - np.exp(-0.45 * x)) + r.normal(0, 0.55, x.size)
    return panels(
        title="Synthetic data C",
        caption="120 points",
        x=x, y=y, xlabel="x", ylabel="y", check="linearity")


# --------------------------------------------------------------------------
# Independence
# --------------------------------------------------------------------------

@figure("independence-positive-example-a")
def independence_positive_1():
    h = homes().sort("sale_date").with_columns(pl.col("sale_date").str.to_date())
    return panels(
        title="Cook County home sales, 2025",
        caption="300 randomly sampled sales: building size vs. price (log scales), by sale date",
        x=h["building_sqft"], y=h["sale_price"], log_x=True, log_y=True,
        xlabel="Building sqft (log scale)", ylabel="Sale price (log scale)",
        x_fmt=thousands, y_fmt=dollars, resid_label="Residual (log10 dollars)",
        x_ticks=HOME_SQFT_TICKS, y_ticks=HOME_PRICE_TICKS,
        order=h["sale_date"].to_numpy(), order_label="Sale date", order_is_date=True,
        check="independence")


@figure("independence-positive-example-b")
def independence_positive_2():
    df = tall_buildings().drop_nulls("year_built")
    # Jitter ties so buildings finished the same year keep a fixed, arbitrary order.
    order = df["year_built"].to_numpy() + rng(12).uniform(-0.4, 0.4, df.height)
    return panels(
        title="Chicago buildings with 10+ stories",
        caption="Stories vs. residential units; residuals on the right in order of year built",
        x=df["stories"], y=df["number_of_units"],
        xlabel="Stories", ylabel="Units", y_fmt=thousands,
        resid_label="Residual (units)", order=order, order_label="Year built",
        x_fmt=None, check="independence")


@figure("independence-positive-example-c")
def independence_positive_3():
    r = rng(4)
    x = r.uniform(0, 10, 100)
    y = 5 + 0.8 * x + r.normal(0, 1.5, x.size)
    return panels(
        title="Synthetic data D",
        caption="100 points, plotted on the right in the order they were collected",
        x=x, y=y, xlabel="x", ylabel="y", check="independence")


@figure("independence-negative-example-a")
def independence_negative_1():
    df = airline()
    t = np.arange(df.height)
    return panels(
        title="Airline passengers, 1949–1960",
        caption="Monthly international passengers (thousands), log scale, Box & Jenkins",
        x=1949 + t / 12, y=df["Passengers"], log_y=True,
        xlabel="Year", ylabel="Passengers (thousands, log scale)",
        x_fmt=years, y_fmt=lambda v, _=None: f"{v:g}", y_ticks=[100, 200, 300, 400, 600],
        resid_label="Residual (log10 passengers)",
        order=df["Month"].to_numpy(), order_label="Month", order_is_date=True,
        check="independence")


@figure("independence-negative-example-b")
def independence_negative_2():
    df = uic_halsted().filter(pl.col("daytype") == "W")
    day = df["date"].dt.ordinal_day().to_numpy()
    return panels(
        title="CTA UIC-Halsted station, 2025",
        caption="Weekday Blue Line entries at UIC-Halsted, with a straight-line trend through the year",
        x=day, y=df["rides"], xlabel="Day of the year", ylabel="Entries",
        y_fmt=thousands, resid_fmt=thousands, resid_label="Residual (entries)",
        order=df["date"].to_numpy(), order_label="Date", order_is_date=True,
        check="independence")


@figure("independence-negative-example-c")
def independence_negative_3():
    r = rng(5)
    n = 100
    x = r.uniform(0, 10, n)
    e = np.zeros(n)
    for i in range(1, n):  # AR(1): each error carries most of the last one
        e[i] = 0.85 * e[i - 1] + r.normal(0, 0.8)
    y = 5 + 0.8 * x + e
    return panels(
        title="Synthetic data E",
        caption="100 points, plotted on the right in the order they were collected",
        x=x, y=y, xlabel="x", ylabel="y", check="independence")


# --------------------------------------------------------------------------
# Nearly normal residuals
# --------------------------------------------------------------------------

@figure("normality-positive-example-a")
def normality_positive_1():
    df = olympics("men_s", since=1948)
    return panels(
        title="Olympic men’s 100 m, 1948–2024",
        caption="Winning time at each Games since World War II",
        x=df["year"], y=df["men_s"], xlabel="Year", ylabel="Winning time",
        x_fmt=years, y_fmt=seconds, resid_label="Residual (seconds)",
        check="normality")


@figure("normality-positive-example-b")
def normality_positive_2():
    r = rng(6)
    x = r.uniform(0, 10, 200)
    y = 4 + 1.2 * x + r.normal(0, 2, x.size)
    return panels(
        title="Synthetic data F",
        caption="200 points",
        x=x, y=y, xlabel="x", ylabel="y", check="normality")


@figure("normality-positive-example-c")
def normality_positive_3():
    r = rng(7)
    x = r.normal(50, 12, 400)
    y = 80 - 0.6 * x + r.normal(0, 5, x.size)
    return panels(
        title="Synthetic data G",
        caption="400 points",
        x=x, y=y, xlabel="x", ylabel="y", check="normality")


@figure("normality-negative-example-a")
def normality_negative_1():
    df = movies().drop_nulls("startYear")
    return panels(
        title="IMDb’s 1,000 most-rated movies",
        caption="Release year vs. number of user ratings (IMDb non-commercial datasets, June 2026)",
        x=df["startYear"], y=df["numVotes"], xlabel="Release year",
        ylabel="Number of ratings", x_fmt=years,
        y_fmt=millions, resid_fmt=millions,
        resid_label="Residual (ratings)", check="normality")


@figure("normality-negative-example-b")
def normality_negative_2():
    df = elections()
    first, last = df["Year"].min(), df["Year"].max()
    return panels(
        title=f"US presidential elections, {first}–{last}",
        caption="Each point is one candidate: election year vs. share of the popular vote (Data 100 elections.csv)",
        x=df["Year"], y=df["%"], xlabel="Election year", ylabel="Share of popular vote (%)",
        x_fmt=years, resid_label="Residual (percentage points)", check="normality")


@figure("normality-negative-example-c")
def normality_negative_3():
    r = rng(8)
    n = 200
    x = r.uniform(0, 10, n)
    # Right-skewed errors: exponential, shifted to mean zero
    y = 3 + 1.0 * x + r.exponential(2.5, n) - 2.5
    return panels(
        title="Synthetic data H",
        caption="200 points",
        x=x, y=y, xlabel="x", ylabel="y", check="normality")


# --------------------------------------------------------------------------
# Equal variability
# --------------------------------------------------------------------------

@figure("equal-variability-positive-example-a")
def equal_variability_positive_1():
    df = movies()
    return panels(
        title="IMDb’s 1,000 most-rated movies",
        caption="Runtime vs. average rating",
        x=df["runtimeMinutes"], y=df["averageRating"],
        xlabel="Runtime (minutes)", ylabel="Average rating (1–10)",
        resid_label="Residual (rating points)", check="equal-variability")


@figure("equal-variability-positive-example-b")
def equal_variability_positive_2():
    r = rng(9)
    x = r.uniform(0, 10, 150)
    y = 2 + 2.1 * x + r.normal(0, 2.2, x.size)
    return panels(
        title="Synthetic data I",
        caption="150 points",
        x=x, y=y, xlabel="x", ylabel="y", check="equal-variability")


@figure("equal-variability-positive-example-c")
def equal_variability_positive_3():
    r = rng(10)
    x = r.uniform(20, 80, 60)
    y = 120 - 0.9 * x + r.normal(0, 6, x.size)
    return panels(
        title="Synthetic data J",
        caption="60 points",
        x=x, y=y, xlabel="x", ylabel="y", check="equal-variability")


@figure("equal-variability-negative-example-a")
def equal_variability_negative_1():
    df = cta_station_averages(2025)
    return panels(
        title="CTA ‘L’ stations, 2025",
        caption="Each point is one station: average weekday vs. weekend/holiday entries (City of Chicago Data Portal)",
        x=df["weekday"], y=df["weekend"], xlabel="Average weekday entries",
        ylabel="Average weekend/holiday entries", x_fmt=thousands, y_fmt=thousands,
        resid_fmt=thousands, resid_label="Residual (entries)",
        check="equal-variability")


@figure("equal-variability-negative-example-b")
def equal_variability_negative_2():
    df = airline()
    t = np.arange(df.height)
    return panels(
        title="Airline passengers, 1949–1960",
        caption="Monthly international passengers (thousands), Box & Jenkins",
        x=1949 + t / 12, y=df["Passengers"], xlabel="Year",
        ylabel="Passengers (thousands)", x_fmt=years,
        resid_label="Residual (thousands)", check="equal-variability")


@figure("equal-variability-negative-example-c")
def equal_variability_negative_3():
    r = rng(11)
    x = r.uniform(0, 10, 150)
    y = 30 - 1.5 * x + r.normal(0, 1, x.size) * (5.5 - 0.5 * x)
    return panels(
        title="Synthetic data K",
        caption="150 points",
        x=x, y=y, xlabel="x", ylabel="y", check="equal-variability")


# --------------------------------------------------------------------------

def main(argv: list[str]) -> None:
    if FONT_PATH.exists():
        font_manager.fontManager.addfont(str(FONT_PATH))
        plt.rcParams["font.family"] = font_manager.FontProperties(
            fname=str(FONT_PATH)).get_name()
    # Text as paths, per STYLE.md: the SVG stays self-contained.
    plt.rcParams["svg.fonttype"] = "path"

    wanted = argv or list(FIGURES)
    unknown = [name for name in wanted if name not in FIGURES]
    if unknown:
        raise SystemExit(f"unknown figure(s): {', '.join(unknown)}\n"
                         f"available: {', '.join(FIGURES)}")
    print(f"writing {len(wanted)} example(s) x 3 builds to {OUT_DIR.relative_to(REPO_ROOT)}")
    for name in wanted:
        meets = "-positive-" in name
        for build in range(3):
            fig = FIGURES[name]()
            apply_build(fig, build, meets)
            out = OUT_DIR / f"{name}-v{build}.svg"
            save_svg(fig, out)
            plt.close(fig)
            print(f"  wrote {out.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
