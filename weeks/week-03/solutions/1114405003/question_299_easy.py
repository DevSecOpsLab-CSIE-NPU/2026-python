"""UVA 299 - Train Swapping, easy version with Chinese comments."""

from __future__ import annotations

import sys


def solve(input_text: str) -> str:
    lines = [line.strip() for line in input_text.splitlines() if line.strip()]
    if not lines:
        return ""

    # 第一行是測資數量，之後每組測資有長度和車廂序列
    test_count = int(lines[0])
    index = 1
    outputs: list[str] = []

    for _ in range(test_count):
        length = int(lines[index])
        sequence = list(map(int, lines[index + 1].split())) if length else []
        index += 2

        swaps = 0
        for left in range(length):
            for right in range(left + 1, length):
                if sequence[left] > sequence[right]:
                    swaps += 1

        outputs.append(f"Optimal train swapping takes {swaps} swaps.")

    return "\n".join(outputs)


def main() -> None:
    data = sys.stdin.read()
    result = solve(data)
    if result:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()