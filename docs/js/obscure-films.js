/* NOTICE: This file was created by an LLM coding system (Claude, August 2026). */
/* Draws the percentile bar chart on /obscure-films/ and runs its gates + sampler.
 *
 * Data comes from /obscure-films/data/obscure-films.json, which
 * datasets/movies-from-imdb/build_obscure.py builds from IMDb's public TSVs.
 *
 * Hand-rolled SVG on purpose: no charting library, no CDN. One hue (CTA Orange
 * #f9461c) for every bar — this is a single series, so the bar *height* (log-scaled
 * total votes) carries the magnitude and the gate *selection* carries the color
 * meaning: bars the selected span touches read full strength, the rest fade.
 *
 * The 100 display bars are one-percent bands (0.1–1, 1–2, …, 98–99, 99–99.9), so
 * the distribution shape resolves to the percentile level. The two gates are
 * independent of those ticks: dragging snaps to 1% steps (integer percentiles
 * 1–99), and double-clicking a gate lets you type an exact value. Each pool film
 * carries its own percentile `p`, so any span — not just whole bands — filters
 * correctly.
 */
(function () {
  "use strict";

  var SVG_NS = "http://www.w3.org/2000/svg";
  var ACCENT = "#f9461c";        // CTA Orange Line — the site's identity color
  var ACCENT_WASH = "#fdece7";   // the wash behind the selected span
  var RULE = "#d8d8d8";          // recessive axis lines
  var MUTED = "#6b6b6b";         // axis labels / captions

  // Chart frame, in SVG user units. The SVG scales to the container width.
  var W = 960, H = 380;
  var M = { top: 56, right: 28, bottom: 58, left: 68 };
  var IL = M.left, IR = W - M.right, IT = M.top, IB = H - M.bottom;
  var IW = IR - IL, IH = IB - IT;

  // Log y-domain, fit to the band totals after load. One-percent bands span a far
  // wider range than the old 10% buckets did (the obscure tail's 1% slices hold
  // very few votes), so the domain is computed from the actual min/max band totals
  // and floored/ceilinged to clean decades for the gridlines.
  var Y_MIN, Y_MAX;

  // Drag grid: integer percentiles. The visible range is [0.1, 99.9] (the most/
  // least-voted 0.1% are excluded), and the gates step in whole 1% from 1 to 99.
  var GRID_MIN = 1, GRID_MAX = 99;

  var TICKS;        // [0.1,10,20,...,99.9] — 11 display ticks framing the 10 bars
  var BARS;         // 10 {low,high,totalVotes,count}
  var POOL;         // ~5000 {id,t,y,g,r,v,p}
  var X_MIN, X_MAX; // first/last tick — the visible percentile range

  // Gate positions, in percentile units. Valid spans: 0.1 < left < right < 99.9.
  var leftPct = 1, rightPct = 99;

  function el(name, attrs, text) {
    var node = document.createElementNS(SVG_NS, name);
    for (var k in attrs) {
      if (attrs[k] !== null && attrs[k] !== undefined) node.setAttribute(k, attrs[k]);
    }
    if (text !== undefined) node.textContent = text;
    return node;
  }

  function xScale(p) { return IL + ((p - X_MIN) / (X_MAX - X_MIN)) * IW; }
  function pctFromX(x) { return X_MIN + ((x - IL) / IW) * (X_MAX - X_MIN); }
  function yScale(v) { return IB - ((Math.log10(v) - Math.log10(Y_MIN)) / (Math.log10(Y_MAX) - Math.log10(Y_MIN))) * IH; }

  // Nearest integer percentile in the drag grid.
  function snap(pct) {
    var s = Math.round(pct);
    return s < GRID_MIN ? GRID_MIN : s > GRID_MAX ? GRID_MAX : s;
  }

  function fmt(n) { return n.toLocaleString("en-US"); }

  // 1.2M / 12k / 999 — for vote totals on the cards and tooltip.
  function fmtCompact(n) {
    if (n >= 1e9) return (n / 1e9).toFixed(n >= 1e10 ? 0 : 1).replace(/\.0$/, "") + "B";
    if (n >= 1e6) return (n / 1e6).toFixed(n >= 1e7 ? 0 : 1).replace(/\.0$/, "") + "M";
    if (n >= 1e3) return Math.round(n / 1e3) + "k";
    return String(n);
  }

  // "50%" or "73.5%" — one decimal max, no trailing .0.
  function fmtPct(v) {
    v = Math.round(v * 10) / 10;
    return (v % 1 === 0 ? String(v) : v.toFixed(1)) + "%";
  }

  function buildChart(svg) {
    // Y gridlines + labels, one per decade across the fitted domain.
    var v = Y_MIN;
    while (v <= Y_MAX * (1 + 1e-9)) {
      var y = yScale(v);
      svg.appendChild(el("line", { class: "obscure-axis", x1: IL, x2: IR, y1: y, y2: y }));
      svg.appendChild(el("text", { class: "obscure-axis obscure-ylabel", x: IL - 10, y: y + 3.5, "text-anchor": "end" }, fmtCompact(v)));
      v *= 10;
    }

    // Baseline.
    svg.appendChild(el("line", { class: "obscure-axis", x1: IL, x2: IR, y1: IB, y2: IB }));

    // Selected-span wash (behind bars).
    var wash = el("rect", { class: "obscure-span-wash", y: IT, height: IH });
    svg.appendChild(wash);

    // Bars + hit areas. With 100 bands the gap and corner radius scale down so
    // thin bars still read as distinct marks rather than a solid wall.
    var barEls = [];
    var slot = IW / BARS.length;
    var gap = Math.min(3, Math.max(0.6, slot * 0.16));
    var rx = Math.min(2, Math.max(0.5, slot * 0.18));
    for (var i = 0; i < BARS.length; i++) {
      var b = BARS[i];
      var x0 = xScale(TICKS[i]), x1 = xScale(TICKS[i + 1]);
      var bx = x0 + gap / 2, bw = x1 - x0 - gap;
      var by = yScale(b.totalVotes), bh = IB - by;
      var bar = el("rect", { class: "obscure-bar obscure-bar-in", x: bx, y: by, width: bw, height: bh, rx: rx });
      svg.appendChild(bar);
      barEls.push(bar);
      // Full-column hit area so the tooltip fires anywhere in the band's column.
      var hit = el("rect", { class: "obscure-hit", x: x0, y: IT, width: x1 - x0, height: IH, "data-i": i });
      svg.appendChild(hit);
    }

    // X ticks: a short minor tick at every band boundary (the 1% steps), with
    // labels only at the decades plus the two 0.1% exclusion endpoints.
    for (var t = 0; t < TICKS.length; t++) {
      var tv = TICKS[t];
      var x = xScale(tv);
      var major = tv === X_MIN || tv === X_MAX || (tv % 1 === 0 && tv % 10 === 0);
      svg.appendChild(el("line", {
        class: "obscure-axis obscure-tick" + (major ? "" : " obscure-tick-minor"),
        x1: x, x2: x, y1: IB, y2: IB + (major ? 5 : 3)
      }));
      if (major) {
        svg.appendChild(el("text", { class: "obscure-axis obscure-xlabel", x: x, y: IB + 20, "text-anchor": "middle" }, fmtPct(tv)));
      }
    }

    // Axis captions.
    svg.appendChild(el("text", { class: "obscure-caption", x: (IL + IR) / 2, y: H - 8, "text-anchor": "middle" },
      "Popularity percentile  (popular → obscure)"));
    // Y caption sits on its own line above the plot — rotated titles force a head-tilt.
    svg.appendChild(el("text", { class: "obscure-caption", x: IL, y: 20 }, "Total votes (log)"));

    // Gates (drawn last so they sit above bars).
    var leftGate = makeGate("left");
    var rightGate = makeGate("right");
    svg.appendChild(leftGate.g);
    svg.appendChild(rightGate.g);

    return { wash: wash, barEls: barEls, leftGate: leftGate, rightGate: rightGate };
  }

  // A gate is a vertical line plus a grabbable tab at the top with its value.
  // A wide transparent hit strip makes the whole gate easy to grab — the 2px
  // line alone is too thin a target.
  function makeGate(side) {
    var g = el("g", { class: "obscure-gate", "data-side": side, tabindex: "0", role: "slider" });
    var hit = el("rect", { class: "obscure-gate-hit", y: IT, width: 30, height: IH, "pointer-events": "all" });
    var line = el("line", { class: "obscure-gate-line", y1: IT, y2: IB });
    var tab = el("rect", { class: "obscure-gate-tab", y: IT - 26, width: 64, height: 24, rx: 5 });
    var label = el("text", { class: "obscure-gate-label", y: IT - 10, "text-anchor": "middle" });
    g.appendChild(hit);
    g.appendChild(line);
    g.appendChild(tab);
    g.appendChild(label);
    return { g: g, hit: hit, line: line, tab: tab, label: label, side: side };
  }

  function positionGate(gate, pct) {
    var x = xScale(pct);
    gate.hit.setAttribute("x", x - 15);
    gate.line.setAttribute("x1", x);
    gate.line.setAttribute("x2", x);
    gate.tab.setAttribute("x", x - 32);
    gate.label.setAttribute("x", x);
    gate.label.textContent = fmtPct(pct);
    gate.g.setAttribute("aria-valuenow", pct);
    gate.g.setAttribute("aria-label", (gate.side === "left" ? "Left" : "Right") + " boundary, " + fmtPct(pct));
  }

  // A display bar is lit when its bucket intersects the selected span.
  function barIn(b) { return b.low < rightPct && b.high > leftPct; }

  function eligibleCount() {
    var n = 0;
    for (var i = 0; i < POOL.length; i++) {
      var p = POOL[i].p;
      if (p >= leftPct && p < rightPct) n++;
    }
    return n;
  }

  function updateView() {
    positionGate(state.leftGate, leftPct);
    positionGate(state.rightGate, rightPct);
    state.wash.setAttribute("x", xScale(leftPct));
    state.wash.setAttribute("width", xScale(rightPct) - xScale(leftPct));
    for (var i = 0; i < state.barEls.length; i++) {
      state.barEls[i].setAttribute("class", barIn(BARS[i]) ? "obscure-bar obscure-bar-in" : "obscure-bar obscure-bar-out");
    }
    rangeLabel.textContent = fmtPct(leftPct) + " – " + fmtPct(rightPct);
    var n = eligibleCount();
    countEl.textContent = fmt(n);
    sampleBtn.disabled = n === 0;
  }

  function nudge(side, dir) {
    if (side === "left") {
      var nl = Math.round(leftPct * 10) / 10 + dir;
      if (nl >= GRID_MIN && nl < rightPct) { leftPct = nl; updateView(); }
    } else {
      var nr = Math.round(rightPct * 10) / 10 + dir;
      if (nr <= GRID_MAX && nr > leftPct) { rightPct = nr; updateView(); }
    }
  }

  // Pointer drag → snap to the nearest 1% grid line under the pointer.
  function attachDrag(gate, side) {
    var g = gate.g;
    g.addEventListener("pointerdown", function (e) {
      e.preventDefault();
      g.setPointerCapture(e.pointerId);
      g.focus();
    });
    g.addEventListener("pointermove", function (e) {
      if (g.hasPointerCapture && g.hasPointerCapture(e.pointerId)) {
        var candidate = snap(pctFromX(svgPoint(e).x));
        if (side === "left") { if (candidate < rightPct) leftPct = candidate; }
        else { if (candidate > leftPct) rightPct = candidate; }
        updateView();
      }
    });
    g.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft" || e.key === "ArrowDown") { nudge(side, -1); e.preventDefault(); }
      else if (e.key === "ArrowRight" || e.key === "ArrowUp") { nudge(side, 1); e.preventDefault(); }
    });
    g.addEventListener("dblclick", function () { typeValue(side); });
  }

  // Double-click → type an exact boundary. Left must be in (0.1, right); right in
  // (left, 99.9). Re-prompts on anything that is not a number in that range.
  function typeValue(side) {
    while (true) {
      var msg, lo, hi;
      if (side === "left") {
        lo = 0.1; hi = rightPct;
        msg = "Left boundary (%ile). Must be greater than 0.1 and less than " + fmtPct(rightPct) + ":";
      } else {
        lo = leftPct; hi = 99.9;
        msg = "Right boundary (%ile). Must be greater than " + fmtPct(leftPct) + " and less than 99.9:";
      }
      var input = window.prompt(msg, String(side === "left" ? leftPct : rightPct));
      if (input === null) return;
      var v = parseFloat(input);
      if (isFinite(v) && v > lo && v < hi) {
        v = Math.round(v * 10) / 10;
        if (side === "left") leftPct = v; else rightPct = v;
        updateView();
        return;
      }
      window.alert("Enter a number greater than " + lo + " and less than " + hi + ".");
    }
  }

  function svgPoint(e) {
    var pt = state.svg.createSVGPoint();
    pt.x = e.clientX; pt.y = e.clientY;
    return pt.matrixTransform(state.svg.getScreenCTM().inverse());
  }

  // --- tooltip -------------------------------------------------------------
  function attachTooltip() {
    var tt = document.querySelector(".obscure-tooltip");
    state.svg.querySelectorAll(".obscure-hit").forEach(function (h) {
      h.addEventListener("mouseenter", function () {
        var b = BARS[+h.getAttribute("data-i")];
        tt.innerHTML = "<b>" + fmtPct(b.low) + " – " + fmtPct(b.high) + "</b><br>" +
          fmt(b.count) + " films · " + fmt(b.totalVotes) + " votes";
        tt.setAttribute("data-visible", "true");
      });
      h.addEventListener("mousemove", function (e) {
        var r = state.host.getBoundingClientRect();
        tt.style.left = (e.clientX - r.left) + "px";
        tt.style.top = (e.clientY - r.top - 12) + "px";
      });
      h.addEventListener("mouseleave", function () { tt.setAttribute("data-visible", "false"); });
    });
  }

  // --- sampling + gallery ---------------------------------------------------
  function sampleEight() {
    var elig = [];
    for (var i = 0; i < POOL.length; i++) {
      var p = POOL[i].p;
      if (p >= leftPct && p < rightPct) elig.push(POOL[i]);
    }
    if (elig.length === 0) return;
    // Partial Fisher–Yates: up to 8 distinct draws.
    var k = Math.min(8, elig.length);
    for (var j = 0; j < k; j++) {
      var r = j + Math.floor(Math.random() * (elig.length - j));
      var tmp = elig[j]; elig[j] = elig[r]; elig[r] = tmp;
    }
    renderGallery(elig.slice(0, k));
  }

  function renderGallery(films) {
    gallery.innerHTML = "";
    films.forEach(function (m) {
      var card = document.createElement("article");
      card.className = "obscure-card";

      var title = document.createElement("h3");
      title.textContent = m.t;

      var meta = document.createElement("p");
      meta.className = "obscure-card-meta";
      var bits = [];
      if (m.y && m.y !== "\\N") bits.push(m.y);
      if (m.g && m.g !== "\\N") bits.push(m.g.replace(/,/g, ", "));
      meta.textContent = bits.join(" · ");

      // Rating, votes, and the popularity percentile this film sits at — each on
      // its own line, grouped together.
      var stats = document.createElement("div");
      stats.className = "obscure-card-stats-group";

      var rating = document.createElement("p");
      rating.className = "obscure-card-stats";
      rating.textContent = "★ " + (m.r === "\\N" ? "—" : m.r);

      var votes = document.createElement("p");
      votes.className = "obscure-card-stats";
      votes.textContent = fmt(m.v) + " votes";

      var pct = document.createElement("p");
      pct.className = "obscure-card-stats obscure-card-pct";
      // p is the film's rank from the most-voted end, so that fraction of films
      // have more votes — i.e. this film has fewer votes than p% of films.
      pct.textContent = "Fewer votes than " + fmtPct(m.p) + " of films in IMDb";

      stats.appendChild(rating);
      stats.appendChild(votes);
      stats.appendChild(pct);

      var link = document.createElement("a");
      link.className = "obscure-card-link";
      link.href = "https://www.imdb.com/title/" + m.id + "/";
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.textContent = "Open on IMDb";

      card.appendChild(title);
      card.appendChild(meta);
      card.appendChild(stats);
      card.appendChild(link);
      gallery.appendChild(card);
    });
  }

  // --- init -----------------------------------------------------------------
  var state, rangeLabel, countEl, sampleBtn, gallery;

  function init(host) {
    state = { host: host };
    fetch(host.getAttribute("data-src")).then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.json();
    }).then(function (data) {
      TICKS = data.ticks;
      BARS = data.bars;
      POOL = data.pool;
      X_MIN = TICKS[0];
      X_MAX = TICKS[TICKS.length - 1];
      leftPct = GRID_MIN;
      rightPct = GRID_MAX;

      // Fit the log y-domain to the band totals, floored/ceilinged to decades.
      var maxBar = 0, minBar = Infinity;
      for (var i = 0; i < BARS.length; i++) {
        var tv = BARS[i].totalVotes;
        if (tv > maxBar) maxBar = tv;
        if (tv && tv < minBar) minBar = tv;
      }
      Y_MAX = Math.pow(10, Math.ceil(Math.log10(maxBar)));
      Y_MIN = Math.pow(10, Math.floor(Math.log10(minBar)));
      if (Y_MAX <= Y_MIN) Y_MAX = Y_MIN * 1e5;

      document.getElementById("obscure-generated").textContent = data.generated;
      document.getElementById("obscure-total").textContent = fmt(data.totalMovies);
      rangeLabel = document.getElementById("obscure-range-label");
      countEl = document.getElementById("obscure-count");
      sampleBtn = document.getElementById("obscure-sample");
      gallery = document.getElementById("obscure-gallery");

      host.classList.remove("obscure-loading");
      host.textContent = "";

      var svg = el("svg", { viewBox: "0 0 " + W + " " + H, preserveAspectRatio: "xMidYMid meet" });
      host.appendChild(svg);
      state.svg = svg;

      var tt = document.createElement("div");
      tt.className = "obscure-tooltip";
      host.appendChild(tt);

      var built = buildChart(svg);
      state.wash = built.wash;
      state.barEls = built.barEls;
      state.leftGate = built.leftGate;
      state.rightGate = built.rightGate;

      attachDrag(built.leftGate, "left");
      attachDrag(built.rightGate, "right");
      attachTooltip();

      sampleBtn.addEventListener("click", sampleEight);
      updateView();
    }).catch(function (err) {
      host.classList.remove("obscure-loading");
      host.classList.add("obscure-error");
      host.textContent = "Could not load film data: " + err.message;
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { init(document.getElementById("obscure-chart")); });
  } else {
    init(document.getElementById("obscure-chart"));
  }
})();