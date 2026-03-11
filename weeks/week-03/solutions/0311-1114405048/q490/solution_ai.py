"""
UVA 490 — 旋轉句子（Rotating Sentences）
AI 教學版本：附繁體中文註解
"""
import sys

# 讀取所有輸入行，去掉行尾換行符
lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

if lines:
    # 找出最長行的長度
    max_len = max(len(line) for line in lines)

    # 將每行補齊到相同長度（用空格填充）
    padded = [line.ljust(max_len) for line in lines]
    n = len(padded)

    # 順時針旋轉 90 度：
    # 原本第 col 欄的字元，從最後一行到第一行排列，形成新的一行
    for col in range(max_len):
        row = []
        for r in range(n - 1, -1, -1):
            row.append(padded[r][col])
        print(''.join(row))
