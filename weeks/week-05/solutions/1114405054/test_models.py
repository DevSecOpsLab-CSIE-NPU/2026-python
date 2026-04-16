"""Phase 1 資料模型的單元測試。"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


def _prepare_import_path() -> None:
    current = Path(__file__).resolve().parent

    for candidate in [current, *current.parents]:
        if (candidate / "game").is_dir():
            sys.path.insert(0, str(candidate))
            return

        if (candidate / "bigtwo" / "game").is_dir():
            sys.path.insert(0, str(candidate / "bigtwo"))
            return


_prepare_import_path()

from game.models import Card, Deck, Hand, Player


class TestCard(unittest.TestCase):
    def test_card_creation(self) -> None:
        card = Card(rank=14, suit=3)
        self.assertEqual(card.rank, 14)
        self.assertEqual(card.suit, 3)

    def test_card_repr_ace(self) -> None:
        self.assertEqual(repr(Card(14, 3)), "♠A")

    def test_card_repr_three(self) -> None:
        self.assertEqual(repr(Card(3, 0)), "♣3")

    def test_card_compare_suit(self) -> None:
        self.assertGreater(Card(14, 3), Card(14, 2))

    def test_card_compare_suit_2(self) -> None:
        self.assertGreater(Card(14, 2), Card(14, 1))

    def test_card_compare_suit_3(self) -> None:
        self.assertGreater(Card(14, 1), Card(14, 0))

    def test_card_compare_rank_2(self) -> None:
        self.assertGreater(Card(15, 0), Card(14, 3))

    def test_card_compare_rank_a(self) -> None:
        self.assertGreater(Card(14, 0), Card(13, 3))

    def test_card_compare_equal(self) -> None:
        self.assertFalse(Card(14, 3) > Card(14, 3))
        self.assertEqual(Card(14, 3), Card(14, 3))

    def test_card_sort_key(self) -> None:
        self.assertEqual(Card(14, 3).to_sort_key(), (14, 3))

    def test_card_hash_allows_set_deduplication(self) -> None:
        cards = {Card(14, 3), Card(14, 3), Card(13, 2)}
        self.assertEqual(len(cards), 2)


class TestDeck(unittest.TestCase):
    def test_deck_has_52_cards(self) -> None:
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_all_unique(self) -> None:
        deck = Deck()
        self.assertEqual(len(set(deck.cards)), 52)

    def test_deck_all_ranks(self) -> None:
        deck = Deck()
        ranks = {card.rank for card in deck.cards}
        self.assertEqual(ranks, set(range(3, 16)))

    def test_deck_all_suits(self) -> None:
        deck = Deck()
        suits = {card.suit for card in deck.cards}
        self.assertEqual(suits, {0, 1, 2, 3})

    def test_deck_shuffle(self) -> None:
        deck = Deck()
        original = [card.to_sort_key() for card in deck.cards]

        changed = False
        for _ in range(5):
            deck.shuffle()
            if [card.to_sort_key() for card in deck.cards] != original:
                changed = True
                break

        self.assertTrue(changed)
        self.assertEqual(len(deck.cards), 52)
        self.assertEqual(set(deck.cards), {Card(rank, suit) for rank in range(3, 16) for suit in range(4)})

    def test_deal_5_cards(self) -> None:
        deck = Deck()
        dealt = deck.deal(5)
        self.assertEqual(len(dealt), 5)
        self.assertEqual(len(deck.cards), 47)

    def test_deal_multiple(self) -> None:
        deck = Deck()
        first = deck.deal(5)
        second = deck.deal(3)
        self.assertEqual(len(first), 5)
        self.assertEqual(len(second), 3)
        self.assertEqual(len(deck.cards), 44)

    def test_deal_exceed(self) -> None:
        deck = Deck()
        dealt = deck.deal(60)
        self.assertEqual(len(dealt), 52)
        self.assertEqual(len(deck.cards), 0)


class TestHand(unittest.TestCase):
    def test_hand_creation(self) -> None:
        hand = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
        self.assertEqual(len(hand), 3)

    def test_hand_sort_desc(self) -> None:
        hand = Hand([Card(3, 0), Card(14, 3), Card(3, 3), Card(13, 2)])
        hand.sort_desc()
        self.assertEqual(list(hand), [Card(14, 3), Card(13, 2), Card(3, 3), Card(3, 0)])

    def test_hand_find_3_clubs(self) -> None:
        hand = Hand([Card(14, 3), Card(3, 0), Card(3, 1)])
        self.assertEqual(hand.find_3_clubs(), Card(3, 0))

    def test_hand_find_3_clubs_none(self) -> None:
        hand = Hand([Card(14, 3), Card(3, 1)])
        self.assertIsNone(hand.find_3_clubs())

    def test_hand_remove(self) -> None:
        hand = Hand([Card(14, 3), Card(3, 0), Card(3, 1)])
        hand.remove([Card(14, 3), Card(3, 0)])
        self.assertEqual(list(hand), [Card(3, 1)])

    def test_hand_remove_not_found(self) -> None:
        hand = Hand([Card(14, 3), Card(3, 0)])
        hand.remove([Card(13, 1)])
        self.assertEqual(len(hand), 2)
        self.assertEqual(list(hand), [Card(14, 3), Card(3, 0)])

    def test_hand_iteration(self) -> None:
        hand = Hand([Card(14, 3), Card(3, 0)])
        self.assertEqual(len(list(hand)), 2)


class TestPlayer(unittest.TestCase):
    def test_player_human(self) -> None:
        player = Player("Player1", False)
        self.assertEqual(player.name, "Player1")
        self.assertFalse(player.is_ai)
        self.assertEqual(player.score, 0)
        self.assertIsInstance(player.hand, Hand)

    def test_player_ai(self) -> None:
        player = Player("AI_1", True)
        self.assertTrue(player.is_ai)

    def test_player_take(self) -> None:
        player = Player("Player1")
        player.take_cards([Card(14, 3), Card(3, 0)])
        self.assertEqual(len(player.hand), 2)
        self.assertEqual(list(player.hand), [Card(14, 3), Card(3, 0)])

    def test_player_play(self) -> None:
        player = Player("Player1")
        cards = [Card(14, 3), Card(3, 0), Card(13, 2)]
        player.take_cards(cards)

        played = player.play_cards([Card(14, 3), Card(13, 2)])

        self.assertEqual(played, [Card(14, 3), Card(13, 2)])
        self.assertEqual(list(player.hand), [Card(3, 0)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
