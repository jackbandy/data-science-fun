# Chicago Bulls Players per Game, 1996–2023

_NOTICE: this file and the extract were substantially drafted by an LLM coding system and have not yet been thoroughly reviewed._

Every Chicago Bulls player who appeared in each Bulls game's play-by-play, regular season and playoffs, 1996–97 through 2022–23. One row per player per game. Extracted from the nbadb "NBA Database" by Wyatt Walsh. For educational purposes only.

## Files

- `bulls_player_games.csv` (1.2 MB): 20,027 rows, 1,942 games, 234 players
- `extract_bulls.py`: rebuilds the CSV from the full database (`python3 datasets/bulls-players-nbadb/extract_bulls.py`)

## Columns

| Column | Description |
|---|---|
| `game_id` | NBA stats game ID, e.g. `0029600001`; the third digit is the game type (2 regular season, 4 playoffs) and the next two are the season |
| `season` | Season, e.g. `1996-97` |
| `season_type` | `regular` or `playoffs` |
| `game_date` | Game date, `YYYY-MM-DD` |
| `player_id` | NBA stats person ID |
| `player_name` | Player name as given in the play-by-play |

## How "played" is defined

The database has no player box scores, so a player is listed for a game if they appear as player 1, 2, or 3 in at least one play credited to the Bulls (a shot, rebound, foul, turnover, substitution, and so on). A player who was on the floor but never took part in a recorded play is missed; since entering the game is itself recorded as a substitution, that is rare.

## Coverage gaps

- Play-by-play starts in 1996–97, so earlier seasons (including most of the Jordan era) are not included.
- The 2012–13 regular season is missing from the database; only 10 playoff games from that season are here.
- In other seasons, about 5–15% of Bulls games have no play-by-play (the 1998–99 lockout season had 50 games; 42 are here).

## Source and license

- nbadb (Wyatt Walsh), "NBA Database," Kaggle, version 238 (June 29, 2026): https://www.kaggle.com/datasets/wyattowalsh/basketball. Built from the NBA stats API by https://github.com/wyattowalsh/nbadb.
- The Kaggle dataset is licensed **CC BY-SA 4.0** (https://creativecommons.org/licenses/by-sa/4.0/). This extract is a derivative and is shared under the same license.
- The full database (`nba.sqlite`, 2.3 GB) is not committed; `extract_bulls.py` expects it at `datasets/nbadb/nba.sqlite` (gitignored).

## Used in

- `docs/assets/bulls-players-network-extended/`: the Bulls "played together" network and its communities.

## Disclaimers

- For educational purposes only.
- Accuracy, completeness, etc. not guaranteed.
