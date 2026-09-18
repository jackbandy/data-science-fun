#!/usr/bin/env python3
"""Figures for the Week 5 "visualization basics" slides.

NOTICE: this file was substantially drafted by an LLM coding system. It is
maintained and vetted by jxb@uic.edu.

One script, one folder of SVGs. Every figure here illustrates a *choice* the
slides are arguing about — scale, conditioning, context, transformation,
colour, length, smoothing — so figures come in matched pairs or short builds
that differ in exactly one decision.

Follows docs/assets/STYLE.md: golden-ratio canvases, grayscale neutrals with
orange reserved for the focal element, vendored Libre Franklin drawn as paths
so the SVG is self-contained.

Data:
  * Cook County home sales 2025 and CTA ridership come from datasets/ in this
    repo (see each dataset's README for provenance).
  * Planned Parenthood service counts and the Kepler orbital elements are
    printed on the source slides and are reproduced here as published.
  * A few figures are explicitly synthetic (the four scatter-plot forms, the
    smoothing walkthrough); they illustrate shapes, not measurements.

Usage:  python3 make_viz_basics_figures.py [name ...]
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import polars as pl
from matplotlib import font_manager
from matplotlib import patheffects as pe
from matplotlib.lines import Line2D
from matplotlib.patches import Circle

OUT_DIR = Path(__file__).resolve().parent
REPO_ROOT = OUT_DIR.parents[2]
DATASETS = REPO_ROOT / "datasets"
FONT_PATH = OUT_DIR.parent / "fonts" / "libre-franklin" / "LibreFranklin-Regular.ttf"

# STYLE.md palette
INK = "#1A1A1A"
TEXT = "#444444"
STEEL = "#565A5C"
MUTED = "#777777"
QUIET = "#AAAAAA"
BORDER = "#DDDDDD"
SOFT_GRAY = "#F4F4F2"
PAPER = "#FFFFFF"
ORANGE = "#F9461C"
ORANGE_DARK = "#C83214"

# Official CTA 'L' route colors (STYLE.md / CTA developer branding guidelines).
CTA = {
    "Red": "#C60C30", "Blue": "#00A1DE", "Brown": "#62361B", "Green": "#009B3A",
    "Orange": "#F9461C", "Purple": "#522398", "Pink": "#E27EA6", "Yellow": "#F9E300",
}

PHI = (1 + 5**0.5) / 2
WIDTH_PX = 1000
HEIGHT_PX = round(WIDTH_PX / PHI)
DPI = 100

FIGURES: dict[str, callable] = {}


def figure(name: str):
    """Register a builder under the filename stem it writes."""
    def wrap(fn):
        FIGURES[name] = fn
        return fn
    return wrap


def new_fig(width=WIDTH_PX, height=None, **kw):
    height = height or round(width / PHI)
    fig, ax = plt.subplots(figsize=(width / DPI, height / DPI), dpi=DPI, **kw)
    fig.patch.set_facecolor(PAPER)
    for a in np.atleast_1d(ax).ravel():
        a.set_facecolor(PAPER)
    return fig, ax


def tidy(ax, *, grid="y", spines=("left", "bottom")):
    """The deck's default axis furniture: two hairline spines, one grid."""
    for side in ("top", "right", "left", "bottom"):
        ax.spines[side].set_visible(side in spines)
        ax.spines[side].set_color(BORDER)
    if grid:
        ax.grid(axis=grid, color=BORDER, linewidth=0.8, alpha=0.7)
    ax.set_axisbelow(True)
    ax.tick_params(colors=STEEL, labelsize=11, length=0)
    for lbl in (ax.xaxis.label, ax.yaxis.label):
        lbl.set_color(STEEL)
        lbl.set_fontsize(13)
    return ax


def title(ax, text, *, pad=14, size=17, color=INK):
    ax.set_title(text, fontsize=size, color=color, pad=pad, loc="left")


def save(fig, name):
    out = OUT_DIR / f"{name}.svg"
    fig.savefig(out, format="svg", facecolor=PAPER, bbox_inches="tight",
                pad_inches=0.12)
    plt.close(fig)
    print(f"  wrote {out.relative_to(REPO_ROOT)}")


# --------------------------------------------------------------------------
# Data loaders (cached; several figures share the same frames)
# --------------------------------------------------------------------------

_cache: dict[str, object] = {}


def homes() -> pl.DataFrame:
    """Cook County single-family sales, filtered the way the slides filter them."""
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
            & pl.col("bedrooms").is_not_null()
        )
    return _cache["homes"]


def annual_boardings() -> pl.DataFrame:
    """CTA boardings by mode and year, 1988 to present."""
    if "annual" not in _cache:
        df = pl.read_csv(DATASETS / "cta-ridership" / "Annual_Boarding_Totals_20260527.csv")
        _cache["annual"] = df.with_columns(
            [pl.col(c).cast(pl.Utf8).str.replace_all(",", "").cast(pl.Float64)
             for c in ("bus", "paratransit", "rail", "total")]
            + [pl.col("year").cast(pl.Int64)]
        ).sort("year")
    return _cache["annual"]


def entries_by_line() -> pl.DataFrame:
    """Median 2019 weekday entries per station, summed by 'L' line.

    Stations serving several lines are counted once per line, which is how the
    CTA's own stop list is shaped; the figure is about comparing magnitudes,
    not about an exact ridership total.
    """
    if "byline" not in _cache:
        stops = pl.read_csv(
            DATASETS / "chicago-l-stations" / "CTA_List_of_'L'_Stops_20260527.csv"
        )
        flags = {"RED": "Red", "BLUE": "Blue", "G": "Green", "BRN": "Brown",
                 "P": "Purple", "Y": "Yellow", "Pnk": "Pink", "O": "Orange"}
        lines = (
            stops.select(["MAP_ID"] + list(flags))
            .unique(subset="MAP_ID")
            .unpivot(index="MAP_ID", variable_name="flag", value_name="on")
            .filter(pl.col("on").cast(pl.Utf8).str.to_lowercase() == "true")
            .with_columns(pl.col("flag").replace_strict(flags).alias("line"))
            .select(pl.col("MAP_ID").alias("station_id"), "line")
        )
        daily = pl.read_csv(
            DATASETS / "cta-ridership" / "Station_Entries_-_Daily_Totals_20260527.csv",
            ignore_errors=True,
        ).with_columns(pl.col("rides").cast(pl.Utf8).str.replace_all(",", "").cast(pl.Int64))
        weekday = (
            daily.filter(pl.col("date").str.ends_with("2019") & (pl.col("daytype") == "W"))
            .group_by("station_id")
            .agg(pl.col("rides").median().alias("rides"))
            .with_columns(pl.col("station_id").cast(pl.Int64))
        )
        _cache["byline"] = (
            lines.join(weekday, on="station_id")
            .group_by("line").agg(pl.col("rides").sum())
            .sort("rides", descending=True)
        )
    return _cache["byline"]


# --------------------------------------------------------------------------
# Bivariate relationships
# --------------------------------------------------------------------------

def _bedroom_frame() -> pl.DataFrame:
    """Home sales bucketed into four bedroom counts and three price tiers."""
    # Escaped dollars: two unescaped $ in one label put matplotlib into
    # mathtext mode, which swallows the signs and italicizes the digits.
    tiers = ["Under $200k", r"\$200k–\$400k", "Over $400k"]
    beds = ["2", "3", "4", "5+"]
    return (
        homes()
        .filter(pl.col("bedrooms").is_between(2, 8))
        .with_columns(
            pl.when(pl.col("bedrooms") >= 5).then(pl.lit("5+"))
              .otherwise(pl.col("bedrooms").cast(pl.Utf8)).alias("beds"),
            pl.when(pl.col("sale_price") < 200_000).then(pl.lit(tiers[0]))
              .when(pl.col("sale_price") < 400_000).then(pl.lit(tiers[1]))
              .otherwise(pl.lit(tiers[2])).alias("tier"),
        )
        .with_columns(pl.col("beds").cast(pl.Enum(beds)),
                      pl.col("tier").cast(pl.Enum(tiers)))
    )


# Three price tiers are ordered, so they get an ordered ramp of one hue rather
# than three unrelated colours: the legend then reads low-to-high on its own.
TIER_COLORS = ["#E6E2DF", "#B9877A", ORANGE]


def _grouped_bars(ax, counts: np.ndarray, beds, tiers, colors, width=0.26):
    xs = np.arange(len(beds))
    for j, (tier, color) in enumerate(zip(tiers, colors)):
        ax.bar(xs + (j - 1) * width, counts[:, j], width=width, color=color,
               edgecolor=PAPER, linewidth=0.8, label=tier, zorder=3)
    ax.set_xticks(xs)
    ax.set_xticklabels(beds)
    ax.set_xlabel("Bedrooms")
    leg = ax.legend(frameon=False, fontsize=11, loc="upper center",
                    bbox_to_anchor=(0.5, -0.12), ncol=2,
                    handlelength=1.1, handleheight=1.1, columnspacing=1.6)
    for t in leg.get_texts():
        t.set_color(STEEL)
    return xs


def _tier_counts(df, beds, tiers) -> np.ndarray:
    wide = (df.group_by(["beds", "tier"]).len()
              .pivot("tier", index="beds", values="len")
              .sort("beds").fill_null(0))
    return np.array([[wide.filter(pl.col("beds") == b)[t].item() for t in tiers]
                     for b in beds], dtype=float)


@figure("two-categorical-counts")
def two_categorical_counts():
    """Raw counts: the tall bedroom categories drown out the short ones."""
    df = _bedroom_frame()
    beds, tiers = ["2", "3", "4", "5+"], ["Under $200k", r"\$200k–\$400k", "Over $400k"]
    counts = _tier_counts(df, beds, tiers)
    fig, ax = new_fig(width=660, height=580)
    _grouped_bars(ax, counts, beds, tiers, TIER_COLORS)
    ax.set_ylabel("Sales")
    tidy(ax)
    title(ax, "Counts: price tier within bedroom count")
    return fig


@figure("two-categorical-normalized")
def two_categorical_normalized():
    """The same table normalized within bedrooms: composition, not volume."""
    df = _bedroom_frame()
    beds, tiers = ["2", "3", "4", "5+"], ["Under $200k", r"\$200k–\$400k", "Over $400k"]
    counts = _tier_counts(df, beds, tiers)
    props = counts / counts.sum(axis=1, keepdims=True)
    fig, ax = new_fig(width=660, height=580)
    _grouped_bars(ax, props, beds, tiers, TIER_COLORS)
    ax.set_ylabel("Share of sales at that bedroom count")
    ax.set_ylim(0, 0.75)
    ax.set_yticks(np.arange(0, 0.76, 0.25))
    ax.set_yticklabels([f"{v:.0%}" for v in np.arange(0, 0.76, 0.25)])
    tidy(ax)
    title(ax, "Normalized within bedroom count")
    return fig


