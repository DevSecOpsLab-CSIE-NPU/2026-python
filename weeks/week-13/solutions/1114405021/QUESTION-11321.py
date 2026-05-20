"""UVA 11321 - Sort! Sort!! and Sort!!!"""

from __future__ import annotations

import sys


def sort_key(value: int, modulo: int) -> tuple[int, int, int]:
    remainder = value % modulo
    is_even = abs(value) % 2 == 0
    if is_even:
        return (remainder, 1, value)
    return (remainder, 0, -value)


def solve() -> None:
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    if not tokens:
        return

    index = 0
    output: list[str] = []

    while index + 1 < len(tokens):
        count = tokens[index]
        modulo = tokens[index + 1]
        index += 2

        if count == 0 and modulo == 0:
            break

        numbers = tokens[index:index + count]
        index += count

        numbers.sort(key=lambda value: sort_key(value, modulo))

        output.append(f"{count} {modulo}")
        output.append(" ".join(map(str, numbers)))

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()