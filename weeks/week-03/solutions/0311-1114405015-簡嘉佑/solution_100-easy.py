"""
UVA 100 - The 3n + 1 Problem（easy 版）

好記口訣：
  一條線做到底：
  1. 先把區間排正（lo=min, hi=max）
  2. 每個 n 算一次 cycle-length
  3. 取最大值

cycle-length 好記：
  - 碰到 1 就停
  - 奇數走 3n+1
  - 偶數砍一半
  - 每走一步 count + 1
"""

from __future__ import annotations

import sys


def cyc(n: int, memo: dict[int, int]) -> int:
    """回傳 n 的 cycle-length（easy 短函式名）。"""
    if n in memo:
        return memo[n]

    if n % 2:
        nxt = 3 * n + 1
    else:
        nxt = n // 2

    memo[n] = 1 + cyc(nxt, memo)
    return memo[n]


def best(i: int, j: int) -> int:
    """區間最大 cycle-length。"""
    lo, hi = (i, j) if i <= j else (j, i)
    memo = {1: 1}

    ans = 0
    for n in range(lo, hi + 1):
        ans = max(ans, cyc(n, memo))
    return ans


def out(i: int, j: int) -> str:
    """輸出格式：i j max_cycle。"""
    return f"{i} {j} {best(i, j)}"


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        i, j = map(int, line.split())
        print(out(i, j))


if __name__ == "__main__":
    main()
