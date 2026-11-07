#!/usr/bin/env python3
"""Extract every Chicago Bulls player-game from the nbadb NBA database.

NOTICE: this file was substantially drafted by an LLM coding system and has not
yet been thoroughly reviewed.

Input:  datasets/nbadb/nba.sqlite (2.3 GB, gitignored), from nbadb (Wyatt Walsh),
        "NBA Database", Kaggle, version 238, CC BY-SA 4.0,
        https://www.kaggle.com/datasets/wyattowalsh/basketball
Output: bulls_player_games.csv, one row per player per Bulls game they played in.

The database has no player box scores, so "played" comes from play-by-play: a
player is listed for a game if they appear as player 1, 2, or 3 in any play
credited to the Bulls. Regular season and playoffs only.

Usage:  python3 datasets/bulls-players-nbadb/extract_bulls.py
"""

from __future__ import annotations

import csv
import sqlite3
from pathlib import Path

HERE = Path(__file__).resolve().parent
DB = HERE.parent / "nbadb" / "nba.sqlite"
OUT = HERE / "bulls_player_games.csv"
BULLS = "1610612741.0"                       # team ids are stored as text floats
SEASON_TYPE = {"2": "regular", "4": "playoffs"}


def season_label(game_id: str) -> str:
    """`0029600001` -> `1996-97`."""
    yy = int(game_id[3:5])
    start = 1900 + yy if yy >= 46 else 2000 + yy
    return f"{start}-{str(start + 1)[-2:]}"


def main():
    if not DB.exists():
        raise SystemExit(f"Missing {DB}; download nba.sqlite from "
                         "https://www.kaggle.com/datasets/wyattowalsh/basketball")
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    plays = " UNION ".join(
        f"SELECT game_id, player{i}_id AS pid, player{i}_name AS name FROM play_by_play "
        f"WHERE player{i}_team_id = ? AND player{i}_id IS NOT NULL"
        for i in (1, 2, 3))
    rows = con.execute(plays, (BULLS,) * 3).fetchall()
    dates = dict(con.execute("SELECT game_id, substr(game_date, 1, 10) FROM game"))
    con.close()
    out = sorted({(g, str(int(float(p))), n) for g, p, n in rows if g[2] in SEASON_TYPE and n},
                 key=lambda r: (r[0], r[2]))
    with open(OUT, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["game_id", "season", "season_type", "game_date", "player_id", "player_name"])
        for g, pid, name in out:
            w.writerow([g, season_label(g), SEASON_TYPE[g[2]], dates.get(g, ""), pid, name])
    games = len({r[0] for r in out})
    print(f"wrote {OUT.name}: {len(out)} player-games, {games} games, "
          f"{len({r[1] for r in out})} players")


if __name__ == "__main__":
    main()
