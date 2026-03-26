import importlib
import unittest


# 動態匯入：若 Phase 2/3 尚未實作完成，測試會先以 skip 呈現。
try:
    models = importlib.import_module("models")
    classifier_mod = importlib.import_module("classifier")
    finder_mod = importlib.import_module("finder")

    Card = models.Card
    Hand = models.Hand
    HandClassifier = classifier_mod.HandClassifier
    CardType = classifier_mod.CardType
    HandFinder = finder_mod.HandFinder

    FINDER_AVAILABLE = True
except Exception:
    Card = Hand = HandClassifier = CardType = HandFinder = None
    FINDER_AVAILABLE = False


def c(rank: int, suit: int):
    """建立測試卡牌，讓案例更精簡。"""
    return Card(rank, suit)


@unittest.skipUnless(FINDER_AVAILABLE, "找不到 finder.py / classifier.py / models.py，請先完成 Phase 2~3 實作")
class TestFindSingles(unittest.TestCase):
    """單張搜尋測試。"""

    def test_find_singles(self):
        hand = Hand([c(14, 3), c(13, 2), c(3, 0)])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 3)
        self.assertTrue(all(len(play) == 1 for play in singles))

    def test_find_singles_empty(self):
        hand = Hand([])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 0)


@unittest.skipUnless(FINDER_AVAILABLE, "找不到 finder.py / classifier.py / models.py，請先完成 Phase 2~3 實作")
class TestFindPairs(unittest.TestCase):
    """對子搜尋測試。"""

    def test_find_pairs_one(self):
        hand = Hand([c(14, 3), c(14, 2), c(3, 0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 1)
        self.assertEqual(HandClassifier.classify(pairs[0]), (CardType.PAIR, 14, 0))

    def test_find_pairs_two(self):
        hand = Hand([c(14, 3), c(14, 2), c(13, 3), c(13, 0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 2)
        for pair in pairs:
            self.assertEqual(len(pair), 2)
            self.assertEqual(HandClassifier.classify(pair)[0], CardType.PAIR)

    def test_find_pairs_none(self):
        hand = Hand([c(14, 3), c(13, 2), c(3, 0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 0)


@unittest.skipUnless(FINDER_AVAILABLE, "找不到 finder.py / classifier.py / models.py，請先完成 Phase 2~3 實作")
class TestFindTriples(unittest.TestCase):
    """三條搜尋測試。"""

    def test_find_triples_one(self):
        hand = Hand([c(14, 3), c(14, 2), c(14, 1), c(3, 0)])
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 1)
        self.assertEqual(HandClassifier.classify(triples[0]), (CardType.TRIPLE, 14, 0))

    def test_find_triples_with_extra(self):
        hand = Hand([c(14, 3), c(14, 2), c(14, 1), c(13, 3), c(13, 0)])
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 1)
        self.assertEqual(HandClassifier.classify(triples[0])[0], CardType.TRIPLE)


@unittest.skipUnless(FINDER_AVAILABLE, "找不到 finder.py / classifier.py / models.py，請先完成 Phase 2~3 實作")
class TestFindFives(unittest.TestCase):
    """五張牌型搜尋測試。"""

    def test_find_straight(self):
        hand = Hand([c(3, 0), c(4, 1), c(5, 2), c(6, 3), c(7, 0), c(14, 3)])
        plays = HandFinder.find_fives(hand)
        types = {HandClassifier.classify(play)[0] for play in plays}
        self.assertIn(CardType.STRAIGHT, types)

    def test_find_flush(self):
        hand = Hand([c(3, 0), c(5, 0), c(7, 0), c(9, 0), c(11, 0), c(14, 3)])
        plays = HandFinder.find_fives(hand)
        types = {HandClassifier.classify(play)[0] for play in plays}
        self.assertIn(CardType.FLUSH, types)

    def test_find_full_house(self):
        hand = Hand([c(14, 3), c(14, 2), c(14, 1), c(15, 0), c(15, 1), c(3, 0)])
        plays = HandFinder.find_fives(hand)
        types = {HandClassifier.classify(play)[0] for play in plays}
        self.assertIn(CardType.FULL_HOUSE, types)

    def test_find_four_of_a_kind(self):
        hand = Hand([c(14, 3), c(14, 2), c(14, 1), c(14, 0), c(3, 1), c(5, 0)])
        plays = HandFinder.find_fives(hand)
        types = {HandClassifier.classify(play)[0] for play in plays}
        self.assertIn(CardType.FOUR_OF_A_KIND, types)

    def test_find_straight_flush(self):
        hand = Hand([c(3, 0), c(4, 0), c(5, 0), c(6, 0), c(7, 0), c(14, 3)])
        plays = HandFinder.find_fives(hand)
        types = {HandClassifier.classify(play)[0] for play in plays}
        self.assertIn(CardType.STRAIGHT_FLUSH, types)


@unittest.skipUnless(FINDER_AVAILABLE, "找不到 finder.py / classifier.py / models.py，請先完成 Phase 2~3 實作")
class TestGetAllValidPlays(unittest.TestCase):
    """合法出牌搜尋測試。"""

    def test_first_turn(self):
        # 第一手必須包含 3♣。
        hand = Hand([c(3, 0), c(14, 3), c(13, 2)])
        plays = HandFinder.get_all_valid_plays(hand, None)
        self.assertTrue(len(plays) >= 1)
        self.assertTrue(all(c(3, 0) in play for play in plays))

    def test_with_last_single(self):
        # 上家出單張 5，回傳合法牌應只含單張。
        hand = Hand([c(3, 0), c(6, 3), c(8, 1), c(14, 2)])
        last_play = [c(5, 0)]
        plays = HandFinder.get_all_valid_plays(hand, last_play)
        self.assertTrue(all(len(play) == 1 for play in plays))

    def test_with_last_pair(self):
        # 上家出對5，回傳合法牌應只含對子。
        hand = Hand([c(6, 3), c(6, 2), c(8, 1), c(8, 0), c(14, 3)])
        last_play = [c(5, 0), c(5, 1)]
        plays = HandFinder.get_all_valid_plays(hand, last_play)
        self.assertTrue(all(len(play) == 2 for play in plays))
        for play in plays:
            self.assertEqual(HandClassifier.classify(play)[0], CardType.PAIR)

    def test_no_valid(self):
        # 無法壓過上家時應回傳空清單。
        hand = Hand([c(3, 0), c(4, 1), c(6, 2)])
        last_play = [c(15, 3)]
        plays = HandFinder.get_all_valid_plays(hand, last_play)
        self.assertEqual(plays, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
