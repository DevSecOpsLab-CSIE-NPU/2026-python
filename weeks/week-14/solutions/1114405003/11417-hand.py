import math
import sys


def solve(data):
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    mx = max((n for n in nums if n != 0), default=0)
    ans = [0] * (mx + 1)
    s = 0

    for n in range(1, mx + 1):
        for i in range(1, n):
            s += math.gcd(i, n)
        ans[n] = s

    out = []
    for n in nums:
        if n == 0:
            break
        out.append(str(ans[n]))
    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))