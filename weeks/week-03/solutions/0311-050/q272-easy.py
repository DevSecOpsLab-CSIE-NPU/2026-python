# 檔名: q272-easy.py
# 這是 UVA 272 的簡易好記版 (Easy Version)

import sys

# 1. 狀態變數放在迴圈最外面，確保換行時引號的開關狀態不會被重置
is_first = True

# 2. 直接逐行讀取系統輸入
for line in sys.stdin:
    # 準備一個空字串，用來收集這一行替換後的結果
    result = ""
    
    # 3. 逐一檢查這行裡面的每一個字元
    for c in line:
        if c == '"':
            # 遇到引號，根據目前的開關狀態決定替換成什麼
            if is_first:
                result += "``"  # 開頭引號
            else:
                result += "''"  # 結尾引號
            # 狀態反轉 (True 變 False，False 變 True)
            is_first = not is_first
        else:
            # 一般字元直接照抄貼上
            result += c
            
    # 4. 印出結果。因為 line 本身已經自帶換行符號 ('\n')，所以要加上 end="" 避免空行
    print(result, end="")