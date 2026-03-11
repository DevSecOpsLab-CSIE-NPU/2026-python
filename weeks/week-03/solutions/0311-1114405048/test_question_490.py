"""
UVA 490 — 旋轉句子（Rotating Sentences）單元測試

測試目標：
1. rotate_sentences(lines)：將多行文字順時針旋轉 90 度
2. 各種長度不等的輸入
3. 邊界與特殊情況
"""

import unittest


# ===== 受測函式 =====

def rotate_sentences(lines):
    """
    將輸入的多行文字順時針旋轉 90 度。
    最後一行變成最左列，第一行變成最右列。
    較短的行用空格補齊到最長行的長度。
    回傳旋轉後的多行字串列表。
    """
    if not lines:
        return []
    # 找出最長行的長度
    max_len = max(len(line) for line in lines)
    # 將每行補齊到相同長度
    padded = [line.ljust(max_len) for line in lines]
    n = len(padded)
    result = []
    # 逐欄取字元：第 col 欄，從最後一行到第一行
    for col in range(max_len):
        row_chars = []
        for row in range(n - 1, -1, -1):
            row_chars.append(padded[row][col])
        result.append(''.join(row_chars))
    return result


# ===== 測試類別 =====


class TestBasicRotation(unittest.TestCase):
    """測試基本旋轉功能"""

    def test_hello_world(self):
        """經典範例：HELLO 和 WORLD 旋轉"""
        lines = ['HELLO', 'WORLD']
        result = rotate_sentences(lines)
        expected = ['WH', 'OE', 'RL', 'LL', 'DO']
        self.assertEqual(result, expected)

    def test_single_line(self):
        """單行輸入：每個字元變成一行"""
        lines = ['ABC']
        result = rotate_sentences(lines)
        expected = ['A', 'B', 'C']
        self.assertEqual(result, expected)

    def test_single_char_lines(self):
        """每行只有一個字元"""
        lines = ['A', 'B', 'C']
        result = rotate_sentences(lines)
        expected = ['CBA']
        self.assertEqual(result, expected)

    def test_two_lines_same_length(self):
        """兩行等長"""
        lines = ['AB', 'CD']
        result = rotate_sentences(lines)
        expected = ['CA', 'DB']
        self.assertEqual(result, expected)


class TestUnequalLengths(unittest.TestCase):
    """測試長度不等的輸入（需補空格）"""

    def test_first_shorter(self):
        """第一行較短，需補空格"""
        lines = ['AB', 'CDEF']
        result = rotate_sentences(lines)
        expected = ['CA', 'DB', 'E ', 'F ']
        self.assertEqual(result, expected)

    def test_second_shorter(self):
        """第二行較短，需補空格"""
        lines = ['ABCD', 'EF']
        result = rotate_sentences(lines)
        expected = ['EA', 'FB', ' C', ' D']
        self.assertEqual(result, expected)

    def test_three_lines_different_lengths(self):
        """三行不同長度"""
        lines = ['A', 'BC', 'DEF']
        result = rotate_sentences(lines)
        # 補齊後：'A  ', 'BC ', 'DEF'
        # col0: D, B, A → 'DBA'
        # col1: E, C, ' ' → 'EC '
        # col2: F, ' ', ' ' → 'F  '
        expected = ['DBA', 'EC ', 'F  ']
        self.assertEqual(result, expected)


class TestSpecialCharacters(unittest.TestCase):
    """測試特殊字元"""

    def test_with_spaces(self):
        """輸入含空格"""
        lines = ['A B']
        result = rotate_sentences(lines)
        expected = ['A', ' ', 'B']
        self.assertEqual(result, expected)

    def test_with_punctuation(self):
        """輸入含標點符號"""
        lines = ['Hi!', 'Ok.']
        result = rotate_sentences(lines)
        expected = ['OH', 'ki', '.!']
        self.assertEqual(result, expected)

    def test_with_numbers(self):
        """輸入含數字"""
        lines = ['123', '456']
        result = rotate_sentences(lines)
        expected = ['41', '52', '63']
        self.assertEqual(result, expected)


class TestEdgeCases(unittest.TestCase):
    """測試邊界情況"""

    def test_empty_input(self):
        """空輸入"""
        self.assertEqual(rotate_sentences([]), [])

    def test_single_char(self):
        """只有一個字元"""
        result = rotate_sentences(['X'])
        self.assertEqual(result, ['X'])

    def test_empty_and_nonempty(self):
        """含空行與非空行"""
        lines = ['', 'AB']
        result = rotate_sentences(lines)
        # 補齊後：'  ', 'AB'
        # col0: A, ' ' → 'A '
        # col1: B, ' ' → 'B '
        expected = ['A ', 'B ']
        self.assertEqual(result, expected)

    def test_all_spaces(self):
        """全部是空格"""
        lines = ['  ', '  ']
        result = rotate_sentences(lines)
        expected = ['  ', '  ']
        self.assertEqual(result, expected)

    def test_many_lines(self):
        """多行輸入，確認旋轉後行數等於最長行長度"""
        lines = ['ABCDE', 'FG', 'HIJ']
        result = rotate_sentences(lines)
        self.assertEqual(len(result), 5)  # 最長行長度為 5


if __name__ == "__main__":
    unittest.main()
