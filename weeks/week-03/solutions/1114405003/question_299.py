from __future__ import annotations

import sys


def solve(input_text: str) -> str:
    lines = [line.strip() for line in input_text.splitlines() if line.strip()]
    if not lines:
        return ""

    test_count = int(lines[0])
    index = 1
    results: list[str] = []

    for _ in range(test_count):
        length = int(lines[index])
        sequence = list(map(int, lines[index + 1].split())) if length else []
        index += 2

        swaps = 0
        for left in range(length):
            for right in range(left + 1, length):
                if sequence[left] > sequence[right]:
                    swaps += 1

        results.append(f"Optimal train swapping takes {swaps} swaps.")

    return "\n".join(results)


def main() -> None:
    output = solve(sys.stdin.read())
    if output:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()