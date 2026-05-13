"""UVA 10929 — Divisibility by 11 的標準解法。

題目的核心判斷技巧：
一個整數 N 被 11 整除 <=> 「奇數位數字之和」與「偶數位數字之和」的差被 11 整除。

這裡的「位」是從右到左計算的（個位是第 1 位、十位是第 2 位、...）。

例如 121：
- 從右到左：位置 1 是 1，位置 2 是 2，位置 3 是 1
- 奇數位（1, 3, ...）：1 + 1 = 2
- 偶數位（2, 4, ...）：2
- 差：2 - 2 = 0，被 11 整除，所以 121 是 11 的倍數。

由於輸入可能最多 1000 位，不能直接轉成整數，必須以字串處理。
"""

from __future__ import annotations

import sys


def is_divisible_by_11(num_str: str) -> bool:
    """判斷一個數（以字串形式）是否為 11 的倍數。
    
    參數：
        num_str: 表示一個正整數的字串，可能超過一般整數的位數限制。
    
    回傳：
        若為 11 的倍數則回傳 True，否則回傳 False。
    """

    odd_sum = 0
    even_sum = 0

    # 從字串的末尾開始往前遍歷（由右到左）
    # 這樣可以正確計算各位在十進制中的位置
    for index, digit_char in enumerate(reversed(num_str)):
        digit_value = int(digit_char)

        # 因為 enumerate 是從 0 開始，所以位置計算為 index + 1
        position = index + 1

        # 奇數位（1, 3, 5, ...）對應 index = 0, 2, 4, ...
        if position % 2 == 1:
            odd_sum += digit_value
        else:
            # 偶數位（2, 4, 6, ...）對應 index = 1, 3, 5, ...
            even_sum += digit_value

    # 檢查差是否被 11 整除
    difference = odd_sum - even_sum
    return difference % 11 == 0


def main() -> None:
    """程式進入點：讀取數字，逐行輸出結果。"""

    while True:
        line = sys.stdin.readline().strip()
        if not line or line == "0":
            break

        if is_divisible_by_11(line):
            print(f"{line} is a multiple of 11.")
        else:
            print(f"{line} is not a multiple of 11.")


if __name__ == "__main__":
    main()
