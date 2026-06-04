"""UVA 11417 GCD — 實作檔

計算：G = Σ Σ gcd(i, j) for 1 ≤ i < j ≤ n
"""

from math import gcd


def sum_of_gcd(n: int) -> int:
    """計算所有 gcd(i, j) 的總和，其中 1 <= i < j <= n"""
    total = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            total += gcd(i, j)
    return total
