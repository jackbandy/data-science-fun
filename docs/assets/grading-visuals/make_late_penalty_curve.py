#!/usr/bin/env python3
"""The late-work sliding scale, drawn as a curve over days late.

Renders the syllabus policy ("Policy for Missed or Late Work") as a picture

This script was substantially drafted by an LLM coding system.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

OUT_DIR = Path(__file__).resolve().parent
REPO_ROOT = OUT_DIR.parents[2]
STEM = "late-penalty-curve"
FONT_PATH = OUT_DIR.parent / "fonts" / "libre-franklin" / "LibreFranklin-Regular.ttf"

# STYLE.md palette
INK = "#1A1A1A"
STEEL = "#565A5C"
QUIET = "#AAAAAA"
BORDER = "#DDDDDD"
SOFT_GRAY = "#F4F4F2"
PAPER = "#FFFFFF"
ORANGE = "#F9461C"

PHI = (1 + 5**0.5) / 2
WIDTH_PX = 1000
HEIGHT_PX = round(WIDTH_PX / PHI)
DPI = 100

FULL_CREDIT = 1.00
FLOOR = 0.50
GRACE_DAYS = 1  # one day late is free: still (almost) full credit
GRACE_CREDIT = 0.99  # the grace day is nominally a point off, so it reads as distinct from the due date
RATE_PER_DAY = 0.10  # the sliding scale, once the grace day is used up
# Where the scale bottoms out: 100% - 10 a day takes five penalized days to
# reach 50%, so day 6. Everything later is the same 50%, out to the 30-day cap.
FLOOR_DAY = GRACE_DAYS + round((FULL_CREDIT - FLOOR) / RATE_PER_DAY)
DAYS_SHOWN = 12  # a few days past the floor, so "level" is visible
LAST_DAY = 30  # the cutoff: nothing is accepted after this

# Days 13-29 are all the same 50%, so they are elided rather than drawn: an
# ellipsis tick, then one more slot standing in for day 30. The x-axis is
# therefore not linear past DAYS_SHOWN, which is what the gap in the line and
# the "..." are there to admit.
X_ELLIPSIS = DAYS_SHOWN + 1
X_END = DAYS_SHOWN + 2


def _use_repo_font() -> str | None:
    """Register the vendored Libre Franklin; return its family name, else None.

    Reads the .ttf rather than the .woff2 beside it: the woff2 is for the web
    slides, and matplotlib cannot decode woff2 without brotli.
    """
    if not FONT_PATH.exists():
        return None
    font_manager.fontManager.addfont(str(FONT_PATH))
    return font_manager.FontProperties(fname=str(FONT_PATH)).get_name()


def credit(days_late: np.ndarray) -> np.ndarray:
    """Maximum credit available, as a fraction, after `days_late` days.

    Full credit through the grace day, then 10 points off per day, then flat
    at the floor. `np.clip` is doing the "down to 50%" clause of the policy,
    and it is also what holds the grace day flat at 100%.
    """
    slid = FULL_CREDIT - RATE_PER_DAY * (days_late - GRACE_DAYS)
    result = np.clip(slid, FLOOR, FULL_CREDIT)
    return np.where(np.asarray(days_late) == GRACE_DAYS, GRACE_CREDIT, result)


def build_figure():
    days = np.arange(0, DAYS_SHOWN + 1)
    values = credit(days)

    fig, ax = plt.subplots(figsize=(WIDTH_PX / DPI, HEIGHT_PX / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)

    ax.set_xlim(-0.5, X_END + 0.7)
    ax.set_ylim(0, 1.12)

    # Everything past one week is the same deal, so it gets one flat band
    # rather than a series of ticks that imply something is still changing.
    ax.axvspan(FLOOR_DAY, X_END + 0.7, color=SOFT_GRAY, zorder=0, linewidth=0)

    # The due date itself: a submission at x = 0 is not late, and the axis
    # starts there so "on time" is the origin rather than a point on a slope.
    ax.axvline(0, color=BORDER, linewidth=1.0, zorder=1)

    ax.plot(
        days, values,
        color=INK, linewidth=2.5, marker="o", markersize=6,
        zorder=3, clip_on=False,
    )
    # The grace day gets its own orange dot, drawn over the line's black one.
    ax.plot(
        [GRACE_DAYS], [GRACE_CREDIT],
        color=ORANGE, marker="o", markersize=6, zorder=4, clip_on=False,
    )

    # Days 13-29: same 50%, drawn as a dotted bridge so the compressed stretch
    # does not read as real, evenly-spaced days.
    ax.plot(
        [DAYS_SHOWN, X_END], [FLOOR, FLOOR],
        color=INK, linewidth=2.5, linestyle=(0, (1.5, 2.5)), zorder=3,
    )
    ax.plot([X_END], [FLOOR], color=INK, marker="o", markersize=6, zorder=3)

    # The cutoff itself: the line stops here rather than running off the edge.
    ax.plot(
        [X_END, X_END], [0, FLOOR],
        color=QUIET, linewidth=1.2, linestyle=(0, (2, 3)), zorder=2,
    )
    ax.annotate(
        "LDOC:\nlast day to submit",
        xy=(X_END, FLOOR),
        xytext=(0, 14),
        textcoords="offset points",
        ha="right", va="bottom", fontsize=13, color=INK, linespacing=1.3,
    )

    ax.annotate(
        "Due date: 100%",
        xy=(0, FULL_CREDIT),
        xytext=(-4, 6),
        textcoords="offset points",
        ha="left", va="bottom", fontsize=14, color=INK, fontweight="bold",
    )
    ax.annotate(
        "Grace day:\nstill 99%",
        xy=(GRACE_DAYS, GRACE_CREDIT),
        xytext=(-16, -12),
        textcoords="offset points",
        ha="center", va="top", fontsize=13, color=ORANGE, linespacing=1.3,
    )
    ax.annotate(
        "Sliding scale (ladder):\n-10% a day",
        xy=(3, credit(np.array([3]))[0]),
        xytext=(4, -30),
        textcoords="offset points",
        ha="right", va="top", fontsize=13, color=STEEL, linespacing=1.3,
    )
    ax.annotate(
        "(50% credit)",
        xy=(FLOOR_DAY + 0.25, FLOOR),
        xytext=(0, 26),
        textcoords="offset points",
        ha="left", va="bottom", fontsize=13, color=STEEL, linespacing=1.3,
    )

    ax.set_xticks(list(days) + [X_ELLIPSIS, X_END])
    ax.set_xticklabels(
        ["due\ndate"]
        + [str(d) for d in days[1:]]
        + ["…", "LDOC"],
        fontsize=12,
        color=STEEL,
    )
    ax.set_xlabel("Days late", fontsize=14, color=STEEL, labelpad=14)

    ax.set_yticks(np.arange(0, 1.01, 0.25))
    ax.set_yticklabels([f"{v:.0%}" for v in np.arange(0, 1.01, 0.25)])
    ax.set_ylabel(
        "Most credit the submission can earn",
        rotation=0, ha="left", va="bottom", fontsize=14, color=STEEL,
    )
    ax.yaxis.set_label_coords(0, 1.015)
    ax.tick_params(axis="y", colors=STEEL, labelsize=12)
    ax.tick_params(axis="x", length=0, colors=STEEL)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_color(BORDER)
    ax.spines["bottom"].set_color(BORDER)
    ax.grid(axis="y", color=BORDER, linewidth=0.8, alpha=0.7)
    ax.set_axisbelow(True)

    ax.set_title(
        "Credit for late homeworks",
        fontsize=19,
        color=INK,
        pad=42,  # clears the horizontal y-axis label sitting above the axis
        loc="left",
    )

    fig.tight_layout()
    return fig


def main() -> None:
    family = _use_repo_font()
    if family:
        plt.rcParams["font.family"] = family
    # Text as paths: the SVG stays self-contained, per STYLE.md.
    plt.rcParams["svg.fonttype"] = "path"

    out_path = OUT_DIR / f"{STEM}.svg"
    fig = build_figure()
    fig.savefig(out_path, format="svg", facecolor=PAPER)
    plt.close(fig)
    print(f"wrote {out_path.relative_to(REPO_ROOT)}")

    for d in (0, 1, 2, 3, FLOOR_DAY, DAYS_SHOWN):
        print(f"  {d:>2} days late -> {credit(np.array([d]))[0]:.1%}")


if __name__ == "__main__":
    main()
