"""
【題目 272: TeX 引號轉換】
 
題目來源: https://zerojudge.tw/ShowProblem?problemid=c007

=====================================================================
【題目說明】

TeX 是一個文書排版軟體，需要使用有方向的雙引號來顯示引文。
本程序將普通的雙引號 (") 轉換為 TeX 風格的有方向雙引號：

- 開啟引號（第1、3、5... 個）: " → `` （兩個左單引號）
- 關閉引號（第2、4、6... 個）: " → '' （兩個右單引號）

【轉換範例】

輸入:  "To be or not to be," quoth the bard, "that is the question."

輸出:  ``To be or not to be,'' quoth the bard, ``that is the question.''

【核心概念】

1. 狀態追蹤: 使用 inside_quote 標誌追蹤是否正在引號內
2. 交替轉換: 奇數個引號使用開啟形式，偶數個使用關閉形式
3. 保留內容: 引號內的所有字符（含特殊字符）都原樣保留
4. 多行支持: 引號狀態在多行間保持一致

=====================================================================
"""

import sys


class TexQuoteConverter:
    """
    TeX 引號轉換器
    
    功能說明:
        將文本中的普通雙引號轉換為 TeX 風格的有方向雙引號
    
    狀態管理:
        - inside_quote (bool): 追蹤目前是否位於引號內部
        - False: 下一個引號是開啟引號 (`)
        - True: 下一個引號是關閉引號 (')
    """
    
    def __init__(self):
        """
        初始化轉換器
        
        功能:
            1. 初始化 inside_quote 標誌為 False
            2. 準備好接收第一個開啟引號
        """
        # 追蹤目前是否在引號內
        # 初始值為 False：表示還沒進入任何引號
        self.inside_quote = False
    
    def convert_quote(self, char):
        """
        轉換單個字符（特別是引號）
        
        演算法邏輯:
        1. 如果字符是引號 ("):
           - 檢查 inside_quote 狀態
           - 若為 False (還未進入引號): 設為 True，返回 `` (開啟引號)
           - 若為 True (已在引號內): 設為 False，返回 '' (關閉引號)
        2. 如果不是引號: 原樣返回該字符
        
        狀態轉移圖:
           False (在引號外) 
             ↓ 遇到 "
           True (在引號內)
             ↓ 遇到 "
           False (回到引號外)
             ↓ 遇到 "
           True ...
        
        參數:
            char (str): 單個字符，通常是文本中的 " 或其他字符
            
        返回:
            str: 轉換後的字符
                 - 如果輸入是 ": 返回 `` 或 ''
                 - 否則: 返回原字符不變
        """
        if char == '"':
            # 引號字符處理邏輯
            if not self.inside_quote:
                # 目前在引號外，這是開啟引號
                self.inside_quote = True
                return '``'  # 返回左雙引號（兩個左單引號組成）
            else:
                # 目前在引號內，這是關閉引號
                self.inside_quote = False
                return "''"  # 返回右雙引號（兩個右單引號組成）
        else:
            # 非引號字符，保持不變
            return char
    
    def convert_line(self, line):
        """
        轉換一行文字的所有引號
        
        處理流程:
        1. 遍歷輸入行的每個字符
        2. 對每個字符調用 convert_quote() 方法
        3. 將結果逐個收集到 result 列表
        4. 最後將列表中的字符串連接成一個字符串返回
        
        重要特性:
        - 跨越行的狀態保持: 轉換器的 inside_quote 狀態在多行間保持一致
          這意味著如果一行結束時處於引號內，下一行會繼續該狀態
        - 字符逐個處理: 逐字符處理確保精確控制每個引號的轉換
        - 結果字符串構建: 使用列表和 join() 方式，效率高於串聯
        
        參數:
            line (str): 輸入的一行文字（可能包含 0 個或多個引號）
            
        返回:
            str: 轉換後的文字
                 - 所有 " 已根據上下文轉換為 `` 或 ''
                 - 其他字符保持原樣
                 
        範例:
            輸入: 'He said "Hello"'
            處理:
              H → H
              e → e
              (空格) → (空格)
              s → s
              a → a
              i → i
              d → d
              (空格) → (空格)
              " → `` (inside_quote: False → True)
              H → H
              e → e
              l → l
              l → l
              o → o
              " → '' (inside_quote: True → False)
            輸出: 'He said ``Hello\'\''
        """
        result = []
        # 逐字符處理輸入行
        for char in line:
            # 調用轉換函數處理每個字符
            result.append(self.convert_quote(char))
        # 將列表中的所有字符串元素連接成一個完整的字符串
        return ''.join(result)
    
    def reset(self):
        """重置轉換器狀態（如果需要）"""
        self.inside_quote = False


