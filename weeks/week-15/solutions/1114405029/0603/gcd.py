"""
UVA 11417 - GCD

計算：

G = Σ Σ gcd(i, j)
    1 ≤ i < j ≤ n
"""

import math


def sum_of_gcd(n: int) -> int:
    """
    計算所有 1 <= i < j <= n 的 gcd(i,j) 總和

    參數:
        n (int)

    回傳:
        int
    """

    total = 0

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += math.gcd(i, j)

    return total