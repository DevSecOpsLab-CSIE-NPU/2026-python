"""
題目 272: TeX 引號轉換 - 單元測試程序
https://zerojudge.tw/ShowProblem?problemid=c007

測試內容：
1. 簡單引號對轉換
2. 多個引號對的交替轉換
3. 無引號文本保持不變
4. 複雜文本的混合情況
5. 邊界情況和特殊場景
6. 多行文本處理
"""

import unittest
from io import StringIO
import sys

# 導入要測試的模組
from solution_question_272 import TexQuoteConverter, convert_tex_quotes


class TestTexQuoteConverter(unittest.TestCase):
    """測試 TexQuoteConverter 類的基本功能"""
    
    def setUp(self):
        """每個測試前初始化轉換器"""
        self.converter = TexQuoteConverter()
    
    def test_single_quote_pair(self):
        """測試：單一引號對的轉換"""
        result = self.converter.convert_line('"Hello"')
        self.assertEqual(result, '``Hello\'\'')
        
    def test_two_quote_pairs(self):
        """測試：兩個引號對的轉換"""
        result = self.converter.convert_line('"First" and "Second"')
        self.assertEqual(result, '``First\'\' and ``Second\'\'')
    
    def test_three_quote_pairs(self):
        """測試：三個引號對的轉換"""
        result = self.converter.convert_line('"A" "B" "C"')
        self.assertEqual(result, '``A\'\' ``B\'\' ``C\'\'')
    
    def test_no_quotes(self):
        """測試：沒有引號的文本保持不變"""
        result = self.converter.convert_line('Hello world')
        self.assertEqual(result, 'Hello world')
    
    def test_quotes_at_start(self):
        """測試：文本開始有引號"""
        result = self.converter.convert_line('"Start"')
        self.assertEqual(result, '``Start\'\'')
    
    def test_quotes_at_end(self):
        """測試：文本末尾有引號"""
        result = self.converter.convert_line('end "Here"')
        self.assertEqual(result, 'end ``Here\'\'')
    
    def test_consecutive_quotes(self):
        """測試：連續的引號（開啟-關閉-開啟-關閉）"""
        result = self.converter.convert_line('""')
        self.assertEqual(result, '``\'\'')
    
    def test_quote_with_comma(self):
        """測試：引號內有逗號"""
        result = self.converter.convert_line('"To be or not to be," quoth')
        self.assertEqual(result, '``To be or not to be,\'\' quoth')
    
    def test_multiple_lines_state_persistence(self):
        """測試：跨越多行時狀態是否保持"""
        # 第一行：開啟引號
        result1 = self.converter.convert_line('He said "Hello')
        self.assertEqual(result1, 'He said ``Hello')
        
        # 第二行：應該關閉引號（狀態應該保持）
        result2 = self.converter.convert_line('there"')
        self.assertEqual(result2, 'there\'\'')


class TestConvertTexQuotes(unittest.TestCase):
    """測試 convert_tex_quotes 函數（處理多行文本）"""
    
    def test_simple_sentence(self):
        """測試：簡單的句子"""
        input_text = '"Hello"'
        expected = '``Hello\'\''
        result = convert_tex_quotes(input_text)
        self.assertEqual(result, expected)
    
    def test_shakespeare_quote(self):
        """測試：題目範例 - 莎士比亞引用"""
        input_text = '"To be or not to be," quoth the bard, "that is the question."'
        expected = '``To be or not to be,\'\' quoth the bard, ``that is the question.\'\''
        result = convert_tex_quotes(input_text)
        self.assertEqual(result, expected)
    
    def test_multiple_lines(self):
        """測試：多行文本"""
        input_text = 'Line 1: "Quote 1"\nLine 2: "Quote 2"'
        expected = 'Line 1: ``Quote 1\'\'\nLine 2: ``Quote 2\'\''
        result = convert_tex_quotes(input_text)
        self.assertEqual(result, expected)
    
    def test_quote_across_lines(self):
        """測試：引號跨越多行"""
        input_text = 'Start "opening\nclosing" end'
        expected = 'Start ``opening\nclosing\'\' end'
        result = convert_tex_quotes(input_text)
        self.assertEqual(result, expected)
    
    def test_empty_string(self):
        """測試：空字符串"""
        result = convert_tex_quotes('')
        self.assertEqual(result, '')
    
    def test_no_quotes(self):
        """測試：完全沒有引號的文本"""
        input_text = 'This is plain text without any quotes.'
        result = convert_tex_quotes(input_text)
        self.assertEqual(result, input_text)
    
    def test_special_characters_inside_quotes(self):
        """測試：引號內含有特殊字符"""
        input_text = '"@#$%^&*()"'
        expected = '``@#$%^&*()\'\''
        result = convert_tex_quotes(input_text)
        self.assertEqual(result, expected)
    
    def test_numbers_inside_quotes(self):
        """測試：引號內含有數字"""
        input_text = '"12345"'
        expected = '``12345\'\''
        result = convert_tex_quotes(input_text)
        self.assertEqual(result, expected)
    
    def test_whitespace_handling(self):
        """測試：空白字符的處理"""
        input_text = '"  spaces  "'
        expected = '``  spaces  \'\''
        result = convert_tex_quotes(input_text)
        self.assertEqual(result, expected)
    
    def test_quote_with_period(self):
        """測試：引號末尾帶句號"""
        input_text = '"sentence."'
        expected = '``sentence.\'\''
        result = convert_tex_quotes(input_text)
        self.assertEqual(result, expected)
    
    def test_alternating_quotes_complex(self):
        """測試：複雜的交替引號"""
        input_text = '"a" "b" "c" "d" "e"'
        expected = '``a\'\' ``b\'\' ``c\'\' ``d\'\' ``e\'\''
        result = convert_tex_quotes(input_text)
        self.assertEqual(result, expected)
    
    def test_mixed_content(self):
        """測試：文本、引號和特殊字符混合"""
        input_text = 'Text "quote" more-text'
        expected = 'Text ``quote\'\' more-text'
        result = convert_tex_quotes(input_text)
        self.assertEqual(result, expected)


