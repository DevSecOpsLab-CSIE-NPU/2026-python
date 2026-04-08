"""UVA 10170（easy 版，容易背）。

公式記法：
- 第 k 團住 k 天
- 從 S 開始累加，找到第一個讓天數總和 >= D 的團號
"""

from __future__ import annotations

import math
import sys


def solve_one(s: int, d: int) -> int:
    """單筆查詢：回傳第 d 天入住團的人數。"""
    # 累積到 n 的三角數 T(n) = n(n+1)/2
    # 需求：T(n) - T(s-1) >= d
    target = d + (s - 1) * s // 2

    # 先用反解估 n，再做微調。
    # 這裡用 isqrt 可避免浮點誤差。
    n = (math.isqrt(1 + 8 * target) - 1) // 2
    if n < s:
        n = s
    while n * (n + 1) // 2 < target:
        n += 1
    return n


def main() -> None:
    # 逐行讀取直到 EOF，每行輸出對應答案。
    ans = []
    for line in sys.stdin.buffer.read().splitlines():
        if not line.strip():
            continue
        s, d = map(int, line.split())
        ans.append(str(solve_one(s, d)))
    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    main()
