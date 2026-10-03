// NOTICE: Moved verbatim out of an inline <script> in exercises.html by an LLM coding
// system (Claude Code), so the Content-Security-Policy can drop 'unsafe-inline'.

// "Read more" reveals the blurb generated from exercises/exercises-about.md.
// Without scripting the blurb stays hidden and the five cards -- the point of
// the page -- are still all there.
(function () {
  var toggle = document.getElementById("readMoreToggle");
  var about = document.getElementById("exercisesAbout");
  if (!toggle || !about) return;
  toggle.addEventListener("click", function () {
    var expanded = toggle.getAttribute("aria-expanded") === "true";
    toggle.setAttribute("aria-expanded", String(!expanded));
    about.hidden = expanded;
    toggle.textContent = expanded ? "Read more" : "Read less";
  });
})();
