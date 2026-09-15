# Group project checkpoints

Source for the group-project checkpoints published at
[dodatascience.fun/project/](https://dodatascience.fun/project/).

Edit the files here (do not edit generated output under `docs/`).

## Layout

One file per checkpoint, `NN-slug.md`:

```
project/
  01-question-memo.md
  02-data-acquisition.md
  ...
```

Frontmatter:

| Key | Meaning |
|:--|:--|
| `summary` | one line, shown on the index and under the page title (required) |
| `topic` | unit / topic label |
| `due` | due date as students should read it |
| `ai_policy` | `double-red`, `red-yellow`, `double-yellow`, or `tk` — the course's CTA signal aspect (see the [FAQ](https://dodatascience.fun/faq.html)) |
| `draft` | `true` to skip the file entirely, so an unfinished stub is not published |

The first `# Heading` in the body becomes the title (removed from the body). A
`## AI/LLM policy` heading gets the matching signal drawing injected beside it by
`docs/_layouts/project-checkpoint.html`.

## Building

```sh
python3 project/build-project-data.py
```

writes `docs/project/<slug>.md` — one Jekyll page per non-draft checkpoint,
served at `/project/<slug>/`. Unlike the coding exercises, the markdown is not
converted here; Jekyll and kramdown render the body, since there is no starter
code or notebook preview to handle.

`docs/project/index.html` is the hand-written index page and is NOT generated —
add a checkpoint's row there yourself when its page goes live.

The generated pages are gitignored. The Pages workflow
(`.github/workflows/deploy-pages.yml`) runs this script on every build, so the
deployed site always matches the sources here. Run it before `jekyll serve` for
a local preview.
