# -*- coding: utf-8 -*-
"""
大二紙牌遊戲 - Phase 1 資料模型單元測試

針對 Card、Deck、Hand、Player 類別的完整測試套件
使用 Python 標準函式庫 unittest
"""

import unittest
from p1_models import Card, Deck, Hand, Player


# ============================================================================
# 【單元測試】
# ============================================================================


class TestCardCreation(unittest.TestCase):
    """Card 類別建立與基本屬性測試"""
    
    def test_card_creation(self):
        """【測試1】Card 初始化成功"""
        card = Card(rank=14, suit=3)
        self.assertEqual(card.rank, 14)
        self.assertEqual(card.suit, 3)


class TestCardRepr(unittest.TestCase):
    """Card 字串表示測試"""
    
    def test_card_repr_ace(self):
        """【測試2】黑桃A（♠A）"""
        card = Card(14, 3)
        self.assertEqual(repr(card), "♠A")
    
    def test_card_repr_three(self):
        """【測試3】梅花3（♣3）"""
        card = Card(3, 0)
        self.assertEqual(repr(card), "♣3")


class TestCardComparison(unittest.TestCase):
    """Card 比較測試（大小判定）"""
    
    def test_card_compare_suit(self):
        """【測試4】相同等級，花色 ♠ > ♥"""
        card1 = Card(14, 3)  # ♠A
        card2 = Card(14, 2)  # ♥A
        self.assertTrue(card1 > card2)
    
    def test_card_compare_suit_2(self):
        """【測試5】相同等級，花色 ♥ > ♦"""
        card1 = Card(14, 2)  # ♥A
        card2 = Card(14, 1)  # ♦A
        self.assertTrue(card1 > card2)
    
    def test_card_compare_suit_3(self):
        """【測試6】相同等級，花色 ♦ > ♣"""
        card1 = Card(14, 1)  # ♦A
        card2 = Card(14, 0)  # ♣A
        self.assertTrue(card1 > card2)
    
    def test_card_compare_rank_2(self):
        """【測試7】2 > A（等級2 > 等級14）"""
        card1 = Card(2, 0)   # ♣2
        card2 = Card(14, 3)  # ♠A
        self.assertTrue(card1 > card2)
    
    def test_card_compare_rank_a(self):
        """【測試8】A > K（等級14 > 等級13）"""
        card1 = Card(14, 0)  # ♣A
        card2 = Card(13, 3)  # ♠K
        self.assertTrue(card1 > card2)
    
    def test_card_compare_equal(self):
        """【測試9】相同牌不大於自己"""
        card1 = Card(14, 3)  # ♠A
        card2 = Card(14, 3)  # ♠A
        self.assertFalse(card1 > card2)


class TestCardSortKey(unittest.TestCase):
    """Card 排序鍵測試"""
    
    def test_card_sort_key(self):
        """【測試10】排序鍵為 (rank, suit) tuple"""
        card = Card(14, 3)
        self.assertEqual(card.to_sort_key(), (14, 3))


class TestDeckCreation(unittest.TestCase):
    """Deck 類別初始化測試"""
    
    def test_deck_has_52_cards(self):
        """【測試11】牌堆初始化有52張牌"""
        deck = Deck()
        self.assertEqual(len(deck), 52)
    
    def test_deck_all_unique(self):
        """【測試12】52張牌全部不重複"""
        deck = Deck()
        cards_set = set(deck.cards)
        self.assertEqual(len(cards_set), 52)
    
    def test_deck_all_ranks(self):
        """【測試13】包含等級 2-14 所有牌"""
        deck = Deck()
        ranks = {card.rank for card in deck.cards}
        self.assertEqual(ranks, set(range(2, 15)))
    
    def test_deck_all_suits(self):
        """【測試14】包含花色 0-3 所有花色"""
        deck = Deck()
        suits = {card.suit for card in deck.cards}
        self.assertEqual(suits, {0, 1, 2, 3})


class TestDeckOperations(unittest.TestCase):
    """Deck 操作測試（洗牌、發牌）"""
    
    def test_deck_shuffle(self):
        """【測試15】洗牌後牌序改變"""
        deck = Deck()
        original_order = [card.to_sort_key() for card in deck.cards]
        deck.shuffle()
        shuffled_order = [card.to_sort_key() for card in deck.cards]
        # 洗牌後順序極可能不同（機率 1 - 1/52! 接近 1）
        self.assertNotEqual(original_order, shuffled_order)
    
    def test_deal_5_cards(self):
        """【測試16】發5張後，發出5張、剩47張"""
        deck = Deck()
        dealt = deck.deal(5)
        self.assertEqual(len(dealt), 5)
        self.assertEqual(len(deck), 47)
    
    def test_deal_multiple(self):
        """【測試17】連續發牌：先發5張，再發3張，剩44張"""
        deck = Deck()
        deck.deal(5)
        deck.deal(3)
        self.assertEqual(len(deck), 44)
    
    def test_deal_exceed(self):
        """【測試18】發牌超出剩餘數：發60張但只有52張，全部發出"""
        deck = Deck()
        dealt = deck.deal(60)
        self.assertEqual(len(dealt), 52)
        self.assertEqual(len(deck), 0)


