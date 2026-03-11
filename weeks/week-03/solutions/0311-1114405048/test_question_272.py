"""
UVA 272 — TeX 引號替換 單元測試

測試目標：
1. convert_quotes(text)：將普通雙引號 " 交替替換為 `` 和 ''
2. 多行輸入的處理
3. 邊界與特殊情況
"""

import unittest


# ===== 受測函式 =====

def convert_quotes(text):
    """
    將輸入文字中的普通雙引號 " 交替替換為 TeX 格式。
    第奇數個（第 1、3、5...）替換為 ``（左雙引號）。
    第偶數個（第 2、4、6...）替換為 ''（右雙引號）。
    其餘字元保持不變。
    """
    opening = True
    out = []
    for ch in text:
        if ch == '"':
            if opening:
                out.append('``')
            else:
                out.append("''")
            opening = not opening
        else:
            out.append(ch)
    return ''.join(out)


# ===== 測試類別 =====


class TestBasicConversion(unittest.TestCase):
    """測試基本的引號替換功能"""

    def test_single_pair(self):
        """一對引號：第一個變 ``，第二個變 ''"""
        result = convert_quotes('"hello"')
        self.assertEqual(result, "``hello''")

    def test_sample_input(self):
        """題目範例輸入"""
        text = '"To be or not to be," quoth the bard, "that is the question."'
        expected = "``To be or not to be,'' quoth the bard, ``that is the question.''"
        self.assertEqual(convert_quotes(text), expected)

    def test_two_pairs(self):
        """兩對引號：交替替換 ``...''...``...''"""
        result = convert_quotes('"A" and "B"')
        self.assertEqual(result, "``A'' and ``B''")

    def test_three_pairs(self):
        """三對引號：正確交替六次"""
        result = convert_quotes('"1" "2" "3"')
        self.assertEqual(result, "``1'' ``2'' ``3''")

    def test_adjacent_quotes(self):
        """緊鄰的引號對"""
        result = convert_quotes('""')
        self.assertEqual(result, "``''")


class TestNoQuotes(unittest.TestCase):
    """測試沒有引號的情況"""

    def test_no_quotes(self):
        """無引號的文字應原樣輸出"""
        text = "Hello, World!"
        self.assertEqual(convert_quotes(text), text)

    def test_empty_string(self):
        """空字串應回傳空字串"""
        self.assertEqual(convert_quotes(""), "")

    def test_only_spaces(self):
        """只有空白的字串應原樣輸出"""
        self.assertEqual(convert_quotes("   "), "   ")


class TestMultiLine(unittest.TestCase):
    """測試多行輸入（引號狀態跨行延續）"""

    def test_quote_across_lines(self):
        """引號狀態跨行：第一行開引號，第二行閉引號"""
        line1 = convert_quotes('"hello')
        # 此時 opening 狀態已翻轉，需要模擬連續處理
        # 使用完整文字測試
        text = '"hello\nworld"'
        result = convert_quotes(text)
        self.assertEqual(result, "``hello\nworld''")

    def test_multiline_two_pairs(self):
        """多行文字中有兩對引號"""
        text = '"line1"\n"line2"'
        result = convert_quotes(text)
        self.assertEqual(result, "``line1''\n``line2''")

    def test_newline_preserved(self):
        """換行符應被保留"""
        text = "abc\ndef\n"
        self.assertEqual(convert_quotes(text), text)


class TestSpecialCharacters(unittest.TestCase):
    """測試含特殊字元的情況"""

    def test_with_backticks(self):
        """輸入中已有反引號，不應被影響"""
        text = '`already` "quoted"'
        result = convert_quotes(text)
        self.assertEqual(result, "`already` ``quoted''")

    def test_with_single_quotes(self):
        """輸入中有單引號，不應被影響"""
        text = "it's \"fine\""
        result = convert_quotes(text)
        self.assertEqual(result, "it's ``fine''")

    def test_with_punctuation(self):
        """引號旁有標點符號"""
        result = convert_quotes('"Hello!"')
        self.assertEqual(result, "``Hello!''")

    def test_with_numbers(self):
        """引號包圍數字"""
        result = convert_quotes('"123"')
        self.assertEqual(result, "``123''")


class TestEdgeCases(unittest.TestCase):
    """測試邊界情況"""

    def test_four_pairs(self):
        """四對引號，確認交替正確"""
        result = convert_quotes('"a" "b" "c" "d"')
        self.assertEqual(result, "``a'' ``b'' ``c'' ``d''")

    def test_empty_quote_pairs(self):
        """連續空引號對："""" → ``''``''"""
        result = convert_quotes('""""')
        self.assertEqual(result, "``''``''")

    def test_long_text_between_quotes(self):
        """引號間有大量文字"""
        text = '"' + 'x' * 100 + '"'
        expected = '``' + 'x' * 100 + "''"
        self.assertEqual(convert_quotes(text), expected)


if __name__ == "__main__":
    unittest.main()
