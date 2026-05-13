"""UVA 10922 — 2 the 9s 的標準解法。

題目的核心是檢查一個數是否為 9 的倍數，
並計算需要多少次「各位數字加總」才能得到個位數 9。

說起來簡單，實作上要注意：
1. 輸入可能是非常大的整數（位數很多），
   所以一開始讀取時不要轉成 int，直接當字串處理。
2. 對字串的每個字元做加總，這樣可以避免大數轉換。
3. 檢查中間結果是否為 9 的倍數，用 % 9 == 0。
4. 終止條件是當結果變成個位數。

這個演算法其實利用了一個數學性質：
一個數 n 能被 9 整除 <=> n 的各位數字和也能被 9 整除。
"""

from __future__ import annotations

import sys
from typing import Optional


def digit_sum(value: str | int) -> int:
    """計算一個數的各位數字總和。
    
    參數可以是字串或整數，都會被轉成字串來逐位加總。
    """

    s = str(value)
    return sum(int(ch) for ch in s if ch.isdigit())


def calculate_nine_degree(value_str: str) -> Optional[int]:
    """計算 9 的深度（9-degree）。
    
    若輸入的數不是 9 的倍數，回傳 None；
    否則回傳需要幾次加總才能得到個位數 9。
    """

    # 先計算初始的各位數字和
    current = digit_sum(value_str)

    # 若初始和就不是 9 的倍數，直接判定不是
    if current % 9 != 0:
        return None

    degree = 0

    # 反覆加總，直到結果變成個位數
    while current >= 10:
        current = digit_sum(current)
        degree += 1

    # 此時 current 應該是 9（因為 current % 9 == 0 且個位數）
    return degree + 1


def main() -> None:
    """程式進入點：讀取整數，逐行輸出結果。"""

    while True:
        line = sys.stdin.readline().strip()
        if not line or line == "0":
            break

        degree = calculate_nine_degree(line)
        if degree is None:
            print(f"{line} is not a multiple of 9.")
        else:
            print(f"9-degree of {line} is {degree}.")


if __name__ == "__main__":
    main()
