/* NOTICE: This file was created by an LLM coding system (Claude, August 2026). */
/* Shuffle behavior for /ideas/.
 *
 * Every card is already in the DOM (rendered from _data/ideas.json at build
 * time), so this file only decides which one is visible. Draws come from a
 * shuffled deck rather than an independent random pick each press: an
 * independent pick repeats often enough to feel broken on a deck this small,
 * while a deck guarantees you see all of them before any of them twice.
 *
 * The current card's index goes in the URL hash so a draw can be linked to or
 * reloaded; landing on such a link deals that card first.
 */
(function () {
  "use strict";

  var deckEl = document.getElementById("ideas-deck");
  var button = document.getElementById("ideas-shuffle");
  var progress = document.getElementById("ideas-progress");
  if (!deckEl || !button) return;

  var cards = Array.prototype.slice.call(deckEl.querySelectorAll(".idea-card"));
  if (cards.length === 0) return;

  cards.forEach(function (card, i) { card.id = "idea-" + (i + 1); });

  var order = [];      // remaining indices in this pass, popped from the end
  // The build already reveals the first card, so the stack starts there.
  var current = cards.findIndex(function (c) { return !c.hidden; });
  if (current < 0) current = 0;
  var drawn = 0;       // how many of this round have been dealt

  function reshuffle(exclude) {
    order = cards.map(function (_, i) { return i; })
                 .filter(function (i) { return i !== exclude; });
    // Fisher-Yates
    for (var i = order.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = order[i]; order[i] = order[j]; order[j] = t;
    }
    drawn = 0;
  }

  function show(index, updateHash) {
    if (current === index) return;
    if (current >= 0) cards[current].hidden = true;
    cards[index].hidden = false;
    current = index;
    if (updateHash) {
      // replaceState keeps the Back button pointing at the page you arrived
      // from, not at a trail of every card you shuffled through.
      if (window.history && window.history.replaceState) {
        window.history.replaceState(null, "", "#" + cards[index].id);
      } else {
        window.location.hash = cards[index].id;
      }
    }
    render();
  }

  function render() {
    if (!progress) return;
    // Total is the size of *this* round, which is one short of the deck
    // whenever the round started by excluding the card already on screen.
    var roundSize = drawn + order.length;
    progress.textContent = roundSize > 1 ? drawn + " of " + roundSize + " this round" : "";
  }

  function draw() {
    if (order.length === 0) reshuffle(current);
    if (order.length === 0) return;   // single-card deck: nothing to draw
    drawn++;
    show(order.pop(), true);
  }

  button.addEventListener("click", draw);

  // A linked card deals first; otherwise start on a random one so the page is
  // not always the same idea.
  var fromHash = cards.indexOf(document.getElementById(window.location.hash.slice(1)));
  reshuffle(current);
  if (fromHash >= 0) {
    order = order.filter(function (i) { return i !== fromHash; });
    drawn = 1;
    show(fromHash, false);
    render();   // show() no-ops when the linked card is the one already on screen
  } else {
    draw();
  }
})();
