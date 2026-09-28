#!/usr/bin/env python3
"""Generate the box, dot/interval, and swarm counterparts to the Week 6 HOP animation.

Draws the same sampled weekdays as make_hops_animation.py and make_violin_plot.py, so the slides compare display types on identical data. The deck order is box, violin, dot/interval, swarm.

This script was substantially drafted by an LLM coding system
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import polars as pl
import seaborn as sns

from make_hops_animation import (
    BORDER,
    DPI,
    HEIGHT_PX,
    INK,
    N_FRAMES,
    ORANGE,
    OUT_DIR,
    PAPER,
    REPO_ROOT,
    SEED,
    STEEL,
    STOPS,
    WIDTH_PX,
    X_POS,
    _use_repo_font,
    load_paired_weekdays,
)

# CTA 'L' route colors (STYLE.md): Halsted in Blue Line blue, 35th/Archer in Orange Line orange.
BLUE = "#00A1DE"
STOP_COLORS = (BLUE, ORANGE)


def sample_title(dates: pl.Series) -> str:
    """Chart title naming which weekdays were drawn."""
    return f"Which stop is busier? ({N_FRAMES} random weekdays, {dates.min():%b %Y}–{dates.max():%b %Y})"


def sample_values() -> tuple[np.ndarray, str]:
    """The HOP's weekdays (same seed), as an (N_FRAMES, 2) array of entries, plus the chart title."""
    paired = load_paired_weekdays()
    rng = np.random.default_rng(SEED)
    idx = rng.choice(len(paired), size=N_FRAMES, replace=False)
    sample = paired[idx]
    values = np.column_stack(
        [sample[STOPS[0][0]].to_numpy(), sample[STOPS[1][0]].to_numpy()]
    ).astype(float)
    return values, sample_title(sample["date"])


def new_axes(values: np.ndarray, title: str):
    """Figure and axes styled to match the HOP and violin slides."""
    fig, ax = plt.subplots(figsize=(WIDTH_PX / DPI, HEIGHT_PX / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(0.0, 100.0 * np.ceil(1.1 * values.max() / 100.0))
    ax.set_ylabel(
        "Total Entries at Station", rotation=0, ha="left", va="bottom", fontsize=14, color=STEEL
    )
    ax.yaxis.set_label_coords(0, 1.015)
    ax.tick_params(axis="y", colors=STEEL, labelsize=12)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_color(BORDER)
    ax.spines["bottom"].set_color(BORDER)
    ax.grid(axis="y", color=BORDER, linewidth=0.8, alpha=0.7)
    ax.set_axisbelow(True)
    ax.set_title(
        title,
        fontsize=19,
        color=INK,
        pad=42,
        loc="left",
    )
    return fig, ax


def finish(fig, ax, name: str) -> None:
    # Set ticks last: seaborn's swarmplot overwrites them.
    ax.set_xlim(-0.5, 1.5)
    ax.set_xticks(X_POS)
    ax.set_xticklabels([label for _, label in STOPS], fontsize=17, color=INK)
    ax.set_xlabel("")
    ax.tick_params(axis="x", length=0)
    fig.tight_layout()
    out_path = OUT_DIR / name
    fig.savefig(out_path, dpi=DPI, facecolor=PAPER)
    plt.close(fig)
    print(f"wrote {out_path.relative_to(REPO_ROOT)}")


def box(values: np.ndarray, title: str) -> None:
    fig, ax = new_axes(values, title)
    parts = ax.boxplot(
        [values[:, 0], values[:, 1]],
        positions=X_POS,
        widths=0.42,
        patch_artist=True,
        boxprops={"alpha": 0.55},
        medianprops={"color": INK, "linewidth": 2.5},
        whiskerprops={"linewidth": 1.5},
        capprops={"linewidth": 1.5},
        flierprops={"marker": "o", "markerfacecolor": "none"},
    )
    for i, color in enumerate(STOP_COLORS):
        parts["boxes"][i].set_facecolor(color)
        parts["boxes"][i].set_edgecolor(color)
        # boxplot returns two whiskers and two caps per box, in box order.
        for line in parts["whiskers"][2 * i : 2 * i + 2] + parts["caps"][2 * i : 2 * i + 2]:
            line.set_color(color)
        parts["fliers"][i].set_markeredgecolor(color)
    finish(fig, ax, "box-ridership-ordering.png")


def dot_interval(values: np.ndarray, title: str) -> None:
    """Median dot with a full-width dashed median line, thick 50% interval, thin 95% interval; no caps."""
    fig, ax = new_axes(values, title)
    # Label each median line at its own stop's edge (Halsted left, 35th/Archer right) so the two close labels don't collide.
    label_spots = ((-0.48, "left", "top"), (1.48, "right", "bottom"))
    for x, col, color, (label_x, ha, va) in zip(X_POS, values.T, STOP_COLORS, label_spots):
        lo95, lo50, med, hi50, hi95 = np.percentile(col, [2.5, 25, 50, 75, 97.5])
        ax.axhline(med, color=color, linewidth=0.8, linestyle=(0, (4, 3)), zorder=1)
        ax.text(label_x, med + (12 if va == "bottom" else -12), "median", color=color, fontsize=12, ha=ha, va=va)
        ax.plot([x, x], [lo95, hi95], color=color, linewidth=2.5, solid_capstyle="butt")
        ax.plot([x, x], [lo50, hi50], color=color, linewidth=14, solid_capstyle="butt")
        ax.plot(x, med, "o", color=color, markersize=13, markeredgecolor=PAPER, markeredgewidth=2)
    finish(fig, ax, "dot-interval-ridership-ordering.png")


def swarm(values: np.ndarray, title: str) -> None:
    fig, ax = new_axes(values, title)
    for x, col, color in zip(X_POS, values.T, STOP_COLORS):
        sns.swarmplot(x=np.full(len(col), x), y=col, native_scale=True, color=color, size=7, ax=ax)
    finish(fig, ax, "swarm-ridership-ordering.png")


def main() -> None:
    family = _use_repo_font()
    if family:
        plt.rcParams["font.family"] = family

    values, title = sample_values()
    box(values, title)
    dot_interval(values, title)
    swarm(values, title)

    for (_, label), col in zip(STOPS, values.T):
        q = np.percentile(col, [2.5, 25, 50, 75, 97.5])
        print(f"  {label}: 95% {q[0]:.0f}-{q[4]:.0f}, 50% {q[1]:.0f}-{q[3]:.0f}, median {q[2]:.0f}")


if __name__ == "__main__":
    main()
