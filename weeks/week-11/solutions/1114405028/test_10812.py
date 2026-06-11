"""
UVA 10812 — Beat the Spread! 測試程式
測試用例：給定兩隊分數之和與差，求各隊得分。
"""

import unittest
from solution_10812 import get_scores


class TestBeatTheSpread(unittest.TestCase):
    """測試 Beat the Spread 問題的解決方案。"""

    def test_case_1(self):
        result = get_scores(40, 20)
        self.assertEqual(result, "30 10")

    def test_case_2(self):
        result = get_scores(20, 40)
        self.assertEqual(result, "impossible")

    def test_case_3(self):
        result = get_scores(10, 2)
        self.assertEqual(result, "6 4")

    def test_case_4(self):
        result = get_scores(5, 2)
        self.assertEqual(result, "impossible")

    def test_case_5(self):
        result = get_scores(10, 10)
        self.assertEqual(result, "10 0")

    def test_case_6(self):
        result = get_scores(20, 0)
        self.assertEqual(result, "10 10")

    def test_case_7(self):
        result = get_scores(100, 50)
        self.assertEqual(result, "75 25")


if __name__ == "__main__":
    unittest.main()
