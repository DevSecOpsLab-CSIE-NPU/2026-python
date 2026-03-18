from __future__ import annotations

import sys


def _carry_count(a: int, b: int) -> int:
    """計算 a + b 的直式加法進位次數。"""
    carry = 0
    total = 0

    while a > 0 or b > 0:
        s = (a % 10) + (b % 10) + carry
        if s >= 10:
            total += 1
            carry = 1
        else:
            carry = 0

        a //= 10
        b //= 10

    return total


def solve(data: str) -> str:
    """
    UVA 10035 手打版

    讀到 0 0 為止，逐筆輸出進位描述字串。
    """
    tokens = data.split()
    out: list[str] = []

    i = 0
    while i + 1 < len(tokens):
        a = int(tokens[i])
        b = int(tokens[i + 1])
        i += 2

        if a == 0 and b == 0:
            break

        c = _carry_count(a, b)
        if c == 0:
            out.append("No carry operation.")
        elif c == 1:
            out.append("1 carry operation.")
        else:
            out.append(f"{c} carry operations.")

    return "\n".join(out)


def main() -> None:
    text = sys.stdin.read()
    sys.stdout.write(solve(text))


if __name__ == "__main__":
    main()
