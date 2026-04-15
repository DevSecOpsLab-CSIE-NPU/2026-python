"""
UVA 490 - Rotating Sentences (manual version)

Rotate a block of text 90 degrees clockwise.
The last input line becomes the leftmost output column.
The first input line becomes the rightmost output column.
Short lines are padded with spaces on the right to form a rectangle.
"""

from __future__ import annotations

import sys


def rot(lines: list[str]) -> list[str]:
    if not lines:
        return []

    max_len = max(len(l) for l in lines)
    padded = [l.ljust(max_len) for l in lines]

    result = []
    for col in range(max_len):
        new_line = "".join(padded[row][col] for row in range(len(padded) - 1, -1, -1))
        result.append(new_line)

    return result


def out(lines: list[str]) -> str:
    return "\n".join(lines)


def main() -> None:
    lines = [line.rstrip("\n") for line in sys.stdin]
    if not lines:
        return
    print(out(rot(lines)))


if __name__ == "__main__":
    main()
