# 題目 10041 的單元測試程式
# 使用 unittest 框架測試 calculate_min_distance 函數
# 測試案例包括基本情況、邊界情況和多組資料

import unittest
from io import StringIO
import sys
import importlib.util

# 動態載入 10041.py 模組
spec = importlib.util.spec_from_file_location("solution", "10041.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

calculate_min_distance = solution.calculate_min_distance
main = solution.main

class Test10041(unittest.TestCase):
    """
    測試類別：針對 10041 問題的測試
    """

    def test_calculate_min_distance_basic(self):
        """
        測試基本情況：奇數個地址
        """
        addresses = [1, 3, 5]
        self.assertEqual(calculate_min_distance(addresses), 4)

    def test_calculate_min_distance_even(self):
        """
        測試偶數個地址
        """
        addresses = [1, 2, 3, 4]
        self.assertEqual(calculate_min_distance(addresses), 4)

    def test_calculate_min_distance_single(self):
        """
        測試單一個地址
        """
        addresses = [10]
        self.assertEqual(calculate_min_distance(addresses), 0)

    def test_calculate_min_distance_duplicates(self):
        """
        測試有重複地址的情況
        """
        addresses = [2, 2, 2]
        self.assertEqual(calculate_min_distance(addresses), 0)

    def test_calculate_min_distance_empty(self):
        """
        測試空列表
        """
        addresses = []
        self.assertEqual(calculate_min_distance(addresses), 0)

    def test_main_function(self):
        """
        測試主函數
        """
        input_data = "1\n3\n1\n3\n5\n"
        expected_output = "4\n"

        old_stdin = sys.stdin
        old_stdout = sys.stdout
        sys.stdin = StringIO(input_data)
        sys.stdout = StringIO()

        try:
            main()
            output = sys.stdout.getvalue()
            self.assertEqual(output, expected_output)
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout

if __name__ == '__main__':
    # 運行測試並輸出結果
    unittest.main(verbosity=2)