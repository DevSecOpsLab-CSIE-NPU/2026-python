import unittest
import importlib

# 依題目規格：Card、Deck、Hand、Player 由你的遊戲模型模組提供。
# 若你的專案檔名不是 models.py，請將下行匯入改成正確路徑。
try:
    models = importlib.import_module("models")
    Card = models.Card
    Deck = models.Deck
    Hand = models.Hand
    Player = models.Player

    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False
    Card = Deck = Hand = Player = None


@unittest.skipUnless(MODELS_AVAILABLE, "找不到 models.py，請先完成模型類別實作")
class TestCard(unittest.TestCase):
    """Card 類別測試：建立、顯示、比較、排序鍵。"""

    def test_card_creation(self):
        card = Card(rank=14, suit=3)
        self.assertEqual(card.rank, 14)
        self.assertEqual(card.suit, 3)

    def test_card_repr_ace(self):
        # \u2660 = ♠
        self.assertEqual(repr(Card(14, 3)), "\u2660A")

    def test_card_repr_three(self):
        # \u2663 = ♣
        self.assertEqual(repr(Card(3, 0)), "\u26633")

    def test_card_compare_suit(self):
        self.assertTrue(Card(14, 3) > Card(14, 2))  # ♠ > ♥

    def test_card_compare_suit_2(self):
        self.assertTrue(Card(14, 2) > Card(14, 1))  # ♥ > ♦

    def test_card_compare_suit_3(self):
        self.assertTrue(Card(14, 1) > Card(14, 0))  # ♦ > ♣

    def test_card_compare_rank_2(self):
        self.assertTrue(Card(15, 0) > Card(14, 3))  # 2 > A

    def test_card_compare_rank_a(self):
        self.assertTrue(Card(14, 0) > Card(13, 3))  # A > K

    def test_card_compare_equal(self):
        self.assertFalse(Card(14, 3) > Card(14, 3))

    def test_card_sort_key(self):
        self.assertEqual(Card(14, 3).to_sort_key(), (14, 3))


@unittest.skipUnless(MODELS_AVAILABLE, "找不到 models.py，請先完成模型類別實作")
class TestDeck(unittest.TestCase):
    """Deck 類別測試：牌組內容、洗牌、發牌。"""

    def test_deck_has_52_cards(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_all_unique(self):
        deck = Deck()
        self.assertEqual(len(set(deck.cards)), 52)

    def test_deck_all_ranks(self):
        deck = Deck()
        ranks = {c.rank for c in deck.cards}
        # 規格包含 2（以 15 表示），因此應為 3~15。
        self.assertEqual(ranks, set(range(3, 16)))

    def test_deck_all_suits(self):
        deck = Deck()
        suits = {c.suit for c in deck.cards}
        self.assertEqual(suits, {0, 1, 2, 3})

    def test_deck_shuffle(self):
        deck = Deck()
        before = list(deck.cards)

        # 洗牌理論上應改變順序；為降低偶發機率，最多嘗試 5 次。
        changed = False
        for _ in range(5):
            deck.shuffle()
            if deck.cards != before:
                changed = True
                break

        self.assertTrue(changed, "shuffle() 未改變牌序")

    def test_deal_5_cards(self):
        deck = Deck()
        dealt = deck.deal(5)
        self.assertEqual(len(dealt), 5)
        self.assertEqual(len(deck.cards), 47)

    def test_deal_multiple(self):
        deck = Deck()
        deck.deal(5)
        deck.deal(3)
        self.assertEqual(len(deck.cards), 44)

    def test_deal_exceed(self):
        deck = Deck()
        dealt = deck.deal(60)
        self.assertEqual(len(dealt), 52)
        self.assertEqual(len(deck.cards), 0)


@unittest.skipUnless(MODELS_AVAILABLE, "找不到 models.py，請先完成模型類別實作")
class TestHand(unittest.TestCase):
    """Hand 類別測試：排序、查找、移除、迭代。"""

    def test_hand_creation(self):
        hand = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
        self.assertEqual(len(hand.cards), 3)

    def test_hand_sort_desc(self):
        # 目標順序：♠A, ♥K, ♠3, ♣3
        hand = Hand([Card(3, 0), Card(14, 3), Card(3, 3), Card(13, 2)])
        hand.sort_desc()
        self.assertEqual(hand.cards, [Card(14, 3), Card(13, 2), Card(3, 3), Card(3, 0)])

    def test_hand_find_3_clubs(self):
        hand = Hand([Card(14, 3), Card(3, 0), Card(3, 1)])
        self.assertEqual(hand.find_3_clubs(), Card(3, 0))

    def test_hand_find_3_clubs_none(self):
        hand = Hand([Card(14, 3), Card(3, 1)])
        self.assertIsNone(hand.find_3_clubs())

    def test_hand_remove(self):
        c1 = Card(14, 3)
        c2 = Card(3, 0)
        hand = Hand([c1, c2])
        hand.remove(c1)
        self.assertEqual(hand.cards, [c2])

    def test_hand_remove_not_found(self):
        hand = Hand([Card(14, 3)])
        hand.remove(Card(3, 0))
        self.assertEqual(len(hand.cards), 1)

    def test_hand_iteration(self):
        cards = [Card(14, 3), Card(3, 0)]
        hand = Hand(cards)
        self.assertEqual(len(list(hand)), 2)


@unittest.skipUnless(MODELS_AVAILABLE, "找不到 models.py，請先完成模型類別實作")
class TestPlayer(unittest.TestCase):
    """Player 類別測試：AI 屬性、拿牌、出牌。"""

    def test_player_human(self):
        player = Player("Player1", False)
        self.assertFalse(player.is_ai)

    def test_player_ai(self):
        player = Player("AI_1", True)
        self.assertTrue(player.is_ai)

    def test_player_take(self):
        player = Player("Player1", False)
        player.take_cards([Card(14, 3), Card(3, 0)])
        self.assertEqual(len(player.hand.cards), 2)

    def test_player_play(self):
        player = Player("Player1", False)
        card = Card(14, 3)
        player.take_cards([card, Card(3, 0)])

        played = player.play(card)
        self.assertEqual(played, card)
        self.assertEqual(len(player.hand.cards), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
