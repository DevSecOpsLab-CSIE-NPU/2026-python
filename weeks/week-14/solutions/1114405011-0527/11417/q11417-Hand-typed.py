import math
import sys


def solve(data):
    nums = [int(x) for x in data.strip().split() if x.strip()]
    if not nums:
        return ""
    limit = 500
    pair_sum = [0] * (limit + 1)
    for i in range(1, limit + 1):
        for j in range(i + 1, limit + 1):
            pair_sum[j] += math.gcd(i, j)
    ans = [0] * (limit + 1)
    for n in range(2, limit + 1):
        ans[n] = ans[n - 1] + pair_sum[n]
    out = []
    for n in nums:
        if n == 0:
            break
        out.append(str(ans[n]))
    return "\n".join(out)


def main():
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
