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

# 讀取所有行，去掉行末換行符（保留行內空白）
lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

if lines:
    # 找最大行寬
    max_width = max(len(line) for line in lines)

    # 每行補空白至相同長度，形成完整矩形
    padded = [line.ljust(max_width) for line in lines]

    nrows = len(padded)   # 原始行數

    # 旋轉後輸出 max_width 行
    for j in range(max_width):
        # 第 j 欄：從最後一行掃到第一行（由下往上），形成旋轉後的一行
        new_row = ''.join(padded[nrows - 1 - i][j] for i in range(nrows))
        print(new_row)
