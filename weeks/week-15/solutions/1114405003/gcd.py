import math

from math import gcd


def sum_of_gcd(n: int) -> int:
    """Return sum of gcd(i, j) for all 1 <= i < j <= n."""
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += gcd(i, j)
    return total
