# -*- coding: utf-8 -*-
"""
解題模組：UVA 11417 — GCD

功能：
- `gcd_pair_sum(n)`：計算所有 1 ≤ i < j ≤ n 的 gcd(i,j) 總和
- `main()`：從 stdin 讀取多個 N（以 0 結束），輸出每個 N 的結果

說明（繁體中文註解）：
- 由於題目限制 n ≤ 500，直接雙層迴圈搭配 Python 的 `math.gcd` 即可在可接受時間內完成。
- 若需進一步最佳化，可使用數論技巧（以 gcd 為基底的計數方法），但為了簡潔與可讀性，採用直接計算法。
"""
from typing import List
import sys
import math


def gcd_pair_sum(n: int) -> int:
    """計算所有 1 ≤ i < j ≤ n 的 gcd(i, j) 總和。

    參數：
    - n: 正整數，n >= 2

    回傳：
    - 整數，表示所有 i<j 的 gcd 之和

    實作說明：直接兩層迴圈計算 gcd(i,j)，時間複雜度 O(n^2)，對 n ≤ 500 足夠。
    """
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += math.gcd(i, j)
    return total


def main() -> None:
    """讀取 stdin，每行一個 N，0 為結束（不處理）。輸出每個 N 的 gcd pair sum。"""
    data = sys.stdin.read().strip().split()
    if not data:
        return
    for token in data:
        try:
            n = int(token)
        except ValueError:
            continue
        if n == 0:
            break
        print(gcd_pair_sum(n))


if __name__ == '__main__':
    main()
