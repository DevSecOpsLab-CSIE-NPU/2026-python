# 題目 10019 的單元測試程式
# 使用 unittest 框架測試 calculate_difference 函數

import unittest
import importlib.util

# 動態載入 10019.py 模組
spec = importlib.util.spec_from_file_location("solution", "10019.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

calculate_difference = solution.calculate_difference

class Test10019(unittest.TestCase):
    """
    測試類別：針對 10019 問題的測試
    """

    def test_calculate_difference_positive(self):
        """
        測試 a > b
        """
        self.assertEqual(calculate_difference(10, 5), 5)

    def test_calculate_difference_negative(self):
        """
        測試 a < b
        """
        self.assertEqual(calculate_difference(5, 10), 5)

    def test_calculate_difference_equal(self):
        """
        測試 a == b
        """
        self.assertEqual(calculate_difference(10, 10), 0)

    def test_calculate_difference_large_numbers(self):
        """
        測試大數字
        """
        self.assertEqual(calculate_difference(1000000, 500000), 500000)

if __name__ == "__main__":
    unittest.main()