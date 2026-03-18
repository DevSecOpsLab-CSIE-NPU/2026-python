from __future__ import annotations

import sys


def solve(data: str) -> str:
    """
    UVA 10019 手打版

    每筆資料有兩個整數，輸出其差值的絕對值。
    """
    tokens = data.split()
    if len(tokens) < 2:
        return ""

    ans: list[str] = []

    i = 0
    while i + 1 < len(tokens):
        a = int(tokens[i])
        b = int(tokens[i + 1])
        ans.append(str(abs(a - b)))
        i += 2

    return "\n".join(ans)


def main() -> None:
    text = sys.stdin.read()
    sys.stdout.write(solve(text))


if __name__ == "__main__":
    main()
