"""
QUESTION-10062-easy
教學版：邏輯更直觀、註解更詳細，仍保留 O(n log n) 效能。
"""

from __future__ import annotations

import sys


class Fenwick:
    """Fenwick Tree（樹狀陣列）

    我們把「某個編號還能不能用」當成 0/1：
    - 1 代表還沒被選走
    - 0 代表已被選走

    這樣前綴和就代表「<= 某個編號」目前還有幾個可用。
    """

    def __init__(self, n: int) -> None:
        self.n = n
        self.t = [0] * (n + 1)

    def add(self, i: int, v: int) -> None:
        while i <= self.n:
            self.t[i] += v
            i += i & -i

    def kth(self, k: int) -> int:
        """找出目前第 k 小的可用編號（k 從 1 開始）。"""
        i = 0

        # 先找一個足夠大的 2 次方步長，後面逐步縮小
        step = 1
        while step < self.n:
            step <<= 1

        # 二進位跳躍：若往右跳後，前綴和仍 < k，表示答案還在更右邊
        while step:
            ni = i + step
            if ni <= self.n and self.t[ni] < k:
                k -= self.t[ni]
                i = ni
            step >>= 1

        return i + 1


def solve(tokens: list[int]) -> str:
    if not tokens:
        return ""

    n = tokens[0]

    # less[i] = 第 i 個位置前面，比自己小的牛有幾頭
    # 題目只提供 i=2..n，i=1 固定是 0
    less = [0] * (n + 1)
    for i in range(2, n + 1):
        less[i] = tokens[i - 1]

    fw = Fenwick(n)

    # 一開始所有編號 1..n 都可用
    for x in range(1, n + 1):
        fw.add(x, 1)

    ans = [0] * (n + 1)

    # 關鍵想法（最容易記）：
    # 從後往前填第 i 個位置。
    # 此時「還沒被用掉」的編號剛好有 i 個，
    # 而第 i 個位置需要前面有 less[i] 個更小值，
    # 所以它就是剩餘編號中的第 less[i] + 1 小。
    for i in range(n, 0, -1):
        pick_rank = less[i] + 1
        ans[i] = fw.kth(pick_rank)
        fw.add(ans[i], -1)

    return "\n".join(str(v) for v in ans[1:])


def main() -> None:
    text = sys.stdin.read().strip().split()
    nums = list(map(int, text)) if text else []
    out = solve(nums)
    if out:
        print(out)


if __name__ == "__main__":
    main()
