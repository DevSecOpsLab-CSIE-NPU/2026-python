"""
Phase 1 Tests: 資料模型測試
Card, Deck, Hand, Player 類別的單元測試
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from game.models import Card, Deck, Hand, Player


class TestCard(unittest.TestCase):
    """Card 類別測試"""
    
    def test_card_creation(self):
        """測試牌的建立"""
        card = Card(14, 3)
        self.assertEqual(card.rank, 14)
        self.assertEqual(card.suit, 3)
    
    def test_card_repr_ace(self):
        """測試 A♠ 的表示"""
        card = Card(14, 3)
        self.assertEqual(repr(card), "♠A")
    
    def test_card_repr_three(self):
        """測試 ♣3 的表示"""
        card = Card(3, 0)
        self.assertEqual(repr(card), "♣3")
    
    def test_card_compare_suit(self):
        """測試花色比較"""
        card1 = Card(14, 3)  # ♠A
        card2 = Card(14, 2)  # ♥A
        self.assertGreater(card1, card2)
    
    def test_card_compare_rank(self):
        """測試數字比較"""
        card1 = Card(14, 0)  # ♣A
        card2 = Card(13, 3)  # ♠K
        self.assertGreater(card1, card2)
    
    def test_card_equal(self):
        """測試牌相等"""
        card1 = Card(14, 3)
        card2 = Card(14, 3)
        self.assertEqual(card1, card2)
    
    def test_card_hash(self):
        """測試牌的雜湊值"""
        card1 = Card(14, 3)
        card2 = Card(14, 3)
        self.assertEqual(hash(card1), hash(card2))


class TestDeck(unittest.TestCase):
    """Deck 類別測試"""
    
    def test_deck_has_52_cards(self):
        """測試牌堆有52張"""
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
    
    def test_deck_all_unique(self):
        """測試牌堆中所有牌都是唯一的"""
        deck = Deck()
        self.assertEqual(len(set(deck.cards)), 52)
    
    def test_deck_all_ranks(self):
        """測試牌堆有所有rank"""
        deck = Deck()
        ranks = {card.rank for card in deck.cards}
        self.assertEqual(ranks, set(range(3, 16)))
    
    def test_deck_all_suits(self):
        """測試牌堆有所有suit"""
        deck = Deck()
        suits = {card.suit for card in deck.cards}
        self.assertEqual(suits, {0, 1, 2, 3})
    
    def test_deck_deal_5_cards(self):
        """測試發5張牌"""
        deck = Deck()
        cards = deck.deal(5)
        self.assertEqual(len(cards), 5)
        self.assertEqual(len(deck.cards), 47)
    
    def test_deck_deal_multiple(self):
        """測試多次發牌"""
        deck = Deck()
        deck.deal(5)
        deck.deal(3)
        self.assertEqual(len(deck.cards), 44)
    
    def test_deck_shuffle(self):
        """測試洗牌"""
        deck1 = Deck()
        cards_before = deck1.cards.copy()
        deck1.shuffle()
        # 洗牌後順序應該改變（理論上）
        # 我們只檢查牌的數量沒變
        self.assertEqual(len(deck1.cards), 52)


class TestHand(unittest.TestCase):
    """Hand 類別測試"""
    
    def test_hand_creation(self):
        """測試手牌建立"""
        cards = [Card(14, 3), Card(13, 2), Card(12, 1)]
        hand = Hand(cards)
        self.assertEqual(len(hand), 3)
    
    def test_hand_find_3_clubs(self):
        """測試找3♣"""
        cards = [Card(14, 3), Card(3, 0), Card(12, 1)]
        hand = Hand(cards)
        three_clubs = hand.find_3_clubs()
        self.assertIsNotNone(three_clubs)
        self.assertEqual(three_clubs.rank, 3)
        self.assertEqual(three_clubs.suit, 0)
    
    def test_hand_find_3_clubs_not_found(self):
        """測試找不到3♣"""
        cards = [Card(14, 3), Card(13, 2), Card(12, 1)]
        hand = Hand(cards)
        three_clubs = hand.find_3_clubs()
        self.assertIsNone(three_clubs)
    
    def test_hand_sort_desc(self):
        """測試手牌排序"""
        cards = [Card(3, 0), Card(14, 3), Card(13, 2)]
        hand = Hand(cards)
        hand.sort_desc()
        self.assertEqual(hand[0].rank, 14)
        self.assertEqual(hand[2].rank, 3)
    
    def test_hand_remove_cards(self):
        """測試移除牌"""
        cards = [Card(14, 3), Card(13, 2), Card(12, 1)]
        hand = Hand(cards)
        hand.remove_cards([cards[0]])
        self.assertEqual(len(hand), 2)


class TestPlayer(unittest.TestCase):
    """Player 類別測試"""
    
    def test_player_human(self):
        """測試人類玩家建立"""
        player = Player("Player 1", is_ai=False)
        self.assertEqual(player.name, "Player 1")
        self.assertFalse(player.is_ai)
    
    def test_player_ai(self):
        """測試 AI 玩家建立"""
        player = Player("AI 1", is_ai=True)
        self.assertEqual(player.name, "AI 1")
        self.assertTrue(player.is_ai)
    
    def test_player_take_cards(self):
        """測試玩家拿牌"""
        player = Player("Player 1")
        cards = [Card(14, 3), Card(13, 2)]
        player.take_cards(cards)
        self.assertEqual(len(player.hand), 2)
    
    def test_player_play_cards(self):
        """測試玩家出牌"""
        player = Player("Player 1")
        cards = [Card(14, 3), Card(13, 2), Card(12, 1)]
        player.take_cards(cards)
        
        played = player.play_cards([cards[0]])
        self.assertEqual(len(played), 1)
        self.assertEqual(len(player.hand), 2)


if __name__ == '__main__':
    unittest.main()
