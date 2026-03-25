from __future__ import annotations

import importlib.util
import pathlib
import unittest

from uva10056 import solve_io as solve_main, winning_probability


def _load_easy():
    path = pathlib.Path(__file__).parent / "uva10056-easy.py"
    spec = importlib.util.spec_from_file_location("uva10056_easy_dynamic", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load easy module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


EASY = _load_easy()
winning_probability_easy = EASY.winning_probability_easy
solve_easy = EASY.solve_io


class TestUVA10056(unittest.TestCase):
    def test_zero_probability(self):
        self.assertEqual(winning_probability(10, 0.0, 3), 0.0)
        self.assertEqual(winning_probability_easy(10, 0.0, 3), 0.0)

    def test_known_case(self):
        # n=3, p=0.5, i=2 -> 0.285714...
        self.assertAlmostEqual(winning_probability(3, 0.5, 2), 0.2857142857, places=8)
        self.assertAlmostEqual(winning_probability_easy(3, 0.5, 2), 0.2857142857, places=8)

    def test_consistency(self):
        cases = [(3, 0.5, 2), (10, 0.1, 1), (5, 0.25, 4)]
        for n, p, i in cases:
            self.assertAlmostEqual(winning_probability(n, p, i), winning_probability_easy(n, p, i), places=10)

    def test_full_io(self):
        data = "3\n3 0.5 2\n10 0.1 1\n10 0.0 3\n"
        expected = "0.2857\n0.1535\n0.0000"
        self.assertEqual(solve_main(data), expected)
        self.assertEqual(solve_easy(data), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
