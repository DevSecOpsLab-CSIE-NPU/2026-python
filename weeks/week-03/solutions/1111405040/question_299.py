"""
UVA 299 - 火車車廂交換次數。
"""

from __future__ import annotations

import sys


def count_swaps(train: list[int]) -> int:
    """
    計算將車廂排序為遞增順序所需的最少相鄰交換次數。

    在只能相鄰交換的條件下，最少交換次數等於反轉數（inversion count）。
    由於題目限制 L <= 50，使用 bubble-sort 風格計數即可通過。
    """
    arr = train[:]
    swaps = 0

    for i in range(len(arr)):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return swaps


def parse_cases(text: str) -> list[list[int]]:
    """將輸入解析為多筆車廂序列。"""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return []

    total = int(lines[0])
    index = 1
    cases: list[list[int]] = []

    for _ in range(total):
        if index >= len(lines):
            break

        length = int(lines[index])
        index += 1

        if length == 0:
            cases.append([])
            continue

        if index >= len(lines):
            cases.append([])
            continue

        values = list(map(int, lines[index].split()))
        index += 1
        cases.append(values[:length])

    return cases


def solve(text: str) -> str:
    """處理所有測資並回傳輸出字串。"""
    outputs = []
    for train in parse_cases(text):
        swaps = count_swaps(train)
        outputs.append(f"Optimal train swapping takes {swaps} swaps.")
    return "\n".join(outputs)


def main() -> None:
    """主程式進入點。"""
    data = sys.stdin.read()
    result = solve(data)
    if result:
        sys.stdout.write(result + "\n")


if __name__ == "__main__":
    main()
