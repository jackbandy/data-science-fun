# Style Guide — `data-science-fun` assets

> _Note: this guide was partly drafted/edited with an LLM._

Visual conventions for figures, diagrams, and slide assets. Mirrors the guide in
`ethical-issues-in-computing-uic`; the repos differ mainly in palette
(oranges here, blues there) and transit motif.

## Colors

From `docs/slides/shared/theme/uic-orange-reveal.scss`. Orange = brand accent; rest is neutral.

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

## CTA branding

We follow the [CTA Trademark Guidelines for Developers](https://www.transitchicago.com/developers/branding/). The aesthetic is a **minimal** read of the CTA system: the official route color as a sparing accent, everything else neutral.

- **Official `'L'` route colors** — CTA explicitly encourages developers to use these "to help people immediately associate the output of your application with…the same visual cues." This repo's accent is the **Orange Line `#F9461C`** (matches `$orange` exactly). Full spec for reference: Red `#C60C30` · Blue `#00A1DE` · Brown `#62361B` · Green `#009B3A` · Orange `#F9461C` · Purple `#522398` · Pink `#E27EA6` · Yellow `#F9E300`; **Sign Grey `#565A5C`** (official neutral = our `$steel`).
- **No CTA logos or marks** — per the guidelines, "Don't use any CTA logo…or any approximations thereof" (incl. the CTA circle logo and text-based logos). Use route *colors* + an original transit motif only; never imply CTA affiliation. (Same disclaimer as the site FAQ.)
- **Minimal by default** — orange as an accent on the focal element; neutrals carry everything else.

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
- **og:image rasters** — social scrapers don't render SVG, so the homepage `og:image` (`assets/orange-line/orange-line-trace-with-stops.png`) is a PNG derived from the source SVG, which stays canonical: render at ~4× (`cairosvg --scale 4`), then `magick … -trim +repage -bordercolor none -border <~5% of long side> -strip -define png:compression-level=9` — trims transparent edges, re-adds an equal margin to keep the art centered, strips metadata, max-compresses; keep the transparent background
- **Self-hosted embedded fonts** — fonts in `assets/fonts/` (OFL, with `OFL.txt`), never a CDN; standalone SVGs embed a base64 `woff2` data URL
- **`SOURCES.md` per folder** — any dir with third-party/remixed material lists each file's source + license
- **Rounded-rect nodes** — `rx="6"`, 3px stroke, neutral fill, centered multi-line text
- **Generated variant sets** — step figures come from a Python generator emitting numbered variants (`v0` plain, `v1…vN` each highlighting one step); keep the script as source of truth
- **Orange-line transit motif** — Chicago / CTA Orange Line is the recurring theme
- **Direction chevrons on line traces** — travel-direction chevrons are identical mirrored marks (white, `stroke-width="9"`), centered on the line's stroke centerline (and on the loop axis where the trace loops); keep both arrows the same size and angle
