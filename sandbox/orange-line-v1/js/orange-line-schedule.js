// ════════════════════════════════════════════════════════════
//  STATION DATA  ←  Edit weeks, names, or closed status here
//
//  Canvas: 648 × 220px
//
//  Loop geometry (single bordered rectangle, border=14px, radius=16px):
//    left=432, top=76, width=200, height=103   box-sizing:border-box
//    → left-edge center  x=439  (432+7)
//    → right-edge center x=625  (432+200−7)
//    → top-edge center   y=83   (76+7)
//    → bottom-edge center y=172 (76+103−7)  matches branch center exactly
//
//  Branch track: top=165, height=14 → center y=172
//  Branch starts at x=14 (left edge of Midway dot) so the line ends at the dot.
//
//  Dot positioning uses transform:translate(-50%,-50%) on left/top = center coords.
//
//  Each station entry:
//    id           – unique key (kebab-case)
//    name         – display name
//    x, y         – pixel center of the dot
//    week         – tooltip label shown on hover
//    transfer     – true  → filled black dot (major transfer)
//    closed       – true  → grayed dot + closed warning
//    closedUntil  – year string (requires closed:true)
//    parking      – true  → "P" box below station
//    airport      – true  → ✈ icon below station
//    tipLeft      – true  → tooltip appears to the LEFT of cursor (loop stations)
// ════════════════════════════════════════════════════════════
const STATIONS = [
  // ── Midway branch (Week 15 → Week 8, reading right to left) ─
  { id: 'midway',            name: 'Midway',                    x:  20, y: 172, week: 'Week 15', parking: true },
  { id: 'pulaski',           name: 'Pulaski',                   x:  76, y: 172, week: 'Week 14', parking: true },
  { id: 'kedzie',            name: 'Kedzie',                    x: 132, y: 172, week: 'Week 13', parking: true },
  { id: 'western',           name: 'Western',                   x: 188, y: 172, week: 'Week 12', parking: true },
  { id: '35th-archer',       name: '35th/Archer',               x: 244, y: 172, week: 'Week 11', parking: true },
  { id: 'ashland',           name: 'Ashland',                   x: 300, y: 172, week: 'Week 10' },
  { id: 'halsted',           name: 'Halsted',                   x: 356, y: 172, week: 'Week 9'  },
  // Roosevelt is before/outside the loop on the branch
  { id: 'roosevelt',         name: 'Roosevelt',                 x: 398, y: 172, week: 'Week 8',  transfer: true },
  // ── Loop – clockwise: up the left, right on top, down the right, left on bottom ──
  //    tipLeft:true → tooltip renders to the left of cursor
  { id: 'harold-washington', name: 'Harold Washington Library', x: 439, y: 148, week: 'Week 1',  tipLeft: true, transfer: true },
  { id: 'lasalle-van-buren', name: 'LaSalle/Van Buren',         x: 439, y: 116, week: 'Week 2',  tipLeft: true },
  { id: 'quincy',            name: 'Quincy',                    x: 480, y:  83, week: 'Week 3',  tipLeft: true },
  { id: 'washington-wells',  name: 'Washington/Wells',          x: 556, y:  83, week: 'Week 4',  tipLeft: true, transfer: true },
  { id: 'clark-lake',        name: 'Clark/Lake',                x: 625, y: 112, week: 'Week 5',  tipLeft: true, transfer: true },
  { id: 'state-lake',        name: 'State/Lake',                x: 625, y: 148, closed: true, closedUntil: '2029', tipLeft: true, transfer: true },
  { id: 'washington-wabash', name: 'Washington/Wabash',         x: 560, y: 172, week: 'Week 6',  tipLeft: true },
  { id: 'adams-wabash',      name: 'Adams/Wabash',              x: 490, y: 172, week: 'Week 7',  tipLeft: true, transfer: true },
];

// ════════════════════════════════════════════════════════════
//  RENDER  (no edits needed below this line)
// ════════════════════════════════════════════════════════════
const map = document.getElementById('ol-map');
const tip = document.getElementById('ol-tooltip');

// ── Midway branch track (horizontal) ─────────────────────────
// Starts at x=14 (left edge of Midway dot) so the line ends AT the dot.
// center y = 167 + 5 = 172
const branch = document.createElement('div');
branch.className = 'ol-track';
branch.style.cssText = 'left:14px;top:165px;width:458px;height:14px;';
map.appendChild(branch);

// ── Loop rectangle with rounded corners ──────────────────────
// top=78, height=99 → top center=83, bottom center=172; matches branch center.
// right outer edge=632, right center=627; dots placed at x=622 (inner edge).
const loop = document.createElement('div');
loop.className = 'ol-loop';
loop.style.cssText = 'left:432px;top:76px;width:200px;height:103px;';
map.appendChild(loop);

// ── Single direction chevron on each loop track ───────────────
// Clockwise: top track → RIGHT (❯), bottom track → LEFT (❮)
// Centered between the two dots on each side.
// Top: between Quincy (480) and Washington/Wells (556) → x=518, y=83
// Bottom: between Adams/Wabash (490) and Washington/Wabash (560) → x=525, y=172
function addChevron(char, x, y) {
  const el = document.createElement('div');
  el.className = 'ol-arrow';
  el.style.cssText = `left:${x}px; top:${y}px;`;
  el.textContent = char;
  map.appendChild(el);
}
addChevron('❯', 518,  83);
addChevron('❮', 525, 172);

// ── Tooltip logic ─────────────────────────────────────────────
function attachTooltip(el, s) {
  el.addEventListener('mouseover', () => {
    if (s.closed) {
      tip.innerHTML =
        `<span class="tip-name">${s.name}</span><br>` +
        `<span class="tip-closed">⚠ Closed — reopening ${s.closedUntil}</span>`;
    } else {
      tip.innerHTML =
        `<span class="tip-name">${s.name}</span> ` +
        `<span class="tip-week">— ${s.week}</span>`;
    }
    tip.style.display = 'block';
  });
  el.addEventListener('mousemove', e => {
    if (s.tipLeft) {
      tip.style.left = (e.clientX - tip.offsetWidth - 14) + 'px';
    } else {
      tip.style.left = (e.clientX + 14) + 'px';
    }
    tip.style.top = (e.clientY - 40) + 'px';
  });
  el.addEventListener('mouseout', () => { tip.style.display = 'none'; });
}

// ── Render each station ───────────────────────────────────────
// Dots use transform:translate(-50%,-50%) so left/top are the exact center coords.
STATIONS.forEach(s => {
  const sz = 12;

  const dot = document.createElement('div');
  dot.className = 'ol-station'
    + (s.transfer ? ' transfer' : '')
    + (s.closed   ? ' closed'   : '');
  dot.style.cssText =
    `left:${s.x}px; top:${s.y}px; width:${sz}px; height:${sz}px;` +
    `transform:translate(-50%,-50%);`;
  dot.setAttribute('aria-label',
    s.closed ? `${s.name} – Closed until ${s.closedUntil}` : `${s.name} – ${s.week}`);
  dot.setAttribute('tabindex', '0');
  map.appendChild(dot);
  attachTooltip(dot, s);

  if (s.parking) {
    const p = document.createElement('div');
    p.className = 'ol-parking';
    p.textContent = 'P';
    p.style.left = (s.x - 6) + 'px';
    p.style.top  = '190px';
    map.appendChild(p);
  }
});


