#!/usr/bin/env python3
"""The Macworld 2008 smartphone market share, drawn as a donut chart.

NOTICE: this file was substantially drafted by an LLM coding system. It is
maintained and vetted by jxb@uic.edu.

The slides walk the same six numbers through three forms: Steve Jobs' 3D pie
(`macworld-pie-3d.svg`), the honest flat pie (`macworld-pie-2d.svg`) and then
this donut, so the only thing that changes between the last two is the hole.
Wedge order (clockwise from 12 o'clock) and wedge colors are matched to the
flat pie on purpose; the drawing itself is ours, so this file carries no
ShareAlike obligation from the Wikimedia original.

Data: Gartner, US smartphone market share, CQ3 2007, as printed on the keynote
slide (see SOURCES.md).

Usage:  python3 make_macworld_donut.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib import font_manager

OUT = Path(__file__).resolve().parent / "macworld-donut.svg"
FONT_PATH = Path(__file__).resolve().parents[1] / "fonts" / "libre-franklin" / "LibreFranklin-Regular.ttf"

INK = "#1A1A1A"
PAPER = "#FFFFFF"

# Clockwise from 12 o'clock, in the flat pie's order and its palette.
SHARES = [
    ("RIM", 39.0, "#9cf"),
    ("Apple", 19.5, "#0c0"),
    ("Palm", 9.8, "#ff6"),
    ("Motorola", 7.4, "#fcc"),
    ("Nokia", 3.1, "#f9f"),
    ("Other", 21.2, "#c0f"),
]


def main() -> None:
    if FONT_PATH.exists():
        font_manager.fontManager.addfont(str(FONT_PATH))
        plt.rcParams["font.family"] = font_manager.FontProperties(
            fname=str(FONT_PATH)).get_name()
    # Text as paths, per docs/assets/STYLE.md: the SVG stays self-contained.
    plt.rcParams["svg.fonttype"] = "path"

    values = [share for _, share, _ in SHARES]
    colors = [color for _, _, color in SHARES]

    fig, ax = plt.subplots(figsize=(6.4, 5.0), dpi=100)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)

    # startangle=90 with counterclock=False puts RIM at 12 o'clock and runs the
    # wedges clockwise, the same reading order as the pie panels.
    # Name and share together, outside the ring: three of the six wedges are
    # too thin to hold a number, and splitting the label from its value would
    # make those three read differently from the other three.
    ax.pie(
        values,
        colors=colors,
        startangle=90,
        counterclock=False,
        labels=[f"{name}\n{share}%" for name, share, _ in SHARES],
        labeldistance=1.14,
        textprops={"color": INK, "fontsize": 13, "ha": "center"},
        wedgeprops={"width": 0.42, "edgecolor": PAPER, "linewidth": 1.5},
    )
    ax.set_aspect("equal")

    fig.savefig(OUT, format="svg", facecolor=PAPER, bbox_inches="tight",
                pad_inches=0.12)
    plt.close(fig)
    print(f"wrote {OUT.name} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
