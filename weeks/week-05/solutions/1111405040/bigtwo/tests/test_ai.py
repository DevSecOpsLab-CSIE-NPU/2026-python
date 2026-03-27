"""
ai 模組測試。
"""

from __future__ import annotations

import unittest

from game.ai import AIStrategy
from game.models import Card, Hand


class TestAI(unittest.TestCase):
    """AI 策略測試。"""

    def test_score_pair_higher_than_single(self) -> None:
        hand = Hand([Card(14, 3), Card(14, 1), Card(7, 0)])
        pair_score = AIStrategy.score_play([Card(14, 3), Card(14, 1)], hand)
        single_score = AIStrategy.score_play([Card(14, 3)], hand)
        self.assertGreater(pair_score, single_score)

    def test_score_near_empty_bonus(self) -> None:
        hand = Hand([Card(3, 0), Card(14, 3)])
        score = AIStrategy.score_play([Card(14, 3)], hand)
        self.assertGreaterEqual(score, 500)

    def test_select_best(self) -> None:
        hand = Hand([Card(14, 3), Card(14, 1), Card(7, 0)])
        valid_plays = [[Card(7, 0)], [Card(14, 3), Card(14, 1)]]
        self.assertEqual(AIStrategy.select_best(valid_plays, hand), [Card(14, 3), Card(14, 1)])

    def test_select_best_first_turn_prefers_3_clubs(self) -> None:
        hand = Hand([Card(3, 0), Card(5, 1), Card(5, 3)])
        valid_plays = [[Card(3, 0)], [Card(3, 0), Card(5, 1), Card(5, 3)]]
        self.assertEqual(AIStrategy.select_best(valid_plays, hand, is_first_turn=True), [Card(3, 0)])

    def test_select_best_empty(self) -> None:
        hand = Hand([])
        self.assertIsNone(AIStrategy.select_best([], hand))


if __name__ == "__main__":
    unittest.main()
