#!/usr/bin/env python3
"""Redraw Tatem et al.'s (2004) "Momentous sprint at the 2156 Olympics?" extrapolation for the Week 6 slides.

Fits a straight line to each of the men's and women's Olympic 100 m winning times in the paper's own Table S1 (1900–2004), extends both lines until they cross, and overlays the five Games held since publication (2008–2024) as hollow points the fit never saw.

Writes two SVGs with identical axes, so the slide can cut from one to the other:
  olympics-100m-dots.svg  the winning times only
  olympics-100m-2156.svg  the same times with both fitted lines extended to the crossing

NOTICE: This script was substantially drafted by an LLM coding system.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import polars as pl
from matplotlib import font_manager

OUT_DIR = Path(__file__).resolve().parent
DATA_DIR = OUT_DIR / "data"
REPO_ROOT = OUT_DIR.parents[2]
STEM = "olympics-100m-2156"
FONT_PATH = OUT_DIR.parent / "fonts" / "libre-franklin" / "LibreFranklin-Regular.ttf"

# STYLE.md palette
ORANGE = "#F9461C"
INK = "#1A1A1A"
STEEL = "#565A5C"
BORDER = "#DDDDDD"
PAPER = "#FFFFFF"

PHI = (1 + 5**0.5) / 2
WIDTH_PX = 1000
HEIGHT_PX = round(WIDTH_PX / PHI)
DPI = 100

X_MAX = 2200
# Women are the orange focal series: their steeper line is what makes the two cross.
SERIES = {"men_s": ("Men", STEEL), "women_s": ("Women", ORANGE)}


def _use_repo_font() -> str | None:
    if not FONT_PATH.exists():
        return None
    font_manager.fontManager.addfont(str(FONT_PATH))
    return font_manager.FontProperties(fname=str(FONT_PATH)).get_name()


def fit_lines(fitted: pl.DataFrame) -> dict[str, np.ndarray]:
    lines = {}
    for col in SERIES:
        d = fitted.select("year", col).drop_nulls()
        lines[col] = np.polyfit(d["year"].to_numpy(), d[col].to_numpy(), 1)
    return lines


def crossing(lines: dict[str, np.ndarray]) -> tuple[float, float]:
    (m1, b1), (m2, b2) = lines["men_s"], lines["women_s"]
    year = (b2 - b1) / (m1 - m2)
    return year, m1 * year + b1


def draw(fitted: pl.DataFrame, later: pl.DataFrame, model: bool, out_path: Path) -> float:
    lines = fit_lines(fitted)
    cross_year, cross_time = crossing(lines)

    fig = plt.figure(figsize=(WIDTH_PX / DPI, HEIGHT_PX / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    ax = fig.add_axes((0.08, 0.12, 0.88, 0.78))
    ax.set_facecolor(PAPER)

    ax.set_xlim(1890, X_MAX)
    ax.set_ylim(7, 12.5)
    ax.set_xticks(range(1900, X_MAX + 1, 50))
    ax.tick_params(axis="both", colors=STEEL, labelsize=22)
    ax.set_ylabel("Winning time (seconds)", rotation=0, ha="left", va="bottom", fontsize=22, color=STEEL)
    ax.yaxis.set_label_coords(0, 1.02)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_color(BORDER)
    ax.spines["bottom"].set_color(BORDER)
    ax.grid(axis="y", color=BORDER, linewidth=0.8)
    ax.set_axisbelow(True)

    last_fit_year = fitted["year"].max()
    for col, (label, color) in SERIES.items():
        slope, intercept = lines[col]
        d = fitted.select("year", col).drop_nulls()
        first = d["year"].min()
        ax.scatter(d["year"], d[col], s=46, color=color, zorder=3)
        ax.scatter(later["year"], later[col], s=46, facecolors=PAPER, edgecolors=color, linewidths=2, zorder=3)
        if not model:
            # With no lines to label, name each cloud of dots: women above theirs, men below theirs.
            ax.annotate(label, xy=(1990, 11.6) if col == "women_s" else (1985, 9.35), ha="center", va="center", fontsize=24, color=color)
            continue
        ax.plot([first, last_fit_year], [slope * first + intercept, slope * last_fit_year + intercept], color=color, linewidth=2.5, zorder=2)
        ax.plot([last_fit_year, cross_year], [slope * last_fit_year + intercept, cross_time], color=color, linewidth=2.5, linestyle=(0, (5, 4)), zorder=2)
        # Both lines fall to the right, so above-right of the women's line and below-left of the men's stay clear of the lines.
        at = 2050 if col == "women_s" else 2090
        ax.annotate(label, xy=(at, slope * at + intercept), xytext=(10, 10) if col == "women_s" else (-10, -10), textcoords="offset points", ha="left" if col == "women_s" else "right", va="bottom" if col == "women_s" else "top", fontsize=24, color=color)

    if model:
        ax.scatter([cross_year], [cross_time], s=110, color=INK, zorder=4)
        ax.annotate("The lines cross:\nwomen win in 2156?", xy=(cross_year, cross_time), xytext=(8, -16), textcoords="offset points", ha="right", va="top", fontsize=22, color=INK)
    first_line = "filled: 1900–2004, used for the fit" if model else "filled: 1900–2004, in the 2004 paper"
    ax.annotate(f"{first_line}\nhollow: 2008–2024, after the paper", xy=(2195, 12.4), ha="right", va="top", fontsize=19, color=STEEL)

    fig.savefig(out_path, format="svg", facecolor=PAPER)
    plt.close(fig)
    return cross_year


def main() -> None:
    family = _use_repo_font()
    if family:
        plt.rcParams["font.family"] = family
    plt.rcParams["svg.fonttype"] = "path"
    plt.rcParams["svg.hashsalt"] = STEM  # stable ids, so re-runs make clean diffs

    fitted = pl.read_csv(DATA_DIR / "tatem-2004-table-s1.csv")
    later = pl.read_csv(DATA_DIR / "olympic-100m-2008-2024.csv")
    for model, name in ((False, "olympics-100m-dots"), (True, STEM)):
        out = OUT_DIR / f"{name}.svg"
        cross_year = draw(fitted, later, model, out)
        print(f"wrote {out.relative_to(REPO_ROOT)}")
    print(f"lines cross in {cross_year:.1f}")


if __name__ == "__main__":
    main()
