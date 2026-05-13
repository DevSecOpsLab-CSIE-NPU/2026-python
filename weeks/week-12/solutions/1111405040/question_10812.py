"""
UVA 10812 - Beat the Spread!
"""

from __future__ import annotations

import sys


def find_scores(total: int, diff: int) -> tuple[int, int] | None:
    """根據總分與分差回推出兩隊分數。"""
    if diff > total:
        return None
    if (total + diff) % 2 != 0:
        return None

    high = (total + diff) // 2
    low = (total - diff) // 2
    if low < 0:
        return None
    return high, low


def solve(data: str) -> str:
    """處理多筆測資並回傳輸出字串。"""
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    cases = int(lines[0])
    outputs: list[str] = []
    for index in range(1, cases + 1):
        total, diff = map(int, lines[index].split())
        result = find_scores(total, diff)
        if result is None:
            outputs.append("impossible")
        else:
            outputs.append(f"{result[0]} {result[1]}")
    return "\n".join(outputs)


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))
