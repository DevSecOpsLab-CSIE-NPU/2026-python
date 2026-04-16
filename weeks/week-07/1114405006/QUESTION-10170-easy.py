"""
QUESTION-10170-easy
最容易記的想法：
找最小的 k，使得 s + (s+1) + ... + k >= d。
"""

from __future__ import annotations

import sys


def total_days(s: int, k: int) -> int:
    # 等差級數和
    n = k - s + 1
    return (s + k) * n // 2


def find_group_size(s: int, d: int) -> int:
    # 1) 先用倍增找到足夠大的右邊界
    l, r = s, s
    while total_days(s, r) < d:
        r *= 2

    # 2) 二分找第一個可行值
    while l < r:
        m = (l + r) // 2
        if total_days(s, m) >= d:
            r = m
        else:
            l = m + 1
    return l


def solve(inp: str) -> str:
    data = inp.strip().split()
    if not data:
        return ""

    nums = list(map(int, data))
    ans = []
    for i in range(0, len(nums), 2):
        s, d = nums[i], nums[i + 1]
        ans.append(str(find_group_size(s, d)))

    return "\n".join(ans)


def main() -> None:
    text = sys.stdin.read()
    out = solve(text)
    if out:
        print(out)


if __name__ == "__main__":
    main()
