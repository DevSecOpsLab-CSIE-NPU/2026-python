# -*- coding: utf-8 -*-
"""
大二紙牌遊戲 - Phase 2 牌型分類單元測試

針對 HandClassifier 類別的完整測試套件
使用 Python 標準函式庫 unittest
"""

import unittest
from enum import Enum
from p1_models import Card, Hand


# ============================================================================
# 【牌型列舉】
# ============================================================================

class CardType(Enum):
    """
    牌型列舉
    
    定義遊戲中所有可能的牌型及其優先級
    """
    SINGLE = 1           # 單張
    PAIR = 2             # 對子
    TRIPLE = 3           # 三條
    STRAIGHT = 4         # 順子（5張）
    FLUSH = 5            # 同花（5張）
    FULL_HOUSE = 6       # 滿堂紅（5張，3+2）
    FOUR_OF_A_KIND = 7   # 四條（5張，4+1）
    STRAIGHT_FLUSH = 8   # 順子同花（5張）


# ============================================================================
# 【分類器類別】（供測試調用）
# ============================================================================

class HandClassifier:
    """
    牌型分類器
    
    根據牌的組合，分類為不同牌型並提供比較機制
    """
    
    @staticmethod
    def classify(cards):
        """
        分類牌型
        
        Args:
            cards: Hand 對象或 Card 列表
            
        Returns:
            (CardType, rank, suit) tuple，無法分類時回傳 None
        """
        if not cards:
            return None
        
        # 轉換為 Card 列表
        card_list = list(cards) if isinstance(cards, Hand) else cards
        length = len(card_list)
        
        # 單張
        if length == 1:
            card = card_list[0]
            return (CardType.SINGLE, card.rank, card.suit)
        
        # 對子
        if length == 2:
            if card_list[0].rank == card_list[1].rank:
                return (CardType.PAIR, card_list[0].rank, card_list[0].suit)
            return None
        
        # 三條
        if length == 3:
            if card_list[0].rank == card_list[1].rank == card_list[2].rank:
                return (CardType.TRIPLE, card_list[0].rank, card_list[0].suit)
            return None
        
        # 五張牌型
        if length == 5:
            # 先判斷是否四條
            four_kind = HandClassifier._check_four_of_a_kind(card_list)
            if four_kind:
                return four_kind
            
            # 再判斷是否滿堂紅
            full_house = HandClassifier._check_full_house(card_list)
            if full_house:
                return full_house
            
            # 再判斷是否順子同花
            straight_flush = HandClassifier._check_straight_flush(card_list)
            if straight_flush:
                return straight_flush
            
            # 再判斷是否同花
            flush = HandClassifier._check_flush(card_list)
            if flush:
                return flush
            
            # 最後判斷是否順子
            straight = HandClassifier._check_straight(card_list)
            if straight:
                return straight
            
            return None
        
        return None
    
    @staticmethod
    def _check_four_of_a_kind(cards):
        """檢查四條"""
        ranks = [card.rank for card in cards]
        rank_counts = {}
        for rank in ranks:
            rank_counts[rank] = rank_counts.get(rank, 0) + 1
        
        for rank, count in rank_counts.items():
            if count == 4:
                return (CardType.FOUR_OF_A_KIND, rank, 0)
        return None
    
    @staticmethod
    def _check_full_house(cards):
        """檢查滿堂紅（三張+對子）"""
        ranks = [card.rank for card in cards]
        rank_counts = {}
        for rank in ranks:
            rank_counts[rank] = rank_counts.get(rank, 0) + 1
        
        if sorted(rank_counts.values()) == [2, 3]:
            # 找到三張的等級
            for rank, count in rank_counts.items():
                if count == 3:
                    return (CardType.FULL_HOUSE, rank, 0)
        return None
    
    @staticmethod
    def _check_straight(cards):
        """檢查順子"""
        ranks = sorted([card.rank for card in cards])
        
        # 檢查普通順子
        if ranks[-1] - ranks[0] == 4 and len(set(ranks)) == 5:
            return (CardType.STRAIGHT, ranks[-1], 0)
        
        # 檢查 A-2-3-4-5 (最小順子，A作為1)
        if set(ranks) == {14, 2, 3, 4, 5}:
            return (CardType.STRAIGHT, 5, 0)
        
        return None
    
    @staticmethod
    def _check_flush(cards):
        """檢查同花（5張相同花色）"""
        suits = [card.suit for card in cards]
        if len(set(suits)) == 1:
            # 所有牌同花，取最大等級
            ranks = [card.rank for card in cards]
            max_rank = max(ranks)
            return (CardType.FLUSH, max_rank, suits[0])
        return None
    
    @staticmethod
    def _check_straight_flush(cards):
        """檢查順子同花"""
        # 先檢查是否同花
        suits = [card.suit for card in cards]
        if len(set(suits)) != 1:
            return None
        
        # 再檢查是否順子
        ranks = sorted([card.rank for card in cards])
        
        # 普通順子同花
        if ranks[-1] - ranks[0] == 4 and len(set(ranks)) == 5:
            return (CardType.STRAIGHT_FLUSH, ranks[-1], suits[0])
        
        # A-2-3-4-5 順子同花
        if set(ranks) == {14, 2, 3, 4, 5}:
            return (CardType.STRAIGHT_FLUSH, 5, suits[0])
        
        return None
    
    @staticmethod
    def compare(classification1, classification2):
        """
        比較兩個牌型
        
        Args:
            classification1: (CardType, rank, suit) tuple
            classification2: (CardType, rank, suit) tuple
            
        Returns:
            1 if classification1 > classification2
            -1 if classification1 < classification2
            0 if equal
        """
        if not classification1 or not classification2:
            return 0
        
        type1, rank1, suit1 = classification1
        type2, rank2, suit2 = classification2
        
        # 先比較牌型等級（同花三條優於順子）
        if type1.value != type2.value:
            return 1 if type1.value > type2.value else -1
        
        # 同牌型，比較等級
        if rank1 != rank2:
            # 特殊情況：等級2最高，除非都包含等級2
            if rank1 == 2:
                return 1
            if rank2 == 2:
                return -1
            return 1 if rank1 > rank2 else -1
        
        # 等級相同，比較花色
        if suit1 != suit2:
            return 1 if suit1 > suit2 else -1
        
        return 0
    
    @staticmethod
    def can_play(last_classification, cards_to_play):
        """
        檢查是否能出牌
        
        Args:
            last_classification: 上一手出的牌型，None表示首手
            cards_to_play: 要出的牌 (Hand 或 Card 列表)
            
        Returns:
            True 可以出牌，False 不能出牌
        """
        # 首手必須包含梅花3
        if last_classification is None:
            card_list = list(cards_to_play)
            for card in card_list:
                if card.rank == 3 and card.suit == 0:
                    return True
            return False
        
        # 非首手：分類牌型，檢查數量和牌型
        current_classification = HandClassifier.classify(cards_to_play)
        if not current_classification:
            return False
        
        # 牌張數相同
        if len(list(cards_to_play)) != len(list(cards_to_play)):
            return False
        
        # 牌型相同或更強
        type1, _, _ = last_classification
        type2, _, _ = current_classification
        
        if type2.value != type1.value:
            return False
        
        # 牌型相同，比較大小
        return HandClassifier.compare(current_classification, last_classification) > 0


