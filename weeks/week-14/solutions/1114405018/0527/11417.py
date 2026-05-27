"""UVA 11417 - GCD.

題目要計算 1 到 N 之間所有兩兩組合的 gcd 總和。
因為 N 最大只有 500，所以直接用雙迴圈暴力枚舉就足夠快。
"""

from __future__ import annotations

import math
import sys


def solve() -> None:
    # 逐行讀入所有測資，遇到 0 就結束。
    out_lines: list[str] = []
    for line in sys.stdin:
        n = int(line.strip())
        if n == 0:
            break

        total = 0
        # 只要把所有 i < j 的 gcd 加起來即可。
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                total += math.gcd(i, j)

        out_lines.append(str(total))

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()