"""11417 的單元測試。"""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent


def load_module(filename: str, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, BASE_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


solution = load_module("11417.py", "solution_11417")
solution_easy = load_module("11417-easy.py", "solution_11417_easy")


class Test11417(unittest.TestCase):
    def test_sample_input(self) -> None:
        """題目範例輸入要回傳對應的三筆答案。"""

        sample_input = """\
10
100
500
0
"""
        expected = "67\n13015\n442011"
        self.assertEqual(solution.solve(sample_input), expected)
        self.assertEqual(solution_easy.solve(sample_input), expected)

    def test_small_limit(self) -> None:
        """N = 2 時只有一組 (1, 2)，gcd 會是 1。"""

        self.assertEqual(solution.sum_gcd_pairs(2), 1)
        self.assertEqual(solution_easy.sum_gcd_pairs(2), 1)

    def test_medium_limit(self) -> None:
        """再確認一個較小的中間值，避免索引錯誤。"""

        self.assertEqual(solution.sum_gcd_pairs(10), 67)
        self.assertEqual(solution_easy.sum_gcd_pairs(10), 67)


if __name__ == "__main__":
    unittest.main()