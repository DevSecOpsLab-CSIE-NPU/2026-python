from __future__ import annotations

import sys


def _is_jolly(arr: list[int]) -> bool:
    """判斷序列是否為 Jolly Jumper。"""
    n = len(arr)
    if n <= 1:
        return True

    diff = set()
    for i in range(1, n):
        diff.add(abs(arr[i] - arr[i - 1]))

    return diff == set(range(1, n))


def solve(data: str) -> str:
    """
    UVA 10038 手打版

    每組資料格式：n 後面接 n 個整數。
    """
    tokens = data.split()
    idx = 0
    out: list[str] = []

    while idx < len(tokens):
        n = int(tokens[idx])
        idx += 1

        if idx + n > len(tokens):
            break

        arr = [int(tokens[idx + i]) for i in range(n)]
        idx += n

        out.append("Jolly" if _is_jolly(arr) else "Not jolly")

    return "\n".join(out)


def main() -> None:
    text = sys.stdin.read()
    sys.stdout.write(solve(text))


if __name__ == "__main__":
    main()
