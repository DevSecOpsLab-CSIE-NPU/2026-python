# -*- coding: utf-8 -*-
"""
大二紙牌遊戲 - Phase 3 牌型搜尋單元測試

針對 HandFinder 類別的完整測試套件
使用 Python 標準函式庫 unittest
"""

import unittest
from typing import List, Optional, Tuple
from p1_models import Card, Hand
from p2_classifier import CardType, HandClassifier


# ============================================================================
# 【牌型搜尋器類別】（供測試調用）
# ============================================================================

class HandFinder:
    """
    牌型搜尋器
    
    根據手牌，搜尋所有可能的牌型組合
    """
    
    @staticmethod
    def find_singles(hand: Hand) -> List[Hand]:
        """
        搜尋所有可能的單張組合
        
        Args:
            hand: 玩家手牌
            
        Returns:
            單張組合清單，每個組合是包含單張的 Hand 物件
        """
        if not hand:
            return []
        
        singles = []
        for card in hand:
            singles.append(Hand([card]))
        return singles
    
    @staticmethod
    def find_pairs(hand: Hand) -> List[Hand]:
        """
        搜尋所有可能的對子組合
        
        Args:
            hand: 玩家手牌
            
        Returns:
            對子組合清單，每個組合是包含對子的 Hand 物件
        """
        if not hand or len(hand) < 2:
            return []
        
        # 記錄每個等級的牌
        rank_to_cards = {}
        for card in hand:
            if card.rank not in rank_to_cards:
                rank_to_cards[card.rank] = []
            rank_to_cards[card.rank].append(card)
        
        pairs = []
        # 對於每個等級，如果有 2 張以上，就取任意 2 張
        for rank, cards in rank_to_cards.items():
            if len(cards) >= 2:
                # 取前 2 張組成對子
                pair = Hand([cards[0], cards[1]])
                pairs.append(pair)
                # 如果有 3 張或 4 張，還可以組成其他對子組合
                if len(cards) >= 3:
                    for i in range(2, len(cards)):
                        pair = Hand([cards[0], cards[i]])
                        pairs.append(pair)
                if len(cards) >= 4:
                    pair = Hand([cards[1], cards[2]])
                    pairs.append(pair)
                    pair = Hand([cards[1], cards[3]])
                    pairs.append(pair)
                    pair = Hand([cards[2], cards[3]])
                    pairs.append(pair)
        
        # 去重並回傳
        seen = set()
        unique_pairs = []
        for pair in pairs:
            key = tuple(sorted([(c.rank, c.suit) for c in pair]))
            if key not in seen:
                seen.add(key)
                unique_pairs.append(pair)
        
        return unique_pairs
    
    @staticmethod
    def find_triples(hand: Hand) -> List[Hand]:
        """
        搜尋所有可能的三條組合
        
        Args:
            hand: 玩家手牌
            
        Returns:
            三條組合清單，每個組合是包含三條的 Hand 物件
        """
        if not hand or len(hand) < 3:
            return []
        
        # 記錄每個等級的牌
        rank_to_cards = {}
        for card in hand:
            if card.rank not in rank_to_cards:
                rank_to_cards[card.rank] = []
            rank_to_cards[card.rank].append(card)
        
        triples = []
        # 對於每個等級，如果有 3 張以上，就取任意 3 張
        for rank, cards in rank_to_cards.items():
            if len(cards) >= 3:
                # 取前 3 張組成三條
                triple = Hand(cards[:3])
                triples.append(triple)
                # 如果有 4 張，還可以其他結合
                if len(cards) >= 4:
                    triple = Hand([cards[0], cards[1], cards[3]])
                    triples.append(triple)
                    triple = Hand([cards[0], cards[2], cards[3]])
                    triples.append(triple)
                    triple = Hand([cards[1], cards[2], cards[3]])
                    triples.append(triple)
        
        # 去重並回傳
        seen = set()
        unique_triples = []
        for triple in triples:
            key = tuple(sorted([(c.rank, c.suit) for c in triple]))
            if key not in seen:
                seen.add(key)
                unique_triples.append(triple)
        
        return unique_triples
    
    @staticmethod
    def find_five_card_combinations(hand: Hand) -> List[Hand]:
        """
        搜尋所有可能的五張牌組合
        
        利用組合學列舉所有可能的 5 張牌組合
        
        Args:
            hand: 玩家手牌
            
        Returns:
            五張牌組合清單，每個組合是 Hand 物件
        """
        if not hand or len(hand) < 5:
            return []
        
        from itertools import combinations as iter_combinations
        cards = list(hand)
        result_combos = []
        
        # 生成所有 5 張牌的組合 (C(n, 5))
        for combo in iter_combinations(cards, 5):
            result_combos.append(Hand(list(combo)))
        
        return result_combos
    
    @staticmethod
    def find_straights(hand: Hand) -> List[Hand]:
        """
        搜尋所有可能的順子
        
        Args:
            hand: 玩家手牌
            
        Returns:
            順子組合清單
        """
        five_combos = HandFinder.find_five_card_combinations(hand)
        straights = []
        
        for combo in five_combos:
            classification = HandClassifier.classify(list(combo))
            if classification and classification[0] == CardType.STRAIGHT:
                straights.append(combo)
        
        return straights
    
    @staticmethod
    def find_flushes(hand: Hand) -> List[Hand]:
        """
        搜尋所有可能的同花
        
        Args:
            hand: 玩家手牌
            
        Returns:
            同花組合清單
        """
        five_combos = HandFinder.find_five_card_combinations(hand)
        flushes = []
        
        for combo in five_combos:
            classification = HandClassifier.classify(list(combo))
            if classification and classification[0] == CardType.FLUSH:
                flushes.append(combo)
        
        return flushes
    
    @staticmethod
    def find_full_houses(hand: Hand) -> List[Hand]:
        """
        搜尋所有可能的滿堂紅（三條 + 對子）
        
        Args:
            hand: 玩家手牌
            
        Returns:
            滿堂紅組合清單
        """
        five_combos = HandFinder.find_five_card_combinations(hand)
        full_houses = []
        
        for combo in five_combos:
            classification = HandClassifier.classify(list(combo))
            if classification and classification[0] == CardType.FULL_HOUSE:
                full_houses.append(combo)
        
        return full_houses
    
    @staticmethod
    def find_four_of_a_kinds(hand: Hand) -> List[Hand]:
        """
        搜尋所有可能的四條
        
        Args:
            hand: 玩家手牌
            
        Returns:
            四條組合清單
        """
        five_combos = HandFinder.find_five_card_combinations(hand)
        four_kinds = []
        
        for combo in five_combos:
            classification = HandClassifier.classify(list(combo))
            if classification and classification[0] == CardType.FOUR_OF_A_KIND:
                four_kinds.append(combo)
        
        return four_kinds
    
    @staticmethod
    def find_straight_flushes(hand: Hand) -> List[Hand]:
        """
        搜尋所有可能的順子同花
        
        Args:
            hand: 玩家手牌
            
        Returns:
            順子同花組合清單
        """
        five_combos = HandFinder.find_five_card_combinations(hand)
        straight_flushes = []
        
        for combo in five_combos:
            classification = HandClassifier.classify(list(combo))
            if classification and classification[0] == CardType.STRAIGHT_FLUSH:
                straight_flushes.append(combo)
        
        return straight_flushes
    
    @staticmethod
    def find_valid_plays(hand: Hand, 
                        last_classification: Optional[Tuple[CardType, int, int]] = None) -> List[Hand]:
        """
        搜尋所有合法的出牌組合
        
        依據上一手的牌型，搜尋所有能夠大於上家的牌型
        
        Args:
            hand: 玩家手牌
            last_classification: 上一手的牌型分類，None 表示首手
            
        Returns:
            所有合法出牌組合清單
        """
        if last_classification is None:
            # 首手：必須包含梅花 3
            for card in hand:
                if card.rank == 3 and card.suit == 0:
                    return [Hand([card])]
            return []
        
        # 非首手：根據上手的牌型，搜尋能打大過的牌
        last_type = last_classification[0]
        valid_plays = []
        
        if last_type == CardType.SINGLE:
            # 上家單張，搜尋所有可能的單張
            for single in HandFinder.find_singles(hand):
                classification = HandClassifier.classify(list(single))
                if classification and HandClassifier.compare(classification, last_classification) > 0:
                    valid_plays.append(single)
        
        elif last_type == CardType.PAIR:
            # 上家對子，搜尋所有可能的對子
            for pair in HandFinder.find_pairs(hand):
                classification = HandClassifier.classify(list(pair))
                if classification and HandClassifier.compare(classification, last_classification) > 0:
                    valid_plays.append(pair)
        
        elif last_type == CardType.TRIPLE:
            # 上家三條，搜尋所有可能的三條
            for triple in HandFinder.find_triples(hand):
                classification = HandClassifier.classify(list(triple))
                if classification and HandClassifier.compare(classification, last_classification) > 0:
                    valid_plays.append(triple)
        
        elif last_type == CardType.STRAIGHT:
            # 上家順子，搜尋順子、同花、滿堂紅、四條、順子同花
            searches = [
                HandFinder.find_straights(hand),
                HandFinder.find_flushes(hand),
                HandFinder.find_full_houses(hand),
                HandFinder.find_four_of_a_kinds(hand),
                HandFinder.find_straight_flushes(hand)
            ]
            for combos in searches:
                for combo in combos:
                    classification = HandClassifier.classify(list(combo))
                    if classification and HandClassifier.compare(classification, last_classification) > 0:
                        valid_plays.append(combo)
        
        elif last_type == CardType.FLUSH:
            # 上家同花，搜尋同花和更強的牌型
            searches = [
                HandFinder.find_flushes(hand),
                HandFinder.find_full_houses(hand),
                HandFinder.find_four_of_a_kinds(hand),
                HandFinder.find_straight_flushes(hand)
            ]
            for combos in searches:
                for combo in combos:
                    classification = HandClassifier.classify(list(combo))
                    if classification and HandClassifier.compare(classification, last_classification) > 0:
                        valid_plays.append(combo)
        
        elif last_type == CardType.FULL_HOUSE:
            # 上家滿堂紅，搜尋滿堂紅和更強的牌型
            searches = [
                HandFinder.find_full_houses(hand),
                HandFinder.find_four_of_a_kinds(hand),
                HandFinder.find_straight_flushes(hand)
            ]
            for combos in searches:
                for combo in combos:
                    classification = HandClassifier.classify(list(combo))
                    if classification and HandClassifier.compare(classification, last_classification) > 0:
                        valid_plays.append(combo)
        
        elif last_type == CardType.FOUR_OF_A_KIND:
            # 上家四條，搜尋四條和順子同花
            searches = [
                HandFinder.find_four_of_a_kinds(hand),
                HandFinder.find_straight_flushes(hand)
            ]
            for combos in searches:
                for combo in combos:
                    classification = HandClassifier.classify(list(combo))
                    if classification and HandClassifier.compare(classification, last_classification) > 0:
                        valid_plays.append(combo)
        
        elif last_type == CardType.STRAIGHT_FLUSH:
            # 上家順子同花，只能用更大的順子同花
            for combo in HandFinder.find_straight_flushes(hand):
                classification = HandClassifier.classify(list(combo))
                if classification and HandClassifier.compare(classification, last_classification) > 0:
                    valid_plays.append(combo)
        
        # 去重
        seen = set()
        unique_plays = []
        for play in valid_plays:
            key = tuple(sorted([(c.rank, c.suit) for c in play]))
            if key not in seen:
                seen.add(key)
                unique_plays.append(play)
        
        return unique_plays


