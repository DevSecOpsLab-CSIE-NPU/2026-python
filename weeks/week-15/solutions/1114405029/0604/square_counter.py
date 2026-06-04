"""
平方數計數

題目：
count_squares(a, b) 回傳區間 [a, b]
之間（包含端點）的完全平方數個數。

例如：

1~10
完全平方數有：
1、4、9

因此回傳：
3
"""

import math


def count_squares(a: int, b: int) -> int:
    """
    計算區間 [a, b] 中完全平方數的數量

    參數：
        a (int): 區間起點
        b (int): 區間終點

    回傳：
        int: 完全平方數個數

    例外：
        若 a > b
        則丟出 ValueError
    """

    # 題目要求：
    # 若 a > b 必須丟出指定錯誤
    if a > b:
        raise ValueError("a must be <= b")

    # 找到第一個可能的平方根
    start = math.ceil(math.sqrt(a))

    # 找到最後一個可能的平方根
    end = math.floor(math.sqrt(b))

    # 若沒有任何平方數
    if start > end:
        return 0

    # 平方根個數就是完全平方數個數
    return end - start + 1