# ============================================================================
# 【單元測試】
# ============================================================================


class TestCardTypeEnum(unittest.TestCase):
    """CardType 列舉測試"""
    
    def test_cardtype_values(self):
        """【測試1】CardType 列舉值正確"""
        self.assertEqual(CardType.SINGLE.value, 1)
        self.assertEqual(CardType.PAIR.value, 2)
        self.assertEqual(CardType.TRIPLE.value, 3)
        self.assertEqual(CardType.STRAIGHT.value, 4)
        self.assertEqual(CardType.FLUSH.value, 5)
        self.assertEqual(CardType.FULL_HOUSE.value, 6)
        self.assertEqual(CardType.FOUR_OF_A_KIND.value, 7)
        self.assertEqual(CardType.STRAIGHT_FLUSH.value, 8)


class TestSingleClassification(unittest.TestCase):
    """單張分類測試"""
    
    def test_classify_single_ace(self):
        """【測試2】分類 A：回傳 (SINGLE, 14, suit)"""
        cards = Hand([Card(14, 3)])  # ♠A
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.SINGLE)
        self.assertEqual(result[1], 14)
        self.assertEqual(result[2], 3)
    
    def test_classify_single_two(self):
        """【測試3】分類 2：回傳 (SINGLE, 2, suit)"""
        cards = Hand([Card(2, 0)])  # ♣2
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.SINGLE)
        self.assertEqual(result[1], 2)
        self.assertEqual(result[2], 0)
    
    def test_classify_single_three(self):
        """【測試4】分類梅花3：回傳 (SINGLE, 3, 0)"""
        cards = Hand([Card(3, 0)])  # ♣3
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.SINGLE)
        self.assertEqual(result[1], 3)
        self.assertEqual(result[2], 0)


