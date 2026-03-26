import unittest

from game.cards import Card, Hand
from game.classifier import CardType, HandClassifier
from game.finder import HandFinder


def C(suit: int, rank: int) -> Card:
    return Card(suit=suit, rank=rank)


class TestFindSingles(unittest.TestCase):
    def test_find_singles(self):
        hand = Hand([C(3, 14), C(0, 3), C(2, 10)])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 3)
        self.assertEqual(singles[0], [C(0, 3)])


class TestFindPairs(unittest.TestCase):
    def test_find_pairs(self):
        hand = Hand([C(0, 7), C(1, 7), C(2, 7), C(3, 9)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 3)
        for p in pairs:
            self.assertEqual(HandClassifier.classify(p)[0], CardType.PAIR)


class TestFindTriples(unittest.TestCase):
    def test_find_triples(self):
        hand = Hand([C(0, 7), C(1, 7), C(2, 7), C(3, 9)])
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 1)
        self.assertEqual(HandClassifier.classify(triples[0])[0], CardType.TRIPLE)


class TestFindStraightFrom(unittest.TestCase):
    def test_find_straight_from_normal(self):
        hand = Hand([C(0, 3), C(1, 4), C(2, 5), C(3, 6), C(0, 7)])
        straight = HandFinder._find_straight_from(hand, 3)
        self.assertIsNotNone(straight)
        self.assertEqual(HandClassifier.classify(straight)[0], CardType.STRAIGHT)

    def test_find_straight_from_ace_low(self):
        hand = Hand([C(0, 14), C(1, 15), C(2, 3), C(3, 4), C(0, 5)])
        straight = HandFinder._find_straight_from(hand, 14)
        self.assertIsNotNone(straight)
        result = HandClassifier.classify(straight)
        self.assertEqual(result[0], CardType.STRAIGHT)
        self.assertEqual(result[1], 5)


class TestFindFives(unittest.TestCase):
    def test_find_fives(self):
        hand = Hand([
            C(0, 3), C(1, 4), C(2, 5), C(3, 6), C(0, 7),
            C(0, 9), C(0, 11), C(0, 13), C(1, 7), C(2, 7),
        ])
        fives = HandFinder.find_fives(hand)
        self.assertTrue(len(fives) >= 1)
        self.assertTrue(all(HandClassifier.classify(f) is not None for f in fives))


class TestGetAllValidPlays(unittest.TestCase):
    def test_get_all_valid_plays_first_turn_contains_3_club(self):
        hand = Hand([C(0, 3), C(1, 5), C(2, 5), C(3, 9)])
        plays = HandFinder.get_all_valid_plays(hand, None)
        self.assertTrue(any(any(c.rank == 3 and c.suit == 0 for c in p) for p in plays))

    def test_get_all_valid_plays_follow_pair(self):
        hand = Hand([C(0, 6), C(1, 6), C(2, 7), C(3, 8)])
        last_play = [C(0, 5), C(1, 5)]
        plays = HandFinder.get_all_valid_plays(hand, last_play)
        self.assertTrue(all(len(p) == 2 for p in plays))
        self.assertTrue(all(HandClassifier.can_play(last_play, p) for p in plays))


if __name__ == "__main__":
    unittest.main()