class TestHandCreation(unittest.TestCase):
    """Hand 類別初始化測試"""
    
    def test_hand_creation(self):
        """【測試19】Hand 初始化成功"""
        cards = [Card(3, 0), Card(5, 1), Card(14, 3)]
        hand = Hand(cards)
        self.assertEqual(len(hand), 3)


class TestHandOperations(unittest.TestCase):
    """Hand 操作測試（排序、查詢、移除）"""
    
    def test_hand_sort_desc(self):
        """【測試20】手牌排序：由大到小（♠A > ♥K > ♠3 > ♣3）"""
        cards = [
            Card(3, 0),   # ♣3
            Card(14, 3),  # ♠A
            Card(3, 3),   # ♠3
            Card(13, 2),  # ♥K
        ]
        hand = Hand(cards)
        hand.sort_desc()
        
        expected_order = [
            Card(14, 3),  # ♠A
            Card(13, 2),  # ♥K
            Card(3, 3),   # ♠3
            Card(3, 0),   # ♣3
        ]
        
        for i, card in enumerate(hand):
            self.assertEqual(card, expected_order[i])
    
    def test_hand_find_3_clubs(self):
        """【測試21】尋找梅花3，找到回傳"""
        cards = [Card(14, 3), Card(3, 0), Card(3, 1)]
        hand = Hand(cards)
        found = hand.find_3_clubs()
        self.assertIsNotNone(found)
        self.assertEqual(found.rank, 3)
        self.assertEqual(found.suit, 0)
    
    def test_hand_find_3_clubs_none(self):
        """【測試22】尋找3但沒有，回傳 None"""
        cards = [Card(14, 3), Card(3, 1)]
        hand = Hand(cards)
        found = hand.find_3_clubs()
        self.assertIsNone(found)
    
    def test_hand_remove(self):
        """【測試23】移除指定牌，成功減少"""
        cards = [Card(14, 3), Card(3, 0)]
        hand = Hand(cards)
        card_to_remove = hand[0]
        success = hand.remove_card(card_to_remove)
        
        self.assertTrue(success)
        self.assertEqual(len(hand), 1)
    
    def test_hand_remove_not_found(self):
        """【測試24】移除不存在牌，數量不變"""
        cards = [Card(14, 3), Card(3, 0)]
        hand = Hand(cards)
        non_existent = Card(5, 2)
        success = hand.remove_card(non_existent)
        
        self.assertFalse(success)
        self.assertEqual(len(hand), 2)
    
    def test_hand_iteration(self):
        """【測試25】支持迭代，list(hand) 相同"""
        cards = [Card(14, 3), Card(3, 0)]
        hand = Hand(cards)
        hand_list = list(hand)
        self.assertEqual(len(hand_list), 2)


class TestPlayerCreation(unittest.TestCase):
    """Player 類別初始化測試"""
    
    def test_player_human(self):
        """【測試26】建立人類玩家"""
        player = Player("Player1", False)
        self.assertEqual(player.name, "Player1")
        self.assertFalse(player.is_ai)
    
    def test_player_ai(self):
        """【測試27】建立 AI 玩家"""
        player = Player("AI_1", True)
        self.assertEqual(player.name, "AI_1")
        self.assertTrue(player.is_ai)


class TestPlayerOperations(unittest.TestCase):
    """Player 操作測試（收牌、出牌）"""
    
    def test_player_take(self):
        """【測試28】收牌：收2張後手牌為2張"""
        player = Player("Player1")
        cards = [Card(14, 3), Card(3, 0)]
        player.take_cards(cards)
        self.assertEqual(len(player.hand), 2)
    
    def test_player_play(self):
        """【測試29】出牌：出牌成功後手牌減少"""
        player = Player("Player1")
        cards = [Card(14, 3), Card(3, 0)]
        player.take_cards(cards)
        
        card_to_play = cards[0]
        result = player.play_card(card_to_play)
        
        self.assertEqual(result, card_to_play)
        self.assertEqual(len(player.hand), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
