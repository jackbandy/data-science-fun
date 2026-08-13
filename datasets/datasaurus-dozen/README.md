# Datasaurus Dozen

Thirteen small two-variable datasets that share nearly identical summary
statistics — mean of x, mean of y, standard deviation of x, standard deviation
of y, and Pearson correlation all agree to two decimal places — but look
completely different when plotted.

Each dataset has 142 points.

### Files

- `datasaurus-dozen.csv` — columns `dataset`, `x`, `y`. The `dataset` column
  takes 13 values: `dino`, `away`, `h_lines`, `v_lines`, `x_shape`, `star`,
  `high_lines`, `dots`, `circle`, `bullseye`, `slant_up`, `slant_down`,
  `wide_lines`.

### Source

Justin Matejka and George Fitzmaurice, "Same Stats, Different Graphs:
Generating Datasets with Varied Appearance and Identical Statistics through
Simulated Annealing," *CHI 2017*.
<https://www.autodesk.com/research/publications/same-stats-different-graphs>

The `dino` dataset is Alberto Cairo's original Datasaurus; the other twelve were
generated from it by the simulated-annealing procedure in the paper.

Retrieved as a plain CSV from the
[Rdatasets](https://vincentarelbundock.github.io/Rdatasets/) mirror of the R
`quartets` package (`csv/quartets/datasaurus_dozen.csv`); the `rownames` column
was dropped. Released by the authors under CC BY-SA 4.0.
