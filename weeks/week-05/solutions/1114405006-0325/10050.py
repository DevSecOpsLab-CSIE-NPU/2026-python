"""
UVA 10050 - Hartals

解法重點：
1. 逐一模擬每個政黨的罷會日（h 的倍數天）
2. 排除每週週五、週六（不計入工作天損失）
3. 用 set 紀錄罷會日，避免多政黨同日重複計算

輸入格式（每組測資）：
- N：模擬天數
- P：政黨數量
- 接著 P 行（或 P 個數字）為各政黨的罷會參數 h

輸出格式：
- 每組測資輸出一行，表示損失的工作天數
"""

from __future__ import annotations

import sys


def lost_working_days(n: int, hartals: list[int]) -> int:
    """計算前 n 天內，因罷會損失的工作天數。"""
    # 用集合自動去重，避免不同政黨在同一天罷會被重複計算。
    lost_days = set()

    for h in hartals:
        # 罷會發生在 h, 2h, 3h, ...
        day = h
        while day <= n:
            # Day 1 是星期日：
            # day % 7 == 6 代表星期五，day % 7 == 0 代表星期六。
            # 題目規定週五、週六是休假日，不列入工作天損失。
            if day % 7 not in (6, 0):
                lost_days.add(day)
            day += h

    return len(lost_days)


def solve(data: str) -> str:
    # 將整份輸入展平成整數序列，方便用索引指標逐段取值。
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    # 第一個數字是測資組數 T。
    t = nums[0]
    idx = 1
    ans: list[str] = []

    for _ in range(t):
        # 每組先讀 N（天數）
        n = nums[idx]
        idx += 1

        # 再讀 P（政黨數）
        p = nums[idx]
        idx += 1

        # 接著讀取 P 個 hartal 參數
        hs = nums[idx : idx + p]
        idx += p

        ans.append(str(lost_working_days(n, hs)))

    return "\n".join(ans)


def main() -> None:
    output = solve(sys.stdin.read())
    if output:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
