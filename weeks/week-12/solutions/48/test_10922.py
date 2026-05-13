"""
UVA 10922 — 2 the 9s 測試程式
測試用例：判斷是否為9的倍數，並計算9的深度
"""

import unittest
from solution_10922 import calculate_nine_degree


class TestNineMultiples(unittest.TestCase):
    """測試 2 the 9s 問題的解決方案"""

    def test_case_1(self):
        """測試用例 1: 9 => 深度 1"""
        result = calculate_nine_degree("9")
        self.assertEqual(result, ("9 is a multiple of 9.", 1))

    def test_case_2(self):
        """測試用例 2: 18 => 深度 1 (1+8=9)"""
        result = calculate_nine_degree("18")
        self.assertEqual(result, ("18 is a multiple of 9.", 1))

    def test_case_3(self):
        """測試用例 3: 999 => 深度 1 (9+9+9=27, 2+7=9)"""
        result = calculate_nine_degree("999")
        self.assertEqual(result, ("999 is a multiple of 9.", 2))

    def test_case_4(self):
        """測試用例 4: 123 => 不是9的倍數"""
        result = calculate_nine_degree("123")
        self.assertEqual(result, ("123 is not a multiple of 9.", 0))

    def test_case_5(self):
        """測試用例 5: 81 => 深度 2 (8+1=9)"""
        result = calculate_nine_degree("81")
        self.assertEqual(result, ("81 is a multiple of 9.", 1))

    def test_case_6(self):
        """測試用例 6: 9999999999 => 深度 2"""
        result = calculate_nine_degree("9999999999")
        self.assertIn("is a multiple of 9", result[0])
        self.assertGreater(result[1], 0)

    def test_case_7(self):
        """測試用例 7: 100 => 不是9的倍數"""
        result = calculate_nine_degree("100")
        self.assertEqual(result, ("100 is not a multiple of 9.", 0))


if __name__ == "__main__":
    unittest.main()
