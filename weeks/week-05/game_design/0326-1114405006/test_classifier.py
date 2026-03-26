"""
Phase 2 牌型分類單元測試

說明：
- 使用 Python 內建 unittest。
- 測試目標為 CardType 與 HandClassifier。
- 本測試依 p2-test.md 規格設計，並加入繁體中文註解。
"""

import unittest

# 優先從同資料夾 models 匯入 Card；若專案路徑不同可自行調整
try:
    from models import Card
except ImportError as e:
    raise ImportError("無法匯入 Card，請先確認 models.py 可被 Python 找到。") from e


# 嘗試常見匯入路徑：classifier / game.classifier
try:
    from classifier import CardType, HandClassifier
except ImportError:
    try:
        from game.classifier import CardType, HandClassifier
    except ImportError as e:
        raise ImportError(
            "無法匯入 CardType, HandClassifier。請確認你的實作模組路徑。"
        ) from e


class TestCardTypeEnum(unittest.TestCase):
    """CardType 列舉測試"""

    def test_cardtype_values(self):
        # 驗證各牌型 enum 數值是否符合規格
        self.assertEqual(CardType.SINGLE.value, 1)
        self.assertEqual(CardType.PAIR.value, 2)
        self.assertEqual(CardType.TRIPLE.value, 3)
        self.assertEqual(CardType.STRAIGHT.value, 4)
        self.assertEqual(CardType.FLUSH.value, 5)
        self.assertEqual(CardType.FULL_HOUSE.value, 6)
        self.assertEqual(CardType.FOUR_OF_A_KIND.value, 7)
        self.assertEqual(CardType.STRAIGHT_FLUSH.value, 8)


class TestClassifySingle(unittest.TestCase):
    """單張分類測試"""

    def setUp(self):
        self.classifier = HandClassifier()

    def test_classify_single_ace(self):
        # [♠A] -> (SINGLE, 14, 3)
        result = self.classifier.classify([Card(14, 3)])
        self.assertEqual(result, (CardType.SINGLE, 14, 3))

    def test_classify_single_two(self):
        # [2♣] -> (SINGLE, 15, 0)
        result = self.classifier.classify([Card(15, 0)])
        self.assertEqual(result, (CardType.SINGLE, 15, 0))

    def test_classify_single_three(self):
        # [♣3] -> (SINGLE, 3, 0)
        result = self.classifier.classify([Card(3, 0)])
        self.assertEqual(result, (CardType.SINGLE, 3, 0))


class TestClassifyPair(unittest.TestCase):
    """對子分類測試"""

    def setUp(self):
        self.classifier = HandClassifier()

    def test_classify_pair(self):
        # [♠A,♥A] -> (PAIR, 14, 0)
        result = self.classifier.classify([Card(14, 3), Card(14, 2)])
        self.assertEqual(result, (CardType.PAIR, 14, 0))

    def test_classify_pair_diff_rank(self):
        # [♠A,♠K] 非對子 -> None
        result = self.classifier.classify([Card(14, 3), Card(13, 3)])
        self.assertIsNone(result)

    def test_classify_pair_from_three(self):
        # 三條取兩張仍可視為對子
        result = self.classifier.classify([Card(14, 3), Card(14, 2)])
        self.assertEqual(result, (CardType.PAIR, 14, 0))


class TestClassifyTriple(unittest.TestCase):
    """三條分類測試"""

    def setUp(self):
        self.classifier = HandClassifier()

    def test_classify_triple(self):
        # [♠A,♥A,♦A] -> (TRIPLE, 14, 0)
        result = self.classifier.classify([Card(14, 3), Card(14, 2), Card(14, 1)])
        self.assertEqual(result, (CardType.TRIPLE, 14, 0))

    def test_classify_triple_not_enough(self):
        # 張數不足 3，不是三條
        result = self.classifier.classify([Card(14, 3), Card(14, 2)])
        self.assertNotEqual(result, (CardType.TRIPLE, 14, 0))


