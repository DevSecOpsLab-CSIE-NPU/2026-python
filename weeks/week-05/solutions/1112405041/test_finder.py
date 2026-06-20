import unittest
from models import Card, Hand
from classifier import HandClassifier
from finder import HandFinder

class TestHandFinder(unittest.TestCase):
    def test_find_singles(self):
        h = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        singles = HandFinder.find_singles(h)
        self.assertEqual(len(singles), 3)

    def test_find_singles_empty(self):
        self.assertEqual(len(HandFinder.find_singles(Hand([]))), 0)

    def test_find_pairs_one(self):
        h = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        pairs = HandFinder.find_pairs(h)
        self.assertEqual(len(pairs), 1)

    def test_find_pairs_two(self):
        h = Hand([Card(14, 3), Card(14, 2), Card(13, 0), Card(13, 1)])
        pairs = HandFinder.find_pairs(h)
        self.assertEqual(len(pairs), 2)

    def test_find_pairs_none(self):
        h = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        pairs = HandFinder.find_pairs(h)
        self.assertEqual(len(pairs), 0)

    def test_find_triples_one(self):
        h = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0)])
        triples = HandFinder.find_triples(h)
        self.assertEqual(len(triples), 1)

    def test_find_straight(self):
        h = Hand([Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0), Card(14, 3)])
        fives = HandFinder.find_fives(h)
        self.assertTrue(any(
            HandClassifier.classify(p)[0].value == 4 for p in fives
        ))

    def test_first_turn(self):
        h = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
        plays = HandFinder.get_all_valid_plays(h, None)
        for p in plays:
            self.assertTrue(any(c.rank == 3 and c.suit == 0 for c in p))

    def test_with_last_single(self):
        h = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        plays = HandFinder.get_all_valid_plays(h, [Card(5, 0)])
        for p in plays:
            self.assertEqual(len(p), 1)
            r = HandClassifier.classify(p)
            r2 = HandClassifier.classify([Card(5, 0)])
            self.assertIsNotNone(r)
            self.assertIsNotNone(r2)
            self.assertGreater(r[1], r2[1])

    def test_no_valid(self):
        h = Hand([Card(3, 0), Card(4, 1)])
        plays = HandFinder.get_all_valid_plays(h, [Card(14, 3)])
        self.assertEqual(len(plays), 0)

if __name__ == "__main__":
    unittest.main()
