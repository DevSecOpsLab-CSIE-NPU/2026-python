import math
import itertools


def gcd_sum(n):
    return sum(math.gcd(i, j) for i, j in itertools.combinations(range(1, n + 1), 2))


def solve() -> None:
    while True:
        n = int(input().strip())
        if n == 0:
            break
        print(gcd_sum(n))


if __name__ == "__main__":
    solve()
