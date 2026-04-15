from __future__ import annotations

import sys


def solve(input_text: str) -> str:
    cache = {1: 1}

    def cycle_length(number: int) -> int:
        original = number
        path: list[int] = []
        while number not in cache:
            path.append(number)
            number = number // 2 if number % 2 == 0 else number * 3 + 1
        length = cache[number]
        for value in reversed(path):
            length += 1
            cache[value] = length
        return cache[original]

    results: list[str] = []
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
        results.append(f"{first} {second} {best}")
    return "\n".join(results)


def main() -> None:
    data = sys.stdin.read()
    output = solve(data)
    if output:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()