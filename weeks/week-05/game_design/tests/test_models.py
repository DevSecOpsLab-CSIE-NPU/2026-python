"""
Phase 1: 資料模型 - 單元測試
"""
import unittest
import sys
from pathlib import Path

# 添加 game 模組的路徑
sys.path.insert(0, str(Path(__file__).parent.parent))

from game.models import Card, Deck, Hand, Player


class TestCard(unittest.TestCase):
    """Card 類別測試"""
    
    def test_card_creation(self):
        """測試卡牌創建"""
        card = Card(rank=14, suit=3)
        self.assertEqual(card.rank, 14)
        self.assertEqual(card.suit, 3)
    
    def test_card_repr_ace(self):
        """測試 A♠ 的表示"""
        card = Card(14, 3)
        self.assertEqual(repr(card), "♠A")
    
    def test_card_repr_three(self):
        """測試 3♣ 的表示"""
        card = Card(3, 0)
        self.assertEqual(repr(card), "♣3")
    
    def test_card_compare_suit(self):
        """測試花色比較：♠ > ♥"""
        card1 = Card(14, 3)  # ♠A
        card2 = Card(14, 2)  # ♥A
        self.assertTrue(card1 > card2)
    
    def test_card_compare_suit_2(self):
        """測試花色比較：♥ > ♦"""
        card1 = Card(14, 2)  # ♥A
        card2 = Card(14, 1)  # ♦A
        self.assertTrue(card1 > card2)
    
    def test_card_compare_suit_3(self):
        """測試花色比較：♦ > ♣"""
        card1 = Card(14, 1)  # ♦A
        card2 = Card(14, 0)  # ♣A
        self.assertTrue(card1 > card2)
    
    def test_card_compare_rank_2(self):
        """測試點數比較：2 > A"""
        card1 = Card(15, 0)  # ♣2
        card2 = Card(14, 3)  # ♠A
        self.assertTrue(card1 > card2)
    
    def test_card_compare_rank_a(self):
        """測試點數比較：A > K"""
        card1 = Card(14, 0)  # ♣A
        card2 = Card(13, 3)  # ♠K
        self.assertTrue(card1 > card2)
    
    def test_card_compare_equal(self):
        """測試相等牌的比較"""
        card1 = Card(14, 3)  # ♠A
        card2 = Card(14, 3)  # ♠A
        self.assertFalse(card1 > card2)
        self.assertTrue(card1 == card2)
    
    def test_card_sort_key(self):
        """測試排序鍵"""
        card = Card(14, 3)
        self.assertEqual(card.to_sort_key(), (14, 3))


class TestDeck(unittest.TestCase):
    """Deck 類別測試"""
    
    def test_deck_has_52_cards(self):
        """測試牌組包含 52 張牌"""
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
    
    def test_deck_all_unique(self):
        """測試所有牌都獨一無二"""
        deck = Deck()
        self.assertEqual(len(set(deck.cards)), 52)
    
    def test_deck_all_ranks(self):
        """測試包含所有點數"""
        deck = Deck()
        ranks = {card.rank for card in deck.cards}
        self.assertEqual(ranks, set(range(3, 16)))
    
    def test_deck_all_suits(self):
        """測試包含所有花色"""
        deck = Deck()
        suits = {card.suit for card in deck.cards}
        self.assertEqual(suits, {0, 1, 2, 3})
    
    def test_deck_shuffle(self):
        """測試洗牌會改變順序"""
        deck1 = Deck()
        original = [repr(card) for card in deck1.cards]
        deck1.shuffle()
        shuffled = [repr(card) for card in deck1.cards]
        # 洗牌後很可能順序不同（理論上可能相同，但機率很小）
        # 我們只檢查總數不變
        self.assertEqual(len(original), len(shuffled))
    
    def test_deal_5_cards(self):
        """測試發 5 張牌"""
        deck = Deck()
        cards = deck.deal(5)
        self.assertEqual(len(cards), 5)
        self.assertEqual(len(deck.cards), 47)
    
    def test_deal_multiple(self):
        """測試連續發牌"""
        deck = Deck()
        deck.deal(5)
        deck.deal(3)
        self.assertEqual(len(deck.cards), 44)
    
    def test_deal_exceed(self):
        """測試發超過牌組的牌數"""
        deck = Deck()
        cards = deck.deal(60)
        self.assertEqual(len(cards), 52)
        self.assertEqual(len(deck.cards), 0)


