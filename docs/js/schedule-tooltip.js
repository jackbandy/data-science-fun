const scheduleTip = document.getElementById('schedule-tooltip');

if (scheduleTip) {
  function clearTip() {
    scheduleTip.replaceChildren();
  }

  function appendSpan(className, text) {
    const span = document.createElement('span');
    span.className = className;
    span.textContent = text;
    scheduleTip.appendChild(span);
  }

  function appendBreak() {
    scheduleTip.appendChild(document.createElement('br'));
  }

  function renderClosedTip(name, closedUntil) {
    clearTip();
    appendSpan('tip-name', name);
    appendBreak();
    appendSpan('tip-closed', `⚠ Closed — reopening ${closedUntil}`);
  }

  function renderWeekTip(name, week) {
    clearTip();
    appendSpan('tip-name', name);
    scheduleTip.appendChild(document.createTextNode(' — '));
    appendSpan('tip-week', week);
  }

  document.querySelectorAll('.schedule-map-station:not(.static)').forEach((dot) => {
    function showTip() {
      if (dot.dataset.closed === 'true') {
        renderClosedTip(dot.dataset.name, dot.dataset.closedUntil);
      } else {
        renderWeekTip(dot.dataset.name, dot.dataset.week);
      }
      scheduleTip.style.display = 'block';
    }

    function moveTip(event) {
      if (dot.classList.contains('tip-left')) {
        scheduleTip.style.left = `${event.clientX - scheduleTip.offsetWidth - 14}px`;
      } else {
        scheduleTip.style.left = `${event.clientX + 14}px`;
      }
      scheduleTip.style.top = `${event.clientY - 40}px`;
    }

    dot.addEventListener('mouseover', showTip);
    dot.addEventListener('mousemove', moveTip);
    dot.addEventListener('mouseout', () => {
      scheduleTip.style.display = 'none';
    });
    dot.addEventListener('focus', () => {
      const rect = dot.getBoundingClientRect();
      showTip();
      scheduleTip.style.left = dot.classList.contains('tip-left')
        ? `${rect.left - scheduleTip.offsetWidth - 14}px`
        : `${rect.right + 14}px`;
      scheduleTip.style.top = `${rect.top - 8}px`;
    });
    dot.addEventListener('blur', () => {
      scheduleTip.style.display = 'none';
    });
  });

  document.querySelectorAll('.schedule-week-dot').forEach((dot) => {
    const [week, stop] = dot.dataset.label.split(', ');

    function showTip(event) {
      renderWeekTip(week, stop);
      scheduleTip.style.left = `${event.clientX + 14}px`;
      scheduleTip.style.top = `${event.clientY - 40}px`;
      scheduleTip.style.display = 'block';
    }

    function moveTip(event) {
      scheduleTip.style.left = `${event.clientX + 14}px`;
      scheduleTip.style.top = `${event.clientY - 40}px`;
    }

    dot.addEventListener('mouseover', showTip);
    dot.addEventListener('mousemove', moveTip);
    dot.addEventListener('mouseout', () => {
      scheduleTip.style.display = 'none';
    });
    dot.addEventListener('focus', () => {
      const rect = dot.getBoundingClientRect();
      renderWeekTip(week, stop);
      scheduleTip.style.left = `${rect.right + 14}px`;
      scheduleTip.style.top = `${rect.top - 8}px`;
      scheduleTip.style.display = 'block';
    });
    dot.addEventListener('blur', () => {
      scheduleTip.style.display = 'none';
    });
  });
}
