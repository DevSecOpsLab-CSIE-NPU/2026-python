"""
UVA 11461 - Square Numbers

題目重點：
給一個區間 [a, b]，計算裡面有幾個完全平方數。
完全平方數就是可以寫成 k * k 的數，例如 1、4、9、16。
輸入 0 0 代表結束，不需要輸出。

解法想法：
小於等於 b 的完全平方數有 floor(sqrt(b)) 個。
小於 a 的完全平方數有 floor(sqrt(a - 1)) 個。
所以 [a, b] 裡的數量就是：
floor(sqrt(b)) - floor(sqrt(a - 1))

Python 的 math.isqrt(x) 會回傳 floor(sqrt(x))，而且不會有浮點數誤差。
"""

import sys
from math import isqrt
from typing import TextIO


def count_squares(a: int, b: int) -> int:
    """計算閉區間 [a, b] 裡的完全平方數數量。"""
    # isqrt(b)：小於等於 b 的平方數數量。
    # isqrt(a - 1)：小於 a 的平方數數量。
    return isqrt(b) - isqrt(a - 1)


def solve(input_stream: TextIO = sys.stdin) -> str:
    """讀取多組 a b，遇到 0 0 停止，回傳每組答案。"""
    output = []
    tokens = input_stream.read().split()

    # 輸入是兩個數字一組，所以每次 index 加 2。
    for index in range(0, len(tokens), 2):
        a = int(tokens[index])
        b = int(tokens[index + 1])

        # 結束條件：0 0 不輸出答案。
        if a == 0 and b == 0:
            break

        output.append(str(count_squares(a, b)))

    return "\n".join(output)


if __name__ == "__main__":
    print(solve())
