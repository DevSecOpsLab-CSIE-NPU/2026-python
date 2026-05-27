import unittest
import importlib.util
import sys

from solution_12019 import solve as solve_normal

# 動態載入帶有連字號 (hyphen) 的 python 檔案 (solution_12019-easy.py)
spec = importlib.util.spec_from_file_location("solution_12019_easy", "solution_12019-easy.py")
solution_easy = importlib.util.module_from_spec(spec)
sys.modules["solution_12019_easy"] = solution_easy
spec.loader.exec_module(solution_easy)
solve_easy = solution_easy.solve

class TestDoomsday(unittest.TestCase):
    def setUp(self):
        # 準備測資：
        # 2011/1/1 是星期六
        # 2011/4/4 是星期一 (Doomsday 本身)
        # 2011/8/9 是星期二 (8/8 是 Monday, 所以 8/9 是 Tuesday)
        self.sample_input = "3\n1 1\n4 4\n8 9\n"
        self.expected_output = "Saturday\nMonday\nTuesday\n"
        
    def test_normal_solution(self):
        """測試標準解法 (使用 Doomsday 陣列對照與餘數計算)"""
        self.assertEqual(solve_normal(self.sample_input), self.expected_output)

    def test_easy_solution(self):
        """測試簡單版解法 (使用 datetime.date(2011, m, d).strftime('%A'))"""
        self.assertEqual(solve_easy(self.sample_input), self.expected_output)

if __name__ == '__main__':
    unittest.main()
