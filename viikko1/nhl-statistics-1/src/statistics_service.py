from player_reader import PlayerReader
from enum import Enum


class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


def sort_by_points(player):
    return player.points


def sort_by_enum_key(player, sortkey):
    if sortkey == SortBy.POINTS:
        return player.points
    elif sortkey == SortBy.GOALS:
        return player.goals
    elif sortkey == SortBy.ASSISTS:
        return player.assists
    else:
        raise ValueError("Invalid SortBy provided")


class StatisticsService:
    def __init__(self, player_reader):
        reader = player_reader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_enum=SortBy.POINTS):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=lambda player: sort_by_enum_key(
                player, sort_enum)
        )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result
