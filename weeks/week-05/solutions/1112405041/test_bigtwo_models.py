import unittest
from bigtwo_models import Card, Deck, Hand, Player

class TestBigTwoModels(unittest.TestCase):
    """
    對齊 game_design/p1-test.md 的單元測試
    """

    def test_card_creation(self):
        # 測試卡片建立
        c = Card(14, 3) # 黑桃 A
        self.assertEqual(c.rank, 14)
        self.assertEqual(c.suit, 3)

    def test_card_repr(self):
        # 測試卡片文字顯示
        self.assertEqual(repr(Card(14, 3)), "♠A")
        self.assertEqual(repr(Card(3, 0)), "♣3")
        self.assertEqual(repr(Card(10, 2)), "♥T")

    def test_card_comparison(self):
        # 測試卡片大小比較 (黑桃 > 紅心 > 方塊 > 梅花)
        self.assertTrue(Card(14, 3) > Card(14, 2)) # ♠A > ♥A
        self.assertTrue(Card(15, 0) > Card(14, 3)) # ♣2 > ♠A (2 最大)
        self.assertTrue(Card(14, 0) > Card(13, 3)) # ♣A > ♠K
        self.assertFalse(Card(14, 3) < Card(14, 3)) # 相同則不小於

    def test_deck_initialization(self):
        # 測試牌組初始化
        d = Deck()
        self.assertEqual(len(d.cards), 52)
        # 測試唯一性 (不重複)
        self.assertEqual(len(set(d.cards)), 52)

    def test_deck_deal(self):
        # 測試發牌邏輯
        d = Deck()
        dealt = d.deal(13)
        self.assertEqual(len(dealt), 13)
        self.assertEqual(len(d.cards), 39)

    def test_hand_sorting(self):
        # 測試手牌排序
        h = Hand([Card(3, 0), Card(14, 3), Card(3, 3), Card(13, 2)])
        h.sort_desc()
        # 預期：♠A, ♥K, ♠3, ♣3
        self.assertEqual(repr(h[0]), "♠A")
        self.assertEqual(repr(h[-1]), "♣3")

    def test_hand_find_3_clubs(self):
        # 測試尋找梅花 3
        h1 = Hand([Card(14, 3), Card(3, 0)])
        self.assertIsNotNone(h1.find_3_clubs())

        h2 = Hand([Card(14, 3), Card(3, 1)])
        self.assertIsNone(h2.find_3_clubs())

    def test_player_initialization(self):
        # 測試玩家建立
        p = Player("CSIE_Student")
        self.assertEqual(p.name, "CSIE_Student")
        self.assertEqual(len(p.hand), 0)

if __name__ == "__main__":
    unittest.main()
