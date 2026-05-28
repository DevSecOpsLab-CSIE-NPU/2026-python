# UVA 11417 — GCD（手打版）
# 計算所有 1 ≤ i < j ≤ N 的 gcd(i, j) 總和
# N ≤ 500，雙層迴圈 O(N² log N) 可接受

from math import gcd

while True:
    n = int(input())  # 讀取 N
    if n == 0:        # 0 代表結束，不處理
        break
    total = 0
    # 枚舉所有合法數對 (i, j)，i < j
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += gcd(i, j)
    print(total)
