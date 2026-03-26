import unittest

from game.cards import Card
from game.classifier import CardType, HandClassifier


def C(suit: int, rank: int) -> Card:
    return Card(suit=suit, rank=rank)


class TestCardType(unittest.TestCase):
    def test_cardtype_values(self):
        self.assertEqual(CardType.SINGLE, 1)
        self.assertEqual(CardType.PAIR, 2)
        self.assertEqual(CardType.TRIPLE, 3)
        self.assertEqual(CardType.STRAIGHT, 4)
        self.assertEqual(CardType.FLUSH, 5)
        self.assertEqual(CardType.FULL_HOUSE, 6)
        self.assertEqual(CardType.FOUR_OF_A_KIND, 7)
        self.assertEqual(CardType.STRAIGHT_FLUSH, 8)


class TestClassifySingle(unittest.TestCase):
    def test_classify_single_ace(self):
        self.assertEqual(HandClassifier.classify([C(3, 14)]), (CardType.SINGLE, 14, 3))

    def test_classify_single_two(self):
        self.assertEqual(HandClassifier.classify([C(0, 15)]), (CardType.SINGLE, 15, 0))

    def test_classify_single_three(self):
        self.assertEqual(HandClassifier.classify([C(0, 3)]), (CardType.SINGLE, 3, 0))


class TestClassifyPair(unittest.TestCase):
    def test_classify_pair(self):
        self.assertEqual(HandClassifier.classify([C(3, 14), C(2, 14)]), (CardType.PAIR, 14, 2))

    def test_classify_pair_diff_rank(self):
        self.assertIsNone(HandClassifier.classify([C(3, 14), C(3, 13)]))

    def test_classify_pair_from_three(self):
        self.assertEqual(HandClassifier.classify([C(3, 14), C(2, 14)]), (CardType.PAIR, 14, 2))


class TestClassifyTriple(unittest.TestCase):
    def test_classify_triple(self):
        self.assertEqual(HandClassifier.classify([C(3, 14), C(2, 14), C(1, 14)]), (CardType.TRIPLE, 14, 1))

    def test_classify_triple_not_enough(self):
        self.assertEqual(HandClassifier.classify([C(3, 14), C(2, 14)]), (CardType.PAIR, 14, 2))


class TestClassifyFiveCards(unittest.TestCase):
    def test_classify_straight(self):
        cards = [C(0, 3), C(1, 4), C(2, 5), C(3, 6), C(0, 7)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT, 7, 0))

    def test_classify_straight_ace_low(self):
        cards = [C(0, 14), C(1, 15), C(2, 3), C(3, 4), C(0, 5)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT, 5, 0))

    def test_classify_flush(self):
        cards = [C(0, 3), C(0, 5), C(0, 7), C(0, 9), C(0, 11)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FLUSH, 11, 0))

    def test_classify_full_house(self):
        cards = [C(3, 14), C(2, 14), C(1, 14), C(0, 15), C(1, 15)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FULL_HOUSE, 14, 0))

    def test_classify_four_of_a_kind(self):
        cards = [C(3, 14), C(2, 14), C(1, 14), C(0, 14), C(1, 3)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FOUR_OF_A_KIND, 14, 0))

    def test_classify_straight_flush(self):
        cards = [C(0, 3), C(0, 4), C(0, 5), C(0, 6), C(0, 7)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT_FLUSH, 7, 0))


class TestCompare(unittest.TestCase):
    def test_compare_single_rank(self):
        self.assertEqual(HandClassifier.compare([C(3, 14)], [C(3, 13)]), 1)

    def test_compare_single_suit(self):
        self.assertEqual(HandClassifier.compare([C(3, 14)], [C(2, 14)]), 1)

    def test_compare_pair_rank(self):
        self.assertEqual(HandClassifier.compare([C(3, 14), C(2, 14)], [C(3, 13), C(2, 13)]), 1)

    def test_compare_pair_suit(self):
        self.assertEqual(HandClassifier.compare([C(3, 14), C(2, 14)], [C(1, 14), C(0, 14)]), 1)

    def test_compare_different_type(self):
        self.assertEqual(HandClassifier.compare([C(3, 14), C(2, 14)], [C(3, 15)]), 1)

    def test_compare_flush_vs_straight(self):
        flush = [C(0, 3), C(0, 5), C(0, 7), C(0, 9), C(0, 11)]
        straight = [C(0, 3), C(1, 4), C(2, 5), C(3, 6), C(0, 7)]
        self.assertEqual(HandClassifier.compare(flush, straight), 1)


class TestCanPlay(unittest.TestCase):
    def test_can_play_first_3clubs(self):
        self.assertTrue(HandClassifier.can_play(None, [C(0, 3)]))

    def test_can_play_first_not_3clubs(self):
        self.assertFalse(HandClassifier.can_play(None, [C(3, 14)]))

    def test_can_play_same_type(self):
        last_play = [C(0, 5), C(1, 5)]
        cards = [C(2, 6), C(3, 6)]
        self.assertTrue(HandClassifier.can_play(last_play, cards))

    def test_can_play_diff_type(self):
        last_play = [C(0, 5), C(1, 5)]
        cards = [C(2, 6)]
        self.assertFalse(HandClassifier.can_play(last_play, cards))

    def test_can_play_not_stronger(self):
        last_play = [C(2, 10), C(3, 10)]
        cards = [C(0, 5), C(1, 5)]
        self.assertFalse(HandClassifier.can_play(last_play, cards))


if __name__ == "__main__":
    unittest.main()
