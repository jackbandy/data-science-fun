"""Slide SVGs of the CS 418 Fall 2026 class estimates (vox classis), with and without the actual values.

NOTICE: this file was drafted by an LLM coding system and has not yet been reviewed. Check every figure against the slide it illustrates.

The drawing code lives in datasets/galton-vox-populi-1907/vox-classis/plot-estimates.py, which also writes the README's PNGs; this script imports it, swaps in the STYLE.md palette and vendored Libre Franklin (drawn as paths so each SVG is self-contained), and writes SVGs here. Dot positions can differ slightly from the PNGs.

Usage:  docs/slides/.venv/bin/python3 make_vox_classis_figures.py
"""

import importlib.util
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib import font_manager

OUT_DIR = Path(__file__).resolve().parent
REPO_ROOT = OUT_DIR.parents[2]
SCRIPT = REPO_ROOT / "datasets" / "galton-vox-populi-1907" / "vox-classis" / "plot-estimates.py"
FONT_PATH = OUT_DIR.parent / "fonts" / "libre-franklin" / "LibreFranklin-Regular.ttf"

spec = importlib.util.spec_from_file_location("plot_estimates", SCRIPT)
pe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pe)

# STYLE.md palette; plot() reads these module globals at call time.
pe.SURFACE = "#FFFFFF"
pe.INK = "#1A1A1A"
pe.INK_2 = "#565A5C"
pe.MUTED = "#777777"
pe.GRID = "#DDDDDD"

font_manager.fontManager.addfont(str(FONT_PATH))
plt.rcParams["font.family"] = font_manager.FontProperties(fname=str(FONT_PATH)).get_name()
plt.rcParams["svg.fonttype"] = "path"

turnout, uic, cta = pe.PLOTS
# Same call order as plot-estimates.py, so the shared jitter RNG is consumed the same way.
pe.plot(*turnout, out_name=OUT_DIR / "vox-classis-turnout.svg")
pe.plot(*uic, out_name=OUT_DIR / "vox-classis-uic-halsted.svg")
pe.plot(*cta, out_name=OUT_DIR / "vox-classis-cta-rail.svg")
pe.plot(*turnout, actual=pe.turnout_range(), out_name=OUT_DIR / "vox-classis-turnout-actual.svg")
results = pe.pd.read_csv(pe.HERE / "results.csv").set_index(["year", "measure"])["value"]
rides = results[2026, "uic_halsted_rides_2026_08_25"]
pe.plot(*uic, actual={"value": rides, "label": f"actual: {rides:,.0f} rides"}, out_name=OUT_DIR / "vox-classis-uic-halsted-actual.svg")
