"""UVA 11461 - Square Numbers.

區間 [a, b] 中完全平方數的個數，可以直接用：
floor(sqrt(b)) - floor(sqrt(a-1))

因為題目只問個數，所以不需要真的列出所有平方數。
"""

from __future__ import annotations

import math
import sys


def solve() -> None:
    out_lines: list[str] = []
    for line in sys.stdin:
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break

        # 左右邊界各自取平方根的整數部分，再相減即可得到答案。
        count = math.isqrt(b) - math.isqrt(a - 1)
        out_lines.append(str(count))

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()