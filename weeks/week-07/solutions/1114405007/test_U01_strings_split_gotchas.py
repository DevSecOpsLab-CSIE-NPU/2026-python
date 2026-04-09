"""
U01. 字串分割與匹配的陷阱 - 單元測試
========================================
測試重點：
1. 捕獲分組保留分隔符
2. startswith 必須傳 tuple，不能傳 list
3. strip 只處理頭尾，不處理中間空白
"""

import unittest
import re


class TestStringsSplitGotchas(unittest.TestCase):
    """字串分割與匹配陷阱的單元測試"""

    def test_capturing_group_preserves_delimiters(self):
        """測試：捕獲分組保留分隔符"""
        # 使用捕獲分組 (;|,|\s) 來保留分隔符
        line = "asdf fjdk; afed, fjek,asdf, foo"
        fields = re.split(r"(;|,|\s)\s*", line)
        
        # 偶數索引是實際值，奇數索引是分隔符
        values = fields[::2]
        delimiters = fields[1::2] + [""]
        
        # 重建字串應該跟原始字串相同（去掉多餘空白）
        rebuilt = "".join(v + d for v, d in zip(values, delimiters))
        self.assertEqual(rebuilt, "asdf fjdk;afed,fjek,asdf,foo")

    def test_startswith_requires_tuple_not_list(self):
        """測試：startswith 必須傳 tuple，不能傳 list"""
        url = "http://www.python.org"
        choices = ["http:", "ftp:"]
        
        # 直接傳 list 會拋出 TypeError
        with self.assertRaises(TypeError):
            url.startswith(choices)  # type: ignore
        
        # 正確做法：轉成 tuple
        self.assertTrue(url.startswith(tuple(choices)))

    def test_strip_only_handles_edges_not_middle(self):
        """測試：strip 只處理頭尾，不處理中間空白"""
        s = "  hello     world  "
        
        # strip() 只移除頭尾空白，中間的多餘空白保留
        stripped = s.strip()
        self.assertEqual(stripped, "hello     world")
        
        # 若要移除所有空白，用 replace
        no_space = s.replace(" ", "")
        self.assertEqual(no_space, "helloworld")
        
        # 若要標準化空白（多個空白變一個），用正則
        normalized = re.sub(r"\s+", " ", s.strip())
        self.assertEqual(normalized, "hello world")

    def test_generator_cleanup_efficient(self):
        """測試：生成器逐行清理（高效）"""
        lines = ["  apple  \n", "  banana  \n"]
        
        # 用生成器逐行清理，不預載入記憶體
        cleaned = list(l.strip() for l in lines)
        self.assertEqual(cleaned, ["apple", "banana"])


if __name__ == "__main__":
    unittest.main()
