"""UVA 10038 Jolly Jumpers 標準版。"""

import sys


def solve():
    out = []
    for line in sys.stdin.buffer.read().splitlines():
        if not line.strip():
            continue

        nums = list(map(int, line.split()))
        n = nums[0]
        seq = nums[1:]

        diff_set = set()
        for i in range(1, n):
            diff_set.add(abs(seq[i] - seq[i - 1]))

        if len(diff_set) == n - 1 and all(1 <= d <= n - 1 for d in diff_set):
            out.append("Jolly")
        else:
            out.append("Not jolly")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()