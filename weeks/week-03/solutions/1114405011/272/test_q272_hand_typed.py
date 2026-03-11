"""
test_q272_hand_typed.py
針對手打程式 q272-Hand-typed.py 的單元測試

由於檔名含連字號無法直接 import，
使用 importlib 動態載入，測試邏輯與 test_q272.py 相同。
"""

import importlib.util
import unittest
from pathlib import Path

# ── 動態載入 q272-Hand-typed.py ──────────────────────────────────────────────
_file = Path(__file__).parent / "q272-Hand-typed.py"
_spec = importlib.util.spec_from_file_location("q272_hand_typed", _file)
_mod  = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

convert = _mod.convert


class TestConvert(unittest.TestCase):
    """測試 convert() 函式，涵蓋各種引號分布與邊界情況。"""

    def test_uva_official_sample(self):
        """UVA 272 官方範例"""
        inp = '"To be or not to be," quoth the bard, "that is the question."'
        exp = "``To be or not to be,'' quoth the bard, ``that is the question.''"
        self.assertEqual(convert(inp), exp)

    def test_single_pair(self):
        """一對引號：第 1 個 → ``，第 2 個 → ''"""
        self.assertEqual(convert('"hello"'), "``hello''")

    def test_two_pairs(self):
        """兩對引號：開閉開閉"""
        self.assertEqual(convert('"a" "b"'), "``a'' ``b''")

    def test_three_pairs(self):
        """三對引號，驗證輪替規律延續正確"""
        self.assertEqual(convert('"1" "2" "3"'), "``1'' ``2'' ``3''")

    def test_four_pairs_alternating(self):
        """四對引號，完整驗證兩輪輪替"""
        self.assertEqual(convert('"A" "B" "C" "D"'), "``A'' ``B'' ``C'' ``D''")

    def test_no_quotes(self):
        """沒有 " 的文字應完全不變"""
        text = "hello world, no quotes here."
        self.assertEqual(convert(text), text)

    def test_empty_string(self):
        """空字串應回傳空字串"""
        self.assertEqual(convert(''), '')

    def test_adjacent_quotes(self):
        """兩個 " 緊鄰：開引號與閉引號相連"""
        self.assertEqual(convert('""'), "``''")

    def test_multiline_single_pair_per_line(self):
        """多行輸入，引號旗標必須跨行維持狀態"""
        inp = '"line1"\n"line2"'
        exp = "``line1''\n``line2''"
        self.assertEqual(convert(inp), exp)

    def test_multiline_quotes_span_lines(self):
        """閉引號在下一行，旗標不可每行重置"""
        self.assertEqual(convert('"open\nclosed"'), "``open\nclosed''")

    def test_trailing_newline_preserved(self):
        """結尾換行符應被保留"""
        self.assertEqual(convert('"hello"\n'), "``hello''\n")

    def test_non_quote_chars_unchanged(self):
        """數字、標點、空白等非 " 字元應完全不變"""
        inp = 'abc 123 !@#$%^&*() "quoted"'
        exp = "abc 123 !@#$%^&*() ``quoted''"
        self.assertEqual(convert(inp), exp)

    def test_quote_surrounded_by_spaces(self):
        """引號前後有空格，空格應完整保留"""
        self.assertEqual(convert(' " hello " '), " `` hello '' ")
        self.assertEqual(convert(' "hi" '), " ``hi'' ")


if __name__ == "__main__":
    unittest.main(verbosity=2)
