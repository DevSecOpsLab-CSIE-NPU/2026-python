"""題目 10193（arctan 分解，手打版）

推導後可得：
  (b-a)(c-a) = a^2 + 1
令 x=b-a, y=c-a，則 x*y=n（n=a^2+1）。
目標最小 b+c = 2a + x + y。

乘積固定時，x+y 最小會出現在最接近 sqrt(n) 的因數配對。
所以從 isqrt(n) 往下找第一個可整除因數即可。
"""

from __future__ import annotations

import math
import sys


def min_sum_bc(a: int) -> int:
    """回傳最小 b+c。"""
    n = a * a + 1
    d = math.isqrt(n)

    while d >= 1:
        if n % d == 0:
            other = n // d
            return 2 * a + d + other
        d -= 1

    # 理論不會發生，保底寫法。
    return 2 * a + n + 1


def solve(data: str) -> str:
    vals = [int(x) for x in data.split()]
    out = [str(min_sum_bc(a)) for a in vals]
    return "\n".join(out)


def main() -> None:
    raw = sys.stdin.read()
    if not raw.strip():
        return
    sys.stdout.write(solve(raw))


if __name__ == "__main__":
    main()
