"""10062 的好記憶版本。

核心想法只有一句：
從右往左填位置，每次都從剩下的數字裡挑第 k 小。
"""

from __future__ import annotations

import sys


class FenwickTree:
    """樹狀陣列，負責：
    1. 標記某個數字還在不在
    2. 快速找到第 k 個還存在的數字
    """

    def __init__(self, size: int) -> None:
        self.size = size
        self.data = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        # 把某個位置加上 delta，往上更新所有相關節點。
        while index <= self.size:
            self.data[index] += delta
            index += index & -index

    def kth(self, k: int) -> int:
        # 找目前第 k 個 1 的位置，k 是從 1 開始算。
        pos = 0
        step = 1 << (self.size.bit_length() - 1)
        while step:
            nxt = pos + step
            if nxt <= self.size and self.data[nxt] < k:
                k -= self.data[nxt]
                pos = nxt
            step >>= 1
        return pos + 1


def solve(text: str) -> str:
    values = list(map(int, text.split()))
    if not values:
        return ""

    n = values[0]
    # counts[1] 對應第 1 個位置，固定是 0；
    # counts[i] 代表第 i 個位置前面有幾個較小的數字。
    counts = [0] + values[1:]

    tree = FenwickTree(n)
    for number in range(1, n + 1):
        tree.add(number, 1)

    result = [0] * (n + 1)

    # 由右往左決定答案：
    # 右邊的位置先確定後，左邊只要挑「剩下數字中第 k 小」就可以。
    for position in range(n, 0, -1):
        need = counts[position - 1] + 1
        chosen = tree.kth(need)
        result[position] = chosen
        tree.add(chosen, -1)

    return "\n".join(str(result[i]) for i in range(1, n + 1))


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()