"""Phase 1: Data models tests."""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.models import Card, Deck, Hand, Player


class TestCard(unittest.TestCase):
    """Card 類別測試。"""

    def test_card_creation(self):
        """測試牌的建立。"""
        card = Card(rank=14, suit=3)
        self.assertEqual(card.rank, 14)
        self.assertEqual(card.suit, 3)

    def test_card_repr_ace(self):
        """測試 A♠ 的字串表示。"""
        card = Card(14, 3)
        self.assertEqual(repr(card), "♠A")

    def test_card_repr_three(self):
        """測試 3♣ 的字串表示。"""
        card = Card(3, 0)
        self.assertEqual(repr(card), "♣3")

    def test_card_compare_suit(self):
        """測試花色比較。"""
        card_spade = Card(14, 3)
        card_heart = Card(14, 2)
        self.assertGreater(card_spade, card_heart)

    def test_card_compare_rank(self):
        """測試數字比較。"""
        card_2 = Card(15, 0)
        card_a = Card(14, 3)
        self.assertGreater(card_2, card_a)

    def test_card_hash(self):
        """測試雜湊值。"""
        card1 = Card(14, 3)
        card2 = Card(14, 3)
        self.assertEqual(hash(card1), hash(card2))


class TestDeck(unittest.TestCase):
    """Deck 類別測試。"""

    def test_deck_has_52_cards(self):
        """測試牌堆有 52 張牌。"""
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_all_unique(self):
        """測試所有牌都不同。"""
        deck = Deck()
        self.assertEqual(len(set(deck.cards)), 52)

    def test_deal_cards(self):
        """測試發牌。"""
        deck = Deck()
        cards = deck.deal(5)
        self.assertEqual(len(cards), 5)
        self.assertEqual(len(deck.cards), 47)


class TestHand(unittest.TestCase):
    """Hand 類別測試。"""

    def test_hand_creation(self):
        """測試手牌建立。"""
        cards = [Card(14, 3), Card(13, 3), Card(3, 0)]
        hand = Hand(cards)
        self.assertEqual(len(hand), 3)

    def test_hand_find_3_clubs(self):
        """測試尋找 3♣。"""
        cards = [Card(14, 3), Card(3, 0)]
        hand = Hand(cards)
        found = hand.find_3_clubs()
        self.assertIsNotNone(found)
        self.assertEqual(found.rank, 3)
        self.assertEqual(found.suit, 0)

    def test_hand_remove(self):
        """測試移除牌。"""
        cards = [Card(14, 3), Card(13, 3), Card(3, 0)]
        hand = Hand(cards)
        to_remove = [Card(14, 3)]
        hand.remove(to_remove)
        self.assertEqual(len(hand), 2)


class TestPlayer(unittest.TestCase):
    """Player 類別測試。"""

    def test_player_creation(self):
        """測試玩家建立。"""
        player = Player("Test", is_ai=False)
        self.assertEqual(player.name, "Test")
        self.assertFalse(player.is_ai)

    def test_player_take_cards(self):
        """測試玩家拿牌。"""
        player = Player("Test")
        cards = [Card(14, 3), Card(13, 3)]
        player.take_cards(cards)
        self.assertEqual(len(player.hand), 2)


if __name__ == '__main__':
    unittest.main()
