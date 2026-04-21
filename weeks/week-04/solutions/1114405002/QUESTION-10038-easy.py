"""UVA 10038 Jolly Jumpers - easy 版。

只要檢查相鄰差值是否剛好包含 1 到 n-1，且每個都只出現一次即可。
"""

import sys


def solve():
    ans = []
    for line in sys.stdin.buffer.read().splitlines():
        if not line.strip():
            continue

        nums = list(map(int, line.split()))
        n = nums[0]
        seq = nums[1:]
        seen = [False] * n

        ok = True
        for i in range(1, n):
            d = abs(seq[i] - seq[i - 1])
            if d < 1 or d >= n or seen[d]:
                ok = False
                break
            seen[d] = True

        ans.append("Jolly" if ok else "Not jolly")

    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    solve()