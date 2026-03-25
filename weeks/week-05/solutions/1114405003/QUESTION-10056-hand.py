"""
UVA 10056 手打版
口訣：先中獎機率 * 等比級數
"""

from __future__ import annotations


def solve(data: str) -> str:
    a = data.split()
    if not a:
        return ""

    t = int(a[0])
    p = 1
    out = []

    for _ in range(t):
        n = int(a[p])
        p += 1
        prob = float(a[p])
        p += 1
        i = int(a[p])
        p += 1

        if prob == 0.0:
            ans = 0.0
        else:
            first = ((1.0 - prob) ** (i - 1)) * prob
            q = (1.0 - prob) ** n
            ans = first / (1.0 - q)

        out.append(f"{ans:.4f}")

    return "\n".join(out)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()))
