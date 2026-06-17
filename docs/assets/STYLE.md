# Style Guide — `data-adventures` assets

> _Note: this guide was partly drafted/edited with an LLM._

Visual conventions for figures, diagrams, and slide assets. Mirrors the guide in
`ethical-issues-in-computing-fall-2025-uic`; the repos differ mainly in palette
(oranges here, blues there) and transit motif.

## Colors

From `docs/slides/theme/uic-orange-reveal.scss`. Orange = brand accent; rest is neutral.

- `#f9461c` — orange (brand / links) · `$orange`
- `#c83214` — orange dark (hover / emphasis) · `$orange-dark`
- `#1a1a1a` — ink (headings, strong text) · `$ink`
- `#444` — body text · `$text`
- `#565a5c` — steel · `$steel`
- `#777` — muted · `$muted`
- `#aaa` — quiet · `$quiet`
- `#fff` — paper / background · `$paper`
- `#f4f4f2` — soft gray (code/panels) · `$soft-gray`
- `#ddd` — border · `$border`

Figures:
- default to grayscale neutrals; orange only as an accent on the focal element
- diagram primitives: stroke/text `#111111`, neutral fill `#EEEEEE`, highlight fill `#222222` with `#FFFFFF` text, white background

## Golden-ratio figures

- lay figures out in a golden-ratio rectangle when content allows
- `PHI = (1 + 5**0.5) / 2`; derive short side from long, e.g. 1000 × 618 (`round(WIDTH / PHI)`)
- see `lifecycle/make_lifecycle_figures.py`

## Arrows

Defaults from `lifecycle/ds-lifecycle-v*.svg`:
- color `#111111`; weight `stroke-width="3"`
- arrowhead: filled triangle marker (`M 0 0 L 5 2.5 L 0 5 z`), size ≈ 5, `markerUnits="strokeWidth"`, `orient="auto"`, refX/refY centered
- shaft ends ~4px short of the node (small gap, not touching)
- entry / external arrows: dashed shaft `stroke-dasharray="9 8"`, same weight + head
- curved edges = cubic Béziers, same stroke; parallel arrows into one target fanned apart

## Fonts

- titles/headings: Big Shoulders (`"Big Shoulders", "Arial Narrow", Arial, sans-serif`)
- body: `"ITC Franklin Gothic", "Libre Franklin", …` (Libre Franklin = self-hosted OFL fallback)
- code: `Courier, "Courier New", monospace`
- figures: Libre Franklin, embedded in the SVG; headings 700, text 400

## Other norms

- **SVG-first** — diagrams are vector; raster only for photos/source imagery
- **Self-hosted embedded fonts** — fonts in `assets/fonts/` (OFL, with `OFL.txt`), never a CDN; standalone SVGs embed a base64 `woff2` data URL
- **`SOURCES.md` per folder** — any dir with third-party/remixed material lists each file's source + license
- **Rounded-rect nodes** — `rx="6"`, 3px stroke, neutral fill, centered multi-line text
- **Generated variant sets** — step figures come from a Python generator emitting numbered variants (`v0` plain, `v1…vN` each highlighting one step); keep the script as source of truth
- **Orange-line transit motif** — Chicago / CTA Orange Line is the recurring theme
