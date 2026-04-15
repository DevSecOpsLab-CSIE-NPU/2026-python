"""UVA 10190 - Divide, But Not Quite Conquer!（手打版）

手打記憶口訣：
- n、m 都要 > 1。
- 一路看能不能整除 m。
- 每次除完把數字記起來。
- 最後要剛好到 1，才不是 Boring!
"""

from __future__ import annotations

import sys


def one_case(n: int, m: int) -> str:
    """處理單筆 n, m。"""
    if n <= 1 or m <= 1:
        return "Boring!"

    seq = [n]

    while n > 1:
        if n % m != 0:
            return "Boring!"
        n //= m
        seq.append(n)

    return " ".join(str(x) for x in seq)


def solve(data: str) -> str:
    tokens = data.split()
    ans: list[str] = []

    # 輸入是多組，直到 EOF。
    for i in range(0, len(tokens), 2):
        n = int(tokens[i])
        m = int(tokens[i + 1])
        ans.append(one_case(n, m))

    return "\n".join(ans)


def main() -> None:
    raw = sys.stdin.read()
    if not raw.strip():
        return
    sys.stdout.write(solve(raw))


if __name__ == "__main__":
    main()
