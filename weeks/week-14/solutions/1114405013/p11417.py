"""
UVA 11417 — GCD（最大公因數總和）
ZeroJudge b410

功能：計算 sum_{i=1}^{N-1} sum_{j=i+1}^{N} gcd(i, j)
"""

import math


def gcd_sum(n):
    """
    計算所有 1 <= i < j <= n 的 gcd(i, j) 總和

    參數：
        n: int — 正整數（2 <= n <= 500）

    回傳值：
        int — GCD 總和
    """
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += math.gcd(i, j)
    return total


def solve() -> None:
    """讀取標準輸入，每行一個 N，直到 N=0 結束"""
    while True:
        n = int(input().strip())
        if n == 0:
            break
        print(gcd_sum(n))


if __name__ == "__main__":
    solve()
