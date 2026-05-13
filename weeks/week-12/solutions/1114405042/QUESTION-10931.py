"""UVA 10931 — Parity 的標準解法。

題目的核心就是計算一個整數的二進位表示中 1 的個數。

在 Python 中，可以用：
1. `bin(n)[2:]` 取得二進位字符串（去掉 '0b' 前綴）
2. `count('1')` 計算 1 的個數
或者
1. `bin(n).count('1')` 直接計算 1 的個數

題目的「奇偶性」定義就是二進位中 1 的個數，
無論這個數字本身是奇數還是偶數都無所謂。
"""

from __future__ import annotations

import sys


def count_ones_in_binary(num: int) -> int:
    """計算一個整數的二進位表示中 1 的個數。
    
    參數：
        num: 一個非負整數。
    
    回傳：
        二進位中 1 的個數。
    """

    return bin(num).count("1")


def get_binary_representation(num: int) -> str:
    """取得一個整數的二進位表示（不含 '0b' 前綴）。
    
    參數：
        num: 一個非負整數。
    
    回傳：
        二進位字符串。
    """

    return bin(num)[2:]


def main() -> None:
    """程式進入點：讀取整數，逐行輸出結果。"""

    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break

        num = int(line)
        if num == 0:
            break

        binary_str = get_binary_representation(num)
        parity = count_ones_in_binary(num)
        print(f"The parity of {binary_str} is {parity} (mod 2).")


if __name__ == "__main__":
    main()
