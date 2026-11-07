"""Load the Chicago Bulls co-play network from the shared-success sports data.

NOTICE: this file was substantially drafted by an LLM coding system and has not
yet been thoroughly reviewed.

Source: datasets/shared-success-sports/upstream (a local, gitignored clone of
https://github.com/smukherjee0305/Skills_Shared_Success_Sports; see
datasets/shared-success-sports/README.md for how to get it).

`nba_matchid_playerid_playernames_date_of_play.txt` has one whitespace-separated
record per player per game: match ID, `<espn id>__<name>`, team, home/away,
date, time. About 100 lines run several records together, and all but the last
record on such a line lose their home/away and date fields; those records are
recovered here (the date comes from `nba_matchid_datetime.txt`).

The per-game lists look like rosters rather than only the players who got
minutes, so "played a game together" here means "were on the Bulls roster for
the same game".
"""

from __future__ import annotations

import collections
import itertools
from pathlib import Path

import networkx as nx

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = (REPO_ROOT / "datasets" / "shared-success-sports" / "upstream"
            / "Data" / "NBA" / "flatfiles")
TEAM = "chicago_bulls"


def season_of(date: str) -> int:
    """Start year of the NBA season a date falls in (Aug-Dec -> that year)."""
    return int(date[:4]) if date[5:7] >= "08" else int(date[:4]) - 1


def load_games(data_dir: Path = DATA_DIR):
    """{match id: set of player keys} and {match id: season start year} for the Bulls."""
    if not data_dir.exists():
        raise SystemExit(f"Missing {data_dir}; clone the data first "
                         "(see datasets/shared-success-sports/README.md).")
    match_date = {}
    with open(data_dir / "nba_matchid_datetime.txt") as f:
        next(f)
        for line in f:
            match, stamp, _ = line.strip().split("|")
            match_date[match] = stamp[:10]
    games = collections.defaultdict(set)
    season = {}
    with open(data_dir / "nba_matchid_playerid_playernames_date_of_play.txt") as f:
        for line in f:
            tokens, i = line.split(), 0
            while i < len(tokens):
                match, player, team = tokens[i:i + 3]
                i += 3
                date = None
                if i < len(tokens) and tokens[i] in ("home", "away"):
                    date = tokens[i + 1]
                    i += 3
                if team == TEAM:
                    games[match].add(player)
                    season[match] = season_of(date or match_date[match])
    return games, season


def build_graph(games) -> nx.Graph:
    """Players are nodes; edge weight = number of games both were on the roster."""
    together = collections.Counter()
    for players in games.values():
        together.update(itertools.combinations(sorted(players), 2))
    # Sorted insertion: node and edge order feed Louvain and the spring layout,
    # and set iteration order changes between Python runs.
    G = nx.Graph()
    G.add_nodes_from(sorted({p for players in games.values() for p in players}))
    for (u, v), w in sorted(together.items()):
        G.add_edge(u, v, weight=w)
    return G


def espn_id(player: str) -> str:
    return player.split("__", 1)[0]


def display_name(player: str) -> str:
    """`3224__joakim_noah` -> `Joakim Noah` (keeps initials like `A.J.` readable)."""
    special = {"aj": "A.J.", "cj": "C.J.", "dj": "D.J.", "jj": "J.J.", "pj": "P.J.", "tj": "T.J.",
               "ii": "II", "iii": "III", "iv": "IV", "jr": "Jr.", "jr.": "Jr."}
    words = player.split("__", 1)[1].split("_")
    return " ".join(special.get(w) or (w.upper() if w.endswith(".") else w[:1].upper() + w[1:])
                    for w in words)
