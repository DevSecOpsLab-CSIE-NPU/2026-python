import unittest
from game.models import Card
from game.classifier import HandClassifier, CardType


def C(rank, suit):
    return Card(rank, suit)


class TestCardTypeValues(unittest.TestCase):

    def test_cardtype_values(self):
        self.assertEqual(CardType.SINGLE.value, 1)
        self.assertEqual(CardType.PAIR.value, 2)
        self.assertEqual(CardType.TRIPLE.value, 3)
        self.assertEqual(CardType.STRAIGHT.value, 4)
        self.assertEqual(CardType.FLUSH.value, 5)
        self.assertEqual(CardType.FULL_HOUSE.value, 6)
        self.assertEqual(CardType.FOUR_OF_A_KIND.value, 7)
        self.assertEqual(CardType.STRAIGHT_FLUSH.value, 8)


class TestClassifySingle(unittest.TestCase):

    def test_classify_single_ace(self):
        r = HandClassifier.classify([C(14, 3)])
        self.assertEqual(r, (CardType.SINGLE, 14, 3))

    def test_classify_single_two(self):
        r = HandClassifier.classify([C(15, 0)])
        self.assertEqual(r, (CardType.SINGLE, 15, 0))

    def test_classify_single_three(self):
        r = HandClassifier.classify([C(3, 0)])
        self.assertEqual(r, (CardType.SINGLE, 3, 0))


class TestClassifyPair(unittest.TestCase):

    def test_classify_pair(self):
        r = HandClassifier.classify([C(14, 3), C(14, 2)])
        self.assertEqual(r[0], CardType.PAIR)
        self.assertEqual(r[1], 14)

    def test_classify_pair_diff_rank(self):
        r = HandClassifier.classify([C(14, 3), C(13, 3)])
        self.assertIsNone(r)

    def test_classify_pair_from_hand(self):
        r = HandClassifier.classify([C(14, 3), C(14, 2)])
        self.assertIsNotNone(r)
        self.assertEqual(r[0], CardType.PAIR)


class TestClassifyTriple(unittest.TestCase):

    def test_classify_triple(self):
        r = HandClassifier.classify([C(14, 3), C(14, 2), C(14, 1)])
        self.assertEqual(r[0], CardType.TRIPLE)
        self.assertEqual(r[1], 14)

    def test_classify_triple_not_enough(self):
        r = HandClassifier.classify([C(14, 3), C(14, 2)])
        self.assertNotEqual(r[0] if r else None, CardType.TRIPLE)


class TestClassifyFive(unittest.TestCase):

    def test_classify_straight(self):
        r = HandClassifier.classify([C(3, 0), C(4, 1), C(5, 2), C(6, 3), C(7, 0)])
        self.assertEqual(r[0], CardType.STRAIGHT)
        self.assertEqual(r[1], 7)

    def test_classify_straight_ace_low(self):
        r = HandClassifier.classify([C(14, 0), C(15, 1), C(3, 2), C(4, 3), C(5, 0)])
        self.assertEqual(r[0], CardType.STRAIGHT)
        self.assertEqual(r[1], 5)

    def test_classify_flush(self):
        r = HandClassifier.classify([C(3, 0), C(5, 0), C(7, 0), C(9, 0), C(11, 0)])
        self.assertEqual(r[0], CardType.FLUSH)
        self.assertEqual(r[1], 11)

    def test_classify_full_house(self):
        r = HandClassifier.classify([C(14, 3), C(14, 2), C(14, 1), C(15, 0), C(15, 1)])
        self.assertEqual(r[0], CardType.FULL_HOUSE)
        self.assertEqual(r[1], 14)

    def test_classify_four_of_a_kind(self):
        r = HandClassifier.classify([C(14, 3), C(14, 2), C(14, 1), C(14, 0), C(3, 1)])
        self.assertEqual(r[0], CardType.FOUR_OF_A_KIND)
        self.assertEqual(r[1], 14)

    def test_classify_straight_flush(self):
        r = HandClassifier.classify([C(3, 0), C(4, 0), C(5, 0), C(6, 0), C(7, 0)])
        self.assertEqual(r[0], CardType.STRAIGHT_FLUSH)
        self.assertEqual(r[1], 7)


class TestCompare(unittest.TestCase):

    def test_compare_single_rank(self):
        self.assertEqual(HandClassifier.compare([C(14, 3)], [C(13, 3)]), 1)

    def test_compare_single_suit(self):
        self.assertEqual(HandClassifier.compare([C(14, 3)], [C(14, 2)]), 1)

    def test_compare_pair_rank(self):
        self.assertEqual(HandClassifier.compare([C(14, 3), C(14, 2)],
                                                 [C(13, 3), C(13, 2)]), 1)

    def test_compare_pair_suit(self):
        # ?A vs ?色A
        self.assertEqual(HandClassifier.compare([C(14, 3), C(14, 2)],
                                                 [C(14, 1), C(14, 0)]), 1)

    def test_compare_different_type(self):
        # pair vs single -> pair wins
        self.assertEqual(HandClassifier.compare([C(14, 3), C(14, 2)], [C(14, 3)]), 1)

    def test_compare_flush_vs_straight(self):
        flush = [C(3, 0), C(5, 0), C(7, 0), C(9, 0), C(11, 0)]
        straight = [C(3, 0), C(4, 1), C(5, 2), C(6, 3), C(7, 0)]
        self.assertEqual(HandClassifier.compare(flush, straight), 1)


class TestCanPlay(unittest.TestCase):

    def test_can_play_first_3clubs(self):
        self.assertTrue(HandClassifier.can_play(None, [C(3, 0)]))

    def test_can_play_first_not_3clubs(self):
        self.assertFalse(HandClassifier.can_play(None, [C(14, 3)]))

    def test_can_play_same_type(self):
        # pair 5 vs pair 6
        self.assertTrue(HandClassifier.can_play([C(5, 0), C(5, 1)],
                                                 [C(6, 0), C(6, 1)]))

    def test_can_play_diff_type(self):
        # pair vs single: different length -> False
        self.assertFalse(HandClassifier.can_play([C(5, 0), C(5, 1)], [C(6, 0)]))

    def test_can_play_not_stronger(self):
        # pair 10 vs pair 5 -> False (5 cannot beat 10)
        self.assertFalse(HandClassifier.can_play([C(10, 3), C(10, 2)],
                                                  [C(5, 0), C(5, 1)]))


if __name__ == '__main__':
    unittest.main()
