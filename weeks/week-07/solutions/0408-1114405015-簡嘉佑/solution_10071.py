"""
UVA 10071 六元組計數 - 正式版

題意：
給定整數集合 S，計算滿足下式的六元組數量：
    a + b + c + d + e = f
其中 a,b,c,d,e,f 都可以從 S 中重複選取。

正式版解法（建議提交）：
1. 先列舉所有 a+b+c+d 的和，並統計每個和出現次數。
2. 再列舉 (e, f)，查詢 (f-e) 在前述統計中出現幾次。
3. 把次數累加，即為答案。

時間複雜度：
- 建表 O(N^4)
- 查詢 O(N^2)
總計 O(N^4)
"""

from __future__ import annotations

from collections import Counter
from typing import Dict, List


def count_six_tuples(values: List[int]) -> int:
    """
    計算滿足 a+b+c+d+e=f 的六元組數量。

    參數：
    values: 集合 S 的元素列表（可視為不重複）

    回傳：
    符合條件的六元組總數
    """
    # 以 Counter 記錄所有四元組和出現次數
    sum4_count: Dict[int, int] = Counter()

    for a in values:
        for b in values:
            for c in values:
                for d in values:
                    sum4_count[a + b + c + d] += 1

    # 對每組 (e, f) 累加對應次數
    ans = 0
    for e in values:
        for f in values:
            ans += sum4_count.get(f - e, 0)

    return ans


def solve_from_stdin() -> int:
    """
    從標準輸入讀取資料並輸出答案。

    輸入格式：
    第一行 N
    接著 N 行，每行一個整數
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return 0

    n = int(data[0])
    values = [int(x) for x in data[1:1 + n]]
    result = count_six_tuples(values)
    sys.stdout.write(str(result))
    return result


if __name__ == "__main__":
    solve_from_stdin()
