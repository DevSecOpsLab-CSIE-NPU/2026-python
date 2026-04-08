"""題目 10071 解法（效率版）。

計算符合 a+b+c+d+e=f 的六元組數量，a..f 皆來自集合 S 且可重複。

做法：
- 先統計所有三元和次數：cnt3[x] = #(a,b,c) 使 a+b+c=x
- 再統計所有二元和次數：cnt2[y] = #(d,e) 使 d+e=y
- 對每個 f in S：
  #(a,b,c,d,e) 使 a+b+c+d+e=f
  = sum_x cnt3[x] * cnt2[f-x]
- 最後把每個 f 的結果加總。
"""

from __future__ import annotations

import sys


def count_six_tuples(values: list[int]) -> int:
    """回傳滿足 a+b+c+d+e=f 的有序六元組總數。"""
    # 範圍：
    # 單值 [-30000, 30000]
    # 二元和 [-60000, 60000]
    # 三元和 [-90000, 90000]
    off2 = 60000
    off3 = 90000
    size2 = 120001
    size3 = 180001

    cnt2 = [0] * size2
    cnt3 = [0] * size3

    # 先枚舉 (d, e) 的所有有序對，建立二元和次數表。
    for a in values:
        for b in values:
            cnt2[a + b + off2] += 1

    # 再枚舉 (a, b, c) 的所有有序三元組，建立三元和次數表。
    for a in values:
        for b in values:
            ab = a + b
            for c in values:
                cnt3[ab + c + off3] += 1

    # 只保留非零三元和，減少後面迴圈次數。
    nz3 = [(i - off3, cnt) for i, cnt in enumerate(cnt3) if cnt]

    total = 0
    for f in values:
        # 固定 f，計算有多少 (s3, s2) 讓 s3+s2=f。
        subtotal = 0
        for s3, c3 in nz3:
            need2 = f - s3
            idx2 = need2 + off2
            if 0 <= idx2 < size2:
                subtotal += c3 * cnt2[idx2]
        total += subtotal

    return total


def main() -> None:
    # 輸入：第 1 個數為 N，後面 N 個整數為集合元素。
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    values = data[1 : 1 + n]
    print(count_six_tuples(values))


if __name__ == "__main__":
    main()
