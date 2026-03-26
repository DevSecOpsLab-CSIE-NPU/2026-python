import unittest

from game.cards import Card, Hand
from game.ai import AIStrategy


def C(suit: int, rank: int) -> Card:
    return Card(suit=suit, rank=rank)


class TestAIScore(unittest.TestCase):
    def setUp(self) -> None:
        self.ai = AIStrategy()

    def test_score_single(self):
        hand = Hand([C(3, 14), C(0, 5)])
        play = [C(3, 14)]
        score = self.ai._score_play(play, hand)
        self.assertEqual(score, 245)

    def test_score_pair_higher(self):
        hand = Hand([C(0, 9), C(1, 9), C(2, 4)])
        single_score = self.ai._score_play([C(2, 4)], hand)
        pair_score = self.ai._score_play([C(0, 9), C(1, 9)], hand)
        self.assertGreater(pair_score, single_score)

    def test_score_triple_higher(self):
        hand = Hand([C(0, 8), C(1, 8), C(2, 8), C(3, 7)])
        pair_score = self.ai._score_play([C(0, 8), C(1, 8)], hand)
        triple_score = self.ai._score_play([C(0, 8), C(1, 8), C(2, 8)], hand)
        self.assertGreater(triple_score, pair_score)

    def test_score_near_empty(self):
        hand = Hand([C(3, 13)])
        play = [C(3, 13)]
        score = self.ai._score_play(play, hand)
        self.assertGreater(score, 10000)

    def test_score_low_cards(self):
        hand = Hand([C(0, 6), C(1, 6)])
        play = [C(0, 6), C(1, 6)]
        score = self.ai._score_play(play, hand)
        self.assertGreater(score, 500)

    def test_score_spade_bonus(self):
        hand = Hand([C(3, 10), C(2, 10)])
        spade_score = self.ai._score_play([C(3, 10)], hand)
        non_spade_score = self.ai._score_play([C(2, 10)], hand)
        self.assertGreaterEqual(spade_score, non_spade_score + 5)


class TestAISelectBest(unittest.TestCase):
    def setUp(self) -> None:
        self.ai = AIStrategy()

    def test_select_best(self):
        hand = Hand([C(0, 6), C(1, 6), C(2, 4)])
        valid_plays = [[C(2, 4)], [C(0, 6), C(1, 6)]]
        best = self.ai._select_best_play(valid_plays, hand)
        self.assertEqual(best, [C(0, 6), C(1, 6)])

    def test_select_first_turn(self):
        hand = Hand([C(0, 3), C(3, 14), C(1, 7)])
        best = self.ai.select_play(hand, last_play=None, is_first_turn=True)
        self.assertEqual(best, [C(0, 3)])

    def test_select_empty(self):
        hand = Hand([C(2, 9)])
        best = self.ai._select_best_play([], hand)
        self.assertIsNone(best)


class TestAIStrategyIntegration(unittest.TestCase):
    def setUp(self) -> None:
        self.ai = AIStrategy()

    def test_ai_always_plays(self):
        hand = Hand([C(0, 3), C(1, 5), C(2, 5)])
        play = self.ai.select_play(hand, last_play=None, is_first_turn=True)
        self.assertIsNotNone(play)

    def test_ai_prefers_high(self):
        hand = Hand([C(0, 8), C(1, 11), C(2, 6), C(3, 3)])
        play = self.ai.select_play(hand, last_play=[C(0, 7)], is_first_turn=False)
        self.assertIsNotNone(play)
        self.assertEqual(len(play), 1)
        self.assertEqual(play[0].rank, 11)

    def test_ai_try_empty(self):
        hand = Hand([C(1, 9)])
        play = self.ai.select_play(hand, last_play=None, is_first_turn=False)
        self.assertEqual(play, [C(1, 9)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
