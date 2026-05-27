# UVA 11417（好記版）
# 核心口訣：
# 1) 兩層迴圈跑 i<j
# 2) 把 gcd(i, j) 全部加起來

import math
import sys


def calc(n):
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += math.gcd(i, j)
    return total


def solve(text):
    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break
        out.append(str(calc(n)))
    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
