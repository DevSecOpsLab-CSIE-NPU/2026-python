"""
UVA 272 - TeX Quotes (ZeroJudge c007)

解法：
  - 維護布林旗標 is_open（True = 下一個 " 換成開引號 ``）
  - 逐字元掃描，遇到 " 依旗標替換，並切換旗標
  - 其他字元原樣輸出
  - 旗標跨行持續（不每行重置），整份輸入統一計算
"""

import sys

is_open = True  # True = 下一個 " 替換為開引號 ``

for line in sys.stdin:
    result = []
    for char in line:
        if char == '"':
            if is_open:
                result.append('``')   # 開引號：兩個 backtick
            else:
                result.append("''")   # 閉引號：兩個 apostrophe
            is_open = not is_open     # 切換開/閉狀態
        else:
            result.append(char)       # 其他字元直接保留

    # end='' 避免多餘換行（line 本身已含 '\n'）
    print(''.join(result), end='')
