"""
UVA 10170 - Infinite Rooms（easy 版）

簡單記法：
- 累加每天由哪些團入住，等價於累加人數 S, S+1, S+2, ...
- 找到第一個讓累加和 >= D 的人數，就是答案。

這版用 while 迴圈直接做，最容易記。
"""

from __future__ import annotations


def solve(s: int, d: int) -> int:
    """回傳第 d 天入住團的人數（易懂版本）。"""
    people = s
    total_days = 0

    # 每一輪代表「people 人的旅行團住 people 天」
    while True:
        total_days += people
        if total_days >= d:
            return people
        people += 1


def main() -> None:
    import sys

    ans = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        s_str, d_str = line.split()
        ans.append(str(solve(int(s_str), int(d_str))))

    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    main()
