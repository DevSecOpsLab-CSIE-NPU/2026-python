"""UVA 490 - Rotating Sentences, easy version with Chinese comments."""

from __future__ import annotations

import sys


def solve(input_text: str) -> str:
    # 先把所有輸入行保留下來，再找出最長的那一行當矩形寬度
    lines = input_text.splitlines()
    if not lines:
        return ""

    width = max(len(line) for line in lines)
    height = len(lines)
    matrix = [line.ljust(width) for line in lines]

    # 順時針旋轉 90 度：第 0 欄會變成最後一行的最左邊
    rotated_lines: list[str] = []
    for col in range(width):
        rotated_line = []
        for row in range(height - 1, -1, -1):
            rotated_line.append(matrix[row][col])
        rotated_lines.append("".join(rotated_line))

    return "\n".join(rotated_lines)


def main() -> None:
    data = sys.stdin.read()
    result = solve(data)
    if result:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()