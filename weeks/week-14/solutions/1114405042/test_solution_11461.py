import unittest
import importlib.util
import sys

from solution_11461 import solve as solve_normal

# 動態載入帶有連字號 (hyphen) 的 python 檔案 (solution_11461-easy.py)
spec = importlib.util.spec_from_file_location("solution_11461_easy", "solution_11461-easy.py")
solution_easy = importlib.util.module_from_spec(spec)
sys.modules["solution_11461_easy"] = solution_easy
spec.loader.exec_module(solution_easy)
solve_easy = solution_easy.solve

class TestSquareNumbers(unittest.TestCase):
    def setUp(self):
        # 題目提供的標準測試資料，以 0 0 結尾
        self.sample_input = "1 4\n1 10\n1 100000\n0 0\n"
        self.expected_output = "2\n3\n316\n"
        
        # 自訂的邊界測資
        self.edge_input = "2 4\n10 20\n0 0\n"
        self.edge_expected = "1\n1\n" # 2到4只有4(1個), 10到20只有16(1個)
        
    def test_normal_solution(self):
        """測試標準版解法 (math.ceil 與 math.floor)"""
        self.assertEqual(solve_normal(self.sample_input), self.expected_output)
        self.assertEqual(solve_normal(self.edge_input), self.edge_expected)

    def test_easy_solution(self):
        """測試簡單版解法 (前綴和 int() 差異)"""
        self.assertEqual(solve_easy(self.sample_input), self.expected_output)
        self.assertEqual(solve_easy(self.edge_input), self.edge_expected)

if __name__ == '__main__':
    unittest.main()
