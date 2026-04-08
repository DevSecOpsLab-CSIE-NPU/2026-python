"""
Phase 5 Tests: 遊戲流程測試
BigTwoGame 類別的單元測試
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from game.game import BigTwoGame
from game.models import Card, Player, Hand


class TestGameSetup(unittest.TestCase):
    """遊戲初始化測試"""
    
    def test_game_has_4_players(self):
        """測試遊戲有4位玩家"""
        game = BigTwoGame()
        game.setup()
        self.assertEqual(len(game.players), 4)
    
    def test_each_player_13_cards(self):
        """測試每位玩家13張牌"""
        game = BigTwoGame()
        game.setup()
        for player in game.players:
            self.assertEqual(len(player.hand), 13)
    
    def test_total_cards_distributed(self):
        """測試總共52張牌被分配"""
        game = BigTwoGame()
        game.setup()
        total = sum(len(player.hand) for player in game.players)
        self.assertEqual(total, 52)
    
    def test_first_player_has_3_clubs(self):
        """測試先手玩家有3♣"""
        game = BigTwoGame()
        game.setup()
        first_player = game.players[game.current_player]
        self.assertIsNotNone(first_player.hand.find_3_clubs())


class TestGamePlay(unittest.TestCase):
    """遊戲出牌測試"""
    
    def setUp(self):
        """設置遊戲"""
        self.game = BigTwoGame()
        self.game.setup()
    
    def test_play_removes_cards(self):
        """測試出牌移除手牌"""
        player = self.game.get_current_player()
        initial_count = len(player.hand)
        
        three_clubs = player.hand.find_3_clubs()
        if three_clubs:
            self.game.play(player, [three_clubs])
            self.assertEqual(len(player.hand), initial_count - 1)
    
    def test_play_sets_last_play(self):
        """測試出牌設定last_play"""
        player = self.game.get_current_player()
        three_clubs = player.hand.find_3_clubs()
        
        if three_clubs:
            self.game.play(player, [three_clubs])
            self.assertIsNotNone(self.game.last_play)


class TestGameWinner(unittest.TestCase):
    """遊戲獲勝測試"""
    
    def test_detect_winner(self):
        """測試檢測獲勝者"""
        game = BigTwoGame()
        game.setup()
        
        # 模擬一位玩家出完牌
        player = game.players[0]
        player.hand.clear()
        
        winner = game.check_winner()
        self.assertEqual(winner, player)


if __name__ == '__main__':
    unittest.main()
