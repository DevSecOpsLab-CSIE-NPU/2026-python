"""
QUESTION-10071-easy
更容易記憶的寫法：
1) 先把三數和 c+d+e 的次數存起來
2) 再枚舉 f、a、b，查詢 f-(a+b) 有幾種 c+d+e
"""

from __future__ import annotations

from collections import Counter
import sys


def solve(tokens: list[int]) -> str:
    if not tokens:
        return ""

    n = tokens[0]
    s = tokens[1 : 1 + n]

    # sum3[x] 代表 x 可以由 (c,d,e) 組成的方式數量
    sum3 = Counter()
    for c in s:
        for d in s:
            for e in s:
                sum3[c + d + e] += 1

    ans = 0

    # 公式：a+b+c+d+e=f
    # 移項得：c+d+e = f-(a+b)
    # 所以固定 f,a,b 後，答案可直接查 sum3
    for f in s:
        for a in s:
            for b in s:
                need = f - (a + b)
                ans += sum3.get(need, 0)

    return str(ans)


def main() -> None:
    text = sys.stdin.read().strip().split()
    nums = list(map(int, text)) if text else []
    out = solve(nums)
    if out:
        print(out)


if __name__ == "__main__":
    main()
