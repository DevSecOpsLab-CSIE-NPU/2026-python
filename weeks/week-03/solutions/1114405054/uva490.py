"""
UVA 490 - Rotating Sentences (ZeroJudge c045)

解法：
  - 讀取所有行（去掉行末換行符）
  - 找最大寬度，補空白讓所有行等長，形成矩形
  - 90° 順時針旋轉：
      新的第 j 行 = 原矩陣第 j 欄，由最後一行往第一行讀（由下往上）
  - 旋轉後共輸出 max_width 行
"""

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

if lines:
    max_width = max(len(line) for line in lines)
    padded = [line.ljust(max_width) for line in lines]
    nrows = len(padded)

    for j in range(max_width):
        new_row = ''.join(padded[nrows - 1 - i][j] for i in range(nrows))
        print(new_row)