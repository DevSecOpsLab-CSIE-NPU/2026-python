"""
question_272.py 單元測試

測試目標：
1. 基本引號替換
2. 多段引號交替替換
3. 多行情況下狀態要延續
4. 不含引號時文字需保持不變

所有說明均為繁體中文。
"""

import unittest

from question_272 import convert_tex_quotes, solve_text


class TestConvertTexQuotes(unittest.TestCase):
    """測試核心函式 convert_tex_quotes。"""

    def test_single_pair_quotes(self):
        """最基本案例：一組引號。"""
        raw = '"Hello"'
        expected = "``Hello''"
        self.assertEqual(convert_tex_quotes(raw), expected)

    def test_uva_classic_example(self):
        """題目經典範例。"""
        raw = '"To be or not to be," quoth the bard, "that is the question."'
        expected = "``To be or not to be,'' quoth the bard, ``that is the question.''"
        self.assertEqual(convert_tex_quotes(raw), expected)

    def test_multiple_quote_pairs(self):
        """同一行有多組引號，必須交替替換。"""
        raw = 'A "B" C "D" E'
        expected = "A ``B'' C ``D'' E"
        self.assertEqual(convert_tex_quotes(raw), expected)

    def test_no_quote(self):
        """沒有雙引號時，輸出應完全相同。"""
        raw = "No quotes here."
        self.assertEqual(convert_tex_quotes(raw), raw)

    def test_multiline_state_continue(self):
        """
        多行時也要依整份文字的順序持續交替。
        第一行開引號，第二行遇到下一個引號應變成閉引號。
        """
        raw = 'Start "line1\nline2" end\n"new"'
        expected = "Start ``line1\nline2'' end\n``new''"
        self.assertEqual(convert_tex_quotes(raw), expected)

    def test_empty_input(self):
        """空字串應回傳空字串。"""
        self.assertEqual(convert_tex_quotes(""), "")


class TestSolveText(unittest.TestCase):
    """測試對外入口 solve_text。"""

    def test_same_as_core(self):
        raw = '"A" and "B"'
        self.assertEqual(solve_text(raw), convert_tex_quotes(raw))


if __name__ == "__main__":
    unittest.main(verbosity=2)
