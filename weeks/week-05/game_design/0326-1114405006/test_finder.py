"""
Phase 3 牌型搜尋單元測試

說明：
- 使用 Python 內建 unittest。
- 測試目標為 HandFinder 類別。
- 內容依 p3-test.md 設計，並加入繁體中文註解。
"""

import unittest

from finder import HandFinder
from models import Card, Hand


class TestFindSingles(unittest.TestCase):
    """單張搜尋測試"""

    def test_find_singles(self):
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 3)
        self.assertTrue(all(len(play) == 1 for play in singles))

    def test_find_singles_empty(self):
        hand = Hand([])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 0)


class TestFindPairs(unittest.TestCase):
    """對子搜尋測試"""

    def test_find_pairs_one(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 1)
        self.assertEqual({c.rank for c in pairs[0]}, {14})

    def test_find_pairs_two(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(13, 3), Card(13, 0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 2)

    def test_find_pairs_none(self):
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 0)


class TestFindTriples(unittest.TestCase):
    """三條搜尋測試"""

    def test_find_triples_one(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0)])
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 1)
        self.assertEqual({c.rank for c in triples[0]}, {14})

    def test_find_triples_with_extra(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 3), Card(13, 0)])
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 1)


class TestFindFives(unittest.TestCase):
    """五張牌型搜尋測試"""

    def test_find_straight(self):
        hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)])
        fives = HandFinder.find_fives(hand)
        self.assertTrue(any(len(play) == 5 for play in fives))

    def test_find_flush(self):
        hand = Hand([Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)])
        fives = HandFinder.find_fives(hand)
        self.assertTrue(any(len(play) == 5 and len({c.suit for c in play}) == 1 for play in fives))

    def test_find_full_house(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(15, 0), Card(15, 1)])
        fives = HandFinder.find_fives(hand)
        self.assertTrue(any(len(play) == 5 for play in fives))

    def test_find_four_of_a_kind(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 1)])
        fives = HandFinder.find_fives(hand)
        self.assertTrue(any(len(play) == 5 for play in fives))

    def test_find_straight_flush(self):
        hand = Hand([Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)])
        fives = HandFinder.find_fives(hand)
        self.assertTrue(any(len(play) == 5 and len({c.suit for c in play}) == 1 for play in fives))


class TestGetAllValidPlays(unittest.TestCase):
    """合法出牌搜尋測試"""

    def test_first_turn(self):
        hand = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
        plays = HandFinder.get_all_valid_plays(hand, None)
        # 第一手所有可出牌都必須包含 3♣
        self.assertTrue(len(plays) > 0)
        self.assertTrue(all(any(c.rank == 3 and c.suit == 0 for c in play) for play in plays))

    def test_with_last_single(self):
        hand = Hand([Card(6, 0), Card(7, 1), Card(9, 2), Card(14, 3)])
        last = [Card(5, 1)]
        plays = HandFinder.get_all_valid_plays(hand, last)
        self.assertTrue(all(len(play) == 1 for play in plays))

    def test_with_last_pair(self):
        hand = Hand([Card(6, 0), Card(6, 1), Card(7, 2), Card(7, 3), Card(3, 0)])
        last = [Card(5, 1), Card(5, 2)]
        plays = HandFinder.get_all_valid_plays(hand, last)
        self.assertTrue(all(len(play) == 2 for play in plays))

    def test_no_valid(self):
        hand = Hand([Card(3, 0), Card(4, 1), Card(6, 2)])
        last = [Card(15, 3)]
        plays = HandFinder.get_all_valid_plays(hand, last)
        self.assertEqual(plays, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
