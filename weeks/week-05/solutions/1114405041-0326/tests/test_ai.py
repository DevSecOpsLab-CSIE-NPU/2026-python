"""Phase 4：AI 策略測試。"""

from __future__ import annotations

import unittest

from game.ai import AIStrategy
from game.models import Card, Hand


class TestScorePlay(unittest.TestCase):
    def test_score_single(self):
        # 準備 5 張手牌，避免觸發「剩餘 <= 3 張」的額外獎勵。
        hand = Hand([Card(14, 3), Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 0)])
        score = AIStrategy.score_play([Card(14, 3)], hand)
        self.assertEqual(score, 245.0)  # 1*100 + 14*10 + ♠加分5

    def test_score_pair_higher(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        pair_score = AIStrategy.score_play([Card(14, 3), Card(14, 2)], hand)
        single_score = AIStrategy.score_play([Card(14, 3)], hand)
        self.assertGreater(pair_score, single_score)

    def test_score_triple_higher(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0)])
        triple = AIStrategy.score_play([Card(14, 3), Card(14, 2), Card(14, 1)], hand)
        pair = AIStrategy.score_play([Card(14, 3), Card(14, 2)], hand)
        self.assertGreater(triple, pair)

    def test_score_near_empty(self):
        hand = Hand([Card(14, 3), Card(14, 2)])
        score = AIStrategy.score_play([Card(14, 3)], hand)
        self.assertGreater(score, 10000)

    def test_score_low_cards(self):
        hand = Hand([Card(14, 3), Card(13, 2), Card(12, 1)])
        score = AIStrategy.score_play([Card(14, 3)], hand)
        self.assertGreater(score, 500)

    def test_score_spade_bonus(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        spade = AIStrategy.score_play([Card(14, 3)], hand)
        non_spade = AIStrategy.score_play([Card(14, 2)], hand)
        self.assertEqual(spade - non_spade, 5.0)


class TestSelectBest(unittest.TestCase):
    def test_select_best(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        valid = [[Card(14, 3)], [Card(14, 3), Card(14, 2)]]
        best = AIStrategy.select_best(valid, hand)
        self.assertEqual(best, [Card(14, 3), Card(14, 2)])

    def test_select_first_turn(self):
        hand = Hand([Card(3, 0), Card(14, 3)])
        valid = [[Card(3, 0)], [Card(14, 3)]]
        best = AIStrategy.select_best(valid, hand, is_first=True)
        self.assertEqual(best, [Card(3, 0)])

    def test_select_empty(self):
        self.assertIsNone(AIStrategy.select_best([], Hand()))


class TestAIStrategyFlow(unittest.TestCase):
    def test_ai_prefers_high(self):
        hand = Hand([Card(10, 3), Card(15, 3)])
        valid = [[Card(10, 3)], [Card(15, 3)]]
        best = AIStrategy.select_best(valid, hand)
        self.assertEqual(best, [Card(15, 3)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
