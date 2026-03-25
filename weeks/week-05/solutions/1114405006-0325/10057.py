"""
UVA 10057 - A mid-summer night's dream

輸出三個值：
1) 能使總距離最小的最小 A
2) 讓總距離最小的資料筆數
3) 可能的 A 有幾種

核心觀念：
- 要讓 |X1-A| + |X2-A| + ... + |Xn-A| 最小，A 必須落在「中位數區間」。
- 當 n 為奇數時，中位數唯一，所以 A 也唯一。
- 當 n 為偶數時，排序後中間兩個值 low, high 之間的所有整數都可達最小值。
"""

from __future__ import annotations

import sys


def solve(data: str) -> str:
    # 題目是 EOF 多組輸入，先把所有數字一次讀入。
    nums = list(map(int, data.split()))
    out: list[str] = []
    idx = 0

    while idx < len(nums):
        # 每組第一個數字是 n，代表這組資料有 n 個整數。
        n = nums[idx]
        idx += 1

        # 取出這組的 n 個數字。
        arr = nums[idx : idx + n]
        idx += n

        # 先排序，才能拿到中位數（或中位數區間）。
        arr.sort()

        if n % 2 == 1:
            # 奇數：中位數唯一。
            a = arr[n // 2]

            # 第二欄：有多少原始數字落在可行 A 範圍。
            # 奇數時可行範圍只有單一值 a，所以就是統計等於 a 的個數。
            count = sum(1 for x in arr if x == a)

            # 第三欄：可能的 A 只有一種。
            ways = 1
        else:
            # 偶數：中間兩個值組成可行區間 [low, high]。
            low = arr[n // 2 - 1]
            high = arr[n // 2]

            # 題目要求輸出第一欄為最小可行 A。
            a = low

            # 第二欄：有多少 Xi 會落在 [low, high]。
            # 這些值都可作為「最小總距離」的代表元素統計。
            count = sum(1 for x in arr if low <= x <= high)

            # 第三欄：可行 A 的整數個數。
            ways = high - low + 1

        out.append(f"{a} {count} {ways}")

    return "\n".join(out)


def main() -> None:
    result = solve(sys.stdin.read())
    if result:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()
