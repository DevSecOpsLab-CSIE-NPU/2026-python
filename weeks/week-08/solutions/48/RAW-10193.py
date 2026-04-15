import math
import sys


def main():
    a = int(sys.stdin.readline())
    target = a * a + 1
    best = None

    for x in range(1, math.isqrt(target) + 1):
        if target % x != 0:
            continue

        y = target // x
        total = 2 * a + x + y
        if best is None or total < best:
            best = total

    print(best)


if __name__ == '__main__':
    main()
