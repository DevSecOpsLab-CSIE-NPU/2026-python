"""
針對 QUESTION-10041-easy.py 的 unittest。

因為檔名含有連字號（-），不能直接用一般 import，
所以使用 importlib 依路徑動態載入模組。
"""

from __future__ import annotations

import importlib.util
import pathlib
import unittest


BASE_DIR = pathlib.Path(__file__).parent
EASY_PATH = BASE_DIR / "QUESTION-10041-easy.py"
DEFAULT_PATH = BASE_DIR / "QUESTION-10041.py"

# 優先載入 -easy 檔名；若不存在，退回目前常用檔名 QUESTION-10041.py。
MODULE_PATH = EASY_PATH if EASY_PATH.exists() else DEFAULT_PATH

spec = importlib.util.spec_from_file_location("question_10041_easy", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"無法載入解答檔：{MODULE_PATH.name}")

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TestQuestion10041Easy(unittest.TestCase):
    """測試核心函式與整體 I/O。"""

    def test_min_total_distance_odd_count(self) -> None:
        # 奇數筆：中位數唯一
        self.assertEqual(module.min_total_distance([2, 4, 6]), 4)

    def test_min_total_distance_even_count(self) -> None:
        # 偶數筆：中間兩個任一點都會是最小值
        self.assertEqual(module.min_total_distance([2, 4, 6, 8]), 8)

    def test_with_duplicate_addresses(self) -> None:
        # 題目說明：門牌可重複
        self.assertEqual(module.min_total_distance([10, 10, 10, 20]), 10)

    def test_solve_multi_case_input(self) -> None:
        # 驗證多組輸入輸出格式
        raw = """2
2 2 4
3 2 4 6
"""
        self.assertEqual(module.solve(raw), "2\n4")


if __name__ == "__main__":
    unittest.main()
