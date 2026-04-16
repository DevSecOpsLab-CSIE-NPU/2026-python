"""
UVA/ZeroJudge 10062（依題目敘述版本）
根據每個位置前方「編號比自己小」的數量，重建原始排列。
"""

from __future__ import annotations

import sys


class FenwickTree:
    """Fenwick Tree (Binary Indexed Tree) 支援：
    1) 單點加值
    2) 前綴和查詢
    3) 查詢第 k 小（以計數陣列表示）
    """

    def __init__(self, n: int) -> None:
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx: int, delta: int) -> None:
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def kth(self, k: int) -> int:
        """回傳目前計數集合中的第 k 小值（k 從 1 開始）。"""
        idx = 0
        # 取得不小於 n 的最高 2 次方位元，做二進位跳躍
        bit_mask = 1
        while bit_mask < self.n:
            bit_mask <<= 1

        step = bit_mask
        while step > 0:
            nxt = idx + step
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                idx = nxt
            step >>= 1
        return idx + 1


def solve(data: list[int]) -> str:
    if not data:
        return ""

    n = data[0]
    smaller_before = [0] * (n + 1)  # 1-indexed，smaller_before[1] 固定為 0

    # 題目輸入給的是第 2 到第 n 個位置的數值
    for i in range(2, n + 1):
        smaller_before[i] = data[i - 1]

    # 可用編號集合一開始是 1..n，每個編號都先放 1（可用）
    ft = FenwickTree(n)
    for x in range(1, n + 1):
        ft.add(x, 1)

    ans = [0] * (n + 1)

    # 從後往前重建：
    # 第 i 個位置的值，在「目前剩下的 i 個數」中是第 smaller_before[i] + 1 小。
    for i in range(n, 0, -1):
        rank = smaller_before[i] + 1
        value = ft.kth(rank)
        ans[i] = value
        ft.add(value, -1)  # 取走此編號

    return "\n".join(map(str, ans[1:]))


def main() -> None:
    raw = sys.stdin.read().strip().split()
    data = list(map(int, raw)) if raw else []
    output = solve(data)
    if output:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
