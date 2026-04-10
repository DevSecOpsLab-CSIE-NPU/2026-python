import unittest
from game.models import Card
from game.ai import AIStrategy

class TestAI(unittest.TestCase):
    def test_ai_sacrifice_penalty(self):
        """[AI 智商] 測試 AI 絕對不會為了出一張牌而拆掉鐵支"""
        # [修正] 給予 6 張牌，避免 AI 判定為「衝刺期」而強行出牌
        hand = [Card(14,0), Card(14,1), Card(14,2), Card(14,3), Card(3,0), Card(4,0)]
        last_play = [Card(13, 0)] # 對手出 ♣K
        
        best_move = AIStrategy.select_best_move(hand, last_play)
        # AI 寧可 Pass (回傳 None)，也絕對不該拆 A 去壓 K
        self.assertIsNone(best_move)

    def test_ai_free_lead_logic(self):
        """[AI 智商] 自由出牌時，AI 應該優先出最小的廢牌"""
        hand = [Card(3,0), Card(15,3)] # ♣3, ♠2
        best_move = AIStrategy.select_best_move(hand, last_play=None)
        self.assertEqual(best_move[0].rank, 3)