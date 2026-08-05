# Slide Check Template

A pass to run over each week's slide deck

---

## 1. Structure

- [ ] **Day 2 marker present.** Each deck that spans two class meetings needs a `# Week N, Day 2` divider so the second session has an obvious starting point.
- [ ] **Day 1 title slide** carries `.course-title .photo-title` and a `background-image`.
- [ ] **Sources slide exists** — one `{.sources}` heading per deck


## 2. Titles

- [ ] **Every `# ` title is unique.** Duplicates sometimes break quarto's slide compiler?
- [ ] **Title case is consistent** across the deck.
- [ ] **No title is too long**

## 3. Small text — captions, notes, eyebrows

The theme defines these; avoid inline `font-size`. See
`theme/uic-orange-reveal.scss`.

| Class | Use for |
|:--|:--|
| `.caption` | credit or source line under a figure (centered) |
| `.note` | aside or pointer to a reading (left-aligned, not under a figure) |
| `.eyebrow` | all-caps orange label above a block; add `.todo` for the boxed marker |
| `.dense` / `.dense-smaller` | shrinking body copy in tight tables and lists |

- [ ] **No stray inline `font-size`** outside deliberate display type (big stat
      numbers, hero text).
      ```sh
      grep -n 'font-size' weekN.md
      ```
- [ ] **Every figure has a credit** with attribution and license wherever appropriate.
- [ ] **Malformed `style="` attributes.** e.g. a missing opening quote renders as literal text on the slide and is easy to miss.

## 4. Placeholders

- [ ] **No `TK` or `TODO` left** in a deck that is about to be taught.
- [ ] **No empty caption blocks** — a `::: {.caption}` with nothing inside it leaves a gap under the figure.

## 5. Links and assets

- [ ] **All images resolve.**
- [ ] **External links work**, especially Wikimedia and DOI links in credits.
- [ ] **Cross-references to the book/syllabus** point at pages that exist.
- [ ] **Footer** names the right week and the right `dodatascience.fun/slides/weekN`

## 6. Render

- [ ] **Deck builds clean.**
      ```sh
      quarto render weekN.md --to revealjs
      ```
- [ ] **Click through in the browser** and watch for text spilling behind the footer, figures overflowing their column, and `.incremental` / `.fragment` blocks revealing in the intended order.
- [ ] **PDF export** bonus but not high-priority
