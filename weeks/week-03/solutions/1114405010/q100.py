"""UVA 100 - 3n + 1"""

import sys


CACHE = {1: 1}


def get_cycle_length(value: int) -> int:
    """以遞迴加快取計算 cycle length。"""
    if value in CACHE:
        return CACHE[value]

    if value % 2 == 0:
        next_value = value // 2
    else:
        next_value = 3 * value + 1

    CACHE[value] = 1 + get_cycle_length(next_value)
    return CACHE[value]


def solve(text: str) -> str:
    result_lines = []
    for raw in text.splitlines():
        raw = raw.strip()
        if not raw:
            continue

        i, j = map(int, raw.split())
        start, end = (i, j) if i <= j else (j, i)

        max_cycle = 0
        for n in range(start, end + 1):
            length = get_cycle_length(n)
            if length > max_cycle:
                max_cycle = length

        result_lines.append(f"{i} {j} {max_cycle}")

    return "\n".join(result_lines)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
