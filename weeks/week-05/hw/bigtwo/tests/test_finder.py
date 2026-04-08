"""
Phase 3 Tests: 牌型搜尋測試
HandFinder 類別的單元測試
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from game.models import Card, Hand
from game.finder import HandFinder


class TestFindSingles(unittest.TestCase):
    """找單張測試"""
    
    def test_find_singles(self):
        """測試找出所有單張"""
        cards = [Card(14, 3), Card(13, 2), Card(12, 1)]
        hand = Hand(cards)
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 3)


class TestFindPairs(unittest.TestCase):
    """找對子測試"""
    
    def test_find_pairs(self):
        """測試找出所有對子"""
        cards = [Card(14, 3), Card(14, 2), Card(13, 1)]
        hand = Hand(cards)
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 1)


class TestFindTriples(unittest.TestCase):
    """找三條測試"""
    
    def test_find_triples(self):
        """測試找出所有三條"""
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 0)]
        hand = Hand(cards)
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 1)


if __name__ == '__main__':
    unittest.main()
