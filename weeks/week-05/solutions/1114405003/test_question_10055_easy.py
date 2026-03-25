"""
QUESTION-10055-easy.py 的單元測試（繁體中文 easy 註解版）

記憶版測試清單：
1) 基本反轉 + 查詢
2) 同位置反轉兩次 -> 回原狀
3) 單點區間 / 全區間
4) 多步驟整合，確認輸出順序
"""

from __future__ import annotations

import importlib.util
import pathlib
import unittest


MODULE_PATH = pathlib.Path(__file__).with_name("QUESTION-10055-easy.py")

spec = importlib.util.spec_from_file_location("question_10055_easy", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("無法載入 QUESTION-10055-easy.py")

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TestQuestion10055Easy(unittest.TestCase):
    """測試 easy 版 10055 解法。"""

    def test_basic_toggle_and_query(self) -> None:
        # 反轉 f2 後，查 [1,3] 內有 1 個減函數 -> 輸出 1
        raw = """5 2
1 2
2 1 3
"""
        self.assertEqual(module.solve(raw), "1")

    def test_toggle_same_index_twice(self) -> None:
        # 同一點反轉兩次，會回到增函數狀態
        raw = """4 3
1 3
1 3
2 1 4
"""
        self.assertEqual(module.solve(raw), "0")

    def test_single_and_full_range(self) -> None:
        # 反轉 f1 與 f4
        # [1,1] 有 1 個減 -> 1
        # [1,4] 有 2 個減 -> 0
        raw = """4 4
1 1
1 4
2 1 1
2 1 4
"""
        self.assertEqual(module.solve(raw), "1\n0")

    def test_multi_queries_order(self) -> None:
        # 驗證多次操作下，答案順序與內容都正確
        raw = """6 7
2 1 6
1 2
2 1 6
1 5
2 2 5
1 2
2 1 3
"""
        self.assertEqual(module.solve(raw), "0\n1\n0\n0")


if __name__ == "__main__":
    unittest.main()
