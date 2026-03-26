# -*- coding: utf-8 -*-
"""
R04. 位元組字串操作 - 單元測試程式

【學習目標】
本程式針對位元組字串（bytes）的各種操作進行單元測試，
幫助理解 bytes 與 str 的差異以及正確的使用方式。

【重要概念】
1. bytes 是「位元組字串」，儲存的是原始二進位資料
2. bytes 支援大部分 str 的方法，但索引行為不同
3. bytes 的索引回傳整數（ASCII 碼），str 的索引回傳字元
4. 正規表達式與 bytes 搭配時，模式需使用 rb"..." 格式
"""

import unittest
import re


class TestBytesStringOperations(unittest.TestCase):
    """測試位元組字串的基本操作"""

    def test_bytes_slicing(self):
        """
        測試 bytes 切片操作

        說明：bytes 物件可以使用切片（slicing）來取得子位元組。
        切片語法與 str 相同，格式為 [start:end]，會返回新的 bytes 物件。

        範例：
        - b"Hello World"[0:5] → b'Hello'
        - b"Hello World"[6:] → b'World'
        """
        data = b"Hello World"
        # 測試切片取得前半部分
        self.assertEqual(data[0:5], b"Hello")
        # 測試切片從指定位置到結尾
        self.assertEqual(data[6:], b"World")
        # 測試負索引切片
        self.assertEqual(data[-5:], b"World")

    def test_bytes_startswith(self):
        """
        測試 bytes 的 startswith() 方法

        說明：startswith() 用來判斷位元組字串是否以指定的前綴開頭。
        注意：前綴參數必須是 bytes 類型（字面量前需加 b）。

        範例：
        - b"Hello World".startswith(b"Hello") → True
        - b"Hello World".startswith(b"World") → False
        """
        data = b"Hello World"
        self.assertTrue(data.startswith(b"Hello"))
        self.assertFalse(data.startswith(b"World"))
        # 測試空字首（任何位元組都以空字首開頭）
        self.assertTrue(data.startswith(b""))

    def test_bytes_split(self):
        """
        測試 bytes 的 split() 方法

        說明：split() 預設以空白字元分隔位元組字串，返回 bytes 的列表。
        這與 str.split() 的行為一致。

        範例：
        - b"Hello World".split() → [b'Hello', b'World']
        - b"a,b,c".split(b",") → [b'a', b'b', b'c']
        """
        data = b"Hello World"
        result = data.split()
        # 驗證分割結果為包含兩個元素的列表
        self.assertEqual(result, [b"Hello", b"World"])
        self.assertEqual(len(result), 2)
        # 驗證每個元素都是 bytes 類型
        self.assertIsInstance(result[0], bytes)
        self.assertIsInstance(result[1], bytes)

    def test_bytes_replace(self):
        """
        測試 bytes 的 replace() 方法

        說明：replace() 用來替換位元組字串中的子字串。
        語法為 replace(old, new)，old 和 new 都必須是 bytes。

        範例：
        - b"Hello World".replace(b"Hello", b"Hi") → b'Hi World'
        """
        data = b"Hello World"
        # 測試基本替換
        result = data.replace(b"Hello", b"Hi")
        self.assertEqual(result, b"Hi World")
        # 測試替換後字串長度（"Hi World" = 8 個字元）
        self.assertEqual(len(result), 8)
        # 測試不存在的替換目標（原字串不變）
        result2 = data.replace(b"Python", b"Java")
        self.assertEqual(result2, b"Hello World")

    def test_bytes_regex_split(self):
        """
        測試 bytes 搭配正規表達式分割

        說明：使用 re.split() 搭配 bytes 時，正規表達式模式必須使用
        rb"..." 格式（raw bytes），而不是 r"..."。

        重要：
        - 錯誤寫法：re.split(r":", b"FOO:BAR")  → 會報錯
        - 正確寫法：re.split(rb":", b"FOO:BAR") → [b'FOO', b'BAR']

        範例：
        - re.split(rb"[:,]", b"FOO:BAR,SPAM") → [b'FOO', b'BAR', b'SPAM']
        """
        raw = b"FOO:BAR,SPAM"
        # 使用正規表達式以冒號或逗號分隔
        result = re.split(rb"[:,]", raw)
        self.assertEqual(result, [b"FOO", b"BAR", b"SPAM"])
        # 驗證結果數量
        self.assertEqual(len(result), 3)

    def test_bytes_indexing_vs_string(self):
        """
        測試 bytes 與 str 索引行為的差異

        【重要差異】
        - str[索引] → 返回「字元」（字串類型），例如 'H'
        - bytes[索引] → 返回「整數」（ASCII 碼），例如 72

        這是因為：
        - str 是 Unicode 字元的序列
        - bytes 是 0-255 整數的序列

        如何從 bytes 取得字元？
        - 方法一：chr(bytes[索引])，例如 chr(72) → 'H'
        - 方法二：bytes.decode()[索引]，例如 b"Hello".decode()[0] → 'H'

        範例：
        - "Hello"[0] → 'H'（字元，str 類型）
        - b"Hello"[0] → 72（整數，int 類型）
        """
        # 建立測試用的 str 和 bytes
        a = "Hello"
        b = b"Hello"

        # str 索引返回字元
        self.assertEqual(a[0], "H")
        self.assertIsInstance(a[0], str)

        # bytes 索引返回整數（ASCII 碼）
        self.assertEqual(b[0], 72)  # 72 是 'H' 的 ASCII 碼
        self.assertIsInstance(b[0], int)

        # 驗證 ASCII 碼的對應關係
        self.assertEqual(ord("H"), 72)
        self.assertEqual(chr(72), "H")

        # 如何從 bytes 取得字元
        self.assertEqual(chr(b[0]), "H")
        self.assertEqual(b.decode()[0], "H")

    def test_bytes_formatting(self):
        """
        測試 bytes 的格式化方式

        【重要限制】
        bytes 類型不能直接使用 format() 方法！

        解決方法：
        1. 先用 str 的 format() 格式化字串
        2. 然後用 .encode() 轉換為 bytes

        範例：
        "{:10s} {:10d}".format("ACME", 100).encode("ascii")
        → b'ACME            100'

        格式化符號說明：
        - {:10s} → 字串，總寬度 10，靠左對齊
        - {:10d} → 整數，總寬度 10，靠右對齊
        """
        # 使用 format() 後再 encode() 的方式
        formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")

        # 驗證結果是 bytes 類型
        self.assertIsInstance(formatted, bytes)

        # 驗證結果以預期的內容開頭和結尾
        self.assertTrue(formatted.startswith(b"ACME"))
        self.assertTrue(formatted.endswith(b"100"))

        # 驗證總長度：{:10s} 佔 10 格 + 格式字串中的空格 + {:10d} 佔 10 格 = 21
        self.assertEqual(len(formatted), 21)


