"""UVA 10062 題意版本的解法。

輸入給的是每個位置前面有多少個較小編號的牛，
我們可以反過來從右往左決定每個位置要放哪個編號。
"""

from __future__ import annotations

import sys


class FenwickTree:
    """樹狀陣列：用來快速找出第 k 個還沒被拿走的位置。"""

    def __init__(self, size: int) -> None:
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def kth(self, k: int) -> int:
        """回傳目前第 k 個 1 的位置，k 從 1 開始。"""

        index = 0
        bit_mask = 1 << (self.size.bit_length() - 1)
        while bit_mask:
            next_index = index + bit_mask
            if next_index <= self.size and self.tree[next_index] < k:
                k -= self.tree[next_index]
                index = next_index
            bit_mask >>= 1
        return index + 1


def solve(data: str) -> str:
    numbers = list(map(int, data.split()))
    if not numbers:
        return ""

    n = numbers[0]
    counts = [0] + numbers[1:]

    # 一開始 1..N 都還沒被使用，所以每個位置都是可選的。
    tree = FenwickTree(n)
    for position in range(1, n + 1):
        tree.add(position, 1)

    answer = [0] * (n + 1)

    # 由右往左填位置：
    # 第 i 個位置要有 counts[i] 個較小數字在前面，
    # 等價於從「還可用的數字」中選第 counts[i] + 1 小的數字。
    for position in range(n, 0, -1):
        target_rank = counts[position - 1] + 1
        value = tree.kth(target_rank)
        answer[position] = value
        tree.add(value, -1)

    return "\n".join(map(str, answer[1:]))


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()