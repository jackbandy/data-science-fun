#!/usr/bin/env python3
"""Sampling figures for the Week 7, Day 2 slides: sampling distributions, standard error, confidence intervals, sampling designs, and the big data paradox.

NOTICE: this file was substantially drafted by an LLM coding system and has not yet been reviewed. Check every figure against the slide it illustrates.

Follows docs/assets/STYLE.md and mirrors week8/make_week8_figures.py: golden-ratio canvases, grayscale neutrals with orange reserved for the focal element, horizontal y-axis labels, vendored Libre Franklin drawn as paths so each SVG is self-contained.

Data (see SOURCES.md in this folder):
  * home-population-sample, clt-panels, standard-error, and ci-coverage read datasets/cook-county-home-sales-2025/, filtered as in Week 8, and treat it as the population.
  * sampling-designs and big-data-paradox are simulated with a fixed seed.

Usage:  python3 make_sampling_figures.py [name ...]
        (docs/slides/.venv has every dependency: numpy, scipy, polars, matplotlib)
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
from scipy import stats

OUT_DIR = Path(__file__).resolve().parent
REPO_ROOT = OUT_DIR.parents[2]
DATASETS = REPO_ROOT / "datasets"
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
ORANGE_DARK = "#C83214"

PHI = (1 + 5**0.5) / 2
WIDTH_PX = 1000
DPI = 100
SEED = 418

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
    ax.tick_params(colors=STEEL, labelsize=12, length=0)
    for lbl in (ax.xaxis.label, ax.yaxis.label):
        lbl.set_color(STEEL)
        lbl.set_fontsize(14)
    return ax


def horizontal_ylabels(fig):
    """STYLE.md: y-axis labels run horizontally across the top of the axis, and any title moves up to clear them."""
    for ax in fig.axes:
        label = ax.yaxis.label
        # A label the figure already turned horizontal (e.g. row labels in a small-multiples grid) keeps its own placement.
        if not label.get_text().strip() or label.get_rotation() == 0 or ax.name != "rectilinear" or ax.get_label() == "<colorbar>":
            continue
        right = ax.yaxis.get_label_position() == "right"
        label.set(rotation=0, ha="right" if right else "left", va="bottom")
        ax.yaxis.set_label_coords(1 if right else 0, 1.025)
        pad = max(30, ax.titleOffsetTrans.get_matrix()[1, 2] * 72 / fig.dpi)
        for loc, title in (("left", ax._left_title), ("center", ax.title), ("right", ax._right_title)):
            if title.get_text():
                ax.set_title(title.get_text(), loc=loc, pad=pad, fontsize=title.get_fontsize(), color=title.get_color(), fontweight=title.get_fontweight())


def save(fig, name):
    out = OUT_DIR / f"{name}.svg"
    horizontal_ylabels(fig)
    fig.savefig(out, format="svg", facecolor=PAPER, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)
    print(f"  wrote {out.relative_to(REPO_ROOT)}")


def dollars(v, _=None):
    return f"${v / 1e6:g}M" if abs(v) >= 1e6 else f"${v / 1e3:,.0f}k"


_cache: dict[str, object] = {}


def home_prices() -> np.ndarray:
    """Cook County single-family sale prices, filtered the way Week 8 filters them, treated here as the population."""
    if "homes" not in _cache:
        df = pl.read_csv(DATASETS / "cook-county-home-sales-2025" / "cook-county-home-sales-2025.csv", ignore_errors=True)
        df = df.filter((pl.col("property_group") == "Single-Family") & (~pl.col("is_multisale")) & (pl.col("sale_price") > 10_000) & pl.col("building_sqft").is_not_null())
        _cache["homes"] = df["sale_price"].to_numpy().astype(float)
    return _cache["homes"]


@figure("home-population-sample")
def home_population_sample():
    """All single-family sale prices (the 'population') with one random sample of 50 drawn underneath."""
    y = home_prices()
    rng = np.random.default_rng(SEED)
    sample = rng.choice(y, 50, replace=False)
    fig, ax = new_fig()
    ax.hist(y, bins=np.arange(0, 2_000_001, 50_000), color=QUIET, zorder=3)
    top = ax.get_ylim()[1]
    ax.scatter(sample, np.full(len(sample), -top * 0.06), marker="|", s=250, color=ORANGE, zorder=4, clip_on=False)
    ax.axvline(y.mean(), color=INK, linewidth=1.5, zorder=4)
    ax.text(y.mean() + 20_000, top * 0.95, f"population mean μ = {dollars(y.mean())}", color=INK, fontsize=14, va="top")
    ax.text(sample.mean() - 20_000, top * 0.83, f"sample mean = {dollars(sample.mean())}", color=ORANGE_DARK, fontsize=14, va="top", ha="right")
    ax.axvline(sample.mean(), color=ORANGE, linewidth=1.5, linestyle=(0, (4, 3)), zorder=4)
    ax.text(1_950_000, top * 0.04, "orange ticks: one random sample of 50", color=ORANGE_DARK, fontsize=13, ha="right")
    ax.set(xlim=(0, 2_000_000), ylim=(-top * 0.12, top), xlabel=f"Sale price ({len(y):,} single-family sales, Cook County 2025; axis cut at $2M)", ylabel="Sales")
    ax.xaxis.set_major_formatter(dollars)
    tidy(ax)
    return fig


@figure("clt-panels")
def clt_panels():
    """The skewed population, then the sampling distribution of the mean for n = 5 and n = 50."""
    y = home_prices()
    rng = np.random.default_rng(SEED)
    panels = [("Population (one sale)", y, QUIET)]
    for n in (5, 50):
        means = rng.choice(y, size=(5000, n), replace=True).mean(axis=1)
        panels.append((f"Means of 5,000 samples, n = {n}", means, ORANGE))
    fig, axes = new_fig(height=640, nrows=3, sharex=True)
    bins = np.arange(0, 2_000_001, 25_000)
    for ax, (title, vals, color) in zip(axes, panels):
        ax.hist(vals, bins=bins, color=color, zorder=3)
        ax.axvline(y.mean(), color=INK, linewidth=1.2, zorder=4)
        ax.set_title(title, fontsize=15, color=INK, loc="left", pad=6)
        ax.set_yticks([])
        tidy(ax, grid=None, spines=("bottom",))
    axes[-1].set(xlim=(0, 2_000_000), xlabel="Sale price; the black line is the population mean")
    axes[-1].xaxis.set_major_formatter(dollars)
    fig.subplots_adjust(hspace=0.45)
    return fig


@figure("standard-error")
def standard_error():
    """Standard error of the sample mean, sigma / sqrt(n), for the home-price population."""
    sigma = home_prices().std()
    n = np.arange(4, 1001)
    fig, ax = new_fig()
    ax.plot(n, sigma / np.sqrt(n), color=ORANGE, linewidth=3, zorder=3)
    for m in (25, 100, 400):
        se = sigma / np.sqrt(m)
        ax.scatter([m], [se], color=INK, s=50, zorder=4)
        ax.text(m + 15, se + 6_000, f"n = {m}: ±{dollars(se)}", color=INK, fontsize=14)
    ax.set(xlim=(0, 1000), ylim=(0, sigma / 2), xlabel="Sample size n", ylabel="Standard error of the sample mean")
    ax.yaxis.set_major_formatter(dollars)
    ax.set_title("Four times the data, half the error", fontsize=16, color=INK, loc="left", pad=10)
    tidy(ax)
    return fig


@figure("ci-coverage")
def ci_coverage():
    """50 random samples of 50 sales, each with a 95% CI for the mean; the orange ones miss the population mean."""
    y = home_prices()
    rng = np.random.default_rng(SEED + 1)
    fig, ax = new_fig(height=700)
    misses = 0
    for i in range(50):
        s = rng.choice(y, 50, replace=False)
        half = stats.t.ppf(0.975, 49) * s.std(ddof=1) / np.sqrt(50)
        lo, hi = s.mean() - half, s.mean() + half
        miss = not (lo <= y.mean() <= hi)
        misses += miss
        color = ORANGE if miss else QUIET
        ax.plot([lo, hi], [i, i], color=color, linewidth=2, zorder=3)
        ax.scatter([s.mean()], [i], color=color if miss else STEEL, s=14, zorder=4)
    ax.axvline(y.mean(), color=INK, linewidth=1.5, zorder=2)
    ax.text(y.mean(), 51.5, f"population mean {dollars(y.mean())}", color=INK, fontsize=13, ha="center")
    ax.set_title(f"{50 - misses} of 50 intervals cover the population mean", fontsize=16, color=INK, loc="left", pad=22)
    ax.set(yticks=[], ylim=(-1, 53), xlabel="95% confidence interval from one sample of 50 sales")
    ax.xaxis.set_major_formatter(dollars)
    tidy(ax, grid="x", spines=("bottom",))
    return fig


@figure("sampling-designs")
def sampling_designs():
    """Four ways to pick 12 of 120: simple random, stratified, cluster, and systematic."""
    rows, cols = 6, 20
    # Numbered down each column, the way a list of 120 would be printed in columns.
    grid = np.array([(r, c) for c in range(cols) for r in range(rows)])
    rng = np.random.default_rng(SEED)
    idx = np.arange(rows * cols)
    designs = {
        "Simple random: any 12": rng.choice(idx, 12, replace=False),
        "Stratified: 2 from each row": np.concatenate([rng.choice(idx[grid[:, 0] == r], 2, replace=False) for r in range(rows)]),
        "Cluster: 3 random blocks of 4": np.concatenate([idx[(grid[:, 1] // 4 == b // rows) & (grid[:, 0] == b % rows)] for b in rng.choice(30, 3, replace=False)]),
        "Systematic: every 10th, random start": idx[rng.integers(10)::10],
    }
    fig, axes = new_fig(height=620, nrows=4)
    for ax, (title, chosen) in zip(axes, designs.items()):
        picked = np.isin(idx, chosen)
        ax.scatter(grid[~picked, 1], -grid[~picked, 0], s=55, color=BORDER, edgecolor=QUIET, linewidth=0.6)
        ax.scatter(grid[picked, 1], -grid[picked, 0], s=70, color=ORANGE, edgecolor=ORANGE_DARK, linewidth=0.8, zorder=3)
        ax.set_title(title, fontsize=15, color=INK, loc="left", pad=4)
        ax.set(xlim=(-0.8, cols - 0.2), ylim=(-rows + 0.4, 0.6))
        ax.axis("off")
    fig.subplots_adjust(hspace=0.5)
    return fig


@figure("big-data-paradox")
def big_data_paradox():
    """A hypothetical poll: a random sample homes in on the truth, a biased one homes in on the wrong answer with ever more confidence."""
    truth = 0.50
    biased = 0.60  # people with the trait respond more often, so the sample overrepresents them
    ns = np.unique(np.logspace(1.5, 5.5, 25).astype(int))
    rng = np.random.default_rng(SEED)
    fig, ax = new_fig()
    for p, color, label in [(truth, STEEL, "random sample"), (biased, ORANGE, "self-selected sample")]:
        est = rng.binomial(ns, p) / ns
        half = 1.96 * np.sqrt(est * (1 - est) / ns)
        ax.fill_between(ns, est - half, est + half, color=color, alpha=0.2, linewidth=0)
        ax.plot(ns, est, color=color, linewidth=2.5, zorder=3)
        ax.text(ns[-1] * 1.15, est[-1], label, color=color, fontsize=14, va="center")
    ax.axhline(truth, color=INK, linewidth=1, linestyle=(0, (4, 4)))
    ax.text(40, truth - 0.03, "true share: 50%", color=INK, fontsize=13)
    ax.set_xscale("log")
    ax.set(ylim=(0.3, 0.75), xlabel="Number of responses (log scale)", ylabel="Estimated share, with 95% CI")
    ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0%}")
    tidy(ax)
    return fig


def main(argv: list[str]) -> None:
    if FONT_PATH.exists():
        font_manager.fontManager.addfont(str(FONT_PATH))
        plt.rcParams["font.family"] = font_manager.FontProperties(fname=str(FONT_PATH)).get_name()
    # Text as paths, per STYLE.md: the SVG stays self-contained.
    plt.rcParams["svg.fonttype"] = "path"

    wanted = argv or list(FIGURES)
    unknown = [name for name in wanted if name not in FIGURES]
    if unknown:
        raise SystemExit(f"unknown figure(s): {', '.join(unknown)}\navailable: {', '.join(FIGURES)}")
    print(f"writing {len(wanted)} figure(s) to {OUT_DIR.relative_to(REPO_ROOT)}")
    for name in wanted:
        save(FIGURES[name](), name)


if __name__ == "__main__":
    main(sys.argv[1:])
