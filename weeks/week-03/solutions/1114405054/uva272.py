"""
UVA 272 - TeX Quotes (ZeroJudge c007)

解法：
  - 維護布林旗標 is_open（True = 下一個 " 換成開引號 ``）
  - 逐字元掃描，遇到 " 依旗標替換，並切換旗標
  - 其他字元原樣輸出
  - 旗標跨行持續（不每行重置），整份輸入統一計算
"""

import sys

is_open = True

for line in sys.stdin:
    result = []
    for char in line:
        if char == '"':
            if is_open:
                result.append('``')
            else:
                result.append("''")
            is_open = not is_open
        else:
            result.append(char)
    print(''.join(result), end='')