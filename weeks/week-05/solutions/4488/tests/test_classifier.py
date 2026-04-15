"""Phase 2: Card type classification tests."""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.models import Card
from game.classifier import HandClassifier, CardType


class TestCardTypeClassification(unittest.TestCase):
    """牌型分類測試。"""

    def test_classify_single(self):
        """測試單張分類。"""
        cards = [Card(14, 3)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.SINGLE)

    def test_classify_pair(self):
        """測試對子分類。"""
        cards = [Card(14, 3), Card(14, 2)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.PAIR)

    def test_classify_triple(self):
        """測試三條分類。"""
        cards = [Card(14, 3), Card(14, 2), Card(14, 1)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.TRIPLE)

    def test_classify_straight(self):
        """測試順子分類。"""
        cards = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.STRAIGHT)

    def test_classify_flush(self):
        """測試同花分類。"""
        cards = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.FLUSH)


class TestCanPlay(unittest.TestCase):
    """合法性檢查測試。"""

    def test_can_play_first_3clubs(self):
        """測試第一回合必須出 3♣。"""
        cards = [Card(3, 0)]
        result = HandClassifier.can_play(None, cards)
        self.assertTrue(result)

    def test_cannot_play_first_not_3clubs(self):
        """測試第一回合不能出其他牌。"""
        cards = [Card(14, 3)]
        result = HandClassifier.can_play(None, cards)
        self.assertFalse(result)

    def test_can_play_same_type_higher(self):
        """測試同牌型可以出更大的牌。"""
        last = [Card(3, 0)]
        cards = [Card(14, 3)]
        result = HandClassifier.can_play(last, cards)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
