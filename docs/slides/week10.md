---
title: "Week 10 (CS 418 @ UIC)"
format:
  revealjs:
    footer: '<img src="../assets/branding/uic-black-logo.svg" alt="UIC logo"> <img src="../assets/branding/cc-by-nc-sa-small.svg" alt="CC BY-NC-SA"> <span class="footer-text">CS 418, Intro to Data Science, Week 10</span><span class="footer-text"><a href="https://dodatascience.fun/slides/week10.html">dodatascience.fun/slides/week10</a></span>'
---

# Week 10 Slide Deck {.course-title}

## Clustering, PCA; Model Evaluation

Jack Bandy
2026

---

# Topic Title Placeholder {.course-title .photo-title data-state="photo-title" background-image="../assets/orange-line-stops-better/stop11-ashland-a.jpg" background-size="cover"}

CS 418 · Week 10 · 🟠 Ashland 🟠

---

# {.photo-only data-state="photo-only" background-image="../assets/orange-line-stops-better/stop11-ashland-a.jpg" background-size="cover"}

---

# Clustering {.section-header}

---

# What Is Clustering?

**Unsupervised** learning — discover what is already there.

- No labels / ground truth
- Group similar observations together
- Use similarity / distance to make groups
- Goals:
	- high similarity within clusters (cohesion)
	- low similarity between cluster (separation)

---

# Types of Clustering

- **Complete vs. partial** — every observation belongs to a cluster, or some may not
- **Non-overlapping vs. overlapping** — each observation belongs to one cluster, or potentially many

A **clustering** is a collection of clusters; different algorithms make different assumptions about these properties.

---

# K-Means Clustering

**Algorithm sketch:**

1. Choose $k$ (number of clusters)
2. Initialize $k$ centroids randomly
3. Assign each point to the nearest centroid
4. Recompute centroids as the mean of assigned points
5. Repeat 3–4 until assignments stabilize

_Sensitive to initialization; run multiple times and keep the best result._

---

# Choosing K

- **Elbow method**
- **Silhouette score**
- **Domain knowledge**
- ?

---

# K-Means Limitations

- Assumes spherical clusters, roughly equal size
- Sensitive to outliers
	- centroid gets pulled
- Must choose $k$ in advance
- Poor for non-convex shapes
	- DBSCAN, hierarchical clustering as alternatives

---

# K-Means Initialization

K-means is **sensitive to initialization**

**Furthest-First Heuristic (FFH):**

1. Pick first centroid randomly from data points
2. For each remaining centroid: pick the point that maximizes minimum distance to already-chosen centroids

**K-means++:** randomized version of FFH — pick next centroid with probability proportional to its minimum distance from existing centroids.

---

# Cluster Evaluation {.section-header}

---

# Cohesion and Separation

- **Cohesion** — how similar observations within a cluster are to each other
- **Separation** — how distinct a cluster is from other clusters

$$\text{cohesion}(C_i) = \frac{1}{|C_i|(|C_i|-1)/2} \sum_{x,y \in C_i} \text{proximity}(x, y)$$

$$\text{separation}(C_i, C_j) = \frac{1}{|C_i||C_j|} \sum_{x \in C_i,\, y \in C_j} \text{proximity}(x, y)$$

We want high cohesion and high separation.

---

# Silhouette Coefficient

Combines cohesion and separation into a single score per observation:

$$s_i = \frac{b - a}{\max(a, b)}$$

- $a$ = average distance from point $i$ to all other points **in the same cluster**
- $b$ = average distance from point $i$ to all points **in the nearest other cluster**

Range: $[-1, 1]$. Negative → misclassified; 0 → overlapping; positive and close to 1 → well-clustered.

---

# Hierarchical Clustering {.section-header}

---

# Hierarchical Clustering

Produces a **dendrogram** — a tree of nested clusters.

Two approaches:

- **Agglomerative (bottom-up):** start with each observation as its own cluster; merge the closest pair at each step until one cluster remains
- **Divisive (top-down):** start with one cluster; split at each step until each observation is its own cluster

Agglomerative is far more common in practice.

---

# Agglomerative Linkage Methods

How to define "closeness" between clusters:

| Method | Distance between $C_i$ and $C_j$ |
|--------|----------------------------------|
| **Single link (MIN)** | min distance between any two points |
| **Complete link (MAX)** | max distance between any two points |
| **Average link** | mean distance across all pairs |

TODO look into Ward's method

Average link is most widely used (more robust to outliers than single/complete).

---

# Principal Component Analysis (PCA) {.section-header}

---

# What Is PCA?

**Dimensionality reduction** — represent high-dimensional data in fewer dimensions, preserve as much variance as possible.

- Find directions ("principal components") of maximum variance
- Each PC is a linear combination of original features
- PCs are orthogonal / uncorrelated

---


# Why Use PCA?

- Visualization (project to 2D/3D for plotting)
- Noise reduction (drop low-variance components)
- Speed up downstream models (fewer features)
- Handle multicollinearity

**Tradeoff:** interpretability — PCs are abstract combinations of original features.

---

# Scree Plot

Plot the **explained variance ratio** for each component. Helps decide how many PCs to keep.

_[TODO: add scree plot example]_

---


# PCA

::: {.columns}
::: {.column width="40%"}
![Pete Crow-Armstrong, Chicago Cubs CF](../assets/portraits/pete-crow-armstrong.jpg){style="max-height:480px;border-radius:6px;"}
:::
::: {.column width="60%"}
**#4 · CF · Chicago Cubs**


- 2025 NL All-Star, Gold Glove winner
- Hit for the cycle on June 15, 2026
	- I was there!
	- And I thought... PCA with PCA?

_Photo: Minda Haas Kuhlmann, [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/), via Wikimedia Commons_
:::
:::

---

# Sources {.sources}

1. GitHub source: <https://github.com/jackbandy/data-science-fun/blob/main/docs/slides/week10.md>.
2. Slides developed using materials from [Elena Zheleva](https://www.cs.uic.edu/~elena/) and [Gonzalo Bello Lander](https://cs.uic.edu/profiles/gonzalo-bello/), the Berkeley DS 100 team, Marine Carpuat, and Brian Ziebart.
3. Slide deck built with [Quarto](https://quarto.org/) revealjs.
4. Title font is Big Shoulders; Body font is [Libre Franklin](https://en.wikipedia.org/wiki/Franklin_Gothic#Libre_Franklin).
