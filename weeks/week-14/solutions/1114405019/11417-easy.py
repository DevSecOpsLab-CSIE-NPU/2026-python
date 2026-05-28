# UVA 11417 — GCD（AI 簡單版）
# 計算所有 1 ≤ i < j ≤ N 的 gcd(i, j) 總和
#
# 公式：G = Σ gcd(i, j)，其中 1 ≤ i < j ≤ N
# N ≤ 500，雙層迴圈 O(N² log N) 完全可接受

from math import gcd

while True:
    n = int(input())
    if n == 0:  # 輸入 0 代表結束
        break
    # sum() 搭配生成器，遍歷所有合法數對 (i, j)
    total = sum(gcd(i, j) for i in range(1, n) for j in range(i + 1, n + 1))
    print(total)
