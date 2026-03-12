"""
UVA 299 - easy 版本（更好記）

口訣：
- 要算最少相鄰交換次數，其實就是「有幾組前大後小」
- 兩層迴圈掃過去，數到幾組就要換幾次
"""

from __future__ import annotations


def inv_easy(a: list[int]) -> int:
    """回傳反序數（最少交換次數）。"""
    ans = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                ans += 1
    return ans


def solve_all(text: str) -> str:
    """處理整份輸入，回傳整份輸出。"""
    ls = [s.strip() for s in text.splitlines() if s.strip()]
    if not ls:
        return ""

    t = int(ls[0])
    p = 1
    out = []

    for _ in range(t):
        l = int(ls[p])
        p += 1

        arr = []
        if l > 0:
            arr = list(map(int, ls[p].split()))
            p += 1

        out.append(f"Optimal train swapping takes {inv_easy(arr)} swaps.")

    return "\n".join(out)


if __name__ == "__main__":
    import sys

    raw = sys.stdin.read()
    if raw.strip():
        print(solve_all(raw))
