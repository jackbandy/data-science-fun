# Sources

## Piecharts.svg

- **File:** `Piecharts.svg`
- **Origin:** Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Piecharts.svg
- **Direct URL:** https://upload.wikimedia.org/wikipedia/commons/b/b4/Piecharts.svg
- **Author:** User:Schutz
- **Date:** 2008-08-28
- **License:** [Creative Commons Attribution 1.0 Generic (CC BY 1.0)](https://creativecommons.org/licenses/by/1.0/)
- **Description:** Three pairs of pie chart and bar chart panels (A, B, C) showing identical data in each form, illustrating that bar charts make relative magnitudes easier to read than pie charts. Created in R, converted from PostScript via pstoedit, refined in Inkscape.

## misleading-macworld-3d-pie-chart.svg

- **File:** `misleading-macworld-3d-pie-chart.svg`
- **Origin:** Wikimedia Commons — https://commons.wikimedia.org/wiki/File:Misleading_macworld_3d_pie_chart.svg
- **Direct URL:** https://upload.wikimedia.org/wikipedia/commons/d/db/Misleading_macworld_3d_pie_chart.svg
- **Author:** User:Cmglee (CMG Lee)
- **License:** [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0)
- **Description:** Two stacked panels of the same US smartphone market share data (RIM 39.0%, Other 21.2%, Apple 19.5%, Palm 9.8%, Motorola 7.4%, Nokia 3.1%). The top panel redraws the 3D perspective pie chart presented at Macworld 2008 (−30° x-rotation, 40% perspective, in LibreOffice Calc); the bottom panel is the same data as a flat 2D pie. Uploader's source for the original: Edward Tufte's notebook, https://www.edwardtufte.com/notebook/pie-charts/.
- **Note:** ShareAlike — if this file is modified or remixed, the derivative must also be CC BY-SA 4.0. Used unmodified here.

## dsc_0143.jpg

- **File:** `dsc_0143.jpg` (440 × 292)
- **Origin:** "The chart-junk of Steve Jobs," Paragraft, 2008-06-03 — https://paragraft.wordpress.com/2008/06/03/the-chart-junk-of-steve-jobs/
- **Description:** Keynote photo of Steve Jobs beside the "U.S. SmartPhone Marketshare" 3D pie chart (RIM 39.0%, Other 21.2%, Apple 19.5%, Palm 9.8%, Motorola 7.4%, Nokia 3.1%) — the slide redrawn in `misleading-macworld-3d-pie-chart.svg` above. The post's point: perspective puts Apple's wedge nearest the viewer, so 19.5% occupies more visible area than the 21.2% "Other" wedge behind it.
- **Photo credit:** The frame carries an Engadget watermark, so the photograph is from Engadget's keynote coverage; the Paragraft post reproduces it without a credit line. The post itself says it found the chart via a discussion on Edward Tufte's forum.
- **License:** Not stated by either the blog post or the watermark. Treat as all-rights-reserved press photography; used here as commentary/criticism of the chart it depicts.

## dsc_0143-golden.png

- **File:** `dsc_0143-golden.png` (1618 × 1000, ratio 1.618 — golden rectangle)
- **Derived from:** `dsc_0143.jpg` above
- **License:** Inherits the unstated status of the original; same commentary use.
- **Description:** Upscaled crop for slide use. Cropped to 440 × 272 (14 px off the top, 6 px off the bottom, no horizontal crop) to reach the golden ratio, then resized ~3.7× with a Lanczos filter and lightly unsharp-masked. Nothing in the chart is redrawn or restyled. Regenerate with:

  ```sh
  magick dsc_0143.jpg -crop 440x272+0+14 +repage \
    -colorspace RGB -filter Lanczos -resize 1618x1000! -colorspace sRGB \
    -unsharp 0x1.0+0.6+0.02 dsc_0143-golden.png
  ```

## macworld-pie-3d.svg and macworld-pie-2d.svg

- **Files:** `macworld-pie-3d.svg` (top panel), `macworld-pie-2d.svg` (bottom panel)
- **Derived from:** `misleading-macworld-3d-pie-chart.svg` above, by `split_macworld_chart.py`
- **Author of the original:** User:Cmglee (CMG Lee)
- **License:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) — ShareAlike, inherited from the original, since these are derivative works
- **Description:** The two panels of the comparison as separate files, so slides can place them side by side instead of stacked. Each keeps its own viewBox and the original's margins; nothing is redrawn or restyled. Regenerate with `python3 split_macworld_chart.py`.
