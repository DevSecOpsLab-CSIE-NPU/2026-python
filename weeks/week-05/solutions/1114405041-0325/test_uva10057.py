from __future__ import annotations

import importlib.util
import pathlib
import unittest

from uva10057 import analyze_medians, solve_io as solve_main


def _load_easy():
    path = pathlib.Path(__file__).parent / "uva10057-easy.py"
    spec = importlib.util.spec_from_file_location("uva10057_easy_dynamic", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load easy module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


EASY = _load_easy()
analyze_medians_easy = EASY.analyze_medians_easy
solve_easy = EASY.solve_io


class TestUVA10057(unittest.TestCase):
    def test_odd_count(self):
        self.assertEqual(analyze_medians([1, 2, 3]), (2, 1, 1))
        self.assertEqual(analyze_medians_easy([1, 2, 3]), (2, 1, 1))

    def test_even_count(self):
        self.assertEqual(analyze_medians([1, 2, 3, 4]), (2, 2, 2))
        self.assertEqual(analyze_medians_easy([1, 2, 3, 4]), (2, 2, 2))

    def test_duplicates(self):
        self.assertEqual(analyze_medians([1, 2, 2, 2, 9]), (2, 3, 1))
        self.assertEqual(analyze_medians_easy([1, 2, 2, 2, 9]), (2, 3, 1))

    def test_full_io(self):
        data = "3\n1 2 3\n4\n1 2 3 4\n5\n1 2 2 2 9\n"
        expected = "2 1 1\n2 2 2\n2 3 1"
        self.assertEqual(solve_main(data), expected)
        self.assertEqual(solve_easy(data), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
