from __future__ import annotations

import sys
from collections import defaultdict
from typing import Iterable, List


def count_tuples(nums: Iterable[int]) -> int:
    """計算滿足 a+b+c+d+e=f 的六元組數量（a..f 皆可重複取自 S）。"""

    # 先轉成 list，方便多次迭代使用。
    values = list(nums)
    if not values:
        return 0

    # pair_count[s] = 有多少組「有序」(a, b) 使 a+b=s
    # 有序代表 (x, y) 與 (y, x) 視為不同組合。
    pair_count = defaultdict(int)
    for a in values:
        for b in values:
            pair_count[a + b] += 1

    # triple_count[s] = 有多少組「有序」(c, d, e) 使 c+d+e=s
    triple_count = defaultdict(int)
    for c in values:
        for d in values:
            cd = c + d
            for e in values:
                triple_count[cd + e] += 1

    # 對每個 f，累加 pair_sum + triple_sum = f 的組合數。
    # 等價於把 a+b 與 c+d+e 分組後做匹配：
    # 若 s2 + s3 = f，則可貢獻 pair_count[s2] * triple_count[s3]。
    total = 0
    for f in values:
        for s2, cnt2 in pair_count.items():
            total += cnt2 * triple_count.get(f - s2, 0)

    return total


def _parse_input_text(text: str) -> List[int]:
    """將輸入文字解析為題目的集合 S。"""

    # split() 可同時處理空白與換行。
    data = [int(x) for x in text.split()]
    if not data:
        return []

    # 第一個數字為 N，接著 N 個數字是集合元素。
    n = data[0]
    return data[1:1 + n]


def solve(data):
    """提供測試使用的介面：可接收字串輸入或數列輸入。"""

    if isinstance(data, str):
        nums = _parse_input_text(data)
        return str(count_tuples(nums))

    return count_tuples(data)


def main() -> None:
    """競賽模式入口：讀 stdin，輸出答案。"""

    text = sys.stdin.read()
    nums = _parse_input_text(text)
    print(count_tuples(nums))


if __name__ == "__main__":
    main()
