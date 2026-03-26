"""
Phase 3: 牌型搜尋 - 單元測試
"""
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from game.models import Card, Hand
from game.finder import HandFinder
from game.classifier import CardType


class TestFindSingles(unittest.TestCase):
    """單張搜尋測試"""
    
    def test_find_singles(self):
        """測試找單張"""
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 3)
    
    def test_find_singles_empty(self):
        """測試空手牌"""
        hand = Hand([])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 0)


class TestFindPairs(unittest.TestCase):
    """對子搜尋測試"""
    
    def test_find_pairs_one(self):
        """測試找一對"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 1)
    
    def test_find_pairs_two(self):
        """測試找兩對"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(13, 3), Card(13, 1)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 2)
    
    def test_find_pairs_none(self):
        """測試找不到對子"""
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 0)
    
    def test_find_pairs_triple(self):
        """測試三條可以組多對"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 3)  # C(3,2) = 3


class TestFindTriples(unittest.TestCase):
    """三條搜尋測試"""
    
    def test_find_triples_one(self):
        """測試找一組三條"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0)])
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 1)
    
    def test_find_triples_none(self):
        """測試找不到三條"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 0)


class TestFindFives(unittest.TestCase):
    """五張牌型搜尋測試"""
    
    def test_find_straight(self):
        """測試找順子"""
        hand = Hand([
            Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0),
            Card(14, 3)
        ])
        fives = HandFinder.find_fives(hand)
        # 應該至少找到一個順子
        straights = [f for f in fives if sum(1 for c in f 
                     if c.rank in [3, 4, 5, 6, 7]) == 5]
        self.assertGreater(len(straights), 0)
    
    def test_find_flush(self):
        """測試找同花"""
        hand = Hand([
            Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0),
            Card(14, 3)
        ])
        fives = HandFinder.find_fives(hand)
        # 應該至少找到一個同花
        flushes = [f for f in fives if len(set(c.suit for c in f)) == 1]
        self.assertGreater(len(flushes), 0)
    
    def test_find_less_than_5(self):
        """測試少於5張牌"""
        hand = Hand([Card(3, 0), Card(4, 1)])
        fives = HandFinder.find_fives(hand)
        self.assertEqual(len(fives), 0)


class TestGetAllValidPlays(unittest.TestCase):
    """合法出牌搜尋測試"""
    
    def test_first_turn_with_3clubs(self):
        """測試第一回合有3♣"""
        hand = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
        valid_plays = HandFinder.get_all_valid_plays(hand, None)
        self.assertEqual(len(valid_plays), 1)
        self.assertEqual(valid_plays[0], [Card(3, 0)])
    
    def test_first_turn_without_3clubs(self):
        """測試第一回合沒有3♣"""
        hand = Hand([Card(14, 3), Card(13, 2)])
        valid_plays = HandFinder.get_all_valid_plays(hand, None)
        self.assertEqual(len(valid_plays), 0)
    
    def test_with_last_single(self):
        """測試跟上一個單張"""
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        last_play = [Card(5, 0)]
        valid_plays = HandFinder.get_all_valid_plays(hand, last_play)
        # 應該找到比5大的單張
        self.assertGreater(len(valid_plays), 0)
    
    def test_with_last_pair(self):
        """測試跟上一對"""
        hand = Hand([
            Card(14, 3), Card(14, 2),
            Card(13, 3), Card(13, 1),
            Card(3, 0)
        ])
        last_play = [Card(5, 0), Card(5, 1)]
        valid_plays = HandFinder.get_all_valid_plays(hand, last_play)
        # 應該只找到對子
        for play in valid_plays:
            self.assertEqual(len(play), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
