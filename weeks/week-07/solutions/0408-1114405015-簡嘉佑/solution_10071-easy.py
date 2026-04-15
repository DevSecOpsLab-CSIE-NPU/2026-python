"""
UVA 10071 六元組計數 - easy 版

這個版本追求「好記、好背」：
1. 先把所有 a+b+c+d 都算出來放到 Counter。
2. 再跑 e 和 f，查 Counter[f-e]。

和正式版邏輯一樣，但程式更短更直覺。
"""

from __future__ import annotations

from collections import Counter
from typing import List


def count_six_tuples_easy(values: List[int]) -> int:
    """
    easy 寫法：
    - 四層迴圈做 sum4 統計
    - 兩層迴圈做 (e, f) 查表
    """
    sum4 = Counter()
    for a in values:
        for b in values:
            for c in values:
                for d in values:
                    sum4[a + b + c + d] += 1

    total = 0
    for e in values:
        for f in values:
            total += sum4[f - e]
    return total


def solve_from_stdin_easy() -> int:
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return 0

    n = int(data[0])
    values = [int(x) for x in data[1:1 + n]]
    ans = count_six_tuples_easy(values)
    sys.stdout.write(str(ans))
    return ans


if __name__ == "__main__":
    solve_from_stdin_easy()
