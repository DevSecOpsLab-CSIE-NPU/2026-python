from __future__ import annotations

import sys


class FenwickTree:
    # 手打版：用 BIT 快速找第 k 小未使用編號。
    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i: int, v: int) -> None:
        while i <= self.n:
            self.tree[i] += v
            i += i & -i

    def kth(self, k: int) -> int:
        idx = 0
        jump = 1 << (self.n.bit_length() - 1)
        while jump:
            nxt = idx + jump
            if nxt <= self.n and self.tree[nxt] < k:
                k -= self.tree[nxt]
                idx = nxt
            jump >>= 1
        return idx + 1


def solve(data: str) -> str:
    nums = [int(x) for x in data.split()]
    if not nums:
        return ""

    n = nums[0]
    a = [0] * (n + 1)
    for pos in range(2, n + 1):
        a[pos] = nums[pos - 1]

    bit = FenwickTree(n)
    for i in range(1, n + 1):
        bit.add(i, 1)

    ans = [0] * (n + 1)
    for pos in range(n, 0, -1):
        ans[pos] = bit.kth(a[pos] + 1)
        bit.add(ans[pos], -1)

    return "\n".join(str(ans[i]) for i in range(1, n + 1))


if __name__ == "__main__":
    out = solve(sys.stdin.read())
    if out:
        sys.stdout.write(out)
