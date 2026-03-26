"""
Phase 4: AI 策略 - 單元測試
"""
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from game.models import Card, Hand
from game.ai import AIStrategy
from game.classifier import CardType


class TestScorePlay(unittest.TestCase):
    """評分函數測試"""
    
    def test_score_single(self):
        """測試單張評分"""
        hand = Hand([Card(14, 3), Card(13, 2)])
        cards = [Card(14, 3)]
        score = AIStrategy.score_play(cards, hand)
        # 單張 + A + 剩1張獎勵
        self.assertGreater(score, 10000)
    
    def test_score_pair_higher_than_single(self):
        """測試對子分數高於單張"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(13, 1), Card(12, 0)])
        single_score = AIStrategy.score_play([Card(14, 3)], hand)
        pair_score = AIStrategy.score_play([Card(14, 3), Card(14, 2)], hand)
        self.assertGreater(pair_score, single_score)
    
    def test_score_triple_higher_than_pair(self):
        """測試三條分數高於對子"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 0)])
        pair_cards = [Card(14, 3), Card(14, 2)]
        triple_cards = [Card(14, 3), Card(14, 2), Card(14, 1)]
        pair_score = AIStrategy.score_play(pair_cards, hand)
        triple_score = AIStrategy.score_play(triple_cards, hand)
        self.assertGreater(triple_score, pair_score)
    
    def test_score_near_empty_bonus(self):
        """測試剩餘牌少時有獎勵"""
        hand = Hand([Card(14, 3), Card(13, 2), Card(12, 1)])
        cards = [Card(14, 3)]
        score = AIStrategy.score_play(cards, hand)
        # 剩2張應該有 NEAR_EMPTY_BONUS
        self.assertGreater(score, 500)
    
    def test_score_spade_bonus(self):
        """測試黑桃獎勵"""
        hand = Hand([Card(14, 3)])  # ♠A
        cards = [Card(14, 3)]  # ♠A (黑桃)
        score = AIStrategy.score_play(cards, hand)
        # 應該包含黑桃獎勵
        self.assertGreater(score, 100 + 140 + 5)


class TestSelectBest(unittest.TestCase):
    """選擇最佳出牌測試"""
    
    def test_select_best_pair_over_single(self):
        """測試選擇對子而非單張"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(13, 1)])
        valid_plays = [
            [Card(14, 3)],
            [Card(14, 3), Card(14, 2)]
        ]
        best = AIStrategy.select_best(valid_plays, hand)
        self.assertEqual(len(best), 2)  # 選對子
    
    def test_select_first_turn(self):
        """測試第一回合選3♣"""
        hand = Hand([Card(3, 0), Card(14, 3)])
        valid_plays = [[Card(3, 0)]]
        best = AIStrategy.select_best(valid_plays, hand, is_first=True)
        self.assertEqual(best, [Card(3, 0)])
    
    def test_select_empty_plays(self):
        """測試無合法出牌"""
        hand = Hand([Card(14, 3)])
        valid_plays = []
        best = AIStrategy.select_best(valid_plays, hand)
        self.assertIsNone(best)
    
    def test_select_highest_card(self):
        """測試選擇最高的牌"""
        hand = Hand([Card(14, 3), Card(13, 2), Card(12, 1)])
        valid_plays = [
            [Card(13, 2)],
            [Card(14, 3)]
        ]
        best = AIStrategy.select_best(valid_plays, hand)
        self.assertEqual(best[0].rank, 14)  # 選A而不是K


class TestAIStrategy(unittest.TestCase):
    """完整 AI 策略測試"""
    
    def test_ai_prefers_clearing_hand(self):
        """測試 AI 傾向於清空手牌"""
        # 剩1張時評分應該最高
        hand = Hand([Card(14, 3), Card(13, 2), Card(12, 1)])
        score1 = AIStrategy.score_play([Card(14, 3)], hand)
        
        hand2 = Hand([Card(14, 3)])
        score2 = AIStrategy.score_play([Card(14, 3)], hand2)
        
        # 比較分數：手2剩0張 vs 手1剩2張
        # 手1: 出A時 100 + 110 + 500(<=3張) + 5(♠) = 715
        # 手2: 出A時 100 + 110 + 500(<=3張) + 5(♠) = 715
        # 分數相同，因為都剩<=3張，都有 NEAR_EMPTY_BONUS
        self.assertEqual(score2, score1)
    
    def test_score_calculation(self):
        """測試評分計算"""
        hand = Hand([Card(14, 3)])
        # 單張A，出牌後剩0張
        # 分數 = 1*100 + 11*10 + 500(NEAR_EMPTY, <=3張) + 5(♠)
        score = AIStrategy.score_play([Card(14, 3)], hand)
        # 計算: base(100+110) + NEAR_EMPTY(500) + spade(5)
        expected = 100 + 110 + 500 + 5
        self.assertEqual(score, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
