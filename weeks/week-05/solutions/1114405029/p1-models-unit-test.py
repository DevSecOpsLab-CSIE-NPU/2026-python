# p1-models-unit-test.py
# Phase 1 單元測試：Card、Deck、Hand、Player
#
# 測試依據：p1-test.md
#
# 執行方式（在 1114405029/ 目錄下）：
#   python p1-models-unit-test.py
#
# 花色：0=♣  1=♦  2=♥  3=♠
# 點數：3–9 照字面，T=10, J=11, Q=12, K=13, A=14, 2=15

import unittest
from p1_models import Card, Deck, Hand, Player


# =========================================================
# TestCard
# =========================================================
class TestCard(unittest.TestCase):

    # ── 建立 ──────────────────────────────────────────────
    def test_card_creation(self):
        """Card(14, 3) 建立後 rank==14, suit==3。"""
        c = Card(14, 3)
        self.assertEqual(c.rank, 14)
        self.assertEqual(c.suit, 3)

    # ── __repr__ ──────────────────────────────────────────
    def test_card_repr_ace(self):
        """A♠ 的字串表示應為 '♠A'。"""
        self.assertEqual(repr(Card(14, 3)), "♠A")

    def test_card_repr_three(self):
        """3♣ 的字串表示應為 '♣3'（遊戲起始牌）。"""
        self.assertEqual(repr(Card(3, 0)), "♣3")

    def test_card_repr_two(self):
        """2♣（rank=15）的字串表示應為 '♣2'（最大牌）。"""
        self.assertEqual(repr(Card(15, 0)), "♣2")

    def test_card_repr_king_heart(self):
        """K♥ 的字串表示應為 '♥K'。"""
        self.assertEqual(repr(Card(13, 2)), "♥K")

    def test_card_repr_ten(self):
        """10♦ 的字串表示應為 '♦T'（T 代表 10）。"""
        self.assertEqual(repr(Card(10, 1)), "♦T")

    # ── __eq__ ────────────────────────────────────────────
    def test_card_eq(self):
        """相同 rank 與 suit 的牌應相等。"""
        self.assertEqual(Card(14, 3), Card(14, 3))

    def test_card_neq_rank(self):
        """rank 不同的牌不應相等。"""
        self.assertNotEqual(Card(14, 3), Card(13, 3))

    def test_card_neq_suit(self):
        """suit 不同的牌不應相等。"""
        self.assertNotEqual(Card(14, 3), Card(14, 2))

    # ── 大小比較（花色） ───────────────────────────────────
    def test_card_compare_suit(self):
        """♠A(3) > ♥A(2)：同 rank 時花色大者勝。"""
        self.assertGreater(Card(14, 3), Card(14, 2))

    def test_card_compare_suit_2(self):
        """♥A(2) > ♦A(1)。"""
        self.assertGreater(Card(14, 2), Card(14, 1))

    def test_card_compare_suit_3(self):
        """♦A(1) > ♣A(0)。"""
        self.assertGreater(Card(14, 1), Card(14, 0))

    # ── 大小比較（點數） ───────────────────────────────────
    def test_card_compare_rank_2(self):
        """2♣（rank=15）> A♠（rank=14）：2 是最大牌。"""
        self.assertGreater(Card(15, 0), Card(14, 3))

    def test_card_compare_rank_a(self):
        """A♣（rank=14）> K♠（rank=13）。"""
        self.assertGreater(Card(14, 0), Card(13, 3))

    def test_card_compare_equal(self):
        """相同的牌 Card(14,3) > Card(14,3) 應為 False。"""
        self.assertFalse(Card(14, 3) > Card(14, 3))

    # ── to_sort_key ───────────────────────────────────────
    def test_card_sort_key(self):
        """to_sort_key() 應回傳 (rank, suit) 元組。"""
        self.assertEqual(Card(14, 3).to_sort_key(), (14, 3))

    def test_card_sort_key_three_clubs(self):
        """3♣ 的排序鍵應為 (3, 0)。"""
        self.assertEqual(Card(3, 0).to_sort_key(), (3, 0))

    # ── __hash__ ──────────────────────────────────────────
    def test_card_hash_equal(self):
        """相等的兩張牌雜湊值必須相同。"""
        self.assertEqual(hash(Card(14, 3)), hash(Card(14, 3)))

    def test_card_in_set(self):
        """Card 可放入 set；两张相同的牌只算一個。"""
        s = {Card(14, 3), Card(14, 3), Card(3, 0)}
        self.assertEqual(len(s), 2)


