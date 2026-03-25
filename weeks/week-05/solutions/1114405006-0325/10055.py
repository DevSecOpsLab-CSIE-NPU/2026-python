"""
UVA 10055

作法：
- 用 Fenwick Tree（BIT）維護每個位置是否為減函數（0/1）。
- 反轉操作：該點從 0<->1，對 BIT 做 +1 或 -1。
- 區間查詢：計算 [L, R] 內 1 的數量奇偶，奇數輸出 1，偶數輸出 0。

觀念：
- 複合函數的單調性只跟「減函數個數的奇偶」有關。
- 區間內減函數數量是偶數，複合後為增函數（輸出 0）。
- 區間內減函數數量是奇數，複合後為減函數（輸出 1）。
"""

from __future__ import annotations

import sys


class FenwickTree:
    """Fenwick Tree（Binary Indexed Tree）支援單點更新、前綴和查詢。"""

    def __init__(self, n: int) -> None:
        self.n = n
        # bit[0] 不使用，節省索引轉換成本。
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        # 將索引 i 的值增加 delta，並更新所有受影響的樹節點。
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def prefix_sum(self, i: int) -> int:
        # 回傳區間 [1, i] 的總和。
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, left: int, right: int) -> int:
        # 區間和 = 前綴和(right) - 前綴和(left-1)
        return self.prefix_sum(right) - self.prefix_sum(left - 1)


def solve(data: str) -> str:
    # 將輸入全部拆成整數，方便用索引依序讀取。
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    idx = 0
    n = nums[idx]
    idx += 1
    q = nums[idx]
    idx += 1

    bit = FenwickTree(n)
    # state[i]：第 i 個函數目前狀態，0 代表增、1 代表減。
    state = [0] * (n + 1)
    out: list[str] = []

    for _ in range(q):
        op = nums[idx]
        idx += 1

        if op == 1:
            # 操作 1：反轉單一函數的增減性。
            i = nums[idx]
            idx += 1

            if state[i] == 0:
                state[i] = 1
                # 由增變減：減函數數量 +1
                bit.add(i, 1)
            else:
                state[i] = 0
                # 由減變增：減函數數量 -1
                bit.add(i, -1)
        else:
            # 操作 2：查詢區間 [left, right] 的複合函數單調性。
            left = nums[idx]
            right = nums[idx + 1]
            idx += 2

            dec_count = bit.range_sum(left, right)
            # 奇數個減函數 => 減（1），偶數個 => 增（0）。
            out.append(str(dec_count % 2))

    return "\n".join(out)


def main() -> None:
    result = solve(sys.stdin.read())
    if result:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()
