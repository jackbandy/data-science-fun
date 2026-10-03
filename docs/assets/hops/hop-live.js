// NOTICE: Moved verbatim out of an inline <script> in hop-live.html by an LLM
// coding system (Claude Code), so the page's Content-Security-Policy can drop
// 'unsafe-inline'.

(() => {
  const NS = "http://www.w3.org/2000/svg";
  const svg = document.getElementById("hop");
  const ORANGE = "#f9461c", STEEL = "#565a5c", INK = "#1a1a1a";
  const FRAME_MS = 350;                          // same pace as the ridership HOP GIF
  const DIST = { A: { mu: 45, sd: 12 }, B: { mu: 55, sd: 12 } };

  // Value scale 0..100 -> y pixels; two panels share it.
  const Y0 = 370, Y1 = 90;
  const y = v => Y0 - (Math.max(0, Math.min(100, v)) / 100) * (Y0 - Y1);
  const PANELS = [
    { x0: 60,  x1: 280, title: "Error bars", sub: "mean ± 2 SD" },
    { x0: 340, x1: 560, title: "HOP",        sub: "one draw per frame" },
  ];
  const catX = (p, k) => p.x0 + (p.x1 - p.x0) * (k === "A" ? 0.3 : 0.7);

  const el = (tag, attrs, text) => {
    const e = document.createElementNS(NS, tag);
    for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, v);
    if (text !== undefined) e.textContent = text;
    svg.appendChild(e);
    return e;
  };

  // Gridlines and y ticks, shared across both panels.
  for (let v = 0; v <= 100; v += 25) {
    el("line", { class: "grid", x1: PANELS[0].x0, x2: PANELS[1].x1, y1: y(v), y2: y(v) });
    el("text", { class: "tick", x: PANELS[0].x0 - 10, y: y(v) + 4, "text-anchor": "end" }, v);
  }

  for (const p of PANELS) {
    const cx = (p.x0 + p.x1) / 2;
    el("text", { class: "panel-title", x: cx, y: 36, "text-anchor": "middle" }, p.title);
    el("text", { class: "panel-sub",   x: cx, y: 58, "text-anchor": "middle" }, p.sub);
    for (const k of ["A", "B"]) {
      el("text", { class: "cat", x: catX(p, k), y: Y0 + 28, "text-anchor": "middle" }, k);
    }
  }

  // Left panel: static error bars.
  const L = PANELS[0];
  for (const k of ["A", "B"]) {
    const { mu, sd } = DIST[k], x = catX(L, k);
    el("line", { x1: x, x2: x, y1: y(mu - 2 * sd), y2: y(mu + 2 * sd), stroke: STEEL, "stroke-width": 3 });
    for (const v of [mu - 2 * sd, mu + 2 * sd]) {
      el("line", { x1: x - 14, x2: x + 14, y1: y(v), y2: y(v), stroke: STEEL, "stroke-width": 3 });
    }
    el("circle", { cx: x, cy: y(mu), r: 7, fill: INK });
  }

  // Right panel: one horizontal mark per variable, moved every frame.
  const R = PANELS[1];
  const marks = {};
  for (const k of ["A", "B"]) {
    const x = catX(R, k);
    marks[k] = el("line", { x1: x - 36, x2: x + 36, y1: y(DIST[k].mu), y2: y(DIST[k].mu),
                            stroke: STEEL, "stroke-width": 6, "stroke-linecap": "round" });
  }
  const tally = el("text", { class: "tally", x: (R.x0 + R.x1) / 2, y: Y0 + 56, "text-anchor": "middle" }, "");
  const hint  = el("text", { class: "hint",  x: PANELS[0].x0 - 40, y: 432, "text-anchor": "start" }, "click to pause");

  // Box-Muller normal draw.
  const normal = (mu, sd) => {
    const u = 1 - Math.random(), v = Math.random();
    return mu + sd * Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
  };

  let frames = 0, bWins = 0;
  const step = () => {
    const a = normal(DIST.A.mu, DIST.A.sd), b = normal(DIST.B.mu, DIST.B.sd);
    frames += 1; if (b > a) bWins += 1;
    for (const [k, v] of [["A", a], ["B", b]]) {
      marks[k].setAttribute("y1", y(v));
      marks[k].setAttribute("y2", y(v));
    }
    marks.A.setAttribute("stroke", a > b ? ORANGE : STEEL);
    marks.B.setAttribute("stroke", b > a ? ORANGE : STEEL);
    tally.textContent = `B > A in ${bWins} of ${frames} frames`;
  };

  // Respect reduced-motion: start paused and step one frame per click.
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  let timer = null;
  const play  = () => { timer = setInterval(step, FRAME_MS); hint.textContent = "click to pause"; };
  const pause = () => { clearInterval(timer); timer = null; hint.textContent = "click to play"; };

  step();
  if (reduced) { hint.textContent = "click for the next draw"; }
  else { play(); }
  svg.addEventListener("click", () => {
    if (reduced) step();
    else if (timer) pause();
    else play();
  });
})();
