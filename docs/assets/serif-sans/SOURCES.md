# Serif vs. Sans-Serif — Attribution and Licensing

> _Note: this file was drafted with an LLM._

All three files are from one Wikimedia Commons series, "Recreated by User:Stannered, original by en:User:Chmod007" (2007), licensed [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). Downloaded 26 Sep 2026, unmodified. Letters are drawn as vector paths, so no font is needed to render them.

| File here | Commons original | Shows |
|---|---|---|
| `serif-and-sans-serif-01.svg` | [File:Serif and sans-serif 01.svg](https://commons.wikimedia.org/wiki/File:Serif_and_sans-serif_01.svg) | "AaBbCc" in Liberation Sans (sans-serif) |
| `serif-and-sans-serif-02.svg` | [File:Serif and sans-serif 02.svg](https://commons.wikimedia.org/wiki/File:Serif_and_sans-serif_02.svg) | "AaBbCc" in Liberation Serif |
| `serif-and-sans-serif-03.svg` | [File:Serif and sans-serif 03.svg](https://commons.wikimedia.org/wiki/File:Serif_and_sans-serif_03.svg) | The same serif letters with the serifs in red |

## Generated replacements (used in the Week 6 slides)

`make_serif_figures.py` (`uvx --from fonttools python make_serif_figures.py`) sets "data" in fonts bundled with macOS and writes the letters as outlined paths, so no font is embedded. The serifs-in-red idea follows the Commons series above; the red regions are hand-placed boxes over the Superclarendon outlines (`SERIF_BOXES` in the script).

| File | Shows | Font |
|---|---|---|
| `serif-demo.svg` | "data" with heavy bracketed serifs and ball terminals | Superclarendon Regular (`/System/Library/Fonts/Supplemental/SuperClarendon.ttc`) |
| `serif-demo-marked.svg` | The same letters with serifs and terminals in red | Superclarendon Regular |
| `sans-demo.svg` | "data" with plain stroke ends | Helvetica (`/System/Library/Fonts/Helvetica.ttc`) |
