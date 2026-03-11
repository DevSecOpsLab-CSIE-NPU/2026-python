"""
test_q272.py — UVA 272 / ZeroJudge c007 單元測試

測試對象：q272.py 中的 convert(input_text) 函式

執行方式：
  python -m pytest test_q272.py -v
  或
  python test_q272.py
"""

import unittest
from q272 import convert


# ─────────────────────────────────────────────────────────────────────────────
class TestConvert(unittest.TestCase):
    """測試 convert() 函式，涵蓋各種引號分布與邊界情況。"""

    def test_uva_official_sample(self):
        """
        UVA 272 官方範例：
        "To be or not to be," quoth the bard, "that is the question."
        """
        inp = '"To be or not to be," quoth the bard, "that is the question."'
        exp = '``To be or not to be,\'\' quoth the bard, ``that is the question.\'\''
        self.assertEqual(convert(inp), exp)

    def test_single_pair(self):
        """最簡單：一對引號，第 1 個 → ``，第 2 個 → ''"""
        self.assertEqual(convert('"hello"'), "``hello''")

    def test_two_pairs(self):
        """兩對引號：開閉開閉"""
        self.assertEqual(convert('"a" "b"'), "``a'' ``b''")

    def test_three_pairs(self):
        """三對引號，驗證輪替規律延續正確"""
        self.assertEqual(convert('"1" "2" "3"'), "``1'' ``2'' ``3''")

    def test_no_quotes(self):
        """沒有 " 的文字應完全不變"""
        text = "hello world, no quotes here."
        self.assertEqual(convert(text), text)

    def test_empty_string(self):
        """空字串應回傳空字串"""
        self.assertEqual(convert(''), '')

    def test_quotes_at_start_and_end(self):
        """引號在字串開頭與結尾"""
        self.assertEqual(convert('"start'), "``start")
        self.assertEqual(convert('end"end"'), "end``end''")

    def test_adjacent_quotes(self):
        """兩個 " 緊鄰：開引號與閉引號相連"""
        self.assertEqual(convert('""'), "``''")

    def test_multiline_single_pair_per_line(self):
        """
        多行輸入，每行有一對引號。
        旗標必須跨行維持狀態：
          第 1 行第 1 個 " → ``，第 2 個 " → ''
          第 2 行第 1 個 " → ``，第 2 個 " → ''
        """
        inp = '"line1"\n"line2"'
        exp = "``line1''\n``line2''"
        self.assertEqual(convert(inp), exp)

    def test_multiline_quotes_span_lines(self):
        """
        引號跨行配對：第 1 行的閉引號在第 2 行。
        旗標必須跨行記憶，不能每行重置。
        """
        inp  = '"open\nclosed"'
        exp  = "``open\nclosed''"
        self.assertEqual(convert(inp), exp)

    def test_non_quote_chars_unchanged(self):
        """數字、標點、空白等非 " 字元應完全不變"""
        inp = 'abc 123 !@#$%^&*() "quoted"'
        exp = 'abc 123 !@#$%^&*() ``quoted\'\''
        self.assertEqual(convert(inp), exp)

    def test_trailing_newline_preserved(self):
        """輸入結尾的換行符應被保留"""
        inp = '"hello"\n'
        exp = "``hello''\n"
        self.assertEqual(convert(inp), exp)

    def test_four_pairs_alternating(self):
        """四對引號，完整驗證兩輪輪替"""
        inp = '"A" "B" "C" "D"'
        exp = "``A'' ``B'' ``C'' ``D''"
        self.assertEqual(convert(inp), exp)

    def test_quote_surrounded_by_spaces(self):
        """引號前後有空格，空格應完整保留（包含引號與文字之間的空格）"""
        # ' " hello " ' → 第1個" → ``，第2個" → ''，空格不動
        self.assertEqual(convert(' " hello " '), " `` hello '' ")
        self.assertEqual(convert(' "hi" '), " ``hi'' ")


if __name__ == "__main__":
    unittest.main(verbosity=2)