# ============================================================================
# 【單元測試】
# ============================================================================


class TestSinglesFinder(unittest.TestCase):
    """單張搜尋測試"""
    
    def test_find_singles(self):
        """【測試1】搜尋單張：3張牌回傳3個單張"""
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])  # ♠A, ♥K, ♣3
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 3)
        self.assertTrue(all(len(s) == 1 for s in singles))
    
    def test_find_singles_empty(self):
        """【測試2】空手牌搜尋單張：回傳空清單"""
        hand = Hand([])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 0)


class TestPairsFinder(unittest.TestCase):
    """對子搜尋測試"""
    
    def test_find_pairs_one(self):
        """【測試3】搜尋對子：1組對子"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])  # ♠A, ♥A, ♣3
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 1)
        self.assertTrue(all(len(p) == 2 for p in pairs))
    
    def test_find_pairs_two(self):
        """【測試4】搜尋多組對子：2組對子"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(13, 3), Card(13, 0)])  # ♠A, ♥A, ♠K, ♣K
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 2)
    
    def test_find_pairs_none(self):
        """【測試5】無對子：回傳空清單"""
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])  # ♠A, ♥K, ♣3
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 0)


class TestTriplesFinder(unittest.TestCase):
    """三條搜尋測試"""
    
    def test_find_triples_one(self):
        """【測試6】搜尋三條：1組三條"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0)])  # ♠A, ♥A, ♦A, ♣3
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 1)
        self.assertTrue(all(len(t) == 3 for t in triples))
    
    def test_find_triples_with_extra(self):
        """【測試7】有額外牌的三條搜尋"""
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 3), Card(13, 2)])
        triples = HandFinder.find_triples(hand)
        # [A, A, A] 三條 + [K, K] 對子
        self.assertEqual(len(triples), 1)


class TestFiveCardFinder(unittest.TestCase):
    """五張牌型搜尋測試"""
    
    def test_find_straight(self):
        """【測試8】搜尋順子"""
        hand = Hand([
            Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0),
            Card(14, 3)
        ])
        straights = HandFinder.find_straights(hand)
        self.assertGreater(len(straights), 0)
    
    def test_find_flush(self):
        """【測試9】搜尋同花"""
        hand = Hand([
            Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0),
            Card(14, 3)
        ])
        flushes = HandFinder.find_flushes(hand)
        self.assertGreater(len(flushes), 0)
    
    def test_find_full_house(self):
        """【測試10】搜尋滿堂紅"""
        hand = Hand([
            Card(14, 3), Card(14, 2), Card(14, 1), Card(2, 0), Card(2, 1),
            Card(5, 3)
        ])
        full_houses = HandFinder.find_full_houses(hand)
        self.assertGreater(len(full_houses), 0)
    
    def test_find_four_of_a_kind(self):
        """【測試11】搜尋四條"""
        hand = Hand([
            Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 0),
            Card(5, 3)
        ])
        four_kinds = HandFinder.find_four_of_a_kinds(hand)
        self.assertGreater(len(four_kinds), 0)
    
    def test_find_straight_flush(self):
        """【測試12】搜尋順子同花"""
        hand = Hand([
            Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0),
            Card(14, 3)
        ])
        straight_flushes = HandFinder.find_straight_flushes(hand)
        self.assertGreater(len(straight_flushes), 0)


class TestValidPlays(unittest.TestCase):
    """合法出牌搜尋測試"""
    
    def test_first_turn_with_3_clubs(self):
        """【測試13】首手有梅花3：只能出梅花3"""
        hand = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
        valid_plays = HandFinder.find_valid_plays(hand, last_classification=None)
        self.assertEqual(len(valid_plays), 1)
        self.assertEqual(valid_plays[0][0].rank, 3)
        self.assertEqual(valid_plays[0][0].suit, 0)
    
    def test_first_turn_without_3_clubs(self):
        """【測試14】首手無梅花3：無法出牌"""
        hand = Hand([Card(14, 3), Card(13, 2), Card(12, 1)])
        valid_plays = HandFinder.find_valid_plays(hand, last_classification=None)
        self.assertEqual(len(valid_plays), 0)
    
    def test_with_last_single(self):
        """【測試15】上家單張：搜尋可靠的單張"""
        last = (CardType.SINGLE, 5, 0)  # 單 5
        hand = Hand([Card(6, 0), Card(7, 1), Card(3, 0)])
        valid_plays = HandFinder.find_valid_plays(hand, last)
        # 應該只有 1 個單張 6 可以出
        self.assertGreater(len(valid_plays), 0)
        self.assertTrue(all(len(p) == 1 for p in valid_plays))
    
    def test_with_last_pair(self):
        """【測試16】上家對子：搜尋可打的對子"""
        last = (CardType.PAIR, 5, 0)  # 對 5
        hand = Hand([Card(6, 0), Card(6, 1), Card(3, 0), Card(3, 1)])
        valid_plays = HandFinder.find_valid_plays(hand, last)
        # 應該有可以出的對子
        self.assertTrue(all(len(p) == 2 for p in valid_plays))
    
    def test_no_valid_plays(self):
        """【測試17】無法大於上家：回傳空清單"""
        last = (CardType.SINGLE, 2, 0)  # ♣2 最大單張
        hand = Hand([Card(14, 3), Card(13, 2), Card(12, 1)])  # A, K, Q 都小於 2
        valid_plays = HandFinder.find_valid_plays(hand, last)
        self.assertEqual(len(valid_plays), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
