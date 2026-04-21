"""UVA 10038 手打版。"""

import sys


def solve():
    data = sys.stdin.buffer.read().splitlines()
    out = []

    for line in data:
        if not line.strip():
            continue

        arr = list(map(int, line.split()))
        n = arr[0]
        nums = arr[1:]

        used = [False] * n
        good = True

        for i in range(1, n):
            d = abs(nums[i] - nums[i - 1])
            if d < 1 or d >= n:
                good = False
                break
            if used[d]:
                good = False
                break
            used[d] = True

        if good:
            out.append("Jolly")
        else:
            out.append("Not jolly")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()