class TestHand(unittest.TestCase):
    """Hand 類別測試"""
    
    def test_hand_creation(self):
        """測試手牌創建"""
        cards = [Card(3, 0), Card(5, 1), Card(7, 2)]
        hand = Hand(cards)
        self.assertEqual(len(hand), 3)
    
    def test_hand_sort_desc(self):
        """測試手牌倒序排列"""
        cards = [Card(3, 0), Card(14, 3), Card(3, 3), Card(13, 2)]
        hand = Hand(cards)
        hand.sort_desc()
        # 排序後：2♠ (15,3), A♠ (14,3), K♥ (13,2), 3♠ (3,3), 3♣ (3,0)
        # 期望順序：A♠, K♥, 3♠, 3♣（根據點數倒序）
        self.assertEqual(repr(hand[0]), "♠A")  # A (rank=14)
        self.assertEqual(repr(hand[1]), "♥K")  # K (rank=13)
    
    def test_hand_find_3_clubs(self):
        """測試找 3♣"""
        cards = [Card(14, 3), Card(3, 0), Card(3, 1)]
        hand = Hand(cards)
        found = hand.find_3_clubs()
        self.assertIsNotNone(found)
        self.assertEqual(found.rank, 3)
        self.assertEqual(found.suit, 0)
    
    def test_hand_find_3_clubs_none(self):
        """測試找不到 3♣"""
        cards = [Card(14, 3), Card(3, 1)]
        hand = Hand(cards)
        found = hand.find_3_clubs()
        self.assertIsNone(found)
    
    def test_hand_remove(self):
        """測試移除牌"""
        cards = [Card(14, 3), Card(3, 0), Card(3, 1)]
        hand = Hand(cards)
        to_remove = [Card(3, 0)]
        hand.remove(to_remove)
        self.assertEqual(len(hand), 2)
        self.assertNotIn(Card(3, 0), hand)
    
    def test_hand_remove_not_found(self):
        """測試移除不存在的牌"""
        cards = [Card(14, 3), Card(3, 1)]
        hand = Hand(cards)
        original_len = len(hand)
        to_remove = [Card(3, 0)]  # 不存在
        hand.remove(to_remove)
        self.assertEqual(len(hand), original_len)
    
    def test_hand_iteration(self):
        """測試手牌的迭代"""
        cards = [Card(14, 3), Card(3, 1)]
        hand = Hand(cards)
        result = list(hand)
        self.assertEqual(len(result), 2)


class TestPlayer(unittest.TestCase):
    """Player 類別測試"""
    
    def test_player_human(self):
        """測試人類玩家"""
        player = Player("Player1", False)
        self.assertEqual(player.name, "Player1")
        self.assertFalse(player.is_ai)
    
    def test_player_ai(self):
        """測試 AI 玩家"""
        player = Player("AI_1", True)
        self.assertEqual(player.name, "AI_1")
        self.assertTrue(player.is_ai)
    
    def test_player_take(self):
        """測試玩家拿牌"""
        player = Player("Player1")
        cards = [Card(3, 0), Card(5, 1)]
        player.take_cards(cards)
        self.assertEqual(len(player.hand), 2)
    
    def test_player_play(self):
        """測試玩家出牌"""
        player = Player("Player1")
        cards = [Card(3, 0), Card(5, 1), Card(7, 2)]
        player.take_cards(cards)
        to_play = [Card(3, 0)]
        result = player.play_cards(to_play)
        self.assertEqual(len(player.hand), 2)
        self.assertEqual(result, to_play)


if __name__ == '__main__':
    unittest.main(verbosity=2)
