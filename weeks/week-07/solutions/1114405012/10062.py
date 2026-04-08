"""UVA 10062 解題程式（正式版，O(N log N)）。

題意給的是：
- 第 pos 個位置前面，有 a[pos] 頭編號比自己小的牛（pos 從 1 開始）

把答案從右往左填時：
- 右側位置先決定，不會影響左側仍待決定的位置
- 在「尚未使用的編號集合」中，第 pos 個位置要拿第 a[pos] + 1 小的編號

因此可用 Fenwick Tree 維護「哪些編號還可用」：
- 初始 1..N 都可用（值為 1）
- 每次用 find_kth(k) 找第 k 小可用編號
- 取出後把該編號標記為不可用（-1）
"""

from __future__ import annotations

import sys


class FenwickTree:
    """Fenwick Tree（Binary Indexed Tree）。

    用途：
    - 維護一個 1-based 陣列的前綴和
    - 支援點更新 add(idx, delta)
    - 支援查詢第 k 小位置（搭配「可用編號標記陣列」）
    """

    def __init__(self, n: int) -> None:
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx: int, delta: int) -> None:
        # 往上跳到所有會覆蓋 idx 的節點。
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def prefix_sum(self, idx: int) -> int:
        # 往父節點回溯，累加到 1..idx。
        total = 0
        while idx > 0:
            total += self.bit[idx]
            idx -= idx & -idx
        return total

    def find_kth(self, k: int) -> int:
        """找目前可用編號中的第 k 小（k 從 1 開始）。"""
        idx = 0
        bit_mask = 1 << (self.n.bit_length() - 1)

        # 二進位跳躍：逐步決定答案索引。
        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                idx = nxt
            bit_mask >>= 1
        return idx + 1


def reconstruct_order(counts: list[int]) -> list[int]:
    """根據每個位置前面較小牛的數量，還原原始排列。

    核心步驟：
    1. 把輸入轉成 1-based 的 a[pos] 形式。
    2. 初始把 1..N 都標記為可用（Fenwick 內值為 1）。
    3. 從右到左決定答案：第 pos 格拿第 a[pos]+1 小的可用編號。
    4. 取走後把該編號的可用值改成 0（add(value, -1)）。
    """
    n = len(counts) + 1

    # a[pos] 與題意一致（pos 從 1 到 N）。
    a = [0] * (n + 1)
    for pos in range(2, n + 1):
        a[pos] = counts[pos - 2]

    # Fenwick 內存的是「這個編號是否仍可用」：可用=1，不可用=0。
    fw = FenwickTree(n)
    for value in range(1, n + 1):
        fw.add(value, 1)

    ans = [0] * (n + 1)

    # 從右往左放：第 pos 個位置拿第 a[pos]+1 小可用編號。
    for pos in range(n, 0, -1):
        k = a[pos] + 1
        value = fw.find_kth(k)
        ans[pos] = value
        fw.add(value, -1)

    return ans[1:]


def main() -> None:
    # 一次讀完整個 stdin，對線上評測與本地測試都方便。
    # 輸入格式：N 後面接 N-1 個整數。
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    counts = data[1:]

    # 題目只需要前 N-1 個 counts；多餘資料（若有）忽略。
    answer = reconstruct_order(counts[: n - 1])

    # 依題意每行輸出一個位置的牛編號。
    sys.stdout.write("\n".join(map(str, answer)))


if __name__ == "__main__":
    main()