class TestEdgeCases(unittest.TestCase):
    """測試邊界情況和特殊場景"""
    
    def test_empty_quotes(self):
        """測試：空引號"""
        converter = TexQuoteConverter()
        result = converter.convert_line('""')
        self.assertEqual(result, '``\'\'')
    
    def test_single_character_quote(self):
        """測試：引號內只有一個字符"""
        converter = TexQuoteConverter()
        result = converter.convert_line('"x"')
        self.assertEqual(result, '``x\'\'')
    
    def test_quote_with_newline_in_text(self):
        """測試：跨越2行並保有多個引號對"""
        text = '"line1\nquote2"'
        result = convert_tex_quotes(text)
        expected = '``line1\nquote2\'\''
        self.assertEqual(result, expected)
    
    def test_converter_state_reset(self):
        """測試：轉換器的狀態管理"""
        converter = TexQuoteConverter()
        
        # 第一個引號對
        result1 = converter.convert_line('"First"')
        self.assertEqual(result1, '``First\'\'')
        
        # 第二個引號對在新行上
        result2 = converter.convert_line('"Second"')
        self.assertEqual(result2, '``Second\'\'')
    
    def test_long_text_with_quotes(self):
        """測試：包含多個詞語和引號的長文本"""
        input_text = 'The "quick" brown "fox" jumps over the "lazy" dog.'
        expected = 'The ``quick\'\' brown ``fox\'\' jumps over the ``lazy\'\' dog.'
        result = convert_tex_quotes(input_text)
        self.assertEqual(result, expected)


class TestRealWorldExamples(unittest.TestCase):
    """測試實際使用場景"""
    
    def test_dialogue_formatting(self):
        """測試：對話格式轉換"""
        input_text = 'Alice said "Hello" and Bob replied "Hi there".'
        expected = 'Alice said ``Hello\'\' and Bob replied ``Hi there\'\'.'
        result = convert_tex_quotes(input_text)
        self.assertEqual(result, expected)
    
    def test_nested_context(self):
        """測試：嵌套的引號內容"""
        # 交替的引號對，不是真正的嵌套（題目說明沒有嵌套）
        input_text = '"First" contains "Second" quote.'
        expected = '``First\'\' contains ``Second\'\' quote.'
        result = convert_tex_quotes(input_text)
        self.assertEqual(result, expected)
    
    def test_document_header(self):
        """測試：類似文檔頭的內容"""
        input_text = '"Chapter 1: Introduction" section discusses "Basic Concepts".'
        expected = '``Chapter 1: Introduction\'\' section discusses ``Basic Concepts\'\'.'
        result = convert_tex_quotes(input_text)
        self.assertEqual(result, expected)
    
    def test_code_quote(self):
        """測試：代碼樣本中的引號"""
        input_text = 'Use "print" function to output "Hello" message.'
        expected = 'Use ``print\'\' function to output ``Hello\'\' message.'
        result = convert_tex_quotes(input_text)
        self.assertEqual(result, expected)


class TestIntegration(unittest.TestCase):
    """整合測試：完整流程測試"""
    
    def test_full_document_conversion(self):
        """測試：完整文檔的轉換"""
        document = '''First paragraph: "This is a quote."
Second: "Another quote" continues.
Third: "Final" "pair" of "quotes".'''
        
        expected = '''First paragraph: ``This is a quote.\'\'
Second: ``Another quote\'\' continues.
Third: ``Final\'\' ``pair\'\' of ``quotes\'\'.'''
        
        result = convert_tex_quotes(document)
        self.assertEqual(result, expected)
    
    def test_converter_reusability(self):
        """測試：轉換器的可重複使用性"""
        converter = TexQuoteConverter()
        
        # 多次連續轉換
        result1 = converter.convert_line('"First"')
        result2 = converter.convert_line('"Second"')
        result3 = converter.convert_line('"Third"')
        
        self.assertEqual(result1, '``First\'\'')
        self.assertEqual(result2, '``Second\'\'')
        self.assertEqual(result3, '``Third\'\'')


if __name__ == '__main__':
    # 設置 unittest 的詳細模式輸出
    unittest.main(verbosity=2)
