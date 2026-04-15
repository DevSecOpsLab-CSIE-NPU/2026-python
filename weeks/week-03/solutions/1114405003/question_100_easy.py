"""UVA 100 - Collatz sequence, easy version with Chinese comments."""

from __future__ import annotations

import sys


def solve(input_text: str) -> str:
    # 用快取保存已計算過的 cycle length，避免重複運算
    cache = {1: 1}

    def cycle_length(number: int) -> int:
        original = number
        path: list[int] = []

        while number not in cache:
            path.append(number)
            if number % 2 == 0:
                number //= 2
            else:
                number = number * 3 + 1

        length = cache[number]
        for value in reversed(path):
            length += 1
            cache[value] = length

        return cache[original]

    outputs: list[str] = []
    for line in input_text.splitlines():
        line = line.strip()
        if not line:
            continue
        first, second = map(int, line.split())
        low = min(first, second)
        high = max(first, second)
        best = 0
        for value in range(low, high + 1):
            best = max(best, cycle_length(value))
        outputs.append(f"{first} {second} {best}")

    return "\n".join(outputs)


def main() -> None:
    data = sys.stdin.read()
    result = solve(data)
    if result:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()