# -*- coding: utf-8 -*-
import unittest
from digit_root import digit_root

class TestDigitRoot(unittest.TestCase):
    """數字根單元測試"""

    def test_basic_cases(self):
        """基本案例測試"""
        self.assertEqual(digit_root(24), 6)   # 2+4=6
        self.assertEqual(digit_root(199), 1)  # 1+9+9=19 -> 1+9=10 -> 1+0=1
        self.assertEqual(digit_root(9999), 9) # 9+9+9+9=36 -> 3+6=9
        self.assertEqual(digit_root(5), 5)    # 已是一位數

    def test_edge_cases(self):
        """邊界案例測試"""
        self.assertEqual(digit_root(1), 1)
        self.assertEqual(digit_root(2000000000), 2) # 2+0...=2

    def test_invalid_input(self):
        """例外行為測試 (n < 1)"""
        with self.assertRaisesRegex(ValueError, "n must be >= 1"):
            digit_root(0)
        with self.assertRaises(ValueError):
            digit_root(-10)

if __name__ == "__main__":
    unittest.main()

