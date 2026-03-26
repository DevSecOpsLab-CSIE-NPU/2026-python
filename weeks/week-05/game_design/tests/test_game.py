"""
Phase 5: 遊戲流程 - 單元測試
"""
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from game.models import Card, Player
from game.game import BigTwoGame


class TestGameSetup(unittest.TestCase):
    """遊戲初始化測試"""
    
    def test_game_has_4_players(self):
        """測試遊戲有4位玩家"""
        game = BigTwoGame(num_human=1)
        game.setup()
        self.assertEqual(len(game.players), 4)
    
    def test_each_player_13_cards(self):
        """測試每位玩家有13張牌"""
        game = BigTwoGame(num_human=1)
        game.setup()
        for player in game.players:
            self.assertEqual(len(player.hand), 13)
    
    def test_total_cards_distributed(self):
        """測試總共52張牌"""
        game = BigTwoGame(num_human=1)
        game.setup()
        total = sum(len(player.hand) for player in game.players)
        self.assertEqual(total, 52)
    
    def test_first_player_has_3_clubs(self):
        """測試先手有3♣"""
        game = BigTwoGame(num_human=1)
        game.setup()
        first_player = game.get_current_player()
        has_3_clubs = first_player.hand.find_3_clubs() is not None
        self.assertTrue(has_3_clubs)
    
    def test_one_human_three_ai(self):
        """測試1人3AI"""
        game = BigTwoGame(num_human=1)
        game.setup()
        human_count = sum(1 for p in game.players if not p.is_ai)
        ai_count = sum(1 for p in game.players if p.is_ai)
        self.assertEqual(human_count, 1)
        self.assertEqual(ai_count, 3)


class TestGamePlay(unittest.TestCase):
    """出牌流程測試"""
    
    def test_play_removes_cards(self):
        """測試出牌移除手牌"""
        game = BigTwoGame(num_human=1)
        game.setup()
        
        player = game.get_current_player()
        initial_count = len(player.hand)
        
        # 找3♣出牌
        card_3_clubs = player.hand.find_3_clubs()
        if card_3_clubs:
            game.play(player, [card_3_clubs])
            self.assertEqual(len(player.hand), initial_count - 1)
    
    def test_play_sets_last_play(self):
        """測試出牌設定 last_play"""
        game = BigTwoGame(num_human=1)
        game.setup()
        
        player = game.get_current_player()
        card_3_clubs = player.hand.find_3_clubs()
        
        if card_3_clubs:
            game.play(player, [card_3_clubs])
            self.assertIsNotNone(game.last_play)
            self.assertEqual(game.last_play[0], [card_3_clubs])
    
    def test_invalid_play_wrong_player(self):
        """測試非當前玩家出牌失敗"""
        game = BigTwoGame(num_human=1)
        game.setup()
        
        current = game.get_current_player()
        other = game.players[(game.current_player + 1) % 4]
        
        result = game.play(other, [Card(14, 3)])
        self.assertFalse(result)


class TestGamePass(unittest.TestCase):
    """過牌流程測試"""
    
    def test_pass_increments_counter(self):
        """測試過牌增加計數"""
        game = BigTwoGame(num_human=1)
        game.setup()
        
        player = game.get_current_player()
        initial = game.pass_count
        
        # 第一回合出3♣
        card_3 = player.hand.find_3_clubs()
        if card_3:
            game.play(player, [card_3])
        
        # 後續玩家過牌
        next_player = game.get_current_player()
        game.pass_(next_player)
        
        self.assertEqual(game.pass_count, 1)


class TestGameTurns(unittest.TestCase):
    """回合流程測試"""
    
    def test_turn_rotates(self):
        """測試輪轉順序"""
        game = BigTwoGame(num_human=1)
        game.setup()
        
        initial_player = game.current_player
        game.next_turn()
        self.assertEqual(game.current_player, (initial_player + 1) % 4)
    
    def test_round_reset(self):
        """測試回合重置"""
        game = BigTwoGame(num_human=1)
        game.setup()
        
        # 設定 3 人過牌
        game.pass_count = 3
        game.last_play = ([Card(3, 0)], 0)
        
        game.check_round_reset()
        
        self.assertIsNone(game.last_play)
        self.assertEqual(game.pass_count, 0)


class TestGameWinner(unittest.TestCase):
    """獲勝判定測試"""
    
    def test_detect_winner(self):
        """測試檢測獲勝者"""
        game = BigTwoGame(num_human=1)
        game.setup()
        
        # 清空一個玩家的手牌
        player = game.players[0]
        player.hand.clear()
        
        winner = game.check_winner()
        self.assertEqual(winner, player)
    
    def test_no_winner_yet(self):
        """測試還有玩家有牌"""
        game = BigTwoGame(num_human=1)
        game.setup()
        
        # 所有玩家都有牌
        winner = game.check_winner()
        self.assertIsNone(winner)
    
    def test_game_over(self):
        """測試遊戲結束判定"""
        game = BigTwoGame(num_human=1)
        game.setup()
        
        self.assertFalse(game.is_game_over())
        
        # 清空一個玩家手牌
        game.players[0].hand.clear()
        game.check_winner()
        
        self.assertTrue(game.is_game_over())


class TestAITurn(unittest.TestCase):
    """AI 回合測試"""
    
    def test_ai_turn_simple(self):
        """測試 AI 出牌"""
        game = BigTwoGame(num_human=1)
        game.setup()
        
        # 設定 AI 為當前玩家
        while game.get_current_player().is_ai:
            game.current_player = (game.current_player + 1) % 4
        
        game.current_player = (game.current_player + 1) % 4
        ai_player = game.get_current_player()
        
        if ai_player.is_ai:
            result = game.ai_turn()
            # 應該成功（要麼出牌，要麼過牌）
            self.assertTrue(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
