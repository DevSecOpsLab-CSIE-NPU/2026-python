"""HAND EASY - QUESTION 10008"""

from __future__ import annotations

import sys


def solve(text: str) -> str:
    lines = text.splitlines()
    if not lines:
        return ""

    n = int(lines[0].strip())
    counter: dict[str, int] = {}

    for line in lines[1 : 1 + n]:
        for char in line:
            if char.isalpha():
                letter = char.upper()
                counter[letter] = counter.get(letter, 0) + 1

    items = list(counter.items())
    items.sort(key=lambda item: (-item[1], item[0]))
    return "\n".join(f"{letter} {count}" for letter, count in items)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
