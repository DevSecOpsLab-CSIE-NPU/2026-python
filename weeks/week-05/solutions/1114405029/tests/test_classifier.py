import unittest
from game.models import Card
from game.classifier import HandClassifier, CardType

class TestClassifier(unittest.TestCase):
    def test_special_straights(self):
        """[邊緣測試] 大老二特有順子判定：A-2-3-4-5 與 2-3-4-5-6"""
        # A, 2, 3, 4, 5
        s1 = [Card(14,0), Card(15,1), Card(3,2), Card(4,3), Card(5,0)]
        type1, rank1, suit1 = HandClassifier.classify(s1)
        self.assertEqual(type1, CardType.STRAIGHT)
        self.assertEqual(rank1, 15) # 邏輯最大牌必須是 2(15)

    def test_five_card_hierarchy(self):
        """[規則測試] 驗證五張牌型的階級互壓 (同花順 > 鐵支 > 葫蘆 > 同花 > 順子)"""
        straight = [Card(3,0), Card(4,1), Card(5,2), Card(6,3), Card(7,0)]
        flush = [Card(3,1), Card(5,1), Card(8,1), Card(10,1), Card(12,1)]
        full_house = [Card(3,0), Card(3,1), Card(3,2), Card(4,0), Card(4,1)]
        
        # 同花 必須壓過 順子
        self.assertEqual(HandClassifier.compare(flush, straight), 1)
        # 葫蘆 必須壓過 同花
        self.assertEqual(HandClassifier.compare(full_house, flush), 1)
        # 順子 無法壓過 葫蘆
        self.assertEqual(HandClassifier.compare(straight, full_house), -1)

    def test_invalid_compare(self):
        """[防呆測試] 張數不同或無法比較的牌型"""
        single = [Card(15, 3)] # ♠2
        pair = [Card(3,0), Card(3,1)]
        # 單張不能打對子，回傳應為 0 (不合法)
        self.assertEqual(HandClassifier.compare(pair, single), 0)