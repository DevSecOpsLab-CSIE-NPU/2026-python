"""
UVA 11005 - Cheapest Base 的 unit test。

測試重點：
1. 驗證 0 的特殊情況
2. 驗證單一 base 的成本計算
3. 驗證多個 base 成本相同時會全部列出
4. 驗證完整輸入輸出格式

這份測試會同時覆蓋標準版與 easy 版，確保兩份程式結果一致。
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load_module(module_name: str, filename: str):
    """從指定檔案動態載入模組，避免檔名中含有連字號時無法直接 import。"""

    module_path = ROOT / filename
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"無法載入模組：{module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


solution = load_module("solution_11005", "11005.py")
easy_solution = load_module("solution_11005_easy", "11005-easy.py")


class CheapestBaseTestCase(unittest.TestCase):
    """針對 Cheapest Base 題目的核心行為做單元測試。"""

    def test_zero_cost_uses_digit_zero_only(self):
        """數字 0 只能印出單一個 0，因此成本應該直接等於 costs[0]。"""

        costs = list(range(36))
        self.assertEqual(solution.digit_costs_for_base(0, 2, costs), 0)
        self.assertEqual(easy_solution.calc_cost(0, 36, costs), 0)

    def test_cost_calculation_for_specific_base(self):
        """檢查某個固定數字在特定進位下的拆位加總是否正確。"""

        costs = [1] * 36
        costs[0] = 5
        costs[1] = 2
        costs[2] = 7
        # 10(十進位) = 1010(二進位)，成本 = 2 + 5 + 2 + 5 = 14
        self.assertEqual(solution.digit_costs_for_base(10, 2, costs), 14)
        self.assertEqual(easy_solution.calc_cost(10, 2, costs), 14)

    def test_tie_bases_are_all_returned(self):
        """當多個 base 成本相同時，應全部輸出且保持遞增順序。"""

        costs = [0] * 36
        expected = list(range(2, 37))
        self.assertEqual(solution.cheapest_bases(12345, costs), expected)
        self.assertEqual(easy_solution.find_best_bases(12345, costs), expected)

    def test_solve_single_case_output(self):
        """驗證完整輸入格式與輸出字串是否符合題目規定。"""

        costs = [0] * 36
        input_data = "\n".join(
            [
                "1",
                " ".join(map(str, costs)),
                "2",
                "0",
                "10",
            ]
        ) + "\n"

        expected = (
            "Case 1:\n"
            "Cheapest base(s) for number 0: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36\n"
            "Cheapest base(s) for number 10: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36"
        )

        self.assertEqual(solution.solve(input_data.split()), expected)

    def test_easy_and_standard_versions_match(self):
        """同一組輸入下，標準版與 easy 版應產生完全相同的結果。"""

        costs = [3] * 36
        costs[0] = 1
        costs[1] = 2
        costs[2] = 4

        # 這組資料不一定需要特定的人工答案，重點是兩個版本的核心邏輯要一致。
        for number in [1, 2, 36, 255, 2026]:
            with self.subTest(number=number):
                self.assertEqual(
                    solution.cheapest_bases(number, costs),
                    easy_solution.find_best_bases(number, costs),
                )


if __name__ == "__main__":
    unittest.main()