"""
UVA 272 - TEX Quotes 簡單版

題目說明：
TeX 排版軟體使用方向的雙引號來標註引用內容。
- 左雙引號：``
- 右雙引號：''

一般鍵盤的雙引號 " 需要轉換為 TeX 風格引號。
轉換規則：
- 第一個 " 換成 ``
- 第二個 " 換成 ''
- 第三個 " 換成 ``
- 第四個 " 換成 ''
- 以此類推...

簡單記憶口號：奇數 `` 偶數 ''
（奇數次出現的引號用 ``，偶數次出現的用 ''）
"""

import sys
import unittest


def tex_quotes(text):
    """
    將文字中的雙引號轉換為 TeX 風格的引號

    參數說明：
        text: 輸入的原始文字（包含一般雙引號 "）

    回傳值：
        轉換後的文字（雙引號被替換為 TeX 風格引號）

    演算法說明：
        1. 建立一個空的列表 result 用來存放轉換後的字元
        2. 建立一個計數器 count，初始值為 0，用來記錄目前處理到第幾個雙引號
        3. 逐一檢視輸入文字中的每個字元：
           - 如果是雙引號 "：
             * 當 count 為偶數（0, 2, 4...）時，替換為 ``（左雙引號）
             * 當 count 為奇數（1, 3, 5...）時，替換為 ''（右雙引號）
             * 將 count 加 1
           - 如果不是雙引號，直接將該字元加入 result 列表
        4. 最後將列表中的所有字元組合成一個字串並回傳

    範例：
        輸入: "Hello" World
        處理過程:
          - 第1個 " → `` (count=0, 偶數)
          - 第2個 " → '' (count=1, 奇數)
        輸出: ``Hello'' World
    """
    result = []  # 存放轉換結果的列表
    count = 0  # 計數器：記錄目前處理到第幾個雙引號

    for char in text:  # 逐一處理每個字元
        if char == '"':  # 判斷是否為雙引號
            if count % 2 == 0:  # 偶數次：使用左雙引號 ``
                result.append("``")
            else:  # 奇數次：使用右雙引號 ''
                result.append("''")
            count += 1  # 計數器遞增，準備處理下一個引號
        else:
            result.append(char)  # 非雙引號字元直接加入結果

    return "".join(result)  # 將列表組合成字串後回傳


def tex_quotes_easy(text):
    """
    另一種簡單的寫法：使用列表存取引號替換順序

    概念說明：
        建立一個列表 quotes = ["``", "''"]
        使用 i % 2 來決定要用哪個引號
        i 從 0 開始，每遇到一個雙引號就遞增

    這個寫法的優點：
        程式碼更簡潔，不需要寫 if-else 判斷
        只要知道位置 mod 2 的值就能決定用哪個引號
    """
    quotes = ["``", "''"]  # 引號列表：索引 0 是 ``，索引 1 是 ''
    result = []
    i = 0

    for char in text:
        if char == '"':
            result.append(quotes[i % 2])  # 使用模運算決定引號
            i += 1
        else:
            result.append(char)

    return "".join(result)


def tex_quotes_simple(text):
    """
    最直觀的寫法：使用布林值 toggle 切換

    概念說明：
        用一個布林變數 left 來記錄當前應該輸出左引號還是右引號
        每次遇到雙引號時，切換 left 的值（True → False → True）

    這個寫法的優點：
        邏輯最直觀，類似於電燈開關切換
        程式碼易讀性高
    """
    result = []
    left = True  # True 表示下一個是左引號 ``，False 表示右引號 ''

    for char in text:
        if char == '"':
            result.append("``" if left else "''")
            left = not left  # 切換狀態
        else:
            result.append(char)

    return "".join(result)


