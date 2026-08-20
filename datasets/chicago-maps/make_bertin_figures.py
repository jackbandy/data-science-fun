"""Render the three Bertin visual-variable maps used in the Week 4 slide deck.

NOTICE: this script was substantially generated with an LLM coding tool. It is
maintained, reviewed, and vetted by humans.

Reads the map data next to this script and writes, into docs/assets/bertin-maps/
so the deck can publish them (Jekyll builds from docs/, so anything under
datasets/ never reaches the site):

    bertin-texture.svg   land coarse / water fine, black and white only
    bertin-color.svg     the same two areas separated by hue alone
    bertin-value.svg     the 50 wards shaded by median household income

Each figure is a golden-ratio portrait frame (1 : 1.618). The map's own extent
is stretched north and south to that ratio so the drawing fills the frame
rather than sitting in a letterbox -- the city keeps its full width and gains
lake and margin above and below.

Run from anywhere:  python3 datasets/chicago-maps/make_bertin_figures.py
"""

import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon as MplPolygon

HERE = Path(__file__).resolve().parent
OUT = HERE.parent.parent / "docs" / "assets" / "bertin-maps"

INK = "#1a1a1a"
TEAL = "#1f8a9b"
SAND = "#efe7d8"

PHI = 1.618033988749895
FIG_W = 4.0
FIG_H = FIG_W * PHI

# The city plus the near-shore strip of Lake Michigan.
XLIM = (-87.95, -87.505)
ASPECT = 1 / 0.745  # Mercator correction at ~41.9 degrees north
Y_MID = 41.83
# Solve for the y-span that makes the drawn map exactly phi tall:
#   display_height / display_width = ASPECT * yspan / xspan
Y_SPAN = PHI * (XLIM[1] - XLIM[0]) / ASPECT
YLIM = (Y_MID - Y_SPAN / 2, Y_MID + Y_SPAN / 2)

plt.rcParams["hatch.linewidth"] = 0.5


def _thin(ring, tol):
    """Drop points closer than `tol` degrees to the last one kept.

    The city files are surveyor-accurate; at slide size that detail is invisible
    but it inflates the SVG, so every ring is decimated on load.
    """
    out = [ring[0]]
    for x, y in ring[1:-1]:
        px, py = out[-1]
        if abs(x - px) > tol or abs(y - py) > tol:
            out.append((x, y))
    out.append(ring[0])
    return out if len(out) > 3 else ring


def rings(name, tol=0.0009):
    """(properties, exterior ring) for every polygon in a GeoJSON file."""
    out = []
    for f in json.loads((HERE / name).read_text())["features"]:
        g = f["geometry"]
        polys = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"]
        for p in polys:
            out.append((f["properties"], _thin([tuple(c) for c in p[0]], tol)))
    return out


CITY = rings("chicago-city.geojson")
WARDS = rings("chicago-wards.geojson")
# Keep the lake, the river, the canals and the harbors; drop the retention ponds.
WATER = [(p, r) for p, r in rings("chicago-water.geojson")
         if int(p["AREAWATER"]) >= 250_000]
INCOME = {int(r["ward"]): int(r["median_household_income_est"])
          for r in csv.DictReader((HERE / "chicago-ward-income.csv").open())}


def frame():
    """A golden-ratio portrait figure whose axes fill it edge to edge."""
    fig = plt.figure(figsize=(FIG_W, FIG_H))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set(xlim=XLIM, ylim=YLIM)
    ax.set_aspect(ASPECT)
    ax.axis("off")
    return fig, ax


def layer(ax, shapes, **kw):
    ax.add_collection(PatchCollection([MplPolygon(r) for _, r in shapes], **kw))


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / name
    fig.savefig(out, format="svg", transparent=False, facecolor="white")
    plt.close(fig)
    print(f"wrote {out.relative_to(HERE.parent.parent)}")


def texture():
    """Grain alone: the amount of black is constant, only the scale changes."""
    fig, ax = frame()
    layer(ax, CITY, facecolor="white", edgecolor=INK, lw=0.8, hatch="..")
    layer(ax, WATER, facecolor="white", edgecolor=INK, lw=0.3, hatch="......")
    save(fig, "bertin-texture.svg")


def color():
    """Hue alone, at a fixed lightness: identity, not magnitude."""
    fig, ax = frame()
    layer(ax, CITY, facecolor=SAND, edgecolor=INK, lw=0.8)
    layer(ax, WATER, facecolor=TEAL, edgecolor="none")
    save(fig, "bertin-color.svg")


def value():
    """Lightness alone: ordered, so darker reads as more."""
    fig, ax = frame()
    vals = [INCOME[int(p["ward"])] for p, _ in WARDS]
    pc = PatchCollection([MplPolygon(r) for _, r in WARDS],
                         edgecolor="white", lw=0.5, cmap="Greys")
    pc.set_array(np.array(vals))
    pc.set_clim(30_000, 190_000)
    ax.add_collection(pc)

    cax = fig.add_axes([0.87, 0.30, 0.028, 0.22])
    cb = fig.colorbar(pc, cax=cax)
    cb.set_ticks([50_000, 100_000, 150_000])
    cb.set_ticklabels(["$50k", "$100k", "$150k"])
    cb.ax.tick_params(labelsize=7, length=2)
    cb.outline.set_visible(False)
    save(fig, "bertin-value.svg")


if __name__ == "__main__":
    texture()
    color()
    value()
