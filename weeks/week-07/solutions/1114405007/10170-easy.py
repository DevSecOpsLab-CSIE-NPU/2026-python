from __future__ import annotations

import sys


def find_group_size(s: int, d: int) -> int:
    """回傳第 d 天住進旅館的人數。

    令 k 表示比起始團多了多少人，
    則前 k+1 個旅行團總共住的天數為：
    (k+1) * (2s + k) / 2
    透過二分搜尋找最小 k 使總天數 >= d。
    """
    left = 0
    right = 2_000_000_000

    while left < right:
        mid = (left + right) // 2
        total_days = (mid + 1) * (2 * s + mid) // 2
        if total_days >= d:
            right = mid
        else:
            left = mid + 1

    return s + left


def solve(data: str) -> str:
    nums = [int(x) for x in data.split()]
    result = []
    for i in range(0, len(nums), 2):
        s = nums[i]
        d = nums[i + 1]
        result.append(str(find_group_size(s, d)))
    return "\n".join(result)


def main() -> None:
    data = sys.stdin.read()
    output = solve(data)
    if output:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
