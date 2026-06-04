"""gcd 實作：提供 sum_of_gcd(n)

功能：計算 1 <= i < j <= n 範圍內所有 gcd(i, j) 的總和。

註解以繁體中文撰寫，供教學與測試使用。
"""

from math import gcd


def sum_of_gcd(n: int) -> int:
    """返回 1 <= i < j <= n 的所有 gcd(i, j) 加總。

    算法：直接雙重迴圈計算，對於題目範圍（測試使用 n <= 100）效能足夠且實作簡潔。
    若需處理更大 n，可改用數論技巧（例如 Euler totient 相關的優化）。
    """
    if n < 2:
        return 0

    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += gcd(i, j)
    return total
