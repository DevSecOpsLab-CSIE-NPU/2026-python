"""UVA 10929 — Divisibility by 11 的手打版。

這份版本保留明確的變數名稱與逐步的判斷邏輯，
看起來比較像人工一步一步思考、逐步寫出來的程式。
"""

from __future__ import annotations

import sys


def main() -> None:
    """主程式：逐行讀取數字並判斷是否為 11 的倍數。"""

    while True:
        input_number = sys.stdin.readline().strip()

        # 碰到 0 或空行就停止
        if not input_number or input_number == "0":
            break

        # 初始化奇數位與偶數位的數字和
        sum_of_odd_positions = 0
        sum_of_even_positions = 0

        # 從右到左遍歷每一位數字
        # 個位、百位、萬位... 是奇數位（位置 1, 3, 5, ...）
        # 十位、千位... 是偶數位（位置 2, 4, 6, ...）
        position_from_right = 0
        for each_digit_character in reversed(input_number):
            position_from_right += 1
            digit_value = int(each_digit_character)

            # 根據位置的奇偶性，累積到對應的和
            if position_from_right % 2 == 1:
                sum_of_odd_positions += digit_value
            else:
                sum_of_even_positions += digit_value

        # 計算奇數位與偶數位的差
        difference_of_sums = sum_of_odd_positions - sum_of_even_positions

        # 判斷差是否被 11 整除
        if difference_of_sums % 11 == 0:
            print(f"{input_number} is a multiple of 11.")
        else:
            print(f"{input_number} is not a multiple of 11.")


if __name__ == "__main__":
    main()
