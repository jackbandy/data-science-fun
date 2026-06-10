#!/usr/bin/env python3
# This file was modified by an LLM coding tool.
"""
Generate progressive DIKW pyramid SVG variants from dikw-pyramid-fonts-v2.svg.

Outputs (same directory):
  01-dikw-pyramid-blank.svg
  02-dikw-pyramid-divided.svg
  03-dikw-pyramid-data.svg
  04-dikw-pyramid-data-info.svg
  05-dikw-pyramid-data-info-knowledge.svg
  06-dikw-pyramid-full.svg

Fonts are subsetted to only the glyphs each file actually uses.
Requires: fonttools  (pip install fonttools)
"""

import base64
import io
import os
import re

from fontTools import subset as ft_subset
from fontTools.ttLib import TTFont

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(SCRIPT_DIR, "dikw-pyramid-fonts-v2.svg")

with open(SOURCE) as f:
    src = f.read()

lines = src.splitlines()

# ── Section extraction ─────────────────────────────────────────────────────────

def find_comment(comment):
    for i, line in enumerate(lines):
        if f"<!-- {comment} -->" in line:
            return i
    raise ValueError(f"Comment not found: {comment!r}")

def get_section_lines(comment):
    """Return the comment line + all immediately following non-blank non-comment lines."""
    start = find_comment(comment)
    end = start + 1
    while end < len(lines) and lines[end].strip() and "<!--" not in lines[end]:
        end += 1
    return lines[start:end]

# ── Font subsetting ────────────────────────────────────────────────────────────

def extract_font(family):
    """Return (mime_prefix, base64_data) for a @font-face block in the source SVG."""
    pat = rf"font-family: '{re.escape(family)}';\s+src: url\('(data:font/[^;]+);base64,([^']+)'\)"
    m = re.search(pat, src, re.DOTALL)
    if not m:
        raise ValueError(f"Font {family!r} not found in source")
    return m.group(1), m.group(2)

def make_font_face(family, text):
    """Return an @font-face block with the font subsetted to only the glyphs in text."""
    mime, b64 = extract_font(family)
    font_bytes = base64.b64decode(b64)

    font = TTFont(io.BytesIO(font_bytes))
    options = ft_subset.Options()
    options.layout_features = ["*"]
    options.ignore_missing_glyphs = True
    subsetter = ft_subset.Subsetter(options)
    subsetter.populate(text=text)
    subsetter.subset(font)

    out = io.BytesIO()
    font.save(out)
    subsetted_b64 = base64.b64encode(out.getvalue()).decode("ascii")

    return (
        f"      @font-face {{\n"
        f"        font-family: '{family}';\n"
        f"        src: url('{mime};base64,{subsetted_b64}');\n"
        f"      }}"
    )

CSS_CLASSES = """\
      .lbl-data   { font-family: 'BPdots', 'Courier New', monospace; font-size: 78px; letter-spacing: 2px; }
      .lbl-info   { font-family: 'VT323', 'Courier New', monospace; font-size: 95px; }
      .lbl-know   { font-family: 'Noteworthy', 'Chalkboard SE', cursive; font-size: 61px; }
      .lbl-wisdom { font-family: 'Arial Black', Arial, sans-serif; font-size: 74px; font-weight: 900; font-style: italic; }"""

# Precompute — each embedded font only ever covers one word
print("Subsetting fonts…")
FONT_BPDOTS = make_font_face("BPdots", "data")   # d, a, t
FONT_VT323  = make_font_face("VT323",  "info")   # i, n, f, o
print("  done\n")

# ── SVG building blocks ────────────────────────────────────────────────────────

SVG_OPEN = lines[0]
RECT_BG  = "  <rect width=\"100%\" height=\"100%\" fill=\"white\" />"

DIV_SIDE  = get_section_lines("Layer division lines: side face")
DIV_FRONT = get_section_lines("Layer division lines: front face")
OUTLINE   = get_section_lines("Pyramid outline")

# [1:] strips the comment line; entries are ordered data → info → knowledge → wisdom
CONNECTORS = get_section_lines("Dashed connectors from labels to layers")[1:]
LABELS     = get_section_lines("Layer labels")[1:]

# Which embedded @font-face block each layer needs (None = system font only)
LAYER_FONTS = [FONT_BPDOTS, FONT_VT323, None, None]

# ── Assembly ───────────────────────────────────────────────────────────────────

def make_svg(include_divisions, n_labels):
    font_blocks = [f for f in LAYER_FONTS[:n_labels] if f is not None]
    style_inner = "\n".join(font_blocks + [CSS_CLASSES])
    defs = f"  <defs>\n    <style>\n{style_inner}\n    </style>\n  </defs>"

    out = [SVG_OPEN, defs, "", RECT_BG]

    if include_divisions:
        out += ["", "\n".join(DIV_SIDE), "", "\n".join(DIV_FRONT)]

    out += ["", "\n".join(OUTLINE)]

    if n_labels > 0:
        out += [
            "",
            "  <!-- Dashed connectors from labels to layers -->",
            *CONNECTORS[:n_labels],
            "",
            "  <!-- Layer labels -->",
            *LABELS[:n_labels],
        ]

    out += ["", "</svg>"]
    return "\n".join(out) + "\n"

# ── Generate files ─────────────────────────────────────────────────────────────

VARIANTS = [
    ("01-dikw-pyramid-blank.svg",                   False, 0),
    ("02-dikw-pyramid-divided.svg",                 True,  0),
    ("03-dikw-pyramid-data.svg",                    True,  1),
    ("04-dikw-pyramid-data-info.svg",               True,  2),
    ("05-dikw-pyramid-data-info-knowledge.svg",     True,  3),
    ("06-dikw-pyramid-full.svg",                    True,  4),
]

for filename, div, n in VARIANTS:
    path = os.path.join(SCRIPT_DIR, filename)
    content = make_svg(div, n)
    with open(path, "w") as f:
        f.write(content)
    size_kb = os.path.getsize(path) / 1024
    print(f"  {filename}  ({size_kb:.0f} KB)")

print("\nDone.")