class TestPairClassification(unittest.TestCase):
    """對子分類測試"""
    
    def test_classify_pair(self):
        """【測試5】分類對A：回傳 (PAIR, 14, suit)"""
        cards = Hand([Card(14, 3), Card(14, 2)])  # ♠A, ♥A
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.PAIR)
        self.assertEqual(result[1], 14)
    
    def test_classify_pair_diff_rank(self):
        """【測試6】分類不同等級：無法分類，回傳 None"""
        cards = Hand([Card(14, 3), Card(13, 3)])  # ♠A, ♠K
        result = HandClassifier.classify(cards)
        self.assertIsNone(result)
    
    def test_classify_pair_from_three(self):
        """【測試7】三張相同等級應分類為三條，不是對子"""
        cards = Hand([Card(14, 3), Card(14, 2), Card(14, 1)])  # ♠A, ♥A, ♦A
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.TRIPLE)


class TestTripleClassification(unittest.TestCase):
    """三條分類測試"""
    
    def test_classify_triple(self):
        """【測試8】分類三條：回傳 (TRIPLE, 14, suit)"""
        cards = Hand([Card(14, 3), Card(14, 2), Card(14, 1)])  # ♠A, ♥A, ♦A
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.TRIPLE)
        self.assertEqual(result[1], 14)
    
    def test_classify_triple_not_enough(self):
        """【測試9】兩張相同等級應分類為對子，不是三條"""
        cards = Hand([Card(14, 3), Card(14, 2)])
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.PAIR)


class TestFiveCardClassification(unittest.TestCase):
    """五張牌型分類測試"""
    
    def test_classify_straight(self):
        """【測試10】分類順子：3-4-5-6-7"""
        cards = Hand([Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)])
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.STRAIGHT)
        self.assertEqual(result[1], 7)  # 最大等級
    
    def test_classify_straight_ace_low(self):
        """【測試11】分類最小順子：A-2-3-4-5（A作為1）"""
        cards = Hand([Card(14, 0), Card(2, 1), Card(3, 2), Card(4, 3), Card(5, 0)])
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.STRAIGHT)
        self.assertEqual(result[1], 5)  # 最大有效等級
    
    def test_classify_flush(self):
        """【測試12】分類同花：5張梅花"""
        cards = Hand([Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)])
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.FLUSH)
        self.assertEqual(result[1], 11)  # 最大等級 (J)
    
    def test_classify_full_house(self):
        """【測試13】分類滿堂紅：3條A + 2條2"""
        cards = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(2, 0), Card(2, 1)])
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.FULL_HOUSE)
        self.assertEqual(result[1], 14)  # 三條的等級
    
    def test_classify_four_of_a_kind(self):
        """【測試14】分類四條：4條A + 1張3"""
        cards = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 0)])
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.FOUR_OF_A_KIND)
        self.assertEqual(result[1], 14)
    
    def test_classify_straight_flush(self):
        """【測試15】分類順子同花：梅花 3-4-5-6-7"""
        cards = Hand([Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)])
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.STRAIGHT_FLUSH)
        self.assertEqual(result[1], 7)


