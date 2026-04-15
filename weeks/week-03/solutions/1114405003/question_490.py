from __future__ import annotations

import sys


def solve(input_text: str) -> str:
    lines = input_text.splitlines()
    if not lines:
        return ""

    width = max(len(line) for line in lines)
    height = len(lines)
    matrix = [line.ljust(width) for line in lines]

    rotated: list[str] = []
    for col in range(width):
        rotated.append("".join(matrix[row][col] for row in range(height - 1, -1, -1)))

    return "\n".join(rotated)


def main() -> None:
    output = solve(sys.stdin.read())
    if output:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()