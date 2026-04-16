"""Tests for Big Two hand finder."""

import unittest
from game.models import Card, Hand
from game.finder import HandFinder


class TestHandFinder(unittest.TestCase):
    def test_find_singles(self):
        hand = Hand([Card(3, 0), Card(14, 3)])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 2)

    def test_find_pairs(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 1)

    def test_find_triples(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0)])
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 1)

    def test_get_all_valid_plays_first_turn(self):
        hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2)])
        plays = HandFinder.get_all_valid_plays(hand, None)
        self.assertEqual(len(plays), 1)
        self.assertEqual(plays[0][0].rank, 3)
        self.assertEqual(plays[0][0].suit, 0)


if __name__ == "__main__":
    unittest.main()
