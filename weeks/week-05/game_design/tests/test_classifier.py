"""
Phase 2: 牌型分類 - 單元測試
"""
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from game.models import Card
from game.classifier import CardType, HandClassifier


class TestCardType(unittest.TestCase):
    """CardType 列舉測試"""
    
    def test_cardtype_values(self):
        """測試牌型值"""
        self.assertEqual(CardType.SINGLE, 1)
        self.assertEqual(CardType.PAIR, 2)
        self.assertEqual(CardType.TRIPLE, 3)
        self.assertEqual(CardType.STRAIGHT, 4)
        self.assertEqual(CardType.FLUSH, 5)
        self.assertEqual(CardType.FULL_HOUSE, 6)
        self.assertEqual(CardType.FOUR_OF_A_KIND, 7)
        self.assertEqual(CardType.STRAIGHT_FLUSH, 8)


class TestClassifySingle(unittest.TestCase):
    """單張分類測試"""
    
    def test_classify_single_ace(self):
        """測試單張A♠"""
        result = HandClassifier.classify([Card(14, 3)])
        self.assertEqual(result, (CardType.SINGLE, 14, 3))
    
    def test_classify_single_two(self):
        """測試單張2♣"""
        result = HandClassifier.classify([Card(15, 0)])
        self.assertEqual(result, (CardType.SINGLE, 15, 0))
    
    def test_classify_single_three(self):
        """測試單張3♣"""
        result = HandClassifier.classify([Card(3, 0)])
        self.assertEqual(result, (CardType.SINGLE, 3, 0))


class TestClassifyPair(unittest.TestCase):
    """對子分類測試"""
    
    def test_classify_pair(self):
        """測試對A"""
        cards = [Card(14, 3), Card(14, 2)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.PAIR)
        self.assertEqual(result[1], 14)
    
    def test_classify_not_pair(self):
        """測試非對子"""
        cards = [Card(14, 3), Card(13, 3)]
        result = HandClassifier.classify(cards)
        self.assertIsNone(result)


class TestClassifyTriple(unittest.TestCase):
    """三條分類測試"""
    
    def test_classify_triple(self):
        """測試三條A"""
        cards = [Card(14, 3), Card(14, 2), Card(14, 1)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.TRIPLE)
        self.assertEqual(result[1], 14)
    
    def test_classify_not_triple(self):
        """測試非三條"""
        cards = [Card(14, 3), Card(14, 2)]
        result = HandClassifier.classify(cards)
        # 2張相同點數應該判定為對子
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.PAIR)


class TestClassifyFive(unittest.TestCase):
    """五張牌型分類測試"""
    
    def test_classify_straight(self):
        """測試順子"""
        cards = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.STRAIGHT)
    
    def test_classify_straight_ace_low(self):
        """測試 A-2-3-4-5 順子"""
        cards = [Card(14, 0), Card(15, 1), Card(3, 2), Card(4, 3), Card(5, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.STRAIGHT)
        self.assertEqual(result[1], 5)  # 最大點數為5
    
    def test_classify_flush(self):
        """測試同花"""
        cards = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.FLUSH)
    
    def test_classify_full_house(self):
        """測試葫蘆"""
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(15, 0), Card(15, 1)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.FULL_HOUSE)
        self.assertEqual(result[1], 14)  # 三條的點數
    
    def test_classify_four_of_a_kind(self):
        """測試四條"""
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.FOUR_OF_A_KIND)
        self.assertEqual(result[1], 14)
    
    def test_classify_straight_flush(self):
        """測試同花順"""
        cards = [Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)]
        result = HandClassifier.classify(cards)
        self.assertEqual(result[0], CardType.STRAIGHT_FLUSH)


class TestCompare(unittest.TestCase):
    """牌型比較測試"""
    
    def test_compare_single_rank(self):
        """測試單張點數比較"""
        play1 = [Card(14, 3)]  # A♠
        play2 = [Card(13, 3)]  # K♠
        self.assertEqual(HandClassifier.compare(play1, play2), 1)
    
    def test_compare_single_suit(self):
        """測試單張花色比較"""
        play1 = [Card(14, 3)]  # A♠
        play2 = [Card(14, 2)]  # A♥
        self.assertEqual(HandClassifier.compare(play1, play2), 1)
    
    def test_compare_pair_rank(self):
        """測試對子點數比較"""
        play1 = [Card(14, 3), Card(14, 2)]  # 對A
        play2 = [Card(13, 3), Card(13, 2)]  # 對K
        self.assertEqual(HandClassifier.compare(play1, play2), 1)
    
    def test_compare_different_type(self):
        """測試不同牌型比較"""
        play1 = [Card(3, 0), Card(3, 1), Card(3, 2)]  # 三條
        play2 = [Card(14, 3), Card(14, 2)]  # 對A
        self.assertEqual(HandClassifier.compare(play1, play2), 1)
    
    def test_compare_flush_vs_straight(self):
        """測試同花 vs 順子"""
        straight = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        flush = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        self.assertEqual(HandClassifier.compare(flush, straight), 1)


class TestCanPlay(unittest.TestCase):
    """合法性檢查測試"""
    
    def test_can_play_first_3clubs(self):
        """測試第一回合出3♣"""
        result = HandClassifier.can_play(None, [Card(3, 0)])
        self.assertTrue(result)
    
    def test_can_play_first_not_3clubs(self):
        """測試第一回合出非3♣"""
        result = HandClassifier.can_play(None, [Card(14, 3)])
        self.assertFalse(result)
    
    def test_can_play_same_type_higher(self):
        """測試同類型更大的牌"""
        last = [Card(5, 0), Card(5, 1)]  # 對5
        curr = [Card(6, 0), Card(6, 1)]  # 對6
        result = HandClassifier.can_play(last, curr)
        self.assertTrue(result)
    
    def test_can_play_same_type_lower(self):
        """測試同類型更小的牌"""
        last = [Card(6, 0), Card(6, 1)]  # 對6
        curr = [Card(5, 0), Card(5, 1)]  # 對5
        result = HandClassifier.can_play(last, curr)
        self.assertFalse(result)
    
    def test_can_play_different_type(self):
        """測試不同類型牌"""
        last = [Card(5, 0), Card(5, 1)]  # 對5
        curr = [Card(14, 3)]  # 單A
        result = HandClassifier.can_play(last, curr)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
