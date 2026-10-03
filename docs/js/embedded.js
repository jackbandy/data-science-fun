// NOTICE: Moved out of identical inline <script> blocks in timer/index.html and
// spectrogram/index.html by an LLM coding system (Claude Code), so the
// Content-Security-Policy can drop 'unsafe-inline'. Loaded in <head> by both.

// Embedded in an iframe (the course slides) the attribution footer is noise,
// and the viewer has no way out of the frame. Swap it for a link to the real
// page. Set in <head> so the footer never flashes before it is hidden.
if (window.self !== window.top) {
  document.documentElement.classList.add('embedded');
  document.addEventListener('DOMContentLoaded', function () {
    // Point at whatever copy of the page is actually framed, so this works
    // from the deployed site and from a local build alike.
    document.getElementById('openStandalone').href = window.location.href;
  });
}

