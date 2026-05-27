# UVA 11417 - GCD
#
# 這是比較簡單、好記的寫法。
#
# 題目要求：
# 對一個 N，計算所有 1 <= i < j <= N 的 gcd(i, j) 總和。
#
# 例如 N = 4 時，要算：
# gcd(1, 2) + gcd(1, 3) + gcd(1, 4)
# + gcd(2, 3) + gcd(2, 4)
# + gcd(3, 4)
#
# 簡單做法：
# 直接用兩層 for 迴圈，把所有 i < j 的組合跑過一次。

from math import gcd


while True:
    n = int(input())

    # 題目規定輸入 0 代表結束。
    if n == 0:
        break

    total = 0

    # i 是第一個數，範圍從 1 到 n - 1。
    for i in range(1, n):
        # j 是第二個數，必須比 i 大，所以從 i + 1 開始。
        for j in range(i + 1, n + 1):
            total += gcd(i, j)

    print(total)
