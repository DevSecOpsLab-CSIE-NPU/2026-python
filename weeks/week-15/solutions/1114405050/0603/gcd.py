import math

def sum_of_gcd(n: int) -> int:
    """
    計算 1 <= i < j <= n 範圍內所有 gcd(i, j) 的總和。
    """
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += math.gcd(i, j)
    return total