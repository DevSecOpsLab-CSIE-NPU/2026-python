import unittest
import importlib.util
import sys

from solution_11417 import solve as solve_normal

# 動態載入帶有連字號 (hyphen) 的 python 檔案 (solution_11417-easy.py)
spec = importlib.util.spec_from_file_location("solution_11417_easy", "solution_11417-easy.py")
solution_easy = importlib.util.module_from_spec(spec)
sys.modules["solution_11417_easy"] = solution_easy
spec.loader.exec_module(solution_easy)
solve_easy = solution_easy.solve

class TestGCD(unittest.TestCase):
    def setUp(self):
        # 題目提供的標準測試資料，以 0 結尾
        self.sample_input = "10\n100\n500\n0\n"
        self.expected_output = "67\n13015\n442011\n"
        
    def test_normal_solution(self):
        """測試一般版本的解法 (雙重迴圈)"""
        result = solve_normal(self.sample_input)
        self.assertEqual(result, self.expected_output)

    def test_easy_solution(self):
        """測試簡單版本的解法 (itertools + sum)"""
        result = solve_easy(self.sample_input)
        self.assertEqual(result, self.expected_output)

if __name__ == '__main__':
    unittest.main()
