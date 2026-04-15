"""
UVA 10019 - 士兵數目差（正式版）

題意摘要：
  每組測試資料有 2 個整數，代表兩方的士兵數（輸入順序不固定）。
  輸出兩數的絕對差（正整數）。
  數字範圍最大到 2^63，Python 大整數原生支援，不需特別處理。

解法：
  讀取每列兩個整數，輸出 abs(a - b)。
  遇到 EOF 結束輸入。
"""

from __future__ import annotations

import sys


def soldier_diff(a: int, b: int) -> int:
    """
    計算兩個整數的絕對差。

    :param a: 第一個整數（士兵數）
    :param b: 第二個整數（士兵數）
    :return:  |a - b|（永遠為非負整數）
    """
    return abs(a - b)


def main() -> None:
    """讀取標準輸入，每列兩個整數，輸出其絕對差。"""
    for line in sys.stdin:
        line = line.strip()
        if not line:        # 跳過空行
            continue
        a, b = map(int, line.split())
        print(soldier_diff(a, b))


if __name__ == "__main__":
    main()
