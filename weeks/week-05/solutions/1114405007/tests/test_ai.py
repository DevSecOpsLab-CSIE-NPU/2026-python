"""Phase 4 AI 策略測試（AIStrategy）。

使用方式（在專案根目錄執行）：
    python -m unittest tests.test_ai -v

預期被測模組位置：
    game/ai.py
"""

from __future__ import annotations

import importlib
import unittest

try:
    _models = importlib.import_module("game.models")
    _ai = importlib.import_module("game.ai")
    _finder = importlib.import_module("game.finder")
except ModuleNotFoundError as exc:
    raise unittest.SkipTest("找不到 game.models / game.ai / game.finder，請先完成實作") from exc

Card = _models.Card
Hand = _models.Hand
AIStrategy = _ai.AIStrategy
HandFinder = _finder.HandFinder


class TestScorePlay(unittest.TestCase):
    """評分函數測試。"""

    def test_score_single(self) -> None:
        # 單張評分：1*100 + 14*10 = 240（再加花色與其餘加分）
        hand = Hand([Card(14, 3), Card(3, 0)])
        score = AIStrategy.score_play([Card(14, 3)], hand)
        self.assertGreaterEqual(score, 240)

    def test_score_pair_higher(self) -> None:
        hand = Hand([Card(10, 3), Card(10, 2), Card(9, 1)])
        pair_score = AIStrategy.score_play([Card(10, 3), Card(10, 2)], hand)
        single_score = AIStrategy.score_play([Card(10, 3)], hand)
        self.assertGreater(pair_score, single_score)

    def test_score_triple_higher(self) -> None:
        hand = Hand([Card(8, 3), Card(8, 2), Card(8, 1), Card(7, 0)])
        triple_score = AIStrategy.score_play([Card(8, 3), Card(8, 2), Card(8, 1)], hand)
        pair_score = AIStrategy.score_play([Card(8, 3), Card(8, 2)], hand)
        self.assertGreater(triple_score, pair_score)

    def test_score_near_empty(self) -> None:
        # 若出牌後手牌剩 1 張，應有大幅加分
        hand = Hand([Card(5, 3), Card(6, 0)])
        score = AIStrategy.score_play([Card(5, 3)], hand)
        self.assertGreater(score, 10000)

    def test_score_low_cards(self) -> None:
        # 若出牌後剩牌 <= 3，應有 near-empty 加分
        hand = Hand([Card(5, 3), Card(6, 0), Card(7, 1), Card(8, 2)])
        score = AIStrategy.score_play([Card(5, 3)], hand)
        self.assertGreater(score, 500)

    def test_score_spade_bonus(self) -> None:
        hand = Hand([Card(9, 3), Card(9, 2), Card(3, 0)])
        spade_score = AIStrategy.score_play([Card(9, 3)], hand)
        heart_score = AIStrategy.score_play([Card(9, 2)], hand)
        self.assertGreaterEqual(spade_score, heart_score + 5)


class TestSelectBest(unittest.TestCase):
    """最佳選擇測試。"""

    def test_select_best(self) -> None:
        hand = Hand([Card(14, 3), Card(14, 2), Card(9, 1)])
        single = [Card(14, 3)]
        pair = [Card(14, 3), Card(14, 2)]
        best = AIStrategy.select_best([single, pair], hand)
        self.assertEqual(best, pair)

    def test_select_first_turn(self) -> None:
        hand = Hand([Card(3, 0), Card(14, 3), Card(14, 2)])
        valid = [[Card(3, 0)], [Card(14, 3)]]
        best = AIStrategy.select_best(valid, hand, is_first=True)
        self.assertEqual(best, [Card(3, 0)])

    def test_select_empty(self) -> None:
        hand = Hand([Card(3, 0)])
        best = AIStrategy.select_best([], hand)
        self.assertIsNone(best)


class TestAIStrategyIntegration(unittest.TestCase):
    """完整策略測試。"""

    def test_ai_always_plays(self) -> None:
        hand = Hand([Card(6, 3), Card(8, 1), Card(10, 0)])
        last_play = [Card(5, 0)]
        valid = HandFinder.get_all_valid_plays(hand, last_play)
        best = AIStrategy.select_best(valid, hand)
        self.assertIsNotNone(best)

    def test_ai_prefers_high(self) -> None:
        hand = Hand([Card(8, 0), Card(9, 1), Card(11, 3)])
        last_play = [Card(7, 2)]
        valid = HandFinder.get_all_valid_plays(hand, last_play)
        best = AIStrategy.select_best(valid, hand)
        self.assertEqual(best, [Card(11, 3)])

    def test_ai_try_empty(self) -> None:
        # 只剩最後一張可出時，應直接出完
        hand = Hand([Card(14, 3)])
        last_play = [Card(13, 3)]
        valid = HandFinder.get_all_valid_plays(hand, last_play)
        best = AIStrategy.select_best(valid, hand)
        self.assertEqual(best, [Card(14, 3)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
