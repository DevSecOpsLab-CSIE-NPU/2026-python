import importlib
import unittest


# 以動態匯入降低專案尚未完成時的編輯器警告；
# 若 models/classifier 未實作，測試會被標記為 skip。
try:
    models = importlib.import_module("models")
    classifier_mod = importlib.import_module("classifier")

    Card = models.Card
    HandClassifier = classifier_mod.HandClassifier
    CardType = classifier_mod.CardType

    CLASSIFIER_AVAILABLE = True
except Exception:
    Card = HandClassifier = CardType = None
    CLASSIFIER_AVAILABLE = False


def c(rank: int, suit: int):
    """建立測試用卡牌，簡化每個案例的可讀性。"""
    return Card(rank, suit)


@unittest.skipUnless(CLASSIFIER_AVAILABLE, "找不到 classifier.py 或 models.py，請先完成 Phase 2 實作")
class TestCardTypeEnum(unittest.TestCase):
    """CardType 列舉值測試。"""

    def test_cardtype_values(self):
        self.assertEqual(CardType.SINGLE.value, 1)
        self.assertEqual(CardType.PAIR.value, 2)
        self.assertEqual(CardType.TRIPLE.value, 3)
        self.assertEqual(CardType.STRAIGHT.value, 4)
        self.assertEqual(CardType.FLUSH.value, 5)
        self.assertEqual(CardType.FULL_HOUSE.value, 6)
        self.assertEqual(CardType.FOUR_OF_A_KIND.value, 7)
        self.assertEqual(CardType.STRAIGHT_FLUSH.value, 8)


@unittest.skipUnless(CLASSIFIER_AVAILABLE, "找不到 classifier.py 或 models.py，請先完成 Phase 2 實作")
class TestClassifyBasic(unittest.TestCase):
    """單張、對子、三條分類測試。"""

    def test_classify_single_ace(self):
        self.assertEqual(HandClassifier.classify([c(14, 3)]), (CardType.SINGLE, 14, 3))

    def test_classify_single_two(self):
        self.assertEqual(HandClassifier.classify([c(15, 0)]), (CardType.SINGLE, 15, 0))

    def test_classify_single_three(self):
        self.assertEqual(HandClassifier.classify([c(3, 0)]), (CardType.SINGLE, 3, 0))

    def test_classify_pair(self):
        # 牌型值使用 rank，對子的花色比較位可固定為 0（依題目規格）。
        self.assertEqual(HandClassifier.classify([c(14, 3), c(14, 2)]), (CardType.PAIR, 14, 0))

    def test_classify_pair_diff_rank(self):
        self.assertIsNone(HandClassifier.classify([c(14, 3), c(13, 3)]))

    def test_classify_pair_from_three(self):
        cards = [c(14, 3), c(14, 2), c(14, 1)]
        self.assertEqual(HandClassifier.classify(cards[:2]), (CardType.PAIR, 14, 0))

    def test_classify_triple(self):
        self.assertEqual(
            HandClassifier.classify([c(14, 3), c(14, 2), c(14, 1)]),
            (CardType.TRIPLE, 14, 0),
        )

    def test_classify_triple_not_enough(self):
        self.assertIsNone(HandClassifier.classify([c(14, 3), c(14, 2)]))


@unittest.skipUnless(CLASSIFIER_AVAILABLE, "找不到 classifier.py 或 models.py，請先完成 Phase 2 實作")
class TestClassifyFiveCards(unittest.TestCase):
    """五張牌型分類測試。"""

    def test_classify_straight(self):
        cards = [c(3, 0), c(4, 1), c(5, 2), c(6, 3), c(7, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT, 7, 0))

    def test_classify_straight_ace_low(self):
        # A-2-3-4-5 需要視為順子，且最高點數以 5 計算。
        cards = [c(14, 0), c(15, 1), c(3, 2), c(4, 3), c(5, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT, 5, 0))

    def test_classify_flush(self):
        cards = [c(3, 0), c(5, 0), c(7, 0), c(9, 0), c(11, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FLUSH, 11, 0))

    def test_classify_full_house(self):
        cards = [c(14, 3), c(14, 2), c(14, 1), c(15, 0), c(15, 1)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FULL_HOUSE, 14, 0))

    def test_classify_four_of_a_kind(self):
        cards = [c(14, 3), c(14, 2), c(14, 1), c(14, 0), c(3, 1)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.FOUR_OF_A_KIND, 14, 0))

    def test_classify_straight_flush(self):
        cards = [c(3, 0), c(4, 0), c(5, 0), c(6, 0), c(7, 0)]
        self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT_FLUSH, 7, 0))


@unittest.skipUnless(CLASSIFIER_AVAILABLE, "找不到 classifier.py 或 models.py，請先完成 Phase 2 實作")
class TestCompare(unittest.TestCase):
    """牌型比較測試：1=前者大、-1=後者大、0=平手。"""

    def test_compare_single_rank(self):
        self.assertEqual(HandClassifier.compare([c(14, 3)], [c(13, 3)]), 1)

    def test_compare_single_suit(self):
        self.assertEqual(HandClassifier.compare([c(14, 3)], [c(14, 2)]), 1)

    def test_compare_pair_rank(self):
        self.assertEqual(
            HandClassifier.compare([c(14, 3), c(14, 2)], [c(13, 3), c(13, 2)]),
            1,
        )

    def test_compare_pair_suit(self):
        # 同 rank 對子時，依實作常見做法會比最大的花色。
        self.assertEqual(
            HandClassifier.compare([c(14, 3), c(14, 2)], [c(14, 1), c(14, 0)]),
            1,
        )

    def test_compare_different_type(self):
        self.assertEqual(HandClassifier.compare([c(14, 3), c(14, 2)], [c(15, 3)]), 1)

    def test_compare_flush_vs_straight(self):
        flush = [c(3, 0), c(5, 0), c(7, 0), c(9, 0), c(11, 0)]
        straight = [c(3, 0), c(4, 1), c(5, 2), c(6, 3), c(7, 0)]
        self.assertEqual(HandClassifier.compare(flush, straight), 1)


@unittest.skipUnless(CLASSIFIER_AVAILABLE, "找不到 classifier.py 或 models.py，請先完成 Phase 2 實作")
class TestCanPlay(unittest.TestCase):
    """出牌合法性檢查測試。"""

    def test_can_play_first_3clubs(self):
        self.assertTrue(HandClassifier.can_play(None, [c(3, 0)]))

    def test_can_play_first_not_3clubs(self):
        self.assertFalse(HandClassifier.can_play(None, [c(14, 3)]))

    def test_can_play_same_type(self):
        # 前一手是對5，這手出對6應合法。
        last_play = [c(5, 3), c(5, 2)]
        new_play = [c(6, 3), c(6, 2)]
        self.assertTrue(HandClassifier.can_play(last_play, new_play))

    def test_can_play_diff_type(self):
        self.assertFalse(HandClassifier.can_play([c(5, 3), c(5, 2)], [c(6, 3)]))

    def test_can_play_not_stronger(self):
        # 前一手對10，這手對5 不夠大，應非法。
        last_play = [c(10, 3), c(10, 2)]
        new_play = [c(5, 3), c(5, 2)]
        self.assertFalse(HandClassifier.can_play(last_play, new_play))


if __name__ == "__main__":
    unittest.main(verbosity=2)
