from __future__ import annotations

import importlib.util
import pathlib
import unittest

from uva10050 import count_hartal_days, solve_io as solve_main


def _load_easy():
    path = pathlib.Path(__file__).parent / "uva10050-easy.py"
    spec = importlib.util.spec_from_file_location("uva10050_easy_dynamic", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load easy module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


EASY = _load_easy()
count_hartal_days_easy = EASY.count_hartal_days_easy
solve_easy = EASY.solve_io


class TestUVA10050(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(count_hartal_days(14, [3, 4, 8]), 5)

    def test_weekend_excluded(self):
        self.assertEqual(count_hartal_days(7, [6, 7]), 0)

    def test_main_easy_consistency(self):
        cases = [(14, [3, 4, 8]), (30, [2, 3, 4]), (20, [12])]
        for days, params in cases:
            self.assertEqual(count_hartal_days(days, params), count_hartal_days_easy(days, params))

    def test_full_io(self):
        data = "2\n14\n3\n3\n4\n8\n30\n3\n2\n3\n4\n"
        self.assertEqual(solve_main(data), "5\n14")
        self.assertEqual(solve_easy(data), "5\n14")


if __name__ == "__main__":
    unittest.main(verbosity=2)
