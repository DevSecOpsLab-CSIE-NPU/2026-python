"""Tests for Big Two game logic."""

import unittest
from game.game import BigTwoGame
from game.models import Card


class TestBigTwoGame(unittest.TestCase):
    def setUp(self):
        self.game = BigTwoGame()

    def test_setup(self):
        self.game.setup()
        self.assertEqual(len(self.game.players), 4)
        self.assertEqual(len(self.game.players[0].hand), 13)

    def test_is_valid_play(self):
        self.game.setup()
        club_3 = self.game.players[self.game.current_player].hand.find_3_clubs()
        self.assertIsNotNone(club_3)
        self.assertTrue(
            self.game.play(self.game.players[self.game.current_player], [club_3])
        )

    def test_pass_turn(self):
        self.game.setup()
        player = self.game.players[self.game.current_player]
        club_3 = player.hand.find_3_clubs()
        self.game.play(player, [club_3])
        self.game.next_turn()
        self.game.pass_turn(self.game.players[self.game.current_player])
        self.assertEqual(self.game.pass_count, 1)

    def test_round_reset(self):
        self.game.setup()
        player = self.game.players[self.game.current_player]
        club_3 = player.hand.find_3_clubs()
        self.game.play(player, [club_3])
        self.game.next_turn()
        for _ in range(3):
            self.game.pass_turn(self.game.players[self.game.current_player])
            self.game.next_turn()
        self.assertIsNone(self.game.last_play)

    def test_game_over(self):
        self.game.setup()
        self.assertFalse(self.game.is_game_over())


if __name__ == "__main__":
    unittest.main()
