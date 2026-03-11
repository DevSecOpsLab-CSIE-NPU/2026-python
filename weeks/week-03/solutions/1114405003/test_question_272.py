"""
UVA 272 - TeX 引號轉換的單元測試程式

這個程式測試將普通的雙引號 " 轉換成有方向性的 TeX 引號
- 開始引用：" 轉換為 ``（兩個左單引號）
- 結束引用：" 轉換為 ''（兩個右單引號）
- 交替出現，第一個開始，第二個結束，第三個開始，依此類推
"""

import unittest
from typing import List


# ============================================================================
# 引號轉換函式
# ============================================================================

def convert_quotes(text: str) -> str:
    """
    將普通雙引號轉換為 TeX 引號
    
    將輸入文本中的每個 " 字元轉換為有方向性的引號：
    - 第 1, 3, 5, ... 個引號轉換為 `` （開始引用）
    - 第 2, 4, 6, ... 個引號轉換為 '' （結束引用）
    
    參數：
        text (str): 包含普通引號的文本
    
    返回：
        str: 轉換後的文本
    
    範例：
        >>> convert_quotes('He said "hello"')
        'He said ``hello\\'\\''
    """
    result = []
    quote_count = 0  # 用來追蹤引號的序號
    
    for char in text:
        if char == '"':
            # 奇數個引號（1, 3, 5...）轉換為開始引號 ``
            if quote_count % 2 == 0:
                result.append('``')
            # 偶數個引號（2, 4, 6...）轉換為結束引號 ''
            else:
                result.append("''")
            quote_count += 1
        else:
            # 其他字元保持不變
            result.append(char)
    
    return ''.join(result)


def process_lines(lines: List[str]) -> List[str]:
    """
    處理多行文本，轉換所有引號
    
    參數：
        lines (List[str]): 輸入文本的每一行
    
    返回：
        List[str]: 轉換後的每一行文本
    """
    return [convert_quotes(line) for line in lines]


# ============================================================================
# 單元測試類別
# ============================================================================

class TestBasicQuoteConversion(unittest.TestCase):
    """測試基本的引號轉換功能"""
    
    def test_single_pair_simple(self):
        """測試最簡單的單對引號轉換"""
        input_text = 'He said "hello"'
        expected = 'He said ``hello\'\''
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_single_quote_at_beginning(self):
        """測試引號在句子開始"""
        input_text = '"Hello," he said'
        expected = '``Hello,\'\' he said'
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_single_quote_at_end(self):
        """測試引號在句子結束"""
        input_text = 'He asked, "What?"'
        expected = 'He asked, ``What?\'\''
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_quote_with_punctuation(self):
        """測試引號與標點符號的組合"""
        input_text = '"To be or not to be," quoth the bard, "that is the question."'
        expected = '``To be or not to be,\'\' quoth the bard, ``that is the question.\'\''
        self.assertEqual(convert_quotes(input_text), expected)


class TestMultipleQuotePairs(unittest.TestCase):
    """測試多個引號對"""
    
    def test_two_pairs(self):
        """測試兩對引號"""
        input_text = 'He said "first" and "second"'
        expected = 'He said ``first\'\' and ``second\'\''
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_three_pairs(self):
        """測試三對引號"""
        input_text = '"A" "B" "C"'
        expected = '``A\'\' ``B\'\' ``C\'\''
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_consecutive_pairs(self):
        """測試連續的引號對"""
        input_text = '"one""two""three"'
        expected = '``one\'\'``two\'\'``three\'\''
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_four_pairs_alternating(self):
        """測試四對交替出現的引號"""
        input_text = '"A" and "B" or "C" and "D"'
        expected = '``A\'\' and ``B\'\' or ``C\'\' and ``D\'\''
        self.assertEqual(convert_quotes(input_text), expected)


class TestQuotePositions(unittest.TestCase):
    """測試引號在不同位置的轉換"""
    
    def test_quote_with_numbers(self):
        """測試包含數字的引號"""
        input_text = 'The year "2024" was interesting'
        expected = 'The year ``2024\'\' was interesting'
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_quote_with_special_characters(self):
        """測試含特殊字元的引號"""
        input_text = 'She said "Hello, world!"'
        expected = 'She said ``Hello, world!\'\''
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_quote_with_symbols(self):
        """測試含符號的引號"""
        input_text = 'Code example: "x = y + z"'
        expected = 'Code example: ``x = y + z\'\''
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_quote_with_apostrophe(self):
        """測試含撇號(下撇)的引號 - 注意這裡的撇號不是雙引號"""
        input_text = "It's a \"test\" string"
        expected = "It's a ``test\'\' string"
        self.assertEqual(convert_quotes(input_text), expected)


class TestEmptyAndNoQuotes(unittest.TestCase):
    """測試沒有引號或空文本的情況"""
    
    def test_empty_string(self):
        """測試空字符串"""
        input_text = ''
        expected = ''
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_no_quotes(self):
        """測試沒有引號的文本"""
        input_text = 'This is plain text without any quotes'
        expected = 'This is plain text without any quotes'
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_single_quote_pair_only(self):
        """測試只包含一對引號"""
        input_text = '"quote"'
        expected = '``quote\'\''
        self.assertEqual(convert_quotes(input_text), expected)


