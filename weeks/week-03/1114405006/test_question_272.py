"""UVA 272：TeX 引號轉換問題的 unit tests。

題目重點：
- 將普通雙引號 " 轉換成 TeX 風格的方向性引號
- 奇數個引號用 ``（左引號），偶數個引號用 ''（右引號）
- 交替出現，其他文字保持不變

測試涵蓋範圍：
1. 單對引號的轉換
2. 多對引號的轉換
3. 混合文字和特殊字符的處理
4. 空字符串和無引號的輸入
5. 單行和多行輸入
"""

import unittest
from question_272 import convert_quotes, process_input


class TestQuestion272(unittest.TestCase):
    """UVA 272 引號轉換的測試套件。"""

    def test_single_pair_quotes(self):
        """測試單對引號的轉換。
        最基本的情況：一個 " 變成 ``，下一個 " 變成 ''。
        """
        result = convert_quotes('He said "Hello"')
        self.assertEqual(result, 'He said ``Hello\'\'')

    def test_multiple_pairs_quotes(self):
        """測試多對引號的轉換。
        第 1、3、5... 個 " 變成 ``，第 2、4、6... 個 " 變成 ''。
        """
        result = convert_quotes('"First" and "Second"')
        self.assertEqual(result, '``First\'\' and ``Second\'\'')

    def test_quote_at_beginning(self):
        """測試引號在文字開始的情況。"""
        result = convert_quotes('"Start')
        self.assertEqual(result, '``Start')

    def test_quote_at_end(self):
        """測試引號在文字結束的情況。
        題目保證偶數個引號，所以最後的引號必定是結束引號（''）。
        """
        result = convert_quotes('End here "quote"')
        self.assertEqual(result, 'End here ``quote\'\'')

    def test_consecutive_quotes(self):
        """測試連續的引號對。"""
        result = convert_quotes('""')
        self.assertEqual(result, '``\'\'')

    def test_no_quotes(self):
        """測試沒有引號的文字。"""
        result = convert_quotes('No quotes here')
        self.assertEqual(result, 'No quotes here')

    def test_empty_string(self):
        """測試空字符串。"""
        result = convert_quotes('')
        self.assertEqual(result, '')

    def test_quote_with_punctuation(self):
        """測試引號和標點符號混合。"""
        result = convert_quotes('"To be or not to be," quoth the bard, "that is the question."')
        self.assertEqual(
            result,
            '``To be or not to be,\'\' quoth the bard, ``that is the question.\'\''
        )

    def test_multiline_input(self):
        """測試多行輸入（保持換行符）。
        引號計數跨越多行進行。
        """
        text = 'First line "quote1"\nSecond line "quote2"'
        result = convert_quotes(text)
        self.assertEqual(
            result,
            'First line ``quote1\'\'\nSecond line ``quote2\'\''
        )

    def test_special_characters_preserved(self):
        """測試特殊字符（非引號字符）保持不變。"""
        result = convert_quotes('He said "Hello, world!" with symbols: !@#$%')
        self.assertEqual(
            result,
            'He said ``Hello, world!\'\' with symbols: !@#$%'
        )

    def test_process_input_single_line(self):
        """測試 process_input 函式處理單行輸入。"""
        result = process_input('He said "Hello"\n')
        self.assertEqual(result, 'He said ``Hello\'\'\n')

    def test_process_input_multiple_lines(self):
        """測試 process_input 函式處理多行輸入。
        每行獨立調用 convert_quotes，但引號計數應該跨越行界。
        """
        input_text = 'Line 1 "quote\nLine 2 quote"\n'
        result = process_input(input_text)
        # 第一個引號是開始，第二個引號是結束
        self.assertEqual(
            result,
            'Line 1 ``quote\nLine 2 quote\'\'\n'
        )

    def test_alternating_quotes_pattern(self):
        """測試引號交替模式。
        奇數序列用 ``，偶數序列用 ''。
        """
        result = convert_quotes('"a" "b" "c" "d"')
        self.assertEqual(result, '``a\'\' ``b\'\' ``c\'\' ``d\'\'')

    def test_quote_in_middle_of_word(self):
        """測試引號在詞語中間出現。"""
        result = convert_quotes('don"t')
        self.assertEqual(result, 'don``t')

    def test_multiple_consecutive_pairs(self):
        """測試多個相鄰的引號對。"""
        result = convert_quotes('""abc""')
        self.assertEqual(result, '``\'\'abc``\'\'')


if __name__ == '__main__':
    unittest.main()
