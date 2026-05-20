"""
Unit tests for Problem 11150

包含數個基礎測試，驗證壓縮與 DP 的正確性。
"""
import unittest
from problem_11150 import solve_one, process


class Test11150(unittest.TestCase):
    def test_no_stones(self):
        # 若無石子，可直接跳過 -> 0
        self.assertEqual(solve_one(10, 2, 3, []), 0)

    def test_single_stone_avoidable(self):
        # 石子在 3，S=2,T=3，可跳過 => 0
        self.assertEqual(solve_one(5, 2, 3, [3]), 0)

    def test_sample_process(self):
        # 測試 process 多組輸入格式
        inp = "10 2 3 0\n"
        self.assertEqual(process(inp).strip(), "0")


if __name__ == '__main__':
    unittest.main()
