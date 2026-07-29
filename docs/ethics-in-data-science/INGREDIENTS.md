---
title: Ingredients
subtitle: Reusable formatting components for the Ethics in Data Science book
---

This page is a **style guide and component library** for the chapters in this book. Copy the source below. Use these canonical forms so formatting stays consistent.

> Convention note: chapters are processed by Quarto/Pandoc. That gives us YAML
> frontmatter, `::: {#fig-…}` figure divs, and `[@citekey]` citations on top of
> ordinary Markdown.

---

## Images & figures

All figures use a Quarto figure div with a stable `#fig-…` id (so they can be cross-referenced), a single `<img>` with the **canonical style string**, and a caption on its own line before the closing `:::`.

```markdown
::: {#fig-ingredient-pyramid}
<img src="../../assets/pyramid/dikw-pyramid-fonts.svg" alt="The DIKW pyramid with four labeled layers: data, information, knowledge, and wisdom." style="width: 100%; height: auto; border: 1px solid var(--bs-border-color);" />

The DIKW pyramid, labeled with four layers.
:::
```

Rules of thumb:

- Path is always `../../assets/<group>/<file>` (relative to the chapter file).
- Prefer `.svg` for diagrams; use `.png`/`.jpg` for photographs.
- The `style` attribute is fixed: `width: 100%; height: auto; border: 1px solid var(--bs-border-color);`. Add `padding: 10px;` only when an image needs breathing room inside the border.
- Always write meaningful `alt` text.
- The `#fig-…` id must be unique within the book.

For a plain image without a caption/border (rare), use a bare `<img>` or
standard Markdown:

```markdown
![Short alt text.](../../assets/group/file.svg)
```

### Linking to a downloadable asset (PDF, etc.)

```markdown
[Massachusetts printed schedule used in the 1790 census](../../assets/census/1790-massachusetts-printed-schedule.pdf).
```

---

## Tables

Pipe tables with a `| --- |` divider row. Use `<br>` to put multiple lines
inside a single cell, and leave a cell blank to visually group rows under the
one above.

```markdown
| Question Type | Description | Example | Answers |
| --- | --- | --- | --- |
| "Whether" | Presents a finite number of direct answers. | Was there a quorum at the meeting? | a. There was a quorum.<br>b. There was no quorum. |
|  |  | Does Alice live in Chicago or New York? | a. Alice lives in Chicago.<br>b. Alice lives in New York. |
| "Which" | Seeks a specific person, thing, or value. | Who was U.S. President in 1978? | a. Jimmy Carter |
```

A two-column mapping table (as used on the index page) follows the same form:

```markdown
| *Learning Data Science* | Corresponding material in this book |
| --- | --- |
| [1.1 Ask a Question](https://learningds.org/ch/01/lifecycle_cycle.html) | [Ethics in Asking Questions](02-ethics-in-asking-questions.md) |
```

---

## Lists

Unordered lists use `*`. Ordered lists use `1.` (let Markdown auto-number).
Citations can appear inline at the end of a list item.

```markdown
* Probability as long-run frequency across repeated trials
* Confidence intervals and p-values as long-run procedures
* The reference-class problem

1. Frame the question
2. Obtain the data
3. Understand the data and the world
```

Nested lists indent by four spaces:

```markdown
* Top-level item
    * Nested item
    * Nested item
```

---

## Blockquotes (epigraphs)

Chapters often open with a quotation followed by an attribution line that starts
with `--`, names the source in *italics*, and ends with a citation.

Only the quotation itself goes in the blockquote. The attribution sits **outside**
the blockquote as normal text, separated by a blank line — not a `>` line — so the
source is visually distinct from the words being quoted.

```markdown
> "Where is the Life we have lost in living? Where is the wisdom we have lost in knowledge? Where is the knowledge we have lost in information?"

-- T. S. Eliot in *The Rock* [@eliot_rock_1934]
```

Do not put the attribution inside the quote:

```markdown
> "Where is the Life we have lost in living?..."
>
> -- T. S. Eliot in *The Rock* [@eliot_rock_1934]
```

When a quotation is introduced in prose that already names the source, no
attribution line is needed — the lead-in carries the citation:

```markdown
A related puzzle, **the muddy children puzzle**, is described by @sep-dynamic-epistemic as follows:

> Three children are playing in the mud...
```

---

## Citations & references

Citations use Pandoc syntax with keys from the shared `.bib` file.

| Need | Source | Renders roughly as |
| --- | --- | --- |
| Parenthetical | `[@rowley_wisdom_2007]` | (Rowley, 2007) |
| With a locator | `[@lucas_hales_aotc_2000, p. 35]` | (Lucas & Hales, 2000, p. 35) |
| Multiple at once | `[@ackoff_data_1989; @vance_information_1997]` | (Ackoff, 1989; Vance, 1997) |
| In-text (narrative) | `as argued by @rowley_wisdom_2007` | as argued by Rowley (2007) |

Every chapter ends with a references heading; Quarto fills in the list:

```markdown
## References
```

---

## Inline text styles & links

```markdown
*italic* for emphasis and titles of works
**bold** for strong emphasis and UI/navigation labels
`inline code` for code, file names, and identifiers like `know` or `wonder`
[link text](https://example.com) for external links
[chapter link](04-ethics-in-understanding.md) for cross-chapter links
```

---

## Status markers & section stubs

Each draft chapter carries a one-line status note near the top, using an emoji
square for the level:

| Marker | Level | Meaning |
| --- | --- | --- |
| ⬜ | early development | mostly an outline; little finished prose |
| 🔴 | in development | some sections drafted, many still outlines |
| 🟡 | working draft | drafted end-to-end, still under revision |
| 🟢 | near-final draft | content settled; only light editing left |

```markdown
🟡 *Chapter Status: working draft. Most sections are drafted....*

TK
```

`TK` ("to come") marks a spot that still needs content. No chapter is 🟢 yet.

---

## Horizontal rule

Use a `---` rule (with blank lines around it) to separate major blocks, as done
throughout this page.

```markdown
---
```
