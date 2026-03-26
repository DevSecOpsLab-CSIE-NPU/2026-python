"""Phase 5：遊戲流程測試。"""

from __future__ import annotations

import unittest

from game.game import BigTwoGame
from game.models import Card, Hand


class TestGameSetup(unittest.TestCase):
    def test_game_has_4_players(self):
        g = BigTwoGame()
        g.setup()
        self.assertEqual(len(g.players), 4)

    def test_each_player_13_cards(self):
        g = BigTwoGame()
        g.setup()
        self.assertTrue(all(len(p.hand) == 13 for p in g.players))

    def test_total_cards_distributed(self):
        g = BigTwoGame()
        g.setup()
        self.assertEqual(sum(len(p.hand) for p in g.players), 52)

    def test_first_player_has_3_clubs(self):
        g = BigTwoGame()
        g.setup()
        self.assertIsNotNone(g.get_current_player().hand.find_3_clubs())

    def test_one_human_three_ai(self):
        g = BigTwoGame()
        g.setup()
        ai_count = sum(1 for p in g.players if p.is_ai)
        self.assertEqual(ai_count, 3)


class TestGamePlayFlow(unittest.TestCase):
    def setUp(self):
        self.g = BigTwoGame()
        self.g.setup()
        # 建立可控場景：玩家0先手，只有 3♣。
        self.g.current_player = 0
        self.g.players[0].hand = Hand([Card(3, 0), Card(14, 3)])
        self.g.players[1].hand = Hand([Card(4, 0)])
        self.g.players[2].hand = Hand([Card(5, 0)])
        self.g.players[3].hand = Hand([Card(6, 0)])
        self.g.last_play = None
        self.g.pass_count = 0

    def test_play_removes_cards(self):
        p = self.g.get_current_player()
        before = len(p.hand)
        ok = self.g.play(p, [Card(3, 0)])
        self.assertTrue(ok)
        self.assertEqual(len(p.hand), before - 1)

    def test_play_sets_last_play(self):
        p = self.g.get_current_player()
        self.g.play(p, [Card(3, 0)])
        self.assertIsNotNone(self.g.last_play)

    def test_invalid_play(self):
        p = self.g.get_current_player()
        ok = self.g.play(p, [Card(14, 3)])  # 第一手不能先出 A
        self.assertFalse(ok)

    def test_pass_increments(self):
        p = self.g.get_current_player()
        self.assertTrue(self.g.pass_(p))
        self.assertEqual(self.g.pass_count, 1)

    def test_three_passes_resets(self):
        p = self.g.get_current_player()
        self.g.play(p, [Card(3, 0)])
        self.g.next_turn(); self.g.pass_(self.g.get_current_player())
        self.g.next_turn(); self.g.pass_(self.g.get_current_player())
        self.g.next_turn(); self.g.pass_(self.g.get_current_player())
        self.g.check_round_reset()
        self.assertIsNone(self.g.last_play)

    def test_turn_rotates(self):
        start = self.g.current_player
        self.g.next_turn()
        self.assertEqual(self.g.current_player, (start + 1) % 4)

    def test_detect_winner(self):
        p = self.g.get_current_player()
        self.g.play(p, [Card(3, 0)])
        self.g.play(p, [Card(14, 3)])
        winner = self.g.check_winner()
        self.assertIsNotNone(winner)

    def test_no_winner_yet(self):
        self.assertIsNone(self.g.check_winner())

    def test_game_ends(self):
        p = self.g.get_current_player()
        self.g.play(p, [Card(3, 0)])
        self.g.play(p, [Card(14, 3)])
        self.g.check_winner()
        self.assertTrue(self.g.is_game_over())


if __name__ == "__main__":
    unittest.main(verbosity=2)
