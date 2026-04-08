"""10071 單元測試。

會同時驗證正式版、easy 版與手打版，
並用暴力法比對小型測資的正確性。
"""

from __future__ import annotations

import importlib.util
import random
import unittest
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load_module(filename: str):
    path = ROOT / filename
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def build_input(values):
    return str(len(values)) + "\n" + "\n".join(map(str, values)) + "\n"


def brute_force(values):
    count = 0
    for a, b, c, d, e, f in product(values, repeat=6):
        if a + b + c + d + e == f:
            count += 1
    return str(count)


class Test10071(unittest.TestCase):
    def setUp(self):
        self.normal = load_module("10071.py")
        self.easy = load_module("10071-easy.py")
        self.hand = load_module("10071-hand.py")

    def assert_all(self, values):
        text = build_input(values)
        expected = brute_force(values)
        self.assertEqual(self.normal.solve(text), expected)
        self.assertEqual(self.easy.solve(text), expected)
        self.assertEqual(self.hand.solve(text), expected)

    def test_small_cases(self):
        self.assert_all([0])
        self.assert_all([1, 2])
        self.assert_all([-2, 0, 3])

    def test_random_cases(self):
        random.seed(10071)
        for _ in range(20):
            values = random.sample(range(-5, 6), 4)
            self.assert_all(values)

    def test_empty_input(self):
        self.assertEqual(self.normal.solve(""), "")
        self.assertEqual(self.easy.solve(""), "")
        self.assertEqual(self.hand.solve(""), "")


if __name__ == "__main__":
    unittest.main()