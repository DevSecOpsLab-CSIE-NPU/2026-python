"""Phase 3：牌型搜尋單元測試

本測試檔對應 week-05/game_design/p3-test.md，
使用 Python 內建 unittest 驗證 HandFinder 的搜尋結果。
"""

import importlib
import unittest


# 動態載入，避免尚未實作時出現靜態匯入警告
_models_module = importlib.import_module("game.models")
_classifier_module = importlib.import_module("game.classifier")
_finder_module = importlib.import_module("game.finder")

Card = _models_module.Card
Hand = _models_module.Hand
CardType = _classifier_module.CardType
HandClassifier = _classifier_module.HandClassifier
HandFinder = _finder_module.HandFinder


def c(rank: int, suit: int) -> Card:
    """快速建立測試用 Card。"""
    return Card(rank, suit)


class TestFindSingles(unittest.TestCase):
    """單張搜尋測試。"""

    def test_find_singles(self):
        # [♠A, ♥K, ♣3] 應找到 3 個單張
        hand = Hand([c(14, 3), c(13, 2), c(3, 0)])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 3)
        self.assertTrue(all(len(play) == 1 for play in singles))

    def test_find_singles_empty(self):
        # 空手牌不應有任何單張組合
        singles = HandFinder.find_singles(Hand())
        self.assertEqual(len(singles), 0)


class TestFindPairs(unittest.TestCase):
    """對子搜尋測試。"""

    def test_find_pairs_one(self):
        # [♠A, ♥A, ♣3] 應找到 1 個對子（A）
        hand = Hand([c(14, 3), c(14, 2), c(3, 0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 1)
        self.assertEqual(HandClassifier.classify(pairs[0])[0], CardType.PAIR)
        self.assertEqual(HandClassifier.classify(pairs[0])[1], 14)

    def test_find_pairs_two(self):
        # [♠A, ♥A, ♠K, ♣K] 應找到 2 個對子
        hand = Hand([c(14, 3), c(14, 2), c(13, 3), c(13, 0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 2)

    def test_find_pairs_none(self):
        # 點數都不同時，不應找到對子
        hand = Hand([c(14, 3), c(13, 2), c(3, 0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 0)


class TestFindTriples(unittest.TestCase):
    """三條搜尋測試。"""

    def test_find_triples_one(self):
        # [♠A, ♥A, ♦A, ♣3] 應找到 1 個三條（A）
        hand = Hand([c(14, 3), c(14, 2), c(14, 1), c(3, 0)])
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 1)
        self.assertEqual(HandClassifier.classify(triples[0])[0], CardType.TRIPLE)
        self.assertEqual(HandClassifier.classify(triples[0])[1], 14)

    def test_find_triples_with_extra(self):
        # [AAA, KK] 應只找到 1 個三條
        hand = Hand([c(14, 3), c(14, 2), c(14, 1), c(13, 3), c(13, 0)])
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 1)


class TestFindFives(unittest.TestCase):
    """五張牌型搜尋測試。"""

    def test_find_straight(self):
        # 有順子牌時，find_fives 應能找到至少一組順子
        hand = Hand([c(3, 0), c(4, 1), c(5, 2), c(6, 3), c(7, 0), c(12, 1)])
        fives = HandFinder.find_fives(hand)
        self.assertTrue(any(HandClassifier.classify(play)[0] == CardType.STRAIGHT for play in fives))

    def test_find_flush(self):
        # 有同花牌時，應能找到至少一組同花
        hand = Hand([c(3, 0), c(5, 0), c(7, 0), c(9, 0), c(11, 0), c(14, 2)])
        fives = HandFinder.find_fives(hand)
        self.assertTrue(any(HandClassifier.classify(play)[0] == CardType.FLUSH for play in fives))

    def test_find_full_house(self):
        # 有葫蘆牌時，應能找到至少一組葫蘆
        hand = Hand([c(14, 3), c(14, 2), c(14, 1), c(15, 0), c(15, 1), c(3, 0)])
        fives = HandFinder.find_fives(hand)
        self.assertTrue(any(HandClassifier.classify(play)[0] == CardType.FULL_HOUSE for play in fives))

    def test_find_four_of_a_kind(self):
        # 有四條牌時，應能找到至少一組四條
        hand = Hand([c(14, 3), c(14, 2), c(14, 1), c(14, 0), c(3, 1), c(6, 2)])
        fives = HandFinder.find_fives(hand)
        self.assertTrue(any(HandClassifier.classify(play)[0] == CardType.FOUR_OF_A_KIND for play in fives))

    def test_find_straight_flush(self):
        # 有同花順牌時，應能找到至少一組同花順
        hand = Hand([c(3, 0), c(4, 0), c(5, 0), c(6, 0), c(7, 0), c(14, 2)])
        fives = HandFinder.find_fives(hand)
        self.assertTrue(any(HandClassifier.classify(play)[0] == CardType.STRAIGHT_FLUSH for play in fives))


class TestGetAllValidPlays(unittest.TestCase):
    """合法出牌搜尋測試。"""

    def test_first_turn(self):
        # 第一回合（last_play=None）只能出含 3♣ 的牌
        hand = Hand([c(3, 0), c(14, 3), c(13, 2)])
        plays = HandFinder.get_all_valid_plays(hand, None)
        self.assertTrue(all(any(card.rank == 3 and card.suit == 0 for card in play) for play in plays))
        self.assertIn([c(3, 0)], plays)

    def test_with_last_single(self):
        # 上家出單張 5，回傳應只包含可壓過的單張
        hand = Hand([c(3, 0), c(6, 1), c(14, 3), c(9, 2)])
        last_play = [c(5, 0)]
        plays = HandFinder.get_all_valid_plays(hand, last_play)
        self.assertTrue(all(len(play) == 1 for play in plays))
        self.assertTrue(all(HandClassifier.can_play(last_play, play) for play in plays))

    def test_with_last_pair(self):
        # 上家出對 5，回傳應只包含可壓過的對子
        hand = Hand([c(6, 3), c(6, 2), c(14, 3), c(13, 2)])
        last_play = [c(5, 0), c(5, 1)]
        plays = HandFinder.get_all_valid_plays(hand, last_play)
        self.assertTrue(all(len(play) == 2 for play in plays))
        self.assertTrue(all(HandClassifier.classify(play)[0] == CardType.PAIR for play in plays))
        self.assertTrue(all(HandClassifier.can_play(last_play, play) for play in plays))

    def test_no_valid(self):
        # 若手牌無法大於上家，應回傳空清單
        hand = Hand([c(3, 0), c(4, 1), c(7, 2)])
        last_play = [c(14, 3)]
        plays = HandFinder.get_all_valid_plays(hand, last_play)
        self.assertEqual(plays, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
