"""任務二: 線性搜尋與二元搜尋。

binary_search 的規則:
- 呼叫端需自行保證 data 已遞增排序。
- 若 data 未排序, 回傳值不保證正確(未定義行為)。
"""

from __future__ import annotations

from typing import Any


def linear_search(data: list[Any], target: Any) -> int:
    """逐一比對 target, 找到回傳 index, 找不到回傳 -1。"""
    for idx, value in enumerate(data):
        if value == target:
            return idx
    return -1


def binary_search(data: list[Any], target: Any) -> int:
    """在已排序資料中做二元搜尋。

    呼叫端必須保證 data 已遞增排序;
    若未排序, 回傳值不保證正確。
    """
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = data[mid]

        if mid_value == target:
            return mid
        if mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
