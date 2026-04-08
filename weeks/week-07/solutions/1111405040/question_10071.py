"""
UVA 10071: Back to High School Physics
"""

from __future__ import annotations

import sys


def compute_displacement(velocity: int, time: int) -> int:
    """根據 s = v * 2t 計算位移。"""
    return 2 * velocity * time


def solve(text: str) -> str:
    """處理多筆輸入直到 EOF。"""
    answers: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        velocity, time = map(int, line.split())
        answers.append(str(compute_displacement(velocity, time)))

    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
