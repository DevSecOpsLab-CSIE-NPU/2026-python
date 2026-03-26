"""Phase 3 牌型搜尋測試（HandFinder）。

使用方式（在專案根目錄執行）：
    python -m unittest tests.test_finder -v

預期被測模組位置：
    game/finder.py
"""

from __future__ import annotations

import importlib
import unittest

try:
    _models = importlib.import_module("game.models")
    _finder = importlib.import_module("game.finder")
    _classifier = importlib.import_module("game.classifier")
except ModuleNotFoundError as exc:
    raise unittest.SkipTest("找不到 game.models / game.finder / game.classifier，請先完成實作") from exc

Card = _models.Card
Hand = _models.Hand
HandFinder = _finder.HandFinder
CardType = _classifier.CardType
HandClassifier = _classifier.HandClassifier


class TestFindSingles(unittest.TestCase):
    """單張搜尋測試。"""

    def test_find_singles(self) -> None:
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 3)
        self.assertTrue(all(len(x) == 1 for x in singles))

    def test_find_singles_empty(self) -> None:
        hand = Hand([])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 0)


class TestFindPairs(unittest.TestCase):
    """對子搜尋測試。"""

    def test_find_pairs_one(self) -> None:
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 1)
        self.assertEqual(HandClassifier.classify(pairs[0]), (CardType.PAIR, 14, 0))

    def test_find_pairs_two(self) -> None:
        hand = Hand([Card(14, 3), Card(14, 2), Card(13, 3), Card(13, 0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 2)

    def test_find_pairs_none(self) -> None:
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 0)


class TestFindTriples(unittest.TestCase):
    """三條搜尋測試。"""

    def test_find_triples_one(self) -> None:
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0)])
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 1)
        self.assertEqual(HandClassifier.classify(triples[0]), (CardType.TRIPLE, 14, 0))

    def test_find_triples_with_extra(self) -> None:
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 3), Card(13, 0)])
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 1)


class TestFindFives(unittest.TestCase):
    """五張牌型搜尋測試。"""

    def test_find_straight(self) -> None:
        hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0), Card(14, 3)])
        fives = HandFinder.find_fives(hand)
        kinds = {HandClassifier.classify(x)[0] for x in fives if HandClassifier.classify(x) is not None}
        self.assertIn(CardType.STRAIGHT, kinds)

    def test_find_flush(self) -> None:
        hand = Hand([Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0), Card(14, 3)])
        fives = HandFinder.find_fives(hand)
        kinds = {HandClassifier.classify(x)[0] for x in fives if HandClassifier.classify(x) is not None}
        self.assertIn(CardType.FLUSH, kinds)

    def test_find_full_house(self) -> None:
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 3), Card(13, 0), Card(3, 0)])
        fives = HandFinder.find_fives(hand)
        kinds = {HandClassifier.classify(x)[0] for x in fives if HandClassifier.classify(x) is not None}
        self.assertIn(CardType.FULL_HOUSE, kinds)

    def test_find_four_of_a_kind(self) -> None:
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 0), Card(5, 1)])
        fives = HandFinder.find_fives(hand)
        kinds = {HandClassifier.classify(x)[0] for x in fives if HandClassifier.classify(x) is not None}
        self.assertIn(CardType.FOUR_OF_A_KIND, kinds)

    def test_find_straight_flush(self) -> None:
        hand = Hand([Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0), Card(14, 3)])
        fives = HandFinder.find_fives(hand)
        kinds = {HandClassifier.classify(x)[0] for x in fives if HandClassifier.classify(x) is not None}
        self.assertIn(CardType.STRAIGHT_FLUSH, kinds)


class TestValidPlays(unittest.TestCase):
    """合法出牌搜尋測試。"""

    def test_first_turn(self) -> None:
        hand = Hand([Card(3, 0), Card(14, 3), Card(5, 2)])
        plays = HandFinder.get_all_valid_plays(hand, None)
        self.assertEqual(plays, [[Card(3, 0)]])

    def test_with_last_single(self) -> None:
        hand = Hand([Card(4, 0), Card(5, 1), Card(8, 3), Card(10, 2)])
        last_play = [Card(5, 0)]
        plays = HandFinder.get_all_valid_plays(hand, last_play)
        self.assertTrue(all(len(p) == 1 for p in plays))
        self.assertTrue(all(HandClassifier.can_play(last_play, p) for p in plays))

    def test_with_last_pair(self) -> None:
        hand = Hand([Card(6, 3), Card(6, 2), Card(7, 3), Card(7, 2), Card(3, 0)])
        last_play = [Card(5, 3), Card(5, 2)]
        plays = HandFinder.get_all_valid_plays(hand, last_play)
        self.assertTrue(all(len(p) == 2 for p in plays))
        self.assertTrue(all(HandClassifier.can_play(last_play, p) for p in plays))

    def test_no_valid(self) -> None:
        hand = Hand([Card(3, 0), Card(4, 1), Card(7, 2)])
        last_play = [Card(15, 3)]  # 上家出 ♠2
        plays = HandFinder.get_all_valid_plays(hand, last_play)
        self.assertEqual(plays, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
