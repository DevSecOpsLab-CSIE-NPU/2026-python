"""
UVA 11461 — Square Numbers 的簡單版。

做法很直覺：
- 完全平方數的個數 = floor(sqrt(b)) - floor(sqrt(a - 1))
- 每讀一行 a b，就輸出該區間內的平方數個數
- 遇到 0 0 就結束

這版刻意寫得簡短、好記。
"""

import math


def count_squares(a: int, b: int) -> int:
    """計算閉區間 [a, b] 中完全平方數的個數。"""
    return math.isqrt(b) - math.isqrt(a - 1)


def solve() -> None:
    """從標準輸入讀資料並輸出答案。"""
    import sys

    answers = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        answers.append(str(count_squares(a, b)))

    if answers:
        print("\n".join(answers))


if __name__ == "__main__":
    solve()
