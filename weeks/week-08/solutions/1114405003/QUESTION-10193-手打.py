import math
import sys


def min_b_plus_c(a):
    """
    由
      arctan(1/a) = arctan(1/b) + arctan(1/c)
    可推出
      (b-a)(c-a) = a^2 + 1
    設 d=b-a, e=c-a，則 d*e=a^2+1
    所以 b+c = 2a + d + e，找最小即可。
    """
    n = a * a + 1
    best = None

    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0:
            e = n // d
            candidate = 2 * a + d + e
            if best is None or candidate < best:
                best = candidate

    return best


def main():
    text = sys.stdin.read().strip()
    if not text:
        return

    a = int(text)
    print(min_b_plus_c(a))


if __name__ == "__main__":
    main()
