"""Phase 2 牌型分類測試（HandClassifier）。

使用方式（在專案根目錄執行）：
    python -m unittest tests.test_classifier -v

預期被測模組位置：
    game/classifier.py
"""

from __future__ import annotations

import importlib
import unittest

# 動態匯入可避免尚未實作時的編輯器靜態錯誤。
try:
    _models = importlib.import_module("game.models")
    _classifier = importlib.import_module("game.classifier")
except ModuleNotFoundError as exc:
    raise unittest.SkipTest("找不到 game.models 或 game.classifier，請先依 p1/p2-dev.md 實作") from exc

Card = _models.Card
CardType = _classifier.CardType
HandClassifier = _classifier.HandClassifier


class TestCardType(unittest.TestCase):
    """CardType 列舉值測試。"""

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
    """單張分類測試。"""

    def test_classify_single_ace(self) -> None:
        result = HandClassifier.classify([Card(14, 3)])
        self.assertEqual(result, (CardType.SINGLE, 14, 3))

    def test_classify_single_two(self) -> None:
        result = HandClassifier.classify([Card(15, 0)])
        self.assertEqual(result, (CardType.SINGLE, 15, 0))

    def test_classify_single_three(self) -> None:
        result = HandClassifier.classify([Card(3, 0)])
        self.assertEqual(result, (CardType.SINGLE, 3, 0))


class TestClassifyPair(unittest.TestCase):
    """對子分類測試。"""

    def test_classify_pair(self) -> None:
        result = HandClassifier.classify([Card(14, 3), Card(14, 2)])
        # p2-test 指定第三欄位預期為 0
        self.assertEqual(result, (CardType.PAIR, 14, 0))

    def test_classify_pair_diff_rank(self) -> None:
        result = HandClassifier.classify([Card(14, 3), Card(13, 3)])
        self.assertIsNone(result)

    def test_classify_pair_from_three(self) -> None:
        result = HandClassifier.classify([Card(14, 3), Card(14, 2)])
        self.assertEqual(result, (CardType.PAIR, 14, 0))


class TestClassifyTriple(unittest.TestCase):
    """三條分類測試。"""

    def test_classify_triple(self) -> None:
        result = HandClassifier.classify([Card(14, 3), Card(14, 2), Card(14, 1)])
        self.assertEqual(result, (CardType.TRIPLE, 14, 0))

    def test_classify_triple_not_enough(self) -> None:
        result = HandClassifier.classify([Card(14, 3), Card(14, 2)])
        self.assertNotEqual(result, (CardType.TRIPLE, 14, 0))


class TestClassifyFiveCards(unittest.TestCase):
    """五張牌型分類測試。"""

    def test_classify_straight(self) -> None:
        cards = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.STRAIGHT, 7, 0))

    def test_classify_straight_ace_low(self) -> None:
        cards = [Card(14, 0), Card(15, 1), Card(3, 2), Card(4, 3), Card(5, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.STRAIGHT, 5, 0))

    def test_classify_flush(self) -> None:
        cards = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.FLUSH, 11, 0))

    def test_classify_full_house(self) -> None:
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(15, 0), Card(15, 1)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.FULL_HOUSE, 14, 0))

    def test_classify_four_of_a_kind(self) -> None:
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 1)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.FOUR_OF_A_KIND, 14, 0))

    def test_classify_straight_flush(self) -> None:
        cards = [Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result, (CardType.STRAIGHT_FLUSH, 7, 0))


class TestCompare(unittest.TestCase):
    """牌型比較測試。"""

    def test_compare_single_rank(self) -> None:
        self.assertEqual(HandClassifier.compare([Card(14, 3)], [Card(13, 3)]), 1)

    def test_compare_single_suit(self) -> None:
        self.assertEqual(HandClassifier.compare([Card(14, 3)], [Card(14, 2)]), 1)

    def test_compare_pair_rank(self) -> None:
        play1 = [Card(14, 3), Card(14, 2)]
        play2 = [Card(13, 3), Card(13, 2)]
        self.assertEqual(HandClassifier.compare(play1, play2), 1)

    def test_compare_pair_suit(self) -> None:
        # 依題意用高花色對比同點數對子
        play1 = [Card(14, 3), Card(14, 2)]
        play2 = [Card(14, 1), Card(14, 0)]
        self.assertEqual(HandClassifier.compare(play1, play2), 1)

    def test_compare_different_type(self) -> None:
        self.assertEqual(HandClassifier.compare([Card(14, 3), Card(14, 2)], [Card(15, 3)]), 1)

    def test_compare_flush_vs_straight(self) -> None:
        flush = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        straight = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        self.assertEqual(HandClassifier.compare(flush, straight), 1)


class TestCanPlay(unittest.TestCase):
    """合法出牌檢查測試。"""

    def test_can_play_first_3clubs(self) -> None:
        self.assertTrue(HandClassifier.can_play(None, [Card(3, 0)]))

    def test_can_play_first_not_3clubs(self) -> None:
        self.assertFalse(HandClassifier.can_play(None, [Card(14, 3)]))

    def test_can_play_same_type(self) -> None:
        last_play = [Card(5, 3), Card(5, 2)]
        now_play = [Card(6, 3), Card(6, 2)]
        self.assertTrue(HandClassifier.can_play(last_play, now_play))

    def test_can_play_diff_type(self) -> None:
        last_play = [Card(5, 3), Card(5, 2)]
        now_play = [Card(6, 3)]
        self.assertFalse(HandClassifier.can_play(last_play, now_play))

    def test_can_play_not_stronger(self) -> None:
        last_play = [Card(10, 3), Card(10, 2)]
        now_play = [Card(5, 3), Card(5, 2)]
        self.assertFalse(HandClassifier.can_play(last_play, now_play))


if __name__ == "__main__":
    unittest.main(verbosity=2)
