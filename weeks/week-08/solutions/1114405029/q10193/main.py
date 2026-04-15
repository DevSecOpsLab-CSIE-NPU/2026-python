import math
import sys


def minimum_sum_bc(a):
    # 由公式推導可得：
    # (b - a)(c - a) = a^2 + 1
    # 設 n = a^2 + 1
    # 若 d * e = n，則 b + c = 2a + d + e
    # 所以只要找最接近 sqrt(n) 的因數對即可讓 d + e 最小
    n = a * a + 1

    root = int(math.isqrt(n))

    for d in range(root, 0, -1):
        if n % d == 0:
            e = n // d
            return 2 * a + d + e

    return -1


def main():
    data = sys.stdin.read().strip()
    if not data:
        return

    a = int(data)
    print(minimum_sum_bc(a))


if __name__ == "__main__":
    main()