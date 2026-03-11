"""
test_q100_hand_typed.py
針對手打程式 q100-Hand-typed.py 的單元測試

由於檔名含連字號無法直接 import，
使用 importlib 動態載入，其餘測試邏輯與 test_q100.py 相同。
"""

import importlib.util
import unittest
from pathlib import Path

# ── 動態載入 q100-Hand-typed.py ──────────────────────────────────────────────
_file = Path(__file__).parent / "q100-Hand-typed.py"
_spec = importlib.util.spec_from_file_location("q100_hand_typed", _file)
_mod  = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

cycle_length       = _mod.cycle_length
max_cycle_in_range = _mod.max_cycle_in_range
solve              = _mod.solve


class TestCycleLength(unittest.TestCase):
    """測試 cycle_length(n)"""

    def test_n_equals_1(self):
        self.assertEqual(cycle_length(1), 1)

    def test_n_equals_2(self):
        self.assertEqual(cycle_length(2), 2)

    def test_n_equals_3(self):
        self.assertEqual(cycle_length(3), 8)

    def test_n_equals_4(self):
        self.assertEqual(cycle_length(4), 3)

    def test_n_equals_5(self):
        self.assertEqual(cycle_length(5), 6)

    def test_n_equals_22(self):
        """題目範例：22 的 cycle-length 應為 16"""
        self.assertEqual(cycle_length(22), 16)

    def test_n_equals_9(self):
        self.assertEqual(cycle_length(9), 20)

    def test_n_large(self):
        """n=27 的 cycle-length 應為 112"""
        self.assertEqual(cycle_length(27), 112)


class TestMaxCycleInRange(unittest.TestCase):
    """測試 max_cycle_in_range(i, j)"""

    def test_range_1_to_10(self):
        self.assertEqual(max_cycle_in_range(1, 10), 20)

    def test_range_100_to_200(self):
        self.assertEqual(max_cycle_in_range(100, 200), 125)

    def test_range_201_to_210(self):
        self.assertEqual(max_cycle_in_range(201, 210), 89)

    def test_range_900_to_1000(self):
        self.assertEqual(max_cycle_in_range(900, 1000), 174)

    def test_reversed_range(self):
        """逆序輸入應與正順序結果相同"""
        self.assertEqual(max_cycle_in_range(10, 1), max_cycle_in_range(1, 10))

    def test_reversed_range_100_200(self):
        self.assertEqual(max_cycle_in_range(200, 100), 125)

    def test_single_element(self):
        self.assertEqual(max_cycle_in_range(22, 22), 16)

    def test_single_element_1(self):
        self.assertEqual(max_cycle_in_range(1, 1), 1)


class TestSolve(unittest.TestCase):
    """測試 solve(input_text) 完整輸入輸出"""

    def test_sample_input(self):
        """題目四組範例"""
        sample_input = "1 10\n100 200\n201 210\n900 1000\n"
        expected     = "1 10 20\n100 200 125\n201 210 89\n900 1000 174"
        self.assertEqual(solve(sample_input), expected)

    def test_single_line(self):
        self.assertEqual(solve("1 10"), "1 10 20")

    def test_reversed_order_in_solve(self):
        """逆序輸入時，輸出保留原始 i j 順序"""
        parts = solve("10 1").split()
        self.assertEqual(parts[0], "10")
        self.assertEqual(parts[1], "1")
        self.assertEqual(int(parts[2]), 20)

    def test_empty_lines_ignored(self):
        result = solve("\n1 10\n\n100 200\n")
        self.assertEqual(result, "1 10 20\n100 200 125")


if __name__ == "__main__":
    unittest.main(verbosity=2)
