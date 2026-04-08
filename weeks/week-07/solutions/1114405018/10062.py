from __future__ import annotations

import sys
from typing import List


def reconstruct(counts: List[int]) -> List[int]:
    """依題目給的 counts 重建最終排列。"""

    # n 頭牛會對應到 n-1 個 counts 值（從第 2 個位置開始描述）。
    n = len(counts) + 1

    # 先放入編號 1，再依序把 2..n 插入正確位置。
    ans = [1]
    for value in range(2, n + 1):
        # c 表示在目前 value 所在位置之前，比 value 小的元素個數。
        c = counts[value - 2]

        # 目前 ans 長度是 value-1，插入索引為 (value-1-c)。
        idx = value - 1 - c
        ans.insert(idx, value)
    return ans


def _parse_input_text(text: str) -> List[int]:
    """將標準輸入文字轉成 counts 陣列。"""

    nums = [int(x) for x in text.split()]
    if not nums:
        return []

    n = nums[0]
    counts = nums[1:1 + max(0, n - 1)]
    return counts


def solve(data):
    """同時支援列表輸入與整段文字輸入。"""

    if isinstance(data, list):
        return reconstruct(data)

    if isinstance(data, str):
        counts = _parse_input_text(data)
        result = reconstruct(counts)
        return "\n".join(map(str, result))

    raise TypeError("solve expects either counts(list[int]) or input text(str)")


def main() -> None:
    # 腳本模式：讀 stdin，計算後逐行輸出答案。
    text = sys.stdin.read()
    counts = _parse_input_text(text)
    result = reconstruct(counts)
    sys.stdout.write("\n".join(map(str, result)))


if __name__ == "__main__":
    main()
