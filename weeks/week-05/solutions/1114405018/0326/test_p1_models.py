"""
Phase 1 資料模型單元測試

本檔案依據 p1-test.md 的測試設計撰寫，使用 Python 內建 unittest。
重點測試對象：Card、Deck、Hand、Player。

執行方式（在專案根目錄或 bigtwo 專案根目錄下）：
    python -m unittest test_p1_models -v
或
    python -m unittest discover -v

注意：
1) 本測試預設你的實作檔案名稱為 models.py，且內含 Card/Deck/Hand/Player。
2) 若你的檔名不同，請調整下方 import 路徑。
"""

import unittest
from typing import List

# 依題意假設類別都在 models.py。
# 若你的專案結構不同，請改成正確匯入路徑。
from models import Card, Deck, Hand, Player


class TestCard(unittest.TestCase):
    """Card 類別測試：建立、顯示、比較與排序鍵值。"""

    def test_card_creation(self):
        """建立卡牌後，rank 與 suit 應正確保存。"""
        c = Card(rank=14, suit=3)
        self.assertEqual(c.rank, 14)
        self.assertEqual(c.suit, 3)

    def test_card_repr_ace(self):
        """A 黑桃的字串表示應為 ♠A。"""
        self.assertEqual(repr(Card(14, 3)), "♠A")

    def test_card_repr_three(self):
        """3 梅花的字串表示應為 ♣3。"""
        self.assertEqual(repr(Card(3, 0)), "♣3")

    def test_card_compare_suit(self):
        """同點數時，花色比較：♠ > ♥。"""
        self.assertTrue(Card(14, 3) > Card(14, 2))

    def test_card_compare_suit_2(self):
        """同點數時，花色比較：♥ > ♦。"""
        self.assertTrue(Card(14, 2) > Card(14, 1))

    def test_card_compare_suit_3(self):
        """同點數時，花色比較：♦ > ♣。"""
        self.assertTrue(Card(14, 1) > Card(14, 0))

    def test_card_compare_rank_2(self):
        """點數比較：2(15) 應大於 A(14)。"""
        self.assertTrue(Card(15, 0) > Card(14, 3))

    def test_card_compare_rank_a(self):
        """點數比較：A(14) 應大於 K(13)。"""
        self.assertTrue(Card(14, 0) > Card(13, 3))

    def test_card_compare_equal(self):
        """相同卡牌彼此不應大於對方。"""
        self.assertFalse(Card(14, 3) > Card(14, 3))

    def test_card_sort_key(self):
        """排序鍵值應回傳 (rank, suit)。"""
        self.assertEqual(Card(14, 3).to_sort_key(), (14, 3))


class TestDeck(unittest.TestCase):
    """Deck 類別測試：牌組完整性、洗牌與發牌行為。"""

    def test_deck_has_52_cards(self):
        """初始化牌組應有 52 張牌。"""
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_all_unique(self):
        """
        52 張牌應全部唯一。
        使用 (rank, suit) 作為唯一鍵，避免卡牌物件未實作 __hash__ 導致 set 問題。
        """
        deck = Deck()
        unique_keys = {(c.rank, c.suit) for c in deck.cards}
        self.assertEqual(len(unique_keys), 52)

    def test_deck_all_ranks(self):
        """牌組點數集合應涵蓋 3~15。"""
        deck = Deck()
        ranks = {c.rank for c in deck.cards}
        self.assertEqual(ranks, set(range(3, 16)))

    def test_deck_all_suits(self):
        """牌組花色集合應涵蓋 0~3。"""
        deck = Deck()
        suits = {c.suit for c in deck.cards}
        self.assertEqual(suits, {0, 1, 2, 3})

    def test_deck_shuffle(self):
        """洗牌後牌序應改變（極小機率可能同序，保守重試）。"""
        deck = Deck()
        original_order = [(c.rank, c.suit) for c in deck.cards]

        changed = False
        for _ in range(5):
            deck.shuffle()
            new_order = [(c.rank, c.suit) for c in deck.cards]
            if new_order != original_order:
                changed = True
                break

        self.assertTrue(changed, "shuffle() 連續多次後仍未改變牌序")

    def test_deal_5_cards(self):
        """發 5 張牌後，應回傳 5 張且牌庫剩 47 張。"""
        deck = Deck()
        dealt = deck.deal(5)
        self.assertEqual(len(dealt), 5)
        self.assertEqual(len(deck.cards), 47)

    def test_deal_multiple(self):
        """連續發牌數量應正確扣減。"""
        deck = Deck()
        first = deck.deal(5)
        second = deck.deal(3)
        self.assertEqual(len(first), 5)
        self.assertEqual(len(second), 3)
        self.assertEqual(len(deck.cards), 44)

    def test_deal_exceed(self):
        """要求超過剩餘牌數時，應回傳剩餘全部牌，牌庫清空。"""
        deck = Deck()
        dealt = deck.deal(60)
        self.assertEqual(len(dealt), 52)
        self.assertEqual(len(deck.cards), 0)


