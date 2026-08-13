# Datasaurus — Attribution and Licensing

> _Note: this file was drafted by an LLM._

## datasaurus-dozen.gif

Animation of the thirteen Datasaurus Dozen datasets morphing into one another
while their summary statistics stay fixed. Used in the Week 4 slides
("Why Visualization?").

**Source of the underlying data and of the idea:** Justin Matejka and George
Fitzmaurice, ["Same Stats, Different Graphs: Generating Datasets with Varied
Appearance and Identical Statistics through Simulated
Annealing," *CHI 2017*](https://www.autodesk.com/research/publications/same-stats-different-graphs).
The `dino` dataset is Alberto Cairo's original Datasaurus. Data released by the
authors under CC BY-SA 4.0; it lives in this repo at
`datasets/datasaurus-dozen/`.

The GIF itself is generated here rather than copied from the paper — see
`make_datasaurus_animation.py`. Cite Matejka & Fitzmaurice wherever it is used.

### Files

- **make_datasaurus_animation.py** — regenerates both files below from the dataset.
- **datasaurus-dozen.gif** — the rendered animation, 680 × 760, ~130 frames.
- **datasaurus-dozen-panel.svg** — the same thirteen datasets as a still 4 × 4 panel
  of small multiples, for the slide that has to stop moving while you talk over it.
