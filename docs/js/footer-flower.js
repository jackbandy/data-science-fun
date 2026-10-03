// NOTICE: Moved verbatim out of an inline <script> in _includes/footer.html by an LLM coding
// system (Claude Code), so the Content-Security-Policy can drop 'unsafe-inline'.

(function () {
  var link = document.querySelector('.footer-flower');
  if (!link || !link.animate) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var flower = link.querySelector('img');
  var spin = flower.animate(
    [{ transform: 'rotate(0deg)' }, { transform: 'rotate(360deg)' }],
    { duration: 8000, iterations: Infinity, easing: 'linear' }
  );
  spin.pause();

  link.addEventListener('mouseenter', function () { spin.play(); });
  link.addEventListener('mouseleave', function () { spin.pause(); });
  link.addEventListener('focus', function () { spin.play(); });
  link.addEventListener('blur', function () { spin.pause(); });
})();
