"""UVA 272 - TeX Quoting (easy 版)

題目重點：
- 將普通雙引號 " 轉換成 TeX 格式
- 第 1, 3, 5, ... 個引號 → `` （開啟引號）
- 第 2, 4, 6, ... 個引號 → '' （關閉引號）
- 其他字元保持不變
- 引號計數跨行連續進行

核心邏輯（超簡單版）：
- 用一個布林開關 opening 追蹤目前狀態
- True = 開啟引號，False = 關閉引號
- 每次見到 " 就切換一次狀態
- 根據狀態輸出對應的符號
"""

import sys

# opening 開關：True 表示下一個引號要「開啟」，False 表示要「關閉」
# 初始是 True，因為第一個引號一定是開啟
opening = True
result = ""

# 逐行讀入標準輸入
for line in sys.stdin:
    # 逐字掃過每一行
    for char in line:
        if char == '"':
            # 遇到引號：根據開關狀態決定用什麼符號
            # 三元運算式：如果 opening 為 True 則用 ``，否則用 ''
            result += "``" if opening else "''"
            # 切換開關，為下一個引號做準備
            opening = not opening
        else:
            # 不是引號的字元直接累加（包括換行符、空格等）
            result += char

# 一次性輸出所有累積的結果
sys.stdout.write(result)
