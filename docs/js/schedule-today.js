const todayLink = document.querySelector('.week-jump-today');

if (todayLink) {
  const now = new Date();
  const pad = (n) => String(n).padStart(2, '0');
  const todayId = `day-${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())}`;

  // Most days have no class, so jump to the next class day; ids are day-YYYY-MM-DD and sort as strings.
  const target = [...document.querySelectorAll('li[id^="day-"]')].find((day) => day.id >= todayId);

  if (target) {
    todayLink.querySelector('a').href = `#${target.id}`;
    todayLink.querySelector('.week-jump-today-date').textContent = now.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' });
    todayLink.hidden = false;
  }
}