def _price_by_beds():
    df = _bedroom_frame().filter(pl.col("sale_price") < 2_000_000)
    beds = ["2", "3", "4", "5+"]
    return beds, [df.filter(pl.col("beds") == b)["sale_price"].to_numpy() / 1000
                  for b in beds]


@figure("box-by-category")
def box_by_category():
    """One quantitative variable split by one categorical variable."""
    beds, groups = _price_by_beds()
    fig, ax = new_fig(width=620, height=540)
    bp = ax.boxplot(groups, labels=beds, widths=0.5, patch_artist=True,
                    showfliers=False)
    for patch in bp["boxes"]:
        patch.set(facecolor=SOFT_GRAY, edgecolor=INK, linewidth=1.3)
    for part in ("whiskers", "caps"):
        for line in bp[part]:
            line.set(color=INK, linewidth=1.1)
    for line in bp["medians"]:
        line.set(color=ORANGE, linewidth=2.4)
    ax.set_xlabel("Bedrooms")
    ax.set_ylabel("Sale price (thousands)")
    tidy(ax)
    title(ax, "Side-by-side box plots")
    return fig


@figure("violin-by-category")
def violin_by_category():
    """The same split as a violin: a box plot that keeps the shape."""
    beds, groups = _price_by_beds()
    fig, ax = new_fig(width=620, height=540)
    parts = ax.violinplot(groups, showextrema=False, widths=0.8)
    for body in parts["bodies"]:
        body.set(facecolor=SOFT_GRAY, edgecolor=INK, linewidth=1.2, alpha=1.0)
    for i, g in enumerate(groups, start=1):
        q1, med, q3 = np.percentile(g, [25, 50, 75])
        ax.plot([i, i], [q1, q3], color=INK, linewidth=4, solid_capstyle="butt", zorder=4)
        ax.plot([i], [med], marker="o", color=ORANGE, markersize=6, zorder=5)
    ax.set_xticks(range(1, len(beds) + 1))
    ax.set_xticklabels(beds)
    ax.set_xlabel("Bedrooms")
    ax.set_ylabel("Sale price (thousands)")
    tidy(ax)
    title(ax, "Side-by-side violin plots")
    return fig


def _city_suburb_prices():
    df = homes().filter(pl.col("sale_price").is_between(30_000, 1_500_000))
    city = df.filter(pl.col("city") == "CHICAGO")["sale_price"].to_numpy() / 1000
    burb = df.filter(pl.col("city") != "CHICAGO")["sale_price"].to_numpy() / 1000
    return city, burb


@figure("overlaid-histogram")
def overlaid_histogram():
    """Two groups, one axis: overlaid histograms need transparency to work."""
    city, burb = _city_suburb_prices()
    bins = np.linspace(0, 1000, 45)
    fig, ax = new_fig()
    ax.hist(city, bins=bins, density=True, color=ORANGE, alpha=0.55,
            label="Chicago", zorder=3)
    ax.hist(burb, bins=bins, density=True, color=STEEL, alpha=0.55,
            label="Suburban Cook County", zorder=3)
    ax.set_xlabel("Sale price (thousands)")
    ax.set_ylabel("Density")
    ax.set_yticklabels([])
    leg = ax.legend(frameon=False, fontsize=12)
    for t in leg.get_texts():
        t.set_color(STEEL)
    tidy(ax)
    title(ax, "Overlaid histograms")
    return fig


@figure("overlaid-density")
def overlaid_density():
    """The same two groups as smooth curves: easier to compare, harder to audit."""
    from scipy.stats import gaussian_kde
    city, burb = _city_suburb_prices()
    grid = np.linspace(0, 1000, 400)
    fig, ax = new_fig()
    for values, color, label in ((city, ORANGE, "Chicago"),
                                 (burb, STEEL, "Suburban Cook County")):
        dens = gaussian_kde(values)(grid)
        ax.fill_between(grid, dens, color=color, alpha=0.18, zorder=2)
        ax.plot(grid, dens, color=color, linewidth=2.2, label=label, zorder=3)
    ax.set_xlabel("Sale price (thousands)")
    ax.set_ylabel("Density")
    ax.set_yticklabels([])
    leg = ax.legend(frameon=False, fontsize=12)
    for t in leg.get_texts():
        t.set_color(STEEL)
    tidy(ax)
    title(ax, "Overlaid density curves")
    return fig


