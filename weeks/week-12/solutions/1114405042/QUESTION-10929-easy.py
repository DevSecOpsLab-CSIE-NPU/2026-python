"""UVA 10929 — Divisibility by 11 的簡單記憶版。

核心邏輯簡化：
1. 直接在迴圈內累積奇偶位數字和。
2. 不用分開函式，直接在 main 裡做完全部。
3. 用簡單的位置判斷。

這樣最容易記：從右到左走，奇數位加上、偶數位減掉，最後看結果被 11 整除沒。
"""

from __future__ import annotations

import sys


def main() -> None:
    """讀取輸入、逐行計算、逐行輸出。"""

    while True:
        line = sys.stdin.readline().strip()
        if not line or line == "0":
            break

        odd_sum = 0
        even_sum = 0

        # 從右到左遍歷
        for idx, ch in enumerate(reversed(line)):
            val = int(ch)
            # idx 為 0 代表個位（奇數位），idx 為 1 代表十位（偶數位）
            if idx % 2 == 0:
                odd_sum += val
            else:
                even_sum += val

        # 判斷差是否被 11 整除
        if (odd_sum - even_sum) % 11 == 0:
            print(f"{line} is a multiple of 11.")
        else:
            print(f"{line} is not a multiple of 11.")


if __name__ == "__main__":
    main()
