"""
UVA 11417 — GCD 的簡單版。

題意很單純：
- 讀入多個 N，直到遇到 0。
- 對每個 N，計算所有 1 <= i < j <= N 的 gcd(i, j) 總和。

這一版用最容易記的暴力法來寫，重點放在可讀性。
"""

import math


def gcd_sum(n: int) -> int:
    """直接枚舉所有成對數字，累加 gcd。"""
    total = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += math.gcd(i, j)
    return total


def solve() -> None:
    """從標準輸入讀值，並輸出每個 N 對應的答案。"""
    import sys

    answers = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break
        answers.append(str(gcd_sum(n)))

    if answers:
        print("\n".join(answers))


if __name__ == "__main__":
    solve()
