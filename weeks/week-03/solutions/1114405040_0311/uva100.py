"""
UVA 100 - The 3n+1 Problem (ZeroJudge c039)

解法：
  - 使用記憶化字典 memo 存已算過的 cycle-length，避免重複計算
  - 對每筆輸入 (i, j)，取 [min(i,j), max(i,j)] 區間的最大 cycle-length
  - 輸出時保持原始 i, j 順序（不按大小排序）
"""

import sys

# 記憶化字典：key = 數字 n，value = n 的 cycle-length
memo = {1: 1}


def cycle_length(n):
    """計算 n 的 Collatz 數列長度（含起點 n 與終點 1）"""
    path = []
    current = n

    # 往前走直到遇到已知結果，沿途記錄未知節點
    while current not in memo:
        path.append(current)
        if current % 2 == 0:
            current = current // 2      # 偶數：除以 2
        else:
            current = 3 * current + 1   # 奇數：3n+1

    # 從已知結果往回填入路徑上每個節點的 cycle-length
    base = memo[current]
    for i, val in enumerate(reversed(path)):
        memo[val] = base + i + 1

    return memo[n]


# 讀取輸入，每行一對 (i, j)
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    i, j = map(int, line.split())

    # 取區間範圍
    lo, hi = min(i, j), max(i, j)

    # 區間內所有數的最大 cycle-length
    max_len = max(cycle_length(n) for n in range(lo, hi + 1))

    # 輸出保持原始 i, j 順序
    print(i, j, max_len)
