import math
import sys


def minimum_sum_bc(a):
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