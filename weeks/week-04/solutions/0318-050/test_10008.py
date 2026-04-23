import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_10008.py 中
# 並且您的解答會提供一個 analyze_crypto(lines) 函式：
# 它接收一個包含多行字串的串列 (list of str)，並回傳一個包含分析結果的串列 (list of str)
# 回傳格式預期為 ["字母 次數", "字母 次數", ...]
from solution_10008 import analyze_crypto

class TestUVA10008(unittest.TestCase):
    
    def test_basic_counting_and_sorting(self):
        """
        基礎測試：驗證基本的字元統計以及雙重排序邏輯。
        測試中 'A' 出現 3 次，'B' 出現 2 次，'C' 出現 2 次。
        預期輸出必須先按次數降冪 (3 -> 2)，次數相同的 B 和 C 則按字母順序升冪排列。
        """
        lines = ["A B C A A B C"]
        expected = [
            "A 3",
            "B 2",
            "C 2"
        ]
        self.assertEqual(analyze_crypto(lines), expected)

    def test_case_insensitivity(self):
        """
        大小寫不敏感測試：
        題目要求大小寫視為相同字元 (例如 'a' 和 'A' 是一樣的)，
        且最終輸出必須統一轉換為大寫。
        """
        lines = ["aAaA bB"]
        # 'A' 總共 4 次 (a, A, a, A)，'B' 總共 2 次 (b, B)
        expected = [
            "A 4",
            "B 2"
        ]
        self.assertEqual(analyze_crypto(lines), expected)

    def test_ignore_non_alphabet(self):
        """
        過濾字元測試：
        題目要求只統計英文字母，必須忽略所有的空白、數字以及標點符號。
        且未出現的字母不應該出現在輸出中。
        """
        lines = [
            "Hello, World! 123",
            "Python 3.10???"
        ]
        # 統計上述字串中的字母：
        # O: 3次, L: 3次, H: 2次, T: 1次, 等等... (注意 O 和 L 次數相同，L 需排在 O 前面)
        expected = [
            "L 3", "O 3",
            "H 2",
            "D 1", "E 1", "N 1", "P 1", "R 1", "T 1", "W 1", "Y 1"
        ]
        self.assertEqual(analyze_crypto(lines), expected)

if __name__ == '__main__':
    unittest.main()