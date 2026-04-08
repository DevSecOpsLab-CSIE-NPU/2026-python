from __future__ import annotations
import sys

class Fenwick:
    def __init__(self, n: int) -> None:
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, v: int) -> None:
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def kth(self, k: int) -> int:
        i = 0
        b = 1 << self.n.bit_length()
        while b:
            ni = i + b
            if ni <= self.n and self.bit[ni] < k:
                k -= self.bit[ni]
                i = ni
            b >>= 1
        return i + 1

def solve(data: str) -> str:
    t = data.strip().split()
    if not t:
        return ""
    n = int(t[0])
    a = [0] * (n + 1)
    for i in range(2, n + 1):
        a[i] = int(t[i - 1])
    fw = Fenwick(n)
    for i in range(1, n + 1):
        fw.add(i, 1)
    ans = [0] * (n + 1)
    for i in range(n, 0, -1):
        p = fw.kth(a[i] + 1)
        ans[i] = p
        fw.add(p, -1)
    return "\n".join(map(str, ans[1:]))

if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))
