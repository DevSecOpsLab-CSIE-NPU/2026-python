"""
game 模組測試。
"""

from __future__ import annotations

import unittest

from game.game import BigTwoGame
from game.models import Card, Hand, Player


class TestBigTwoGame(unittest.TestCase):
    """遊戲流程測試。"""

    def test_setup_distributes_cards(self) -> None:
        game = BigTwoGame(seed=7)
        game.setup()
        self.assertEqual(len(game.players), 4)
        self.assertEqual(sum(len(player.hand) for player in game.players), 52)
        self.assertTrue(all(len(player.hand) == 13 for player in game.players))
        self.assertEqual(sum(1 for player in game.players if player.is_ai), 3)

    def test_first_player_has_3_clubs(self) -> None:
        game = BigTwoGame(seed=7)
        game.setup()
        self.assertEqual(game.get_current_player().hand.find_3_clubs(), Card(3, 0))

    def test_play_removes_cards_and_sets_last_play(self) -> None:
        game = BigTwoGame(seed=7)
        player = Player("Player")
        player.hand = Hand([Card(3, 0), Card(9, 1)])
        game.players = [player, Player("AI1", True), Player("AI2", True), Player("AI3", True)]
        game.current_player_index = 0
        game.first_turn = True
        self.assertTrue(game.play(player, [Card(3, 0)]))
        self.assertEqual(len(player.hand), 1)
        self.assertEqual(game.last_play, [Card(3, 0)])

    def test_invalid_play_returns_false(self) -> None:
        game = BigTwoGame(seed=7)
        player = Player("Player")
        player.hand = Hand([Card(14, 3)])
        game.players = [player, Player("AI1", True), Player("AI2", True), Player("AI3", True)]
        game.current_player_index = 0
        game.first_turn = True
        self.assertFalse(game.play(player, [Card(14, 3)]))

    def test_three_passes_reset_round(self) -> None:
        game = BigTwoGame(seed=7)
        players = [Player("P0"), Player("P1", True), Player("P2", True), Player("P3", True)]
        for idx, player in enumerate(players):
            player.hand = Hand([Card(3 + idx, 0)])
        game.players = players
        game.current_player_index = 1
        game.last_play = [Card(9, 3)]
        game.last_player_index = 0
        game.first_turn = False
        self.assertTrue(game.pass_turn(players[1]))
        self.assertTrue(game.pass_turn(players[2]))
        self.assertTrue(game.pass_turn(players[3]))
        self.assertIsNone(game.last_play)
        self.assertEqual(game.current_player_index, 0)

    def test_detect_winner(self) -> None:
        game = BigTwoGame(seed=7)
        winner = Player("Winner")
        winner.hand = Hand([])
        game.players = [winner, Player("AI1", True), Player("AI2", True), Player("AI3", True)]
        self.assertEqual(game.check_winner(), winner)
        self.assertTrue(game.is_game_over())

    def test_ai_turn_plays_when_possible(self) -> None:
        game = BigTwoGame(seed=7)
        human = Player("Human")
        ai = Player("AI1", True)
        ai.hand = Hand([Card(3, 0), Card(9, 1)])
        other_ai = Player("AI2", True)
        other_ai.hand = Hand([Card(4, 0)])
        other_ai2 = Player("AI3", True)
        other_ai2.hand = Hand([Card(5, 0)])
        game.players = [ai, human, other_ai, other_ai2]
        game.current_player_index = 0
        game.first_turn = True
        self.assertTrue(game.ai_turn())
        self.assertEqual(game.last_play, [Card(3, 0)])


if __name__ == "__main__":
    unittest.main()
