"""10170 easy-hand：手打版。"""

import math
import sys


def solve_one(s, d):
    # 找最小 n，使 S+...+n >= d
    # 即 T(n) - T(s-1) >= d
    target = d + (s - 1) * s // 2

    n = (math.isqrt(1 + 8 * target) - 1) // 2
    if n < s:
        n = s

    while n * (n + 1) // 2 < target:
        n += 1

    return n


def main():
    out = []
    for line in sys.stdin.buffer.read().splitlines():
        if not line.strip():
            continue
        s, d = map(int, line.split())
        out.append(str(solve_one(s, d)))
    sys.stdout.write('\n'.join(out))


if __name__ == '__main__':
    main()
