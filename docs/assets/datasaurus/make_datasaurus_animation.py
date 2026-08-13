#!/usr/bin/env python3
"""Generate the Datasaurus Dozen animation and still panel for the Week 4 slides.

Thirteen datasets, one animation: the cloud of points morphs from a dinosaur to
a star to a circle to a set of stripes, while the summary statistics printed
under it -- mean of x, mean of y, both standard deviations, and Pearson's r --
never move, because to two decimal places they are the same in every one of the
thirteen datasets. That is the argument for plotting your data, made in a single
frame-by-frame image.

Data and construction: Justin Matejka and George Fitzmaurice, "Same Stats,
Different Graphs: Generating Datasets with Varied Appearance and Identical
Statistics through Simulated Annealing," CHI 2017.

Design notes (see docs/assets/STYLE.md):
  - points are orange, because they are the only thing on the canvas that
    changes; the statistics readout is steel, because it is the constant.
  - the axes box takes the data's own aspect ratio, so the dinosaur is never
    stretched; the canvas is sized around it.
  - the morph interpolates each point along a straight line to its counterpart
    in the next dataset. Points are matched by their angle around the shared
    centroid, which keeps the cloud from folding through itself mid-transition.

This script was substantially drafted by an LLM coding system
"""

from __future__ import annotations

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
DATA_PATH = REPO_ROOT / "datasets" / "datasaurus-dozen" / "datasaurus-dozen.csv"
OUT_PATH = OUT_DIR / "datasaurus-dozen.gif"
PANEL_PATH = OUT_DIR / "datasaurus-dozen-panel.svg"
PANEL_BARE_PATH = OUT_DIR / "datasaurus-dozen-panel-unlabelled.svg"
FONT_PATH = OUT_DIR.parent / "fonts" / "libre-franklin" / "LibreFranklin-Regular.ttf"

# STYLE.md palette
ORANGE = "#F9461C"
INK = "#1A1A1A"
STEEL = "#565A5C"
QUIET = "#AAAAAA"
BORDER = "#DDDDDD"
PAPER = "#FFFFFF"

# The dinosaur is taller than it is wide (x spans ~76 units, y spans ~100), so
# the canvas is portrait-leaning and the axes box is pinned to the data's own
# aspect ratio below. A 16:9 frame would render the dino squashed, which is a
# strange thing to do in a figure whose entire argument is "look at the shape."
WIDTH_PX = 680
HEIGHT_PX = 760
DPI = 100

# The still panel is a 4 x 4 grid of small multiples. The dinosaur takes the
# top-left 2 x 2 block -- it is the one everybody recognizes, and it is the
# shape the other twelve were generated from -- and the remaining twelve fill
# the other twelve cells exactly. The frame is square, so the 2 x 2 dino block
# and the twelve single cells are all square too.
PANEL_WIDTH_PX = 900
PANEL_HEIGHT_PX = 900

# Start and end on the dinosaur so the loop closes where it began. The middle
# is ordered to alternate between "obviously structured" and "looks like noise".
ORDER = (
    "dino",
    "star",
    "h_lines",
    "circle",
    "x_shape",
    "v_lines",
    "bullseye",
    "slant_up",
    "dots",
    "slant_down",
    "high_lines",
    "wide_lines",
    "away",
)

HOLD_FRAMES = 7  # frames a shape sits still, long enough to read it
MORPH_FRAMES = 9  # frames spent travelling to the next shape
FRAME_MS = 60

LABELS = {
    "dino": "dino",
    "star": "star",
    "h_lines": "h_lines",
    "circle": "circle",
    "x_shape": "x_shape",
    "v_lines": "v_lines",
    "bullseye": "bullseye",
    "slant_up": "slant_up",
    "dots": "dots",
    "slant_down": "slant_down",
    "high_lines": "high_lines",
    "wide_lines": "wide_lines",
    "away": "away",
}


def _use_repo_font() -> str | None:
    """Register the vendored Libre Franklin; return its family name, else None."""
    if not FONT_PATH.exists():
        return None
    font_manager.fontManager.addfont(str(FONT_PATH))
    return font_manager.FontProperties(fname=str(FONT_PATH)).get_name()


