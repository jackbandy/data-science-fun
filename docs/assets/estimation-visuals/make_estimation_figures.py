#!/usr/bin/env python3
"""Estimation figures for the Week 7, Day 2 slides: Galton's ox-weight guesses and the Adams/Wabash Fermi estimate.

NOTICE: this file was substantially drafted by an LLM coding system and has not yet been reviewed. Check every figure against the slide it illustrates.

Follows docs/assets/STYLE.md: golden-ratio canvases, grayscale neutrals with orange reserved for the focal element, horizontal y-axis labels, vendored Libre Franklin drawn as paths so each SVG is self-contained.

Data (see SOURCES.md in this folder):
  * vox-populi reads the synthetic reconstruction in datasets/galton-vox-populi-1907/.
  * adams-wabash-weekdays reads datasets/cta-ridership/ (the 60 MB daily file).

Usage:  python3 make_estimation_figures.py [name ...]
        (docs/slides/.venv has every dependency: numpy, polars, matplotlib)
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


@figure("vox-populi")
def vox_populi():
    """Galton's 787 ox-weight guesses (synthetic reconstruction from his published quantiles)."""
    guesses = pl.read_csv(DATASETS / "galton-vox-populi-1907" / "vox-populi-synthetic.csv")["estimate"].to_numpy()
    fig, ax = new_fig()
    ax.hist(guesses, bins=np.arange(880, 1540, 20), color=QUIET, zorder=3)
    top = ax.get_ylim()[1]
    ax.axvline(1198, color=INK, linewidth=2, zorder=4)
    ax.axvline(np.median(guesses), color=ORANGE, linewidth=2, linestyle=(0, (4, 3)), zorder=4)
    ax.text(1188, top * 0.97, "actual\n1,198 lb", color=INK, fontsize=14, ha="right", va="top")
    ax.text(1217, top * 0.97, f"median guess\n{np.median(guesses):,.0f} lb", color=ORANGE_DARK, fontsize=14, va="top")
    ax.set(xlabel="Guessed dressed weight of the ox (lb)", ylabel="Guesses")
    tidy(ax)
    return fig


@figure("adams-wabash-weekdays")
def adams_wabash_weekdays():
    """Weekday entries at Adams/Wabash in 2025, the answer key for the Fermi estimate."""
    df = pl.read_csv(DATASETS / "cta-ridership" / "Station_Entries_-_Daily_Totals_20260527.csv", infer_schema_length=0)
    rides = df.filter((pl.col("station_id") == "40680") & (pl.col("daytype") == "W") & pl.col("date").str.ends_with("/2025"))["rides"].str.replace_all(",", "").cast(pl.Int64).to_numpy()
    fig, ax = new_fig()
    ax.hist(rides, bins=25, color=QUIET, zorder=3)
    med = np.median(rides)
    ax.axvline(med, color=ORANGE, linewidth=2.5, zorder=4)
    ax.text(med * 1.02, ax.get_ylim()[1] * 0.95, f"median weekday\n{med:,.0f} entries", color=ORANGE_DARK, fontsize=15, va="top")
    ax.set(xlabel=f"Entries per weekday at Adams/Wabash, 2025 ({len(rides)} weekdays)", ylabel="Weekdays")
    ax.xaxis.set_major_formatter(lambda v, _: f"{v:,.0f}")
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
