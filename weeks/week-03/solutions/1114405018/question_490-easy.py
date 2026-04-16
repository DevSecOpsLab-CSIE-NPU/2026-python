"""UVA 490 - Rotating Sentences（easy 版）

題目要求：
1. 讀入多行文字（直到 EOF）。
2. 將整體文字矩陣順時針旋轉 90 度。
3. 長度不足的位置視為空白補齊。
4. 輸出每行尾端多餘空白要移除。

這份 easy 版重點：
- 直接用兩層迴圈做「逐欄輸出」。
- 外層跑欄位，內層由下往上取字元。
"""

import sys

# 讀取所有輸入行（保留空行，不含行尾換行符）
lines = sys.stdin.read().splitlines()

# 沒有任何輸入就直接結束
if not lines:
    raise SystemExit

# 原始矩陣寬度 = 最長那一行的長度
w = max(len(s) for s in lines)

# 儲存旋轉後的每一行
ans = []

# 逐欄處理：旋轉後的「每一行」其實對應原本的某一欄
for c in range(w):
    row = ""

    # 由下往上取字元，達成順時針旋轉 90 度
    for r in range(len(lines) - 1, -1, -1):
        # 若該行有第 c 欄字元就取出；否則補空白
        row += lines[r][c] if c < len(lines[r]) else " "

    # 移除輸出行尾端多餘空白，符合題目輸出需求
    ans.append(row.rstrip())

# 將結果逐行輸出
sys.stdout.write("\n".join(ans))
