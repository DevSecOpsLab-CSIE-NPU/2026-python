# -*- coding: utf-8 -*-
"""
簡易版（-easy）：UVA 11417 — GCD（詳細說明）

這個檔案提供一個極簡單且易記的實作 `gcd_pair_sum_easy(n)`，
使用 Python 的生成式搭配 `math.gcd`，直接對所有 1 ≤ i < j ≤ n 的對
計算 gcd 並求和。

設計說明（繁體中文）：
- 題目：計算所有不同整數對 (i, j) (1 ≤ i < j ≤ n) 的 gcd 總和。
- 直覺做法：依序列舉每一對 (i, j)，計算 gcd 並累加；此方式簡潔易懂，
  對 N ≤ 500 時，時間複雜度 O(N^2) 足以應付。

實作重點：
- 使用生成式 `sum(math.gcd(i, j) for i in range(1, n) for j in range(i+1, n+1))`，
  能以一行表達完整邏輯，方便記憶與教學。
- 若要在更大輸入下最佳化，可改用數論技巧（例如對每個 d 計算
  以 d 為 gcd 的 pair 數量，再乘上 d）；那是進階解法，此處不採用。

時間與空間複雜度：
- 時間：O(N^2)（主要成本為兩層迴圈與 gcd 計算）
- 空間：O(1) 額外空間（生成式會逐一產生值而非一次性建立完整清單）

使用範例：
    >>> gcd_pair_sum_easy(10)
    67

注意事項：
- 若 n < 2，回傳 0（沒有合法的 i<j 對）。

"""
import sys
import math


def gcd_pair_sum_easy(n: int) -> int:
    """最簡潔的 gcd pair sum 實作。

    參數:
    - n: 正整數

    回傳:
    - int: 所有 1 ≤ i < j ≤ n 的 gcd(i,j) 總和
    """
    if n < 2:
        return 0
    # 生成式：逐一計算每個 pair 的 gcd 並相加，語句短且直觀
    return sum(math.gcd(i, j) for i in range(1, n) for j in range(i + 1, n + 1))


def main() -> None:
    """從 stdin 讀取多個整數 token，遇到 0 則停止，輸出每個 n 的結果。"""
    data = sys.stdin.read().strip().split()
    if not data:
        return
    for token in data:
        try:
            n = int(token)
        except ValueError:
            # 遇到非整數 token 則跳過
            continue
        if n == 0:
            break
        print(gcd_pair_sum_easy(n))


if __name__ == '__main__':
    main()
