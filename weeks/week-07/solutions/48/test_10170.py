"""10170 單元測試。

會同時驗證正式版、easy 版與手打版，
並用直接模擬旅館入住流程的小資料做比對。
"""

from __future__ import annotations

import importlib.util
import random
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load_module(filename: str):
    path = ROOT / filename
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def build_input(pairs):
    lines = [f"{start} {day}" for start, day in pairs]
    return "\n".join(lines) + "\n"


def brute_force(start: int, day: int) -> int:
    total = 0
    people = start
    while True:
        total += people
        if day <= total:
            return people
        people += 1


class Test10170(unittest.TestCase):
    def setUp(self):
        self.normal = load_module("10170.py")
        self.easy = load_module("10170-easy.py")
        self.hand = load_module("10170-hand.py")

    def assert_all(self, pairs):
        text = build_input(pairs)
        expected = "\n".join(str(brute_force(start, day)) for start, day in pairs)
        self.assertEqual(self.normal.solve(text), expected)
        self.assertEqual(self.easy.solve(text), expected)
        self.assertEqual(self.hand.solve(text), expected)

    def test_small_cases(self):
        self.assert_all([(1, 1)])
        self.assert_all([(4, 1), (4, 4), (4, 5), (4, 9), (4, 10)])

    def test_random_cases(self):
        random.seed(10170)
        pairs = []
        for _ in range(10):
            start = random.randint(1, 20)
            day = random.randint(1, 500)
            pairs.append((start, day))
        self.assert_all(pairs)

    def test_empty_input(self):
        self.assertEqual(self.normal.solve(""), "")
        self.assertEqual(self.easy.solve(""), "")
        self.assertEqual(self.hand.solve(""), "")


if __name__ == "__main__":
    unittest.main()