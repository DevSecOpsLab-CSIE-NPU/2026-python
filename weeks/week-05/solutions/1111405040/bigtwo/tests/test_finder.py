"""
finder 模組測試。
"""

from __future__ import annotations

import unittest

from game.finder import HandFinder
from game.models import Card, Hand


class TestFinder(unittest.TestCase):
    """可用出牌搜尋測試。"""

    def test_find_singles(self) -> None:
        hand = Hand([Card(14, 3), Card(7, 1), Card(3, 0)])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 3)
        self.assertEqual(singles[0], [Card(14, 3)])

    def test_find_pairs(self) -> None:
        hand = Hand([Card(14, 3), Card(14, 1), Card(9, 0), Card(9, 2)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 2)

    def test_find_triples(self) -> None:
        hand = Hand([Card(14, 3), Card(14, 1), Card(14, 0), Card(9, 2)])
        triples = HandFinder.find_triples(hand)
        self.assertEqual(triples, [[Card(14, 3), Card(14, 1), Card(14, 0)]])

    def test_find_fives(self) -> None:
        hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 0), Card(7, 3)])
        fives = HandFinder.find_fives(hand)
        self.assertEqual(len(fives), 1)

    def test_get_all_valid_plays_first_turn(self) -> None:
        hand = Hand([Card(3, 0), Card(5, 1), Card(5, 3)])
        plays = HandFinder.get_all_valid_plays(hand, None, is_first_turn=True)
        self.assertTrue(all(Card(3, 0) in play for play in plays))

    def test_get_all_valid_plays_with_last_single(self) -> None:
        hand = Hand([Card(3, 0), Card(10, 1), Card(14, 3)])
        plays = HandFinder.get_all_valid_plays(hand, [Card(10, 1)])
        self.assertEqual(plays, [[Card(14, 3)]])


if __name__ == "__main__":
    unittest.main()
