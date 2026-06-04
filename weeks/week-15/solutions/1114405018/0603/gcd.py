"""Implementation for UVA 11417 — sum_of_gcd(n)."""

from math import gcd


def sum_of_gcd(n: int) -> int:
    """Return the sum of gcd(i, j) for 1 <= i < j <= n.

    Constraints: n up to ~500 in this exercise, so an O(n^2) approach is fine.
    """
    if n <= 1:
        return 0

    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += gcd(i, j)
    return total


__all__ = ["sum_of_gcd"]
