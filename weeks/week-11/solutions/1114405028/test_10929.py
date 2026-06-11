"""
UVA 10929 測試程式
測試用例：判斷超大數字是否為 11 的倍數。
"""

import unittest
from solution_10929 import is_multiple_of_11


class TestMultipleOf11(unittest.TestCase):
    """測試 11 的倍數判斷功能。"""

    def test_case_1(self):
        self.assertEqual(is_multiple_of_11("11"), "11 is a multiple of 11.")

    def test_case_2(self):
        self.assertEqual(is_multiple_of_11("22"), "22 is a multiple of 11.")

    def test_case_3(self):
        self.assertEqual(is_multiple_of_11("121"), "121 is a multiple of 11.")

    def test_case_4(self):
        self.assertEqual(is_multiple_of_11("123"), "123 is not a multiple of 11.")

    def test_case_5(self):
        self.assertEqual(is_multiple_of_11("1"), "1 is not a multiple of 11.")

    def test_case_6(self):
        self.assertEqual(is_multiple_of_11("99"), "99 is a multiple of 11.")

    def test_case_7(self):
        self.assertEqual(is_multiple_of_11("1001"), "1001 is a multiple of 11.")


if __name__ == "__main__":
    unittest.main()
