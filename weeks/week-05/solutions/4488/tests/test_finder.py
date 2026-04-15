"""Phase 3: Hand pattern finder tests."""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.models import Card, Hand
from game.finder import HandFinder


class TestHandFinder(unittest.TestCase):
    """牌型搜尋測試。"""

    def test_find_singles(self):
        """測試尋找單張。"""
        cards = [Card(14, 3), Card(13, 2), Card(3, 0)]
        hand = Hand(cards)
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 3)

    def test_find_pairs(self):
        """測試尋找對子。"""
        cards = [Card(14, 3), Card(14, 2), Card(3, 0)]
        hand = Hand(cards)
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 1)

    def test_find_triples(self):
        """測試尋找三條。"""
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0)]
        hand = Hand(cards)
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 1)

    def test_get_valid_plays_first(self):
        """測試第一回合合法出牌。"""
        cards = [Card(3, 0), Card(14, 3), Card(13, 2)]
        hand = Hand(cards)
        plays = HandFinder.get_all_valid_plays(hand, None)
        # 第一回合只能出 3♣
        self.assertEqual(len(plays), 1)
        self.assertEqual(len(plays[0]), 1)


if __name__ == '__main__':
    unittest.main()
