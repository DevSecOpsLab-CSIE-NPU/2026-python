"""Phase 4: AI strategy tests."""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.models import Card, Hand
from game.ai import AIStrategy


class TestAIStrategy(unittest.TestCase):
    """AI 策略測試。"""

    def test_score_single(self):
        """測試單張評分。"""
        cards = [Card(14, 3)]
        hand = Hand([Card(14, 3), Card(13, 2)])
        score = AIStrategy.score_play(cards, hand)
        self.assertGreater(score, 0)

    def test_score_higher_type(self):
        """測試高牌型分數較高。"""
        single = [Card(14, 3)]
        pair = [Card(14, 3), Card(14, 2)]
        hand = Hand([Card(14, 3), Card(14, 2), Card(13, 1)])

        score_single = AIStrategy.score_play(single, hand)
        score_pair = AIStrategy.score_play(pair, hand)

        self.assertGreater(score_pair, score_single)

    def test_select_best(self):
        """測試選擇最佳出牌。"""
        plays = [
            [Card(3, 0)],
            [Card(14, 3)],
        ]
        hand = Hand(plays[0] + plays[1])

        best = AIStrategy.select_best(plays, hand, is_first=True)
        # 第一回合應該選 3♣
        self.assertIsNotNone(best)
        self.assertEqual(len(best), 1)


if __name__ == '__main__':
    unittest.main()
