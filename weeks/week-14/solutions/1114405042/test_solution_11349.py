import unittest
import importlib.util
import sys

from solution_11349 import solve as solve_normal

# 動態載入帶有連字號 (hyphen) 的 python 檔案 (solution_11349-easy.py)
spec = importlib.util.spec_from_file_location("solution_11349_easy", "solution_11349-easy.py")
solution_easy = importlib.util.module_from_spec(spec)
sys.modules["solution_11349_easy"] = solution_easy
spec.loader.exec_module(solution_easy)
solve_easy = solution_easy.solve

class TestSymmetricMatrix(unittest.TestCase):
    def setUp(self):
        # 題目提供的標準測試資料
        self.sample_input = "2\nN = 3\n5 1 3\n2 0 2\n3 1 5\nN = 3\n5 1 3\n2 0 2\n0 1 5\n"
        self.expected_output = "Test #1: Symmetric.\nTest #2: Non-symmetric.\n"
        
        # 邊界測試資料：含有負數的狀況，對稱矩陣條件是元素必須大於等於 0
        self.negative_input = "1\nN = 2\n-1 2\n2 -1\n"
        self.negative_expected = "Test #1: Non-symmetric.\n"
        
    def test_normal_solution(self):
        """測試一般版本的解法 (利用 2D 矩陣檢查)"""
        self.assertEqual(solve_normal(self.sample_input), self.expected_output)
        self.assertEqual(solve_normal(self.negative_input), self.negative_expected)

    def test_easy_solution(self):
        """測試簡單版本的解法 (利用 1D 陣列反轉檢查)"""
        self.assertEqual(solve_easy(self.sample_input), self.expected_output)
        self.assertEqual(solve_easy(self.negative_input), self.negative_expected)

if __name__ == '__main__':
    unittest.main()
