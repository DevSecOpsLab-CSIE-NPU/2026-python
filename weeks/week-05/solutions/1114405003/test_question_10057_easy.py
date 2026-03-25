"""
QUESTION-10057-easy.py 的單元測試（繁體中文 easy 註解版）

記憶版測試清單：
1) 奇數筆：唯一中位數
2) 偶數筆：中位數區間
3) 重複值：統計範圍內個數
4) solve()：多組 EOF 輸入
"""

from __future__ import annotations

import importlib.util
import pathlib
import unittest


MODULE_PATH = pathlib.Path(__file__).with_name("QUESTION-10057-easy.py")

spec = importlib.util.spec_from_file_location("question_10057_easy", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("無法載入 QUESTION-10057-easy.py")

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TestQuestion10057Easy(unittest.TestCase):
    """測試 easy 版 10057 解法。"""

    def test_odd_count_case(self) -> None:
        # [10,20,30] -> 最佳區間 [20,20]
        self.assertEqual(module.analyze_case([10, 20, 30]), (20, 1, 1))

    def test_even_count_case(self) -> None:
        # [10,20,30,40] -> 最佳區間 [20,30]
        # 範圍內有 20,30 共 2 個；可行 A 共有 11 種（20~30）。
        self.assertEqual(module.analyze_case([10, 20, 30, 40]), (20, 2, 11))

    def test_with_duplicates(self) -> None:
        # [1,2,2,2,3,4] -> 最佳區間 [2,2]
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
