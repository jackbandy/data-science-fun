# NOTICE: This file was  modified by an LLM (Claude Sonnet 4.6).
# Generates synthetic individual estimates from vox-populi-quantiles.csv by
# interpolating across quantiles, then adding small jitter to non-pinned rows
# so the final distribution matches the original quantile targets exactly.

import numpy as np
import polars as pl

rng = np.random.default_rng(42)

# Load quantile targets and extend interpolation range to [900, 1500]
# so the bottom/top 5% spread across the tails instead of clamping to one value.
q = pl.read_csv('vox-populi-quantiles.csv')
probs = q['quantile'].to_numpy() / 100
vals = q['estimate'].to_numpy()
full_probs = np.concatenate([[0.0], probs, [1.0]])
full_vals  = np.concatenate([[900],  vals,  [1500]])

# Interpolate n evenly-spaced quantile positions onto the value scale
n = 787
estimates = np.round(np.interp(np.linspace(0, 1, n), full_probs, full_vals)).astype(int)

# Identify the bracket [lo, hi] each estimate falls in for clamping jitter
j = np.searchsorted(full_probs, np.arange(n) / (n - 1), side='right')
lo = full_vals[np.clip(j - 1, 0, len(full_vals) - 1)]
hi = full_vals[np.clip(j,     0, len(full_vals) - 1)]

# Pin rows that correspond to known quantile positions
pinned = {int(r) for p in probs for r in (np.floor(p * (n-1)), np.ceil(p * (n-1)))}
tail_lo = int(np.floor(probs[0]  * (n - 1)))
tail_hi = int(np.ceil( probs[-1] * (n - 1)))
free = np.array([i for i in range(n) if i not in pinned])

# Tail rows get larger jitter so they spread naturally across 900–1074 / 1293–1500
interior = free[(free >= tail_lo) & (free <= tail_hi)]
tails    = free[(free <  tail_lo) | (free >  tail_hi)]
estimates[interior] = np.clip(
    estimates[interior] + np.round(rng.normal(0, 3,  len(interior))).astype(int),
    lo[interior], hi[interior],
)
estimates[tails] = np.clip(
    estimates[tails]    + np.round(rng.normal(0, 10, len(tails))).astype(int),
    lo[tails], hi[tails],
)
estimates.sort()

# Overwrite pinned positions with exact quantile values
for p, v in zip(probs, vals):
    estimates[[int(np.floor(p * (n-1))), int(np.ceil(p * (n-1)))]] = v

pl.DataFrame({'estimate': estimates}).write_csv('vox-populi-synthetic.csv')
