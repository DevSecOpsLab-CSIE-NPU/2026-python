"""Tests for Big Two AI strategy."""

import unittest
from game.models import Card, Hand
from game.ai import AIStrategy
from game.classifier import CardType


class TestAIStrategy(unittest.TestCase):
    def test_score_single(self):
        hand = Hand([Card(3, 0), Card(14, 3)])
        card = [Card(14, 3)]
        score = AIStrategy.score_play(card, hand)
        self.assertGreater(score, 0)

    def test_score_pair_higher_than_single(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        pair = [Card(14, 3), Card(14, 2)]
        single = [Card(3, 0)]
        score_pair = AIStrategy.score_play(pair, hand)
        score_single = AIStrategy.score_play(single, hand)
        self.assertGreater(score_pair, score_single)

    def test_select_best(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        valid_plays = [[Card(3, 0)], [Card(14, 3), Card(14, 2)]]
        best = AIStrategy.select_best(valid_plays, hand)
        self.assertEqual(len(best), 2)

    def test_select_best_first_turn(self):
        hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2)])
        valid_plays = [[Card(3, 0)], [Card(4, 1)]]
        best = AIStrategy.select_best(valid_plays, hand, is_first=True)
        self.assertEqual(best[0].rank, 3)
        self.assertEqual(best[0].suit, 0)


if __name__ == "__main__":
    unittest.main()
