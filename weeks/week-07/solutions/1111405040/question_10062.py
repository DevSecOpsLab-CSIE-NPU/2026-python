"""
UVA 10062: Tell me the frequencies!
"""

from __future__ import annotations

from collections import Counter
import sys


def frequency_pairs(line: str) -> list[tuple[int, int]]:
    """統計每個字元的 ASCII 與出現次數。"""
    counts = Counter(ord(char) for char in line)
    return sorted(counts.items(), key=lambda item: (item[1], -item[0]))


def solve(text: str) -> str:
    """依題目規則輸出每一行的 ASCII 頻率表。"""
    blocks: list[str] = []

    for line in text.splitlines():
        pairs = frequency_pairs(line)
        block = "\n".join(f"{ascii_code} {count}" for ascii_code, count in pairs)
        blocks.append(block)

    return "\n\n".join(blocks)


def main() -> None:
    data = sys.stdin.read()
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()
