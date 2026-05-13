"""UVA 10922 — 2 the 9s 的手打版。

這份版本保留明確的變數名稱與逐步判斷邏輯，
看起來比較像人工一步一步思考、逐步寫出來的程式。
"""

from __future__ import annotations

import sys


def main() -> None:
    """主程式：逐行讀取整數並判斷是否為 9 的倍數及其深度。"""

    while True:
        input_number = sys.stdin.readline().strip()

        # 碰到 0 或空行就停止
        if not input_number or input_number == "0":
            break

        # 計算這個數的各位數字總和
        digit_total = sum(int(digit) for digit in input_number if digit.isdigit())

        # 檢查初始的各位和是否能被 9 整除
        if digit_total % 9 != 0:
            print(f"{input_number} is not a multiple of 9.")
            continue

        # 若是 9 的倍數，開始計算需要多少次加總才能得到個位數 9
        counting_steps = 0
        current_sum = digit_total

        while current_sum >= 10:
            # 再次計算各位數字的和
            current_sum = sum(int(digit) for digit in str(current_sum))
            counting_steps += 1

        # 深度 = 初始加總一次 + 之後的加總次數
        nine_degree = counting_steps + 1

        print(f"9-degree of {input_number} is {nine_degree}.")


if __name__ == "__main__":
    main()
