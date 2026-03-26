import unittest
from p1_models import Card
from p2_classifier import HandClassifier, CardType


class TestPair(unittest.TestCase):
    def test_pair(self):
        result = HandClassifier.classify([Card(14, 3), Card(14, 2)])
        self.assertEqual(result, (CardType.PAIR, 14, 3))


class TestSingle(unittest.TestCase):
    def test_single(self):
        result = HandClassifier.classify([Card(14, 3)])
        self.assertEqual(result, (CardType.SINGLE, 14, 3))


class TestCompare(unittest.TestCase):
    def test_compare_pair(self):
        self.assertEqual(
            HandClassifier.compare(
                [Card(14, 3), Card(14, 2)],
                [Card(13, 3), Card(13, 2)]
            ),
            1
        )


class TestCanPlay(unittest.TestCase):
    def test_first_move(self):
        self.assertTrue(HandClassifier.can_play(None, [Card(3, 0)]))


if __name__ == "__main__":
    unittest.main(verbosity=2)