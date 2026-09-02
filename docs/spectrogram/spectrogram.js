/* NOTICE: This file was substantially generated/modified by an LLM.
   Live microphone spectrogram, styled after the Merlin Bird ID Sound ID view:
   ink on paper, time scrolling under a cursor pinned at "now". */

(function () {
  'use strict';

  // The plot always holds exactly this many seconds, whatever the frame rate or
  // the width of the window. Scrolling by elapsed time rather than by a fixed
  // number of pixels per frame is what makes that promise true -- and what lets
  // the one-second ticks line up with the time axis.
  var WINDOW_SECONDS = 8;

  // Widest column a single frame may draw, in CSS pixels. Only sizes the
  // scratch buffer: a slow frame paints a wide column, a fast one a narrow one.
  var MAX_COLUMN_CSS_W = 12;

  // 8192-point FFT at 48 kHz is ~5.9 Hz per bin: fine enough that a whistle is
  // a hairline rather than a band, and the analyser still keeps up at 60 fps.
  var FFT_SIZE = 8192;

  // Loudness window, in dBFS, mapped onto white..black. Fixed, and deliberately
  // set as sensitive as the analyser goes: a floor near the noise floor of the
  // mic itself means every sound in the room leaves a mark, which is the point
  // of the demo. The ceiling stays well below 0 so ordinary speech saturates to
  // black rather than sitting in the greys.
  var DB_FLOOR = -100;
  var DB_CEILING = -30;

  var PHI = (1 + Math.sqrt(5)) / 2;

  var micBtn = document.getElementById('micBtn');
  var clearBtn = document.getElementById('clearBtn');
  var rangeSelect = document.getElementById('rangeSelect');
  var plot = document.getElementById('plot');
  var canvas = document.getElementById('spectrogram');
  var axisCanvas = document.getElementById('axis');
  var gridlines = document.getElementById('gridlines');
  var cursor = document.getElementById('cursor');
  var idleMessage = document.getElementById('idleMessage');
  var nowLabel = document.getElementById('nowLabel');
  var hopMs = document.getElementById('hopMs');

  var ctx = canvas.getContext('2d', { alpha: false });
  var axisCtx = axisCanvas.getContext('2d');

  var audioCtx = null;
  var analyser = null;
  var stream = null;
  var bins = null;          // Uint8Array of the current frame's magnitudes
  var column = null;        // ImageData for the single column being drawn
  var running = false;
  var rafId = null;

  var dpr = 1;
  var pixelW = 0, pixelH = 0;   // canvas backing-store size
  var cssW = 0, cssH = 0;
  var maxColW = 0;              // scratch-buffer width, in backing-store pixels
  var pxPerSec = 0;             // CSS pixels of plot per second of audio
  var pendingPx = 0;            // sub-pixel remainder carried between frames
  var lastFrameMs = 0;
  var plotMs = 0;               // audio time drawn so far, in ms
  var nextTickMs = 0;           // plot time at which the next tick is due
  var cursorX = 0;              // left edge of the next column, in CSS pixels
  var filling = true;           // still sweeping left-to-right for the first time
  var frameTimes = [];          // recent frame timestamps, for the hop readout
  var frameCount = 0;

  var maxHz = Number(rangeSelect.value);

  /* --- layout ---------------------------------------------------------- */

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);

    // Golden-ratio box, per the repo style guide, clamped so the plot stays
    // usable on a phone and does not run off a laptop screen.
    var w = plot.clientWidth;
    var h = Math.max(200, Math.min(420, Math.round(w / PHI)));
    plot.style.height = h + 'px';

    cssW = w;
    cssH = h;
    pixelW = Math.round(w * dpr);
    pixelH = Math.round(h * dpr);
    maxColW = Math.max(1, Math.round(MAX_COLUMN_CSS_W * dpr));
    pxPerSec = cssW / WINDOW_SECONDS;

    canvas.width = pixelW;
    canvas.height = pixelH;
    column = ctx.createImageData(maxColW, pixelH);

    axisCanvas.width = Math.round(46 * dpr);
    axisCanvas.height = pixelH;
    axisCanvas.style.height = h + 'px';

    clear();
    drawAxis();
    updateHop();
  }

  function clear() {
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, pixelW, pixelH);
    cursorX = 0;
    filling = true;
    pendingPx = 0;
    lastFrameMs = 0;
    plotMs = 0;
    nextTickMs = 1000;
    positionCursor();
  }

  /* --- axes ------------------------------------------------------------ */

  // Ticks every 1 kHz below 5 kHz, every 2 kHz above: enough resolution where
  // voices and most bird song live, without crowding the top of the plot.
  function tickStep() {
    return maxHz <= 5000 ? 1000 : 2000;
  }

  function drawAxis() {
    var step = tickStep();
    axisCtx.clearRect(0, 0, axisCanvas.width, axisCanvas.height);
    axisCtx.fillStyle = '#777777';
    axisCtx.textAlign = 'right';
    axisCtx.textBaseline = 'middle';
    axisCtx.font = (11 * dpr) + 'px "Libre Franklin", Arial, sans-serif';

    gridlines.textContent = '';

    for (var hz = 0; hz <= maxHz; hz += step) {
      var frac = hz / maxHz;               // 0 at the bottom, 1 at the top
      var y = (1 - frac) * axisCanvas.height;
      var label = (hz / 1000) + (hz === maxHz ? ' kHz' : '');

      // Nudge the end labels inward so neither is clipped by the plot edge.
      var ty = Math.min(axisCanvas.height - 8 * dpr, Math.max(8 * dpr, y));
      axisCtx.fillText(label, axisCanvas.width - 6 * dpr, ty);

      if (hz > 0 && hz < maxHz) {
        var line = document.createElement('i');
        line.style.top = ((1 - frac) * 100) + '%';
        gridlines.appendChild(line);
      }
    }
  }

  // The hop -- how much time one stripe of pixels stands for -- is one frame,
  // so it is measured rather than assumed: frame rate varies by display and by
  // how busy the tab is.
  function updateHop() {
    var fps = 60;
    if (frameTimes.length > 10) {
      var span = frameTimes[frameTimes.length - 1] - frameTimes[0];
      if (span > 0) fps = (frameTimes.length - 1) / (span / 1000);
    }
    hopMs.textContent = Math.round(1000 / fps);
  }

  /* --- drawing --------------------------------------------------------- */

  // Paint one column: for every pixel row, find the frequency it stands for,
  // read that bin, and ink it. getByteFrequencyData has already mapped
  // [minDecibels, maxDecibels] onto 0..255, so the only work left is the
  // vertical mapping and the white-to-black ramp.
  function drawColumn(colW) {
    analyser.getByteFrequencyData(bins);

    var nyquist = audioCtx.sampleRate / 2;
    var topBin = Math.min(bins.length - 1, Math.floor((maxHz / nyquist) * bins.length));
    var data = column.data;

    for (var y = 0; y < pixelH; y++) {
      var frac = 1 - (y / (pixelH - 1));          // bottom row = 0 Hz
      var pos = frac * topBin;
      var i = Math.floor(pos);
      var lo = bins[i];
      var hi = bins[Math.min(topBin, i + 1)];
      var v = (lo + (hi - lo) * (pos - i)) / 255;  // 0..1 loudness

      // Gamma < 1 lifts the quiet detail (room tone, harmonics) that a linear
      // ramp would leave invisible on white.
      var ink = Math.pow(v, 0.75);
      var shade = Math.round(255 - ink * 255);

      // The scratch buffer is maxColW wide, so rows are strided by that even
      // when only the leftmost colW pixels of each row get painted.
      var p = y * maxColW * 4;
      for (var x = 0; x < colW; x++) {
        data[p]     = shade;
        data[p + 1] = shade;
        data[p + 2] = shade;
        data[p + 3] = 255;
        p += 4;
      }
    }

    var destX;
    if (filling) {
      destX = Math.round(cursorX * dpr);
      cursorX += colW / dpr;
      if (cursorX * dpr + colW > pixelW) filling = false;
    } else {
      // Scroll the whole plot left by this column's width, then draw at the
      // right edge. 'copy' lets the canvas be its own source without
      // compositing the old frame over the shifted one.
      ctx.globalCompositeOperation = 'copy';
      ctx.drawImage(canvas, -colW, 0);
      ctx.globalCompositeOperation = 'source-over';
      destX = pixelW - colW;
      cursorX = cssW - colW / dpr;
    }

    ctx.putImageData(column, destX, 0, 0, 0, colW, pixelH);
    return destX;
  }

  // One tick per second of elapsed time, painted into the plot so it scrolls
  // away with the audio it marks -- a tick is a moment, not a fixed place, so
  // it belongs on the canvas rather than in the static gridline overlay.
  // Faint down the middle so it never competes with the signal, solid at the
  // two edges where there is almost never anything to obscure.
  function drawTick(x) {
    var w = Math.max(1, Math.round(dpr));
    var cap = Math.round(7 * dpr);

    ctx.fillStyle = 'rgba(26, 26, 26, 0.16)';
    ctx.fillRect(x, 0, w, pixelH);
    ctx.fillStyle = '#1a1a1a';
    ctx.fillRect(x, 0, w, cap);
    ctx.fillRect(x, pixelH - cap, w, cap);
  }

  function positionCursor() {
    var x = Math.round(cursorX + 1);
    cursor.style.left = x + 'px';

    // The label sits to the left of the cursor once there is room for it, and
    // flips to the right while the cursor is still near the start of the plot.
    var NOW_LABEL_W = 26;
    if (x > NOW_LABEL_W + 10) {
      nowLabel.style.left = (x - NOW_LABEL_W - 4) + 'px';
    } else {
      nowLabel.style.left = (x + 5) + 'px';
    }
  }

  function frame(now) {
    rafId = requestAnimationFrame(frame);

    if (!lastFrameMs) {
      lastFrameMs = now;
      plotMs = 0;
      nextTickMs = 1000;
      return;
    }

    // Advance by however much time actually passed, capped so that returning to
    // a backgrounded tab redraws a sliver rather than the whole window.
    var elapsed = Math.min(now - lastFrameMs, 250);
    lastFrameMs = now;
    plotMs += elapsed;
    pendingPx += (elapsed / 1000) * pxPerSec;

    // While the plot is still filling left to right, never draw wider than the
    // space left: a column that ran off the right edge would be clipped, and
    // the time it stood for would vanish, putting a seam in the tick spacing at
    // the moment the plot switches over to scrolling.
    if (filling && cssW - cursorX < 1) filling = false;
    var room = filling ? Math.floor(cssW - cursorX) : MAX_COLUMN_CSS_W;

    var colCss = Math.min(Math.floor(pendingPx), MAX_COLUMN_CSS_W, room);
    if (colCss >= 1) {
      pendingPx -= colCss;
      var destX = drawColumn(Math.max(1, Math.round(colCss * dpr)));

      // Ticks count plot time, not wall-clock time. The two only agree while
      // frames arrive steadily; keying off the clock would let a stall push a
      // tick off the pixel grid, so the marks would no longer sit exactly one
      // second of plot apart.
      if (plotMs >= nextTickMs) {
        // Right edge of the column just drawn: the newest pixels, i.e. now.
        drawTick(destX + Math.round(colCss * dpr) - Math.max(1, Math.round(dpr)));
        nextTickMs += 1000;
      }

      positionCursor();
    }

    frameTimes.push(now);
    if (frameTimes.length > 90) frameTimes.shift();
    if (++frameCount % 30 === 0) updateHop();
  }

  /* --- microphone ------------------------------------------------------ */

  function showMessage(html, isError) {
    idleMessage.innerHTML = html;
    idleMessage.classList.toggle('error', !!isError);
    idleMessage.classList.remove('hidden');
  }

  function start() {
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
      showMessage('<p><b>No microphone access.</b> This browser does not expose ' +
        'getUserMedia, or the page is not on https:// or localhost.</p>', true);
      return;
    }

    micBtn.disabled = true;
    micBtn.textContent = '⏳ Starting…';

    // Every bit of "helpful" processing is off: gain control would flatten the
    // dynamics the plot is meant to show, and noise suppression would erase
    // exactly the faint background sounds that make a spectrogram interesting.
    navigator.mediaDevices.getUserMedia({
      audio: {
        echoCancellation: false,
        noiseSuppression: false,
        autoGainControl: false
      }
    }).then(function (s) {
      stream = s;
      audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      analyser = audioCtx.createAnalyser();
      analyser.fftSize = FFT_SIZE;
      // No temporal smoothing: a smoothed analyser blurs each column into the
      // one before it, which reads as vertical smear on a scrolling plot.
      analyser.smoothingTimeConstant = 0;
      analyser.minDecibels = DB_FLOOR;
      analyser.maxDecibels = DB_CEILING;

      audioCtx.createMediaStreamSource(stream).connect(analyser);
      bins = new Uint8Array(analyser.frequencyBinCount);

      idleMessage.classList.add('hidden');
      cursor.classList.add('live');
      nowLabel.classList.add('live');
      running = true;
      micBtn.disabled = false;
      micBtn.textContent = '⏹️ Stop (turn off microphone)';
      frameTimes = [];
      lastFrameMs = 0;
      rafId = requestAnimationFrame(frame);
    }).catch(function (err) {
      micBtn.disabled = false;
      micBtn.textContent = '▶️ Start (turn on microphone)';
      var reason = (err && err.name === 'NotAllowedError')
        ? 'The browser blocked microphone access. Allow it for this site and try again.'
        : 'Could not open the microphone (' + ((err && err.name) || 'unknown error') + ').';
      showMessage('<p><b>No signal.</b> ' + reason + '</p>', true);
    });
  }

  function stop() {
    running = false;
    if (rafId) cancelAnimationFrame(rafId);
    rafId = null;
    if (stream) stream.getTracks().forEach(function (t) { t.stop(); });
    stream = null;
    if (audioCtx) audioCtx.close();
    audioCtx = null;
    analyser = null;
    cursor.classList.remove('live');
    nowLabel.classList.remove('live');
    micBtn.textContent = '▶️ Start (turn on microphone)';
  }

  /* --- wiring ---------------------------------------------------------- */

  micBtn.addEventListener('click', function () {
    if (running) stop(); else start();
  });

  clearBtn.addEventListener('click', clear);

  rangeSelect.addEventListener('change', function () {
    maxHz = Number(rangeSelect.value);
    clear();
    drawAxis();
  });

  var resizeTimer = null;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(resize, 150);
  });

  window.addEventListener('pagehide', stop);

  resize();
})();