def convert_tex_quotes(text):
    """
    轉換整段文本（可能包含多行）的引號
    
    功能概述:
        封裝轉換器，提供簡單的接口來轉換多行文本
    
    演算法步驟:
    1. 建立一個 TexQuoteConverter 轉換器實例
    2. 使用 '\\n' 分割輸入文本為多行
    3. 對每一行調用轉換器的 convert_line() 方法
    4. 將轉換後的行逐個收集到 result_lines 列表
    5. 使用 '\\n' 將所有行重新連接成完整的文本
    
    狀態管理:
        轉換器在所有行間保持狀態一致
        如果第一行結束時在開啟引號狀態，第二行會繼續在該狀態下處理
    
    參數:
        text (str): 輸入文本，可包含多行（用 \\n 分隔）
        
    返回:
        str: 轉換後的文本，格式完全相同但引號已轉換
        
    使用範例:
        >>> text = '"Hello" and "World"'
        >>> result = convert_tex_quotes(text)
        >>> print(result)
        ``Hello'' and ``World''
    """
    # 建立轉換器實例（初始狀態: inside_quote = False）
    converter = TexQuoteConverter()
    # 使用換行符分割文本為多行列表
    lines = text.split('\\n')
    result_lines = []
    
    # 遍歷每一行
    for line in lines:
        # 轉換該行的引號，添加到結果列表
        result_lines.append(converter.convert_line(line))
    
    # 使用換行符將所有轉換後的行重新連接成完整文本
    return '\\n'.join(result_lines)


def main():
    """
    主程序：從標準輸入讀取並轉換引號
    
    程序流程:
    1. 建立 TexQuoteConverter 轉換器實例
    2. 進入無限迴圈，逐行讀取輸入
    3. 對每一行調用轉換器的 convert_line() 方法
    4. 將轉換後的行輸出到標準輸出
    5. 當遇到 EOFError（文件末尾）時正常結束程序
    
    輸入方式:
        - 從標準輸入（鍵盤或檔案重定向）逐行讀取
        - 直到 EOF (End Of File)
    
    輸出方式:
        - 轉換後的每一行輸出到標準輸出
        - 保持原有的行結構
    
    異常處理:
        - 捕捉 EOFError: 正常的程序結束信號
        - 其他異常: 不捕捉，由系統處理
    
    演算法:
        使用單一的 TexQuoteConverter 實例，確保所有行的引號狀態一致
        這對於跨越多行的引號對至關重要
    """
    # 建立轉換器，使用一個實例保持全局狀態
    converter = TexQuoteConverter()
    
    try:
        # 無限迴圈：逐行讀取輸入
        while True:
            # 從標準輸入讀取一行（不包括換行符）
            line = input()
            # 轉換該行的引號
            converted = converter.convert_line(line)
            # 輸出轉換後的行
            print(converted)
    except EOFError:
        # 到達文件末尾，這是正常的結束方式
        # Python 在讀取超過檔案末尾時拋出 EOFError
        # 我們捕捉此異常並優雅地結束程序
        pass


if __name__ == '__main__':
    """
    主程序進入點
    
    說明:
        - 當此文件直接執行時（而非被導入），執行 main() 函數
        - 如果被其他程序導入，只會導入類和函數，不執行 main()
    """
    # 示例 1：簡單的引號對
    print("=" * 60)
    print("範例 1: 簡單的引號對")
    print("=" * 60)
    
    # 演示簡單的單一引號對轉換
    example1 = 'She said "Hello"'
    result1 = convert_tex_quotes(example1)
    print(f"輸入:  {example1}")
    print(f"輸出:  {result1}")
    print()
    
    # 示例 2：莎士比亞引用
    print("=" * 60)
    print("範例 2: 題目中的莎士比亞引用")
    print("=" * 60)
    
    # 演示複雜的多引號對轉換
    # 這是題目中提供的原始範例
    example2 = '"To be or not to be," quoth the bard, "that is the question."'
    result2 = convert_tex_quotes(example2)
    print(f"輸入:  {example2}")
    print(f"輸出:  {result2}")
    print()
    
    # 示例 3：多個引號對
    print("=" * 60)
    print("範例 3: 多個引號對")
    print("=" * 60)
    
    # 演示交替的多個引號對
    example3 = '"First" and "Second" and "Third"'
    result3 = convert_tex_quotes(example3)
    print(f"輸入:  {example3}")
    print(f"輸出:  {result3}")
    print()
    
    # 示例 4：沒有引號的文本
    print("=" * 60)
    print("範例 4: 沒有引號的文本")
    print("=" * 60)
    
    # 演示不包含引號的文本保持原樣
    example4 = 'This is plain text without quotes'
    result4 = convert_tex_quotes(example4)
    print(f"輸入:  {example4}")
    print(f"輸出:  {result4}")
    print()