def load_shapes() -> dict[str, np.ndarray]:
    """One (142, 2) array per dataset, rows sorted by angle around the centroid.

    Every dataset shares a centroid to two decimals, so sorting each one the
    same way pairs up point i in shape A with a point in shape B that sits in
    roughly the same direction from the middle. Straight-line interpolation
    between the two then reads as the cloud rearranging itself rather than
    scrambling.
    """
    df = pl.read_csv(DATA_PATH)
    shapes: dict[str, np.ndarray] = {}
    for name in ORDER:
        sub = df.filter(pl.col("dataset") == name)
        pts = np.column_stack([sub["x"].to_numpy(), sub["y"].to_numpy()])
        centered = pts - pts.mean(axis=0)
        # Scale y by the x/y spread ratio first, so "angle" means angle in the
        # plot's own units rather than in the raw (very unequal) data units.
        angle = np.arctan2(
            centered[:, 1] / centered[:, 1].std(), centered[:, 0] / centered[:, 0].std()
        )
        shapes[name] = pts[np.argsort(angle)]
    return shapes


def stats_line(pts: np.ndarray) -> str:
    x, y = pts[:, 0], pts[:, 1]
    r = np.corrcoef(x, y)[0, 1]
    return (
        f"mean(x) = {x.mean():.2f}     mean(y) = {y.mean():.2f}     "
        f"sd(x) = {x.std(ddof=1):.2f}     sd(y) = {y.std(ddof=1):.2f}     "
        f"r = {r:.2f}"
    )


def smoothstep(t: float) -> float:
    """Ease in and out, so shapes settle instead of stopping dead."""
    return t * t * (3 - 2 * t)


def _grow(limits: tuple[float, float], span: float) -> tuple[float, float]:
    """Widen `limits` to `span`, keeping the midpoint where it is."""
    mid = sum(limits) / 2
    return (mid - span / 2, mid + span / 2)


