"""UVA/ZeroJudge 10062 解答。

題意（依本課程題面）：
- 給定 N 與 N-1 個數值 a[2..N]。
- a[i] 表示在隊伍第 i 個位置之前，編號比該牛小的數量。
- 需要還原每個位置的牛編號。

做法：
- 由後往前還原。
- 維護目前可用的編號集合 {1..N}。
- 第 i 個位置要選「剩餘編號中的第 a[i] + 1 小」。
- 透過 Fenwick Tree 維護可用數量並做 k-th 查詢，時間 O(N log N)。
"""

from __future__ import annotations

import sys
from typing import List


class FenwickTree:
    """Fenwick Tree（Binary Indexed Tree），支援前綴和與第 k 小查詢。"""

    def __init__(self, size: int) -> None:
        self.n = size
        self.bit = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        while index <= self.n:
            self.bit[index] += delta
            index += index & -index

    def kth(self, k: int) -> int:
        """回傳最小的 idx，使得 prefix_sum(idx) >= k。"""
        idx = 0
        step = 1 << (self.n.bit_length() - 1)
        while step:
            nxt = idx + step
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                idx = nxt
            step >>= 1
        return idx + 1


def solve(input_data: str) -> str:
    nums = [int(x) for x in input_data.split()]
    if not nums:
        return ""

    n = nums[0]
    a = [0] * (n + 1)

    # 讀入 a[2..N]，第一個位置預設為 0（題目不提供）
    for i in range(2, n + 1):
        a[i] = nums[i - 1]

    fw = FenwickTree(n)
    for x in range(1, n + 1):
        fw.add(x, 1)  # 一開始每個編號都可用

    ans = [0] * (n + 1)

    # 由後往前決定每個位置的編號
    for i in range(n, 0, -1):
        k = a[i] + 1
        value = fw.kth(k)
        ans[i] = value
        fw.add(value, -1)  # 移除此編號

    return "\n".join(map(str, ans[1:]))


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        sys.stdout.write(out + "\n")


if __name__ == "__main__":
    main()
