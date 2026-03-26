"""
Phase 1 資料模型單元測試

說明：
- 本檔案使用 Python 內建 unittest 撰寫。
- 測試目標為 Card、Deck、Hand、Player 四個類別。
- 請依你的專案實際模組路徑，調整下方 import 區塊。
"""

import unittest


# =========================
# 匯入待測模組（請依實際專案調整）
# =========================
# 預設先嘗試從 models 匯入；若你的結構不同請改成正確路徑。
try:
    from models import Card, Deck, Hand, Player
except ImportError as e:
    raise ImportError(
        "無法匯入 Card/Deck/Hand/Player。請確認模組路徑，例如 from bigtwo.models import ..."
    ) from e


class TestCard(unittest.TestCase):
    """Card 類別測試"""

    def test_card_creation(self):
        # 驗證建構子是否正確保存 rank 與 suit
        card = Card(rank=14, suit=3)
        self.assertEqual(card.rank, 14)
        self.assertEqual(card.suit, 3)

    def test_card_repr_ace(self):
        # 驗證 A 黑桃的字串表示
        card = Card(14, 3)
        self.assertEqual(repr(card), "♠A")

    def test_card_repr_three(self):
        # 驗證 3 梅花的字串表示
        card = Card(3, 0)
        self.assertEqual(repr(card), "♣3")

    def test_card_compare_suit(self):
        # 同點數時，比花色：♠ > ♥
        self.assertTrue(Card(14, 3) > Card(14, 2))

    def test_card_compare_suit_2(self):
        # 同點數時，比花色：♥ > ♦
        self.assertTrue(Card(14, 2) > Card(14, 1))

    def test_card_compare_suit_3(self):
        # 同點數時，比花色：♦ > ♣
        self.assertTrue(Card(14, 1) > Card(14, 0))

    def test_card_compare_rank_2(self):
        # 比點數：2(15) > A(14)
        self.assertTrue(Card(15, 0) > Card(14, 3))

    def test_card_compare_rank_a(self):
        # 比點數：A(14) > K(13)
        self.assertTrue(Card(14, 0) > Card(13, 3))

    def test_card_compare_equal(self):
        # 同一張牌不應大於自己
        self.assertFalse(Card(14, 3) > Card(14, 3))

    def test_card_sort_key(self):
        # 驗證排序鍵是否為 (rank, suit)
        self.assertEqual(Card(14, 3).to_sort_key(), (14, 3))


class TestDeck(unittest.TestCase):
    """Deck 類別測試"""

    def test_deck_has_52_cards(self):
        # 一副牌應有 52 張
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_all_unique(self):
        # 每張牌都應唯一（以 repr 做唯一性判斷）
        deck = Deck()
        self.assertEqual(len({repr(c) for c in deck.cards}), 52)

    def test_deck_all_ranks(self):
        # 點數集合應完整（3 到 A，再到 2）
        deck = Deck()
        ranks = {c.rank for c in deck.cards}
        self.assertEqual(ranks, set(range(3, 16)))

    def test_deck_all_suits(self):
        # 花色集合應為 0,1,2,3
        deck = Deck()
        suits = {c.suit for c in deck.cards}
        self.assertEqual(suits, {0, 1, 2, 3})

    def test_deck_shuffle(self):
        # 洗牌後牌序應改變（極低機率碰撞，測試採穩健比較）
        deck = Deck()
        original_order = [repr(c) for c in deck.cards]
        deck.shuffle()
        shuffled_order = [repr(c) for c in deck.cards]
        self.assertNotEqual(original_order, shuffled_order)

    def test_deal_5_cards(self):
        # 發 5 張後，回傳 5 張且牌堆剩 47 張
        deck = Deck()
        dealt = deck.deal(5)
        self.assertEqual(len(dealt), 5)
        self.assertEqual(len(deck.cards), 47)

    def test_deal_multiple(self):
        # 連續發牌後，剩餘張數應正確
        deck = Deck()
        _ = deck.deal(5)
        _ = deck.deal(3)
        self.assertEqual(len(deck.cards), 44)

    def test_deal_exceed(self):
        # 要求超過牌堆數量時，應只回傳可發出的牌
        deck = Deck()
        dealt = deck.deal(60)
        self.assertEqual(len(dealt), 52)
        self.assertEqual(len(deck.cards), 0)


class TestHand(unittest.TestCase):
    """Hand 類別測試"""

    def test_hand_creation(self):
        # Hand 建立後，應包含傳入的牌
        hand = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
        self.assertEqual(len(hand.cards), 3)

    def test_hand_sort_desc(self):
        # 驗證由大到小排序：♠A, ♥K, ♠3, ♣3
        hand = Hand([Card(3, 0), Card(14, 3), Card(3, 3), Card(13, 2)])
        hand.sort_desc()
        actual = [repr(c) for c in hand.cards]
        self.assertEqual(actual, ["♠A", "♥K", "♠3", "♣3"])

    def test_hand_find_3_clubs(self):
        # 有 ♣3 時應找得到
        hand = Hand([Card(14, 3), Card(3, 0), Card(3, 1)])
        card = hand.find_3_clubs()
        self.assertIsNotNone(card)
        self.assertEqual(repr(card), "♣3")

    def test_hand_find_3_clubs_none(self):
        # 沒有 ♣3 時應回傳 None
        hand = Hand([Card(14, 3), Card(3, 1)])
        self.assertIsNone(hand.find_3_clubs())

    def test_hand_remove(self):
        # 移除存在的牌後，手牌數量應減少
        c1 = Card(14, 3)
        c2 = Card(3, 0)
        hand = Hand([c1, c2])
        hand.remove(c1)
        self.assertEqual(len(hand.cards), 1)
        self.assertEqual(repr(hand.cards[0]), "♣3")

    def test_hand_remove_not_found(self):
        # 移除不存在的牌，不應影響原本手牌
        hand = Hand([Card(14, 3), Card(3, 0)])
        hand.remove(Card(10, 2))
        self.assertEqual(len(hand.cards), 2)

    def test_hand_iteration(self):
        # Hand 應可被迭代
        hand = Hand([Card(14, 3), Card(3, 0)])
        self.assertEqual(len(list(hand)), 2)


class TestPlayer(unittest.TestCase):
    """Player 類別測試"""

    def test_player_human(self):
        # 驗證真人玩家旗標
        player = Player("Player1", False)
        self.assertFalse(player.is_ai)

    def test_player_ai(self):
        # 驗證 AI 玩家旗標
        player = Player("AI_1", True)
        self.assertTrue(player.is_ai)

    def test_player_take(self):
        # 玩家拿牌後，手牌數應增加
        player = Player("Player1", False)
        player.take_cards([Card(14, 3), Card(3, 0)])
        self.assertEqual(len(player.hand.cards), 2)

    def test_player_play(self):
        # 出牌後，手牌應減少且回傳所出的牌
        player = Player("Player1", False)
        target = Card(14, 3)
        player.take_cards([target, Card(3, 0)])
        played = player.play(target)
        self.assertEqual(repr(played), "♠A")
        self.assertEqual(len(player.hand.cards), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
