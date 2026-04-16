"""UVA 490：文字旋轉問題的單元測試。

題目核心：
- 把輸入的多行文字視為矩陣
- 以順時針方向旋轉 90 度
- 旋轉後每一行長度要補齊到原始最寬行的寬度

測試重點：
1. 基本矩形旋轉
2. 單行輸入的轉換
3. 不同長度行的補空白處理
4. 含空白字元的保留
5. 空輸入與多組行為
"""

import unittest

from question_490 import rotate_lines, solve_text


class TestQuestion490(unittest.TestCase):
    """UVA 490 的測試套件。"""

    def test_rotate_two_equal_length_lines(self):
        """測試兩行等長文字的順時針旋轉。"""
        lines = ["HELLO", "WORLD"]
        expected = ["WH", "OE", "RL", "LL", "DO"]
        self.assertEqual(rotate_lines(lines), expected)

    def test_rotate_single_line(self):
        """測試單行文字的旋轉結果會變成直列輸出。"""
        lines = ["HELLO"]
        expected = ["H", "E", "L", "L", "O"]
        self.assertEqual(rotate_lines(lines), expected)

    def test_rotate_single_character_lines(self):
        """測試每行只有一個字元的情況。"""
        lines = ["A", "B", "C"]
        expected = ["CBA"]
        self.assertEqual(rotate_lines(lines), expected)

    def test_rotate_ragged_lines(self):
        """測試不同長度行的補空白處理。"""
        lines = ["ABC", "D E", "FGHI"]
        expected = ["FDA", "G B", "HEC", "I  "]
        self.assertEqual(rotate_lines(lines), expected)

    def test_rotate_lines_with_spaces(self):
        """測試行內空白字元要原樣保留。"""
        lines = ["A B", "C D"]
        expected = ["CA", "  ", "DB"]
        self.assertEqual(rotate_lines(lines), expected)

    def test_empty_input_lines(self):
        """測試空輸入行列表。"""
        self.assertEqual(rotate_lines([]), [])

    def test_empty_string_line(self):
        """測試只有空字串的一行。"""
        lines = [""]
        expected = []
        self.assertEqual(rotate_lines(lines), expected)

    def test_solve_text_basic_sample(self):
        """測試 solve_text 處理基本範例。"""
        input_text = "HELLO\nWORLD\n"
        expected = "WH\nOE\nRL\nLL\nDO\n"
        self.assertEqual(solve_text(input_text), expected)

    def test_solve_text_single_line(self):
        """測試 solve_text 處理單行輸入。"""
        input_text = "HELLO\n"
        expected = "H\nE\nL\nL\nO\n"
        self.assertEqual(solve_text(input_text), expected)

    def test_solve_text_with_empty_middle_line(self):
        """測試中間包含空行的情況。"""
        input_text = "AB\n\nCD\n"
        expected = "C A\nD B\n"
        self.assertEqual(solve_text(input_text), expected)

    def test_solve_text_preserves_trailing_spaces(self):
        """測試輸出尾端空白仍要保留。"""
        input_text = "A  \nBC \n"
        expected = "BA\nC \n  \n"
        self.assertEqual(solve_text(input_text), expected)

    def test_solve_text_empty_input(self):
        """測試空輸入。"""
        self.assertEqual(solve_text(""), "")


if __name__ == "__main__":
    unittest.main()
