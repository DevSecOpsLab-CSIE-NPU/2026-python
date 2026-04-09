# 測試題目 10101: 移動木棒的單元測試

import unittest
from question_10101 import solve_equation

class TestEquation(unittest.TestCase):
    def test_case_1(self):
        expr = "1+1=2#"
        expected = "1+1=2#"
        self.assertEqual(solve_equation(expr), expected)

    def test_case_2(self):
        # 假設 "5=5#", 但需要等式
        expr = "5-3=2#"
        expected = "5-3=2#"
        self.assertEqual(solve_equation(expr), expected)

    def test_no_solution(self):
        expr = "1+1=3#"
        expected = "No"
        self.assertEqual(solve_equation(expr), expected)

if __name__ == '__main__':
    unittest.main()