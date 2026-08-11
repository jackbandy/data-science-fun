#!/usr/bin/env python3
"""Generate the Hypothetical Outcome Plot (HOP) animation for the Week 6 slides.

A HOP replaces a static summary of a distribution (error bar, violin, shaded
band) with an animation: each frame is one draw. The viewer reads uncertainty
off how much the marks move, and reads "how sure are we?" off how often the
ordering flips -- the framing in Hullman, Resnick & Adar (2015),
doi:10.1371/journal.pone.0142444.

This script was substantially drafted by an LLM coding system
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import polars as pl
from matplotlib import font_manager
from matplotlib.animation import PillowWriter

OUT_DIR = Path(__file__).resolve().parent
REPO_ROOT = OUT_DIR.parents[2]
DATA_DIR = REPO_ROOT / "datasets" / "cta-ridership"
OUT_PATH = OUT_DIR / "hops-ridership-ordering.gif"
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

# (dataset station name, label for the slide)
STOPS = (("Halsted-Orange", "Halsted"), ("35th/Archer", "35th/Archer"))
START_DATE = date(2025, 1, 1)

N_FRAMES = 60
FRAME_MS = 350
SEED = 418

X_POS = np.array([0.0, 1.0])
MARK_HALF_WIDTH = 0.26


def _use_repo_font() -> str | None:
    """Register the vendored Libre Franklin; return its family name, else None.

    Reads the .ttf rather than the .woff2 sitting beside it: the woff2 is for the
    web slides, and matplotlib cannot decode woff2 without brotli. Falls back to
    matplotlib's default sans if the file is missing, so the script still runs.
    """
    if not FONT_PATH.exists():
        return None
    font_manager.fontManager.addfont(str(FONT_PATH))
    return font_manager.FontProperties(fname=str(FONT_PATH)).get_name()


def load_paired_weekdays() -> pl.DataFrame:
    """One row per weekday, with both stops' entries; dates present for both."""
    matches = sorted(DATA_DIR.glob("Station_Entries_*.csv"))
    if not matches:
        raise FileNotFoundError(f"no Station_Entries_*.csv in {DATA_DIR}")
    csv_path = matches[-1]

    names = [name for name, _ in STOPS]
    df = (
        pl.read_csv(csv_path)
        .with_columns(
            pl.col("date").str.to_date("%m/%d/%Y"),
            # `rides` ships with thousands separators, e.g. "1,059".
            pl.col("rides").str.replace_all(",", "").cast(pl.Int64),
        )
        .filter(
            pl.col("stationname").is_in(names)
            & (pl.col("daytype") == "W")  # W = weekday
            & (pl.col("date") >= START_DATE)
        )
    )
    return (
        df.pivot(values="rides", index="date", on="stationname")
        .drop_nulls()
        .sort("date")
    )


def main() -> None:
    family = _use_repo_font()
    if family:
        plt.rcParams["font.family"] = family

    paired = load_paired_weekdays()
    a_name, b_name = STOPS[0][0], STOPS[1][0]

    rng = np.random.default_rng(SEED)
    idx = rng.choice(len(paired), size=N_FRAMES, replace=False)
    sample = paired[idx]

    dates = sample["date"].to_list()
    values = np.column_stack(
        [sample[a_name].to_numpy(), sample[b_name].to_numpy()]
    ).astype(float)

    y_min = 0.0
    y_max = 100.0 * np.ceil(1.1 * values.max() / 100.0)

    fig, ax = plt.subplots(figsize=(WIDTH_PX / DPI, HEIGHT_PX / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)

    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(X_POS)
    ax.set_xticklabels([label for _, label in STOPS], fontsize=17, color=INK)
    # Horizontal label above the axis: readable without tilting your head, and
    # it clears the tick labels instead of crowding them.
    ax.set_ylabel(
        "Total Entries at Station", rotation=0, ha="left", va="bottom", fontsize=14, color=STEEL
    )
    ax.yaxis.set_label_coords(0, 1.015)
    ax.tick_params(axis="y", colors=STEEL, labelsize=12)
    ax.tick_params(axis="x", length=0)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_color(BORDER)
    ax.spines["bottom"].set_color(BORDER)
    ax.grid(axis="y", color=BORDER, linewidth=0.8, alpha=0.7)
    ax.set_axisbelow(True)

    # Faint vertical guides so the marks read as "same slot, different day".
    for x in X_POS:
        ax.plot([x, x], [y_min, y_max], color=BORDER, linewidth=1.0, zorder=1)

    ax.set_title(
        "Which stop is busier? (One weekday per frame)",
        fontsize=19,
        color=INK,
        pad=42,  # clears the horizontal "Total Entries" label sitting above the axis
        loc="left",
    )

    marks = [
        ax.plot([], [], linewidth=7, solid_capstyle="butt", zorder=3)[0] for _ in STOPS
    ]
    date_label = ax.text(
        1.5,
        y_min + 0.03 * (y_max - y_min),
        "",
        ha="right",
        va="bottom",
        fontsize=13,
        color=QUIET,
    )

    fig.tight_layout()

    def update(frame: int):
        row = values[frame]
        leader = int(np.argmax(row))
        for i, (mark, value) in enumerate(zip(marks, row)):
            mark.set_data(
                [X_POS[i] - MARK_HALF_WIDTH, X_POS[i] + MARK_HALF_WIDTH],
                [value, value],
            )
            # Orange marks the stop that happens to be busier this day.
            mark.set_color(ORANGE if i == leader else STEEL)
        date_label.set_text(dates[frame].strftime("%a, %b %-d, %Y"))
        return (*marks, date_label)

    writer = PillowWriter(fps=1000 / FRAME_MS)
    with writer.saving(fig, str(OUT_PATH), dpi=DPI):
        for frame in range(N_FRAMES):
            update(frame)
            writer.grab_frame(facecolor=PAPER)

    plt.close(fig)

    wins_b = int((values[:, 1] > values[:, 0]).sum())
    overall = int((paired[b_name] > paired[a_name]).sum())
    print(f"wrote {OUT_PATH.relative_to(REPO_ROOT)}")
    print(f"  sampled {N_FRAMES} of {len(paired)} paired weekdays since {START_DATE}")
    print(f"  35th/Archer busier in {wins_b}/{N_FRAMES} frames ({wins_b / N_FRAMES:.0%})")
    print(f"  ...vs {overall}/{len(paired)} ({overall / len(paired):.0%}) across all weekdays")


if __name__ == "__main__":
    main()
