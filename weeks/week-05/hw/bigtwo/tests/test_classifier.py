"""
Phase 2 Tests: 牌型分類測試
HandClassifier 類別的單元測試
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from game.models import Card, Hand
from game.classifier import HandClassifier, CardType


class TestCardType(unittest.TestCase):
    """CardType 列舉測試"""
    
    def test_cardtype_values(self):
        """測試 CardType 的值"""
        self.assertEqual(CardType.SINGLE, 1)
        self.assertEqual(CardType.PAIR, 2)
        self.assertEqual(CardType.TRIPLE, 3)
        self.assertEqual(CardType.STRAIGHT, 4)
        self.assertEqual(CardType.FLUSH, 5)
        self.assertEqual(CardType.FULL_HOUSE, 6)
        self.assertEqual(CardType.FOUR_OF_A_KIND, 7)
        self.assertEqual(CardType.STRAIGHT_FLUSH, 8)


class TestClassify(unittest.TestCase):
    """牌型分類測試"""
    
    def test_classify_single(self):
        """測試單張分類"""
        cards = [Card(14, 3)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.SINGLE)
        self.assertEqual(result[1], 14)
    
    def test_classify_pair(self):
        """測試對子分類"""
        cards = [Card(14, 3), Card(14, 2)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.PAIR)
        self.assertEqual(result[1], 14)
    
    def test_classify_pair_invalid(self):
        """測試無效的對子"""
        cards = [Card(14, 3), Card(13, 2)]
        result = HandClassifier.classify(cards)
        self.assertIsNone(result)
    
    def test_classify_triple(self):
        """測試三條分類"""
        cards = [Card(14, 3), Card(14, 2), Card(14, 1)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.TRIPLE)
        self.assertEqual(result[1], 14)
    
    def test_classify_straight(self):
        """測試順子分類"""
        cards = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.STRAIGHT)
    
    def test_classify_flush(self):
        """測試同花分類"""
        cards = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.FLUSH)
    
    def test_classify_full_house(self):
        """測試葫蘆分類"""
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 0), Card(13, 3)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.FULL_HOUSE)
    
    def test_classify_four_of_a_kind(self):
        """測試四條分類"""
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(13, 3)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.FOUR_OF_A_KIND)


class TestCompare(unittest.TestCase):
    """牌型比較測試"""
    
    def test_compare_single_rank(self):
        """測試單張等級比較"""
        play1 = [Card(14, 3)]  # A
        play2 = [Card(13, 3)]  # K
        result = HandClassifier.compare(play1, play2)
        self.assertEqual(result, 1)
    
    def test_compare_different_type(self):
        """測試不同牌型比較"""
        play1 = [Card(14, 3), Card(14, 2)]  # Pair
        play2 = [Card(13, 3)]  # Single
        result = HandClassifier.compare(play1, play2)
        self.assertEqual(result, 1)


class TestCanPlay(unittest.TestCase):
    """可出牌檢查測試"""
    
    def test_can_play_first_3clubs(self):
        """測試第一回合只能出3♣"""
        cards = [Card(3, 0)]
        result = HandClassifier.can_play(None, cards)
        self.assertTrue(result)
    
    def test_can_play_first_not_3clubs(self):
        """測試第一回合不能出其他牌"""
        cards = [Card(14, 3)]
        result = HandClassifier.can_play(None, cards)
        self.assertFalse(result)
    
    def test_can_play_same_type(self):
        """測試可以出相同牌型"""
        last_play = ([Card(5, 3)], "Player 2")
        cards = [Card(6, 2)]
        result = HandClassifier.can_play(last_play, cards)
        self.assertTrue(result)
    
    def test_can_play_different_type(self):
        """測試不能出不同牌型"""
        last_play = ([Card(14, 3), Card(14, 2)], "Player 2")
        cards = [Card(13, 3)]
        result = HandClassifier.can_play(last_play, cards)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
