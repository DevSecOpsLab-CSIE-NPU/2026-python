import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_272.py 中
# 並且您的解答會提供一個 solve(lines) 函式：
# 它接收一個包含多行字串的 list，並回傳替換雙引號後的字串 list。
from solution_272 import solve

class TestUVA272(unittest.TestCase):
    
    def test_sample_case(self):
        """
        測試題目給定的標準範例。
        確保同一行內出現多個雙引號時，能正確地交替替換。
        第一個 " 替換為 `` (兩個左單引號/反引號)
        第二個 " 替換為 '' (兩個右單引號)
        """
        input_lines = [
            '"To be or not to be," quoth the bard, "that is the question."'
        ]
        expected_lines = [
            "``To be or not to be,'' quoth the bard, ``that is the question.''"
        ]
        self.assertEqual(solve(input_lines), expected_lines)

    def test_multi_line_quotes(self):
        """
        邊界陷阱測試：測試跨行的引號替換。
        UVA 272 的核心難點在於，文章是多行的，但引號的「開關狀態 (布林值)」
        必須跨越換行持續保持。例如第一行開啟了引號但沒關閉，第二行的第一個引號就必須被視為「關閉」。
        """
        input_lines = [
            '"First line',     # 開啟引號 (變成 ``)
            'Second line"',    # 上一行未關閉，所以這裡要關閉引號 (變成 '')
            '"Third" line'     # 重新開啟 (``) 又立刻關閉 ('')
        ]
        expected_lines = [
            "``First line",
            "Second line''",
            "``Third'' line"
        ]
        self.assertEqual(solve(input_lines), expected_lines)

    def test_no_quotes(self):
        """
        基礎測試：測試完全沒有雙引號的情況。
        程式不應該更動到其他任何字元。
        """
        input_lines = [
            "Hello World!",
            "This is a test without quotes."
        ]
        expected_lines = input_lines # 預期結果等於輸入結果
        self.assertEqual(solve(input_lines), expected_lines)

if __name__ == '__main__':
    unittest.main()