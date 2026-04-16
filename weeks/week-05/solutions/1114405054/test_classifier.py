"""Phase 2 牌型分類的單元測試。"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


def _prepare_import_path() -> None:
    current = Path(__file__).resolve().parent

    for candidate in [current, *current.parents]:
        if (candidate / "game").is_dir():
            sys.path.insert(0, str(candidate))
            return

        if (candidate / "bigtwo" / "game").is_dir():
            sys.path.insert(0, str(candidate / "bigtwo"))
            return


_prepare_import_path()

from game.classifier import CardType, HandClassifier
from game.models import Card


def make_card(rank: int, suit: int) -> Card:
    return Card(rank, suit)


class TestCardType(unittest.TestCase):
    def test_cardtype_values(self) -> None:
        self.assertEqual(CardType.SINGLE.value, 1)
        self.assertEqual(CardType.PAIR.value, 2)
        self.assertEqual(CardType.TRIPLE.value, 3)
        self.assertEqual(CardType.STRAIGHT.value, 4)
        self.assertEqual(CardType.FLUSH.value, 5)
        self.assertEqual(CardType.FULL_HOUSE.value, 6)
        self.assertEqual(CardType.FOUR_OF_A_KIND.value, 7)
        self.assertEqual(CardType.STRAIGHT_FLUSH.value, 8)


class TestClassifySingle(unittest.TestCase):
    def test_classify_single_ace(self) -> None:
        cards = [make_card(14, 3)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.SINGLE, 14, 3))

    def test_classify_single_two(self) -> None:
        cards = [make_card(15, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.SINGLE, 15, 0))

    def test_classify_single_three(self) -> None:
        cards = [make_card(3, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.SINGLE, 3, 0))


class TestClassifyPair(unittest.TestCase):
    def test_classify_pair(self) -> None:
        cards = [make_card(14, 3), make_card(14, 2)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.PAIR, 14, 0))

    def test_classify_pair_diff_rank(self) -> None:
        cards = [make_card(14, 3), make_card(13, 3)]
        self.assertIsNone(HandClassifier.classify(cards))


class TestClassifyTriple(unittest.TestCase):
    def test_classify_triple(self) -> None:
        cards = [make_card(14, 3), make_card(14, 2), make_card(14, 1)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.TRIPLE, 14, 0))


class TestClassifyFiveCardHands(unittest.TestCase):
    def test_classify_straight(self) -> None:
        cards = [make_card(3, 0), make_card(4, 1), make_card(5, 2), make_card(6, 3), make_card(7, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT, 7, 0))

    def test_classify_straight_ace_low(self) -> None:
        cards = [make_card(14, 0), make_card(15, 1), make_card(3, 2), make_card(4, 3), make_card(5, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT, 5, 0))

    def test_classify_flush(self) -> None:
        cards = [make_card(3, 0), make_card(5, 0), make_card(7, 0), make_card(9, 0), make_card(11, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FLUSH, 11, 0))

    def test_classify_full_house(self) -> None:
        cards = [make_card(14, 3), make_card(14, 2), make_card(14, 1), make_card(15, 0), make_card(15, 1)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FULL_HOUSE, 14, 0))

    def test_classify_four_of_a_kind(self) -> None:
        cards = [make_card(14, 3), make_card(14, 2), make_card(14, 1), make_card(14, 0), make_card(3, 1)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FOUR_OF_A_KIND, 14, 0))

    def test_classify_straight_flush(self) -> None:
        cards = [make_card(3, 0), make_card(4, 0), make_card(5, 0), make_card(6, 0), make_card(7, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT_FLUSH, 7, 0))


class TestCompare(unittest.TestCase):
    def test_compare_single_rank(self) -> None:
        left = [make_card(14, 3)]
        right = [make_card(13, 3)]
        self.assertEqual(HandClassifier.compare(left, right), 1)

    def test_compare_single_suit(self) -> None:
        left = [make_card(14, 3)]
        right = [make_card(14, 2)]
        self.assertEqual(HandClassifier.compare(left, right), 1)

    def test_compare_pair_rank(self) -> None:
        left = [make_card(14, 3), make_card(14, 2)]
        right = [make_card(13, 3), make_card(13, 2)]
        self.assertEqual(HandClassifier.compare(left, right), 1)

    def test_compare_pair_suit(self) -> None:
        left = [make_card(14, 3), make_card(14, 2)]
        right = [make_card(14, 1), make_card(14, 0)]
        self.assertEqual(HandClassifier.compare(left, right), 1)

    def test_compare_different_type(self) -> None:
        left = [make_card(14, 3), make_card(14, 2)]
        right = [make_card(15, 3)]
        self.assertEqual(HandClassifier.compare(left, right), 1)

    def test_compare_flush_vs_straight(self) -> None:
        flush_cards = [make_card(3, 0), make_card(5, 0), make_card(7, 0), make_card(9, 0), make_card(11, 0)]
        straight_cards = [make_card(3, 0), make_card(4, 1), make_card(5, 2), make_card(6, 3), make_card(7, 0)]
        self.assertEqual(HandClassifier.compare(flush_cards, straight_cards), 1)


class TestCanPlay(unittest.TestCase):
    def test_can_play_first_3clubs(self) -> None:
        self.assertTrue(HandClassifier.can_play(None, [make_card(3, 0)]))

    def test_can_play_first_not_3clubs(self) -> None:
        self.assertFalse(HandClassifier.can_play(None, [make_card(14, 3)]))

    def test_can_play_same_type(self) -> None:
        last_play = [make_card(5, 3), make_card(5, 2)]
        cards = [make_card(6, 3), make_card(6, 2)]
        self.assertTrue(HandClassifier.can_play(last_play, cards))

    def test_can_play_diff_type(self) -> None:
        last_play = [make_card(5, 3), make_card(5, 2)]
        cards = [make_card(6, 3)]
        self.assertFalse(HandClassifier.can_play(last_play, cards))

    def test_can_play_not_stronger(self) -> None:
        last_play = [make_card(10, 3), make_card(10, 2)]
        cards = [make_card(5, 3), make_card(5, 2)]
        self.assertFalse(HandClassifier.can_play(last_play, cards))


if __name__ == "__main__":
    unittest.main(verbosity=2)
