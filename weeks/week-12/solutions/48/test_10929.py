"""
UVA 10929 測試程式
測試用例：判斷超大數字（最多1000位）是否為11的倍數
"""

import unittest
from solution_10929 import is_multiple_of_11


class TestMultipleOf11(unittest.TestCase):
    """測試超大數字是否為11的倍數"""

    def test_case_1(self):
        """測試用例 1: 11 => 是11的倍數"""
        result = is_multiple_of_11("11")
        self.assertEqual(result, "11 is a multiple of 11.")

    def test_case_2(self):
        """測試用例 2: 22 => 是11的倍數"""
        result = is_multiple_of_11("22")
        self.assertEqual(result, "22 is a multiple of 11.")

    def test_case_3(self):
        """測試用例 3: 121 => 是11的倍數 (奇數位=1+1=2, 偶數位=2, 差=0)"""
        result = is_multiple_of_11("121")
        self.assertEqual(result, "121 is a multiple of 11.")

    def test_case_4(self):
        """測試用例 4: 123 => 不是11的倍數"""
        result = is_multiple_of_11("123")
        self.assertEqual(result, "123 is not a multiple of 11.")

    def test_case_5(self):
        """測試用例 5: 1 => 不是11的倍數"""
        result = is_multiple_of_11("1")
        self.assertEqual(result, "1 is not a multiple of 11.")

    def test_case_6(self):
        """測試用例 6: 99 => 是11的倍數"""
        result = is_multiple_of_11("99")
        self.assertEqual(result, "99 is a multiple of 11.")

    def test_case_7(self):
        """測試用例 7: 1001 => 是11的倍數"""
        result = is_multiple_of_11("1001")
        self.assertEqual(result, "1001 is a multiple of 11.")


if __name__ == "__main__":
    unittest.main()
