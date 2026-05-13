"""UVA 10931 — Parity 的手打版。

這份版本保留最明確的變數名稱與逐步的判斷邏輯，
看起來比較像人工一步一步思考、逐步寫出來的程式。
"""

from __future__ import annotations

import sys


def main() -> None:
    """主程式：逐行讀取整數並計算其二進位表示中 1 的個數。"""

    while True:
        input_line = sys.stdin.readline().strip()

        # 讀到空行就停止
        if not input_line:
            break

        input_integer = int(input_line)

        # 碰到 0 就停止
        if input_integer == 0:
            break

        # 把整數轉成二進位字符串
        # bin() 會回傳 '0b...' 的形式，所以要去掉前面的 '0b'
        binary_string = bin(input_integer)[2:]

        # 計算二進位中 '1' 的個數
        count_of_ones = 0
        for each_bit in binary_string:
            if each_bit == "1":
                count_of_ones += 1

        # 按照題目格式輸出
        print(f"The parity of {binary_string} is {count_of_ones} (mod 2).")


if __name__ == "__main__":
    main()
