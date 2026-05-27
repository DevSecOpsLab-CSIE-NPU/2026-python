"""
UVA 11417 - GCD

題目重點：
輸入多個 N，對每個 N 計算所有 1 <= i < j <= N 的 gcd(i, j) 總和。
輸入 0 代表結束，不需要輸出。

正式版解法：
因為同一份輸入可能有很多個 N，所以先把 2 到最大 N 的答案預先算好。
如果已經知道 G(n - 1)，那 G(n) 只需要再加上 gcd(1, n) 到 gcd(n - 1, n)。
這樣比每次都重新從頭算快，也方便多筆測資查詢。
"""

import sys
from math import gcd
from typing import List, TextIO


def gcd_sum(n: int) -> int:
    """直接計算單一 n 的 GCD 總和，主要給測試使用。"""
    total = 0

    # i 從 1 到 n - 1。
    for i in range(1, n):
        # j 一定要比 i 大，避免重複計算同一組數字。
        for j in range(i + 1, n + 1):
            total += gcd(i, j)

    return total


def build_gcd_sums(max_n: int) -> List[int]:
    """建立答案表，sums[n] 就是題目要求的 G(n)。"""
    sums = [0] * (max_n + 1)

    for n in range(2, max_n + 1):
        # G(n) = G(n - 1) + gcd(1, n) + gcd(2, n) + ... + gcd(n - 1, n)
        sums[n] = sums[n - 1]

        for i in range(1, n):
            sums[n] += gcd(i, n)

    return sums


def solve(input_stream: TextIO = sys.stdin) -> str:
    """讀取多筆 N，遇到 0 停止，回傳每筆答案。"""
    queries = []

    for token in input_stream.read().split():
        number = int(token)

        # 題目規定 N = 0 是結束符號，後面不需要再處理。
        if number == 0:
            break

        queries.append(number)

    if not queries:
        return ""

    # 只預先算到輸入中最大的 N，避免做多餘計算。
    gcd_sums = build_gcd_sums(max(queries))

    return "\n".join(str(gcd_sums[number]) for number in queries)


if __name__ == "__main__":
    print(solve())