class TestTexQuotes(unittest.TestCase):
    """
    TEX Quotes 轉換功能的單元測試類別

    測試方法說明：
    - test_basic_quote_conversion: 測試基本引號轉換（題目範例）
    - test_multiple_pairs: 測試多對引號的情況
    - test_only_quotes: 測試只有引號沒有其他文字的情況
    - test_quotes_with_newlines: 測試包含換行符的情況
    - test_odd_number_of_quotes: 測試奇數個引號的情況
    - test_single_quote_pair: 測試單一對引號
    - test_no_quotes: 測試沒有引號的情況
    - test_empty_string: 測試空字串
    """

    def test_basic_quote_conversion(self):
        """
        測試基本引號轉換

        這是題目提供的範例：
        輸入: "To be or not to be," quoth the bard, "that is the question."
        輸出: ``To be or not to be,'' quoth the bard, ``that is the question.'

        說明：
        - 第1個 " → ``
        - 第2個 " → ''
        - 第3個 " → ``
        - 第4個 " → ''
        """
        input_text = '"To be or not to be," quoth the bard, "that is the question."'
        expected = "``To be or not to be,'' quoth the bard, ``that is the question.''"
        self.assertEqual(tex_quotes(input_text), expected)

    def test_multiple_pairs(self):
        """
        測試多對引號

        測試連續多個獨立的引號對：
        輸入: "first" "second" "third"
        輸出: ``first'' ``second'' ``third''

        說明：共6個雙引號
        - 第1,3,5個（奇數）→ ``
        - 第2,4,6個（偶數）→ ''
        """
        input_text = '"first" "second" "third"'
        expected = "``first'' ``second'' ``third''"
        self.assertEqual(tex_quotes(input_text), expected)

    def test_only_quotes(self):
        """
        測試只有引號的情況

        測試連續兩個雙引號：
        輸入: ""
        輸出: ``''

        說明：
        - 第1個 " → ``
        - 第2個 " → ''
        """
        input_text = '""'
        expected = "``''"
        self.assertEqual(tex_quotes(input_text), expected)

    def test_quotes_with_newlines(self):
        """
        測試包含換行符的情況

        確保換行符不會影響引號的計數：
        輸入: "Hello"\n"World"
        輸出: ``Hello''\n``World''

        說明：換行符視為一般字元，不影響計數
        """
        input_text = '"Hello"\n"World"'
        expected = "``Hello''\n``World''"
        self.assertEqual(tex_quotes(input_text), expected)

    def test_odd_number_of_quotes(self):
        """
        測試奇數個引號

        根據題目說明，輸入保證會有偶數個雙引號。
        此測試確保程式在奇數個引號時也能正確運作：
        輸入: "Hello" "World"
        輸出: ``Hello'' ``World''

        說明：這裡測試的是多對引號的情況（總數仍是偶數）
        """
        input_text = '"Hello" "World"'
        expected = "``Hello'' ``World''"
        self.assertEqual(tex_quotes(input_text), expected)

    def test_single_quote_pair(self):
        """
        測試單一對引號

        最基本的一組引號：
        輸入: "Hello World"
        輸出: ``Hello World''

        說明：
        - 第1個 " → ``
        - 第2個 " → ''
        """
        input_text = '"Hello World"'
        expected = "``Hello World''"
        self.assertEqual(tex_quotes(input_text), expected)

    def test_no_quotes(self):
        """
        測試沒有引號的情況

        確保沒有雙引號時，輸出與輸入完全相同：
        輸入: Hello, world!
        輸出: Hello, world!
        """
        input_text = "Hello, world!"
        self.assertEqual(tex_quotes(input_text), input_text)

    def test_empty_string(self):
        """
        測試空字串

        確保空字串也能正確處理：
        輸入: （空字串）
        輸出: （空字串）
        """
        self.assertEqual(tex_quotes(""), "")


if __name__ == "__main__":
    import argparse

    # 命令列參數解析器
    # 用法：
    #   python test_QUESTION-272-easy.py          # 從 stdin 讀取輸入並處理
    #   python test_QUESTION-272-easy.py --test    # 執行單元測試
    parser = argparse.ArgumentParser(description="UVA 272 - TEX Quotes 轉換程式")
    parser.add_argument("--test", action="store_true", help="執行單元測試")
    args = parser.parse_args()

    if args.test:
        # 執行單元測試模式
        unittest.main()
    else:
        # 正常模式：從標準輸入讀取資料並處理後輸出
        output = tex_quotes(sys.stdin.read())
        print(output, end="")
