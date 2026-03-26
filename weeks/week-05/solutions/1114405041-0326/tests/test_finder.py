"""Phase 3：HandFinder 測試。"""

from __future__ import annotations

import unittest

from game.finder import HandFinder
from game.models import Card, Hand


class TestFindSingles(unittest.TestCase):
    def test_find_singles(self):
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        out = HandFinder.find_singles(hand)
        self.assertEqual(len(out), 3)

    def test_find_singles_empty(self):
        self.assertEqual(HandFinder.find_singles(Hand()), [])


class TestFindPairs(unittest.TestCase):
    def test_find_pairs_one(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        out = HandFinder.find_pairs(hand)
        self.assertEqual(len(out), 1)

    def test_find_pairs_two(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(13, 3), Card(13, 0)])
        out = HandFinder.find_pairs(hand)
        self.assertEqual(len(out), 2)

    def test_find_pairs_none(self):
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        self.assertEqual(HandFinder.find_pairs(hand), [])


class TestFindTriples(unittest.TestCase):
    def test_find_triples_one(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0)])
        out = HandFinder.find_triples(hand)
        self.assertEqual(len(out), 1)

    def test_find_triples_with_extra(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 3), Card(13, 2)])
        out = HandFinder.find_triples(hand)
        self.assertEqual(len(out), 1)


class TestFindFives(unittest.TestCase):
    def test_find_straight(self):
        hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)])
        out = HandFinder.find_fives(hand)
        self.assertTrue(any(len(p) == 5 for p in out))

    def test_find_flush(self):
        hand = Hand([Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0), Card(14, 1)])
        out = HandFinder.find_fives(hand)
        self.assertTrue(any(len(p) == 5 for p in out))

    def test_find_full_house(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(15, 0), Card(15, 1), Card(3, 0)])
        out = HandFinder.find_fives(hand)
        self.assertTrue(any(len(p) == 5 for p in out))

    def test_find_four_of_a_kind(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 1), Card(5, 2)])
        out = HandFinder.find_fives(hand)
        self.assertTrue(any(len(p) == 5 for p in out))

    def test_find_straight_flush(self):
        hand = Hand([Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0), Card(9, 2)])
        out = HandFinder.find_fives(hand)
        self.assertTrue(any(len(p) == 5 for p in out))


class TestValidPlays(unittest.TestCase):
    def test_first_turn(self):
        hand = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
        out = HandFinder.get_all_valid_plays(hand, None)
        self.assertEqual(out, [[Card(3, 0)]])

    def test_with_last_single(self):
        hand = Hand([Card(6, 0), Card(7, 0), Card(3, 0)])
        out = HandFinder.get_all_valid_plays(hand, [Card(5, 0)])
        self.assertTrue(all(len(p) == 1 for p in out))

    def test_with_last_pair(self):
        hand = Hand([Card(6, 0), Card(6, 1), Card(3, 0)])
        out = HandFinder.get_all_valid_plays(hand, [Card(5, 0), Card(5, 1)])
        self.assertTrue(all(len(p) == 2 for p in out))

    def test_no_valid(self):
        hand = Hand([Card(3, 0), Card(4, 1)])
        out = HandFinder.get_all_valid_plays(hand, [Card(15, 3)])
        self.assertEqual(out, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
