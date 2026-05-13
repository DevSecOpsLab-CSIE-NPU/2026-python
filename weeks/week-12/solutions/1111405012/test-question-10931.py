"""測試 UVA 10931 - Parity。"""

from __future__ import annotations

import unittest

from test_support import load_module


module = load_module("question-10931.py")


class ParityTest(unittest.TestCase):
    def test_one_has_one_bit(self) -> None:
        # 正常情況：1 的二進位只有一個 1。
        self.assertEqual(module.describe_number(
            1), "The parity of 1 is 1 (mod 2).")

    def test_ten_has_two_ones(self) -> None:
        # 正常情況：10 轉為二進位後有兩個 1。
        self.assertEqual(module.describe_number(
            10), "The parity of 1010 is 2 (mod 2).")

    def test_zero_is_terminator_not_output(self) -> None:
        # 邊界情況：0 是結束符號，但單獨函式仍可被安全處理。
        self.assertEqual(module.format_binary_parity(0), ("0", 0))


if __name__ == "__main__":
    unittest.main()
