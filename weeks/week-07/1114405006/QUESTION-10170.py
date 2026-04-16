"""
UVA 10170 - The Hotel with Infinite Rooms
給定 S 與 D，找出第 D 天對應的旅行團人數。
"""

from __future__ import annotations

import sys


def days_from_s_to_k(s: int, k: int) -> int:
    """回傳從人數 s 到 k（含）總共覆蓋幾天。"""
    cnt = k - s + 1
    return (s + k) * cnt // 2


def answer_one(s: int, d: int) -> int:
    """找最小 k >= s，使得 sum(s..k) >= d。"""
    lo = s
    hi = s

    # 先倍增上界，保證答案在 [lo, hi]
    while days_from_s_to_k(s, hi) < d:
        hi *= 2

    # 二分搜尋最小可行 k
    while lo < hi:
        mid = (lo + hi) // 2
        if days_from_s_to_k(s, mid) >= d:
            hi = mid
        else:
            lo = mid + 1
    return lo


def solve(text: str) -> str:
    tokens = text.strip().split()
    if not tokens:
        return ""

    vals = list(map(int, tokens))
    out = []
    for i in range(0, len(vals), 2):
        s = vals[i]
        d = vals[i + 1]
        out.append(str(answer_one(s, d)))
    return "\n".join(out)


def main() -> None:
    text = sys.stdin.read()
    out = solve(text)
    if out:
        sys.stdout.write(out)


if __name__ == "__main__":
    main()
