"""Phase 2：牌型分類單元測試

本測試檔對應 week-05/game_design/p2-test.md，
使用 Python 內建 unittest 驗證 CardType 與 HandClassifier 的行為。
"""

import importlib
import unittest


# 動態載入，避免在未建立模組時出現靜態匯入警告
# 依開發文件優先使用 game.classifier / game.models
_classifier_module = importlib.import_module("game.classifier")
_models_module = importlib.import_module("game.models")

CardType = _classifier_module.CardType
HandClassifier = _classifier_module.HandClassifier
Card = _models_module.Card


def c(rank: int, suit: int) -> Card:
    """快速建立 Card，讓測試資料更精簡易讀。"""
    return Card(rank, suit)


class TestCardType(unittest.TestCase):
    """CardType 列舉值測試。"""

    def test_cardtype_values(self):
        # 驗證 enum 數值是否符合規格
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

    def test_classify_single_ace(self):
        # [♠A] -> (SINGLE, 14, 3)
        self.assertEqual(HandClassifier.classify([c(14, 3)]), (CardType.SINGLE, 14, 3))

    def test_classify_single_two(self):
        # [2♣] -> (SINGLE, 15, 0)
        self.assertEqual(HandClassifier.classify([c(15, 0)]), (CardType.SINGLE, 15, 0))

    def test_classify_single_three(self):
        # [♣3] -> (SINGLE, 3, 0)
        self.assertEqual(HandClassifier.classify([c(3, 0)]), (CardType.SINGLE, 3, 0))


class TestClassifyPair(unittest.TestCase):
    """對子分類測試。"""

    def test_classify_pair(self):
        # [♠A,♥A] -> (PAIR, 14, 0)
        self.assertEqual(HandClassifier.classify([c(14, 3), c(14, 2)]), (CardType.PAIR, 14, 0))

    def test_classify_pair_diff_rank(self):
        # 不同點數不構成對子
        self.assertIsNone(HandClassifier.classify([c(14, 3), c(13, 3)]))

    def test_classify_pair_from_three(self):
        # 從三條取任兩張仍可形成對子
        self.assertEqual(HandClassifier.classify([c(14, 3), c(14, 2)]), (CardType.PAIR, 14, 0))


class TestClassifyTriple(unittest.TestCase):
    """三條分類測試。"""

    def test_classify_triple(self):
        # [♠A,♥A,♦A] -> (TRIPLE, 14, 0)
        self.assertEqual(
            HandClassifier.classify([c(14, 3), c(14, 2), c(14, 1)]),
            (CardType.TRIPLE, 14, 0),
        )

    def test_classify_triple_not_enough(self):
        # 只有兩張且不成對，不算三條
        self.assertIsNone(HandClassifier.classify([c(14, 3), c(13, 2)]))


class TestClassifyFiveCards(unittest.TestCase):
    """五張牌型分類測試。"""

    def test_classify_straight(self):
        # 一般順子：3-4-5-6-7
        cards = [c(3, 0), c(4, 1), c(5, 2), c(6, 3), c(7, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT, 7, 0))

    def test_classify_straight_ace_low(self):
        # 特例順子：A-2-3-4-5（A 當低位）
        cards = [c(14, 0), c(15, 1), c(3, 2), c(4, 3), c(5, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT, 5, 0))

    def test_classify_flush(self):
        # 同花：五張花色相同
        cards = [c(3, 0), c(5, 0), c(7, 0), c(9, 0), c(11, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FLUSH, 11, 0))

    def test_classify_full_house(self):
        # 葫蘆：三條 + 一對
        cards = [c(14, 3), c(14, 2), c(14, 1), c(15, 0), c(15, 1)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FULL_HOUSE, 14, 0))

    def test_classify_four_of_a_kind(self):
        # 四條：四張同點數 + 任意一張
        cards = [c(14, 3), c(14, 2), c(14, 1), c(14, 0), c(3, 1)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FOUR_OF_A_KIND, 14, 0))

    def test_classify_straight_flush(self):
        # 同花順：同花且連續
        cards = [c(3, 0), c(4, 0), c(5, 0), c(6, 0), c(7, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT_FLUSH, 7, 0))


class TestCompare(unittest.TestCase):
    """牌型比較測試。"""

    def test_compare_single_rank(self):
        # 單張比點數：A > K
        self.assertEqual(HandClassifier.compare([c(14, 3)], [c(13, 3)]), 1)

    def test_compare_single_suit(self):
        # 單張同點數比花色：♠ > ♥
        self.assertEqual(HandClassifier.compare([c(14, 3)], [c(14, 2)]), 1)

    def test_compare_pair_rank(self):
        # 對子比點數：AA > KK
        self.assertEqual(HandClassifier.compare([c(14, 3), c(14, 2)], [c(13, 3), c(13, 2)]), 1)

    def test_compare_pair_suit(self):
        # 對子同點數時，較高花色組合應較大
        self.assertEqual(HandClassifier.compare([c(14, 3), c(14, 2)], [c(14, 1), c(14, 0)]), 1)

    def test_compare_different_type(self):
        # 不同牌型時，牌型級別高者勝（對子 > 單張）
        self.assertEqual(HandClassifier.compare([c(10, 0), c(10, 1)], [c(6, 3)]), 1)

    def test_compare_flush_vs_straight(self):
        # 五張牌中同花 > 順子
        flush = [c(3, 0), c(5, 0), c(7, 0), c(9, 0), c(11, 0)]
        straight = [c(3, 0), c(4, 1), c(5, 2), c(6, 3), c(7, 0)]
        self.assertEqual(HandClassifier.compare(flush, straight), 1)


class TestCanPlay(unittest.TestCase):
    """合法出牌檢查測試。"""

    def test_can_play_first_3clubs(self):
        # 首出必須包含 3♣，此案例合法
        self.assertTrue(HandClassifier.can_play(None, [c(3, 0)]))

    def test_can_play_first_not_3clubs(self):
        # 首出若不含 3♣，應不合法
        self.assertFalse(HandClassifier.can_play(None, [c(14, 3)]))

    def test_can_play_same_type(self):
        # 相同牌型且更大 -> 可出
        last_play = [c(5, 0), c(5, 1)]
        cards = [c(6, 0), c(6, 1)]
        self.assertTrue(HandClassifier.can_play(last_play, cards))

    def test_can_play_diff_type(self):
        # 不同牌型（對子接單張）-> 不可出
        last_play = [c(5, 0), c(5, 1)]
        cards = [c(6, 0)]
        self.assertFalse(HandClassifier.can_play(last_play, cards))

    def test_can_play_not_stronger(self):
        # 相同牌型但不夠大 -> 不可出
        last_play = [c(10, 0), c(10, 1)]
        cards = [c(5, 0), c(5, 1)]
        self.assertFalse(HandClassifier.can_play(last_play, cards))


if __name__ == "__main__":
    unittest.main(verbosity=2)
