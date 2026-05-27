# -*- coding: utf-8 -*-
"""
解題模組（可匯入版本）：UVA 11417 — GCD

此檔案提供：
- `gcd_pair_sum(n)`：計算所有 1 ≤ i < j ≤ n 的 gcd(i, j) 總和
- `main()`：從標準輸入讀取多個 N（以 0 結束），印出每個 N 的結果

詳細說明（繁體中文）：

題目說明：給定正整數 N，計算所有不同整數對 (i, j)（1 ≤ i < j ≤ N）
的最大公因數（gcd）總和。輸入多個 N，以 0 結束。

實作策略：
- 由於題目限制 N ≤ 500，直接採用兩層迴圈搭配內建 `math.gcd` 計算即可，
  時間複雜度為 O(N^2)，在此限制下效能足夠且實作簡潔。
- 若 N 更大，可改用數論優化（例如枚舉 d 作為 gcd，計算互質計數），
  但此處為了可讀性與教學目的採取直接方式。

邊界與錯誤處理：
- 輸入行可能包含非數字或多個數字，本實作以 `split()` 取得 token，再嘗試轉 int；
- 當讀到 `0` 時停止處理，不輸出該筆。

範例：
輸入：
10
0
輸出：
67

註：此檔案名稱使用底線（`_`）以便在測試模組中直接匯入。
"""
import sys
import math
from typing import List


def gcd_pair_sum(n: int) -> int:
    """計算並回傳 1 ≤ i < j ≤ n 的 gcd 總和。

    參數:
    - n: 正整數（n >= 2），表示矩陣上限

    回傳:
    - int: 所有 i<j 的 gcd(i,j) 總和
    """
    total = 0
    # 雙層迴圈，對每一對 (i, j) 計算 gcd 並累加
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += math.gcd(i, j)
    return total


def main() -> None:
    """從標準輸入讀取多個 N，並輸出每個 N 的 gcd pair sum。

    處理方式：
    - 使用 `sys.stdin.read().split()` 將所有 token 讀入；
    - 每個 token 嘗試轉成整數，忽略無法轉換的 token；
    - 讀到 0 則結束處理。
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return
    for token in data:
        try:
            n = int(token)
        except ValueError:
            # 若 token 非整數則跳過
            continue
        if n == 0:
            break
        print(gcd_pair_sum(n))


if __name__ == '__main__':
    main()
