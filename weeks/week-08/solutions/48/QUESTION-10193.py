import math
import sys


def main():
    # 題目只給一個 a
    a = int(sys.stdin.readline())
    # 由推導可知要找的是 a^2 + 1 的因數配對
    target = a * a + 1
    best = None

    # 枚舉因數對，找 b + c 最小的組合
    for x in range(1, math.isqrt(target) + 1):
        if target % x != 0:
            continue

        y = target // x

        # 由 (b-a)(c-a)=a^2+1 可得 b=a+x、c=a+y
        total = 2 * a + x + y
        if best is None or total < best:
            best = total

    print(best)


if __name__ == '__main__':
    main()
