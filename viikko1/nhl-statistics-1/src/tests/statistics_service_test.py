import unittest
from statistics_service import StatisticsService, SortBy
from statistics_service import sort_by_points
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        player = self.stats.search("Lemieux")
        self.assertEqual(player.name, "Lemieux")

    def test_search_not_found(self):
        player = self.stats.search("Selänne")
        self.assertIsNone(player)

    def test_sort_by_points(self):
        player = self.stats.search("Kurri")
        points = sort_by_points(player)
        self.assertEqual(points, 37+53)

    def test_team(self):
        team = self.stats.team("EDM")
        self.assertEqual(len(team), 3)
        for player in team:
            self.assertEqual(player.team, "EDM")
            self.assertIn(player.name, ["Semenko", "Kurri", "Gretzky"])

    def test_top_default(self):
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")

    def test_top_points(self):
        top_players = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")

    def test_top_goals(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Lemieux")
        self.assertEqual(top_players[1].name, "Yzerman")
        self.assertEqual(top_players[2].name, "Kurri")

    def test_top_assists(self):
        top_players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Yzerman")
        self.assertEqual(top_players[2].name, "Lemieux")

    def test_top_invalid_enum(self):
        with self.assertRaises(ValueError):
            top_players = self.stats.top(3, 1)
