# UVA 11461（好記版）
# 核心口訣：
# [a,b] 的平方數個數 = floor(sqrt(b)) - floor(sqrt(a-1))

import math
import sys


def count_in_range(a, b):
    return math.isqrt(b) - math.isqrt(a - 1)


def solve(text):
    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        out.append(str(count_in_range(a, b)))
    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
