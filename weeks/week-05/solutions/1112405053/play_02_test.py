"""Week 05 - Phase 2 牌型分類單元測試。

本檔案依據 p2-test.md 設計，使用 Python 內建 unittest。
測試範圍：CardType、HandClassifier.classify、compare、can_play。
"""

import unittest
from importlib import import_module


# 以動態匯入處理不同執行路徑下的模組解析問題。
try:
	models = import_module("game.models")
	classifier = import_module("game.classifier")
	Card = models.Card
	CardType = classifier.CardType
	HandClassifier = classifier.HandClassifier
	IMPORT_ERROR = None
except ModuleNotFoundError as error:
	Card = CardType = HandClassifier = None
	IMPORT_ERROR = error


@unittest.skipIf(IMPORT_ERROR is not None, "找不到 game.models 或 game.classifier，請在專案根目錄執行測試")
class TestCardType(unittest.TestCase):
	"""測試 CardType 列舉值是否符合題目定義。"""

	def test_cardtype_values(self):
		self.assertEqual(CardType.SINGLE.value, 1)
		self.assertEqual(CardType.PAIR.value, 2)
		self.assertEqual(CardType.TRIPLE.value, 3)
		self.assertEqual(CardType.STRAIGHT.value, 4)
		self.assertEqual(CardType.FLUSH.value, 5)
		self.assertEqual(CardType.FULL_HOUSE.value, 6)
		self.assertEqual(CardType.FOUR_OF_A_KIND.value, 7)
		self.assertEqual(CardType.STRAIGHT_FLUSH.value, 8)


@unittest.skipIf(IMPORT_ERROR is not None, "找不到 game.models 或 game.classifier，請在專案根目錄執行測試")
class TestClassify(unittest.TestCase):
	"""測試 HandClassifier.classify 的牌型分類結果。"""

	def test_classify_single_ace(self):
		self.assertEqual(HandClassifier.classify([Card(14, 3)]), (CardType.SINGLE, 14, 3))

	def test_classify_single_two(self):
		self.assertEqual(HandClassifier.classify([Card(15, 0)]), (CardType.SINGLE, 15, 0))

	def test_classify_single_three(self):
		self.assertEqual(HandClassifier.classify([Card(3, 0)]), (CardType.SINGLE, 3, 0))

	def test_classify_pair(self):
		self.assertEqual(
			HandClassifier.classify([Card(14, 3), Card(14, 2)]),
			(CardType.PAIR, 14, 0),
		)

	def test_classify_pair_diff_rank(self):
		self.assertIsNone(HandClassifier.classify([Card(14, 3), Card(13, 3)]))

	def test_classify_pair_from_three(self):
		# 由三條中任取兩張，仍應視為合法對子。
		self.assertEqual(
			HandClassifier.classify([Card(14, 3), Card(14, 2)]),
			(CardType.PAIR, 14, 0),
		)

	def test_classify_triple(self):
		self.assertEqual(
			HandClassifier.classify([Card(14, 3), Card(14, 2), Card(14, 1)]),
			(CardType.TRIPLE, 14, 0),
		)

	def test_classify_triple_not_enough(self):
		self.assertIsNone(HandClassifier.classify([Card(14, 3), Card(14, 2)]))

	def test_classify_straight(self):
		cards = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
		self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT, 7, 0))

	def test_classify_straight_ace_low(self):
		cards = [Card(14, 0), Card(15, 1), Card(3, 2), Card(4, 3), Card(5, 0)]
		self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT, 5, 0))

	def test_classify_flush(self):
		cards = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
		self.assertEqual(HandClassifier.classify(cards), (CardType.FLUSH, 11, 0))

	def test_classify_full_house(self):
		cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(15, 0), Card(15, 1)]
		self.assertEqual(HandClassifier.classify(cards), (CardType.FULL_HOUSE, 14, 0))

	def test_classify_four_of_a_kind(self):
		cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 1)]
		self.assertEqual(HandClassifier.classify(cards), (CardType.FOUR_OF_A_KIND, 14, 0))

	def test_classify_straight_flush(self):
		cards = [Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)]
		self.assertEqual(HandClassifier.classify(cards), (CardType.STRAIGHT_FLUSH, 7, 0))


@unittest.skipIf(IMPORT_ERROR is not None, "找不到 game.models 或 game.classifier，請在專案根目錄執行測試")
class TestCompare(unittest.TestCase):
	"""測試 HandClassifier.compare 的大小比較邏輯。"""

	def test_compare_single_rank(self):
		self.assertEqual(HandClassifier.compare([Card(14, 3)], [Card(13, 3)]), 1)

	def test_compare_single_suit(self):
		self.assertEqual(HandClassifier.compare([Card(14, 3)], [Card(14, 2)]), 1)

	def test_compare_pair_rank(self):
		play1 = [Card(14, 3), Card(14, 2)]
		play2 = [Card(13, 3), Card(13, 2)]
		self.assertEqual(HandClassifier.compare(play1, play2), 1)

	def test_compare_pair_suit(self):
		play1 = [Card(14, 3), Card(14, 2)]
		play2 = [Card(14, 1), Card(14, 0)]
		self.assertEqual(HandClassifier.compare(play1, play2), 1)

	def test_compare_different_type(self):
		pair_play = [Card(6, 3), Card(6, 1)]
		single_play = [Card(15, 0)]
		self.assertEqual(HandClassifier.compare(pair_play, single_play), 1)

	def test_compare_flush_vs_straight(self):
		flush_play = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
		straight_play = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
		self.assertEqual(HandClassifier.compare(flush_play, straight_play), 1)


@unittest.skipIf(IMPORT_ERROR is not None, "找不到 game.models 或 game.classifier，請在專案根目錄執行測試")
class TestCanPlay(unittest.TestCase):
	"""測試 HandClassifier.can_play 的出牌合法性。"""

	def test_can_play_first_3clubs(self):
		self.assertTrue(HandClassifier.can_play(None, [Card(3, 0)]))

	def test_can_play_first_not_3clubs(self):
		self.assertFalse(HandClassifier.can_play(None, [Card(14, 3)]))

	def test_can_play_same_type(self):
		last_play = [Card(5, 3), Card(5, 2)]
		new_play = [Card(6, 3), Card(6, 2)]
		self.assertTrue(HandClassifier.can_play(last_play, new_play))

	def test_can_play_diff_type(self):
		last_play = [Card(5, 3), Card(5, 2)]
		new_play = [Card(6, 3)]
		self.assertFalse(HandClassifier.can_play(last_play, new_play))

	def test_can_play_not_stronger(self):
		last_play = [Card(10, 3), Card(10, 2)]
		new_play = [Card(5, 3), Card(5, 2)]
		self.assertFalse(HandClassifier.can_play(last_play, new_play))


if __name__ == "__main__":
	unittest.main(verbosity=2)
