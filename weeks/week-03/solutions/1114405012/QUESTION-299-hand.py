#!/usr/bin/env python3
"""UVA 299 手打版。

用氣泡排序計算最少相鄰交換次數。
"""

import sys


def bubble_swap_count(arr: list[int]) -> int:
    """回傳把 arr 排成遞增所需的相鄰交換次數。"""
    a = arr[:]  # 保留原資料，操作複本
    n = len(a)
    swaps = 0

    for i in range(n):
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1

    return swaps


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    t = int(data[idx])
    idx += 1

    answer: list[str] = []

    for _ in range(t):
        length = int(data[idx])
        idx += 1

        train = list(map(int, data[idx : idx + length]))
        idx += length

        swaps = bubble_swap_count(train)
        answer.append(f"Optimal train swapping takes {swaps} swaps.")

    sys.stdout.write("\n".join(answer))


if __name__ == "__main__":
    main()
