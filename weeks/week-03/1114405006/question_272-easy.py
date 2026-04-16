"""UVA 272 的簡易版本 - 最容易背誦的實現。

這份簡化版特點：
- 去掉所有不必要的複雜度
- 直白展示核心邏輯：計數引號、交替替換
- 適合快速理解和背誦的場景
- 完全可以在筆試中快速手寫

背誦要點（三行總結）：
1. 遍歷每個字符
2. 遇到 " 就累加計數器
3. 計數是奇數用 ``，偶數用 ''

對應的 TeX 規則：
- 左引號（開始引用）：`` （兩個 backtick）
- 右引號（結束引用）：'' （兩個 apostrophe）
- 成對出現，交替使用

時間複雜度：O(n)，空間複雜度：O(n)
"""

import sys


def convert_quotes_easy(text: str) -> str:
    """簡易版：將雙引號轉換成 TeX 引號。
    
    這是最小化的實現，易於理解和背誦。
    
    邏輯流程：
    1. result 列表存放轉換後的字符
    2. counter 記錄遇到的 " 的個數
    3. 逐字符掃描輸入文本
    4. 非引號字符直接加入結果
    5. 遇到 " 就根據 counter 決定替換方式
    
    參數：
    - text：輸入的文本字符串
    
    回傳：
    - 轉換後的字符串
    
    範例：
    - '"Hello"' -> '``Hello\\'\\''
    - '"A" "B"' -> '``A\\'\\'  ``B\\'\\'
    """
    result = []
    counter = 0  # 計數器，追蹤第幾個引號
    
    # 逐字符掃描文本
    for char in text:
        if char == '"':
            # 遇到普通雙引號，先遞增計數器
            counter += 1
            
            # 根據計數器的奇偶性判斷用哪種 TeX 引號
            if counter % 2 == 1:
                # 計數器是 1, 3, 5... 時，用左引號 `` 開始引用
                result.append('``')
            else:
                # 計數器是 2, 4, 6... 時，用右引號 '' 結束引用
                result.append("''")
        else:
            # 不是雙引號的字符直接加入
            # 包括字母、數字、標點符號、換行符等
            result.append(char)
    
    # 把 list 中的所有字符串連接成一個字符串並返回
    return ''.join(result)


def process_input(text: str) -> str:
    """處理輸入文本。
    
    這個包裝函式統一處理輸入，便於擴展。
    目前直接調用 convert_quotes_easy。
    
    參數：
    - text：可能包含換行符的多行文本
    
    回傳：
    - 轉換後的文本，換行符保持
    
    說明：
    - 因為 " 是引號字符，計數器在全文範圍內連續進行
    - 換行符不是引號，所以引號計數跨越行界
    """
    return convert_quotes_easy(text)


def main():
    """主函式：讀取標準輸入，轉換，輸出。
    
    標準輸入/輸出流程：
    1. sys.stdin.read()：讀取所有輸入直到 EOF
    2. process_input()：轉換引號
    3. print(..., end='')：輸出，不添加額外換行
    
    為什麼用 end=''？
    - 輸入文本本身可能已包含換行符
    - 用 end='' 可以保留原來的換行位置
    - 避免多出一行空行
    """
    # 一次性讀取所有輸入（到 EOF）
    input_text = sys.stdin.read()
    
    # 轉換引號
    output_text = process_input(input_text)
    
    # 輸出結果，不加額外換行
    print(output_text, end='')


if __name__ == '__main__':
    main()
