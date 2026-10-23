#!/usr/bin/env python3
"""Build center-fielders.csv from three Baseball Savant leaderboards (2026 season).

NOTICE: this file was substantially drafted by an LLM coding system and has not
yet been reviewed.

1. Outs Above Average, qualified center fielders (pos=8): who is in the table.
2. Custom batter leaderboard, 100+ PA: hitting and running rates.
3. Arm strength: average throw speed from center field.

Joined on Savant's player_id. Run with:  python3 -I collect.py
"""

import csv
import io
import urllib.request
from pathlib import Path

YEAR = 2026
OUT = Path(__file__).resolve().parent / "center-fielders.csv"
SAVANT = "https://baseballsavant.mlb.com/leaderboard"

OAA_URL = (f"{SAVANT}/outs_above_average?type=Fielder&startYear={YEAR}&endYear={YEAR}"
           "&split=no&team=&range=year&min=q&pos=8&roles=&viz=hide&csv=true")
BAT_COLS = ["pa", "home_run", "k_percent", "bb_percent", "oz_swing_percent", "whiff_percent",
            "isolated_power", "barrel_batted_rate", "hard_hit_percent", "sprint_speed",
            "r_total_stolen_base"]
BAT_URL = (f"{SAVANT}/custom?year={YEAR}&type=batter&filter=&min=100&selections="
           + ",".join(BAT_COLS) + "&chart=false&csv=true")
ARM_URL = f"{SAVANT}/arm-strength?type=player&year={YEAR}&minThrows=50&pos=8&team=&csv=true"

# output column <- (source table, source column)
COLUMNS = {
    "player": ("oaa", "last_name, first_name"),
    "team": ("oaa", "display_team_name"),
    "pa": ("bat", "pa"),
    "hr": ("bat", "home_run"),
    "k_pct": ("bat", "k_percent"),
    "bb_pct": ("bat", "bb_percent"),
    "chase_pct": ("bat", "oz_swing_percent"),
    "whiff_pct": ("bat", "whiff_percent"),
    "iso": ("bat", "isolated_power"),
    "barrel_pct": ("bat", "barrel_batted_rate"),
    "hard_hit_pct": ("bat", "hard_hit_percent"),
    "sprint_speed": ("bat", "sprint_speed"),
    "sb": ("bat", "r_total_stolen_base"),
    "oaa": ("oaa", "outs_above_average"),
    "arm_mph": ("arm", "arm_cf"),
}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        text = resp.read().decode("utf-8-sig")
    return {row["player_id"]: row for row in csv.DictReader(io.StringIO(text))}


def main():
    tables = {"oaa": fetch(OAA_URL), "bat": fetch(BAT_URL), "arm": fetch(ARM_URL)}
    rows, dropped = [], []
    for pid in tables["oaa"]:
        if not all(pid in t and t[pid] for t in tables.values()):
            dropped.append(tables["oaa"][pid]["last_name, first_name"])
            continue
        row = {"player_id": pid}
        for out, (src, col) in COLUMNS.items():
            row[out] = tables[src][pid][col].strip()
        if not all(row.values()):
            dropped.append(row["player"])
            continue
        rows.append(row)
    rows.sort(key=lambda r: r["player"])
    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["player_id", *COLUMNS])
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} center fielders to {OUT.name}")
    if dropped:
        print(f"dropped (missing from a leaderboard): {'; '.join(dropped)}")


if __name__ == "__main__":
    main()
