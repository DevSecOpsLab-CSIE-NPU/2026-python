"""
UVA 10019 - 士兵數目差（easy 版）

簡單記法：
  兩個數相減取絕對值就是答案。
  Python 的 abs() 內建函式直接搞定，不需要自己判斷大小。

核心概念：
  abs(a - b)
    ↑
    不管 a、b 誰大誰小，abs() 都會回傳正數

輸入處理：
  讀到 EOF 為止，每列讀兩個整數，計算並印出差值。
  Python 大整數：直接支援超過 2^63 的數，完全不必擔心溢位。
"""

from __future__ import annotations

import sys


def diff(a: int, b: int) -> int:
    """
    回傳兩數的絕對差。

    :param a: 第一個整數
    :param b: 第二個整數
    :return:  |a - b|

    為何用 abs()：
      - 若 a > b：abs(a - b) = a - b（正數）
      - 若 a < b：abs(a - b) = b - a（正數）
      - 若 a = b：abs(a - b) = 0
      → 三種情況都正確，一行搞定
    """
    return abs(a - b)


def main() -> None:
    """
    讀取每列兩個整數，輸出其絕對差。
    遇到 EOF（檔案結尾）自動停止。
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # 把一列文字拆成兩個整數
        a, b = map(int, line.split())
        # 印出絕對差
        print(diff(a, b))


if __name__ == "__main__":
    main()
