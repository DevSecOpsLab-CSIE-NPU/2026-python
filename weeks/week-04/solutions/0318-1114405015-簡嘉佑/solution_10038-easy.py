"""
UVA 10038 - Jolly Jumpers（easy 版）

超好記版本：
  - 把每一對相鄰數字的「差的絕對值」蒐集起來。
  - 最後只要比對：差值集合 == {1, 2, ..., n-1}

一句口訣：
  相鄰做差、取絕對、收成集合、比對目標。
"""

from __future__ import annotations

import sys


def is_jolly(nums: list[int]) -> bool:
    """
    easy 判斷函式。

    :param nums: 整數序列
    :return: 是否為 Jolly
    """
    n = len(nums)
    if n <= 1:
        return True

    diffs = {abs(nums[i] - nums[i + 1]) for i in range(n - 1)}
    return diffs == set(range(1, n))


def judge(n: int, nums: list[int]) -> str:
    """回傳題目要求輸出字串。"""
    if n != len(nums):
        return "Not jolly"
    return "Jolly" if is_jolly(nums) else "Not jolly"


def main() -> None:
    """讀入每行資料並輸出 Jolly / Not jolly。"""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        a = list(map(int, line.split()))
        n = a[0]
        nums = a[1:]
        print(judge(n, nums))


if __name__ == "__main__":
    main()
