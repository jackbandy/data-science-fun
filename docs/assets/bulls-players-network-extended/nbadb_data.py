"""Load the Chicago Bulls "played together" network from the Bulls nbadb extract.

NOTICE: this file was substantially drafted by an LLM coding system and has not
yet been thoroughly reviewed.

Source: datasets/bulls-players-nbadb/bulls_player_games.csv, one row per player
per Bulls game, extracted from nbadb (Wyatt Walsh), "NBA Database", Kaggle,
version 238, CC BY-SA 4.0 (see that folder's README). "Played" there means the
player appears in at least one Bulls play in the game's play-by-play.

Coverage, regular season plus playoffs: 1996-97 through 2022-23; the 2012-13
regular season is missing, and in other seasons roughly 5-15% of games have no
play-by-play.
"""

from __future__ import annotations

import collections
import csv
import itertools
from pathlib import Path

import networkx as nx

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA = REPO_ROOT / "datasets" / "bulls-players-nbadb" / "bulls_player_games.csv"


def load_games(path: Path = DATA):
    """{game id: set of player keys} and {game id: season start year}.

    Player keys are `<nba person id>__<name>`.
    """
    games = collections.defaultdict(set)
    season = {}
    with open(path) as f:
        for r in csv.DictReader(f):
            games[r["game_id"]].add(f"{r['player_id']}__{r['player_name']}")
            season[r["game_id"]] = int(r["season"][:4])
    return games, season


def build_graph(games) -> nx.Graph:
    """Players are nodes; edge weight = number of games both played for the Bulls."""
    together = collections.Counter()
    for players in games.values():
        together.update(itertools.combinations(sorted(players), 2))
    # Sorted insertion: node and edge order feed Louvain and the spring layout.
    G = nx.Graph()
    G.add_nodes_from(sorted({p for players in games.values() for p in players}))
    for (u, v), w in sorted(together.items()):
        G.add_edge(u, v, weight=w)
    return G


def display_name(player: str) -> str:
    return player.split("__", 1)[1]
