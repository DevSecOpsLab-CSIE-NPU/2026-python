"""Solution: sum_of_gcd for UVA 11417

Implementation using Euler's totient function sieve and prefix sums.
"""
from typing import List


def _compute_phi(n: int) -> List[int]:
    phi = list(range(n + 1))
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return phi


def sum_of_gcd(n: int) -> int:
    if n < 2:
        return 0
    phi = _compute_phi(n)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + phi[i]

    total = 0
    for k in range(1, n + 1):
        m = n // k
        if m >= 2:
            total += k * (prefix[m] - 1)
    return total


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        print(sum_of_gcd(n))
    else:
        print("Usage: python gcd.py <n>")
