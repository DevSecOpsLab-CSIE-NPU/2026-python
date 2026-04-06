import unittest

from game.ai import AIStrategy
from game.models import Card, Hand


class TestAI(unittest.TestCase):
    def test_score_single(self):
        hand = Hand([Card(14, 3), Card(3, 0)])
        score = AIStrategy.score_play([Card(14, 3)], hand)
        self.assertTrue(score >= 240)

    def test_select_best(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        valid_plays = [[Card(14, 3)], [Card(14, 3), Card(14, 2)]]
        best = AIStrategy.select_best(valid_plays, hand)
        self.assertEqual(len(best), 2)

    def test_select_first_turn(self):
        hand = Hand([Card(3, 0), Card(14, 3)])
        valid_plays = [[Card(14, 3)], [Card(3, 0)]]
        best = AIStrategy.select_best(valid_plays, hand, is_first=True)
        self.assertEqual(best, [Card(3, 0)])


if __name__ == "__main__":
    unittest.main()
