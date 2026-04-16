"""Phase 1 標準版模型測試。

使用 unittest 驗證 Card / Deck / Hand / Player 是否符合題目規格。
"""

from __future__ import annotations

import unittest

from game.models import Card, Deck, Hand, Player


class TestCard(unittest.TestCase):
    # Card 基礎建立與顯示
    def test_card_creation(self):
        c = Card(rank=14, suit=3)
        self.assertEqual(c.rank, 14)
        self.assertEqual(c.suit, 3)

    def test_card_repr_ace(self):
        self.assertEqual(repr(Card(14, 3)), "♠A")

    def test_card_repr_three(self):
        self.assertEqual(repr(Card(3, 0)), "♣3")

    # 比較規則：先點數，再花色
    def test_card_compare_suit(self):
        self.assertTrue(Card(14, 3) > Card(14, 2))

    def test_card_compare_rank_2(self):
        self.assertTrue(Card(15, 0) > Card(14, 3))

    def test_card_compare_equal(self):
        self.assertFalse(Card(14, 3) > Card(14, 3))
        self.assertEqual(Card(14, 3), Card(14, 3))

    def test_card_sort_key(self):
        self.assertEqual(Card(14, 3).to_sort_key(), (14, 3))


class TestDeck(unittest.TestCase):
    def test_deck_has_52_cards(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_all_unique(self):
        deck = Deck()
        self.assertEqual(len(set(deck.cards)), 52)

    def test_deck_all_ranks_and_suits(self):
        deck = Deck()
        ranks = {c.rank for c in deck.cards}
        suits = {c.suit for c in deck.cards}
        self.assertEqual(ranks, set(range(3, 16)))
        self.assertEqual(suits, {0, 1, 2, 3})

    def test_deck_shuffle(self):
        deck = Deck()
        before = deck.cards[:]
        deck.shuffle()
        # 洗牌有極小機率與原順序相同，因此允許最多重試 5 次。
        for _ in range(5):
            if deck.cards != before:
                break
            deck.shuffle()
        self.assertNotEqual(deck.cards, before)

    def test_deal_5_cards(self):
        deck = Deck()
        cards = deck.deal(5)
        self.assertEqual(len(cards), 5)
        self.assertEqual(len(deck.cards), 47)

    def test_deal_multiple(self):
        deck = Deck()
        deck.deal(5)
        deck.deal(3)
        self.assertEqual(len(deck.cards), 44)

    def test_deal_exceed(self):
        deck = Deck()
        cards = deck.deal(60)
        self.assertEqual(len(cards), 52)
        self.assertEqual(len(deck.cards), 0)


class TestHand(unittest.TestCase):
    def test_hand_creation(self):
        h = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
        self.assertEqual(len(h), 3)

    def test_hand_sort_desc(self):
        h = Hand([Card(3, 0), Card(14, 3), Card(3, 3), Card(13, 2)])
        h.sort_desc()
        self.assertEqual(h, [Card(14, 3), Card(13, 2), Card(3, 0), Card(3, 3)])

    def test_hand_find_3_clubs(self):
        h = Hand([Card(14, 3), Card(3, 0), Card(3, 1)])
        self.assertEqual(h.find_3_clubs(), Card(3, 0))

    def test_hand_find_3_clubs_none(self):
        h = Hand([Card(14, 3), Card(3, 1)])
        self.assertIsNone(h.find_3_clubs())

    def test_hand_remove(self):
        c1, c2, c3 = Card(3, 0), Card(14, 3), Card(13, 2)
        h = Hand([c1, c2, c3])
        h.remove([c1, c3])
        self.assertEqual(h, [c2])

    def test_hand_remove_not_found(self):
        h = Hand([Card(3, 0), Card(14, 3)])
        h.remove([Card(13, 2)])
        self.assertEqual(len(h), 2)


class TestPlayer(unittest.TestCase):
    def test_player_human(self):
        p = Player("Player1", False)
        self.assertFalse(p.is_ai)

    def test_player_ai(self):
        p = Player("AI_1", True)
        self.assertTrue(p.is_ai)

    def test_player_take(self):
        p = Player("P")
        p.take_cards([Card(3, 0), Card(14, 3)])
        self.assertEqual(len(p.hand), 2)

    def test_player_play(self):
        c1, c2 = Card(3, 0), Card(14, 3)
        p = Player("P")
        p.take_cards([c1, c2])
        played = p.play_cards([c2])
        self.assertEqual(played, [c2])
        self.assertEqual(p.hand, [c1])


if __name__ == "__main__":
    unittest.main()
