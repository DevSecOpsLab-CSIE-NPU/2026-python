"""Week 05 - Phase 1 資料模型單元測試。

本檔案依據 p1-test.md 設計，使用 Python 內建 unittest 框架。
測試目標：Card、Deck、Hand、Player 四個類別的核心行為。
"""

import unittest
from importlib import import_module


# 透過動態匯入降低執行目錄差異造成的路徑問題。
try:
	models = import_module("game.models")
	Card = models.Card
	Deck = models.Deck
	Hand = models.Hand
	Player = models.Player
	IMPORT_ERROR = None
except ModuleNotFoundError as error:
	Card = Deck = Hand = Player = None
	IMPORT_ERROR = error


@unittest.skipIf(IMPORT_ERROR is not None, "找不到 game.models，請在專案根目錄執行測試")
class TestCard(unittest.TestCase):
	"""Card 類別測試：建立、顯示、比較與排序鍵。"""

	def test_card_creation(self):
		card = Card(rank=14, suit=3)
		self.assertEqual(card.rank, 14)
		self.assertEqual(card.suit, 3)

	def test_card_repr_ace(self):
		self.assertEqual(repr(Card(14, 3)), "♠A")

	def test_card_repr_three(self):
		self.assertEqual(repr(Card(3, 0)), "♣3")

	def test_card_compare_suit(self):
		self.assertGreater(Card(14, 3), Card(14, 2))  # ♠ > ♥

	def test_card_compare_suit_2(self):
		self.assertGreater(Card(14, 2), Card(14, 1))  # ♥ > ♦

	def test_card_compare_suit_3(self):
		self.assertGreater(Card(14, 1), Card(14, 0))  # ♦ > ♣

	def test_card_compare_rank_2(self):
		self.assertGreater(Card(15, 0), Card(14, 3))  # 2 > A

	def test_card_compare_rank_a(self):
		self.assertGreater(Card(14, 0), Card(13, 3))  # A > K

	def test_card_compare_equal(self):
		self.assertFalse(Card(14, 3) > Card(14, 3))

	def test_card_sort_key(self):
		self.assertEqual(Card(14, 3).to_sort_key(), (14, 3))


@unittest.skipIf(IMPORT_ERROR is not None, "找不到 game.models，請在專案根目錄執行測試")
class TestDeck(unittest.TestCase):
	"""Deck 類別測試：52 張牌、洗牌、發牌。"""

	def test_deck_has_52_cards(self):
		deck = Deck()
		self.assertEqual(len(deck.cards), 52)

	def test_deck_all_unique(self):
		deck = Deck()
		self.assertEqual(len(set(deck.cards)), 52)

	def test_deck_all_ranks(self):
		deck = Deck()
		ranks = {card.rank for card in deck.cards}
		# 依遊戲規則應包含 3~15（15 代表 2）。
		self.assertEqual(ranks, set(range(3, 16)))

	def test_deck_all_suits(self):
		deck = Deck()
		suits = {card.suit for card in deck.cards}
		self.assertEqual(suits, {0, 1, 2, 3})

	def test_deck_shuffle(self):
		deck = Deck()
		before = list(deck.cards)
		deck.shuffle()
		after = deck.cards
		# 洗牌後應維持同一組牌，且順序通常會改變。
		self.assertEqual(set(before), set(after))
		self.assertNotEqual(before, after)

	def test_deal_5_cards(self):
		deck = Deck()
		dealt = deck.deal(5)
		self.assertEqual(len(dealt), 5)
		self.assertEqual(len(deck.cards), 47)

	def test_deal_multiple(self):
		deck = Deck()
		first = deck.deal(5)
		second = deck.deal(3)
		self.assertEqual(len(first), 5)
		self.assertEqual(len(second), 3)
		self.assertEqual(len(deck.cards), 44)

	def test_deal_exceed(self):
		deck = Deck()
		dealt = deck.deal(60)
		self.assertEqual(len(dealt), 52)
		self.assertEqual(len(deck.cards), 0)


@unittest.skipIf(IMPORT_ERROR is not None, "找不到 game.models，請在專案根目錄執行測試")
class TestHand(unittest.TestCase):
	"""Hand 類別測試：初始化、排序、查找、移除。"""

	def test_hand_creation(self):
		hand = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
		self.assertEqual(len(hand), 3)

	def test_hand_sort_desc(self):
		hand = Hand([
			Card(3, 0),   # ♣3
			Card(14, 3),  # ♠A
			Card(3, 3),   # ♠3
			Card(13, 2),  # ♥K
		])
		hand.sort_desc()
		self.assertEqual(hand, [Card(14, 3), Card(13, 2), Card(3, 3), Card(3, 0)])

	def test_hand_find_3_clubs(self):
		hand = Hand([Card(14, 3), Card(3, 0), Card(3, 1)])
		self.assertEqual(hand.find_3_clubs(), Card(3, 0))

	def test_hand_find_3_clubs_none(self):
		hand = Hand([Card(14, 3), Card(3, 1)])
		self.assertIsNone(hand.find_3_clubs())

	def test_hand_remove(self):
		c1 = Card(3, 0)
		c2 = Card(14, 3)
		c3 = Card(13, 2)
		hand = Hand([c1, c2, c3])
		hand.remove([c1, c2])
		self.assertEqual(hand, [c3])

	def test_hand_remove_not_found(self):
		hand = Hand([Card(3, 0), Card(14, 3)])
		hand.remove([Card(9, 1)])
		self.assertEqual(len(hand), 2)

	def test_hand_iteration(self):
		hand = Hand([Card(3, 0), Card(14, 3)])
		self.assertEqual(len(list(hand)), 2)


@unittest.skipIf(IMPORT_ERROR is not None, "找不到 game.models，請在專案根目錄執行測試")
class TestPlayer(unittest.TestCase):
	"""Player 類別測試：玩家屬性、拿牌、出牌。"""

	def test_player_human(self):
		player = Player("Player1", False)
		self.assertEqual(player.name, "Player1")
		self.assertFalse(player.is_ai)

	def test_player_ai(self):
		player = Player("AI_1", True)
		self.assertEqual(player.name, "AI_1")
		self.assertTrue(player.is_ai)

	def test_player_take(self):
		player = Player("Player1")
		player.take_cards([Card(3, 0), Card(14, 3)])
		self.assertEqual(len(player.hand), 2)

	def test_player_play(self):
		player = Player("Player1")
		cards = [Card(3, 0), Card(14, 3), Card(13, 2)]
		player.take_cards(cards)

		played = player.play_cards([cards[0], cards[1]])

		self.assertEqual(played, [cards[0], cards[1]])
		self.assertEqual(player.hand, Hand([cards[2]]))


if __name__ == "__main__":
	unittest.main(verbosity=2)
