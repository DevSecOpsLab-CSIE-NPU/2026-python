"""
classifier 模組測試。
"""

from __future__ import annotations

import unittest

from game.classifier import CardType, HandClassifier
from game.models import Card


class TestClassifier(unittest.TestCase):
    """牌型辨識與比較測試。"""

    def test_cardtype_values(self) -> None:
        self.assertEqual(CardType.SINGLE.value, 1)
        self.assertEqual(CardType.STRAIGHT_FLUSH.value, 8)

    def test_classify_single_pair_triple(self) -> None:
        self.assertEqual(
            HandClassifier.classify([Card(14, 3)]),
            (CardType.SINGLE, 14, 3),
        )
        self.assertEqual(
            HandClassifier.classify([Card(14, 3), Card(14, 1)]),
            (CardType.PAIR, 14, 3),
        )
        self.assertEqual(
            HandClassifier.classify([Card(14, 3), Card(14, 1), Card(14, 0)]),
            (CardType.TRIPLE, 14, 3),
        )

    def test_classify_straight(self) -> None:
        cards = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 0), Card(7, 3)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.STRAIGHT, 7, 3),
        )

    def test_classify_straight_ace_low(self) -> None:
        cards = [Card(14, 2), Card(15, 0), Card(3, 0), Card(4, 1), Card(5, 3)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.STRAIGHT, 5, 3),
        )

    def test_classify_flush(self) -> None:
        cards = [Card(3, 2), Card(7, 2), Card(9, 2), Card(11, 2), Card(13, 2)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.FLUSH, 13, 2),
        )

    def test_classify_full_house(self) -> None:
        cards = [Card(14, 3), Card(14, 1), Card(14, 0), Card(9, 2), Card(9, 1)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.FULL_HOUSE, 14, 3),
        )

    def test_classify_four_of_a_kind(self) -> None:
        cards = [Card(10, 0), Card(10, 1), Card(10, 2), Card(10, 3), Card(7, 2)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.FOUR_OF_A_KIND, 10, 3),
        )

    def test_classify_straight_flush(self) -> None:
        cards = [Card(7, 3), Card(8, 3), Card(9, 3), Card(10, 3), Card(11, 3)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.STRAIGHT_FLUSH, 11, 3),
        )

    def test_compare_single_rank_and_suit(self) -> None:
        self.assertEqual(HandClassifier.compare([Card(14, 3)], [Card(13, 3)]), 1)
        self.assertEqual(HandClassifier.compare([Card(14, 3)], [Card(14, 2)]), 1)

    def test_compare_five_card_type(self) -> None:
        flush = [Card(3, 2), Card(7, 2), Card(9, 2), Card(11, 2), Card(13, 2)]
        straight = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 0), Card(7, 3)]
        self.assertEqual(HandClassifier.compare(flush, straight), 1)

    def test_can_play_first_turn_must_contain_3_clubs(self) -> None:
        self.assertTrue(HandClassifier.can_play(None, [Card(3, 0)], is_first_turn=True))
        self.assertFalse(HandClassifier.can_play(None, [Card(14, 3)], is_first_turn=True))

    def test_can_play_same_type_stronger(self) -> None:
        self.assertTrue(
            HandClassifier.can_play([Card(10, 2)], [Card(14, 3)]),
        )
        self.assertFalse(
            HandClassifier.can_play([Card(14, 3)], [Card(10, 2)]),
        )

    def test_can_play_different_type_invalid_for_non_five_cards(self) -> None:
        self.assertFalse(
            HandClassifier.can_play([Card(9, 1)], [Card(12, 0), Card(12, 3)]),
        )


if __name__ == "__main__":
    unittest.main()
