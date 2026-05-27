"""11349 的單元測試。

這份測試同時驗證：
1. 題目範例可正常輸出。
2. 負數會直接判定為非對稱。
3. 單一元素矩陣的基本邏輯。
"""

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


solution = load_module("11349.py", "solution_11349")
solution_easy = load_module("11349-easy.py", "solution_11349_easy")


class Test11349(unittest.TestCase):
    def test_sample_input(self) -> None:
        """題目提供的範例輸入應該要得到相同輸出。"""

        sample_input = """\
2
N = 3
5 1 3
2 0 2
3 1 5
N = 3
5 1 3
2 0 2
0 1 5
"""
        expected = "Test #1: Symmetric.\nTest #2: Non-symmetric."
        self.assertEqual(solution.solve(sample_input), expected)
        self.assertEqual(solution_easy.solve(sample_input), expected)

    def test_negative_value_is_not_symmetric(self) -> None:
        """只要出現負數，就不符合題目第一個條件。"""

        matrix = [[1, 2], [2, -1]]
        self.assertFalse(solution.is_symmetric_matrix(matrix))
        self.assertFalse(solution_easy.is_symmetric_matrix(matrix))

    def test_single_cell_positive_matrix(self) -> None:
        """1x1 而且是非負數時，答案應該是對稱。"""

        matrix = [[7]]
        self.assertTrue(solution.is_symmetric_matrix(matrix))
        self.assertTrue(solution_easy.is_symmetric_matrix(matrix))


if __name__ == "__main__":
    unittest.main()