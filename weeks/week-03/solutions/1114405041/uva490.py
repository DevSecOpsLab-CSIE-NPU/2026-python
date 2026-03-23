"""UVA 490 - Rotating Sentences."""

import sys


def main() -> None:
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    width = max(len(line) for line in lines)
    padded = [line.ljust(width) for line in lines]

    for col in range(width):
        rotated_row = [padded[row][col] for row in range(len(padded) - 1, -1, -1)]
        print("".join(rotated_row).rstrip())


if __name__ == "__main__":
    main()
