"""
UVA 11461 — Square Numbers（完全平方數）
ZeroJudge d186

功能：計算閉區間 [a, b] 中完全平方數的個數
"""

import math


def count_square_numbers(a, b):
    """
    計算閉區間 [a, b] 中完全平方數的個數

    參數：
        a: int — 區間下界
        b: int — 區間上界

    回傳值：
        int — 完全平方數的個數
    """
    # 第一個 >= a 的完全平方數的平方根
    start = math.isqrt(a)
    if start * start < a:
        start += 1
    # 最後一個 <= b 的完全平方數的平方根
    end = math.isqrt(b)
    return max(0, end - start + 1)


def solve() -> None:
    """讀取標準輸入，每行 a b，直到 a=b=0 結束"""
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        print(count_square_numbers(a, b))


if __name__ == "__main__":
    solve()
