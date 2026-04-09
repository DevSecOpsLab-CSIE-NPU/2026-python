"""
U02. 正則表達式進階技巧 - 單元測試
=================================
測試重點：
1. 預編譯的正則表達式效能更好
2. sub 可以使用回呼函數進行動態替換
3. 保持大小寫一致的替換
"""

import unittest
import re
from calendar import month_abbr


class TestRegexAdvanced(unittest.TestCase):
    """正則表達式進階技巧的單元測試"""

    def test_precompiled_regex_performance_matters(self):
        """測試：預編譯的正則表達式"""
        text = "Today is 11/27/2012. PyCon starts 3/13/2013."
        
        # 預編譯一次，可重複使用
        datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
        result = datepat.findall(text)
        
        self.assertEqual(result, [("11", "27", "2012"), ("3", "13", "2013")])

    def test_sub_with_callback_function(self):
        """測試：sub 回呼函數進行動態替換"""
        text = "Today is 11/27/2012. PyCon starts 3/13/2013."
        datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
        
        # 定義回呼函數，接收 Match 物件
        def change_date(m: re.Match) -> str:
            mon_name = month_abbr[int(m.group(1))]
            return f"{m.group(2)} {mon_name} {m.group(3)}"
        
        result = datepat.sub(change_date, text)
        expected = "Today is 27 Nov 2012. PyCon starts 13 Mar 2013."
        self.assertEqual(result, expected)

    def test_case_preserving_substitution(self):
        """測試：保持大小寫一致的替換"""
        def matchcase(word: str):
            """返回一個替換函數，保持原始大小寫"""
            def replace(m: re.Match) -> str:
                t = m.group()
                if t.isupper():
                    return word.upper()
                if t.islower():
                    return word.lower()
                if t[0].isupper():
                    return word.capitalize()
                return word
            return replace

        s = "UPPER PYTHON, lower python, Mixed Python"
        result = re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE)
        expected = "UPPER SNAKE, lower snake, Mixed Snake"
        self.assertEqual(result, expected)

    def test_findall_with_groups(self):
        """測試：findall 回傳捕獲分組"""
        text = "The price is $100 and $250"
        pattern = re.compile(r"\$(\d+)")
        
        # findall 回傳捕獲分組的內容
        matches = pattern.findall(text)
        self.assertEqual(matches, ["100", "250"])


if __name__ == "__main__":
    unittest.main()
