"""Phase 2：HandClassifier 單元測試。

依據 p2-test.md 的案例設計，涵蓋：
1. CardType 列舉值
2. 各牌型分類
3. compare 比較規則
4. can_play 出牌合法性
"""

from __future__ import annotations

import unittest

from game.classifier import CardType, HandClassifier
from game.models import Card


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


class TestClassifySinglesPairsTriples(unittest.TestCase):
    def test_classify_single_ace(self):
        self.assertEqual(HandClassifier.classify([Card(14, 3)]), (CardType.SINGLE, 14, 3))

    def test_classify_single_two(self):
        self.assertEqual(HandClassifier.classify([Card(15, 0)]), (CardType.SINGLE, 15, 0))

    def test_classify_single_three(self):
        self.assertEqual(HandClassifier.classify([Card(3, 0)]), (CardType.SINGLE, 3, 0))

    def test_classify_pair(self):
        self.assertEqual(HandClassifier.classify([Card(14, 3), Card(14, 2)]), (CardType.PAIR, 14, 3))

    def test_classify_pair_diff_rank(self):
        self.assertIsNone(HandClassifier.classify([Card(14, 3), Card(13, 3)]))

    def test_classify_pair_from_three(self):
        self.assertEqual(HandClassifier.classify([Card(14, 3), Card(14, 2)]), (CardType.PAIR, 14, 3))

    def test_classify_triple(self):
        self.assertEqual(
            HandClassifier.classify([Card(14, 3), Card(14, 2), Card(14, 1)]),
            (CardType.TRIPLE, 14, 3),
        )

    def test_classify_triple_not_enough(self):
        # 兩張不同點數既不是對子也不是三條，應回傳 None。
        self.assertIsNone(HandClassifier.classify([Card(14, 3), Card(13, 2)]))


class TestClassifyFiveCards(unittest.TestCase):
    def test_classify_straight(self):
        cards = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT, 7, 3))

    def test_classify_straight_ace_low(self):
        cards = [Card(14, 0), Card(15, 1), Card(3, 2), Card(4, 3), Card(5, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT, 5, 3))

    def test_classify_flush(self):
        cards = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FLUSH, 11, 0))

    def test_classify_full_house(self):
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(15, 0), Card(15, 1)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FULL_HOUSE, 14, 3))

    def test_classify_four_of_a_kind(self):
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 1)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FOUR_OF_A_KIND, 14, 3))

    def test_classify_straight_flush(self):
        cards = [Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT_FLUSH, 7, 0))


class TestCompare(unittest.TestCase):
    def test_compare_single_rank(self):
        self.assertEqual(HandClassifier.compare([Card(14, 3)], [Card(13, 3)]), 1)

    def test_compare_single_suit(self):
        self.assertEqual(HandClassifier.compare([Card(14, 3)], [Card(14, 2)]), 1)

    def test_compare_pair_rank(self):
        a_pair = [Card(14, 3), Card(14, 2)]
        k_pair = [Card(13, 3), Card(13, 2)]
        self.assertEqual(HandClassifier.compare(a_pair, k_pair), 1)

    def test_compare_pair_suit(self):
        high = [Card(14, 3), Card(14, 2)]
        low = [Card(14, 1), Card(14, 0)]
        self.assertEqual(HandClassifier.compare(high, low), 1)

    def test_compare_different_type(self):
        self.assertEqual(HandClassifier.compare([Card(14, 3), Card(14, 2)], [Card(15, 3)]), 1)

    def test_compare_flush_vs_straight(self):
        flush = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        straight = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        self.assertEqual(HandClassifier.compare(flush, straight), 1)


class TestCanPlay(unittest.TestCase):
    def test_can_play_first_3clubs(self):
        self.assertTrue(HandClassifier.can_play(None, [Card(3, 0)]))

    def test_can_play_first_not_3clubs(self):
        self.assertFalse(HandClassifier.can_play(None, [Card(14, 3)]))

    def test_can_play_same_type(self):
        last_play = [Card(5, 0), Card(5, 1)]
        cards = [Card(6, 0), Card(6, 1)]
        self.assertTrue(HandClassifier.can_play(last_play, cards))

    def test_can_play_diff_type(self):
        last_play = [Card(5, 0), Card(5, 1)]
        cards = [Card(6, 0)]
        self.assertFalse(HandClassifier.can_play(last_play, cards))

    def test_can_play_not_stronger(self):
        last_play = [Card(10, 0), Card(10, 1)]
        cards = [Card(5, 0), Card(5, 1)]
        self.assertFalse(HandClassifier.can_play(last_play, cards))


if __name__ == "__main__":
    unittest.main(verbosity=2)
