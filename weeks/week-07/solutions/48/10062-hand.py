"""10062 手打版。

這版寫法偏直覺：
先把所有編號都放進樹狀陣列，
再從右往左一個一個挑出目前第 k 小的可用數字。
"""

from __future__ import annotations

import sys


class FenwickTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def kth(self, k: int) -> int:
        # 找出目前第 k 個還存在的位置。
        pos = 0
        step = 1 << (self.n.bit_length() - 1)
        while step > 0:
            nxt = pos + step
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                pos = nxt
            step >>= 1
        return pos + 1


def solve(text: str) -> str:
    data = list(map(int, text.split()))
    if not data:
        return ""

    n = data[0]
    cnt = [0] + data[1:]

    tree = FenwickTree(n)
    for value in range(1, n + 1):
        tree.add(value, 1)

    ans = [0] * (n + 1)
    for pos in range(n, 0, -1):
        pick = tree.kth(cnt[pos - 1] + 1)
        ans[pos] = pick
        tree.add(pick, -1)

    return "\n".join(str(ans[i]) for i in range(1, n + 1))


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()