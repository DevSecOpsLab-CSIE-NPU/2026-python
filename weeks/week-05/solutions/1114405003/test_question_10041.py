"""
UVA 10041 單元測試（對應 QUESTION-10041.py）

測試重點：
1) 核心函式 min_total_distance 是否正確
2) 整體輸入輸出函式 solve 是否符合題目格式
3) 包含重複門牌與偶數/奇數筆資料等情境
"""

from __future__ import annotations

import importlib.util
import pathlib
import unittest


# 由於原始檔名含有連字號（-），無法直接使用 import 語法，
# 因此改用 importlib 依「檔案路徑」動態載入模組。
MODULE_PATH = pathlib.Path(__file__).with_name("QUESTION-10041.py")

spec = importlib.util.spec_from_file_location("question_10041", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("無法載入 QUESTION-10041.py")

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TestQuestion10041(unittest.TestCase):
    """測試 UVA 10041 的解法。"""

    def test_odd_count_addresses(self) -> None:
        # 奇數個門牌：中位數唯一，最小總距離可直接驗算
        self.assertEqual(module.min_total_distance([2, 4, 6]), 4)

    def test_even_count_addresses(self) -> None:
        # 偶數個門牌：中間兩個位置都能達到相同最小值
        self.assertEqual(module.min_total_distance([2, 4, 6, 8]), 8)

    def test_duplicate_addresses(self) -> None:
        # 題目提到門牌可能重複，需確認演算法可正確處理
        self.assertEqual(module.min_total_distance([10, 10, 10, 20]), 10)

    def test_multi_case_input_output(self) -> None:
        # 多組資料格式測試：驗證 solve() 是否輸出逐行答案
        raw = """2
2 2 4
3 2 4 6
"""
        self.assertEqual(module.solve(raw), "2\n4")


if __name__ == "__main__":
    unittest.main()
