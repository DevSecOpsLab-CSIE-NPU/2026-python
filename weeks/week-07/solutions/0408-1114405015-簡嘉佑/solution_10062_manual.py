"""
UVA 10062 manual solution.

Given n and an array counts of length n-1 where counts[i-1] means:
for position i (1-based, i >= 2), how many previous cows have smaller id.

This implementation rebuilds the permutation using a Fenwick Tree in O(n log n).
"""

from __future__ import annotations

from typing import List


class FenwickTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx: int, delta: int) -> None:
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def prefix_sum(self, idx: int) -> int:
        total = 0
        while idx > 0:
            total += self.bit[idx]
            idx -= idx & -idx
        return total

    def find_kth(self, k: int) -> int:
        if k <= 0 or k > self.prefix_sum(self.n):
            raise ValueError("k out of range")

        idx = 0
        bit_mask = 1 << (self.n.bit_length() - 1)

        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                idx = nxt
            bit_mask >>= 1

        return idx + 1


def solve_cow_order(n: int, counts: List[int]) -> List[int]:
    if n < 2:
        raise ValueError("n must be >= 2")
    if len(counts) != n - 1:
        raise ValueError("counts length must be n-1")

    ft = FenwickTree(n)
    for x in range(1, n + 1):
        ft.add(x, 1)

    ans = [0] * n

    # Fill from right to left.
    for i in range(n, 1, -1):
        c = counts[i - 2]
        if c < 0 or c >= i:
            raise ValueError(f"invalid count at position {i-1}: {c}")
        ans[i - 1] = ft.find_kth(c + 1)
        ft.add(ans[i - 1], -1)

    ans[0] = ft.find_kth(1)
    return ans


def main() -> None:
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    counts = [int(x) for x in data[1:]]
    order = solve_cow_order(n, counts)
    sys.stdout.write("\n".join(map(str, order)))


if __name__ == "__main__":
    main()
