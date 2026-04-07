# 題目 10038 的單元測試程式
# 使用 unittest 框架測試 is_jolly_jumper 函數

import unittest
import importlib.util

# 動態載入 10038.py 模組
spec = importlib.util.spec_from_file_location("solution", "10038.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

is_jolly_jumper = solution.is_jolly_jumper

class Test10038(unittest.TestCase):
    """
    測試類別：針對 10038 問題的測試
    """

    def test_jolly_example(self):
        """
        測試 jolly jumper 範例
        """
        sequence = [1, 4, 2, 3]
        self.assertTrue(is_jolly_jumper(sequence))

    def test_not_jolly_example(self):
        """
        測試非 jolly jumper 範例
        """
        sequence = [1, 4, 2, -1, 6]
        self.assertFalse(is_jolly_jumper(sequence))

    def test_single_element(self):
        """
        測試單一元素
        """
        sequence = [5]
        self.assertTrue(is_jolly_jumper(sequence))

    def test_two_elements_jolly(self):
        """
        測試兩個元素 jolly
        """
        sequence = [1, 2]
        self.assertTrue(is_jolly_jumper(sequence))

    def test_two_elements_not_jolly(self):
        """
        測試兩個元素非 jolly
        """
        sequence = [1, 3]
        self.assertFalse(is_jolly_jumper(sequence))

    def test_duplicate_diffs(self):
        """
        測試重複差值
        """
        sequence = [1, 2, 1, 3]
        self.assertFalse(is_jolly_jumper(sequence))

if __name__ == "__main__":
    unittest.main()