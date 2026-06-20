import unittest
from models import Card, Hand, Player
from classifier import HandClassifier, CardType
from finder import HandFinder
from ai import AIStrategy

class TestAIStrategy(unittest.TestCase):
    def test_score_single(self):
        c = Card(14, 3)
        h = Hand([c, Card(3, 0)])
        s = AIStrategy.score_play([c], h)
        self.assertGreater(s, 200)

    def test_score_pair_higher_than_single(self):
        pair = [Card(14, 3), Card(14, 2)]
        single = [Card(14, 3)]
        h = Hand(pair + [Card(3, 0)])
        sp = AIStrategy.score_play(pair, h)
        ss = AIStrategy.score_play(single, h)
        self.assertGreater(sp, ss)

    def test_score_near_empty(self):
        c = Card(14, 3)
        h = Hand([c])
        s = AIStrategy.score_play([c], h)
        self.assertGreater(s, 10000)

    def test_score_spade_bonus(self):
        c = Card(14, 3)
        c2 = Card(13, 2)
        h = Hand([c, c2])
        s = AIStrategy.score_play([c], h)
        s2 = AIStrategy.score_play([c2], h)
        self.assertGreater(s, s2)

    def test_select_best(self):
        h = Hand([Card(3, 0), Card(14, 3)])
        singles = HandFinder.find_singles(h)
        best = AIStrategy.select_best(singles, h)
        self.assertIsNotNone(best)

    def test_select_first_turn(self):
        h = Hand([Card(3, 0), Card(14, 3)])
        singles = HandFinder.find_singles(h)
        best = AIStrategy.select_best(singles, h, is_first=True)
        self.assertEqual(best, [Card(3, 0)])

    def test_select_empty(self):
        best = AIStrategy.select_best([], Hand([]))
        self.assertIsNone(best)

if __name__ == "__main__":
    unittest.main()
