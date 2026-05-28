import math
import sys


def solve(data: str) -> str:
    out = []
    for s in data.split():
        n = int(s)
        if n == 0:
            break
        ans = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                ans += math.gcd(i, j)
        out.append(str(ans))
    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
