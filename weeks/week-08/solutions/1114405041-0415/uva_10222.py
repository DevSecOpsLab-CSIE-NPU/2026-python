from __future__ import annotations

import sys


ROWS = [
    "`1234567890-=",
    "qwertyuiop[]\\",
    "asdfghjkl;'",
    "zxcvbnm,./",
]

TRANSLATION = {}
for row in ROWS + [row.upper() for row in ROWS]:
    for index in range(1, len(row)):
        TRANSLATION[row[index]] = row[index - 1]


def solve(data: str) -> str:
    decoded_lines = []
    for line in data.splitlines():
        decoded = "".join(TRANSLATION.get(char, char) for char in line)
        decoded_lines.append(decoded)
    return "\n".join(decoded_lines)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
