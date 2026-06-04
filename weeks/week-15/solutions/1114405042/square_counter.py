"""平方數計數（學生解答目錄）

提供 `count_squares(a, b)`：回傳區間 [a, b]（含）內完全平方數的個數。

例外：若 a > b，會丟出 ValueError("a must be <= b")。

實作說明：使用 `math.isqrt` 以 O(1) 時間計算上下界的平方根整數數量差，適合大範圍上限。
"""
from __future__ import annotations

from math import isqrt


def count_squares(a: int, b: int) -> int:
    """回傳區間 [a, b] 內完全平方數的個數。

    參數:
    - a, b: 正整數（條件 1 ≤ a ≤ b ≤ 100000），若 a > b 則拋出 ValueError。

    回傳值:
    - int: 區間內完全平方數的個數。
    """
    if a > b:
        raise ValueError("a must be <= b")

    # isqrt(x) 回傳不大於 sqrt(x) 的最大整數
    # 區間內的完全平方數個數 = isqrt(b) - isqrt(a-1)
    lower = a - 1
    if lower < 0:
        lower = 0
    return isqrt(b) - isqrt(lower)


__all__ = ["count_squares"]
