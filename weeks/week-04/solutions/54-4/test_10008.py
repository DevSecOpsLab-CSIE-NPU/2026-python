# 題目 10008 的單元測試程式
# 使用 unittest 框架測試 analyze_text 函數
# 測試案例包括基本情況、邊界情況和排序

import unittest
import importlib.util

# 動態載入 10008.py 模組
spec = importlib.util.spec_from_file_location("solution", "10008.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

analyze_text = solution.analyze_text

class Test10008(unittest.TestCase):
    """
    測試類別：針對 10008 問題的測試
    """

    def test_analyze_text_basic(self):
        """
        測試基本情況：簡單文本
        """
        text = "Hello World"
        expected = [('L', 3), ('O', 2), ('H', 1), ('E', 1), ('W', 1), ('R', 1), ('D', 1)]
        self.assertEqual(analyze_text(text), expected)

    def test_analyze_text_case_insensitive(self):
        """
        測試大小寫不敏感
        """
        text = "AaBbCc"
        expected = [('A', 2), ('B', 2), ('C', 2)]
        self.assertEqual(analyze_text(text), expected)

    def test_analyze_text_with_spaces(self):
        """
        測試包含空白字元
        """
        text = "A B C"
        expected = [('A', 1), ('B', 1), ('C', 1)]
        self.assertEqual(analyze_text(text), expected)

    def test_analyze_text_empty(self):
        """
        測試空文本
        """
        text = ""
        expected = []
        self.assertEqual(analyze_text(text), expected)

    def test_analyze_text_no_letters(self):
        """
        測試無字母的文本
        """
        text = "123!@#"
        expected = []
        self.assertEqual(analyze_text(text), expected)

    def test_analyze_text_complex(self):
        """
        測試複雜文本
        """
        text = "This is a test sentence with some repeated letters."
        result = analyze_text(text)
        # 檢查 T 出現次數最多
        self.assertEqual(result[0][0], 'T')
        self.assertEqual(result[0][1], 4)

if __name__ == "__main__":
    unittest.main()