class TestComparison(unittest.TestCase):
    """牌型比較測試"""
    
    def test_compare_single_rank(self):
        """【測試16】單張比較：A > K"""
        cls1 = (CardType.SINGLE, 14, 3)  # ♠A
        cls2 = (CardType.SINGLE, 13, 3)  # ♠K
        result = HandClassifier.compare(cls1, cls2)
        self.assertEqual(result, 1)
    
    def test_compare_single_suit(self):
        """【測試17】同等級單張比較：♠ > ♥"""
        cls1 = (CardType.SINGLE, 14, 3)  # ♠A
        cls2 = (CardType.SINGLE, 14, 2)  # ♥A
        result = HandClassifier.compare(cls1, cls2)
        self.assertEqual(result, 1)
    
    def test_compare_pair_rank(self):
        """【測試18】對子比較：對A > 對K"""
        cls1 = (CardType.PAIR, 14, 0)  # 對A
        cls2 = (CardType.PAIR, 13, 0)  # 對K
        result = HandClassifier.compare(cls1, cls2)
        self.assertEqual(result, 1)
    
    def test_compare_pair_suit(self):
        """【測試19】同等級對子比較：♠♥A > ♦♣A"""
        cls1 = (CardType.PAIR, 14, 3)  # ♠A
        cls2 = (CardType.PAIR, 14, 1)  # ♦A
        result = HandClassifier.compare(cls1, cls2)
        self.assertEqual(result, 1)
    
    def test_compare_different_type(self):
        """【測試20】不同牌型比較：對子 > 單張"""
        cls1 = (CardType.PAIR, 3, 0)      # 對3
        cls2 = (CardType.SINGLE, 14, 3)   # 單A
        result = HandClassifier.compare(cls1, cls2)
        self.assertEqual(result, 1)
    
    def test_compare_flush_vs_straight(self):
        """【測試21】同花 > 順子"""
        cls1 = (CardType.FLUSH, 7, 0)
        cls2 = (CardType.STRAIGHT, 14, 0)
        result = HandClassifier.compare(cls1, cls2)
        self.assertEqual(result, 1)


class TestCanPlay(unittest.TestCase):
    """合法性檢查測試"""
    
    def test_can_play_first_3clubs(self):
        """【測試22】首手必須梅花3：可以出"""
        cards = Hand([Card(3, 0)])  # ♣3
        result = HandClassifier.can_play(None, cards)
        self.assertTrue(result)
    
    def test_can_play_first_not_3clubs(self):
        """【測試23】首手非梅花3：不能出"""
        cards = Hand([Card(14, 3)])  # ♠A
        result = HandClassifier.can_play(None, cards)
        self.assertFalse(result)
    
    def test_can_play_same_type(self):
        """【測試24】出牌類型相同但更大：可以出"""
        last = (CardType.PAIR, 5, 0)  # 對5
        cards = Hand([Card(6, 3), Card(6, 2)])  # 對6
        result = HandClassifier.can_play(last, cards)
        self.assertTrue(result)
    
    def test_can_play_diff_type(self):
        """【測試25】出牌類型不同：不能出"""
        last = (CardType.PAIR, 5, 0)  # 對5
        cards = Hand([Card(6, 0)])    # 單6
        result = HandClassifier.can_play(last, cards)
        self.assertFalse(result)
    
    def test_can_play_not_stronger(self):
        """【測試26】出牌不夠大：不能出"""
        last = (CardType.PAIR, 10, 0)  # 對10
        cards = Hand([Card(5, 3), Card(5, 2)])  # 對5
        result = HandClassifier.can_play(last, cards)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
