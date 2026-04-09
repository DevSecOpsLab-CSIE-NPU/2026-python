"""
UVA 272 - TEX Quotes 程式

題目說明：
TeX 排版軟體使用方向的雙引號來標註引用內容。
- 左雙引號：``
- 右雙引號：''

一般鍵盤的雙引號 " 需要轉換為 TeX 風格引號。
轉換規則：
- 第1,3,5...個雙引號（奇數）→ ``
- 第2,4,6...個雙引號（偶數）→ ''

簡單記憶口號：奇數 `` 偶數 ''
"""

import sys
import unittest


def tex_quotes(text):
    """
    將文字中的雙引號轉換為 TeX 風格的引號

    參數:
        text: 輸入的原始文字

    回傳:
        轉換後的文字

    演算法:
        1. 用 count 計數器追蹤目前處理到第幾個雙引號
        2. 偶數次（0,2,4...）→ ``
        3. 奇數次（1,3,5...）→ ''
    """
    result = []
    count = 0

    for char in text:
        if char == '"':
            result.append("``" if count % 2 == 0 else "''")
            count += 1
        else:
            result.append(char)

    return "".join(result)


def tex_quotes_easy(text):
    """
    使用列表存取版本
    """
    quotes = ["``", "''"]
    result = []
    i = 0

    for char in text:
        if char == '"':
            result.append(quotes[i % 2])
            i += 1
        else:
            result.append(char)

    return "".join(result)


def tex_quotes_simple(text):
    """
    使用 toggle 布林值版本
    """
    result = []
    left = True

    for char in text:
        if char == '"':
            result.append("``" if left else "''")
            left = not left
        else:
            result.append(char)

    return "".join(result)


class TestTexQuotes(unittest.TestCase):
    """TEX Quotes 轉換功能測試類別"""

    def test_basic_quote_conversion(self):
        """測試基本引號轉換（題目範例）"""
        input_text = '"To be or not to be," quoth the bard, "that is the question."'
        expected = "``To be or not to be,'' quoth the bard, ``that is the question.''"
        self.assertEqual(tex_quotes(input_text), expected)

    def test_multiple_pairs(self):
        """測試多對引號"""
        input_text = '"first" "second" "third"'
        expected = "``first'' ``second'' ``third''"
        self.assertEqual(tex_quotes(input_text), expected)

    def test_only_quotes(self):
        """測試只有引號的情況"""
        input_text = '""'
        expected = "``''"
        self.assertEqual(tex_quotes(input_text), expected)

    def test_quotes_with_newlines(self):
        """測試包含換行符的情況"""
        input_text = '"Hello"\n"World"'
        expected = "``Hello''\n``World''"
        self.assertEqual(tex_quotes(input_text), expected)

    def test_odd_number_of_quotes(self):
        """測試奇數個引號"""
        input_text = '"Hello" "World"'
        expected = "``Hello'' ``World''"
        self.assertEqual(tex_quotes(input_text), expected)

    def test_single_quote_pair(self):
        """測試單一對引號"""
        input_text = '"Hello World"'
        expected = "``Hello World''"
        self.assertEqual(tex_quotes(input_text), expected)

    def test_no_quotes(self):
        """測試沒有引號的情況"""
        input_text = "Hello, world!"
        self.assertEqual(tex_quotes(input_text), input_text)

    def test_empty_string(self):
        """測試空字串"""
        self.assertEqual(tex_quotes(""), "")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sys.argv = [sys.argv[0]] + sys.argv[2:]
        unittest.main()
    else:
        output = tex_quotes(sys.stdin.read())
        print(output, end="")
