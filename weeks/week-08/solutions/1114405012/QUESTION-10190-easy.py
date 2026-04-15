"""UVA 10190 - Divide, But Not Quite Conquer!（easy 版）

重點記憶：
1. n、m 都必須 > 1。
2. 一路做 n //= m，每步都要整除。
3. 最後一定要剛好到 1，否則就是 Boring!
"""

from __future__ import annotations

import sys


def one_case_easy(n: int, m: int) -> str:
    """回傳單筆輸出字串。"""
    if n <= 1 or m <= 1:
        return "Boring!"

    seq = [n]

    while n > 1:
        if n % m != 0:
            return "Boring!"
        n //= m
        seq.append(n)

    return " ".join(str(x) for x in seq)


def solve(raw_input: str) -> str:
    tokens = raw_input.split()
    out = []

    for i in range(0, len(tokens), 2):
        n = int(tokens[i])
        m = int(tokens[i + 1])
        out.append(one_case_easy(n, m))

    return "\n".join(out)


def main() -> None:
    data = sys.stdin.read()
    if not data.strip():
        return
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()
