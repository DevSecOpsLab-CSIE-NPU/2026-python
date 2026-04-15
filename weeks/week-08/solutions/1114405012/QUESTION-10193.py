"""題目 10193（依題述：arctan 分解）

由公式可化為：
  (b - a)(c - a) = a^2 + 1
令 x = b-a, y = c-a，則 x*y = a^2+1 且
  b + c = 2a + x + y
要讓 b+c 最小，就是讓 x+y 最小（乘積固定）。
因此找最接近 sqrt(a^2+1) 的因數配對即可。
"""

from __future__ import annotations

import math
import sys


def min_b_plus_c(a: int) -> int:
    """回傳使 arctan(1/a)=arctan(1/b)+arctan(1/c) 的最小 b+c。"""
    n = a * a + 1
    root = math.isqrt(n)

    # 從 sqrt 往下找第一個可整除因數，該配對可使 x+y 最小。
    for x in range(root, 0, -1):
        if n % x == 0:
            y = n // x
            return 2 * a + x + y

    # 理論上不會到這裡（至少 x=1 一定可整除）。
    return 2 * a + 1 + n


def solve(raw_input: str) -> str:
    tokens = raw_input.split()
    answers = [str(min_b_plus_c(int(tok))) for tok in tokens]
    return "\n".join(answers)


def main() -> None:
    data = sys.stdin.read()
    if not data.strip():
        return
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()
