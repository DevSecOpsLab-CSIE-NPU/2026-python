"""
第三題 任意進位的數字根 - 測試檔案
學號: 1114405003
base = 3 (個位查對照表)
"""
import unittest
from digit_root import digit_root, to_base, sum_digits


class TestDigitRoot(unittest.TestCase):
    """數字根測試"""

    def test_sample_0(self):
        """範例: 0 -> 0"""
        self.assertEqual(digit_root(0, 3), 0)

    def test_sample_8(self):
        """範例: 8 -> 2"""
        self.assertEqual(digit_root(8, 3), 2)

    def test_sample_63(self):
        """範例: 63 -> 1"""
        self.assertEqual(digit_root(63, 3), 1)

    def test_single_digit(self):
        """一位數直接返回"""
        # 5 in base 3: 12 -> 1+2=3 -> 10 -> 1+0=1
        self.assertEqual(digit_root(5, 3), 1)

    def test_base_2(self):
        """base=2 測試"""
        self.assertEqual(digit_root(7, 2), 1)

    def test_base_8(self):
        """base=8 測試: 8 -> 1"""
        self.assertEqual(digit_root(8, 8), 1)

    def test_large_number(self):
        """大數測試"""
        # 10^9 in base 3 digit root = 2
        self.assertEqual(digit_root(10**9, 3), 2)

    def test_to_base_conversion(self):
        """進位轉換測試"""
        self.assertEqual(to_base(8, 3), [2, 2])
        self.assertEqual(to_base(63, 3), [2, 1, 0, 0])

    def test_sum_digits(self):
        """位數相加測試"""
        self.assertEqual(sum_digits([2, 2], 3), 4)
        self.assertEqual(sum_digits([2, 1, 0, 0], 3), 3)

    def test_edge_case_1(self):
        """edge case: x=1"""
        self.assertEqual(digit_root(1, 3), 1)

    def test_edge_case_base_16(self):
        """edge case: base=16"""
        self.assertEqual(digit_root(255, 16), 15)

    def test_edge_case_exact_single_digit_in_base(self):
        """刚好在 base 下是一位數"""
        self.assertEqual(digit_root(2, 3), 2)

    def test_repeated_sum(self):
        """需要多次相加"""
        # 100 in base 3: 10201 -> 1+0+2+0+1=4 -> 11 -> 1+1=2
        self.assertEqual(digit_root(100, 3), 2)


if __name__ == "__main__":
    unittest.main()
