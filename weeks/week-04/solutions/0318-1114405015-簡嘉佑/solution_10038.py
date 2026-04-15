"""
UVA 10038 - Jolly Jumpers（正式版）

題意摘要：
  給定一個長度為 n 的整數序列，若相鄰元素差值的絕對值
  恰好包含 1 到 n-1 的每個整數，則輸出 "Jolly"，否則輸出 "Not jolly"。

解法重點：
  1. 逐一計算相鄰兩數的絕對差。
  2. 差值必須都落在 1..n-1。
  3. 最後差值集合需剛好等於 {1,2,...,n-1}。
"""

from __future__ import annotations

import sys


def is_jolly_sequence(nums: list[int]) -> bool:
    """
    判斷序列是否為 Jolly jumper。

    :param nums: 整數序列
    :return: True 表示 Jolly，False 表示 Not jolly

    判斷條件：
      - n <= 1 時，視為 Jolly（沒有相鄰差值要檢查）。
      - 對每個相鄰差值 d = abs(nums[i] - nums[i+1])：
          1 <= d <= n-1 才合法。
      - 最後差值集合必須完整覆蓋 1..n-1。
    """
    n = len(nums)
    if n <= 1:
        return True

    diffs: set[int] = set()
    for i in range(n - 1):
        d = abs(nums[i] - nums[i + 1])
        if d < 1 or d > n - 1:
            return False
        diffs.add(d)

    return diffs == set(range(1, n))


def judge_line(n: int, nums: list[int]) -> str:
    """
    將單行資料轉成題目要求輸出字串。

    :param n: 序列長度
    :param nums: 序列內容
    :return: "Jolly" 或 "Not jolly"

    若 n 與序列實際長度不符，直接回傳 "Not jolly"。
    """
    if n != len(nums):
        return "Not jolly"
    return "Jolly" if is_jolly_sequence(nums) else "Not jolly"


def main() -> None:
    """逐行讀取輸入並輸出判定結果。"""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = list(map(int, line.split()))
        n = parts[0]
        nums = parts[1:]
        print(judge_line(n, nums))


if __name__ == "__main__":
    main()
