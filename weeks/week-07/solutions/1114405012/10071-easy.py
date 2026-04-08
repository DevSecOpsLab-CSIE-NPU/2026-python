"""題目 10071 解法（easy 版，步驟直觀）。

目標：計算 a+b+c+d+e=f 的六元組數量。

記憶口訣：
1. 先做兩個表：三元和次數、二元和次數。
2. 再把 f 固定住，去找三元和 + 二元和 = f。
3. 每種和的組合數用乘法累加。

此版以 dict.Counter 風格實作，便於理解。
"""

from __future__ import annotations

from collections import defaultdict
import sys


def solve(values: list[int]) -> int:
    """用字典統計和的次數，再做配對累加。"""
    cnt2: dict[int, int] = defaultdict(int)
    cnt3: dict[int, int] = defaultdict(int)

    # cnt2[s] = d,e 的有序對數量（d+e=s）。
    for d in values:
        for e in values:
            cnt2[d + e] += 1

    # cnt3[s] = a,b,c 的有序三元組數量（a+b+c=s）。
    for a in values:
        for b in values:
            for c in values:
                cnt3[a + b + c] += 1

    # 固定 f，找出所有 s3 使 f-s3 在 cnt2 中有對應次數。
    ans = 0
    for f in values:
        # 需要 s3 + s2 = f。
        for s3, c3 in cnt3.items():
            ans += c3 * cnt2.get(f - s3, 0)

    return ans


def main() -> None:
    # 讀入格式：N + N 個整數。
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    values = data[1 : 1 + n]
    print(solve(values))


if __name__ == "__main__":
    main()
