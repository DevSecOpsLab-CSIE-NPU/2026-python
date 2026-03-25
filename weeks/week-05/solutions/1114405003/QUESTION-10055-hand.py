"""
UVA 10055（依題意）手打版
口訣：減函數記 1，區間奇偶決定答案
"""

from __future__ import annotations


class BIT:
    def __init__(self, n: int) -> None:
        self.n = n
        self.t = [0] * (n + 1)

    def add(self, i: int, v: int) -> None:
        while i <= self.n:
            self.t[i] += v
            i += i & -i

    def sum(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.t[i]
            i -= i & -i
        return s

    def query(self, l: int, r: int) -> int:
        return self.sum(r) - self.sum(l - 1)


def solve(data: str) -> str:
    a = list(map(int, data.split()))
    if not a:
        return ""

    p = 0
    n, q = a[p], a[p + 1]
    p += 2

    state = [0] * (n + 1)  # 0: 增, 1: 減
    bit = BIT(n)
    out = []

    for _ in range(q):
        op = a[p]
        p += 1

        if op == 1:
            i = a[p]
            p += 1
            if state[i] == 0:
                state[i] = 1
                bit.add(i, 1)
            else:
                state[i] = 0
                bit.add(i, -1)
        else:
            l, r = a[p], a[p + 1]
            p += 2
            out.append("1" if bit.query(l, r) % 2 else "0")

    return "\n".join(out)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()))