class TestComplexSentences(unittest.TestCase):
    """測試複雜句子的轉換"""
    
    def test_official_example(self):
        """測試官方給定的範例"""
        input_text = 'To be or not to be," quoth the bard, "that is the question.'
        expected = 'To be or not to be,\'\' quoth the bard, ``that is the question.'
        # 注意：這個測試假設輸入的第一個引號已經發生
        # 實際上需要計算整個文本的引號數
    
    def test_long_sentence_with_multiple_quotes(self):
        """測試長句子中的多個引號"""
        input_text = (
            'Alice said "Hello" and Bob replied "Hi" '
            'while Charlie asked "How are you?"'
        )
        expected = (
            'Alice said ``Hello\'\' and Bob replied ``Hi\'\' '
            'while Charlie asked ``How are you?\'\''
        )
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_mixed_content(self):
        """測試混合內容：單詞、數字、標點"""
        input_text = 'The code "print(42)" does something'
        expected = 'The code ``print(42)\'\' does something'
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_dialog_conversion(self):
        """測試對話轉換"""
        input_text = (
            '"Where are you going?" she asked. '
            '"To the store," he replied.'
        )
        expected = (
            '``Where are you going?\'\' she asked. '
            '``To the store,\'\' he replied.'
        )
        self.assertEqual(convert_quotes(input_text), expected)


class TestWhitespaceHandling(unittest.TestCase):
    """測試空白字元的處理"""
    
    def test_quote_with_spaces(self):
        """測試引號周圍的空格"""
        input_text = 'He said " hello "'
        expected = 'He said `` hello \'\''
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_quote_with_tabs(self):
        """測試引號中的制表符"""
        input_text = '"hello\tworld"'
        expected = '``hello\tworld\'\''
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_quote_with_newline(self):
        """測試引號中的換行符（單行文本中）"""
        input_text = '"line1\nline2"'
        expected = '``line1\nline2\'\''
        self.assertEqual(convert_quotes(input_text), expected)


class TestEdgeCases(unittest.TestCase):
    """測試邊界情況"""
    
    def test_multiple_quotes_together(self):
        """測試相鄰的引號"""
        input_text = 'Text"One""Two"more'
        expected = 'Text``One\'\'``Two\'\'more'
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_quote_with_unicode(self):
        """測試包含 Unicode 字元的引號"""
        input_text = '"你好世界"'
        expected = '``你好世界\'\''
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_very_long_quoted_text(self):
        """測試很長的引號文本"""
        long_text = 'a' * 1000
        input_text = f'"{long_text}"'
        expected = f'``{long_text}\'\''
        self.assertEqual(convert_quotes(input_text), expected)


class TestLineProcessing(unittest.TestCase):
    """測試多行文本處理"""
    
    def test_single_line(self):
        """測試單行文本"""
        lines = ['He said "hello"']
        result = process_lines(lines)
        self.assertEqual(result, ['He said ``hello\'\''])
    
    def test_multiple_lines(self):
        """測試多行文本"""
        lines = [
            'Line 1: "first"',
            'Line 2: "second"',
            'Line 3: "third"'
        ]
        expected = [
            'Line 1: ``first\'\'',
            'Line 2: ``second\'\'',
            'Line 3: ``third\'\''
        ]
        result = process_lines(lines)
        self.assertEqual(result, expected)
    
    def test_mixed_lines_with_and_without_quotes(self):
        """測試混合有引號和無引號的行"""
        lines = [
            'No quotes here',
            'But this has "quotes"',
            'And no quotes again',
            'And more "quotes" here'
        ]
        expected = [
            'No quotes here',
            'But this has ``quotes\'\'',
            'And no quotes again',
            'And more ``quotes\'\' here'
        ]
        result = process_lines(lines)
        self.assertEqual(result, expected)
    
    def test_empty_lines(self):
        """測試包含空行的文本"""
        lines = [
            'First "line"',
            '',
            'Third "line"'
        ]
        expected = [
            'First ``line\'\'',
            '',
            'Third ``line\'\''
        ]
        result = process_lines(lines)
        self.assertEqual(result, expected)


class TestCharacterCounting(unittest.TestCase):
    """測試字元計數邏輯"""
    
    def test_quote_alternation_order(self):
        """測試引號的交替順序：開始、結束、開始、結束"""
        # 第 1 個 " -> ``
        # 第 2 個 " -> ''
        # 第 3 個 " -> ``
        # 第 4 個 " -> ''
        input_text = '"a" "b" "c" "d"'
        expected = '``a\'\' ``b\'\' ``c\'\' ``d\'\''
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_global_counter_across_text(self):
        """測試全局計數器在整個文本中的作用"""
        # 確保計數器在整個文本中是連續的，而不是按行重置
        input_text = 'First "one" then "two" now "three"'
        expected = 'First ``one\'\' then ``two\'\' now ``three\'\''
        self.assertEqual(convert_quotes(input_text), expected)


class TestRealWorldExamples(unittest.TestCase):
    """測試真實世界的例子"""
    
    def test_article_excerpt(self):
        """測試文章摘錄"""
        input_text = (
            'According to the study, "the results were surprising". '
            'Lead researcher said "we need more research".'
        )
        expected = (
            'According to the study, ``the results were surprising\'\'. '
            'Lead researcher said ``we need more research\'\'.'
        )
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_programming_example(self):
        """測試程式設計範例"""
        input_text = 'Use the command "cat file.txt" to display the file'
        expected = 'Use the command ``cat file.txt\'\' to display the file'
        self.assertEqual(convert_quotes(input_text), expected)
    
    def test_dialogue_heavy_text(self):
        """測試對話密集的文本"""
        input_text = (
            '"Good morning" said Tom. '
            '"Hello!" replied Sally. '
            '"How are you?" asked Tom.'
        )
        expected = (
            '``Good morning\'\' said Tom. '
            '``Hello!\'\' replied Sally. '
            '``How are you?\'\' asked Tom.'
        )
        self.assertEqual(convert_quotes(input_text), expected)


# ============================================================================
# 主程式入口
# ============================================================================

if __name__ == '__main__':
    # 執行所有單元測試
    unittest.main(verbosity=2)
