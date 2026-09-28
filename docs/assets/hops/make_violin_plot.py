#!/usr/bin/env python3
"""Generate the static violin-plot counterpart to the Week 6 HOP animation.

Draws the same sampled weekdays as make_hops_animation.py, summarized as violins instead of animated one frame at a time, so the two slides compare display types on identical data (Hullman, Resnick & Adar 2015, doi:10.1371/journal.pone.0142444).

This script was substantially drafted by an LLM coding system
"""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from make_hops_animation import (
    BORDER,
    DPI,
    HEIGHT_PX,
    INK,
    N_FRAMES,
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
from make_summary_plots import STOP_COLORS, sample_title

OUT_PATH = OUT_DIR / "violin-ridership-ordering.png"


def main() -> None:
    family = _use_repo_font()
    if family:
        plt.rcParams["font.family"] = family

    paired = load_paired_weekdays()
    a_name, b_name = STOPS[0][0], STOPS[1][0]

    # Same draw as the HOP, so both slides show the same weekdays.
    rng = np.random.default_rng(SEED)
    idx = rng.choice(len(paired), size=N_FRAMES, replace=False)
    sample = paired[idx]
    values = np.column_stack(
        [sample[a_name].to_numpy(), sample[b_name].to_numpy()]
    ).astype(float)

    y_min = 0.0
    y_max = 100.0 * np.ceil(1.1 * values.max() / 100.0)

    fig, ax = plt.subplots(figsize=(WIDTH_PX / DPI, HEIGHT_PX / DPI), dpi=DPI)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)

    parts = ax.violinplot(
        [values[:, 0], values[:, 1]],
        positions=X_POS,
        widths=0.52,
        showmedians=True,
        showextrema=False,
    )
    for body, color in zip(parts["bodies"], STOP_COLORS):
        body.set_facecolor(color)
        body.set_edgecolor(color)
        body.set_alpha(0.55)
    parts["cmedians"].set_color(INK)
    parts["cmedians"].set_linewidth(2.5)

    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(X_POS)
    ax.set_xticklabels([label for _, label in STOPS], fontsize=17, color=INK)
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

    ax.set_title(
        sample_title(sample["date"]),
        fontsize=19,
        color=INK,
        pad=42,
        loc="left",
    )

    fig.tight_layout()
    fig.savefig(OUT_PATH, dpi=DPI, facecolor=PAPER)
    plt.close(fig)

    medians = np.median(values, axis=0)
    print(f"wrote {OUT_PATH.relative_to(REPO_ROOT)}")
    print(f"  medians: {STOPS[0][1]} {medians[0]:.0f}, {STOPS[1][1]} {medians[1]:.0f}")


if __name__ == "__main__":
    main()
