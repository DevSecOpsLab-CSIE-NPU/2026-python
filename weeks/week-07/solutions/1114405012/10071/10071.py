"""UVA/ZeroJudge 10071 解答。

題意（依課程題面）：計算有序六元組 (a,b,c,d,e,f) 的數量，滿足
a + b + c + d + e = f，且每個變數都可從集合 S 中重複選取。

做法：
- 先統計所有有序二元和 (d,e) 的出現次數 cnt2。
- 再統計所有有序三元和 (a,b,c) 的出現次數 cnt3。
- 對每個 f in S，答案累加 sum(cnt3[t] * cnt2[f - t])。

時間大約 O(N^3 + R*|S|)，N<=100 可接受。
"""

from __future__ import annotations

import sys
from typing import List


def solve(input_data: str) -> str:
    nums = [int(x) for x in input_data.split()]
    if not nums:
        return ""

    n = nums[0]
    s = nums[1 : 1 + n]

    if n <= 0:
        return "0"

    min_v = min(s)
    max_v = max(s)

    # pair sum 範圍: [2*min_v, 2*max_v]
    p_lo = 2 * min_v
    p_hi = 2 * max_v
    cnt2 = [0] * (p_hi - p_lo + 1)

    for a in s:
        for b in s:
            cnt2[a + b - p_lo] += 1

    # triple sum 範圍: [3*min_v, 3*max_v]
    t_lo = 3 * min_v
    t_hi = 3 * max_v
    cnt3 = [0] * (t_hi - t_lo + 1)

    for a in s:
        for b in s:
            ab = a + b
            for c in s:
                cnt3[ab + c - t_lo] += 1

    ans = 0
    for f in s:
        # 對每個 triple sum t，找 pair sum = f - t
        for idx_t, c3 in enumerate(cnt3):
            if c3 == 0:
                continue
            t = t_lo + idx_t
            need = f - t
            if p_lo <= need <= p_hi:
                ans += c3 * cnt2[need - p_lo]

    return str(ans)


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        sys.stdout.write(out + "\n")


if __name__ == "__main__":
    main()
