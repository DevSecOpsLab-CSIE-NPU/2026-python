"""
QUESTION-10057.py 的單元測試（繁體中文註解）。

測試重點：
1) 奇數筆資料（唯一中位數）
2) 偶數筆資料（中位數區間）
3) 含重複值情境
4) solve() 多組 EOF 輸入格式
"""

from __future__ import annotations

import importlib.util
import pathlib
import unittest


MODULE_PATH = pathlib.Path(__file__).with_name("QUESTION-10057.py")

spec = importlib.util.spec_from_file_location("question_10057", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("無法載入 QUESTION-10057.py")

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TestQuestion10057(unittest.TestCase):
    """測試 UVA 10057 解法。"""

    def test_odd_count_case(self) -> None:
        # 唯一中位數 20，落在 [20,20] 的數量為 1，可行 A 只有 1 種。
        self.assertEqual(module.analyze_case([10, 20, 30]), (20, 1, 1))

    def test_even_count_case(self) -> None:
        # 排序後 [10,20,30,40]，最佳 A 範圍 [20,30]。
        # 範圍內有 20,30 共 2 個，可行 A 有 11 種（20~30）。
        self.assertEqual(module.analyze_case([10, 20, 30, 40]), (20, 2, 11))

    def test_with_duplicates(self) -> None:
        # 排序後 [1,2,2,2,3,4]，最佳 A 範圍 [2,2]。
        self.assertEqual(module.analyze_case([1, 2, 2, 2, 3, 4]), (2, 3, 1))

    def test_solve_multiple_cases(self) -> None:
        raw = """3
10 20 30
4
10 20 30 40
6
1 2 2 2 3 4
"""
        self.assertEqual(module.solve(raw), "20 1 1\n20 2 11\n2 3 1")


if __name__ == "__main__":
    unittest.main()
