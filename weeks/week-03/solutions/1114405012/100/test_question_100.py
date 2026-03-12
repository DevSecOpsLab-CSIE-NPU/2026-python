"""
question_100.py 的單元測試

測試目標：
1. 核心函式 cycle_length 的正確性
2. 區間最大值函式 max_cycle_length_in_range 的正確性
3. 題目輸出格式函式 solve_pair / solve_text 的正確性

所有註解皆為繁體中文，方便複習與教學。
"""

import unittest

from question_100 import (
    cycle_length,
    max_cycle_length_in_range,
    solve_pair,
    solve_text,
    reset_memo,
)


class TestCycleLength(unittest.TestCase):
    """測試單一數字的 cycle length。"""

    def setUp(self) -> None:
        # 每個測試前重設快取，確保測試彼此獨立
        reset_memo()

    def test_base_case(self):
        """n=1 時，長度應為 1。"""
        self.assertEqual(cycle_length(1), 1)

    def test_known_case_22(self):
        """題目範例：22 的長度應為 16。"""
        self.assertEqual(cycle_length(22), 16)

    def test_small_even(self):
        """偶數簡單例：2 -> 1，所以長度是 2。"""
        self.assertEqual(cycle_length(2), 2)

    def test_small_odd(self):
        """奇數簡單例：3 的長度是 8。"""
        self.assertEqual(cycle_length(3), 8)

    def test_invalid_n(self):
        """非正整數應拋出錯誤。"""
        with self.assertRaises(ValueError):
            cycle_length(0)


class TestRangeMax(unittest.TestCase):
    """測試區間最大 cycle length。"""

    def setUp(self) -> None:
        reset_memo()

    def test_uva_sample_1(self):
        self.assertEqual(max_cycle_length_in_range(1, 10), 20)

    def test_uva_sample_2(self):
        self.assertEqual(max_cycle_length_in_range(100, 200), 125)

    def test_uva_sample_3(self):
        self.assertEqual(max_cycle_length_in_range(201, 210), 89)

    def test_uva_sample_4(self):
        self.assertEqual(max_cycle_length_in_range(900, 1000), 174)

    def test_reverse_order(self):
        """輸入順序顛倒時，答案應相同。"""
        self.assertEqual(
            max_cycle_length_in_range(10, 1),
            max_cycle_length_in_range(1, 10),
        )


class TestOutputFormat(unittest.TestCase):
    """測試輸出字串格式。"""

    def setUp(self) -> None:
        reset_memo()

    def test_solve_pair(self):
        self.assertEqual(solve_pair(1, 10), "1 10 20")

    def test_solve_pair_keep_input_order(self):
        """即使內部用 min/max 計算，也要保留原始 i, j 顯示順序。"""
        self.assertEqual(solve_pair(10, 1), "10 1 20")

    def test_solve_text(self):
        raw = "1 10\n100 200\n201 210\n900 1000\n"
        expected = "\n".join([
            "1 10 20",
            "100 200 125",
            "201 210 89",
            "900 1000 174",
        ])
        self.assertEqual(solve_text(raw), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
