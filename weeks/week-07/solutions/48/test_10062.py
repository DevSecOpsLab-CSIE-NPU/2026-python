"""10062 單元測試。

這份測試會同時驗證正式版、easy 版與手打版，
確認三個版本都能把「位置前面較小數字的數量」正確還原成排列。
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


def build_input_from_permutation(perm):
    # 依照題意計算每個位置前面有幾個較小的數字。
    counts = [0]
    for i in range(1, len(perm)):
        smaller = 0
        for j in range(i):
            if perm[j] < perm[i]:
                smaller += 1
        counts.append(smaller)
    return str(len(perm)) + "\n" + "\n".join(map(str, counts[1:])) + ("\n" if len(perm) > 1 else "")


class Test10062(unittest.TestCase):
    def setUp(self):
        self.normal = load_module("10062.py")
        self.easy = load_module("10062-easy.py")
        self.hand = load_module("10062-hand.py")

    def assert_solution(self, perm):
        input_text = build_input_from_permutation(perm)
        expected = "\n".join(map(str, perm))
        self.assertEqual(self.normal.solve(input_text), expected)
        self.assertEqual(self.easy.solve(input_text), expected)
        self.assertEqual(self.hand.solve(input_text), expected)

    def test_small_examples(self):
        self.assert_solution([1, 2])
        self.assert_solution([2, 1, 3])
        self.assert_solution([3, 1, 2, 4])

    def test_random_permutations(self):
        random.seed(10062)
        for n in range(2, 8):
            for _ in range(30):
                perm = list(range(1, n + 1))
                random.shuffle(perm)
                self.assert_solution(perm)

    def test_empty_input(self):
        self.assertEqual(self.normal.solve(""), "")
        self.assertEqual(self.easy.solve(""), "")
        self.assertEqual(self.hand.solve(""), "")


if __name__ == "__main__":
    unittest.main()