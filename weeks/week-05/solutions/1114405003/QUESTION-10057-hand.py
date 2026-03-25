"""
UVA 10057 手打版
口訣：排序 -> 中間兩個 -> 三個答案
"""

from __future__ import annotations


def solve(data: str) -> str:
    a = list(map(int, data.split()))
    i = 0
    out = []

    while i < len(a):
        n = a[i]
        i += 1
        if n <= 0:
            break

        arr = a[i:i + n]
        i += n
        arr.sort()

        low = arr[(n - 1) // 2]
        high = arr[n // 2]

        cnt = sum(1 for x in arr if low <= x <= high)
        ways = high - low + 1

        out.append(f"{low} {cnt} {ways}")

    return "\n".join(out)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()))