# =========================================================
# TestDeck
# =========================================================
class TestDeck(unittest.TestCase):

    def setUp(self):
        """每個測試前建立全新牌組。"""
        self.deck = Deck()

    def test_deck_has_52_cards(self):
        """牌組初始應有恰好 52 張牌。"""
        self.assertEqual(len(self.deck.cards), 52)

    def test_deck_all_unique(self):
        """52 張牌必須全部不重複。"""
        self.assertEqual(len(set(self.deck.cards)), 52)

    def test_deck_all_ranks(self):
        """牌組應包含 rank 3–15 的所有點數。"""
        ranks = {c.rank for c in self.deck.cards}
        self.assertEqual(ranks, set(range(3, 16)))

    def test_deck_all_suits(self):
        """每個花色（0–3）均應出現。"""
        suits = {c.suit for c in self.deck.cards}
        self.assertEqual(suits, {0, 1, 2, 3})

    def test_deck_shuffle(self):
        """洗牌後牌的順序應改變（機率極低為相同，可接受）。"""
        before = list(self.deck.cards)
        self.deck.shuffle()
        # 確認集合不變（沒有遺失或新增牌）
        self.assertEqual(set(self.deck.cards), set(before))
        # 確認張數不變
        self.assertEqual(len(self.deck.cards), 52)

    def test_deal_5_cards(self):
        """deal(5) 應回傳 5 張，牌組剩 47 張。"""
        dealt = self.deck.deal(5)
        self.assertEqual(len(dealt), 5)
        self.assertEqual(len(self.deck.cards), 47)

    def test_deal_multiple(self):
        """deal(5) 後再 deal(3)，牌組應剩 44 張。"""
        self.deck.deal(5)
        self.deck.deal(3)
        self.assertEqual(len(self.deck.cards), 44)

    def test_deal_exceed(self):
        """deal(60) 超過張數時，應回傳 52 張且牌組清空。"""
        dealt = self.deck.deal(60)
        self.assertEqual(len(dealt), 52)
        self.assertEqual(len(self.deck.cards), 0)


# =========================================================
# TestHand
# =========================================================
class TestHand(unittest.TestCase):

    def test_hand_creation(self):
        """Hand 傳入 3 張牌後長度應為 3。"""
        hand = Hand([Card(14, 3), Card(3, 0), Card(13, 2)])
        self.assertEqual(len(hand), 3)

    def test_hand_creation_empty(self):
        """Hand() 不傳參數應建立空手牌。"""
        self.assertEqual(len(Hand()), 0)

    def test_hand_creation_none(self):
        """Hand(None) 應等同於空手牌。"""
        self.assertEqual(len(Hand(None)), 0)

    def test_hand_is_list(self):
        """Hand 繼承 list，isinstance 應為 True。"""
        self.assertIsInstance(Hand(), list)

    def test_hand_iteration(self):
        """Hand 應可迭代，list() 轉換長度應一致。"""
        hand = Hand([Card(14, 3), Card(3, 0)])
        self.assertEqual(len(list(hand)), 2)

    def test_hand_sort_desc(self):
        """sort_desc() 排序：rank 倒序，同 rank 時 suit 倒序。

        輸入  : [3♣, ♠A, ♠3, ♥K]
        預期  : [♠A, ♥K, ♠3, ♣3]
        """
        hand = Hand([Card(3, 0), Card(14, 3), Card(3, 3), Card(13, 2)])
        hand.sort_desc()
        expected = [Card(14, 3), Card(13, 2), Card(3, 3), Card(3, 0)]
        self.assertEqual(hand, expected)

    def test_hand_find_3_clubs_present(self):
        """手牌中有 3♣ 時，find_3_clubs() 應回傳 Card(3, 0)。"""
        hand = Hand([Card(14, 3), Card(3, 0), Card(10, 1)])
        self.assertEqual(hand.find_3_clubs(), Card(3, 0))

    def test_hand_find_3_clubs_none(self):
        """手牌中沒有 3♣（只有 3♦）時，應回傳 None。"""
        hand = Hand([Card(14, 3), Card(3, 1)])
        self.assertIsNone(hand.find_3_clubs())

    def test_hand_remove(self):
        """remove() 移除一張後，手牌剩 1 張。"""
        hand = Hand([Card(14, 3), Card(3, 0)])
        hand.remove([Card(14, 3)])
        self.assertEqual(len(hand), 1)
        self.assertNotIn(Card(14, 3), hand)

    def test_hand_remove_not_found(self):
        """remove() 移除不存在的牌，手牌張數不應改變。"""
        hand = Hand([Card(14, 3)])
        hand.remove([Card(3, 0)])   # 不在手牌中
        self.assertEqual(len(hand), 1)


# =========================================================
# TestPlayer
# =========================================================
class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.human = Player("Player1", False)
        self.ai = Player("AI_1", True)

    def test_player_human(self):
        """人類玩家 is_ai 應為 False。"""
        self.assertFalse(self.human.is_ai)

    def test_player_ai(self):
        """AI 玩家 is_ai 應為 True。"""
        self.assertTrue(self.ai.is_ai)

    def test_player_name(self):
        """name 屬性應正確儲存。"""
        self.assertEqual(self.human.name, "Player1")

    def test_player_initial_hand_empty(self):
        """初始手牌應為空。"""
        self.assertEqual(len(self.human.hand), 0)

    def test_player_initial_score_zero(self):
        """初始分數應為 0。"""
        self.assertEqual(self.human.score, 0)

    def test_player_hand_is_hand(self):
        """hand 屬性應為 Hand 型別。"""
        self.assertIsInstance(self.human.hand, Hand)

    def test_player_take(self):
        """take_cards() 後手牌長度應增加。"""
        self.human.take_cards([Card(14, 3), Card(3, 0)])
        self.assertEqual(len(self.human.hand), 2)

    def test_player_take_twice(self):
        """兩次 take_cards() 應累積，不覆蓋。"""
        self.human.take_cards([Card(14, 3)])
        self.human.take_cards([Card(3, 0)])
        self.assertEqual(len(self.human.hand), 2)

    def test_player_play(self):
        """play_cards() 應從手牌移除出牌，並回傳出牌列表。"""
        cards = [Card(14, 3), Card(3, 0)]
        self.human.take_cards(cards)
        played = self.human.play_cards([Card(14, 3)])
        self.assertEqual(played, [Card(14, 3)])
        self.assertNotIn(Card(14, 3), self.human.hand)
        self.assertEqual(len(self.human.hand), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
