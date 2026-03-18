from __future__ import annotations

import sys


def _is_jolly(sequence: list[int]) -> bool:
    """判斷整數序列是否為 Jolly Jumper。"""
    n = len(sequence)
    if n <= 1:
        return True

    differences = {abs(sequence[i] - sequence[i - 1]) for i in range(1, n)}
    return differences == set(range(1, n))


def solve(data: str) -> str:
    """
    UVA 10038 - Jolly Jumpers
    每筆資料格式為：n 後面接 n 個整數。
    """
    tokens = data.split()
    idx = 0
    outputs: list[str] = []

    while idx < len(tokens):
        n = int(tokens[idx])
        idx += 1

        if idx + n > len(tokens):
            break

        sequence = [int(tokens[idx + i]) for i in range(n)]
        idx += n

        outputs.append("Jolly" if _is_jolly(sequence) else "Not jolly")

    return "\n".join(outputs)


def main() -> None:
    raw_input = sys.stdin.read()
    sys.stdout.write(solve(raw_input))


if __name__ == "__main__":
    main()
