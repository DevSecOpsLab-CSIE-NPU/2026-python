"""UVA 10931 — Parity 的簡單記憶版。

核心邏輯簡化：
1. 用 Python 內建的 bin() 和 count()。
2. 直接在 main 裡做完全部，不用分離函式。
3. 最短最簡單的寫法。

這樣最容易記：整數轉二進位字串，數一下 '1' 的個數，輸出就好。
"""

from __future__ import annotations

import sys


def main() -> None:
    """讀取輸入、逐行計算、逐行輸出。"""

    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break

        num = int(line)
        if num == 0:
            break

        # 取二進位字串（去掉 '0b'）
        binary = bin(num)[2:]

        # 計算 '1' 的個數
        parity = binary.count("1")

        print(f"The parity of {binary} is {parity} (mod 2).")


if __name__ == "__main__":
    main()
