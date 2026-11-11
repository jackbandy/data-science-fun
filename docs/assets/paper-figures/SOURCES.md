# Paper Figures — Attribution and Licensing

Figures cropped from published/preprint papers, for use in slides. One entry per
source paper; filenames follow `<first-author>-et-al-<venue>-<year>-fig<n><panel>`.

> _Note: this file was drafted with an LLM._

## Huszár et al., "Algorithmic Amplification of Politics on Twitter"

- Ferenc Huszár, Sofia Ira Ktena, Conor O'Brien, Luca Belli, Andrew Schlaikjer,
  Moritz Hardt
- *Proceedings of the National Academy of Sciences* 119(1), e2025334119 (2022;
  published online 21 Dec 2021) — [doi:10.1073/pnas.2025334119](https://doi.org/10.1073/pnas.2025334119)
- BibTeX key in `docs/slides/shared/references.bib`: `huszar2022`

### Files

All three panels were rendered at 600 dpi from **page 4 of the arXiv preprint**
([arXiv:2110.11010v1](https://arxiv.org/abs/2110.11010), 21 Oct 2021) and cropped
with ImageMagick. The preprint's Figure 1 is the same three-panel figure as the
published version; the preprint was used because the PNAS and PMC copies are not
machine-retrievable. Preprint is under the
[arXiv non-exclusive distribution license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/);
the PNAS version of record is CC BY-NC-ND.

1. **huszar-et-al-pnas-2021-fig1a.png** — Fig. 1A: group amplification of each
   major political party across 7 countries, parties ordered left-to-right by
   2019 Chapel Hill Expert Survey ideology score.
2. **huszar-et-al-pnas-2021-fig1b.png** — Fig. 1B: pairwise comparison of the
   largest mainstream left- vs. right-wing party in each country, against the
   equal-amplification diagonal.
3. **huszar-et-al-pnas-2021-fig1c.png** — Fig. 1C: violin plots of *individual*
   politician amplification, US House / US Senate / UK Commons / CA Commons.

## Padilla et al., "Effects of Ensemble and Summary Displays on Interpretations of Geospatial Uncertainty Data"

- Lace M. Padilla, Ian T. Ruginski, Sarah H. Creem-Regehr
- *Cognitive Research: Principles and Implications* 2(1), 40 (2017) —
  [doi:10.1186/s41235-017-0076-1](https://doi.org/10.1186/s41235-017-0076-1)
- BibTeX key in `docs/slides/shared/references.bib`: `padilla2017ensemble`
- Licensed **CC BY 4.0** (version of record), so these are redistributable with
  attribution. Downloaded at published resolution from the SpringerOpen article;
  no rescaling other than the panel crop noted below.

### Files

1. **padilla-et-al-cogres-2017-fig1.png** — Fig. 1: the National Hurricane
   Center's "cone of uncertainty" track forecast for Hurricane Gustav, 5 PM EDT
   30 Aug 2008 (NWS/TPC Advisory 25). The underlying NHC graphic is a US
   government work in the public domain.
2. **padilla-et-al-cogres-2017-fig2.png** — Fig. 2: four-panel comparison of
   summary displays (a, c — cone) against ensemble displays (b, d — individual
   forecast tracks), for two different storm scenarios.
3. **padilla-et-al-cogres-2017-fig2b.png** — Fig. 2, panel *b* only, cropped
   with ImageMagick for use on a slide where only the ensemble ("spaghetti")
   display is being shown.

## Hullman, Resnick & Adar, "Hypothetical Outcome Plots Outperform Error Bars and Violin Plots…"

- Jessica Hullman, Paul Resnick, Eytan Adar
- *PLOS ONE* 10(11), e0142444 (2015) —
  [doi:10.1371/journal.pone.0142444](https://doi.org/10.1371/journal.pone.0142444)
- BibTeX key in `docs/slides/shared/references.bib`: `hullman2015hops`
- Licensed **CC BY 4.0**, so redistributable with attribution. Downloaded at
  "large" size from the PLOS figure endpoint; not otherwise modified.

### Files

1. **hullman-et-al-plosone-2015-fig2.png** — Fig. 2: the same distribution shown
   three ways — error bars, a violin plot, and selected frames of a Hypothetical
   Outcome Plot (HOP), which animates draws from the distribution instead of
   summarizing it.

## Strömberg, Lei & Wu, "The Generative AI Learning Penalty: Evidence from Chinese Secondary Education"

- David Strömberg (Stockholm University), Victor Lei (University of Hong Kong),
  Yanhui Wu (University of Hong Kong)
- Working paper, June 2026 — https://dx.doi.org/10.2139/ssrn.6868618

### Files

All 24 figures were extracted as **vector SVG** by rendering the relevant PDF
page with `pdftocairo -svg` and then rewriting the SVG `viewBox` to crop to the
figure region. The PDF's figures are TikZ/pgfplots output (vector); `pdfimages`
only recovers a single embedded raster, so the SVG route is the only way to keep
them sharp at slide resolution. Previews were rendered with `rsvg-convert`.


## Galton, "Vox Populi"

- Francis Galton
- *Nature* 75(1949), 450–451 (7 March 1907) — [doi:10.1038/075450a0](https://doi.org/10.1038/075450a0)
- BibTeX key in `docs/slides/shared/references.bib`: `galton1907`
- Public domain (published 1907).

### Files

1. **galton-nature-1907-p450.png** — page 450, rendered at 150 dpi with `pdftoppm -f 1 -l 1 -r 150` from the scan at <https://galton.org/essays/1900-1911/galton-1907-vox-populi.pdf>; not otherwise modified. The left column's top half is the end of an unrelated article. (Drafted by an LLM coding system and has not yet been reviewed.)

## Granovetter, "The Strength of Weak Ties"

- Mark S. Granovetter (Johns Hopkins University)
- *American Journal of Sociology* 78(6), 1360–1380 (May 1973) — [doi:10.1086/225469](https://doi.org/10.1086/225469)
- BibTeX key in `docs/slides/shared/references.bib`: `granovetter1973`
- © 1973 University of Chicago Press; first page shown in class for commentary.

### Files

1. **granovetter-ajs-1973-p1360.png** — first page of the article (page 1360), rendered at 150 dpi with `pdftoppm -f 2 -l 2 -r 150` (PDF page 1 is a JSTOR cover sheet) from the copy at <https://snap.stanford.edu/class/cs224w-readings/granovetter73weakties.pdf>; not otherwise modified. (Drafted by an LLM coding system and has not yet been reviewed.)
