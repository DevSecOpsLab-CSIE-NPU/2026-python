import unittest
from game.models import Card, Deck, Player

class TestModels(unittest.TestCase):
    def test_card_sorting_and_comparison(self):
        """[上市標準] 確保大老二絕對牌值：2 > A > K"""
        c1 = Card(3, 0)   # ♣3 (最小)
        c2 = Card(14, 3)  # ♠A
        c3 = Card(15, 0)  # ♣2 (最大數字)
        c4 = Card(15, 3)  # ♠2 (遊戲絕對最大牌)

        self.assertTrue(c3 > c2)  # 2 必須大於 A
        self.assertTrue(c4 > c3)  # 黑桃 2 必須大於 梅花 2
        self.assertTrue(c2 > c1)  # A 必須大於 3

    def test_deck_integrity(self):
        """[防作弊] 確保牌堆每次發出來都是乾淨的 52 張，且無重複"""
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        self.assertEqual(len(set(deck.cards)), 52) # 檢查重複
        
        hand = deck.deal(13)
        self.assertEqual(len(hand), 13)
        self.assertEqual(len(deck.cards), 39)

    def test_player_remove_cards(self):
        """[記憶體安全] 測試出牌後手牌精確移除"""
        p = Player("Test")
        p.hand = [Card(3, 0), Card(4, 1), Card(5, 2)]
        p.remove_cards([Card(3, 0)]) # 打出梅花 3
        self.assertEqual(len(p.hand), 2)
        self.assertTrue(Card(3, 0) not in p.hand)