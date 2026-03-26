# p3-finder-unit-test.py
# Phase 3 單元測試：HandFinder
#
# 測試依據：p3-test.md
# 依賴：p1_models.py、p2_classifier.py、p3_finder.py（請自行建立實作）
#
# 執行方式：
#   python p3-finder-unit-test.py

import unittest
from p1_models import Card, Hand
from p2_classifier import CardType, HandClassifier

# 請在完成 p3_finder.py 後取消下方的 import 註解
from p3_finder import HandFinder


# =========================================================
# TestFindSingles — 單張搜尋
# =========================================================
class TestFindSingles(unittest.TestCase):

    def test_find_singles(self):
        """[♠A, ♥K, ♣3] 應找到 3 個單張。"""
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        result = HandFinder.find_singles(hand)
        self.assertEqual(len(result), 3)
        # 每個元素應為長度 1 的 list
        for play in result:
            self.assertEqual(len(play), 1)

    def test_find_singles_empty(self):
        """空手牌應找到 0 個單張。"""
        result = HandFinder.find_singles(Hand())
        self.assertEqual(len(result), 0)


# =========================================================
# TestFindPairs — 對子搜尋
# =========================================================
class TestFindPairs(unittest.TestCase):

    def test_find_pairs_one(self):
        """[♠A, ♥A, ♣3] 應找到 1 個對子（A 對）。"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        result = HandFinder.find_pairs(hand)
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), 2)

    def test_find_pairs_two(self):
        """[♠A, ♥A, ♠K, ♣K] 應找到 2 個對子。"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(13, 3), Card(13, 0)])
        result = HandFinder.find_pairs(hand)
        self.assertEqual(len(result), 2)

    def test_find_pairs_none(self):
        """[♠A, ♥K, ♣3] 沒有相同點數，應找到 0 個對子。"""
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        result = HandFinder.find_pairs(hand)
        self.assertEqual(len(result), 0)


# =========================================================
# TestFindTriples — 三條搜尋
# =========================================================
class TestFindTriples(unittest.TestCase):

    def test_find_triples_one(self):
        """[♠A, ♥A, ♦A, ♣3] 應找到 1 個三條（A 三條）。"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0)])
        result = HandFinder.find_triples(hand)
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), 3)

    def test_find_triples_with_extra(self):
        """[♠A, ♥A, ♦A, ♠K, ♣K] 含三條 A，應至少找到 1 個三條。"""
        hand = Hand([
            Card(14, 3), Card(14, 2), Card(14, 1),
            Card(13, 3), Card(13, 0),
        ])
        result = HandFinder.find_triples(hand)
        self.assertGreaterEqual(len(result), 1)


# =========================================================
# TestFindFives — 五張牌型搜尋
# =========================================================
class TestFindFives(unittest.TestCase):

    def _all_types(self, hand: Hand):
        """輔助：取得 find_fives 結果中所有 CardType 集合。"""
        results = HandFinder.find_fives(hand)
        types = set()
        for play in results:
            r = HandClassifier.classify(play)
            if r:
                types.add(r[0])
        return types

    def test_find_straight(self):
        """含 3♣→7♣ 連續牌的手牌，應能找到順子。"""
        hand = Hand([
            Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0),
            Card(14, 3),
        ])
        types = self._all_types(hand)
        self.assertIn(CardType.STRAIGHT, types)

    def test_find_flush(self):
        """含五張 ♣ 的手牌，應能找到同花。"""
        hand = Hand([
            Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0),
            Card(14, 3),
        ])
        types = self._all_types(hand)
        self.assertIn(CardType.FLUSH, types)

    def test_find_full_house(self):
        """含 AAA + KK 的手牌，應能找到葫蘆。"""
        hand = Hand([
            Card(14, 3), Card(14, 2), Card(14, 1),
            Card(13, 3), Card(13, 0),
        ])
        types = self._all_types(hand)
        self.assertIn(CardType.FULL_HOUSE, types)

    def test_find_four_of_a_kind(self):
        """含四張 A 的手牌，應能找到四條。"""
        hand = Hand([
            Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0),
            Card(3, 0),
        ])
        types = self._all_types(hand)
        self.assertIn(CardType.FOUR_OF_A_KIND, types)

    def test_find_straight_flush(self):
        """含五張同花連續牌，應能找到同花順。"""
        hand = Hand([
            Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0),
        ])
        types = self._all_types(hand)
        self.assertIn(CardType.STRAIGHT_FLUSH, types)


# =========================================================
# TestGetAllValidPlays — 合法出牌搜尋
# =========================================================
class TestGetAllValidPlays(unittest.TestCase):

    def test_first_turn(self):
        """第一回合（last=None），手牌有 3♣，只應回傳含 3♣ 的出牌。"""
        hand = Hand([Card(3, 0), Card(14, 3), Card(14, 2)])
        result = HandFinder.get_all_valid_plays(hand, None)
        # 所有合法出牌必須包含 3♣
        for play in result:
            self.assertIn(Card(3, 0), play)

    def test_with_last_single(self):
        """上家出單張 5♣，只應回傳單張出牌。"""
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        last = [Card(5, 0)]
        result = HandFinder.get_all_valid_plays(hand, last)
        for play in result:
            self.assertEqual(len(play), 1)

    def test_with_last_pair(self):
        """上家出對 5，只應回傳對子出牌。"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        last = [Card(5, 0), Card(5, 1)]
        result = HandFinder.get_all_valid_plays(hand, last)
        for play in result:
            self.assertEqual(len(play), 2)

    def test_no_valid(self):
        """手牌無法大過上家時，應回傳空清單。"""
        hand = Hand([Card(3, 0), Card(4, 1)])  # 只有小牌
        last = [Card(14, 3)]                   # 上家出 ♠A
        result = HandFinder.get_all_valid_plays(hand, last)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
