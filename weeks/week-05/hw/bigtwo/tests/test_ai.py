"""
Phase 4 Tests: AI 策略測試
AIStrategy 類別的單元測試
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from game.models import Card, Hand
from game.ai import AIStrategy


class TestScorePlay(unittest.TestCase):
    """AI 評分測試"""
    
    def test_score_single(self):
        """測試單張評分"""
        cards = [Card(14, 3)]
        hand = Hand([Card(14, 3), Card(13, 2)])
        score = AIStrategy.score_play(cards, hand)
        self.assertGreater(score, 0)
    
    def test_score_pair_higher_than_single(self):
        """測試對子分數大於單張"""
        single_cards = [Card(14, 3)]
        pair_cards = [Card(14, 3), Card(14, 2)]
        
        hand = Hand([Card(14, 3), Card(14, 2), Card(13, 1)])
        
        score_single = AIStrategy.score_play(single_cards, hand)
        score_pair = AIStrategy.score_play(pair_cards, hand)
        
        self.assertGreater(score_pair, score_single)


class TestSelectBest(unittest.TestCase):
    """AI 選擇最佳出牌測試"""
    
    def test_select_best_first_turn(self):
        """測試第一回合選擇3♣"""
        valid_plays = [
            [Card(3, 0)],  # 3♣
            [Card(14, 3)],  # A♠
        ]
        hand = Hand(valid_plays[0] + valid_plays[1])
        best = AIStrategy.select_best(valid_plays, hand, is_first=True)
        self.assertEqual(best, [Card(3, 0)])
    
    def test_select_best_empty_list(self):
        """測試空列表返回None"""
        hand = Hand()
        best = AIStrategy.select_best([], hand)
        self.assertIsNone(best)


if __name__ == '__main__':
    unittest.main()
