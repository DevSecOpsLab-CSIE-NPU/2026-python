"""
UVA 11417 — 容易記憶版

使用 itertools.combinations 取代雙層迴圈，
程式碼更簡潔、語意更清楚，容易記憶。
"""

import math
import itertools


def gcd_sum(n):
    """
    計算所有 1 <= i < j <= n 的 gcd(i, j) 總和（簡潔版）

    combinations 直接產生所有 (i, j) 數對，
    語意上更接近數學定義的 sum_{i<j}
    """
    # combinations(range(1, n+1), 2) 自動產生所有 i<j 的數對
    return sum(math.gcd(i, j) for i, j in itertools.combinations(range(1, n + 1), 2))


def solve() -> None:
    """讀取標準輸入，每行一個 N，直到 N=0 結束"""
    while True:
        n = int(input().strip())
        if n == 0:
            break
        print(gcd_sum(n))


if __name__ == "__main__":
    solve()
