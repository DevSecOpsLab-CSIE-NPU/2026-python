"""
UVA 10922 — 2 the 9s 測試程式
測試用例：判斷是否為 9 的倍數，並計算 9 的深度。
"""

import unittest
from solution_10922 import calculate_nine_degree


class TestNineMultiples(unittest.TestCase):
    """測試 2 the 9s 問題的解決方案。"""

    def test_case_1(self):
        result = calculate_nine_degree("9")
        self.assertEqual(result, ("9-degree of 9 is 1.", 1))

    def test_case_2(self):
        result = calculate_nine_degree("18")
        self.assertEqual(result, ("9-degree of 18 is 1.", 1))

    def test_case_3(self):
        result = calculate_nine_degree("999")
        self.assertEqual(result, ("9-degree of 999 is 2.", 2))

    def test_case_4(self):
        result = calculate_nine_degree("123")
        self.assertEqual(result, ("123 is not a multiple of 9.", 0))

    def test_case_5(self):
        result = calculate_nine_degree("81")
        self.assertEqual(result, ("9-degree of 81 is 1.", 1))

    def test_case_6(self):
        result = calculate_nine_degree("9999999999")
        self.assertTrue("is a multiple of 9" in result[0])
        self.assertGreater(result[1], 0)

    def test_case_7(self):
        result = calculate_nine_degree("100")
        self.assertEqual(result, ("100 is not a multiple of 9.", 0))


if __name__ == "__main__":
    unittest.main()
