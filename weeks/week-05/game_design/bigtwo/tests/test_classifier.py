"""Tests for Big Two hand classifier."""

import unittest
from game.models import Card
from game.classifier import HandClassifier, CardType


class TestHandClassifier(unittest.TestCase):
    def test_classify_single(self):
        card = Card(14, 3)
        result = HandClassifier.classify([card])
        self.assertEqual(result[0], CardType.SINGLE)
        self.assertEqual(result[1], 14)

    def test_classify_pair(self):
        cards = [Card(14, 3), Card(14, 2)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.PAIR)
        self.assertEqual(result[1], 14)

    def test_classify_triple(self):
        cards = [Card(14, 3), Card(14, 2), Card(14, 1)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.TRIPLE)
        self.assertEqual(result[1], 14)

    def test_classify_straight(self):
        cards = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.STRAIGHT)

    def test_classify_straight_12345(self):
        cards = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(14, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.STRAIGHT)

    def test_classify_flush(self):
        cards = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.FLUSH)

    def test_classify_full_house(self):
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 0), Card(13, 1)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.FULL_HOUSE)

    def test_classify_four_of_a_kind(self):
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 1)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.FOUR_OF_A_KIND)

    def test_classify_straight_flush(self):
        cards = [Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.STRAIGHT_FLUSH)

    def test_compare_straight_flush_vs_flush(self):
        sf = [Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)]
        fl = [Card(10, 1), Card(12, 1), Card(14, 1), Card(3, 1), Card(5, 1)]
        self.assertGreater(HandClassifier.compare(sf, fl), 0)

    def test_can_play_first_turn(self):
        card = Card(3, 0)
        self.assertTrue(HandClassifier.can_play(None, [card]))

    def test_can_play_first_turn_wrong(self):
        card = Card(4, 0)
        self.assertFalse(HandClassifier.can_play(None, [card]))


if __name__ == "__main__":
    unittest.main()
