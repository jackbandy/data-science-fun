---
title: "Week 12 (CS 418 @ UIC)"
format:
  revealjs:
    footer: '<img src="../assets/branding/uic-black-logo.svg" alt="UIC logo"> <img src="../assets/branding/cc-by-nc-sa-small.svg" alt="CC BY-NC-SA"> <span class="footer-text">CS 418, Intro to Data Science, Week 12</span><span class="footer-text"><a href="https://dodatascience.fun/slides/week12.html">dodatascience.fun/slides/week12</a></span>'
nocite: |
  @blondel2008, @fortunato2010, @newman2004, @prakash2010, @tong2010, @chakrabarti2012, @goel2016structural
---

# Week 12 Slide Deck {.course-title}

## Intro to Network Analysis

Jack Bandy
2026

---

# Topic Title Placeholder {.course-title .photo-title data-state="photo-title" background-image="../assets/orange-line-stops-better/stop13-western-c.jpg" background-size="cover"}

CS 418 · Week 12 · 🟠 Western 🟠

---

# {.photo-only data-state="photo-only" background-image="../assets/orange-line-stops-better/stop13-western-c.jpg" background-size="cover"}

---

# What is a Graph?

:::: {.columns}
::: {.column width="50%"}
**A graph represents objects and relationships**

::: {.incremental}
- $G = (V, E)$
- $V$ = vertices (objects)
- $E$ = edges (relationships)
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Social network graph *(placeholder)*
:::
:::
::::

---

# Graph Applications

:::: {.columns}
::: {.column width="50%"}
**Graphs model many real-world systems:**

::: {.incremental}
- World Wide Web
- Social networks
- Transportation networks
- Computer networks
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Graph applications *(placeholder)*
:::
:::
::::

---

# Graph Terminology

:::: {.columns}
::: {.column width="50%"}
**Key concepts:**

::: {.incremental}
- **Endpoints:** Vertices connected by an edge
- **Adjacent:** Vertices connected by an edge
- **Degree:** Number of edges on a vertex
- **Self-loop:** Edge from vertex to itself
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Graph terminology *(placeholder)*
:::
:::
::::

---

# Adjacency Matrix

:::: {.columns}
::: {.column width="50%"}
**Matrix representation of graphs**

<!-- $$M_{ij} = \begin{cases}
1 & \text{if edge exists} \\
0 & \text{if no edge}
\end{cases}$$ -->
<!-- complex formula — left commented for now -->


::: {.incremental}
- Efficient for dense graphs
- Easy to check connections
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Adjacency matrix example *(placeholder)*
:::
:::
::::

---

# Types of Graphs

:::: {.columns}
::: {.column width="50%"}
**Three important types:**

::: {.incremental}
- **Directed:** Edges have direction
- **Weighted:** Edges have values
- **Attributed:** Nodes have properties
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Graph types *(placeholder)*
:::
:::
::::

---

# Community Detection

:::: {.columns}
::: {.column width="50%"}
**Finding groups in networks**

::: {.incremental}
- Communities = densely connected groups
- Sparse connections between groups
- Social groups in social networks
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Community detection *(placeholder)*
:::
:::
::::

---

# Goodness Metrics

:::: {.columns}
::: {.column width="50%"}
**Measuring community quality**

**Density:** Ratio of actual to possible edges

$$\frac{2E_s}{S(S-1)}$$

**Conductance:** Fraction of edges leaving

$$\frac{O_s}{2E_s + O_s}$$
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Modularity concept *(placeholder)*
:::
:::
::::

---

# Modularity

:::: {.columns}
::: {.column width="50%"}
**Most popular community detection metric**

<!-- $$Q = \frac{1}{2m} \sum_{v,w} \left[ A_{vw} - \frac{k_v k_w}{2m} \right] \delta(v,w)$$ -->
<!-- complex formula — left commented for now -->


::: {.incremental}
- Actual edges − Expected edges
- Higher Q = better communities
- Maximizing Q is NP-complete
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Modularity visualization *(placeholder)*
:::
:::
::::

---

# Louvain Method

:::: {.columns}
::: {.column width="50%"}
**Greedy modularity optimization**

::: {.incremental}
1. Start with each node as community 
2. Move nodes to maximize Q 
3. Aggregate communities into supernodes 
4. Repeat until convergence 
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Community detection *(placeholder)*
:::
:::
::::

---

# Network Diffusion

:::: {.columns}
::: {.column width="50%"}
**How events spread through networks**

**Key questions:** 

::: {.incremental}
- Will it spread?
- Which nodes to target?
- How to stop it?
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Simple network *(placeholder)*
:::
:::
::::

---

# Broadcast vs. Viral

:::: {.columns}
::: {.column width="50%"}
**Two ways content reaches a crowd** [@goel2016structural]

::: {.incremental}
- **Broadcast:** one source reaches many directly (e.g. a front page, the Super Bowl)
- **Viral:** person-to-person, over many generations
- Real cascades mix the two
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Broadcast (shallow) vs. viral (deep) diffusion trees *(placeholder)*
:::
:::
::::

---

# Structural Virality

:::: {.columns}
::: {.column width="50%"}
**A single number for tree shape** [@goel2016structural]

Average distance between all pairs of nodes in a diffusion tree (the *Wiener index*):

$$\nu(T) = \frac{1}{n(n-1)} \sum_{i=1}^{n} \sum_{j=1}^{n} d_{ij}$$

