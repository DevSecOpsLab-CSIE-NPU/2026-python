"""
UVA 10062: Tell me the frequencies!（簡單版）
"""

from __future__ import annotations

import sys


def solve(text: str) -> str:
    """逐行計算頻率，並依題目要求排序輸出。"""
    answers: list[str] = []

    for line in text.splitlines():
        counts = [0] * 128

        for char in line:
            counts[ord(char)] += 1

        pairs: list[tuple[int, int]] = []
        for ascii_code in range(128):
            if counts[ascii_code] > 0:
                pairs.append((ascii_code, counts[ascii_code]))

        pairs.sort(key=lambda item: (item[1], -item[0]))
        answers.append("\n".join(f"{ascii_code} {count}" for ascii_code, count in pairs))

    return "\n\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
