import math
import sys


def solve(data):
    out = []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        out.append(str(math.isqrt(b) - math.isqrt(a - 1)))
    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))