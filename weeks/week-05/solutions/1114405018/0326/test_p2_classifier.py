"""
Phase 2：牌型分類（HandClassifier）單元測試

本檔案依據 p2-test.md 的規格撰寫，使用 Python 標準函式庫 unittest。
測試重點：
1. CardType 列舉值
2. classify() 對單張、對子、三條、五張牌型的判定
3. compare() 對同型/異型牌的比較
4. can_play() 的合法出牌邏輯

使用前提：
- 已完成 Phase 1 的 Card 類別（建議可從 models.py 匯入）
- 已實作 HandClassifier 與 CardType（建議可從 classifier.py 匯入）

執行方式（切到本檔所在資料夾後）：
    python -m unittest test_p2_classifier -v
"""

import unittest

# 依常見專案命名匯入。
# 若你的檔名不同，請改成實際路徑。
from models import Card
from classifier import HandClassifier, CardType


class TestCardTypeEnum(unittest.TestCase):
    """測試 CardType 列舉值是否符合規格。"""

    def test_cardtype_values(self):
        self.assertEqual(CardType.SINGLE.value, 1)
        self.assertEqual(CardType.PAIR.value, 2)
        self.assertEqual(CardType.TRIPLE.value, 3)
        self.assertEqual(CardType.STRAIGHT.value, 4)
        self.assertEqual(CardType.FLUSH.value, 5)
        self.assertEqual(CardType.FULL_HOUSE.value, 6)
        self.assertEqual(CardType.FOUR_OF_A_KIND.value, 7)
        self.assertEqual(CardType.STRAIGHT_FLUSH.value, 8)


class TestClassifierBasic(unittest.TestCase):
    """測試單張、對子、三條的分類結果。"""

    def test_classify_single_ace(self):
        # [♠A] -> (SINGLE, 14, 3)
        cards = [Card(14, 3)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.SINGLE, 14, 3),
        )

    def test_classify_single_two(self):
        # [2♣] -> (SINGLE, 15, 0)
        cards = [Card(15, 0)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.SINGLE, 15, 0),
        )

    def test_classify_single_three(self):
        # [♣3] -> (SINGLE, 3, 0)
        cards = [Card(3, 0)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.SINGLE, 3, 0),
        )

    def test_classify_pair(self):
        # [♠A, ♥A] -> (PAIR, 14, 0)
        cards = [Card(14, 3), Card(14, 2)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.PAIR, 14, 0),
        )

    def test_classify_pair_diff_rank(self):
        # [♠A, ♠K] 非對子 -> None
        cards = [Card(14, 3), Card(13, 3)]
        self.assertIsNone(HandClassifier.classify(cards))

    def test_classify_pair_from_three(self):
        # 三張中任取兩張同點數，仍應被視為對子
        cards = [Card(14, 3), Card(14, 2)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.PAIR, 14, 0),
        )

    def test_classify_triple(self):
        # [♠A, ♥A, ♦A] -> (TRIPLE, 14, 0)
        cards = [Card(14, 3), Card(14, 2), Card(14, 1)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.TRIPLE, 14, 0),
        )

    def test_classify_triple_not_enough(self):
        # 兩張不能構成三條
        cards = [Card(14, 3), Card(14, 2)]
        # 這組牌會被判為 PAIR，不是 TRIPLE；故此處明確檢查不是三條
        result = HandClassifier.classify(cards)
        self.assertNotEqual(result, (CardType.TRIPLE, 14, 0))


