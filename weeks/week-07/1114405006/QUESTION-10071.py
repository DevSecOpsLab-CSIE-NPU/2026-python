"""
UVA/ZeroJudge 10071
計算六元組數量：a + b + c + d + e = f，且六個值都來自集合 S（可重複使用）。
"""

from __future__ import annotations

from collections import Counter
import sys


def count_six_tuples(values: list[int]) -> int:
    """回傳符合 a+b+c+d+e=f 的六元組總數。"""
    # 先預算所有 c+d+e 的出現次數，之後可用 O(1) 查表
    sum3 = Counter()
    for c in values:
        for d in values:
            cd = c + d
            for e in values:
                sum3[cd + e] += 1

    total = 0

    # 對每個 f、每個 (a,b)，需要 c+d+e = f-(a+b)
    # 直接累加該和在 sum3 的出現次數即可
    for f in values:
        for a in values:
            for b in values:
                total += sum3.get(f - (a + b), 0)

    return total


def solve(data: list[int]) -> str:
    if not data:
        return ""

    n = data[0]
    values = data[1 : 1 + n]
    return str(count_six_tuples(values))


def main() -> None:
    raw = sys.stdin.read().strip().split()
    nums = list(map(int, raw)) if raw else []
    out = solve(nums)
    if out:
        sys.stdout.write(out)


if __name__ == "__main__":
    main()
