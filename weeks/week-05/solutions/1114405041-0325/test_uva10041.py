"""UVA 10041 單元測試。

測試重點：
1. 驗證主解法（中位數）結果正確。
2. 驗證 -easy 版本（枚舉）結果正確。
3. 比對兩版本在同一組資料上的一致性。
4. 驗證整體 I/O 解析流程。
"""

from __future__ import annotations

import importlib.util
import pathlib
import unittest

from uva10041 import minimum_total_distance, solve_io as solve_main


def _load_easy_module():
    """動態載入檔名含 '-' 的 easy 模組。"""
    current_dir = pathlib.Path(__file__).parent
    easy_path = current_dir / "uva10041-easy.py"

    spec = importlib.util.spec_from_file_location("uva10041_easy_dynamic", easy_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("無法載入 uva10041-easy.py")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


EASY_MODULE = _load_easy_module()
minimum_total_distance_easy = EASY_MODULE.minimum_total_distance_easy
solve_easy = EASY_MODULE.solve_io


class TestUVA10041(unittest.TestCase):
    """針對 UVA 10041 的功能測試。"""

    def test_sample_case_main(self):
        # 經典範例：最佳位置在 2，總距離 = 2
        self.assertEqual(minimum_total_distance([1, 2, 3]), 2)

    def test_sample_case_easy(self):
        self.assertEqual(minimum_total_distance_easy([1, 2, 3]), 2)

    def test_even_count_addresses(self):
        # 偶數筆資料時，中間區間任一點都可達到最小值。
        addresses = [2, 4, 6, 8]
        self.assertEqual(minimum_total_distance(addresses), 8)
        self.assertEqual(minimum_total_distance_easy(addresses), 8)

    def test_duplicate_addresses(self):
        # 有重複地址時也要正確處理。
        addresses = [10, 10, 10, 20]
        self.assertEqual(minimum_total_distance(addresses), 10)
        self.assertEqual(minimum_total_distance_easy(addresses), 10)

    def test_main_and_easy_consistency(self):
        # 比對兩版本在多組資料上的一致性。
        cases = [
            [1, 2, 3, 4, 5],
            [7, 7, 7],
            [1, 100, 200, 300],
            [5, 2, 9, 2, 8, 10],
        ]
        for addresses in cases:
            self.assertEqual(
                minimum_total_distance(addresses),
                minimum_total_distance_easy(addresses),
            )

    def test_full_io_main(self):
        input_data = "2\n3 1 2 3\n4 2 4 6 8\n"
        expected = "2\n8"
        self.assertEqual(solve_main(input_data), expected)

    def test_full_io_easy(self):
        input_data = "2\n3 1 2 3\n4 2 4 6 8\n"
        expected = "2\n8"
        self.assertEqual(solve_easy(input_data), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