class TestClassifierFiveCards(unittest.TestCase):
    """測試五張牌型（順子、同花、葫蘆、鐵支、同花順）。"""

    def test_classify_straight(self):
        # [3♣,4♦,5♥,6♠,7♣] -> STRAIGHT，高牌 7
        cards = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.STRAIGHT, 7, 0),
        )

    def test_classify_straight_ace_low(self):
        # [A♣,2♦,3♥,4♠,5♣] -> A2345 順（低 A），高牌視為 5
        cards = [Card(14, 0), Card(15, 1), Card(3, 2), Card(4, 3), Card(5, 0)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.STRAIGHT, 5, 0),
        )

    def test_classify_flush(self):
        # 同花 -> FLUSH，第二欄通常用最大點數
        cards = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.FLUSH, 11, 0),
        )

    def test_classify_full_house(self):
        # [A,A,A,2,2] -> FULL_HOUSE，關鍵點數為三條的點數 A=14
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(15, 0), Card(15, 1)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.FULL_HOUSE, 14, 0),
        )

    def test_classify_four_of_a_kind(self):
        # [A,A,A,A,3] -> FOUR_OF_A_KIND，關鍵點數 A=14
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 1)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.FOUR_OF_A_KIND, 14, 0),
        )

    def test_classify_straight_flush(self):
        # [♣3,♣4,♣5,♣6,♣7] -> STRAIGHT_FLUSH，高牌 7
        cards = [Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)]
        self.assertEqual(
            HandClassifier.classify(cards),
            (CardType.STRAIGHT_FLUSH, 7, 0),
        )


class TestCompare(unittest.TestCase):
    """測試 compare(a, b) 回傳值：a>b 回傳 1，a<b 回傳 -1，相等回傳 0。"""

    def test_compare_single_rank(self):
        # ♠A vs ♠K -> A 較大
        a = [Card(14, 3)]
        b = [Card(13, 3)]
        self.assertEqual(HandClassifier.compare(a, b), 1)

    def test_compare_single_suit(self):
        # ♠A vs ♥A -> 同點數比花色，♠ > ♥
        a = [Card(14, 3)]
        b = [Card(14, 2)]
        self.assertEqual(HandClassifier.compare(a, b), 1)

    def test_compare_pair_rank(self):
        # 對 A > 對 K
        a = [Card(14, 3), Card(14, 2)]
        b = [Card(13, 3), Card(13, 2)]
        self.assertEqual(HandClassifier.compare(a, b), 1)

    def test_compare_pair_suit(self):
        # 同為對 A，預期以內部 tie-break 規則分出高下
        a = [Card(14, 3), Card(14, 2)]  # ♠♥A
        b = [Card(14, 1), Card(14, 0)]  # ♦♣A
        self.assertEqual(HandClassifier.compare(a, b), 1)

    def test_compare_different_type(self):
        # 對子牌型階級 > 單張
        a = [Card(5, 3), Card(5, 2)]
        b = [Card(6, 3)]
        self.assertEqual(HandClassifier.compare(a, b), 1)

    def test_compare_flush_vs_straight(self):
        # 同花牌型階級 > 順子
        flush_cards = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        straight_cards = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        self.assertEqual(HandClassifier.compare(flush_cards, straight_cards), 1)


class TestCanPlay(unittest.TestCase):
    """測試 can_play(last_play, new_play) 合法性判斷。"""

    def test_can_play_first_3clubs(self):
        # 首輪無上家牌時，若包含 ♣3 應允許
        self.assertTrue(HandClassifier.can_play(None, [Card(3, 0)]))

    def test_can_play_first_not_3clubs(self):
        # 首輪第一手若不含 ♣3，應拒絕
        self.assertFalse(HandClassifier.can_play(None, [Card(14, 3)]))

    def test_can_play_same_type(self):
        # 同牌型下，對 6 可壓對 5
        last_play = [Card(5, 3), Card(5, 2)]
        new_play = [Card(6, 3), Card(6, 2)]
        self.assertTrue(HandClassifier.can_play(last_play, new_play))

    def test_can_play_diff_type(self):
        # 對子不能壓單張（不同張數/不同牌型）
        last_play = [Card(5, 3), Card(5, 2)]
        new_play = [Card(6, 3)]
        self.assertFalse(HandClassifier.can_play(last_play, new_play))

    def test_can_play_not_stronger(self):
        # 對 5 不能壓對 10（新牌較弱）
        last_play = [Card(10, 3), Card(10, 2)]
        new_play = [Card(5, 3), Card(5, 2)]
        self.assertFalse(HandClassifier.can_play(last_play, new_play))


if __name__ == "__main__":
    unittest.main(verbosity=2)
