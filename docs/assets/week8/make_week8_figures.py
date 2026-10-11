#!/usr/bin/env python3
"""Figures for the Week 8, Day 1 "intro to modeling" slides.

NOTICE: this file was substantially drafted by an LLM coding system and has not
yet been reviewed. Check every figure against the slide it illustrates.

Follows docs/assets/STYLE.md and mirrors viz-basics/make_viz_basics_figures.py:
golden-ratio canvases, grayscale neutrals with orange reserved for the focal
element, vendored Libre Franklin drawn as paths so each SVG is self-contained.

Data:
  * Cook County home sales 2025 come from datasets/ in this repo, filtered the
    same way as the Week 5 slides (see the dataset README for provenance).
  * The bias-variance bullseyes are synthetic, redrawn after Scott
    Fortmann-Roe, "Understanding the Bias-Variance Tradeoff" (2012). See
    SOURCES.md in this folder.
  * The loss-function curves are plain math, no data.

Usage:  python3 make_week8_figures.py [name ...]
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
from matplotlib.patches import Circle

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

PHI = (1 + 5**0.5) / 2
WIDTH_PX = 1000
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


def save(fig, name):
    out = OUT_DIR / f"{name}.svg"
    fig.savefig(out, format="svg", facecolor=PAPER, bbox_inches="tight",
                pad_inches=0.12)
    plt.close(fig)
    print(f"  wrote {out.relative_to(REPO_ROOT)}")


def dollars(v, _=None):
    return f"${v / 1e6:g}M" if abs(v) >= 1e6 else f"${v / 1e3:,.0f}k"


_cache: dict[str, object] = {}


def homes() -> pl.DataFrame:
    """Cook County single-family sales, filtered the way the Week 5 slides filter them."""
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
    return _cache["homes"]


# --------------------------------------------------------------------------
# Loss
# --------------------------------------------------------------------------

@figure("loss-functions")
def loss_functions():
    """Squared vs. absolute loss for one point, as a function of the error."""
    err = np.linspace(-3, 3, 400)
    fig, ax = new_fig(width=820)
    ax.plot(err, err**2, color=ORANGE, linewidth=3, zorder=3)
    ax.plot(err, np.abs(err), color=STEEL, linewidth=3, zorder=3)
    ax.text(0, 8.2, "squared  $(y - \\theta)^2$", color=ORANGE, fontsize=15, ha="center")
    ax.text(0, 7.3, "absolute  $|y - \\theta|$", color=STEEL, fontsize=15, ha="center")
    ax.set(xlim=(-3, 3), ylim=(0, 9), xlabel="Error, $y - \\theta$", ylabel="Loss")
    tidy(ax)
    return fig


@figure("house-average-loss")
def house_average_loss():
    """Average loss over all home sales for every candidate constant theta.

    Squared loss bottoms out at the mean, absolute loss at the median. Each
    curve is rescaled to its own minimum so the two shapes share one axis.
    """
    y = homes()["sale_price"].to_numpy().astype(float)
    thetas = np.linspace(100_000, 900_000, 161)
    mse = np.array([np.mean((y - t) ** 2) for t in thetas])
    mae = np.array([np.mean(np.abs(y - t)) for t in thetas])
    mean, median = y.mean(), np.median(y)

    fig, axes = new_fig(width=1000, height=420, ncols=2)
    for ax, curve, best, color, name, est in [
        (axes[0], mse, mean, ORANGE, "Average squared loss", "mean"),
        (axes[1], mae, median, STEEL, "Average absolute loss", "median"),
    ]:
        scaled = curve / curve.min()
        ax.plot(thetas, scaled, color=color, linewidth=3, zorder=3)
        ax.axvline(best, color=INK, linewidth=1, linestyle=(0, (4, 4)), zorder=2)
        ax.text(best + 15_000, scaled.max(), f"{est} = {dollars(best)}",
                color=INK, fontsize=13, va="top")
        ax.set_title(name, fontsize=16, color=INK, loc="left", pad=10)
        ax.set_xlabel("$\\theta$ (one predicted price for every home)")
        ax.xaxis.set_major_formatter(dollars)
        ax.set_yticks([])
        tidy(ax, grid=None, spines=("bottom",))
    fig.subplots_adjust(wspace=0.12)
    return fig


# --------------------------------------------------------------------------
# Bias and variance
# --------------------------------------------------------------------------

@figure("bias-variance-bullseye")
def bias_variance_bullseye():
    """Four targets: rows are bias, columns are variance.

    Each dot is one fitted model (one re-run of the whole data-collection and
    fitting process). Redrawn after Fortmann-Roe (2012).
    """
    rng = np.random.default_rng(418)
    fig, axes = new_fig(width=760, height=760, nrows=2, ncols=2)
    for i, (bias_name, offset) in enumerate([("Low bias", 0.0), ("High bias", 0.48)]):
        for j, (var_name, spread) in enumerate([("Low variance", 0.07), ("High variance", 0.24)]):
            ax = axes[i][j]
            for k, r in enumerate([1.0, 0.75, 0.5, 0.25]):
                ax.add_patch(Circle((0, 0), r, facecolor=PAPER if k % 2 == 0 else SOFT_GRAY,
                                    edgecolor=QUIET, linewidth=1.2, zorder=1))
            ax.add_patch(Circle((0, 0), 0.1, facecolor=ORANGE, edgecolor="none", zorder=2))
            pts = rng.normal(0, spread, size=(12, 2)) + np.array([offset * 0.7, offset * 0.7])
            ax.scatter(pts[:, 0], pts[:, 1], s=46, color=INK, zorder=3,
                       edgecolor=PAPER, linewidth=0.8)
            ax.set(xlim=(-1.08, 1.08), ylim=(-1.08, 1.08), aspect="equal")
            ax.axis("off")
            if i == 0:
                ax.set_title(var_name, fontsize=16, color=INK, pad=8)
            if j == 0:
                ax.text(-1.25, 0, bias_name, fontsize=16, color=INK, rotation=90,
                        ha="center", va="center")
    fig.subplots_adjust(wspace=0.05, hspace=0.08)
    return fig


# --------------------------------------------------------------------------
# Overfitting
# --------------------------------------------------------------------------

def _overfit_sample() -> tuple[np.ndarray, np.ndarray]:
    df = (homes().filter((pl.col("sale_price") < 1_200_000)
                         & (pl.col("building_sqft") < 4_000))
          .sample(14, seed=418))
    return (df["building_sqft"].to_numpy().astype(float),
            df["sale_price"].to_numpy().astype(float))


def _overfit(labeled: bool):
    x, y = _overfit_sample()
    # Polynomials on standardized x, so the degree-10 fit stays numerically sane.
    mu, sd = x.mean(), x.std()
    grid = np.linspace(x.min() - 50, x.max() + 50, 600)
    fits = [
        ("A", 0, "Underfit", "one number for every home"),
        ("B", 1, "Just right", "a line follows the trend"),
        ("C", 10, "Overfit", "chases the noise in 14 sales"),
    ]
    fig, axes = new_fig(width=1100, height=400, ncols=3, sharey=True)
    for ax, (letter, deg, name, note) in zip(axes, fits):
        coef = np.polyfit((x - mu) / sd, y, deg)
        ax.plot(grid, np.polyval(coef, (grid - mu) / sd), color=ORANGE,
                linewidth=2.6, zorder=2)
        ax.scatter(x, y, s=40, color=INK, zorder=3, edgecolor=PAPER, linewidth=0.8)
        ax.set(ylim=(0, 1_300_000))
        ax.yaxis.set_major_formatter(dollars)
        ax.set_xticks([1000, 1500, 2000])
        ax.set_xlabel("Building sqft")
        heading = f"{letter}. {name}" if labeled else letter
        # Same title pad in both versions, so the plain and labeled SVGs line
        # up when one replaces the other on the slide.
        ax.set_title(heading, fontsize=18, color=INK, loc="left", pad=30)
        if labeled:
            ax.text(0, 1.03, note, transform=ax.transAxes, fontsize=12,
                    color=STEEL, va="bottom")
        tidy(ax)
    fig.subplots_adjust(wspace=0.08)
    return fig


@figure("overfit-abc")
def overfit_abc():
    return _overfit(labeled=False)


@figure("overfit-abc-labeled")
def overfit_abc_labeled():
    return _overfit(labeled=True)


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
