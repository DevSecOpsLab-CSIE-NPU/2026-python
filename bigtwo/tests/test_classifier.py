import unittest
from game.models import Card
from game.classifier import CardType, HandClassifier

class TestCardType(unittest.TestCase):
    def test_cardtype_values(self):
        self.assertEqual(CardType.SINGLE.value, 1)
        self.assertEqual(CardType.PAIR.value, 2)
        self.assertEqual(CardType.TRIPLE.value, 3)
        self.assertEqual(CardType.STRAIGHT.value, 4)
        self.assertEqual(CardType.FLUSH.value, 5)
        self.assertEqual(CardType.FULL_HOUSE.value, 6)
        self.assertEqual(CardType.FOUR_OF_A_KIND.value, 7)
        self.assertEqual(CardType.STRAIGHT_FLUSH.value, 8)

class TestClassifier(unittest.TestCase):
    def test_classify_single_ace(self):
        result = HandClassifier.classify([Card(14, 3)])
        self.assertEqual(result[0], CardType.SINGLE)

    def test_classify_single_two(self):
        result = HandClassifier.classify([Card(15, 0)])
        self.assertEqual(result[0], CardType.SINGLE)

    def test_classify_pair(self):
        result = HandClassifier.classify([Card(14, 3), Card(14, 2)])
        self.assertEqual(result[0], CardType.PAIR)

    def test_classify_pair_diff_rank(self):
        result = HandClassifier.classify([Card(14, 3), Card(13, 3)])
        self.assertIsNone(result)

    def test_classify_triple(self):
        result = HandClassifier.classify([Card(14, 3), Card(14, 2), Card(14, 1)])
        self.assertEqual(result[0], CardType.TRIPLE)

    def test_classify_straight(self):
        cards = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.STRAIGHT)

    def test_classify_straight_ace_low(self):
        cards = [Card(14, 0), Card(15, 1), Card(3, 2), Card(4, 3), Card(5, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.STRAIGHT)

    def test_classify_flush(self):
        cards = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.FLUSH)

    def test_classify_full_house(self):
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0), Card(3, 1)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.FULL_HOUSE)

    def test_classify_four_of_a_kind(self):
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.FOUR_OF_A_KIND)

    def test_classify_straight_flush(self):
        cards = [Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.STRAIGHT_FLUSH)

    def test_compare_single_rank(self):
        self.assertEqual(HandClassifier.compare([Card(14, 0)], [Card(13, 0)]), 1)

    def test_compare_single_suit(self):
        self.assertEqual(HandClassifier.compare([Card(14, 3)], [Card(14, 2)]), 1)

    def test_compare_different_type(self):
        r1 = HandClassifier.classify([Card(14, 3), Card(14, 2)])
        r2 = HandClassifier.classify([Card(13, 0)])
        if r1 and r2:
            self.assertGreater(r1[0].value, r2[0].value)

    def test_can_play_first_3clubs(self):
        self.assertTrue(HandClassifier.can_play(None, [Card(3, 0)]))

    def test_can_play_first_not_3clubs(self):
        self.assertFalse(HandClassifier.can_play(None, [Card(14, 3)]))

    def test_can_play_same_type(self):
        last = [Card(5, 0)]
        cur = [Card(6, 0)]
        self.assertTrue(HandClassifier.can_play(last, cur))

    def test_can_play_not_stronger(self):
        last = [Card(10, 0)]
        cur = [Card(5, 0)]
        self.assertFalse(HandClassifier.can_play(last, cur))

if __name__ == "__main__":
    unittest.main()