class TestBytesAdditionalOperations(unittest.TestCase):
    """測試位元組字串的其他常用操作"""

    def test_bytes_endswith(self):
        """測試 bytes 的 endswith() 方法"""
        data = b"Hello World"
        self.assertTrue(data.endswith(b"World"))
        self.assertFalse(data.endswith(b"Hello"))

    def test_bytes_upper_lower(self):
        """
        測試 bytes 的大小寫轉換

        注意：bytes 使用 .upper() 和 .lower() 方法時，
        返回的仍是 bytes 類型。
        """
        data = b"Hello"
        self.assertEqual(data.upper(), b"HELLO")
        self.assertEqual(data.lower(), b"hello")

    def test_bytes_join(self):
        """
        測試 bytes 的 join() 方法

        說明：b''.join(list_of_bytes) 用來連接多個 bytes。
        """
        parts = [b"Hello", b"World"]
        self.assertEqual(b" ".join(parts), b"Hello World")
        self.assertEqual(b"-".join(parts), b"Hello-World")

    def test_bytes_encode_decode(self):
        """
        測試 encode() 和 decode() 方法

        【相互轉換】
        - encode() : str → bytes（文字轉位元組）
        - decode() : bytes → str（位元組轉文字）

        常用編碼：
        - utf-8 : 萬用編碼，支援各國語言
        - ascii : 僅支援英文字母和基本符號
        """
        # str → bytes（編碼）
        text = "Hello"
        data = text.encode("utf-8")
        self.assertEqual(data, b"Hello")
        self.assertIsInstance(data, bytes)

        # bytes → str（解碼）
        restored = data.decode("utf-8")
        self.assertEqual(restored, "Hello")
        self.assertIsInstance(restored, str)

    def test_bytes_count(self):
        """測試 bytes 的 count() 方法"""
        data = b"Hello World"
        # 計算 'o' 出現次數
        self.assertEqual(data.count(b"o"), 2)
        # 計算 'l' 出現次數
        self.assertEqual(data.count(b"l"), 3)

    def test_bytes_find(self):
        """測試 bytes 的 find() 方法"""
        data = b"Hello World"
        # 找到時返回索引位置
        self.assertEqual(data.find(b"World"), 6)
        # 找不到時返回 -1
        self.assertEqual(data.find(b"Python"), -1)


if __name__ == "__main__":
    # 執行所有測試，verbosity=2 顯示詳細輸出
    unittest.main(verbosity=2)
