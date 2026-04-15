"""
UVA 299 - Train Swapping（easy 版）

超好記口訣：
  「每一個逆序對，都要至少交換一次。」

所以答案就是：
  數出有幾對 (i, j) 滿足 i < j 且 a[i] > a[j]。

因為 L 很小（<= 50），直接雙迴圈最直觀。
"""

from __future__ import annotations

import sys


def cnt(arr: list[int]) -> int:
    """easy 版：計算反序數（也就是最少相鄰交換次數）。"""
    n = len(arr)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                ans += 1
    return ans


def out(swaps: int) -> str:
    """輸出格式字串。"""
    return f"Optimal train swapping takes {swaps} swaps."


def solve(arr: list[int]) -> str:
    """單筆測資求解。"""
    return out(cnt(arr))


def main() -> None:
    first = sys.stdin.readline().strip()
    if not first:
        return

    t = int(first)
    for _ in range(t):
        l_line = sys.stdin.readline().strip()
        while l_line == "":
            l_line = sys.stdin.readline().strip()
        _l = int(l_line)

        a_line = sys.stdin.readline().strip()
        while a_line == "":
            a_line = sys.stdin.readline().strip()
        arr = list(map(int, a_line.split()))

        print(solve(arr))


if __name__ == "__main__":
    main()
