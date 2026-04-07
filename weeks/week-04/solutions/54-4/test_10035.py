# 題目 10035 的單元測試程式
# 使用 unittest 框架測試 count_carry_operations 函數

import unittest
import importlib.util

# 動態載入 10035.py 模組
spec = importlib.util.spec_from_file_location("solution", "10035.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

count_carry_operations = solution.count_carry_operations

class Test10035(unittest.TestCase):
    """
    測試類別：針對 10035 問題的測試
    """

    def test_no_carry(self):
        """
        測試無進位
        """
        self.assertEqual(count_carry_operations(123, 456), 0)

    def test_one_carry(self):
        """
        測試一次進位
        """
        self.assertEqual(count_carry_operations(5, 5), 1)

    def test_multiple_carry(self):
        """
        測試多次進位
        """
        self.assertEqual(count_carry_operations(999, 1), 3)

    def test_different_lengths(self):
        """
        測試不同長度
        """
        self.assertEqual(count_carry_operations(99, 1), 1)

    def test_zero(self):
        """
        測試包含0
        """
        self.assertEqual(count_carry_operations(0, 0), 0)

if __name__ == "__main__":
    unittest.main()