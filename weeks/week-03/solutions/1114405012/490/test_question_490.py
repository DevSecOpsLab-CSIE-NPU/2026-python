"""
question_490.py 單元測試

測試重點：
1. 基本旋轉（固定長度）
2. 不等長字串補空白
3. 空輸入、單行輸入
4. 含空行情況

全部註解為繁體中文。
"""

import unittest

from question_490 import rotate_90_clockwise, solve_text


class TestRotate90Clockwise(unittest.TestCase):
    """測試核心旋轉函式。"""

    def test_hello_world(self):
        """題意示例：HELLO + WORLD。"""
        lines = ["HELLO", "WORLD"]
        expected = ["WH", "OE", "RL", "LL", "DO"]
        self.assertEqual(rotate_90_clockwise(lines), expected)

    def test_uneven_lines(self):
        """不等長行需要補空白。"""
        lines = ["ABC", "DE"]
        expected = ["DA", "EB", " C"]
        self.assertEqual(rotate_90_clockwise(lines), expected)

    def test_single_line(self):
        """單行輸入會變成直向輸出。"""
        lines = ["ABC"]
        expected = ["A", "B", "C"]
        self.assertEqual(rotate_90_clockwise(lines), expected)

    def test_empty_list(self):
        self.assertEqual(rotate_90_clockwise([]), [])

    def test_with_blank_line(self):
        """中間空行也算矩陣的一列。"""
        lines = ["A", "", "BC"]
        expected = ["B A", "C"]
        self.assertEqual(rotate_90_clockwise(lines), expected)


class TestSolveText(unittest.TestCase):
    """測試文字輸入輸出入口。"""

    def test_text_input(self):
        raw = "HELLO\nWORLD\n"
        expected = "WH\nOE\nRL\nLL\nDO"
        self.assertEqual(solve_text(raw), expected)

    def test_empty_text(self):
        self.assertEqual(solve_text(""), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
