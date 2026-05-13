"""
UVA 10931 - Parity
"""

from __future__ import annotations

import sys


def parity_text(value: int) -> str:
    """回傳二進位表示與 1 的個數。"""
    binary = format(value, "b")
    ones = binary.count("1")
    return f"The parity of {binary} is {ones} (mod 2)."


def solve(data: str) -> str:
    """逐行處理直到遇到 0 為止。"""
    outputs: list[str] = []
    for raw_line in data.splitlines():
        text = raw_line.strip()
        if not text:
            continue
        value = int(text)
        if value == 0:
            break
        outputs.append(parity_text(value))
    return "\n".join(outputs)


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))
