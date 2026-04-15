"""UVA 10190 - Divide, But Not Quite Conquer!

正式版：檢查是否能從 n 持續整除 m 到 1，能則輸出序列，否則輸出 Boring!。
"""

from __future__ import annotations

import sys


def build_sequence(n: int, m: int) -> list[int] | None:
    """若是合法序列回傳數列，否則回傳 None。"""
    if n <= 1 or m <= 1:
        return None

    sequence = [n]
    current = n

    # 每一步都必須可整除且嚴格遞減，最後必須剛好到 1。
    while current > 1:
        if current % m != 0:
            return None
        nxt = current // m
        if nxt >= current:
            return None
        sequence.append(nxt)
        current = nxt

    return sequence


def solve(raw_input: str) -> str:
    tokens = raw_input.split()
    outputs: list[str] = []

    for i in range(0, len(tokens), 2):
        n = int(tokens[i])
        m = int(tokens[i + 1])
        seq = build_sequence(n, m)
        if seq is None:
            outputs.append("Boring!")
        else:
            outputs.append(" ".join(map(str, seq)))

    return "\n".join(outputs)


def main() -> None:
    data = sys.stdin.read()
    if not data.strip():
        return
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()
