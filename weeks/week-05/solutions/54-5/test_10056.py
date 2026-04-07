import os
import unittest
import importlib.util

here = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("solution", os.path.join(here, "10056.py"))
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

player_win_probability = solution.player_win_probability


class Test10056(unittest.TestCase):
    def assertFloatAlmostEqual(self, value, expected):
        self.assertAlmostEqual(value, expected, places=6)

    def test_first_player_simple(self):
        self.assertFloatAlmostEqual(player_win_probability(3, 0.5, 1), 0.5714285714285714)

    def test_second_player(self):
        self.assertFloatAlmostEqual(player_win_probability(3, 0.5, 2), 0.2857142857142857)

    def test_last_player(self):
        self.assertFloatAlmostEqual(player_win_probability(3, 0.5, 3), 0.14285714285714285)

    def test_small_probability(self):
        self.assertFloatAlmostEqual(player_win_probability(4, 0.2, 3), 0.21680216802168029)

    def test_zero_probability(self):
        self.assertFloatAlmostEqual(player_win_probability(4, 0.0, 2), 0.0)


if __name__ == "__main__":
    unittest.main()
