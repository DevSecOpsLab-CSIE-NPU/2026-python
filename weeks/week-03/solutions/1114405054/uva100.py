"""
UVA 100 - The 3n+1 Problem (ZeroJudge c039)

解法：
  - 使用記憶化字典 memo 存已算過的 cycle-length，避免重複計算
  - 對每筆輸入 (i, j)，取 [min(i,j), max(i,j)] 區間的最大 cycle-length
  - 輸出時保持原始 i, j 順序（不按大小排序）
"""

import sys

memo = {1: 1}


def cycle_length(n):
    """計算 n 的 Collatz 數列長度（含起點 n 與終點 1）"""
    path = []
    current = n

    while current not in memo:
        path.append(current)
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1

    base = memo[current]
    for i, val in enumerate(reversed(path)):
        memo[val] = base + i + 1

    return memo[n]


for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    i, j = map(int, line.split())
    lo, hi = min(i, j), max(i, j)
    max_len = max(cycle_length(n) for n in range(lo, hi + 1))
    print(i, j, max_len)