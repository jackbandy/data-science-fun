# Coding exercises

Source for the five coding exercises published at
[dodatascience.fun/exercises.html](https://dodatascience.fun/exercises.html).

Edit the files here ( do not edit generated output under `docs/`)

## Layout

One folder per exercise, `NN-slug`:

```
exercises/
  NN-slug/
    exercise.md     the prompt (frontmatter + markdown)
    starter/        starter code, copied to the site as-is
```

`exercise.md` frontmatter:

| Key | Meaning |
|:--|:--|
| `summary` | one line, shown on the index card (required) |
| `topic` | unit / topic label, e.g. `Exploratory data analysis` |
| `due` | due date as students should read it |
| `ai_policy` | `double-red`, `red-yellow`, `double-yellow`, or `tk` — the course's CTA signal aspect (see the [FAQ](https://dodatascience.fun/faq.html)) |

The first `# Heading` in the body becomes the title (removed from the body).

## Building

```sh
python3 exercises/build-exercises-data.py
```

regenerates:

- `docs/_data/exercises.yml` — the index page's cards
- `docs/exercises/<slug>.html` — one page per exercise, at `/exercises/<slug>/`
- `docs/exercises/<slug>/starter/…` — copies of the starter files (`.ipynb_checkpoints/`, `__pycache__/`, `.DS_Store` and `.pyc` are skipped)
- `docs/_includes/exercises-about.html` — the "Read more" blurb, from `exercises-about.md`

Any `.ipynb` in `starter/` is also rendered to a static HTML preview, appended to its exercise page inside a collapsed `<details>`. A student can then read the starter without downloading it.

 `docs/exercises.html`, is hand-written index page 

The generated files are not committed - they are gitignored. The Pages workflow (`.github/workflows/deploy-pages.yml`) runs this script on every build, so the deployed site always matches the sources here. Run with `jekyll serve` for a local preview.


## Markdown support

The converter handles headings, paragraphs, ordered/unordered lists, fenced and inline code, blockquotes, `---`, links, bold, and italics. It does **not** currently do tables or images.