::: {.incremental}
- $\nu(T) \approx 2$: pure broadcast (a star)
- Large $\nu(T)$: deep, multigenerational spread
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Diffusion tree with pairwise distances *(placeholder)*
:::
:::
::::

---

# What Spreads Online?

:::: {.columns}
::: {.column width="50%"}
**~1 billion Twitter diffusion events** [@goel2016structural]

::: {.incremental}
- Over 99% of cascades die in one generation
- Virality varies widely (**no** "tipping point")
- Popularity is driven mostly by the largest broadcast
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Distribution of cascade sizes and structural virality *(placeholder)*
:::
:::
::::

---

# Virus Propagation Models

:::: {.columns}
::: {.column width="50%"}
**VPMs simplify disease spread**

::: {.incremental}
- How virulent?
- Recovery rate?
- Immunity?
- Immunity duration?
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
SIS model *(placeholder)*
:::
:::
::::

---

# $SIS$ Model

:::: {.columns}
::: {.column width="50%"}
**Susceptible → Infected → Susceptible**

::: {.incremental}
- Example: flu
- $\beta$ = transmission probability
- $\delta$ = healing probability
- No immunity
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
SIS model diagram *(placeholder)*
:::
:::
::::

---

# $SIR$ Model

:::: {.columns}
::: {.column width="50%"}
**Susceptible → Infected → Recovered**

::: {.incremental}
- Example: mumps
- $\beta$ = transmission probability
- $\delta$ = healing probability
- Life-time immunity
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
SIR model diagram *(placeholder)*
:::
:::
::::

---

# $SIRS$ Model

:::: {.columns}
::: {.column width="50%"}
**Temporary immunity**

::: {.incremental}
- Example: whooping cough
- $\gamma$ = immunity loss probability
- Immunity wears off over time
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
SIRS model diagram *(placeholder)*
:::
:::
::::

---

# $SEIV$ Model

:::: {.columns}
::: {.column width="50%"}
**Most complex VPM**

::: {.incremental}
- **E** = Exposed (incubation)
- **V** = Vaccinated
- $\varepsilon$ = virus maturation
- $\theta$ = vaccination rate
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
SEIV model diagram *(placeholder)*
:::
:::
::::

---

# Epidemic Threshold

:::: {.columns}
::: {.column width="50%"}
**Critical point for virus spread**

$$s = \lambda_1 \cdot C_{VPM}$$

::: {.incremental}
- $s < 1$: Virus dies out
- $s > 1$: Epidemic spreads
- $\lambda_1$ = network connectivity
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Epidemic threshold *(placeholder)*
:::
:::
::::

---

# Network Connectivity

:::: {.columns}
::: {.column width="50%"}
**Why spectral radius matters**

::: {.incremental}
- Average degree ignores paths
- $\lambda_1$ considers all path lengths
- Better predicts spread
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Network connectivity examples *(placeholder)*
:::
:::
::::

---

# Effective Strength

:::: {.columns}
::: {.column width="50%"}
**Predicting epidemic spread**

$$s = \lambda_1 \cdot C_{VPM}$$

**For SIS:** $s = \lambda_1 \cdot \frac{\beta}{\delta}$

::: {.incremental}
- Higher connectivity → more spread
- Higher transmission → more spread
- Higher healing → less spread
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Epidemic threshold visualization *(placeholder)*
:::
:::
::::

---

# Immunization Problem

:::: {.columns}
::: {.column width="50%"}
**Which $k$ nodes to vaccinate?**

**Goal:** Minimize $\lambda_1$

**Approaches:** 

::: {.incremental}
- Random (poor)
- High-degree nodes (better)
- NetShield (best)
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Network connectivity *(placeholder)*
:::
:::
::::

---

# NetShield Algorithm

:::: {.columns}
::: {.column width="50%"}
**Efficient immunization**

<!-- $$Sv(S) = \sum_{i \in S} 2\lambda_1 u_1(i)^2 - \sum_{i,j \in S} A(i,j) u_1(i) u_1(j)$$ -->
<!-- complex formula — left commented for now -->


::: {.incremental}
- Approximates eigen-drop
- Greedy selection
- Outperforms heuristics
:::
:::
::: {.column width="50%"}
![](../assets/orange-line/orange-line-trace-with-stops.svg){style="border: 1px solid #999; padding: 6px; max-width: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;"}

::: {style="text-align: center;"}
Community detection showing key nodes *(placeholder)*
:::
:::
::::

---



# References & Credits {.sources}

::: {#refs}
:::

::: {.credits}
- GitHub source: <https://github.com/jackbandy/data-science-fun/blob/main/docs/slides/week12.md>.
- Slides developed using materials from [Elena Zheleva](https://www.cs.uic.edu/~elena/) and [Gonzalo Bello Lander](https://cs.uic.edu/profiles/gonzalo-bello/), the Berkeley DS 100 team, Marine Carpuat, and Brian Ziebart. Network analysis content heavily adapted from Gonzalo Bello's **CS 418 - Lecture Slides 20 - Network Analysis.pdf**.
- Slide deck built with [Quarto](https://quarto.org/) revealjs.
- Title font is Big Shoulders; Body font is [Libre Franklin](https://en.wikipedia.org/wiki/Franklin_Gothic#Libre_Franklin).
:::
