"""UVA 11417 GCD

題目：計算 1 <= i < j <= n 範圍內所有 gcd(i, j) 的總和。
"""

from math import gcd


def sum_of_gcd(n: int) -> int:
    """
    計算 1 <= i < j <= n 範圍內所有 gcd(i, j) 的總和。
    
    Args:
        n: 正整數上限
    
    Returns:
        所有 gcd(i, j) 的總和
    """
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += gcd(i, j)
    return total
