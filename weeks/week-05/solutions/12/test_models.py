"""Phase 1：資料模型單元測試

本測試檔對應 week-05/game_design/p1-test.md 的需求，
使用 Python 內建 unittest 進行驗證。

預設匯入路徑為 game.models（依 p1-dev.md 規格）。
若你的專案實作在其他模組，可調整下方匯入區塊。
"""

import unittest
import importlib

def _load_models_module():
    """動態載入模型模組，避免編輯器在尚未實作時出現靜態匯入警告。"""
    for module_name in ("game.models", "models"):
        try:
            return importlib.import_module(module_name)
        except ModuleNotFoundError:
            continue
    raise ModuleNotFoundError(
        "找不到模型模組。請建立 game/models.py（或 models.py）後再執行測試。"
    )


_models = _load_models_module()
Card = _models.Card
Deck = _models.Deck
Hand = _models.Hand
Player = _models.Player


class TestCard(unittest.TestCase):
    """Card 類別測試。"""

    def test_card_creation(self):
        # 測試：初始化後 rank/suit 屬性是否正確
        card = Card(rank=14, suit=3)
        self.assertEqual(card.rank, 14)
        self.assertEqual(card.suit, 3)

    def test_card_repr_ace(self):
        # 測試：A♠ 的字串表示
        self.assertEqual(repr(Card(14, 3)), "♠A")

    def test_card_repr_three(self):
        # 測試：3♣ 的字串表示
        self.assertEqual(repr(Card(3, 0)), "♣3")

    def test_card_compare_suit(self):
        # 同點數比花色：♠ > ♥
        self.assertTrue(Card(14, 3) > Card(14, 2))

    def test_card_compare_suit_2(self):
        # 同點數比花色：♥ > ♦
        self.assertTrue(Card(14, 2) > Card(14, 1))

    def test_card_compare_suit_3(self):
        # 同點數比花色：♦ > ♣
        self.assertTrue(Card(14, 1) > Card(14, 0))

    def test_card_compare_rank_2(self):
        # 點數優先：2(15) > A(14)
        self.assertTrue(Card(15, 0) > Card(14, 3))

    def test_card_compare_rank_a(self):
        # 點數優先：A(14) > K(13)
        self.assertTrue(Card(14, 0) > Card(13, 3))

    def test_card_compare_equal(self):
        # 同一張牌不應大於自己
        self.assertFalse(Card(14, 3) > Card(14, 3))

    def test_card_sort_key(self):
        # to_sort_key 應回傳 (rank, suit)
        self.assertEqual(Card(14, 3).to_sort_key(), (14, 3))


class TestDeck(unittest.TestCase):
    """Deck 類別測試。"""

    def test_deck_has_52_cards(self):
        # 牌組初始化應包含 52 張牌
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_all_unique(self):
        # 全牌組不應有重複
        deck = Deck()
        self.assertEqual(len(set(deck.cards)), 52)

    def test_deck_all_ranks(self):
        # 點數集合應為 3..15（3~A~2）
        deck = Deck()
        ranks = {card.rank for card in deck.cards}
        self.assertEqual(ranks, set(range(3, 16)))

    def test_deck_all_suits(self):
        # 花色集合應為 0,1,2,3
        deck = Deck()
        suits = {card.suit for card in deck.cards}
        self.assertEqual(suits, {0, 1, 2, 3})

    def test_deck_shuffle(self):
        # 洗牌後牌序應改變（理論上幾乎一定改變）
        deck = Deck()
        before = list(deck.cards)
        deck.shuffle()
        after = deck.cards
        self.assertEqual(len(after), 52)
        self.assertNotEqual(before, after)

    def test_deal_5_cards(self):
        # 發 5 張：回傳 5 張、牌堆剩 47 張
        deck = Deck()
        dealt = deck.deal(5)
        self.assertEqual(len(dealt), 5)
        self.assertEqual(len(deck.cards), 47)

    def test_deal_multiple(self):
        # 連續發牌後，剩餘張數應正確
        deck = Deck()
        deck.deal(5)
        deck.deal(3)
        self.assertEqual(len(deck.cards), 44)

    def test_deal_exceed(self):
        # 超過牌堆剩餘張數時，應只回傳現有全部牌
        deck = Deck()
        dealt = deck.deal(60)
        self.assertEqual(len(dealt), 52)
        self.assertEqual(len(deck.cards), 0)


class TestHand(unittest.TestCase):
    """Hand 類別測試。"""

    def test_hand_creation(self):
        # Hand 初始化時應能接收牌列表
        hand = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
        self.assertEqual(len(hand), 3)

    def test_hand_sort_desc(self):
        # 依題目期望排序：♠A, ♥K, ♠3, ♣3
        hand = Hand([Card(3, 0), Card(14, 3), Card(3, 3), Card(13, 2)])
        hand.sort_desc()
        self.assertEqual(hand, [Card(14, 3), Card(13, 2), Card(3, 3), Card(3, 0)])

    def test_hand_find_3_clubs(self):
        # 應正確找到 3♣
        hand = Hand([Card(14, 3), Card(3, 0), Card(3, 1)])
        self.assertEqual(hand.find_3_clubs(), Card(3, 0))

    def test_hand_find_3_clubs_none(self):
        # 若沒有 3♣，應回傳 None
        hand = Hand([Card(14, 3), Card(3, 1)])
        self.assertIsNone(hand.find_3_clubs())

    def test_hand_remove(self):
        # 移除存在的牌後，手牌數應減少
        hand = Hand([Card(14, 3), Card(3, 0)])
        hand.remove([Card(3, 0)])
        self.assertEqual(len(hand), 1)
        self.assertEqual(hand[0], Card(14, 3))

    def test_hand_remove_not_found(self):
        # 移除不存在的牌，不應丟例外且手牌數不變
        hand = Hand([Card(14, 3), Card(3, 0)])
        hand.remove([Card(13, 2)])
        self.assertEqual(len(hand), 2)

    def test_hand_iteration(self):
        # Hand 應可被迭代（因為繼承 list）
        hand = Hand([Card(14, 3), Card(3, 0)])
        self.assertEqual(len(list(hand)), 2)


class TestPlayer(unittest.TestCase):
    """Player 類別測試。"""

    def test_player_human(self):
        # 人類玩家預期 is_ai=False
        player = Player("Player1", False)
        self.assertFalse(player.is_ai)

    def test_player_ai(self):
        # AI 玩家預期 is_ai=True
        player = Player("AI_1", True)
        self.assertTrue(player.is_ai)

    def test_player_take(self):
        # take_cards 後手牌數應增加
        player = Player("P1", False)
        player.take_cards([Card(14, 3), Card(3, 0)])
        self.assertEqual(len(player.hand), 2)

    def test_player_play(self):
        # play_cards 應回傳出牌，且玩家手牌減少
        player = Player("P1", False)
        cards = [Card(14, 3), Card(3, 0)]
        player.take_cards(cards)

        played = player.play_cards([Card(3, 0)])
        self.assertEqual(played, [Card(3, 0)])
        self.assertEqual(len(player.hand), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