class TestClassifyFiveCards(unittest.TestCase):
    """五張牌型分類測試"""

    def setUp(self):
        self.classifier = HandClassifier()

    def test_classify_straight(self):
        # [3♣,4♦,5♥,6♠,7♣] -> STRAIGHT，高牌 7
        cards = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        self.assertEqual(self.classifier.classify(cards), (CardType.STRAIGHT, 7, 0))

    def test_classify_straight_ace_low(self):
        # [A♣,2♦,3♥,4♠,5♣] -> A2345 順子，高牌 5
        cards = [Card(14, 0), Card(15, 1), Card(3, 2), Card(4, 3), Card(5, 0)]
        self.assertEqual(self.classifier.classify(cards), (CardType.STRAIGHT, 5, 0))

    def test_classify_flush(self):
        # 同花牌型 -> FLUSH，取最大點數 J(11)
        cards = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        self.assertEqual(self.classifier.classify(cards), (CardType.FLUSH, 11, 0))

    def test_classify_full_house(self):
        # 葫蘆：AAA22 -> FULL_HOUSE，關鍵點數為三條的 A(14)
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(15, 0), Card(15, 1)]
        self.assertEqual(self.classifier.classify(cards), (CardType.FULL_HOUSE, 14, 0))

    def test_classify_four_of_a_kind(self):
        # 鐵支：AAAA3 -> FOUR_OF_A_KIND，關鍵點數 A(14)
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 1)]
        self.assertEqual(
            self.classifier.classify(cards), (CardType.FOUR_OF_A_KIND, 14, 0)
        )

    def test_classify_straight_flush(self):
        # 同花順：♣3~♣7 -> STRAIGHT_FLUSH，高牌 7
        cards = [Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)]
        self.assertEqual(
            self.classifier.classify(cards), (CardType.STRAIGHT_FLUSH, 7, 0)
        )


class TestCompareHands(unittest.TestCase):
    """牌型比較測試"""

    def setUp(self):
        self.classifier = HandClassifier()

    def test_compare_single_rank(self):
        # 單張比點數：A > K
        result = self.classifier.compare([Card(14, 3)], [Card(13, 3)])
        self.assertEqual(result, 1)

    def test_compare_single_suit(self):
        # 同點數時比花色：♠A > ♥A
        result = self.classifier.compare([Card(14, 3)], [Card(14, 2)])
        self.assertEqual(result, 1)

    def test_compare_pair_rank(self):
        # 對 A > 對 K
        result = self.classifier.compare(
            [Card(14, 3), Card(14, 2)], [Card(13, 3), Card(13, 2)]
        )
        self.assertEqual(result, 1)

    def test_compare_pair_suit(self):
        # 同點數對子時，依規格檢查比較結果（預期前者較大）
        result = self.classifier.compare(
            [Card(14, 3), Card(14, 2)], [Card(14, 1), Card(14, 0)]
        )
        self.assertEqual(result, 1)

    def test_compare_different_type(self):
        # 對子應大於單張
        result = self.classifier.compare([Card(5, 3), Card(5, 2)], [Card(6, 3)])
        self.assertEqual(result, 1)

    def test_compare_flush_vs_straight(self):
        # 同花應大於順子
        flush_cards = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        straight_cards = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        result = self.classifier.compare(flush_cards, straight_cards)
        self.assertEqual(result, 1)


class TestCanPlay(unittest.TestCase):
    """合法性檢查測試"""

    def setUp(self):
        self.classifier = HandClassifier()

    def test_can_play_first_3clubs(self):
        # 首出且包含 ♣3 應合法
        self.assertTrue(self.classifier.can_play(None, [Card(3, 0)]))

    def test_can_play_first_not_3clubs(self):
        # 首出若不含 ♣3 應不合法
        self.assertFalse(self.classifier.can_play(None, [Card(14, 3)]))

    def test_can_play_same_type(self):
        # 同牌型且更大時可出（對6 > 對5）
        prev = [Card(5, 3), Card(5, 2)]
        curr = [Card(6, 3), Card(6, 1)]
        self.assertTrue(self.classifier.can_play(prev, curr))

    def test_can_play_diff_type(self):
        # 既有出牌為對子，單張不可直接壓
        prev = [Card(5, 3), Card(5, 2)]
        curr = [Card(6, 3)]
        self.assertFalse(self.classifier.can_play(prev, curr))

    def test_can_play_not_stronger(self):
        # 對5 無法壓過對10
        prev = [Card(10, 3), Card(10, 2)]
        curr = [Card(5, 3), Card(5, 2)]
        self.assertFalse(self.classifier.can_play(prev, curr))


if __name__ == "__main__":
    unittest.main(verbosity=2)