@figure("three-univariate")
def three_univariate():
    """Three one-variable plots of the same table: no relationship is visible."""
    df = _bedroom_frame()
    fig, axes = plt.subplots(1, 3, figsize=(WIDTH_PX / DPI, 380 / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)

    beds = ["2", "3", "4", "5+"]
    counts = [df.filter(pl.col("beds") == b).height for b in beds]
    axes[0].bar(beds, counts, color=QUIET, width=0.62, zorder=3)
    axes[0].set_xlabel("Bedrooms")

    tiers = ["Under $200k", r"\$200k–\$400k", "Over $400k"]
    tcounts = [df.filter(pl.col("tier") == t).height for t in tiers]
    axes[1].bar(["<200k", "200–400k", ">400k"], tcounts, color=QUIET, width=0.62, zorder=3)
    axes[1].set_xlabel("Price tier")

    axes[2].hist(df["sale_price"].to_numpy() / 1000, bins=np.linspace(0, 900, 30),
                 color=QUIET, zorder=3)
    axes[2].set_xlabel("Sale price (thousands)")

    for ax in axes:
        ax.set_facecolor(PAPER)
        tidy(ax)
        ax.set_ylabel("")
        ax.tick_params(labelsize=10)
    axes[0].set_ylabel("Sales")
    fig.suptitle("Three univariate views of one table", x=0.005, ha="left",
                 fontsize=17, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    return fig


@figure("scatter-forms")
def scatter_forms():
    """Four shapes a scatter plot can uncover. Synthetic, on purpose."""
    rng = np.random.default_rng(418)
    n = 110
    x = np.sort(rng.uniform(0, 10, n))
    panels = [
        ("Simple linear", 0.9 * x + rng.normal(0, 0.8, n)),
        ("Simple nonlinear", 0.28 * x**2 + rng.normal(0, 0.8, n)),
        ("Unequal spread", 0.9 * x + rng.normal(0, 0.34 * x + 0.1, n)),
        ("Complex nonlinear", 0.6 * (x - 5) ** 2 - 6 + rng.normal(0, 1.1, n)),
    ]
    fig, axes = plt.subplots(2, 2, figsize=(WIDTH_PX / DPI, HEIGHT_PX / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    for ax, (label, y) in zip(axes.ravel(), panels):
        ax.set_facecolor(PAPER)
        ax.scatter(x, y, s=22, facecolor="none", edgecolor=INK, linewidth=0.9,
                   alpha=0.75, zorder=3)
        ax.set_title(label, fontsize=14, color=INK, pad=8, loc="left")
        tidy(ax, grid=None, spines=("left", "bottom"))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
    fig.tight_layout()
    return fig


# --------------------------------------------------------------------------
# Scale — the 2015 Planned Parenthood chart, three ways
#
# Four numbers, published in the Americans United for Life report Rep. Chaffetz
# displayed at the 29 Sep 2015 Oversight Committee hearing and printed on the
# chart itself. Only the *drawing* changes between these three figures.
# --------------------------------------------------------------------------

PP = {"year": [2006, 2013],
      "Cancer screening": [2_007_371, 935_573],
      "Abortion": [289_750, 327_000]}


@figure("scale-two-axes")
def scale_two_axes():
    """The published version: two series, two invisible scales, one crossing."""
    fig, ax = new_fig()
    yrs = PP["year"]
    screen, abort = PP["Cancer screening"], PP["Abortion"]

    # Each series is drawn in its own 0-1 space, which is exactly the trick:
    # the lines cross because they were stretched to, not because they met.
    def rescale(v, lo, hi):
        return [(x - lo) / (hi - lo) for x in v]

    ax.plot(yrs, rescale(screen, 800_000, 2_100_000), color="#F4A9A0",
            linewidth=5, marker="o", markersize=9, zorder=3)
    ax.plot(yrs, rescale(abort, 250_000, 400_000), color=ORANGE,
            linewidth=5, marker="o", markersize=9, zorder=3)

    ax.annotate("Cancer screening", xy=(2006, rescale(screen, 800_000, 2_100_000)[0]),
                xytext=(6, 12), textcoords="offset points", color="#C9736A", fontsize=14)
    ax.annotate("Abortion", xy=(2011.6, 0.63), xytext=(0, 0),
                textcoords="offset points", color=ORANGE, fontsize=14, ha="center")
    for x, y, v in ((2006, rescale(screen, 800_000, 2_100_000)[0], screen[0]),
                    (2013, rescale(screen, 800_000, 2_100_000)[1], screen[1]),
                    (2006, rescale(abort, 250_000, 400_000)[0], abort[0]),
                    (2013, rescale(abort, 250_000, 400_000)[1], abort[1])):
        ax.annotate(f"{v:,}", xy=(x, y), xytext=(0, -22 if x == 2006 else -22),
                    textcoords="offset points", ha="center", color=STEEL, fontsize=12)

    ax.set_xlim(2005.4, 2013.6)
    ax.set_ylim(-0.25, 1.25)
    ax.set_xticks(range(2006, 2014))
    ax.set_yticks([])
    tidy(ax, grid=None, spines=("bottom",))
    title(ax, "As published: no y-axis at all")
    return fig


@figure("scale-one-axis")
def scale_one_axis():
    """The same four numbers on one shared, labelled scale."""
    fig, ax = new_fig()
    yrs = PP["year"]
    ax.plot(yrs, PP["Cancer screening"], color=STEEL, linewidth=3,
            marker="o", markersize=8, label="Cancer screening", zorder=3)
    ax.plot(yrs, PP["Abortion"], color=ORANGE, linewidth=3,
            marker="o", markersize=8, label="Abortion", zorder=3)
    ax.set_xticks(yrs)
    ax.set_xlim(2005.4, 2013.6)
    ax.set_ylim(0, 2_200_000)
    ax.set_yticks(np.arange(0, 2_200_001, 500_000))
    ax.set_yticklabels([f"{v/1e6:g}M" for v in np.arange(0, 2_200_001, 500_000)])
    ax.set_ylabel("Services provided")
    leg = ax.legend(frameon=False, fontsize=12, loc="upper right")
    for t in leg.get_texts():
        t.set_color(STEEL)
    tidy(ax)
    title(ax, "One shared scale, starting at zero")
    return fig


@figure("scale-percent")
def scale_percent():
    """Neither series alone is the story: the mix is. So plot the mix."""
    fig, ax = new_fig()
    total = [s + a for s, a in zip(PP["Cancer screening"], PP["Abortion"])]
    share = [a / t for a, t in zip(PP["Abortion"], total)]
    xs = np.arange(2)
    ax.bar(xs, share, width=0.42, color=ORANGE, zorder=3)
    for x, v in zip(xs, share):
        ax.annotate(f"{v:.0%}", xy=(x, v), xytext=(0, 8), textcoords="offset points",
                    ha="center", color=INK, fontsize=15, fontweight="bold")
    ax.set_xticks(xs)
    ax.set_xticklabels([str(y) for y in PP["year"]])
    ax.set_ylim(0, 0.36)
    ax.set_yticks(np.arange(0, 0.36, 0.1))
    ax.set_yticklabels([f"{v:.0%}" for v in np.arange(0, 0.36, 0.1)])
    ax.set_ylabel("Abortions as a share of the two services")
    tidy(ax)
    title(ax, "Or plot the quantity actually in dispute")
    return fig


# --------------------------------------------------------------------------
# Conditioning — the same table, four drawings
# --------------------------------------------------------------------------

def _median_price_grid():
    """Median sale price by bedroom count, conditioned on Chicago vs suburbs."""
    beds = ["2", "3", "4", "5+"]
    df = (_bedroom_frame()
          .with_columns(pl.when(pl.col("city") == "CHICAGO").then(pl.lit("Chicago"))
                          .otherwise(pl.lit("Suburban Cook")).alias("where"))
          .group_by(["where", "beds"]).agg(pl.col("sale_price").median().alias("p")))
    grab = lambda w: [df.filter((pl.col("where") == w) & (pl.col("beds") == b))["p"].item() / 1000
                      for b in beds]
    return beds, grab("Chicago"), grab("Suburban Cook")


@figure("conditioning-bars")
def conditioning_bars():
    """Grouped bars: every value is legible, but the *gap* is not."""
    beds, chi, sub = _median_price_grid()
    fig, ax = new_fig()
    xs = np.arange(len(beds))
    ax.bar(xs - 0.18, chi, width=0.34, color=ORANGE, label="Chicago", zorder=3)
    ax.bar(xs + 0.18, sub, width=0.34, color=STEEL, label="Suburban Cook", zorder=3)
    ax.set_xticks(xs)
    ax.set_xticklabels(beds)
    ax.set_xlabel("Bedrooms")
    ax.set_ylabel("Median sale price (thousands)")
    leg = ax.legend(frameon=False, fontsize=12, loc="upper left")
    for t in leg.get_texts():
        t.set_color(STEEL)
    tidy(ax)
    title(ax, "Grouped bars")
    return fig


@figure("conditioning-dots")
def conditioning_dots():
    """A Cleveland dot plot: same numbers, a fifth of the ink."""
    beds, chi, sub = _median_price_grid()
    fig, ax = new_fig()
    ys = np.arange(len(beds))[::-1]
    for y, c, s in zip(ys, chi, sub):
        ax.plot([c, s], [y, y], color=BORDER, linewidth=2, zorder=2)
    ax.scatter(chi, ys, s=110, color=ORANGE, zorder=3, label="Chicago")
    ax.scatter(sub, ys, s=110, color=STEEL, zorder=3, label="Suburban Cook")
    ax.set_yticks(ys)
    ax.set_yticklabels([f"{b} bd" for b in beds])
    ax.set_xlabel("Median sale price (thousands)")
    ax.set_ylim(-0.6, len(beds) - 0.4)
    leg = ax.legend(frameon=False, fontsize=12, loc="upper right")
    for t in leg.get_texts():
        t.set_color(STEEL)
    tidy(ax, grid="x")
    title(ax, "Cleveland dot plot")
    return fig


@figure("conditioning-lines")
def conditioning_lines():
    """Connect the dots and the widening gap becomes the shape of the chart."""
    beds, chi, sub = _median_price_grid()
    fig, ax = new_fig()
    xs = np.arange(len(beds))
    ax.fill_between(xs, sub, chi, color=ORANGE, alpha=0.10, zorder=2)
    ax.plot(xs, chi, color=ORANGE, linewidth=3, marker="o", markersize=9, zorder=3)
    ax.plot(xs, sub, color=STEEL, linewidth=3, marker="o", markersize=9, zorder=3)
    ax.annotate("Chicago", xy=(xs[-1], chi[-1]), xytext=(10, 0),
                textcoords="offset points", color=ORANGE, fontsize=14, va="center")
    ax.annotate("Suburban Cook", xy=(xs[-1], sub[-1]), xytext=(10, 0),
                textcoords="offset points", color=STEEL, fontsize=14, va="center")
    gap = sub[-1] - chi[-1]
    ax.annotate(f"${gap:,.0f}k gap at 5+ bedrooms",
                xy=(xs[-1] - 0.06, (chi[-1] + sub[-1]) / 2),
                xytext=(-16, -26), textcoords="offset points", ha="right",
                color=INK, fontsize=13, va="center",
                arrowprops=dict(arrowstyle="-", color=QUIET, linewidth=1.2))
    ax.set_xticks(xs)
    ax.set_xticklabels(beds)
    ax.set_xlim(-0.3, len(beds) - 0.02)
    ax.set_xlabel("Bedrooms")
    ax.set_ylabel("Median sale price (thousands)")
    tidy(ax)
    title(ax, "Lines: the comparison becomes the shape")
    return fig


# --------------------------------------------------------------------------
# Context
# --------------------------------------------------------------------------

def _rail_series():
    a = annual_boardings().filter(pl.col("year") >= 1999)
    return a["year"].to_numpy(), a["rail"].to_numpy() / 1e6


@figure("context-bare")
def context_bare():
    """A correct chart that tells you nothing you did not already bring."""
    yrs, rail = _rail_series()
    fig, ax = new_fig()
    ax.plot(yrs, rail, color=ORANGE, linewidth=2.6, zorder=3)
    tidy(ax, grid=None)
    ax.tick_params(labelsize=11)
    return fig


@figure("context-annotated")
def context_annotated():
    """Same line. Units, a reference level, the two events, and a source."""
    yrs, rail = _rail_series()
    fig, ax = new_fig()
    peak_i = int(np.argmax(rail))
    ax.axhline(rail[0], color=BORDER, linewidth=1.4, linestyle=(0, (4, 4)), zorder=2)
    ax.annotate(f"1999 level ({rail[0]:.0f}M)", xy=(yrs[-1], rail[0]),
                xytext=(0, 7), textcoords="offset points", ha="right",
                color=MUTED, fontsize=11)
    ax.plot(yrs, rail, color=ORANGE, linewidth=2.6, zorder=3)
    ax.scatter([yrs[peak_i]], [rail[peak_i]], s=70, color=ORANGE_DARK, zorder=4)
    ax.annotate(f"Peak: {rail[peak_i]:.0f}M rides in {yrs[peak_i]}",
                xy=(yrs[peak_i], rail[peak_i]), xytext=(-8, 12),
                textcoords="offset points", ha="right", color=INK, fontsize=13)
    covid = int(np.where(yrs == 2020)[0][0])
    ax.scatter([2020], [rail[covid]], s=70, color=ORANGE_DARK, zorder=4)
    ax.annotate("2020: pandemic\nservice and demand collapse",
                xy=(2020, rail[covid]), xytext=(-14, -6), textcoords="offset points",
                ha="right", va="top", color=STEEL, fontsize=12, linespacing=1.35)
    ax.set_ylim(0, 260)
    ax.set_xlabel("Year")
    ax.set_ylabel("Rail boardings (millions)")
    tidy(ax)
    title(ax, "CTA rail boardings, 1999–2025", pad=16)
    fig.text(0.005, -0.02, "Data: CTA Annual Boarding Totals, Chicago Data Portal.",
             fontsize=10.5, color=MUTED, ha="left")
    return fig


# --------------------------------------------------------------------------
# Transformations
# --------------------------------------------------------------------------

@figure("skew-linear")
def skew_linear():
    """Right-skewed money data: the bulk is squashed into the first inch."""
    price = homes()["sale_price"].to_numpy() / 1000
    fig, ax = new_fig()
    ax.hist(price, bins=90, color=ORANGE, alpha=0.9, zorder=3)
    ax.set_xlabel("Sale price (thousands)")
    ax.set_ylabel("Sales")
    tidy(ax)
    title(ax, "Sale price, linear axis")
    ax.annotate("A long right tail nobody can read,\nand a spike nobody can resolve",
                xy=(0.42, 0.62), xycoords="axes fraction", color=STEEL,
                fontsize=13, linespacing=1.4)
    return fig


@figure("skew-log")
def skew_log():
    """The same column on a log axis: two modes and a floor become visible."""
    price = homes()["sale_price"].to_numpy() / 1000
    fig, ax = new_fig()
    bins = np.logspace(np.log10(price.min()), np.log10(price.max()), 90)
    ax.hist(price, bins=bins, color=ORANGE, alpha=0.9, zorder=3)
    ax.set_xscale("log")
    ax.set_xticks([10, 30, 100, 300, 1000, 3000])
    ax.set_xticklabels(["$10k", "$30k", "$100k", "$300k", "$1M", "$3M"])
    ax.minorticks_off()
    ax.set_xlabel("Sale price (log scale)")
    ax.set_ylabel("Sales")
    tidy(ax)
    title(ax, "Sale price, log axis")
    return fig


@figure("functional-relations")
def functional_relations():
    """The four shapes worth recognizing before you reach for a log."""
    fig, axes = plt.subplots(2, 2, figsize=(WIDTH_PX / DPI, HEIGHT_PX / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    x = np.linspace(-3, 3, 400)
    xp = np.linspace(0.05, 3, 400)
    panels = [
        ("$y = x$", [(x, x, ORANGE, None)]),
        ("$y = x^2$,  $y = x^3$", [(x, x**2, ORANGE, "$x^2$"), (x, x**3, STEEL, "$x^3$")]),
        ("$y = \\log(x)$", [(xp, np.log(xp), ORANGE, None)]),
        ("$y = e^{x}$", [(x, np.exp(x), ORANGE, None)]),
    ]
    for ax, (label, series) in zip(axes.ravel(), panels):
        ax.set_facecolor(PAPER)
        for xs, ys, color, lab in series:
            ax.plot(xs, ys, color=color, linewidth=2.4, label=lab, zorder=3)
        if any(lab for *_, lab in series):
            leg = ax.legend(frameon=False, fontsize=11, loc="upper left")
            for t in leg.get_texts():
                t.set_color(STEEL)
        ax.set_title(label, fontsize=14, color=INK, pad=6, loc="left")
        ax.axhline(0, color=BORDER, linewidth=1)
        ax.axvline(0, color=BORDER, linewidth=1)
        tidy(ax, grid=None, spines=())
        ax.tick_params(labelsize=10)
    fig.tight_layout()
    return fig


@figure("log-linearize")
def log_linearize():
    """A log on the y-axis turns exponential growth into a straight line."""
    fig, axes = plt.subplots(1, 2, figsize=(WIDTH_PX / DPI, 400 / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    x = np.linspace(0, 6, 60)
    y = 3 * 2.0**x
    for ax, logy in zip(axes, (False, True)):
        ax.set_facecolor(PAPER)
        ax.plot(x, y, color=ORANGE, linewidth=2.6, zorder=3)
        if logy:
            ax.set_yscale("log")
            ax.set_ylabel("$\\log(y)$")
            ax.set_title("log y: a straight line", fontsize=14, color=INK,
                         pad=8, loc="left")
        else:
            ax.set_ylabel("$y$")
            ax.set_title("Linear y: a hockey stick", fontsize=14, color=INK,
                         pad=8, loc="left")
        ax.set_xlabel("$x$")
        tidy(ax)
    fig.tight_layout()
    return fig


# Semi-major axis (AU) and orbital period (days), as printed on the source
# slide; the modern IAU values agree to the digits shown.
KEPLER = {
    "Mercury": (0.389, 87.77), "Venus": (0.724, 224.70), "Earth": (1.0, 365.25),
    "Mars": (1.524, 686.95), "Jupiter": (5.2, 4332.62), "Saturn": (9.510, 10759.2),
}


def _kepler_arrays():
    names = list(KEPLER)
    a = np.array([KEPLER[n][0] for n in names])
    p = np.array([KEPLER[n][1] for n in names])
    return names, a, p


@figure("kepler-linear")
def kepler_linear():
    """Six planets, linear axes: obviously curved, otherwise unreadable."""
    names, a, p = _kepler_arrays()
    fig, ax = new_fig()
    ax.scatter(a, p, s=95, color=ORANGE, zorder=3)
    for n, x, y in zip(names, a, p):
        ax.annotate(n, xy=(x, y), xytext=(9, -4), textcoords="offset points",
                    color=STEEL, fontsize=12)
    ax.set_xlabel("Mean distance to the Sun (AU)")
    ax.set_ylabel("Orbital period (days)")
    ax.set_xlim(0, 11)
    tidy(ax)
    title(ax, "Linear axes")
    return fig


@figure("kepler-loglog")
def kepler_loglog():
    """Log-log: a power law becomes a line, and its slope is the exponent."""
    names, a, p = _kepler_arrays()
    la, lp = np.log10(a), np.log10(p)
    slope, intercept = np.polyfit(la, lp, 1)
    fig, ax = new_fig()
    grid = np.linspace(la.min() - 0.15, la.max() + 0.15, 50)
    ax.plot(grid, slope * grid + intercept, color=QUIET, linewidth=1.8,
            linestyle=(0, (5, 4)), zorder=2)
    ax.scatter(la, lp, s=95, color=ORANGE, zorder=3)
    for n, x, y in zip(names, la, lp):
        ax.annotate(n, xy=(x, y), xytext=(9, -4), textcoords="offset points",
                    color=STEEL, fontsize=12)
    ax.annotate(f"slope = {slope:.2f}  ≈  3/2", xy=(0.05, 0.86),
                xycoords="axes fraction", color=INK, fontsize=15)
    ax.annotate("$P^2 \\propto a^3$", xy=(0.05, 0.75), xycoords="axes fraction",
                color=ORANGE_DARK, fontsize=17)
    ax.set_xlabel("log$_{10}$ mean distance (AU)")
    ax.set_ylabel("log$_{10}$ period (days)")
    tidy(ax)
    title(ax, "Log-log axes")
    return fig


# --------------------------------------------------------------------------
# Perception — colour
# --------------------------------------------------------------------------

# Okabe & Ito's eight-colour qualitative palette (2008), designed to stay
# distinguishable under the common colour-vision deficiencies.
OKABE_ITO = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
             "#0072B2", "#D55E00", "#CC79A7", "#000000"]


def _hex_to_rgb(h):
    h = h.lstrip("#")
    return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], dtype=float) / 255


def _rgb_to_hex(rgb):
    v = np.clip(rgb, 0, 1) * 255
    return "#" + "".join(f"{int(round(c)):02X}" for c in v)


def simulate_deuteranopia(hex_color: str) -> str:
    """Viénot–Brettel–Mollon (1999) deuteranope simulation, done in linear RGB.

    Used to *check* a palette, never to design one: the point of the slide is
    that a chart should survive this transform, not that this transform is what
    anyone actually sees.
    """
    srgb = _hex_to_rgb(hex_color)
    lin = np.where(srgb <= 0.04045, srgb / 12.92, ((srgb + 0.055) / 1.055) ** 2.4)
    to_lms = np.array([[17.8824, 43.5161, 4.11935],
                       [3.45565, 27.1554, 3.86714],
                       [0.0299566, 0.184309, 1.46709]])
    deut = np.array([[1.0, 0.0, 0.0],
                     [0.494207, 0.0, 1.24827],
                     [0.0, 0.0, 1.0]])
    out = np.linalg.inv(to_lms) @ (deut @ (to_lms @ lin))
    out = np.clip(out, 0, 1)
    srgb_out = np.where(out <= 0.0031308, out * 12.92, 1.055 * out ** (1 / 2.4) - 0.055)
    return _rgb_to_hex(srgb_out)


def _swatch_row(ax, colors, y, label, *, h=0.62):
    for i, c in enumerate(colors):
        ax.add_patch(plt.Rectangle((i, y), 0.96, h, facecolor=c,
                                   edgecolor=PAPER, linewidth=1.2))
    ax.text(-0.35, y + h / 2, label, ha="right", va="center",
            color=INK, fontsize=13)


@figure("color-schemes")
def color_schemes():
    """Three jobs, three kinds of scheme. Picking the wrong one is the bug."""
    fig, ax = new_fig(height=460)
    seq = [plt.get_cmap("YlOrBr")(v) for v in np.linspace(0.15, 0.92, 8)]
    div = [plt.get_cmap("RdBu_r")(v) for v in np.linspace(0.02, 0.98, 8)]
    _swatch_row(ax, OKABE_ITO, 2.0, "Categorical\n(no order)")
    _swatch_row(ax, seq, 1.0, "Sequential\n(low to high)")
    _swatch_row(ax, div, 0.0, "Diverging\n(two ends, a middle)")
    for y, note in ((2.0, "Maximally distinct hues; nothing implies rank."),
                    (1.0, "One hue, lightness carries the value."),
                    (0.0, "Light at the midpoint; both extremes emphasized.")):
        ax.text(0, y - 0.20, note, color=MUTED, fontsize=11.5, va="top")
    ax.set_xlim(-3.4, 8.2)
    ax.set_ylim(-0.55, 2.85)
    ax.axis("off")
    return fig


@figure("colormap-luminance")
def colormap_luminance():
    """Why viridis: the ramp's lightness has to climb, and jet's does not."""
    fig, axes = plt.subplots(2, 1, figsize=(WIDTH_PX / DPI, 430 / DPI), dpi=DPI,
                             gridspec_kw=dict(height_ratios=[1, 1.5], hspace=0.55))
    fig.patch.set_facecolor(PAPER)
    grad = np.linspace(0, 1, 256).reshape(1, -1)
    top = axes[0]
    top.set_facecolor(PAPER)
    top.imshow(grad, aspect="auto", cmap="jet", extent=(0, 1, 1.05, 2.0))
    top.imshow(grad, aspect="auto", cmap="viridis", extent=(0, 1, 0, 0.95))
    top.text(-0.012, 1.52, "jet", ha="right", va="center", color=INK, fontsize=13)
    top.text(-0.012, 0.47, "viridis", ha="right", va="center", color=INK, fontsize=13)
    top.set_xlim(0, 1)
    top.set_ylim(0, 2.0)
    top.axis("off")

    bot = axes[1]
    bot.set_facecolor(PAPER)
    xs = np.linspace(0, 1, 256)
    for cmap_name, color, label in (("jet", STEEL, "jet"), ("viridis", ORANGE, "viridis")):
        rgb = plt.get_cmap(cmap_name)(xs)[:, :3]
        lum = 0.2126 * rgb[:, 0] + 0.7152 * rgb[:, 1] + 0.0722 * rgb[:, 2]
        bot.plot(xs, lum, color=color, linewidth=2.6, label=label, zorder=3)
    bot.set_xlabel("Position along the colormap")
    bot.set_ylabel("Perceived lightness")
    leg = bot.legend(frameon=False, fontsize=12, loc="upper left")
    for t in leg.get_texts():
        t.set_color(STEEL)
    tidy(bot)
    bot.set_yticklabels([])
    return fig


def _monthly_median_by_beds() -> tuple[np.ndarray, dict[str, np.ndarray]]:
    """Median monthly sale price in 2025 for 2-, 3- and 4-bedroom homes.

    Three real series of comparable magnitude, which is all the colour demos
    need: they are about how the lines are *coloured*, not about housing.
    """
    if "monthly" not in _cache:
        df = (homes()
              .with_columns(pl.col("sale_date").str.slice(5, 2).cast(pl.Int64).alias("month"))
              .filter(pl.col("bedrooms").is_between(2, 4))
              .group_by(["bedrooms", "month"])
              .agg(pl.col("sale_price").median().alias("p"))
              .sort("month"))
        months = np.arange(1, 13)
        series = {f"{b} bedrooms": np.array(
            [df.filter((pl.col("bedrooms") == b) & (pl.col("month") == mth))["p"].item() / 1000
             for mth in months]) for b in (2, 3, 4)}
        _cache["monthly"] = (months, series)
    return _cache["monthly"]


def _line_demo(ax, colors, *, linewidth=2.8, dashes=(None, None, None)):
    """A small multi-series line chart, drawn in whatever colours are handed in."""
    months, series = _monthly_median_by_beds()
    for (label, values), color, dash in zip(series.items(), colors, dashes):
        ax.plot(months, values, color=color, linewidth=linewidth, label=label,
                dashes=dash if dash else (None, None), zorder=3)
        # Labelled at the end of the line rather than in a legend: one less
        # hop for the reader, and it survives the colour-blindness simulation.
        ax.annotate(label, xy=(months[-1], values[-1]), xytext=(7, 0),
                    textcoords="offset points", color=color, fontsize=11,
                    va="center")
    ax.set_xticks([1, 4, 7, 10])
    ax.set_xticklabels(["Jan", "Apr", "Jul", "Oct"])
    ax.set_xlim(0.6, 16.8)
    ax.set_xlabel("2025")
    ax.set_ylabel("Median sale price ($k)")
    ax.set_ylim(150, 700)
    tidy(ax)


@figure("color-red-green")
def color_red_green():
    """The default temptation: three series separated by hue alone."""
    fig, axes = plt.subplots(1, 2, figsize=(WIDTH_PX / DPI, 400 / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    naive = ["#D62728", "#2CA02C", "#8C564B"]
    for ax, palette, sub in (
        (axes[0], naive, "As drawn"),
        (axes[1], [simulate_deuteranopia(c) for c in naive], "Deuteranope simulation"),
    ):
        ax.set_facecolor(PAPER)
        _line_demo(ax, palette)
        ax.set_title(sub, fontsize=14, color=INK, pad=8, loc="left")
    fig.tight_layout()
    return fig


@figure("color-redundant")
def color_redundant():
    """Okabe–Ito hues plus dash pattern: the chart survives the simulation."""
    fig, axes = plt.subplots(1, 2, figsize=(WIDTH_PX / DPI, 400 / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    safe = [OKABE_ITO[4], OKABE_ITO[5], OKABE_ITO[2]]
    dashes = [(None, None), (6, 3), (1.5, 2.5)]
    for ax, palette, sub in (
        (axes[0], safe, "As drawn"),
        (axes[1], [simulate_deuteranopia(c) for c in safe], "Deuteranope simulation"),
    ):
        ax.set_facecolor(PAPER)
        _line_demo(ax, palette, dashes=dashes)
        ax.set_title(sub, fontsize=14, color=INK, pad=8, loc="left")
    fig.tight_layout()
    return fig


@figure("color-saturation")
def color_saturation():
    """Same chart, same encoding, different loudness."""
    fig, axes = plt.subplots(1, 2, figsize=(WIDTH_PX / DPI, 400 / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    loud = ["#FF0000", "#00FF00", "#0000FF"]
    calm = [ORANGE, STEEL, "#7EA8B5"]
    for ax, palette, sub in ((axes[0], loud, "Fully saturated"),
                             (axes[1], calm, "Muted")):
        ax.set_facecolor(PAPER)
        _line_demo(ax, palette, linewidth=3.4)
        ax.set_title(sub, fontsize=14, color=INK, pad=8, loc="left")
    fig.tight_layout()
    return fig


# --------------------------------------------------------------------------
# Perception — length
# --------------------------------------------------------------------------

@figure("area-vs-length")
def area_vs_length():
    """Circles sized by area against the same numbers as positions on a scale."""
    df = entries_by_line()
    lines = df["line"].to_list()
    rides = df["rides"].to_numpy()

    fig, axes = plt.subplots(1, 2, figsize=(WIDTH_PX / DPI, 430 / DPI), dpi=DPI,
                             gridspec_kw=dict(width_ratios=[1.15, 1]))
    fig.patch.set_facecolor(PAPER)

    left = axes[0]
    left.set_facecolor(PAPER)
    radii = np.sqrt(rides / rides.max())          # area, not radius, holds the value
    x = 0.0
    centers = []
    for r in radii:
        x += r
        centers.append(x)
        x += r + 0.06
    for cx, r, line, v in zip(centers, radii, lines, rides):
        left.add_patch(Circle((cx, 0), r, facecolor=CTA[line], edgecolor=STEEL,
                              linewidth=0.9, alpha=0.95))
        left.text(cx, -1.16, line, ha="center", va="top", color=STEEL,
                  fontsize=10, rotation=90)
    left.set_xlim(-0.15, x + 0.1)
    left.set_ylim(-2.25, 1.15)
    left.set_aspect("equal")
    left.axis("off")
    left.set_title("Encoded as area", fontsize=14, color=INK, pad=8, loc="left")

    right = axes[1]
    right.set_facecolor(PAPER)
    ys = np.arange(len(lines))[::-1]
    right.hlines(ys, 0, rides / 1000, color=BORDER, linewidth=1.4, zorder=2)
    right.scatter(rides / 1000, ys, s=90,
                  color=[CTA[line] for line in lines], zorder=3)
    right.set_yticks(ys)
    right.set_yticklabels(lines)
    right.set_xlabel("Median weekday entries (thousands)")
    tidy(right, grid="x")
    right.set_title("Encoded as position", fontsize=14, color=INK, pad=8, loc="left")
    fig.tight_layout()
    return fig


def _modes():
    a = annual_boardings()
    return (a["year"].to_numpy(),
            a["bus"].to_numpy() / 1e6,
            a["rail"].to_numpy() / 1e6,
            a["paratransit"].to_numpy() / 1e6)


@figure("stacked-area")
def stacked_area():
    """Stacked: only the bottom band sits on a flat baseline."""
    yrs, bus, rail, para = _modes()
    fig, ax = new_fig()
    ax.stackplot(yrs, bus, rail, para,
                 labels=["Bus", "Rail", "Paratransit"],
                 colors=["#B9BDBF", CTA["Blue"], ORANGE], edgecolor=PAPER,
                 linewidth=0.8, zorder=3)
    ax.set_xlabel("Year")
    ax.set_ylabel("Boardings (millions)")
    leg = ax.legend(frameon=False, fontsize=12, loc="upper right")
    for t in leg.get_texts():
        t.set_color(STEEL)
    tidy(ax)
    title(ax, "Stacked areas")
    return fig


@figure("unstacked-lines")
def unstacked_lines():
    """Unstacked: each series gets its own baseline, and paratransit vanishes."""
    yrs, bus, rail, para = _modes()
    fig, ax = new_fig()
    for series, color, label in ((bus, "#8E9295", "Bus"), (rail, CTA["Blue"], "Rail"),
                                 (para, ORANGE, "Paratransit")):
        ax.plot(yrs, series, color=color, linewidth=2.6, label=label, zorder=3)
    ax.set_xlabel("Year")
    ax.set_ylabel("Boardings (millions)")
    leg = ax.legend(frameon=False, fontsize=12, loc="upper right")
    for t in leg.get_texts():
        t.set_color(STEEL)
    tidy(ax)
    title(ax, "Unstacked lines, linear scale")
    ax.annotate("Paratransit is here, flat against zero",
                xy=(2000, 6), xytext=(0, 22), textcoords="offset points",
                color=ORANGE_DARK, fontsize=12,
                arrowprops=dict(arrowstyle="-", color=ORANGE_DARK, linewidth=1.1))
    return fig


@figure("log-lines")
def log_lines():
    """A log axis buys back the small series without hiding the big ones."""
    yrs, bus, rail, para = _modes()
    fig, ax = new_fig()
    for series, color, label in ((bus, "#8E9295", "Bus"), (rail, CTA["Blue"], "Rail"),
                                 (para, ORANGE, "Paratransit")):
        ax.plot(yrs, series, color=color, linewidth=2.6, label=label, zorder=3)
    ax.set_yscale("log")
    ax.set_yticks([1, 10, 100, 1000])
    ax.set_yticklabels(["1M", "10M", "100M", "1B"])
    ax.set_ylim(0.5, 1500)
    ax.minorticks_off()
    ax.annotate("Paratransit transfers to Pace in 2006;\nthe series is zero after that, and a\nlog axis has nowhere to draw a zero.",
                xy=(2006.5, 1.2), xytext=(6, 34), textcoords="offset points",
                color=ORANGE_DARK, fontsize=11.5, linespacing=1.35,
                arrowprops=dict(arrowstyle="-", color=ORANGE_DARK, linewidth=1.1))
    ax.set_xlabel("Year")
    ax.set_ylabel("Boardings (log scale)")
    leg = ax.legend(frameon=False, fontsize=12, loc="upper right")
    for t in leg.get_texts():
        t.set_color(STEEL)
    tidy(ax)
    title(ax, "Unstacked lines, log scale")
    return fig


# --------------------------------------------------------------------------
# Causality
# --------------------------------------------------------------------------

@figure("spurious-random-walks")
def spurious_random_walks():
    """Two series with nothing between them, drawn the way a scare chart is.

    Both are random walks from `numpy`; the seed was chosen to give a high
    correlation, which is the whole point — in trending series a coefficient
    near 1 is cheap, and dual axes will always let two lines be made to touch.
    """
    rng = np.random.default_rng(78)
    n = 26
    yrs = np.arange(1998, 1998 + n)
    a = np.cumsum(rng.normal(0.8, 1.0, n)) + 40
    b = np.cumsum(rng.normal(0.7, 1.0, n)) * 3.1 + 980
    r = float(np.corrcoef(a, b)[0, 1])

    fig, ax = new_fig()
    ax.plot(yrs, a, color=ORANGE, linewidth=3, marker="o", markersize=5, zorder=3)
    ax.set_ylabel("Series A (arbitrary units)", color=ORANGE)
    ax.tick_params(axis="y", colors=ORANGE)

    ax2 = ax.twinx()
    ax2.plot(yrs, b, color=STEEL, linewidth=3, marker="s", markersize=5, zorder=3)
    ax2.set_ylabel("Series B (arbitrary units)", color=STEEL, rotation=270,
                   labelpad=18)
    ax2.tick_params(axis="y", colors=STEEL, labelsize=11, length=0)
    for side in ("top", "left", "bottom"):
        ax2.spines[side].set_visible(False)
    ax2.spines["right"].set_color(BORDER)

    ax.annotate(f"r = {r:.2f}", xy=(0.03, 0.90), xycoords="axes fraction",
                color=INK, fontsize=20)
    ax.annotate("Both series are random walks from a\nrandom number generator. Neither one\n"
                "has anything to do with the other.",
                xy=(0.42, 0.22), xycoords="axes fraction", color=STEEL,
                fontsize=13, linespacing=1.4, va="top")
    ax.set_xlabel("Year")
    tidy(ax, grid=None, spines=("left", "bottom"))
    return fig


# --------------------------------------------------------------------------
# Large N — overplotting
# --------------------------------------------------------------------------

def _sqft_price():
    df = homes().filter((pl.col("building_sqft") < 6000)
                        & (pl.col("sale_price") < 2_000_000))
    return (df["building_sqft"].to_numpy().astype(float),
            df["sale_price"].to_numpy().astype(float) / 1000)


def _price_axes(ax):
    ax.set_xlabel("Building square footage")
    ax.set_ylabel("Sale price (thousands)")
    ax.set_xlim(0, 6000)
    ax.set_ylim(0, 2000)
    tidy(ax)


@figure("overplot-solid")
def overplot_solid():
    """Every point at full opacity: a silhouette, not a distribution."""
    x, y = _sqft_price()
    fig, ax = new_fig()
    ax.scatter(x, y, s=9, color=INK, zorder=3)
    _price_axes(ax)
    title(ax, f"{len(x):,} sales, one opaque dot each")
    return fig


@figure("overplot-alpha")
def overplot_alpha():
    """Transparency turns overlap back into a readable density."""
    x, y = _sqft_price()
    fig, ax = new_fig()
    ax.scatter(x, y, s=6, color=ORANGE, alpha=0.06, linewidths=0, zorder=3)
    _price_axes(ax)
    title(ax, "The same points at 6% opacity")
    return fig


@figure("overplot-hexbin")
def overplot_hexbin():
    """Bin the plane and colour by count: a two-dimensional histogram."""
    x, y = _sqft_price()
    fig, ax = new_fig()
    hb = ax.hexbin(x, y, gridsize=48, cmap="YlOrBr", bins="log",
                   extent=(0, 6000, 0, 2000), mincnt=1, linewidths=0)
    cb = fig.colorbar(hb, ax=ax, pad=0.015)
    cb.outline.set_visible(False)
    cb.set_label("Sales per cell (log)", color=STEEL, fontsize=12)
    cb.ax.tick_params(colors=STEEL, labelsize=10, length=0)
    _price_axes(ax)
    title(ax, "Hex-binned counts")
    return fig


def _bin_means(x, y, edges, min_n=3):
    idx = np.digitize(x, edges) - 1
    centers, means = [], []
    for k in range(len(edges) - 1):
        sel = idx == k
        if sel.sum() >= min_n:
            centers.append((edges[k] + edges[k + 1]) / 2)
            means.append(y[sel].mean())
    return np.array(centers), np.array(means)


def _kernel_smooth(x, y, grid, h):
    """Nadaraya–Watson: a weighted average of y, weights from a Gaussian kernel."""
    out = np.empty_like(grid, dtype=float)
    for i, g in enumerate(grid):
        w = np.exp(-0.5 * ((x - g) / h) ** 2)
        out[i] = np.sum(w * y) / np.sum(w)
    return out


@figure("overplot-smooth")
def overplot_smooth():
    """A local average through the cloud: the conditional centre of y given x."""
    x, y = _sqft_price()
    grid = np.linspace(600, 5200, 220)
    fig, ax = new_fig()
    ax.scatter(x, y, s=6, color=QUIET, alpha=0.06, linewidths=0, zorder=2)
    ax.plot(grid, _kernel_smooth(x, y, grid, 180), color=ORANGE, linewidth=3.4,
            zorder=4)
    _price_axes(ax)
    title(ax, "Same cloud, with a local (kernel) average")
    return fig


@figure("smoothing-conditioned")
def smoothing_conditioned():
    """One curve per bedroom count: smoothing and conditioning, together."""
    df = (_bedroom_frame()
          .filter((pl.col("building_sqft") < 5000) & (pl.col("sale_price") < 2_000_000)))
    fig, ax = new_fig()
    palette = {"2": "#C9CCCE", "3": "#8E9295", "4": ORANGE_DARK, "5+": ORANGE}
    for beds in ("2", "3", "4", "5+"):
        sub = df.filter(pl.col("beds") == beds)
        x = sub["building_sqft"].to_numpy().astype(float)
        y = sub["sale_price"].to_numpy().astype(float) / 1000
        lo, hi = np.percentile(x, [4, 96])
        grid = np.linspace(lo, hi, 160)
        ax.plot(grid, _kernel_smooth(x, y, grid, 170), color=palette[beds],
                linewidth=3, zorder=3)
        ax.annotate(f"{beds} bd", xy=(grid[-1], _kernel_smooth(x, y, grid[-1:], 170)[0]),
                    xytext=(7, 0), textcoords="offset points", color=palette[beds],
                    fontsize=12, va="center")
    ax.set_xlim(0, 5600)
    ax.set_ylim(0, 1400)
    ax.set_xlabel("Building square footage")
    ax.set_ylabel("Local average sale price (thousands)")
    tidy(ax)
    title(ax, "One smooth curve per bedroom count")
    return fig


# --------------------------------------------------------------------------
# Smoothing detour — KDE, built one kernel at a time
#
# Three points, chosen so each step of the construction is countable by eye.
# --------------------------------------------------------------------------

KDE_POINTS = np.array([2.0, 3.0, 5.0])
KDE_H = 0.75


def _gauss(grid, mu, h):
    return np.exp(-0.5 * ((grid - mu) / h) ** 2) / (h * np.sqrt(2 * np.pi))


def _kde_axes(ax):
    ax.set_xlim(-0.4, 8.4)
    ax.set_ylim(0, 0.42)
    ax.set_xticks(range(0, 9, 2))
    ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4])
    tidy(ax)
    for p in KDE_POINTS:
        ax.plot([p, p], [0, 0.014], color=INK, linewidth=2.4, zorder=5)


def _kde_fig(*, kernels=0, total=False, h=KDE_H, note=None, heading=""):
    grid = np.linspace(-1, 9, 600)
    fig, ax = new_fig(height=430)
    for p in KDE_POINTS[:kernels]:
        ax.plot(grid, _gauss(grid, p, h) / 3, color=QUIET, linewidth=2, zorder=3)
    if total:
        ax.plot(grid, sum(_gauss(grid, p, h) for p in KDE_POINTS) / 3,
                color=ORANGE, linewidth=3.2, zorder=4)
    _kde_axes(ax)
    if note:
        ax.annotate(note, xy=(0.03, 0.93), xycoords="axes fraction", color=STEEL,
                    fontsize=13, va="top", linespacing=1.4)
    title(ax, heading)
    return fig


@figure("kde-1-points")
def kde_1_points():
    """Three observations, drawn as a rug. Nothing has been estimated yet."""
    return _kde_fig(heading="Three data points")


@figure("kde-2-one-kernel")
def kde_2_one_kernel():
    """One point becomes a small hill of area 1/3."""
    return _kde_fig(kernels=1, heading="Put a Gaussian kernel on the first point",
                    note="Area under each kernel: 1/3")


@figure("kde-3-kernels")
def kde_3_kernels():
    """One hill per observation; the areas still sum to one."""
    return _kde_fig(kernels=3, heading="One kernel per observation",
                    note="Three kernels, 1/3 of the area each")


@figure("kde-4-sum")
def kde_4_sum():
    """Add the hills and the density estimate is the sum."""
    return _kde_fig(kernels=3, total=True, heading="Sum the kernels: the density curve")


@figure("kde-bandwidth")
def kde_bandwidth():
    """The bandwidth is the whole decision: same points, three answers."""
    grid = np.linspace(-1, 9, 600)
    fig, axes = plt.subplots(1, 3, figsize=(WIDTH_PX / DPI, 340 / DPI), dpi=DPI,
                             sharey=True)
    fig.patch.set_facecolor(PAPER)
    for ax, h, label in zip(axes, (0.25, 0.75, 2.0),
                            ("h = 0.25 (undersmoothed)", "h = 0.75",
                             "h = 2.0 (oversmoothed)")):
        ax.set_facecolor(PAPER)
        ax.plot(grid, sum(_gauss(grid, p, h) for p in KDE_POINTS) / 3,
                color=ORANGE, linewidth=2.8, zorder=4)
        _kde_axes(ax)
        ax.set_ylim(0, 0.62)
        ax.set_title(label, fontsize=13, color=INK, pad=8, loc="left")
        ax.tick_params(labelsize=10)
    fig.tight_layout()
    return fig


# --------------------------------------------------------------------------
# Smoothing a scatter plot, one step at a time
# --------------------------------------------------------------------------

def _smooth_demo_data():
    rng = np.random.default_rng(418)
    x = np.sort(rng.uniform(1, 21, 46))
    y = 4 + 0.75 * x - 0.014 * x**2 + rng.normal(0, 1.5, len(x))
    return x, y


SMOOTH_BINS = np.arange(1, 22, 4.0)


def _smooth_axes(ax):
    ax.set_xlim(0, 22)
    ax.set_ylim(0, 20)
    tidy(ax)


def _smooth_fig(*, window=None, bins=False, bin_means=False, curve=False,
                kernel=None, heading="", note=None):
    x, y = _smooth_demo_data()
    fig, ax = new_fig(height=430)
    if bins:
        for edge in SMOOTH_BINS:
            ax.axvline(edge, color=BORDER, linewidth=1.2, linestyle=(0, (4, 4)),
                       zorder=1)
    if window is not None:
        lo, hi = window
        ax.axvspan(lo, hi, color=SOFT_GRAY, zorder=0)
        inside = (x >= lo) & (x <= hi)
    else:
        inside = np.zeros_like(x, dtype=bool)
    ax.scatter(x[~inside], y[~inside], s=34, color=QUIET, zorder=3)
    ax.scatter(x[inside], y[inside], s=44, color=ORANGE, zorder=4)
    if window is not None and inside.any():
        ax.plot([(window[0] + window[1]) / 2], [y[inside].mean()], marker="^",
                markersize=13, color=INK, zorder=6)
    if bin_means or curve:
        cx, cy = _bin_means(x, y, SMOOTH_BINS)
        if curve:
            ax.plot(cx, cy, color=INK, linewidth=2.2, zorder=5)
        ax.plot(cx, cy, marker="^", markersize=13, linestyle="none", color=INK,
                zorder=6)
    if kernel is not None:
        grid = np.linspace(x.min(), x.max(), 260)
        ax.plot(grid, _kernel_smooth(x, y, grid, kernel), color=ORANGE,
                linewidth=3.2, zorder=5)
    _smooth_axes(ax)
    if note:
        ax.annotate(note, xy=(0.03, 0.94), xycoords="axes fraction", color=STEEL,
                    fontsize=13, va="top", linespacing=1.4)
    title(ax, heading)
    return fig


@figure("smooth-1-scatter")
def smooth_1_scatter():
    """The starting point: y against x, no summary yet."""
    return _smooth_fig(heading="Smooth the y-values as a function of x")


@figure("smooth-2-window")
def smooth_2_window():
    """One window, one average: the first point of the curve."""
    return _smooth_fig(window=(5.0, 9.0),
                       heading="For one x, average the y's of its neighbours",
                       note="The triangle is the mean of the highlighted points")


@figure("smooth-3-bin-means")
def smooth_3_bin_means():
    """Repeat for every bin."""
    return _smooth_fig(bins=True, bin_means=True,
                       heading="Bin all of x, average y within each bin")


@figure("smooth-4-curve")
def smooth_4_curve():
    """Connect the bin means and a shape appears."""
    return _smooth_fig(bins=True, curve=True,
                       heading="These averages sketch out a curve")


@figure("smooth-5-kernel")
def smooth_5_kernel():
    """Weights from a kernel instead of hard bin edges: no more corners."""
    return _smooth_fig(kernel=1.6,
                       heading="Kernel weights instead of hard bins",
                       note="Points far from x contribute almost nothing")


@figure("smooth-6-bandwidth")
def smooth_6_bandwidth():
    """The same trade-off as the KDE, on the same picture."""
    x, y = _smooth_demo_data()
    grid = np.linspace(x.min(), x.max(), 260)
    fig, ax = new_fig(height=430)
    ax.scatter(x, y, s=34, color=QUIET, zorder=3)
    for h, color, label in ((0.6, STEEL, "h = 0.6"), (1.6, ORANGE, "h = 1.6"),
                            (6.0, INK, "h = 6.0")):
        ax.plot(grid, _kernel_smooth(x, y, grid, h), color=color, linewidth=2.8,
                zorder=5, label=label)
    leg = ax.legend(frameon=False, fontsize=12, loc="lower right")
    for t in leg.get_texts():
        t.set_color(STEEL)
    _smooth_axes(ax)
    title(ax, "Bandwidth is the knob")
    return fig



# --------------------------------------------------------------------------
# Line graphs and time series
#
# A time series is the one case where connecting the dots is not decoration:
# the gaps between successive x values are real and ordered, so the segment
# between two points is itself a claim about what happened in between.
# --------------------------------------------------------------------------

@figure("time-series-line")
def time_series_line():
    """The same yearly totals as points, then as a line.

    Stacked rather than side by side: the two panels share one x-axis, so
    reading down the column puts each year's dot directly above its segment.
    """
    a = annual_boardings().filter(pl.col("year") >= 1999)
    yrs = a["year"].to_numpy()
    rail = a["rail"].to_numpy() / 1e6
    fig, axes = new_fig(width=560, height=620, nrows=2, sharex=True, sharey=True)
    for ax, connect, heading in zip(axes, (False, True),
                                    ("Points only", "Points connected in time order")):
        ax.scatter(yrs, rail, s=26, color=QUIET if connect else ORANGE, zorder=3)
        if connect:
            ax.plot(yrs, rail, color=ORANGE, linewidth=2.6, zorder=4)
        ax.set_xticks([2000, 2010, 2020])
        ax.set_ylabel("Rail boardings (millions)")
        tidy(ax)
        title(ax, heading, size=14)
    axes[0].set_ylim(0, 260)
    axes[1].set_xlabel("Year")
    fig.subplots_adjust(hspace=0.28)
    fig.text(0.005, -0.02, "Data: CTA Annual Boarding Totals, Chicago Data Portal.",
             fontsize=10.5, color=MUTED, ha="left")
    return fig


# --------------------------------------------------------------------------
# Reading a histogram by area
#
# Straight out of *Computational and Inferential Thinking* 7.2: with unequal
# bins the density scale is not a nicety, it is the difference between a
# histogram and a picture that misreports the data. Same sale prices, same
# uneven bins, two vertical axes.
# --------------------------------------------------------------------------

# Four $100k bins and one $500k bin at the top, where the sales thin out. The
# wide bin holds the most sales of any bin and is still nearly the shortest
# bar on the density scale -- which is the whole point.
UNEVEN_BINS = np.array([0, 100, 200, 300, 400, 900], dtype=float)  # $1,000s


def _uneven_hist():
    price = homes().filter(pl.col("sale_price") < 900_000)["sale_price"].to_numpy() / 1e3
    counts, _ = np.histogram(price, bins=UNEVEN_BINS)
    widths = np.diff(UNEVEN_BINS)
    percents = 100 * counts / counts.sum()
    return counts, widths, percents


def _uneven_axes(ax):
    ax.set_xlim(UNEVEN_BINS[0], UNEVEN_BINS[-1])
    ax.set_xticks(UNEVEN_BINS)
    ax.set_xticklabels([f"{int(b)}" for b in UNEVEN_BINS])
    ax.set_xlabel("Sale price ($1,000s)")
    tidy(ax)


@figure("histogram-area")
def histogram_area():
    """Density on top (a histogram), raw counts below (not one).

    Stacked so the two vertical scales sit over one shared set of bin edges:
    the bars are the same width in both panels and only their heights change.
    """
    counts, widths, percents = _uneven_hist()
    fig, axes = new_fig(width=560, height=620, nrows=2, sharex=True)

    # Height in "% per $10,000" rather than per dollar: same shape, readable ticks.
    axes[0].bar(UNEVEN_BINS[:-1], 10 * percents / widths, width=widths, align="edge",
                color=ORANGE, edgecolor=PAPER, linewidth=1.2, zorder=3)
    for left, w, pct in zip(UNEVEN_BINS[:-1], widths, percents):
        axes[0].annotate(f"{pct:.0f}%", xy=(left + w / 2, 10 * pct / w),
                         xytext=(0, 7), textcoords="offset points", ha="center",
                         color=INK, fontsize=11)
    axes[0].set_ylim(0, 2.9)
    axes[0].set_ylabel("% per $10,000")
    _uneven_axes(axes[0])
    title(axes[0], "Density scale: area is the percent", size=14)

    axes[1].bar(UNEVEN_BINS[:-1], counts, width=widths, align="edge",
                color=QUIET, edgecolor=PAPER, linewidth=1.2, zorder=3)
    axes[1].set_ylabel("Number of sales")
    axes[1].set_yticklabels([])
    _uneven_axes(axes[1])
    title(axes[1], "Counts: the wide bin takes over", size=14)

    axes[0].set_xlabel("")
    fig.subplots_adjust(hspace=0.3)
    fig.text(0.005, -0.02,
             "Data: Cook County single-family sales under $900k, 2025.",
             fontsize=10.5, color=MUTED, ha="left")
    return fig


# --------------------------------------------------------------------------
# Simpson's paradox — synthetic, three departments
#
# Salary rises with seniority inside every department, but senior people are
# concentrated in the departments that pay least, so the pooled cloud slopes
# the other way. The two figures share one dataset and one set of axes; only
# the grouping changes.
# --------------------------------------------------------------------------

# Every department pays the same premium per year of seniority (RAISE). What
# separates them is where they sit: the best-paid department is also the
# youngest, so the between-department drop (about -$37k per year of mean
# seniority) swamps the within-department rise and flips the pooled slope.
RAISE = 17_000

# (label, colour, mean seniority, mean salary)
DEPTS = [("Data science", "#522398", 2.0, 225_000),
         ("Product", "#00A1DE", 3.5, 165_000),
         ("HR", ORANGE, 4.8, 120_000)]


def _simpsons_data(seed=418):
    rng = np.random.default_rng(seed)
    rows = []
    for name, color, mu, pay_mean in DEPTS:
        # Resampled, not clipped: clipping stacks the tails into a visible
        # stripe at the limits, which reads as a real feature of the data.
        yrs = rng.normal(mu, 0.85, 320)
        while (bad := (yrs < 0.4) | (yrs > 7.0)).any():
            yrs[bad] = rng.normal(mu, 0.85, int(bad.sum()))
        pay = pay_mean + RAISE * (yrs - mu) + rng.normal(0, 20_000, 320)
        rows.append((name, color, yrs, pay))
    return rows


def _simpsons_axes(ax):
    ax.set_xlim(0, 7.2)
    ax.set_ylim(40_000, 300_000)
    ax.set_yticks(np.arange(50_000, 300_001, 50_000))
    ax.set_yticklabels([f"${v // 1000:.0f}k" for v in np.arange(50_000, 300_001, 50_000)])
    ax.set_xlabel("Years of seniority")
    ax.set_ylabel("Salary")
    tidy(ax)


def _fit_line(ax, x, y, color, lw=3.0):
    """Least-squares line over the span of x actually observed."""
    slope, intercept = np.polyfit(x, y, 1)
    span = np.array([x.min(), x.max()])
    ax.plot(span, intercept + slope * span, color=color, linewidth=lw, zorder=6)


@figure("simpsons-paradox-pooled")
def simpsons_paradox_pooled():
    """Everyone in one cloud: pay looks like it falls with seniority."""
    rows = _simpsons_data()
    x = np.concatenate([r[2] for r in rows])
    y = np.concatenate([r[3] for r in rows])
    fig, ax = new_fig(width=620, height=540)
    ax.scatter(x, y, s=9, color=QUIET, zorder=3)
    _fit_line(ax, x, y, INK)
    _simpsons_axes(ax)
    title(ax, "Pooled: salary falls with seniority")
    return fig


@figure("simpsons-paradox-split")
def simpsons_paradox_split():
    """Split by department and every line tilts the other way."""
    rows = _simpsons_data()
    fig, ax = new_fig(width=620, height=540)
    for name, color, xs, ys in rows:
        ax.scatter(xs, ys, s=9, color=color, alpha=0.55, zorder=3)
        _fit_line(ax, xs, ys, color)
        # Label at the left end of each fitted line, inside the frame, so the
        # three groups read without a legend and without widening the axes.
        ax.annotate(name, xy=(xs.min(), np.polyval(np.polyfit(xs, ys, 1), xs.min())),
                    xytext=(4, -8), textcoords="offset points", color=color,
                    fontsize=13, fontweight="bold", va="top",
                    path_effects=[pe.withStroke(linewidth=3.5, foreground=PAPER)])
    _simpsons_axes(ax)
    title(ax, "Within each department: salary rises")
    return fig


# --------------------------------------------------------------------------
# Geospatial — one row per station, placed where the station is
# --------------------------------------------------------------------------

def _station_points() -> pl.DataFrame:
    """2019 median weekday entries per 'L' station, with latitude and longitude."""
    if "stations" not in _cache:
        stops = pl.read_csv(
            DATASETS / "chicago-l-stations" / "CTA_List_of_'L'_Stops_20260527.csv"
        )
        coords = (
            stops.select("MAP_ID", "Location")
            .unique(subset="MAP_ID")
            .with_columns(
                pl.col("Location").str.extract(r"\(([-0-9.]+),", 1).cast(pl.Float64).alias("lat"),
                pl.col("Location").str.extract(r",\s*([-0-9.]+)\)", 1).cast(pl.Float64).alias("lon"),
                pl.col("MAP_ID").cast(pl.Int64).alias("station_id"),
            )
            .drop_nulls(["lat", "lon"])
        )
        daily = pl.read_csv(
            DATASETS / "cta-ridership" / "Station_Entries_-_Daily_Totals_20260527.csv",
            ignore_errors=True,
        ).with_columns(pl.col("rides").cast(pl.Utf8).str.replace_all(",", "").cast(pl.Int64))
        weekday = (
            daily.filter(pl.col("date").str.ends_with("2019") & (pl.col("daytype") == "W"))
            .group_by("station_id").agg(pl.col("rides").median().alias("rides"))
            .with_columns(pl.col("station_id").cast(pl.Int64))
        )
        _cache["stations"] = coords.join(weekday, on="station_id")
    return _cache["stations"]


def _city_outline(ax):
    """The city boundary, thinned, as a pale backdrop for the station dots."""
    import json
    geo = json.loads((DATASETS / "chicago-maps" / "chicago-city.geojson").read_text())
    for feat in geo["features"]:
        g = feat["geometry"]
        polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
        for poly in polys:
            ring = np.asarray(poly[0], dtype=float)[::4]
            ax.fill(ring[:, 0], ring[:, 1], facecolor=SOFT_GRAY,
                    edgecolor=BORDER, linewidth=1.0, zorder=1)


@figure("geospatial-stations")
def geospatial_stations():
    """Position carries the geography; area carries the ridership."""
    pts = _station_points()
    lon, lat = pts["lon"].to_numpy(), pts["lat"].to_numpy()
    rides = pts["rides"].to_numpy().astype(float)

    fig, ax = new_fig(width=620, height=780)
    _city_outline(ax)
    # Area proportional to ridership, per the area principle: a station with
    # twice the entries gets twice the ink, not twice the radius.
    ax.scatter(lon, lat, s=rides / 14, color=ORANGE, alpha=0.55,
               edgecolor=ORANGE_DARK, linewidth=0.5, zorder=3)

    for label, size in ((" 2,000", 2_000), (" 10,000", 10_000), (" 20,000", 20_000)):
        ax.scatter([], [], s=size / 14, color=ORANGE, alpha=0.55,
                   edgecolor=ORANGE_DARK, linewidth=0.5, label=label)
    leg = ax.legend(frameon=False, fontsize=11, loc="lower left",
                    labelspacing=1.5, borderpad=1.0, handletextpad=1.4,
                    title="Median weekday entries")
    leg.get_title().set_color(STEEL)
    leg.get_title().set_fontsize(11)
    for t in leg.get_texts():
        t.set_color(STEEL)

    ax.set_xlim(-87.95, -87.51)
    ax.set_ylim(41.63, 42.07)
    ax.set_aspect(1 / 0.745)  # Mercator correction at ~41.9 degrees north
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    title(ax, "Chicago 'L' stations, 2019")
    fig.text(0.005, 0.0, "Data: CTA station entries and stop list, Chicago Data Portal.",
             fontsize=10.5, color=MUTED, ha="left")
    return fig


# --------------------------------------------------------------------------
# Uncertainty — the same four estimates, with and without their error bars
# --------------------------------------------------------------------------

@figure("uncertainty-intervals")
def uncertainty_intervals():
    """A mean is a guess about a population; the interval says how good a guess.

    Drawn from a 40-sale sample of each group rather than all 22,000 rows.
    With the full county the intervals are narrower than the marker and the
    figure would argue the opposite of what it is here to argue: an estimate
    off a handful of sales is exactly where the uncertainty lives.
    """
    df = _bedroom_frame().filter(pl.col("sale_price") < 2_000_000)
    beds = ["2", "3", "4", "5+"]
    rng = np.random.default_rng(418)
    means, errs = [], []
    for b in beds:
        v = df.filter(pl.col("beds") == b)["sale_price"].to_numpy() / 1e3
        v = rng.choice(v, 40, replace=False)
        means.append(v.mean())
        errs.append(1.96 * v.std(ddof=1) / np.sqrt(len(v)))  # 95% interval
    means, errs = np.array(means), np.array(errs)

    xs = np.arange(len(beds))
    fig, axes = new_fig(height=380, ncols=2, sharey=True)

    axes[0].bar(xs, means, width=0.5, color=QUIET, zorder=3)
    title(axes[0], "Estimates alone", size=14)

    axes[1].errorbar(xs, means, yerr=errs, fmt="o", markersize=9, color=ORANGE,
                     ecolor=ORANGE, elinewidth=2.4, capsize=7, capthick=2.4, zorder=3)
    title(axes[1], "Estimates with 95% intervals", size=14)

    for ax in axes:
        ax.set_xticks(xs)
        ax.set_xticklabels(beds)
        ax.set_xlim(-0.6, len(beds) - 0.4)
        ax.set_xlabel("Bedrooms")
        tidy(ax)
    axes[0].set_ylim(0, (means + errs).max() * 1.2)
    axes[0].set_ylabel("Mean sale price ($1,000s)")
    fig.subplots_adjust(wspace=0.1)
    fig.text(0.005, -0.03,
             "Data: 40 sampled Cook County single-family sales per group, 2025.",
             fontsize=10.5, color=MUTED, ha="left")
    return fig


# Proportional ink — the bar's ink is its value, so the baseline is not a
# styling choice. Same four numbers, two baselines.
# --------------------------------------------------------------------------

@figure("proportional-ink")
def proportional_ink():
    """A truncated baseline multiplies the difference it draws.

    CTA rail boardings fell about 10% over these five years. From zero the
    bars say "roughly flat, drifting down"; from 210 million the same five
    numbers say "collapse", because the ink is no longer the quantity -- it is
    whatever is left above an arbitrary line.
    """
    a = annual_boardings().filter(pl.col("year").is_between(2015, 2019))
    yrs = a["year"].to_numpy()
    rail = a["rail"].to_numpy() / 1e6
    xs = np.arange(len(yrs))
    fig, axes = new_fig(height=380, ncols=2)

    for ax, base, color, heading in (
            (axes[0], 0.0, ORANGE, "From zero: ink is the quantity"),
            (axes[1], 210.0, QUIET, "From 210M: ink is a leftover")):
        ax.bar(xs, rail - base, bottom=base, width=0.6, color=color, zorder=3)
        ax.set_xticks(xs)
        ax.set_xticklabels([str(y) for y in yrs])
        ax.set_ylim(base, rail.max() * (1.05 if base == 0 else 1.005))
        ax.set_ylabel("Rail boardings (millions)")
        tidy(ax)
        title(ax, heading, size=14)

    fig.subplots_adjust(wspace=0.26)
    fig.text(0.005, -0.03, "Data: CTA Annual Boarding Totals, Chicago Data Portal.",
             fontsize=10.5, color=MUTED, ha="left")
    return fig


# Correlation matrix — every pair at once
# --------------------------------------------------------------------------

CORR_VARS = [("sale_price", "Price"), ("building_sqft", "Building sqft"),
             ("land_sqft", "Land sqft"), ("rooms", "Rooms"),
             ("full_baths", "Full baths"), ("year_built", "Year built"),
             ("miles_from_loop", "Miles from Loop")]

LOOP = (41.8827, -87.6233)  # State and Madison, the origin of Chicago's grid


def _with_distance(df: pl.DataFrame) -> pl.DataFrame:
    """Straight-line miles from the Loop. Flat-earth is fine over one county."""
    return df.drop_nulls(["latitude", "longitude"]).with_columns(
        (((pl.col("latitude") - LOOP[0]) * 69.0) ** 2
         + ((pl.col("longitude") - LOOP[1]) * 51.4) ** 2).sqrt().alias("miles_from_loop"))


def _corr_frame() -> tuple[np.ndarray, list[str]]:
    cols = [c for c, _ in CORR_VARS]
    df = (_with_distance(homes()).filter(pl.col("sale_price") < 2_000_000)
          .select(cols).drop_nulls())
    m = np.corrcoef(df.to_numpy().T)
    return m, [lab for _, lab in CORR_VARS]


@figure("correlation-matrix")
def correlation_matrix():
    """One number per pair, laid out so the eye can scan for the strong ones."""
    m, labels = _corr_frame()
    n = len(labels)
    fig, ax = new_fig(width=780, height=680)
    # Diverging ramp: white at zero, orange for positive, steel for negative,
    # because a correlation has two meaningful ends and a meaningful middle.
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        "corr", ["#2C5F6B", "#FFFFFF", ORANGE])
    ax.imshow(m, cmap=cmap, vmin=-1, vmax=1, zorder=2)
    for i in range(n):
        for j in range(n):
            ax.text(j, i, f"{m[i, j]:.2f}".replace("-", "−"),
                    ha="center", va="center", fontsize=12.5, zorder=3,
                    color=PAPER if abs(m[i, j]) > 0.6 else INK)
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(labels, rotation=30, ha="right")
    ax.set_yticklabels(labels)
    ax.tick_params(colors=STEEL, labelsize=12, length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    title(ax, "Cook County home sales, 2025")
    return fig


@figure("scatterplot-matrix")
def scatterplot_matrix():
    """The same pairs, drawn. Shape survives here and dies in the table."""
    cols = ["sale_price", "building_sqft", "land_sqft", "year_built"]
    labels = ["Price", "Building sqft", "Land sqft", "Year built"]
    df = (homes().select(cols).drop_nulls()
          .filter((pl.col("sale_price") < 1_200_000) & (pl.col("land_sqft") < 20_000))
          .sample(1400, seed=418))
    data = [df[c].to_numpy().astype(float) for c in cols]
    n = len(cols)
    fig, axes = new_fig(width=760, height=700, nrows=n, ncols=n)
    for i in range(n):
        for j in range(n):
            ax = axes[i][j]
            if i == j:
                ax.hist(data[i], bins=26, color=BORDER, zorder=3)
            else:
                ax.scatter(data[j], data[i], s=3, color=ORANGE, alpha=0.25, zorder=3)
            ax.set_xticks([])
            ax.set_yticks([])
            for s in ax.spines.values():
                s.set(color=BORDER, linewidth=0.8)
            if i == n - 1:
                ax.set_xlabel(labels[j], fontsize=11, color=STEEL)
            if j == 0:
                ax.set_ylabel(labels[i], fontsize=11, color=STEEL)
    fig.subplots_adjust(wspace=0.08, hspace=0.08)
    fig.suptitle("Cook County home sales, 2025", fontsize=17, color=INK,
                 x=0.09, ha="left")
    return fig

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
    print(f"writing {len(wanted)} figure(s) to {OUT_DIR.relative_to(REPO_ROOT)}")
    for name in wanted:
        save(FIGURES[name](), name)


if __name__ == "__main__":
    main(sys.argv[1:])
