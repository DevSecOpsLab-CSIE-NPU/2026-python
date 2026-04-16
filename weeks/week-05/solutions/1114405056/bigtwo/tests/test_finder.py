import unittest
from game.models import Card, Hand
from game.finder import HandFinder
from game.classifier import HandClassifier, CardType


def C(rank, suit):
    return Card(rank, suit)


class TestFindSingles(unittest.TestCase):

    def test_find_singles(self):
        h = Hand([C(14, 3), C(13, 2), C(3, 0)])
        result = HandFinder.find_singles(h)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(len(p) == 1 for p in result))

    def test_find_singles_empty(self):
        h = Hand([])
        result = HandFinder.find_singles(h)
        self.assertEqual(len(result), 0)


class TestFindPairs(unittest.TestCase):

    def test_find_pairs_one(self):
        h = Hand([C(14, 3), C(14, 2), C(3, 0)])
        result = HandFinder.find_pairs(h)
        self.assertEqual(len(result), 1)

    def test_find_pairs_two(self):
        h = Hand([C(14, 3), C(14, 2), C(13, 3), C(13, 2)])
        result = HandFinder.find_pairs(h)
        self.assertEqual(len(result), 2)

    def test_find_pairs_none(self):
        h = Hand([C(14, 3), C(13, 2), C(3, 0)])
        result = HandFinder.find_pairs(h)
        self.assertEqual(len(result), 0)


class TestFindTriples(unittest.TestCase):

    def test_find_triples_one(self):
        h = Hand([C(14, 3), C(14, 2), C(14, 1), C(3, 0)])
        result = HandFinder.find_triples(h)
        self.assertEqual(len(result), 1)

    def test_find_triples_with_extra(self):
        h = Hand([C(14, 3), C(14, 2), C(14, 1), C(13, 3), C(13, 2)])
        result = HandFinder.find_triples(h)
        self.assertEqual(len(result), 1)  # only 3 Aces


class TestFindFives(unittest.TestCase):

    def test_find_straight(self):
        h = Hand([C(3, 0), C(4, 1), C(5, 2), C(6, 3), C(7, 0)])
        result = HandFinder.find_fives(h)
        types = [HandClassifier.classify(p)[0] for p in result]
        self.assertIn(CardType.STRAIGHT, types)

    def test_find_flush(self):
        h = Hand([C(3, 0), C(5, 0), C(7, 0), C(9, 0), C(11, 0)])
        result = HandFinder.find_fives(h)
        types = [HandClassifier.classify(p)[0] for p in result]
        self.assertIn(CardType.FLUSH, types)

    def test_find_full_house(self):
        h = Hand([C(14, 3), C(14, 2), C(14, 1), C(13, 3), C(13, 2)])
        result = HandFinder.find_fives(h)
        types = [HandClassifier.classify(p)[0] for p in result]
        self.assertIn(CardType.FULL_HOUSE, types)

    def test_find_four_of_a_kind(self):
        h = Hand([C(14, 3), C(14, 2), C(14, 1), C(14, 0), C(3, 0)])
        result = HandFinder.find_fives(h)
        types = [HandClassifier.classify(p)[0] for p in result]
        self.assertIn(CardType.FOUR_OF_A_KIND, types)

    def test_find_straight_flush(self):
        h = Hand([C(3, 0), C(4, 0), C(5, 0), C(6, 0), C(7, 0)])
        result = HandFinder.find_fives(h)
        types = [HandClassifier.classify(p)[0] for p in result]
        self.assertIn(CardType.STRAIGHT_FLUSH, types)


class TestGetAllValidPlays(unittest.TestCase):

    def test_first_turn(self):
        # Hand has 3♣; last=None -> only plays containing 3♣
        h = Hand([C(3, 0), C(14, 3), C(14, 2)])
        result = HandFinder.get_all_valid_plays(h, None)
        self.assertTrue(len(result) > 0)
        for play in result:
            self.assertTrue(any(c.rank == 3 and c.suit == 0 for c in play))

    def test_with_last_single(self):
        last = [C(5, 0)]
        h = Hand([C(6, 0), C(14, 3)])
        result = HandFinder.get_all_valid_plays(h, last)
        self.assertTrue(all(len(p) == 1 for p in result))

    def test_with_last_pair(self):
        last = [C(5, 0), C(5, 1)]
        h = Hand([C(6, 0), C(6, 1), C(14, 3)])
        result = HandFinder.get_all_valid_plays(h, last)
        self.assertTrue(all(len(p) == 2 for p in result))

    def test_no_valid(self):
        last = [C(15, 3)]  # highest single
        h = Hand([C(3, 0), C(4, 1)])
        result = HandFinder.get_all_valid_plays(h, last)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
