"""題目 10193（easy 版）

由推導得到：
(b-a)(c-a)=a^2+1，令 x=b-a, y=c-a，則 x*y=N。
而 b+c=2a+x+y，所以只要找乘積固定下最小 x+y 的因數配對。

最簡記法：從 sqrt(N) 往下找第一個因數 d，配對是 d 與 N/d。
"""

from __future__ import annotations

import math
import sys


def solve_one(a: int) -> int:
    """計算單一 a 的最小 b+c。"""
    n = a * a + 1
    d = math.isqrt(n)

    while d > 0:
        if n % d == 0:
            other = n // d
            return 2 * a + d + other
        d -= 1

    return 2 * a + n + 1


def solve(raw_input: str) -> str:
    nums = [int(x) for x in raw_input.split()]
    return "\n".join(str(solve_one(a)) for a in nums)


def main() -> None:
    data = sys.stdin.read()
    if not data.strip():
        return
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()
