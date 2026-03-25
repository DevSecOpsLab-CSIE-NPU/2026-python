"""
QUESTION-10055.py 的單元測試（繁體中文註解）。

測試策略：
1) 基本流程：反轉 + 查詢
2) 同一位置反轉兩次應回復
3) 邊界區間與單點區間
4) 多操作整合，驗證輸出順序與正確性
"""

from __future__ import annotations

import importlib.util
import pathlib
import unittest


MODULE_PATH = pathlib.Path(__file__).with_name("QUESTION-10055.py")

spec = importlib.util.spec_from_file_location("question_10055", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("無法載入 QUESTION-10055.py")

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TestQuestion10055(unittest.TestCase):
    """測試 10055 解法是否符合題意。"""

    def test_basic_toggle_and_query(self) -> None:
        # N=5, 全增開始
        # 反轉 f2 後，查 [1,3] 會有 1 個減函數 -> 輸出 1
        raw = """5 2
1 2
2 1 3
"""
        self.assertEqual(module.solve(raw), "1")

    def test_toggle_same_index_twice(self) -> None:
        # 同一位置反轉兩次，狀態應回到原本（增函數）。
        raw = """4 3
1 3
1 3
2 1 4
"""
        self.assertEqual(module.solve(raw), "0")

    def test_single_point_and_full_range(self) -> None:
        # 反轉 f1 與 f4，
        # [1,1] -> 1（奇數）
        # [1,4] -> 2（偶數）
        raw = """4 4
1 1
1 4
2 1 1
2 1 4
"""
        self.assertEqual(module.solve(raw), "1\n0")

    def test_multiple_queries_order(self) -> None:
        raw = """6 7
2 1 6
1 2
2 1 6
1 5
2 2 5
1 2
2 1 3
"""
        # 初始 [1,6] 全增 -> 0
        # 反轉 2 後 [1,6] -> 1
        # 再反轉 5 後 [2,5] 有兩個減 -> 0
        # 再反轉 2 後 [1,3] 只剩全增 -> 0
        self.assertEqual(module.solve(raw), "0\n1\n0\n0")


if __name__ == "__main__":
    unittest.main()
