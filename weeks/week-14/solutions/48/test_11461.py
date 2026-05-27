"""11461 的單元測試。"""

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


solution = load_module("11461.py", "solution_11461")
solution_easy = load_module("11461-easy.py", "solution_11461_easy")


class Test11461(unittest.TestCase):
    def test_sample_input(self) -> None:
        """題目範例要輸出 2、3、316。"""

        sample_input = """\
1 4
1 10
1 100000
0 0
"""
        expected = "2\n3\n316"
        self.assertEqual(solution.solve(sample_input), expected)
        self.assertEqual(solution_easy.solve(sample_input), expected)

    def test_single_square_number(self) -> None:
        """區間只包含 16 時，答案就是 1。"""

        self.assertEqual(solution.count_square_numbers(16, 16), 1)
        self.assertEqual(solution_easy.count_square_numbers(16, 16), 1)

    def test_no_square_number(self) -> None:
        """區間沒有完全平方數時，答案應該是 0。"""

        self.assertEqual(solution.count_square_numbers(2, 3), 0)
        self.assertEqual(solution_easy.count_square_numbers(2, 3), 0)


if __name__ == "__main__":
    unittest.main()