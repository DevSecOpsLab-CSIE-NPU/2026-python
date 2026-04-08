"""Week 05 - Phase 3 牌型搜尋單元測試。

本檔案依據 p3-test.md 與 p3-dev.md 設計，
測試目標為 HandFinder 的牌型搜尋與合法出牌搜尋。
"""

import unittest
from importlib import import_module


# 動態匯入可避免不同執行目錄造成的 import 路徑問題。
try:
	models = import_module("game.models")
	finder_mod = import_module("game.finder")
	classifier_mod = import_module("game.classifier")
	Card = models.Card
	Hand = models.Hand
	HandFinder = finder_mod.HandFinder
	HandClassifier = classifier_mod.HandClassifier
	CardType = classifier_mod.CardType
	IMPORT_ERROR = None
except ModuleNotFoundError as error:
	Card = Hand = HandFinder = HandClassifier = CardType = None
	IMPORT_ERROR = error


@unittest.skipIf(IMPORT_ERROR is not None, "找不到 game 模組，請在專案根目錄執行測試")
class TestFindSingles(unittest.TestCase):
	"""測試單張搜尋。"""

	def test_find_singles(self):
		hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
		singles = HandFinder.find_singles(hand)
		self.assertEqual(len(singles), 3)
		self.assertTrue(all(len(play) == 1 for play in singles))

	def test_find_singles_empty(self):
		hand = Hand([])
		singles = HandFinder.find_singles(hand)
		self.assertEqual(singles, [])


@unittest.skipIf(IMPORT_ERROR is not None, "找不到 game 模組，請在專案根目錄執行測試")
class TestFindPairs(unittest.TestCase):
	"""測試對子搜尋。"""

	def test_find_pairs_one(self):
		hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
		pairs = HandFinder.find_pairs(hand)
		self.assertEqual(len(pairs), 1)
		self.assertEqual([c.rank for c in pairs[0]], [14, 14])

	def test_find_pairs_two(self):
		hand = Hand([Card(14, 3), Card(14, 2), Card(13, 3), Card(13, 0)])
		pairs = HandFinder.find_pairs(hand)
		self.assertEqual(len(pairs), 2)
		self.assertTrue(all(len(play) == 2 for play in pairs))

	def test_find_pairs_none(self):
		hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
		pairs = HandFinder.find_pairs(hand)
		self.assertEqual(pairs, [])


@unittest.skipIf(IMPORT_ERROR is not None, "找不到 game 模組，請在專案根目錄執行測試")
class TestFindTriples(unittest.TestCase):
	"""測試三條搜尋。"""

	def test_find_triples_one(self):
		hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0)])
		triples = HandFinder.find_triples(hand)
		self.assertEqual(len(triples), 1)
		self.assertEqual([c.rank for c in triples[0]], [14, 14, 14])

	def test_find_triples_with_extra(self):
		# AAA + KK 應只產生 1 組三條。
		hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 3), Card(13, 2)])
		triples = HandFinder.find_triples(hand)
		self.assertEqual(len(triples), 1)


@unittest.skipIf(IMPORT_ERROR is not None, "找不到 game 模組，請在專案根目錄執行測試")
class TestFindFives(unittest.TestCase):
	"""測試五張牌型搜尋。"""

	def _contains_type(self, plays, target_type):
		# 將每一組五張牌交給 HandClassifier 判定，確認是否含指定牌型。
		for play in plays:
			classified = HandClassifier.classify(play)
			if classified is not None and classified[0] == target_type:
				return True
		return False

	def test_find_straight(self):
		hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0), Card(11, 2)])
		fives = HandFinder.find_fives(hand)
		self.assertTrue(self._contains_type(fives, CardType.STRAIGHT))

	def test_find_flush(self):
		hand = Hand([Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0), Card(4, 1)])
		fives = HandFinder.find_fives(hand)
		self.assertTrue(self._contains_type(fives, CardType.FLUSH))

	def test_find_full_house(self):
		hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 3), Card(13, 2), Card(4, 0)])
		fives = HandFinder.find_fives(hand)
		self.assertTrue(self._contains_type(fives, CardType.FULL_HOUSE))

	def test_find_four_of_a_kind(self):
		hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 1), Card(5, 2)])
		fives = HandFinder.find_fives(hand)
		self.assertTrue(self._contains_type(fives, CardType.FOUR_OF_A_KIND))

	def test_find_straight_flush(self):
		hand = Hand([Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0), Card(10, 2)])
		fives = HandFinder.find_fives(hand)
		self.assertTrue(self._contains_type(fives, CardType.STRAIGHT_FLUSH))


@unittest.skipIf(IMPORT_ERROR is not None, "找不到 game 模組，請在專案根目錄執行測試")
class TestGetAllValidPlays(unittest.TestCase):
	"""測試合法出牌搜尋。"""

	def test_first_turn(self):
		hand = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
		plays = HandFinder.get_all_valid_plays(hand, None)
		# 第一手必須含 3♣，此處至少應包含 [3♣]。
		self.assertIn([Card(3, 0)], plays)

	def test_with_last_single(self):
		hand = Hand([Card(6, 0), Card(7, 1), Card(10, 2), Card(11, 3)])
		last_play = [Card(5, 2)]
		plays = HandFinder.get_all_valid_plays(hand, last_play)
		self.assertTrue(all(len(play) == 1 for play in plays))

	def test_with_last_pair(self):
		hand = Hand([Card(6, 3), Card(6, 2), Card(8, 3), Card(9, 2)])
		last_play = [Card(5, 3), Card(5, 2)]
		plays = HandFinder.get_all_valid_plays(hand, last_play)
		self.assertTrue(all(len(play) == 2 for play in plays))

	def test_no_valid(self):
		hand = Hand([Card(3, 1), Card(4, 2), Card(7, 0), Card(9, 3)])
		last_play = [Card(15, 3)]
		plays = HandFinder.get_all_valid_plays(hand, last_play)
		self.assertEqual(plays, [])


if __name__ == "__main__":
	unittest.main(verbosity=2)
