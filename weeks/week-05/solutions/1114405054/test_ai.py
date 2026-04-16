"""Phase 4 AI 策略的單元測試。"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


def _prepare_import_path() -> None:
    current = Path(__file__).resolve().parent

    for candidate in [current, *current.parents]:
        if (candidate / "game").is_dir():
            sys.path.insert(0, str(candidate))
            return

        if (candidate / "bigtwo" / "game").is_dir():
            sys.path.insert(0, str(candidate / "bigtwo"))
            return


_prepare_import_path()

from game.ai import AIStrategy
from game.finder import HandFinder
from game.models import Card, Hand


def make_card(rank: int, suit: int) -> Card:
    return Card(rank, suit)


class TestScorePlay(unittest.TestCase):
    def test_score_single(self) -> None:
        hand = Hand([make_card(14, 3), make_card(3, 0)])
        play = [make_card(14, 3)]
        score = AIStrategy.score_play(play, hand)
        self.assertGreaterEqual(score, 240)

    def test_score_pair_higher(self) -> None:
        hand = Hand([make_card(14, 3), make_card(14, 2), make_card(13, 1)])
        single = [make_card(13, 1)]
        pair = [make_card(14, 3), make_card(14, 2)]
        self.assertGreater(AIStrategy.score_play(pair, hand), AIStrategy.score_play(single, hand))

    def test_score_triple_higher(self) -> None:
        hand = Hand([make_card(14, 3), make_card(14, 2), make_card(14, 1), make_card(13, 0)])
        pair = [make_card(14, 3), make_card(14, 2)]
        triple = [make_card(14, 3), make_card(14, 2), make_card(14, 1)]
        self.assertGreater(AIStrategy.score_play(triple, hand), AIStrategy.score_play(pair, hand))

    def test_score_near_empty(self) -> None:
        hand = Hand([make_card(14, 3), make_card(13, 2)])
        play = [make_card(14, 3)]
        self.assertGreater(AIStrategy.score_play(play, hand), 10000)

    def test_score_low_cards(self) -> None:
        hand = Hand([make_card(14, 3), make_card(13, 2), make_card(12, 1), make_card(3, 0)])
        play = [make_card(3, 0)]
        self.assertGreater(AIStrategy.score_play(play, hand), 500)

    def test_score_spade_bonus(self) -> None:
        hand = Hand([make_card(10, 3), make_card(10, 2)])
        spade_play = [make_card(10, 3)]
        non_spade_play = [make_card(10, 2)]
        self.assertGreater(AIStrategy.score_play(spade_play, hand), AIStrategy.score_play(non_spade_play, hand))


class TestSelectBest(unittest.TestCase):
    def test_select_best(self) -> None:
        hand = Hand([make_card(14, 3), make_card(14, 2), make_card(13, 1)])
        valid_plays = [[make_card(13, 1)], [make_card(14, 3), make_card(14, 2)]]
        self.assertEqual(AIStrategy.select_best(valid_plays, hand), [make_card(14, 3), make_card(14, 2)])

    def test_select_first_turn(self) -> None:
        hand = Hand([make_card(3, 0), make_card(14, 3), make_card(13, 2)])
        valid_plays = [[make_card(3, 0)], [make_card(14, 3)]]
        self.assertEqual(AIStrategy.select_best(valid_plays, hand, is_first=True), [make_card(3, 0)])

    def test_select_empty(self) -> None:
        hand = Hand([make_card(14, 3)])
        self.assertIsNone(AIStrategy.select_best([], hand))


class TestAIStrategyFlow(unittest.TestCase):
    def test_ai_always_plays(self) -> None:
        hand = Hand([make_card(6, 3), make_card(7, 1), make_card(3, 0)])
        last_play = [make_card(5, 2)]
        valid_plays = HandFinder.get_all_valid_plays(hand, last_play)
        self.assertTrue(len(valid_plays) > 0)
        best = AIStrategy.select_best(valid_plays, hand)
        self.assertIsNotNone(best)

    def test_ai_prefers_high(self) -> None:
        hand = Hand([make_card(6, 3), make_card(12, 2), make_card(14, 0)])
        last_play = [make_card(5, 2)]
        valid_plays = HandFinder.get_all_valid_plays(hand, last_play)
        self.assertEqual(AIStrategy.select_best(valid_plays, hand), [make_card(14, 0)])

    def test_ai_try_empty(self) -> None:
        hand = Hand([make_card(15, 3)])
        valid_plays = [[make_card(15, 3)]]
        self.assertEqual(AIStrategy.select_best(valid_plays, hand), [make_card(15, 3)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
