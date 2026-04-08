from __future__ import annotations

import sys


class FenwickTree:
    """Fenwick Tree（又稱 BIT）：支援前綴和與第 k 小查詢。"""

    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, index: int, delta: int) -> None:
        # 把某個位置的值加上 delta，並更新所有受影響的父節點。
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index

    def kth(self, k: int) -> int:
        """找目前集合中第 k 小的編號（1-based）。"""
        idx = 0
        jump = 1 << (self.n.bit_length() - 1)
        while jump > 0:
            nxt = idx + jump
            if nxt <= self.n and self.tree[nxt] < k:
                k -= self.tree[nxt]
                idx = nxt
            jump >>= 1
        return idx + 1


def solve(data: str) -> str:
    values = [int(x) for x in data.split()]
    if not values:
        return ""

    n = values[0]

    # input 只給第 2..N 個位置，因此第 1 個位置補 0。
    count_smaller_before = [0] * (n + 1)
    for pos in range(2, n + 1):
        count_smaller_before[pos] = values[pos - 1]

    # 一開始可用的編號是 1..N，每個都先放進 BIT。
    bit = FenwickTree(n)
    for cow_id in range(1, n + 1):
        bit.add(cow_id, 1)

    result = [0] * (n + 1)

    # 從後往前填：第 pos 個位置要取「剩下編號中的第 (a[pos]+1) 小」。
    for pos in range(n, 0, -1):
        rank = count_smaller_before[pos] + 1
        chosen_id = bit.kth(rank)
        result[pos] = chosen_id
        bit.add(chosen_id, -1)  # 用掉就移除

    return "\n".join(str(result[i]) for i in range(1, n + 1))


def main() -> None:
    data = sys.stdin.read()
    output = solve(data)
    if output:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
