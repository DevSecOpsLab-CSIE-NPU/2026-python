"""
models 模組測試。
"""

from __future__ import annotations

import unittest

from game.models import Card, Deck, Hand, Player


class TestCard(unittest.TestCase):
    """Card 資料模型測試。"""

    def test_card_creation(self) -> None:
        card = Card(rank=14, suit=3)
        self.assertEqual(card.rank, 14)
        self.assertEqual(card.suit, 3)

    def test_card_repr_ace_of_spades(self) -> None:
        self.assertEqual(repr(Card(14, 3)), "AS")

    def test_card_compare_suit(self) -> None:
        self.assertGreater(Card(14, 3), Card(14, 2))
        self.assertGreater(Card(14, 2), Card(14, 1))
        self.assertGreater(Card(14, 1), Card(14, 0))

    def test_card_compare_rank(self) -> None:
        self.assertGreater(Card(15, 0), Card(14, 3))
        self.assertGreater(Card(14, 0), Card(13, 3))

    def test_card_sort_key(self) -> None:
        self.assertEqual(Card(14, 3).to_sort_key(), (14, 3))


class TestDeck(unittest.TestCase):
    """Deck 相關測試。"""

    def test_deck_has_52_unique_cards(self) -> None:
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        self.assertEqual(len(set(deck.cards)), 52)

    def test_deck_contains_all_ranks_and_suits(self) -> None:
        deck = Deck()
        ranks = {card.rank for card in deck.cards}
        suits = {card.suit for card in deck.cards}
        self.assertEqual(ranks, set(range(3, 16)))
        self.assertEqual(suits, {0, 1, 2, 3})

    def test_deal_cards_reduces_deck(self) -> None:
        deck = Deck(shuffle_on_init=False)
        hand = deck.deal(5)
        self.assertEqual(len(hand), 5)
        self.assertEqual(len(deck.cards), 47)

    def test_deal_exceed_returns_remaining_cards(self) -> None:
        deck = Deck(shuffle_on_init=False)
        hand = deck.deal(60)
        self.assertEqual(len(hand), 52)
        self.assertEqual(len(deck.cards), 0)


class TestHand(unittest.TestCase):
    """Hand 容器測試。"""

    def test_sort_desc(self) -> None:
        hand = Hand([Card(3, 0), Card(14, 3), Card(15, 1), Card(14, 1)])
        hand.sort_desc()
        self.assertEqual(hand.cards, [Card(15, 1), Card(14, 3), Card(14, 1), Card(3, 0)])

    def test_find_3_clubs(self) -> None:
        hand = Hand([Card(14, 3), Card(3, 0), Card(7, 2)])
        self.assertEqual(hand.find_3_clubs(), Card(3, 0))

    def test_find_3_clubs_none(self) -> None:
        hand = Hand([Card(14, 3), Card(4, 0)])
        self.assertIsNone(hand.find_3_clubs())

    def test_remove_cards_success(self) -> None:
        hand = Hand([Card(14, 3), Card(3, 0)])
        self.assertTrue(hand.remove_cards([Card(3, 0)]))
        self.assertEqual(hand.cards, [Card(14, 3)])

    def test_remove_cards_not_found(self) -> None:
        hand = Hand([Card(14, 3)])
        self.assertFalse(hand.remove_cards([Card(3, 0)]))
        self.assertEqual(hand.cards, [Card(14, 3)])


class TestPlayer(unittest.TestCase):
    """Player 類別測試。"""

    def test_take_cards(self) -> None:
        player = Player("Player1")
        player.take_cards([Card(3, 0), Card(14, 3)])
        self.assertEqual(len(player.hand), 2)
        self.assertEqual(player.hand.cards[0], Card(14, 3))

    def test_play_cards(self) -> None:
        player = Player("Player1")
        player.take_cards([Card(3, 0), Card(14, 3)])
        self.assertTrue(player.play_cards([Card(3, 0)]))
        self.assertEqual(len(player.hand), 1)


if __name__ == "__main__":
    unittest.main()
