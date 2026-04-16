import unittest
from game.models import Card, Hand
from game.classifier import CardType
from game.ai import AIStrategy


def C(rank, suit):
    return Card(rank, suit)


class TestScorePlay(unittest.TestCase):

    def test_score_single(self):
        cards = [C(14, 3)]
        # hand has 5 cards so after playing 1, 4 remain (no near-empty bonus)
        hand = Hand([C(14, 3), C(5, 0), C(6, 0), C(7, 0), C(8, 0)])
        score = AIStrategy.score_play(cards, hand)
        # type=1*100 + rank=14*10 + spade_bonus=5 = 245
        self.assertEqual(score, 1 * 100 + 14 * 10 + 5)

    def test_score_pair_higher(self):
        single = [C(14, 3)]
        pair = [C(14, 3), C(14, 2)]
        hand = Hand([C(14, 3), C(14, 2), C(5, 0)])
        self.assertGreater(AIStrategy.score_play(pair, hand),
                           AIStrategy.score_play(single, hand))

    def test_score_triple_higher(self):
        pair = [C(14, 3), C(14, 2)]
        triple = [C(14, 3), C(14, 2), C(14, 1)]
        hand = Hand([C(14, 3), C(14, 2), C(14, 1), C(5, 0)])
        self.assertGreater(AIStrategy.score_play(triple, hand),
                           AIStrategy.score_play(pair, hand))

    def test_score_near_empty(self):
        cards = [C(14, 3)]
        hand = Hand([C(14, 3)])  # 1 card left -> becomes 0 after play
        score = AIStrategy.score_play(cards, hand)
        self.assertGreater(score, AIStrategy.EMPTY_HAND_BONUS)

    def test_score_low_cards(self):
        cards = [C(14, 3)]
        hand = Hand([C(14, 3), C(5, 0), C(3, 0)])  # 2 left after
        score = AIStrategy.score_play(cards, hand)
        self.assertGreater(score, AIStrategy.NEAR_EMPTY_BONUS)

    def test_score_spade_bonus(self):
        spade = [C(14, 3)]   # ??        club = [C(14, 0)]    # ??        hand = Hand([C(14, 3), C(14, 0), C(5, 1)])
        self.assertGreater(AIStrategy.score_play(spade, hand),
                           AIStrategy.score_play(club, hand))


class TestSelectBest(unittest.TestCase):

    def test_select_best(self):
        single = [C(14, 3)]
        pair = [C(14, 3), C(14, 2)]
        hand = Hand([C(14, 3), C(14, 2), C(5, 0)])
        best = AIStrategy.select_best([single, pair], hand)
        self.assertEqual(len(best), 2)  # pair selected

    def test_select_first_turn(self):
        three_clubs = [C(3, 0)]
        other = [C(14, 3)]
        hand = Hand([C(3, 0), C(14, 3)])
        best = AIStrategy.select_best([three_clubs, other], hand, is_first=True)
        self.assertIsNotNone(best)
        self.assertTrue(any(c.rank == 3 and c.suit == 0 for c in best))

    def test_select_empty(self):
        best = AIStrategy.select_best([], Hand([C(14, 3)]))
        self.assertIsNone(best)


class TestAIStrategy(unittest.TestCase):

    def test_ai_always_plays(self):
        # If there are valid plays, select_best returns one
        plays = [[C(5, 0)], [C(6, 0)], [C(14, 3)]]
        hand = Hand([C(5, 0), C(6, 0), C(14, 3)])
        result = AIStrategy.select_best(plays, hand)
        self.assertIsNotNone(result)

    def test_ai_prefers_high(self):
        low = [C(3, 0)]
        high = [C(14, 3)]
        hand = Hand([C(3, 0), C(14, 3)])
        best = AIStrategy.select_best([low, high], hand)
        # High rank card should score higher
        self.assertEqual(best[0].rank, 14)

    def test_ai_try_empty(self):
        # Playing last card gets EMPTY_HAND_BONUS
        last_card = [C(14, 3)]
        hand = Hand([C(14, 3)])
        score = AIStrategy.score_play(last_card, hand)
        self.assertGreater(score, AIStrategy.EMPTY_HAND_BONUS)


if __name__ == '__main__':
    unittest.main()
