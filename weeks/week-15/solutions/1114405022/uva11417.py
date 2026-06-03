from math import gcd

def sum_gcd_pairs(n: int) -> int:
    """Return sum of gcd(i, j) for all 1 <= i < j <= n.

    Naive O(n^2) implementation using math.gcd. Suitable for typical classroom
    input sizes used in exercises and tests.
    """
    if n < 2:
        return 0
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += gcd(i, j)
    return total

if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        print(sum_gcd_pairs(n))
