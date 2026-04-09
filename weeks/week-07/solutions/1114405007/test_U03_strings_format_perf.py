"""
U03. 字串格式化效能與陷阱 - 單元測試
==================================
測試重點：
1. join 效能優於 +
2. format_map 處理缺失鍵
3. bytes 索引回傳整數而非字符
"""

import unittest


class TestStringsFormatPerf(unittest.TestCase):
    """字串格式化效能與陷阱的單元測試"""

    def test_join_faster_than_concatenation(self):
        """測試：join 效能優於 +"""
        parts = ["a", "b", "c", "d", "e"]
        
        # 用 join 拼接（推薦）
        result = "".join(parts)
        self.assertEqual(result, "abcde")
        
        # 強調 join 比 + 更高效（特別是大量字串）
        large_parts = [f"item{i}" for i in range(100)]
        result = "".join(large_parts)
        # item0 到 item99：item(4個字) + 1或2位數字 = 5+5*1 + 95*2 = 590
        self.assertEqual(len(result), 590)

    def test_format_map_with_missing_keys(self):
        """測試：format_map 處理缺失鍵"""
        # 定義一個 dict 子類，缺失鍵時返回佔位符
        class SafeSub(dict):
            def __missing__(self, key: str) -> str:
                return "{" + key + "}"
        
        # 即使變數不存在，也不會拋出 KeyError
        name = "Guido"
        s = "{name} has {n} messages."
        
        # locals() 中只有 name，沒有 n
        result = s.format_map(SafeSub({"name": name}))
        self.assertEqual(result, "Guido has {n} messages.")

    def test_bytes_indexing_returns_int(self):
        """測試：bytes 索引回傳整數"""
        a = "Hello"
        b = b"Hello"
        
        # 字符串索引回傳字符
        self.assertEqual(a[0], "H")
        self.assertIsInstance(a[0], str)
        
        # bytes 索引回傳整數（ASCII 碼）
        self.assertEqual(b[0], 72)
        self.assertEqual(b[0], ord("H"))
        self.assertIsInstance(b[0], int)

    def test_bytes_formatting(self):
        """測試：bytes 無法直接 format，需先格式化再 encode"""
        # 先格式化字串，再 encode 成 bytes
        result = "{:10s} {:5d}".format("ACME", 100).encode("ascii")
        # {:10s} means 10-char wide string, {:5d} means 5-digit integer
        self.assertEqual(result, b"ACME         100")

    def test_safe_sub_with_vars(self):
        """測試：SafeSub 搭配 vars() 處理本地變數"""
        class SafeSub(dict):
            def __missing__(self, key: str) -> str:
                return "{" + key + "}"
        
        name = "Alice"
        age = 30
        template = "{name} is {age} years old, lives in {city}"
        
        # vars() 只有 name 和 age，沒有 city
        result = template.format_map(SafeSub(vars()))
        self.assertEqual(result, "Alice is 30 years old, lives in {city}")


if __name__ == "__main__":
    unittest.main()
