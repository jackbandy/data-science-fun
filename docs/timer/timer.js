---
---
/* NOTICE: This file was substantially generated/modified by an LLM.
   Adapted from jackbandy.com/extras/cta-style-timer, reworked for the Orange Line. */

(function() {
  // Orange Line stops in service order for a train heading toward Midway:
  // clockwise around the inner Loop (Van Buren > Wells > Lake > Wabash), then
  // south to Midway. State/Lake is listed but not selectable — it is closed for
  // reconstruction until 2029, so no train stops there.
  var stations = [
    "Harold Washington Library","LaSalle/Van Buren","Quincy",
    "Washington/Wells","Clark/Lake","State/Lake","Washington/Wabash",
    "Adams/Wabash","Roosevelt","Halsted","Ashland","35th/Archer","Western",
    "Kedzie","Pulaski","Midway"
  ];

  var closedStations = {
    "State/Lake": "Closed for reconstruction"
  };

  // Class date -> station, from _data/schedule.csv and _data/stations.yml
  // (the same source the homepage schedule table renders from). Used below
  // to default the picker to whichever stop is nearest to today.
  var scheduleStations = [
    {%- for row in site.data.schedule -%}
    {%- assign station = site.data.stations[row.Week] -%}
    { date: "{{ row.Date }}", station: "{{ station }}" }{% unless forloop.last %},{% endunless %}
    {%- endfor %}
  ];

  // When today is more than this many days from the nearest class date
  // (e.g. over a break, or before/after the semester), fall back to the
  // Orange Line's last stop rather than guessing at a class week.
  var FALLBACK_STATION = 'Midway';
  var FALLBACK_THRESHOLD_DAYS = 16;

  function nearestScheduledStation() {
    var today = new Date();
    today.setHours(0, 0, 0, 0);
    var bestStation = null;
    var bestDiffDays = Infinity;
    scheduleStations.forEach(function(entry) {
      var diffDays = Math.abs(new Date(entry.date + 'T00:00:00') - today) / 86400000;
      if (diffDays < bestDiffDays) {
        bestDiffDays = diffDays;
        bestStation = entry.station;
      }
    });
    if (bestStation === null || bestDiffDays > FALLBACK_THRESHOLD_DAYS) return FALLBACK_STATION;
    return bestStation;
  }

  var DEFAULT_STATION = nearestScheduledStation();

  var select = document.getElementById('minuteSelect');
  var customWrapper = document.getElementById('customMinutesWrapper');
  var customInput = document.getElementById('customMinutes');
  var startBtn = document.getElementById('startBtn');
  var timerDisplay = document.getElementById('timerDisplay');
  var stationName = document.getElementById('stationName');
  var infoBtn = document.getElementById('infoBtn');
  var stationPicker = document.getElementById('stationPicker');
  var intervalId = null;
  var remainingSeconds = 0;
  var running = false;

  stations.forEach(function(name) {
    var btn = document.createElement('button');
    btn.textContent = name;

    if (closedStations[name]) {
      btn.classList.add('closed');
      btn.disabled = true;
      btn.title = closedStations[name];
      stationPicker.appendChild(btn);
      return;
    }

    if (name === DEFAULT_STATION) btn.classList.add('active');
    btn.addEventListener('click', function() {
      stationName.textContent = name;
      stationPicker.querySelectorAll('button').forEach(function(b) {
        b.classList.remove('active');
      });
      btn.classList.add('active');
      stationPicker.classList.remove('visible');
    });
    stationPicker.appendChild(btn);
  });

  stationName.textContent = DEFAULT_STATION;

  infoBtn.addEventListener('click', function() {
    if (!running) stationPicker.classList.toggle('visible');
  });

  select.addEventListener('change', function() {
    if (select.value === 'custom') {
      customWrapper.classList.add('visible');
      customInput.focus();
    } else {
      customWrapper.classList.remove('visible');
    }
  });

  function getMinutes() {
    if (select.value === 'custom') {
      var val = parseInt(customInput.value, 10);
      return val > 0 ? val : 0;
    }
    return parseInt(select.value, 10);
  }

  function setDisabled(disabled) {
    select.disabled = disabled;
    customInput.disabled = disabled;
    infoBtn.disabled = disabled;
    if (disabled) stationPicker.classList.remove('visible');
  }

  function updateDisplay() {
    if (remainingSeconds <= 0) {
      timerDisplay.innerHTML = '<span class="ea-line-time-big">Due</span>';
      clearInterval(intervalId);
      intervalId = null;
      return;
    }
    var minutes = Math.ceil(remainingSeconds / 60);
    if (minutes <= 1) {
      timerDisplay.innerHTML = '<span class="ea-line-time-big">&lt;1</span> min';
    } else {
      timerDisplay.innerHTML = '<span class="ea-line-time-big">' + minutes + '</span> min';
    }
  }

  startBtn.addEventListener('click', function() {
    if (running) {
      clearInterval(intervalId);
      intervalId = null;
      running = false;
      remainingSeconds = 0;
      startBtn.textContent = 'Start';
      setDisabled(false);
      updateDisplay();
    } else {
      var minutes = getMinutes();
      if (minutes <= 0) return;
      running = true;
      startBtn.textContent = 'Reset';
      setDisabled(true);
      remainingSeconds = minutes * 60;
      updateDisplay();
      intervalId = setInterval(function() {
        remainingSeconds--;
        updateDisplay();
      }, 1000);
    }
  });

  customInput.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') startBtn.click();
  });
})();
