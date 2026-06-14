import math
def sum_of_gcd(n: int) -> int:
    g = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            g += math.gcd(i, j)
    return g
