"""Phase 5: Game flow tests."""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.game import BigTwoGame


class TestBigTwoGame(unittest.TestCase):
    """遊戲流程測試。"""

    def setUp(self):
        """設置測試遊戲。"""
        self.game = BigTwoGame()
        self.game.setup()

    def test_game_setup(self):
        """測試遊戲初始化。"""
        self.assertEqual(len(self.game.players), 4)
        for player in self.game.players:
            self.assertEqual(len(player.hand), 13)

    def test_first_player_has_3_clubs(self):
        """測試先手有 3♣。"""
        player = self.game.get_current_player()
        found = player.hand.find_3_clubs()
        self.assertIsNotNone(found)

    def test_play_removes_cards(self):
        """測試出牌移除手牌。"""
        player = self.game.get_current_player()
        initial_count = len(player.hand)

        # 第一回合必須出3♣
        three_clubs = player.hand.find_3_clubs()
        self.assertIsNotNone(three_clubs)
        
        self.game.play(player, [three_clubs])

        self.assertEqual(len(player.hand), initial_count - 1)

    def test_pass_increments_counter(self):
        """測試過牌增加計數。"""
        player = self.game.get_current_player()
        initial_pass = self.game.pass_count

        self.game.pass_(player)

        self.assertEqual(self.game.pass_count, initial_pass + 1)

    def test_no_winner_initially(self):
        """測試遊戲初期無獲勝者。"""
        self.assertIsNone(self.game.check_winner())
        self.assertFalse(self.game.is_game_over())


if __name__ == '__main__':
    unittest.main()
