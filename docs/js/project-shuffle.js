// NOTICE: Moved verbatim out of an inline <script> in project/index.html by an LLM coding
// system (Claude Code), so the Content-Security-Policy can drop 'unsafe-inline'.

// Shuffle on every load so no group is always listed first.
(function () {
  var cells = Array.prototype.slice.call(document.querySelectorAll('.project-gallery td'))
    .filter(function (td) { return td.firstElementChild; });
  var links = cells.map(function (td) { return td.firstElementChild; });
  for (var i = links.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var t = links[i]; links[i] = links[j]; links[j] = t;
  }
  cells.forEach(function (td, k) { td.appendChild(links[k]); });
})();
