import math
import sys


def solve(text):
    """把題目輸入轉成答案字串。"""

    a = int(text.strip())

    # 由反正切加法公式可得：
    #   (b - a) * (c - a) = a^2 + 1
    # 所以只要找 a^2 + 1 的因數對，就能得到 b、c。
    target = a * a + 1
    best = 10**18

    # 只要掃到平方根即可，因為因數會成對出現
    for d in range(1, math.isqrt(target) + 1):
        if target % d == 0:
            e = target // d
            b = a + d
            c = a + e
            best = min(best, b + c)

    return str(best)


def main():
    """競賽模式入口：讀標準輸入，印出答案。"""

    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()