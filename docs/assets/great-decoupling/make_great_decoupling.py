#!/usr/bin/env python3
"""Recreate Brynjolfsson & McAfee's "Great Decoupling" chart for the Week 6 slides.

Four U.S. series, each indexed to 1947 = 100: labor productivity, real GDP per
capita, private employment, and median family income. The original (HBR, June
2015) is in this folder; this rebuilds it from current FRED / Census vintages,
so values differ slightly from the printed chart.

Writes two SVGs with identical geometry, so the slide can cut from one to the other:
  great-decoupling-blank.svg     axes, ticks, and labels only (the "frame")
  great-decoupling-complete.svg  the same frame with the four lines

NOTICE: This script was substantially drafted by an LLM coding system.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import polars as pl
from matplotlib import font_manager

OUT_DIR = Path(__file__).resolve().parent
DATA_DIR = OUT_DIR / "data"
REPO_ROOT = OUT_DIR.parents[2]
STEM = "great-decoupling"
FONT_PATH = OUT_DIR.parent / "fonts" / "libre-franklin" / "LibreFranklin-Regular.ttf"

# STYLE.md palette
ORANGE = "#F9461C"
INK = "#1A1A1A"
STEEL = "#565A5C"
QUIET = "#AAAAAA"
BORDER = "#DDDDDD"
PAPER = "#FFFFFF"

PHI = (1 + 5**0.5) / 2
WIDTH_PX = 1000
HEIGHT_PX = round(WIDTH_PX / PHI)
DPI = 100

START_YEAR = 1947
END_YEAR = 2012  # the HBR chart runs through roughly 2012

# (label, color). Median family income is the orange focal line: it is the one
# that "falls behind," which is the whole point of the chart.
SERIES = {
    "productivity": ("Labor productivity", INK),
    "gdp": ("Real GDP per capita", STEEL),
    "employment": ("Private employment", QUIET),
    "income": ("Median family income", ORANGE),
}


def _use_repo_font() -> str | None:
    if not FONT_PATH.exists():
        return None
    font_manager.fontManager.addfont(str(FONT_PATH))
    return font_manager.FontProperties(fname=str(FONT_PATH)).get_name()


def _fred_annual(series_id: str) -> pl.DataFrame:
    """Calendar-year mean of a FRED series (quarterly or monthly)."""
    return (
        pl.read_csv(DATA_DIR / f"fred-{series_id}.csv", try_parse_dates=True)
        .rename({"observation_date": "date", series_id: "value"})
        .group_by(pl.col("date").dt.year().alias("year"))
        .agg(pl.col("value").mean())
    )


def load_indexed() -> pl.DataFrame:
    frames = {
        "productivity": _fred_annual("OPHNFB"),
        "gdp": _fred_annual("A939RX0Q048SBEA"),
        "employment": _fred_annual("USPRIV"),
        "income": pl.read_csv(DATA_DIR / "census-f7-median-family-income.csv").select(
            "year", pl.col("median_family_income_2025_dollars").alias("value")
        ),
    }
    out = None
    for key, df in frames.items():
        df = df.filter(pl.col("year").is_between(START_YEAR, END_YEAR)).sort("year")
        base = df.filter(pl.col("year") == START_YEAR)["value"].item()
        df = df.select("year", (100 * pl.col("value") / base).alias(key))
        out = df if out is None else out.join(df, on="year", how="full", coalesce=True)
    return out.sort("year")


def draw(data: pl.DataFrame, complete: bool, out_path: Path) -> None:
    fig = plt.figure(figsize=(WIDTH_PX / DPI, HEIGHT_PX / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    # Fixed axes box (no tight_layout / bbox="tight") so both files line up exactly.
    ax = fig.add_axes((0.07, 0.10, 0.68, 0.78))
    ax.set_facecolor(PAPER)

    ax.set_xlim(START_YEAR, END_YEAR)
    ax.set_ylim(50, 450)
    ax.set_xticks(range(1950, END_YEAR + 1, 10))
    ax.set_yticks(range(100, 451, 100))
    ax.tick_params(axis="both", colors=STEEL, labelsize=14)
    ax.set_ylabel("Index (1947 = 100)", rotation=0, ha="left", va="bottom", fontsize=15, color=STEEL)
    ax.yaxis.set_label_coords(0, 1.02)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_color(BORDER)
    ax.spines["bottom"].set_color(BORDER)
    ax.grid(axis="y", color=BORDER, linewidth=0.8)
    ax.set_axisbelow(True)

    if complete:
        years = data["year"].to_numpy()
        ends = []
        for key, (label, color) in SERIES.items():
            y = data[key].to_numpy()
            ax.plot(years, y, color=color, linewidth=3, solid_capstyle="round", zorder=3)
            ends.append((y[-1], label))
        # Direct labels at the right end, nudged apart so they never overlap.
        ends.sort()
        min_gap = 22
        placed = []
        for value, label in ends:
            pos = max(value, placed[-1] + min_gap) if placed else value
            placed.append(pos)
            ax.annotate(
                label, xy=(END_YEAR, value), xytext=(END_YEAR + 1.2, pos),
                va="center", ha="left", fontsize=15, color=INK, annotation_clip=False,
            )

    fig.savefig(out_path, format="svg", facecolor=PAPER)
    plt.close(fig)


def main() -> None:
    family = _use_repo_font()
    if family:
        plt.rcParams["font.family"] = family
    plt.rcParams["svg.fonttype"] = "path"
    plt.rcParams["svg.hashsalt"] = STEM  # stable ids, so re-runs make clean diffs

    data = load_indexed()
    for complete, suffix in ((False, "blank"), (True, "complete")):
        out = OUT_DIR / f"{STEM}-{suffix}.svg"
        draw(data, complete, out)
        print(f"wrote {out.relative_to(REPO_ROOT)}")
    last = data.filter(pl.col("year") == END_YEAR).row(0, named=True)
    print("  " + ", ".join(f"{k}={v:.0f}" for k, v in last.items() if k != "year") + f" in {END_YEAR}")


if __name__ == "__main__":
    main()
