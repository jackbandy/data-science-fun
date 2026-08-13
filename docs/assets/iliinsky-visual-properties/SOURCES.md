# Sources — `iliinsky-visual-properties`

> _Note: this file was drafted by an LLM._

- `visualpropertiestable2.gif` — third-party raster: Noah Iliinsky, "Properties
  and Best Uses of Visual Encodings," complexdiagrams.com/properties, June 2012.
  Found via Ken Flerlage's ["Revisiting Tableau Desktop
  Fundamentals"](https://datavizblog.com/2017/06/13/revisiting-tableau-desktop-fundamentals/)
  (DataVizBlog, 13 June 2017). The image carries a **CC BY-SA** badge; the badge
  does not state a version, so treat it as BY-SA generally and attribute
  Iliinsky. Kept as the reference for the redraw.
- `iliinsky-visual-properties.svg` — redrawn in this repo by
  `make_iliinsky_visual_properties_figure.py`. **This is a derivative of a
  CC BY-SA work**: the same fifteen encodings, same four data-type columns, and
  the same "Good" judgements as the source, re-laid-out on the repo's
  1000 × 618 golden-ratio canvas with the repo's fonts. It therefore carries
  attribution in the figure's own bottom margin and must stay under the same
  share-alike terms — keep the credit line if you reuse or modify it.

  Deliberate departures from the source, none of which change its claims:
  - the four data-type columns use a filled dot rather than sixty repetitions of
    the word "Good" — a dot matrix can be scanned down a column, the word can't;
  - example marks are drawn in the repo accent orange (`#F9461C`) instead of the
    source's blue, with everything else neutral, per `../STYLE.md`; the "color"
    row uses three CTA route colors;
  - the "weight, boldness" example shows actual type weights, which is what the
    row names, rather than reusing the line-weight example as the source does.

Fonts are read from `../fonts/` at build time and embedded in the SVG as base64
woff2, so nothing here needs a local copy: Big Shoulders sets the title and
Libre Franklin the table, per `../STYLE.md`. Both are SIL Open Font License 1.1
(see the `OFL.txt` beside each).
