import unittest

from game.classifier import CardType, HandClassifier
from game.models import Card


class TestClassifier(unittest.TestCase):
    def test_cardtype_values(self):
        self.assertEqual(CardType.SINGLE, 1)
        self.assertEqual(CardType.STRAIGHT_FLUSH, 8)

    def test_single_pair_triple(self):
        self.assertEqual(HandClassifier.classify([Card(14, 3)]), (CardType.SINGLE, 14, 3))
        self.assertEqual(HandClassifier.classify([Card(14, 3), Card(14, 2)]), (CardType.PAIR, 14, 0))
        self.assertEqual(
            HandClassifier.classify([Card(14, 3), Card(14, 2), Card(14, 1)]),
            (CardType.TRIPLE, 14, 0),
        )

    def test_five_types(self):
        straight = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        flush = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        full_house = [Card(14, 3), Card(14, 2), Card(14, 1), Card(15, 0), Card(15, 1)]
        four = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 1)]
        straight_flush = [Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)]

        self.assertEqual(HandClassifier.classify(straight), (CardType.STRAIGHT, 7, 0))
        self.assertEqual(HandClassifier.classify(flush), (CardType.FLUSH, 11, 0))
        self.assertEqual(HandClassifier.classify(full_house), (CardType.FULL_HOUSE, 14, 0))
        self.assertEqual(HandClassifier.classify(four), (CardType.FOUR_OF_A_KIND, 14, 0))
        self.assertEqual(HandClassifier.classify(straight_flush), (CardType.STRAIGHT_FLUSH, 7, 0))

    def test_compare_and_can_play(self):
        self.assertEqual(HandClassifier.compare([Card(14, 3)], [Card(13, 3)]), 1)
        self.assertEqual(
            HandClassifier.compare([Card(14, 3), Card(14, 2)], [Card(14, 1), Card(14, 0)]),
            0,
        )
        self.assertTrue(HandClassifier.can_play(None, [Card(3, 0)]))
        self.assertFalse(HandClassifier.can_play(None, [Card(14, 3)]))


if __name__ == "__main__":
    unittest.main()
