# SVG Tracing Notes for `orange-line-stops-unlabeled-manual-rotated.png`

Two prior attempts failed to produce an accurate trace. These notes document what was learned so the next attempt starts with correct data.

## Orange Line file inventory

| File | Source | Purpose |
|---|---|---|
| `Chicago_Orange_line.png` | Existing CTA Orange Line reference image, 378 × 1436 PNG. | Tall source/reference map used while collecting Orange Line visual assets. |
| `OrangeLine.jpg` | Existing Orange Line reference image, 800 × 191 JPEG. | Wide source/reference image for Orange Line appearance and proportions. |
| `orangelin.jpeg` | Existing Orange Line reference image, 759 × 372 JPEG. | Additional source/reference image for Orange Line appearance. |
| `orange-line-stops.png` | Manually prepared raster asset, 933 × 1492 RGBA PNG. | Earlier stop/line composite before the final rotated tracing target. |
| `orange-line-stops-unlabeled-manual.png` | Manual edit derived from the stop/line raster, 933 × 1492 RGBA PNG. | Unlabeled working raster with station markers, before rotation. |
| `orange-line-stops-unlabeled-manual-rotated.png` | Rotated version of `orange-line-stops-unlabeled-manual.png`, 1492 × 933 RGBA PNG. | Primary tracing source for the current SVG geometry and station coordinates. |
| `orange-line-trace.svg` | Generated trace attempt derived from `orange-line-stops-unlabeled-manual-rotated.png`. | Earlier full SVG trace with orange line and station circles; useful as a comparison/reference, not the current schedule background. |
| `orange-line-trace-gpt5.svg` | Generated GPT-5 trace attempt. | Experimental trace variant; not used by the index page. |
| `orange-trace-june4.svg` | June 4 generated/edited SVG trace. | Intermediate cleaned trace retaining line and station overlays. |
| `orange-line-trace-line-only.svg` | Pixelmator-exported SVG, then manually edited. | Current line-only SVG used as the Schedule background on `docs/index.html`; station markers are overlaid in HTML/CSS. |
| `stop-airport.png` | Existing 20 × 20 grayscale stop icon asset. | Airport stop icon reference/overlay asset. |
| `stop-isa.png` | Existing 21 × 21 grayscale stop icon asset. | Accessible station icon reference/overlay asset. |
| `stop-park.png` | Existing 21 × 21 grayscale stop icon asset. | Parking stop icon reference/overlay asset. |

## Critical facts

- **Image size**: 1492 × 933 px, **RGBA with fully transparent background** (alpha = 0). Never load as RGB — transparent pixels become `(0,0,0)` (black), making black-detection wrong. Use `Image.open(...).convert("RGBA")` throughout.
- **Orange color**: `#FF6115` (R=255, G=97, B=21). Detection mask: `(A>200) & (R>200) & (G>50) & (G<160) & (B<60)`.
- **Stroke width**: exactly **30 px** (measured on clean straight segments: loop top and loop right side both read 30–31 px).

## The S-curve is NOT a function of x — this broke the first SVG

At x = 245–265 the orange line exists at **three distinct y-bands simultaneously** (the path passes through the same x-value three times). Scanning horizontal slices and taking a single centerline y per x completely misses this; the resulting spline "shortcuts" the S-curve and is visually wrong. You must parameterize by arc length, not x.

```
x=250: 3 bands → y≈203 (top arm), y≈286 (mid arm), y≈367 (bottom arm)
```

Stations at `(254, 242)` and `(254, 329)` are on the top and bottom arms of the S.

## Recommended tracing approach

1. Build the orange mask (RGBA, as above).
2. Run `skimage.morphology.skeletonize` on the filled orange mask (`scipy.ndimage.binary_fill_holes` first).
3. **BFS/DFS trace from the left terminus** (~84, 90) along skeleton connectivity — do NOT use Douglas-Peucker with epsilon > 1 or the S-curve detail is lost.
4. Sample the skeleton trace every ~5 skeleton pixels to produce 150–200 waypoints.
5. Fit a `scipy.interpolate.CubicSpline` using **chord-length parameterization** (not index-based).
6. Convert to SVG cubic Bézier segments using tangent-derived control points.

## Exact loop geometry (measured from pixel scans)

| Segment | Coordinate |
|---|---|
| Bottom (stem + loop floor) | y = 607.5, x ≈ 84 → 1309 |
| Left side | x = 999, y ≈ 344 → 607 |
| Top | y = 344.5, x ≈ 999 → 1309 |
| Right side | x = 1309, y ≈ 344 → 607 |

T-junction: the main diagonal arrives at the loop floor (~x=797, y=607.5); draw as two overlapping stroked paths — one for the main diagonal + floor, one for the three remaining loop sides (left + top + right).

## Circle classification (18 total; background is transparent, not white)

- **12 white-filled** (no ring): `fill="white"`, r = 11 px. Positions: `(87,90) (209,148) (254,242) (254,329) (486,430) (594,504) (704,580) (998,458) (999,403) (1060,344) (1204,607) (1309,471)`.
- **6 black-ring**: draw as two stacked circles — black outer (r=19) then white inner (r=13). Positions: `(834,607) (1000,537) (1076,606) (1204,343) (1310,400) (1310,538)`.
- Detection: a circle is "black-ring" if >20 actual black pixels (A>200, R<40, G<40, B<40) exist in the annulus r=14–22 around its centre.

## Verification step (do not skip)

After writing the SVG, render it with `cairosvg` to a PNG at the same 1492×933 resolution, then compute the **Chamfer / pixel-distance error** between the original orange mask and the SVG orange mask. Target: mean distance < 3 px everywhere. If the S-curve region shows error > 5 px, add more skeleton waypoints in that zone.
