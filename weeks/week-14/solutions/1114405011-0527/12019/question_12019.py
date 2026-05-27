"""UVA 12019 - Doom's Day Algorithm（一般版，繁中註解）"""

from __future__ import annotations

import sys

WEEKDAYS = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]

# 2012 是閏年。
MONTH_DAYS_2012 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def weekday_2012(month: int, day: int) -> str:
    """回傳 2012 年指定日期是星期幾。"""
    days_passed = sum(MONTH_DAYS_2012[: month - 1]) + (day - 1)
    # 2012/01/01 是 Sunday。
    return WEEKDAYS[days_passed % 7]


def solve(data: str) -> str:
    nums = [int(x) for x in data.strip().split() if x.strip()]
    if not nums:
        return ""

    t = nums[0]
    out: list[str] = []
    idx = 1
    for _ in range(t):
        month = nums[idx]
        day = nums[idx + 1]
        idx += 2
        out.append(weekday_2012(month, day))

    return "\n".join(out)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
