"""
UVA 10019 - Hashmat the Brave Warrior (manual version)

Problem summary:
  Given two integers representing soldier counts (order may vary),
  output their absolute difference.
  Numbers can be as large as 2^63; Python handles big integers natively.
"""

from __future__ import annotations

import sys


def soldier_diff(a: int, b: int) -> int:
    return abs(a - b)


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        print(soldier_diff(a, b))


if __name__ == "__main__":
    main()
