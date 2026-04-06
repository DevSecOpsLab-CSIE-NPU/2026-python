import unittest

from game.finder import HandFinder
from game.models import Card, Hand


class TestFinder(unittest.TestCase):
    def test_find_singles(self):
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        self.assertEqual(len(HandFinder.find_singles(hand)), 3)

    def test_find_pairs(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(13, 3), Card(13, 0)])
        self.assertEqual(len(HandFinder.find_pairs(hand)), 2)

    def test_find_triples(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0)])
        self.assertEqual(len(HandFinder.find_triples(hand)), 1)

    def test_find_fives(self):
        hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0), Card(14, 3)])
        fives = HandFinder.find_fives(hand)
        self.assertTrue(len(fives) >= 1)

    def test_get_all_valid_plays_first(self):
        hand = Hand([Card(3, 0), Card(14, 3)])
        plays = HandFinder.get_all_valid_plays(hand, None)
        self.assertEqual(plays, [[Card(3, 0)]])


if __name__ == "__main__":
    unittest.main()
