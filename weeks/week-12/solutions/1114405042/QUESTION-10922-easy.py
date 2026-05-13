"""UVA 10922 — 2 the 9s 的簡單記憶版。

核心邏輯：
1. 簡化函式數量，一個函式處理全部檢查與計數。
2. 直接用 % 9 檢查倍數關係。
3. 不用分離 digit_sum，直接在迴圈內計算。

這樣比較好記：加總 → 檢查是否 9 的倍數 → 不是就輸出 impossible → 是就計數加總過程。
"""

from __future__ import annotations

import sys


def solve(num_str: str) -> str:
    """處理單筆測資，直接回傳輸出字串。"""

    # 計算初始的各位數字和
    total = sum(int(c) for c in num_str if c.isdigit())

    # 不是 9 的倍數，直接無解
    if total % 9 != 0:
        return f"{num_str} is not a multiple of 9."

    # 計算深度：反覆加總直到個位數
    depth = 0
    while total >= 10:
        total = sum(int(c) for c in str(total))
        depth += 1

    return f"9-degree of {num_str} is {depth + 1}."


def main() -> None:
    """讀取輸入、逐行計算、逐行輸出。"""

    while True:
        line = sys.stdin.readline().strip()
        if not line or line == "0":
            break
        print(solve(line))


if __name__ == "__main__":
    main()
