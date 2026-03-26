"""Phase 1 資料模型測試（Card / Deck / Hand / Player）。

使用方式（在專案根目錄執行）：
    python -m unittest tests.test_models -v

預期被測模組位置：
    game/models.py
"""

from __future__ import annotations

import importlib
import unittest

# 依照題目設計，模型應放在 game/models.py。
# 使用動態匯入可避免在尚未建立模組時出現編輯器靜態錯誤。
try:
    _models = importlib.import_module("game.models")
except ModuleNotFoundError as exc:
    raise unittest.SkipTest("找不到 game.models，請先依 p1-dev.md 實作模型") from exc

Card = _models.Card
Deck = _models.Deck
Hand = _models.Hand
Player = _models.Player


class TestCard(unittest.TestCase):
    """Card 類別測試。"""

    def test_card_creation(self) -> None:
        card = Card(rank=14, suit=3)
        self.assertEqual(card.rank, 14)
        self.assertEqual(card.suit, 3)

    def test_card_repr_ace(self) -> None:
        self.assertEqual(repr(Card(14, 3)), "♠A")

    def test_card_repr_three(self) -> None:
        self.assertEqual(repr(Card(3, 0)), "♣3")

    def test_card_compare_suit(self) -> None:
        self.assertTrue(Card(14, 3) > Card(14, 2))  # ♠ > ♥

    def test_card_compare_suit_2(self) -> None:
        self.assertTrue(Card(14, 2) > Card(14, 1))  # ♥ > ♦

    def test_card_compare_suit_3(self) -> None:
        self.assertTrue(Card(14, 1) > Card(14, 0))  # ♦ > ♣

    def test_card_compare_rank_2(self) -> None:
        self.assertTrue(Card(15, 0) > Card(14, 3))  # 2 > A

    def test_card_compare_rank_a(self) -> None:
        self.assertTrue(Card(14, 0) > Card(13, 3))  # A > K

    def test_card_compare_equal(self) -> None:
        self.assertFalse(Card(14, 3) > Card(14, 3))

    def test_card_sort_key(self) -> None:
        self.assertEqual(Card(14, 3).to_sort_key(), (14, 3))


class TestDeck(unittest.TestCase):
    """Deck 類別測試。"""

    def test_deck_has_52_cards(self) -> None:
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_all_unique(self) -> None:
        deck = Deck()
        # 題目要求每張牌都唯一，若 __eq__/__hash__ 有問題，這裡會抓出來。
        self.assertEqual(len(set(deck.cards)), 52)

    def test_deck_all_ranks(self) -> None:
        deck = Deck()
        ranks = {card.rank for card in deck.cards}
        self.assertEqual(ranks, set(range(3, 16)))  # 3..15

    def test_deck_all_suits(self) -> None:
        deck = Deck()
        suits = {card.suit for card in deck.cards}
        self.assertEqual(suits, {0, 1, 2, 3})

    def test_deck_shuffle(self) -> None:
        deck = Deck()
        before = list(deck.cards)

        # 洗牌有極小機率與原順序相同，重試數次以降低偶發失敗。
        changed = False
        for _ in range(5):
            deck.shuffle()
            if deck.cards != before:
                changed = True
                break

        self.assertTrue(changed, "shuffle() 未改變牌序（連續 5 次皆相同）")
        # 洗牌後仍應保有同一批牌。
        self.assertEqual(set(deck.cards), set(before))

    def test_deal_5_cards(self) -> None:
        deck = Deck()
        dealt = deck.deal(5)
        self.assertEqual(len(dealt), 5)
        self.assertEqual(len(deck.cards), 47)

    def test_deal_multiple(self) -> None:
        deck = Deck()
        deck.deal(5)
        deck.deal(3)
        self.assertEqual(len(deck.cards), 44)

    def test_deal_exceed(self) -> None:
        deck = Deck()
        dealt = deck.deal(60)
        self.assertEqual(len(dealt), 52)
        self.assertEqual(len(deck.cards), 0)


class TestHand(unittest.TestCase):
    """Hand 類別測試。"""

    def test_hand_creation(self) -> None:
        hand = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
        self.assertEqual(len(hand), 3)

    def test_hand_sort_desc(self) -> None:
        # 輸入：[♣3, ♠A, ♠3, ♥K]
        hand = Hand([Card(3, 0), Card(14, 3), Card(3, 3), Card(13, 2)])
        hand.sort_desc()
        # 預期：♠A, ♥K, ♠3, ♣3
        self.assertEqual(hand, [Card(14, 3), Card(13, 2), Card(3, 3), Card(3, 0)])

    def test_hand_find_3_clubs(self) -> None:
        hand = Hand([Card(14, 3), Card(3, 0), Card(3, 1)])
        self.assertEqual(hand.find_3_clubs(), Card(3, 0))

    def test_hand_find_3_clubs_none(self) -> None:
        hand = Hand([Card(14, 3), Card(3, 1)])
        self.assertIsNone(hand.find_3_clubs())

    def test_hand_remove(self) -> None:
        c1, c2 = Card(3, 0), Card(14, 3)
        hand = Hand([c1, c2])
        hand.remove([c1])
        self.assertEqual(hand, [c2])

    def test_hand_remove_not_found(self) -> None:
        c1, c2 = Card(3, 0), Card(14, 3)
        hand = Hand([c1])
        hand.remove([c2])
        self.assertEqual(len(hand), 1)
        self.assertEqual(hand[0], c1)

    def test_hand_iteration(self) -> None:
        hand = Hand([Card(3, 0), Card(14, 3)])
        self.assertEqual(len(list(hand)), 2)


class TestPlayer(unittest.TestCase):
    """Player 類別測試。"""

    def test_player_human(self) -> None:
        player = Player("Player1", False)
        self.assertFalse(player.is_ai)

    def test_player_ai(self) -> None:
        player = Player("AI_1", True)
        self.assertTrue(player.is_ai)

    def test_player_take(self) -> None:
        player = Player("P1", False)
        player.take_cards([Card(3, 0), Card(14, 3)])
        self.assertEqual(len(player.hand), 2)

    def test_player_play(self) -> None:
        player = Player("P1", False)
        c1, c2 = Card(3, 0), Card(14, 3)
        player.take_cards([c1, c2])

        played = player.play_cards([c1])

        self.assertEqual(played, [c1])
        self.assertEqual(player.hand, Hand([c2]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
