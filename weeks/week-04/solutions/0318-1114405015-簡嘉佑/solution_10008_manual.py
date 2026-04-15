"""
UVA 10008 - Vito's Family (Letter Frequency Count) - manual version

Problem summary:
  Read N lines of text, count occurrences of each letter A-Z.
  - Case insensitive (a and A are the same).
  - Output only letters that appear at least once.
  - Sort by count descending; break ties by alphabetical order ascending.
"""

from __future__ import annotations

import sys


def count_letters(lines: list[str]) -> list[tuple[str, int]]:
    counts: dict[str, int] = {}
    for line in lines:
        for ch in line.upper():
            if "A" <= ch <= "Z":
                counts[ch] = counts.get(ch, 0) + 1
    result = list(counts.items())
    result.sort(key=lambda x: (-x[1], x[0]))
    return result


def main() -> None:
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    lines = data[1: n + 1]
    for letter, cnt in count_letters(lines):
        print(f"{letter} {cnt}")


if __name__ == "__main__":
    main()
