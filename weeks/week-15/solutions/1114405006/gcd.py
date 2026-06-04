"""Solution implementation for UVA 11417 GCD: sum_of_gcd(n)

This file provides a straightforward, correct implementation using
math.gcd. It's O(n^2) and intended for the small test inputs in the
exercise (n up to 10 in tests). For large n an optimized algorithm
would be needed.
"""
from math import gcd


def sum_of_gcd(n: int) -> int:
    """Return sum of gcd(i, j) for 1 <= i < j <= n.

    Examples:
    - sum_of_gcd(1) == 0
    - sum_of_gcd(2) == 1
    - sum_of_gcd(10) == 67
    """
    if n < 2:
        return 0
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += gcd(i, j)
    return total
