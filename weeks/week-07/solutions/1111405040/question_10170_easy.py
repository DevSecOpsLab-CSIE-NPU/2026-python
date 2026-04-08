"""
UVA 10170: The Hotel with Infinite Rooms（簡單版）
"""

from __future__ import annotations

import sys


def days_from(start: int, end: int) -> int:
    """算出從 start 到 end 這些旅行團一共住了幾天。"""
    amount = end - start + 1
    return amount * (start + end) // 2


def solve(text: str) -> str:
    """用二分搜尋找出第 D 天所在的旅行團。"""
    results: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        s, d = map(int, line.split())
        left = s
        right = s

        while days_from(s, right) < d:
            right *= 2

        while left < right:
            mid = (left + right) // 2
            if days_from(s, mid) >= d:
                right = mid
            else:
                left = mid + 1

        results.append(str(left))

    return "\n".join(results)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