class TestHand(unittest.TestCase):
    """Hand 類別測試：建立、排序、搜尋、移除與迭代。"""

    def test_hand_creation(self):
        """建立手牌後，張數應與輸入一致。"""
        cards = [Card(3, 0), Card(14, 3), Card(13, 2)]
        hand = Hand(cards)
        self.assertEqual(len(list(hand)), 3)

    def test_hand_sort_desc(self):
        """排序後應為由大到小：♠A, ♥K, ♠3, ♣3。"""
        hand = Hand([Card(3, 0), Card(14, 3), Card(3, 3), Card(13, 2)])
        hand.sort_desc()
        self.assertEqual([repr(c) for c in hand], ["♠A", "♥K", "♠3", "♣3"])

    def test_hand_find_3_clubs(self):
        """有 ♣3 時，應能找到該卡。"""
        hand = Hand([Card(14, 3), Card(3, 0), Card(3, 1)])
        c = hand.find_3_clubs()
        self.assertIsNotNone(c)
        self.assertEqual((c.rank, c.suit), (3, 0))

    def test_hand_find_3_clubs_none(self):
        """沒有 ♣3 時，應回傳 None。"""
        hand = Hand([Card(14, 3), Card(3, 1)])
        self.assertIsNone(hand.find_3_clubs())

    def test_hand_remove(self):
        """移除存在的牌後，手牌數量應減少。"""
        c1 = Card(14, 3)
        c2 = Card(3, 0)
        hand = Hand([c1, c2])
        hand.remove(c1)
        self.assertEqual(len(list(hand)), 1)
        self.assertEqual(repr(list(hand)[0]), "♣3")

    def test_hand_remove_not_found(self):
        """移除不存在的牌，手牌數量應不變。"""
        hand = Hand([Card(14, 3), Card(3, 0)])
        hand.remove(Card(13, 2))
        self.assertEqual(len(list(hand)), 2)

    def test_hand_iteration(self):
        """Hand 應可迭代，轉成 list 後長度正確。"""
        hand = Hand([Card(14, 3), Card(3, 0)])
        cards = list(hand)
        self.assertEqual(len(cards), 2)


class TestPlayer(unittest.TestCase):
    """Player 類別測試：身份設定、拿牌、出牌流程。"""

    def test_player_human(self):
        """真人玩家 is_ai 應為 False。"""
        p = Player("Player1", False)
        self.assertFalse(p.is_ai)

    def test_player_ai(self):
        """AI 玩家 is_ai 應為 True。"""
        p = Player("AI_1", True)
        self.assertTrue(p.is_ai)

    def test_player_take(self):
        """玩家拿牌後，手牌數量應增加。"""
        p = Player("P", False)
        cards = [Card(14, 3), Card(3, 0)]
        p.take_cards(cards)
        self.assertEqual(len(list(p.hand)), 2)

    def test_player_play(self):
        """玩家出牌後，應回傳該牌且手牌數量減 1。"""
        p = Player("P", False)
        cards = [Card(14, 3), Card(3, 0)]
        p.take_cards(cards)

        # 以第一張牌作為出牌目標
        first_card = list(p.hand)[0]
        played = p.play(first_card)

        # play 介面預期回傳實際打出的卡牌
        self.assertEqual((played.rank, played.suit), (first_card.rank, first_card.suit))
        self.assertEqual(len(list(p.hand)), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