def write_panel(shapes: dict[str, np.ndarray], path: Path, labelled: bool) -> None:
    """All thirteen shapes as small multiples, for the slide that has to hold still.

    The animation makes the point in motion; this makes the same point on a
    slide you can talk over. No statistics are printed on it — they go beside
    the panel on the slide, computed from the data, so the picture stays a
    picture and the numbers stay one line.

    `labelled=False` drops the dataset names, for uses where the shapes are the
    whole message and the names are noise.
    """
    fig = plt.figure(figsize=(PANEL_WIDTH_PX / DPI, PANEL_HEIGHT_PX / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    grid = fig.add_gridspec(4, 4)

    # dino spans the top-left 2 x 2 block; the other twelve fill the rest.
    cells = [grid[0:2, 0:2]]
    cells += [grid[r, c] for r in (0, 1) for c in (2, 3)]
    cells += [grid[r, c] for r in (2, 3) for c in range(4)]

    every = np.vstack(list(shapes.values()))
    xlim = (every[:, 0].min() - 4, every[:, 0].max() + 4)
    ylim = (every[:, 1].min() - 4, every[:, 1].max() + 4)
    # Every cell in the 4 x 4 has the frame's own proportions. Rather than
    # squash the shapes into that slot, widen the limits until the data window
    # matches it: the circle stays a circle, and the cells still tile solidly.
    cell_ratio = PANEL_HEIGHT_PX / PANEL_WIDTH_PX
    if np.ptp(ylim) / np.ptp(xlim) < cell_ratio:
        ylim = _grow(ylim, np.ptp(xlim) * cell_ratio)
    else:
        xlim = _grow(xlim, np.ptp(ylim) / cell_ratio)

    for cell, name in zip(cells, ORDER):
        ax = fig.add_subplot(cell)
        pts = shapes[name]
        big = name == "dino"
        ax.scatter(
            pts[:, 0], pts[:, 1],
            s=9 if big else 4, color=ORANGE, alpha=0.85, linewidths=0,
        )
        if labelled:
            ax.set_title(LABELS[name], fontsize=15 if big else 11, color=INK, pad=3)
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
        ax.set_xticks([])
        ax.set_yticks([])
        # Cells fill their slots so the 4 x 4 reads as a solid block. Every
        # panel shares one pair of limits and one slot shape, so the whole grid
        # is stretched by the same small factor and the shapes stay comparable.
        for side in ax.spines.values():
            side.set_color(BORDER)
        ax.set_facecolor(PAPER)

    fig.tight_layout(pad=0.6)
    fig.savefig(path, facecolor=PAPER, format="svg")
    plt.close(fig)


def main() -> None:
    family = _use_repo_font()
    if family:
        plt.rcParams["font.family"] = family

    shapes = load_shapes()
    write_panel(shapes, PANEL_PATH, labelled=True)
    write_panel(shapes, PANEL_BARE_PATH, labelled=False)
    every = np.vstack(list(shapes.values()))
    pad_x = 0.06 * np.ptp(every[:, 0])
    pad_y = 0.10 * np.ptp(every[:, 1])

    fig, ax = plt.subplots(figsize=(WIDTH_PX / DPI, HEIGHT_PX / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)

    ax.set_xlim(every[:, 0].min() - pad_x, every[:, 0].max() + pad_x)
    ax.set_ylim(every[:, 1].min() - pad_y, every[:, 1].max() + pad_y)
    ax.set_xlabel("x", fontsize=13, color=STEEL)
    ax.set_ylabel("y", rotation=0, fontsize=13, color=STEEL, ha="right", va="center")
    ax.tick_params(colors=STEEL, labelsize=11)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_color(BORDER)
    ax.spines["bottom"].set_color(BORDER)
    # One data unit is the same length on both axes: the dino keeps its shape.
    ax.set_box_aspect(np.ptp(ax.get_ylim()) / np.ptp(ax.get_xlim()))

    scatter = ax.scatter([], [], s=42, color=ORANGE, alpha=0.85, linewidths=0, zorder=3)

    # The whole point of the figure: this line is pinned outside the axes and
    # never changes while the cloud underneath it does.
    fig.text(
        0.5,
        0.955,
        stats_line(shapes["dino"]),
        ha="center",
        va="center",
        fontsize=12,
        color=STEEL,
    )
    name_label = ax.text(
        0.99,
        0.97,
        "",
        transform=ax.transAxes,
        ha="right",
        va="top",
        fontsize=16,
        color=INK,
        weight="bold",
    )
    ax.text(
        0.01,
        0.02,
        "Matejka & Fitzmaurice, CHI 2017",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=10,
        color=QUIET,
    )

    fig.subplots_adjust(left=0.12, right=0.97, top=0.93, bottom=0.07)

    # (points, label) for every frame, laid out as hold-then-morph per shape.
    frames: list[tuple[np.ndarray, str]] = []
    for i, name in enumerate(ORDER):
        here = shapes[name]
        there = shapes[ORDER[(i + 1) % len(ORDER)]]
        frames.extend((here, LABELS[name]) for _ in range(HOLD_FRAMES))
        for step in range(1, MORPH_FRAMES + 1):
            t = smoothstep(step / (MORPH_FRAMES + 1))
            frames.append(((1 - t) * here + t * there, ""))

    writer = PillowWriter(fps=1000 / FRAME_MS)
    with writer.saving(fig, str(OUT_PATH), dpi=DPI):
        for pts, label in frames:
            scatter.set_offsets(pts)
            name_label.set_text(label)
            writer.grab_frame(facecolor=PAPER)

    plt.close(fig)

    print(f"wrote {PANEL_PATH.relative_to(REPO_ROOT)}")
    print(f"wrote {PANEL_BARE_PATH.relative_to(REPO_ROOT)}")
    print(f"wrote {OUT_PATH.relative_to(REPO_ROOT)}")
    print(f"  {len(ORDER)} datasets, {len(frames)} frames at {FRAME_MS} ms")
    for name in ORDER:
        print(f"  {name:>11}  {stats_line(shapes[name])}")


if __name__ == "__main__":
    main()
